"""Strict v1 snapshot validation and descriptor-confined local input.

No extraction, comparison, export, network or persistent storage is performed.
The Python API preserves supplied data; literal evidence proves quoting, not truth.
"""

from __future__ import annotations

from contextlib import contextmanager
from datetime import date
import json
import math
import os
import re
import stat
from typing import Iterator

MAX_BYTES = 1_048_576
MAX_DEPTH = 16
MAX_RECORDS = 100
MAX_SOURCES = 100
ID_PATTERN = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:-]{0,63}")
DATE_PATTERN = re.compile(r"[0-9]{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])")
TIME_PATTERN = re.compile(r"(?:[01][0-9]|2[0-3]):[0-5][0-9]")
OFFSET_PATTERN = re.compile(r"[+-](?:(?:0[0-9]|1[0-3]):[0-5][0-9]|14:00)")
SNAPSHOT_FIELDS = frozenset(("schema_version", "snapshot_id", "scope", "sources", "records"))
SOURCE_FIELDS = frozenset(("source_id", "source_type", "label", "text", "authority_confirmed_by_user"))
RECORD_FIELDS = frozenset((
    "item_id", "module_id", "title", "due_date", "due_time", "timezone",
    "time_precision", "source_id", "source_excerpt", "explicit_cancellation", "user_confirmed",
))


class ValidationError(Exception):
    """A safe error category and fixed field path, never source contents."""

    def __init__(self, code: str, field_path: str = "$") -> None:
        self.code = code
        self.field_path = field_path
        super().__init__(f"{code} {field_path}")


def _reject_json(_value: object) -> None:
    raise ValidationError("INVALID_SCHEMA")


def _finite_float(token: str) -> float:
    value = float(token)
    if not math.isfinite(value):
        raise ValidationError("INVALID_SCHEMA")
    return value


def _unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in pairs:
        if key in value:
            # Unknown or duplicated keys may themselves contain sensitive text.
            raise ValidationError("INVALID_SCHEMA")
        value[key] = item
    return value


def _text_depth(text: str, field_path: str) -> None:
    """Reject excessive containers before invoking the recursive JSON decoder."""
    depth = 0
    quoted = escaped = False
    for character in text:
        if quoted:
            if escaped:
                escaped = False
            elif character == "\\":
                escaped = True
            elif character == '"':
                quoted = False
        elif character == '"':
            quoted = True
        elif character in "[{":
            depth += 1
            if depth > MAX_DEPTH:
                raise ValidationError("INVALID_SCHEMA", field_path)
        elif character in "]}":
            depth -= 1
    # Bracket/string syntax is deliberately left to json.loads.


def _object_depth(value: object, field_path: str) -> None:
    pending = [(value, 0)]
    while pending:
        current, parent_depth = pending.pop()
        if type(current) not in (dict, list):
            continue
        depth = parent_depth + 1
        if depth > MAX_DEPTH:
            raise ValidationError("INVALID_SCHEMA", field_path)
        children = current.values() if type(current) is dict else current
        pending.extend((child, depth) for child in children)


def decode_snapshot(payload: bytes, field_path: str = "$") -> dict[str, object]:
    """Decode and validate bounded strict UTF-8 JSON; raise safe ValidationError.

    Duplicate keys, BOMs, invalid UTF-8, non-finite constants and depth >16 fail
    before version/structure/semantic validation. Input is never modified/logged.
    """
    if type(payload) is not bytes:
        raise ValidationError("INVALID_SCHEMA", field_path)
    if len(payload) > MAX_BYTES:
        raise ValidationError("INPUT_TOO_LARGE", field_path)
    try:
        text = payload.decode("utf-8", errors="strict")
        if text.startswith("\ufeff"):
            raise ValidationError("INVALID_SCHEMA", field_path)
        _text_depth(text, field_path)
        value = json.loads(text, object_pairs_hook=_unique_object, parse_constant=_reject_json, parse_float=_finite_float)
    except ValidationError as error:
        raise ValidationError(error.code, field_path) from None
    except (UnicodeError, ValueError, RecursionError):
        raise ValidationError("INVALID_SCHEMA", field_path) from None
    return validate_snapshot(value, field_path)


def _exact_object(value: object, fields: frozenset[str], path: str, errors: list[str]) -> bool:
    if type(value) is not dict:
        errors.append(path)
        return False
    if any(key not in fields for key in value):
        # Never include a user-chosen unknown key in a diagnostic path.
        errors.append(path)
    errors.extend(f"{path}.{key}" for key in fields if key not in value)
    return True


def _string(value: object, minimum: int, maximum: int, allow_lines: bool = False) -> bool:
    if type(value) is not str or not minimum <= len(value) <= maximum:
        return False
    allowed = (9, 10, 13) if allow_lines else ()
    return all(not (ord(char) < 32 and ord(char) not in allowed) and ord(char) != 127 for char in value)


def _matches(value: object, pattern: re.Pattern[str]) -> bool:
    return type(value) is str and pattern.fullmatch(value) is not None


def _source_errors(value: object, path: str, errors: list[str]) -> None:
    if not _exact_object(value, SOURCE_FIELDS, path, errors):
        return
    checks = {
        "source_id": _matches(value.get("source_id"), ID_PATTERN),
        "source_type": type(value.get("source_type")) is str and value.get("source_type") in ("text", "notice", "brief", "other"),
        "label": _string(value.get("label"), 1, 200),
        "text": _string(value.get("text"), 1, 16_000, allow_lines=True),
        "authority_confirmed_by_user": value.get("authority_confirmed_by_user") is False,
    }
    errors.extend(f"{path}.{key}" for key, good in checks.items() if not good)


def _record_errors(value: object, path: str, errors: list[str]) -> None:
    if not _exact_object(value, RECORD_FIELDS, path, errors):
        return
    for key in ("module_id", "item_id", "source_id"):
        if not _matches(value.get(key), ID_PATTERN):
            errors.append(f"{path}.{key}")
    if not _string(value.get("title"), 1, 200):
        errors.append(f"{path}.title")
    if not _string(value.get("source_excerpt"), 1, 2000, allow_lines=True):
        errors.append(f"{path}.source_excerpt")
    if type(value.get("explicit_cancellation")) is not bool:
        errors.append(f"{path}.explicit_cancellation")
    if value.get("user_confirmed") is not False:
        errors.append(f"{path}.user_confirmed")
    for key, pattern in (("due_date", DATE_PATTERN), ("due_time", TIME_PATTERN), ("timezone", OFFSET_PATTERN)):
        if value.get(key) is not None and not _matches(value.get(key), pattern):
            errors.append(f"{path}.{key}")
    if value.get("timezone") == "-00:00":
        errors.append(f"{path}.timezone")
    precision = value.get("time_precision")
    if type(precision) is not str or precision not in ("date", "minute", "unknown", "none"):
        errors.append(f"{path}.time_precision")
    if value.get("explicit_cancellation") is True:
        if precision != "none":
            errors.append(f"{path}.time_precision")
        for key in ("due_date", "due_time", "timezone"):
            if value.get(key) is not None:
                errors.append(f"{path}.{key}")
    elif value.get("explicit_cancellation") is False and precision == "none":
        errors.append(f"{path}.time_precision")
    if precision == "date":
        if type(value.get("due_date")) is not str:
            errors.append(f"{path}.due_date")
        for key in ("due_time", "timezone"):
            if value.get(key) is not None:
                errors.append(f"{path}.{key}")
    elif precision == "minute":
        for key in ("due_date", "due_time"):
            if type(value.get(key)) is not str:
                errors.append(f"{path}.{key}")
    elif precision == "unknown":
        for key in ("due_date", "due_time", "timezone"):
            if value.get(key) is not None:
                errors.append(f"{path}.{key}")


def validate_snapshot(value: object, field_path: str = "$") -> dict[str, object]:
    """Validate native snapshot structure/semantics without mutation or I/O.

    Returns the supplied dict on success. Call decode_snapshot for byte/JSON
    guarantees. Error priority is version, structure, date, duplicates, source,
    excerpt; within each category the lexicographically first safe path wins.
    """
    _object_depth(value, field_path)
    if type(value) is dict and type(value.get("schema_version")) is str and value.get("schema_version") != "1.0":
        raise ValidationError("UNSUPPORTED_VERSION", f"{field_path}.schema_version")
    errors: list[str] = []
    complete = _exact_object(value, SNAPSHOT_FIELDS, field_path, errors)
    if complete:
        if value.get("schema_version") != "1.0":
            errors.append(f"{field_path}.schema_version")
        if not _matches(value.get("snapshot_id"), ID_PATTERN):
            errors.append(f"{field_path}.snapshot_id")
        if type(value.get("scope")) is not str or value.get("scope") not in ("complete", "partial"):
            errors.append(f"{field_path}.scope")
        for name, maximum, checker in (("sources", MAX_SOURCES, _source_errors), ("records", MAX_RECORDS, _record_errors)):
            items = value.get(name)
            if type(items) is not list or len(items) > maximum:
                errors.append(f"{field_path}.{name}")
                continue
            for index, item in enumerate(items):
                checker(item, f"{field_path}.{name}[{index}]", errors)
    if errors:
        raise ValidationError("INVALID_SCHEMA", min(errors))

    records, sources = value.get("records"), value.get("sources")
    bad_dates = []
    for index, record in enumerate(records):
        if record["due_date"] is not None:
            try:
                date.fromisoformat(record["due_date"])
            except ValueError:
                bad_dates.append(f"{field_path}.records[{index}].due_date")
    if bad_dates:
        raise ValidationError("INVALID_DATE", min(bad_dates))
    duplicate_paths: list[str] = []
    seen_sources: set[str] = set()
    for index, source in enumerate(sources):
        source_id = source["source_id"]
        if source_id in seen_sources:
            duplicate_paths.append(f"{field_path}.sources[{index}].source_id")
        seen_sources.add(source_id)
    seen_records: set[tuple[str, str, str]] = set()
    for index, record in enumerate(records):
        identity = (record["module_id"], record["item_id"], record["source_id"])
        if identity in seen_records:
            duplicate_paths.append(f"{field_path}.records[{index}].source_id")
        seen_records.add(identity)
    if duplicate_paths:
        raise ValidationError("DUPLICATE_IDENTIFIER", min(duplicate_paths))
    unknown_paths = [f"{field_path}.records[{index}].source_id" for index, record in enumerate(records) if record["source_id"] not in seen_sources]
    if unknown_paths:
        raise ValidationError("UNKNOWN_SOURCE", min(unknown_paths))
    source_text = {source["source_id"]: source["text"] for source in sources}
    excerpt_paths = [f"{field_path}.records[{index}].source_excerpt" for index, record in enumerate(records) if record["source_excerpt"] not in source_text[record["source_id"]]]
    if excerpt_paths:
        raise ValidationError("INVALID_EVIDENCE", min(excerpt_paths))
    return value


def _identity(info: os.stat_result) -> tuple[int, int]:
    return info.st_dev, info.st_ino


def _file_revision(info: os.stat_result) -> tuple[int, int, int, int, int]:
    return info.st_dev, info.st_ino, info.st_size, info.st_mtime_ns, info.st_ctime_ns


def _require_descriptor_support(field_path: str) -> None:
    required = ("O_DIRECTORY", "O_NOFOLLOW", "O_NONBLOCK", "O_CLOEXEC")
    if os.name != "posix" or not all(hasattr(os, flag) for flag in required) or os.open not in os.supports_dir_fd or os.stat not in os.supports_dir_fd or os.stat not in os.supports_follow_symlinks:
        raise ValidationError("UNSAFE_PATH", field_path)


def _verify_links(links: list[tuple[int, str, int]], field_path: str) -> None:
    """Verify every open child still occupies its selected parent/name entry."""
    for parent, name, child in links:
        current = os.stat(name, dir_fd=parent, follow_symlinks=False)
        opened = os.fstat(child)
        if stat.S_ISLNK(current.st_mode) or _identity(current) != _identity(opened):
            raise ValidationError("UNSAFE_PATH", field_path)


@contextmanager
def open_workspace(workspace: str) -> Iterator[tuple[int, list[tuple[int, str, int]]]]:
    """Open an explicitly selected POSIX workspace without following symlinks.

    All ancestor descriptors remain open for link-identity checks. Unsupported
    platforms fail closed. This is not a general sandbox against a malicious OS.
    """
    path = "$.workspace"
    _require_descriptor_support(path)
    descriptors: list[int] = []
    try:
        if type(workspace) is not str or not workspace or "\x00" in workspace or "\\" in workspace:
            raise ValidationError("UNSAFE_PATH", path)
        raw_parts = workspace.split("/")
        if ".." in raw_parts or ("." in raw_parts and workspace != "."):
            raise ValidationError("UNSAFE_PATH", path)
        # abspath is lexical; symlink checks happen on every absolute component.
        absolute = os.path.abspath(workspace)
        root = os.open("/", os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC)
        descriptors.append(root)
        links: list[tuple[int, str, int]] = []
        parent = root
        for name in absolute.split("/")[1:]:
            if not name:
                continue
            before = os.stat(name, dir_fd=parent, follow_symlinks=False)
            child = os.open(name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC, dir_fd=parent)
            descriptors.append(child)
            if not stat.S_ISDIR(before.st_mode) or _identity(before) != _identity(os.fstat(child)):
                raise ValidationError("UNSAFE_PATH", path)
            links.append((parent, name, child))
            parent = child
        _verify_links(links, path)
        yield parent, links
    except (OSError, ValueError, NotImplementedError):
        raise ValidationError("UNSAFE_PATH", path) from None
    finally:
        for descriptor in reversed(descriptors):
            os.close(descriptor)


def _relative_components(relative_path: str, field_path: str) -> list[str]:
    if type(relative_path) is not str or not relative_path or "\x00" in relative_path or "\\" in relative_path or relative_path.startswith("/"):
        raise ValidationError("UNSAFE_PATH", field_path)
    parts = relative_path.split("/")
    if any(part in ("", ".", "..") for part in parts) or not parts[-1].endswith(".json"):
        raise ValidationError("UNSAFE_PATH", field_path)
    return parts


def read_snapshot(workspace: tuple[int, list[tuple[int, str, int]]], relative_path: str, field_path: str = "$") -> dict[str, object]:
    """Read only an explicit regular .json file beneath an open workspace.

    Uses descriptor-relative nofollow opens, bounded reads and pre/post identity
    checks. A detected rename, replacement or in-place modification fails closed.
    No path or source value is included in ValidationError diagnostics.
    """
    root, root_links = workspace
    descriptors: list[int] = []
    try:
        parts = _relative_components(relative_path, field_path)
        _verify_links(root_links, field_path)
        links = list(root_links)
        parent = root
        for name in parts[:-1]:
            before = os.stat(name, dir_fd=parent, follow_symlinks=False)
            child = os.open(name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC, dir_fd=parent)
            descriptors.append(child)
            if not stat.S_ISDIR(before.st_mode) or _identity(before) != _identity(os.fstat(child)):
                raise ValidationError("UNSAFE_PATH", field_path)
            links.append((parent, name, child))
            parent = child
        name = parts[-1]
        before = os.stat(name, dir_fd=parent, follow_symlinks=False)
        if not stat.S_ISREG(before.st_mode):
            raise ValidationError("UNSAFE_PATH", field_path)
        descriptor = os.open(name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK | os.O_CLOEXEC, dir_fd=parent)
        descriptors.append(descriptor)
        opened = os.fstat(descriptor)
        if not stat.S_ISREG(opened.st_mode) or _identity(before) != _identity(opened):
            raise ValidationError("UNSAFE_PATH", field_path)
        links.append((parent, name, descriptor))
        if opened.st_size > MAX_BYTES:
            raise ValidationError("INPUT_TOO_LARGE", field_path)
        remaining = MAX_BYTES + 1
        chunks: list[bytes] = []
        while remaining:
            chunk = os.read(descriptor, min(65_536, remaining))
            if not chunk:
                break
            chunks.append(chunk)
            remaining -= len(chunk)
        _verify_links(links, field_path)
        if _file_revision(opened) != _file_revision(os.fstat(descriptor)):
            raise ValidationError("UNSAFE_PATH", field_path)
        payload = b"".join(chunks)
        if len(payload) > MAX_BYTES:
            raise ValidationError("INPUT_TOO_LARGE", field_path)
        return decode_snapshot(payload, field_path)
    except (OSError, ValueError, NotImplementedError):
        raise ValidationError("UNSAFE_PATH", field_path) from None
    finally:
        for descriptor in reversed(descriptors):
            os.close(descriptor)


def load_snapshot(workspace: str, relative_path: str, field_path: str = "$") -> dict[str, object]:
    """Open one explicitly selected workspace/file and return a valid snapshot."""
    with open_workspace(workspace) as opened:
        return read_snapshot(opened, relative_path, field_path)
