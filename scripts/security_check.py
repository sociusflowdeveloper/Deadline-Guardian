#!/usr/bin/env python3
"""Bounded, offline repository checks; heuristic findings never echo contents.

This maintainer tool inspects repository files and optionally reachable local Git
blobs, including bounded ZIP members in memory. It does not scan user workspaces,
contact a network, install dependencies or change repository/platform settings.
Its patterns and AST policy are review aids, not a security certification.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import io
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
import zipfile

MAX_FILE_BYTES = 10 * 1024 * 1024
MAX_TOTAL_BYTES = 100 * 1024 * 1024
MAX_ZIP_FILES = 1000
MAX_OBJECTS = 5000
RUNTIME_PREFIX = 'skills/academic-deadline-drift-guard/scripts/'
RUNTIME_IMPORTS = frozenset((
    '__future__', 'argparse', 'json', 'sys', 'csv', 'html', 'io', 'os',
    'secrets', 'stat', 'contextlib', 'datetime', 'math', 're', 'typing',
    'validator', 'comparator', 'exporter',
))
# Assemble recognisers to avoid embedding credential-shaped examples in source.
SECRET_PATTERNS = (
    ('GITHUB_TOKEN', re.compile(('gh' + '[pousr]_' + '[A-Za-z0-9]{30,}').encode())),
    ('GITHUB_FINE_GRAINED_TOKEN', re.compile(('github_' + 'pat_' + '[A-Za-z0-9_]{40,}').encode())),
    ('AWS_ACCESS_KEY_ID', re.compile(('AK' + 'IA' + '[A-Z0-9]{16}').encode())),
    ('PRIVATE_KEY_HEADER', re.compile(('-----BEGIN ' + '(?:RSA |EC |OPENSSH )?' + 'PRIVATE KEY-----').encode())),
    ('SLACK_TOKEN', re.compile(('xox' + '[baprs]-' + '[A-Za-z0-9-]{20,}').encode())),
    ('SK_STYLE_TOKEN', re.compile(('s' + 'k-' + '[A-Za-z0-9_-]{32,}').encode())),
)


class ScanIncomplete(Exception):
    """A fixed non-sensitive reason why a scan cannot be considered complete."""


def runtime_policy(source: str) -> set[str]:
    """Return conservative AST review categories for application source only."""
    tree = ast.parse(source)
    findings = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports = [name.name.split('.')[0] for name in node.names]
        elif isinstance(node, ast.ImportFrom):
            imports = [(node.module or '').split('.')[0]]
        else:
            imports = []
        if any(name not in RUNTIME_IMPORTS for name in imports):
            findings.add('RUNTIME_IMPORT_REQUIRES_REVIEW')
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id in ('eval', 'exec', 'compile', '__import__', 'open'):
                findings.add('DYNAMIC_EXECUTION_OR_UNCONFINED_OPEN')
        if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name):
            if node.value.id == 'os' and (
                node.attr in ('environ', 'getenv', 'system', 'popen') or
                node.attr.startswith(('exec', 'spawn'))
            ):
                findings.add('ENVIRONMENT_OR_PROCESS_ACCESS')
    return findings


class Scanner:
    """Collect counts/categories only; never return matched text or filenames."""

    def __init__(self):
        self.findings = []
        self.bytes_scanned = 0
        self.payloads_scanned = 0
        self.archive_files_scanned = 0

    def _finding(self, category: str, location: str):
        self.findings.append({
            'category': category,
            'source_id': hashlib.sha256(location.encode('utf-8', errors='replace')).hexdigest()[:16],
        })

    def scan_payload(self, payload: bytes, location: str, archive: bool = True):
        """Inspect bounded bytes/ZIP text without extracting or executing them."""
        if len(payload) > MAX_FILE_BYTES:
            raise ScanIncomplete('FILE_BOUND_EXCEEDED')
        self.bytes_scanned += len(payload)
        if self.bytes_scanned > MAX_TOTAL_BYTES:
            raise ScanIncomplete('TOTAL_BOUND_EXCEEDED')
        self.payloads_scanned += 1
        for category, pattern in SECRET_PATTERNS:
            if pattern.search(payload):
                self._finding(category, location)
        if not payload.startswith(b'PK\x03\x04'):
            return
        if not archive:
            raise ScanIncomplete('NESTED_ARCHIVE_NOT_SCANNED')
        try:
            with zipfile.ZipFile(io.BytesIO(payload)) as zipped:
                members = zipped.infolist()
                if len(members) > MAX_ZIP_FILES or sum(info.file_size for info in members) > MAX_FILE_BYTES:
                    raise ScanIncomplete('ARCHIVE_BOUND_EXCEEDED')
                for index, info in enumerate(members):
                    if info.is_dir():
                        continue
                    if info.file_size > MAX_FILE_BYTES:
                        raise ScanIncomplete('ARCHIVE_MEMBER_BOUND_EXCEEDED')
                    self.archive_files_scanned += 1
                    self.scan_payload(zipped.read(info), f'{location}:member:{index}', archive=False)
        except (OSError, RuntimeError, ValueError, zipfile.BadZipFile):
            raise ScanIncomplete('ARCHIVE_UNREADABLE') from None


def _git(root: Path, *arguments: str) -> bytes:
    """Run fixed local Git inspection commands without a shell/network action."""
    result = subprocess.run(['git', '-C', str(root), *arguments], capture_output=True, timeout=30)
    if result.returncode:
        raise ScanIncomplete('LOCAL_GIT_INSPECTION_FAILED')
    return result.stdout


def scan_repository(root: Path, include_history: bool) -> dict:
    """Scan non-ignored tracked/untracked files and optional available history.

    Locations are hashed to avoid exposing content encoded in a filename. Git
    history is limited to objects reachable in this checkout, which may be
    shallow; unreferenced objects, inaccessible refs and remote settings are not
    inspected. No absence-of-personal-data or comprehensive-secret claim follows.
    """
    if os.name != 'posix' or not all(hasattr(os, flag) for flag in ('O_NOFOLLOW', 'O_NONBLOCK')):
        raise ScanIncomplete('UNSUPPORTED_SCAN_PLATFORM')
    scanner = Scanner()
    files = sorted(set(_git(root, 'ls-files', '-z', '--cached', '--others', '--exclude-standard').split(b'\0')) - {b''})
    for encoded in files:
        relative = os.fsdecode(encoded)
        parts = Path(relative).parts
        if Path(relative).is_absolute() or '..' in parts:
            raise ScanIncomplete('UNSAFE_REPOSITORY_PATH')
        target = root / relative
        # Do not follow a checked-in or untracked symlink into another workspace.
        if any((root.joinpath(*parts[:index])).is_symlink() for index in range(1, len(parts) + 1)):
            raise ScanIncomplete('SYMLINK_REPOSITORY_PATH')
        descriptor = os.open(target, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
        try:
            info = os.fstat(descriptor)
            if not stat.S_ISREG(info.st_mode) or info.st_size > MAX_FILE_BYTES:
                raise ScanIncomplete('UNSUPPORTED_REPOSITORY_FILE')
            chunks = []
            remaining = MAX_FILE_BYTES + 1
            while remaining:
                chunk = os.read(descriptor, min(65536, remaining))
                if not chunk:
                    break
                chunks.append(chunk)
                remaining -= len(chunk)
            payload = b''.join(chunks)
        finally:
            os.close(descriptor)
        scanner.scan_payload(payload, 'current:' + relative)
        if relative.startswith(RUNTIME_PREFIX) and relative.endswith('.py'):
            for category in sorted(runtime_policy(payload.decode('utf-8'))):
                scanner._finding(category, 'current:' + relative)
    history_count = 0
    shallow = _git(root, 'rev-parse', '--is-shallow-repository').strip() == b'true'
    if include_history:
        object_ids = sorted({line.split(b' ', 1)[0] for line in _git(root, 'rev-list', '--objects', '--all').splitlines()})
        if len(object_ids) > MAX_OBJECTS:
            raise ScanIncomplete('HISTORY_OBJECT_BOUND_EXCEEDED')
        for object_id in object_ids:
            if not re.fullmatch(rb'[0-9a-f]{40,64}', object_id):
                raise ScanIncomplete('INVALID_LOCAL_OBJECT_ID')
            sha = object_id.decode('ascii')
            if _git(root, 'cat-file', '-t', sha).strip() != b'blob':
                continue
            size = int(_git(root, 'cat-file', '-s', sha))
            if size > MAX_FILE_BYTES:
                raise ScanIncomplete('HISTORY_BLOB_BOUND_EXCEEDED')
            scanner.scan_payload(_git(root, 'cat-file', 'blob', sha), 'history:' + sha)
            history_count += 1
    return {
        'status': 'FINDINGS_REQUIRE_REVIEW' if scanner.findings else 'CHECKS_PASSED_WITH_LIMITS',
        'current_files_scanned': len(files),
        'history_requested': include_history,
        'history_scope': 'reachable-local-objects-only',
        'shallow_checkout': shallow,
        'history_blobs_scanned': history_count,
        'archive_files_scanned': scanner.archive_files_scanned,
        'payloads_scanned': scanner.payloads_scanned,
        'bytes_scanned': scanner.bytes_scanned,
        'findings': scanner.findings,
        'limitations': [
            'Heuristic credential patterns and conservative runtime AST policy only; manual review is required.',
            'No personal-data clearance, complete secret detection or host prompt-injection guarantee.',
            'Remote settings, inaccessible/unreferenced history and provider controls were not inspected.',
        ],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--history', action='store_true', help='also inspect reachable objects present in this checkout')
    arguments = parser.parse_args(argv)
    root = Path(__file__).resolve().parents[1]
    try:
        result = scan_repository(root, arguments.history)
    except (ScanIncomplete, OSError, ValueError, UnicodeError, SyntaxError, subprocess.SubprocessError) as error:
        code = str(error) if isinstance(error, ScanIncomplete) else 'INSPECTION_ERROR'
        print(json.dumps({'status': 'SCAN_INCOMPLETE', 'reason': code}))
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    return 1 if result['findings'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
