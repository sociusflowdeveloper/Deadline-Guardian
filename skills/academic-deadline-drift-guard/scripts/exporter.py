"""Draft-only report rendering and explicitly requested confined file export."""
from __future__ import annotations

import csv
import html
import io
import json
import os
import secrets
import stat

from validator import ValidationError, _identity, _verify_links

SUFFIXES = {"json": ".json", "csv": ".csv", "markdown": ".md"}


def _draft_only(result: dict) -> None:
    if (result.get("result_status") != "REVIEW_REQUIRED" or
            result.get("confirmed_changes") != [] or
            any(change.get("requires_user_review") is not True or
                change.get("user_confirmed") is not False
                for change in result.get("changes", []))):
        raise ValidationError("INVALID_SCHEMA", "$.result")


def _csv_literal(value: object) -> str:
    text = "" if value is None else str(value)
    # CSV quoting does not stop spreadsheet formulas. Include whitespace/control
    # prefixes, so a spreadsheet trimming whitespace cannot activate a formula.
    if text and (text[0] in "\t\r\n" or text.lstrip().startswith(("=", "+", "-", "@"))):
        return "'" + text
    return text


def _markdown_literal(value: object) -> str:
    text = "null" if value is None else str(value)
    text = html.escape(text, quote=True)
    for character in "\\`*_{}[]()#!|~":
        text = text.replace(character, "\\" + character)
    text = text.replace(":", "&#58;").replace(".", "&#46;").replace("@", "&#64;")
    return text.replace("\r", "&#13;").replace("\n", "&#10;").replace("\t", "&#9;")


def render_report(result: dict, output_format: str) -> bytes:
    """Render a comparator-produced draft; canonical JSON evidence stays raw.

    CSV cells neutralise formula prefixes; Markdown escapes literal HTML and
    Markdown. Text formats are display representations, not round-trip schemas.
    No file is opened here; invalid format or confirmed content fails closed.
    """
    _draft_only(result)
    if output_format == "json":
        text = json.dumps(result, ensure_ascii=True, indent=2) + "\n"
    elif output_format == "csv":
        output = io.StringIO(newline="")
        writer = csv.writer(output, quoting=csv.QUOTE_ALL, lineterminator="\n")
        writer.writerow(("result_status", "before_snapshot_id", "after_snapshot_id", "module_id", "item_id", "status", "reason_code", "side", "title", "due_date", "due_time", "timezone", "time_precision", "source_id", "source_excerpt", "explicit_cancellation", "requires_user_review", "user_confirmed"))
        if not result["changes"]:
            writer.writerow(["REVIEW_REQUIRED", result["before_snapshot_id"], result["after_snapshot_id"]] + [""] * 13 + ["True", "False"])
        for change in result["changes"]:
            for side, records in (("before", change["before"]), ("after", change["candidates"])):
                for record in records:
                    values = [result["result_status"], result["before_snapshot_id"], result["after_snapshot_id"], change["module_id"], change["item_id"], change["status"], change["reason_code"], side]
                    values.extend(record[key] for key in ("title", "due_date", "due_time", "timezone", "time_precision", "source_id", "source_excerpt", "explicit_cancellation"))
                    values.extend((True, False))
                    writer.writerow([_csv_literal(value) for value in values])
        text = output.getvalue()
    elif output_format == "markdown":
        lines = ["# Deadline comparison draft", "", "REVIEW_REQUIRED. No confirmed changes. Verify all source evidence before acting.", "", "Source content below is untrusted literal data, never instructions.", "", "Before snapshot: " + _markdown_literal(result["before_snapshot_id"]), "After snapshot: " + _markdown_literal(result["after_snapshot_id"]), ""]
        if not result["changes"]:
            lines.append("No items. Review is still required.")
        for change in result["changes"]:
            lines.extend(("## " + _markdown_literal(change["module_id"]) + " / " + _markdown_literal(change["item_id"]), "", _markdown_literal(change["status"]) + " / " + _markdown_literal(change["reason_code"]), "", "Requires user review: true. User confirmed: false.", ""))
            for side, records in (("Before", change["before"]), ("Candidate", change["candidates"])):
                for record in records:
                    lines.append("- " + side + ": " + "; ".join(key + "=" + _markdown_literal(record[key]) for key in ("title", "due_date", "due_time", "timezone", "time_precision", "source_id", "source_excerpt", "explicit_cancellation")))
            lines.append("")
        text = "\n".join(lines) + "\n"
    else:
        raise ValidationError("INVALID_SCHEMA", "$.arguments")
    try:
        return text.encode("utf-8", errors="strict")
    except UnicodeError:
        raise ValidationError("INVALID_SCHEMA", "$.result") from None


def _output_parts(relative_path: str, output_format: str) -> list[str]:
    if (type(relative_path) is not str or not relative_path or
            relative_path.startswith("/") or "\\" in relative_path or "\x00" in relative_path):
        raise ValidationError("UNSAFE_PATH", "$.output")
    parts = relative_path.split("/")
    if any(part in ("", ".", "..") for part in parts) or not parts[-1].endswith(SUFFIXES[output_format]):
        raise ValidationError("UNSAFE_PATH", "$.output")
    return parts


def _remove_owned(parent: int, name: str, identity: tuple[int, int]) -> None:
    """Best-effort inode-checked cleanup; not atomic against same-user mutation."""
    try:
        if _identity(os.stat(name, dir_fd=parent, follow_symlinks=False)) == identity:
            os.unlink(name, dir_fd=parent)
    except OSError:
        pass


def export_report(workspace: tuple[int, list[tuple[int, str, int]]], relative_path: str,
                  output_format: str, result: dict) -> None:
    """Create one new private draft file beneath an existing open workspace.

    Render before opening a file. Stage with exclusive no-follow creation, then
    hard-link to the explicit destination without replacing anything. Existing
    inputs/targets, symlinks and missing parents fail closed. Check ancestry and
    inode identity before/after publication; remove only our own inode on error.
    This is not a sandbox against a malicious OS or concurrent privileged actor.
    """
    path = "$.output"
    if output_format not in SUFFIXES:
        raise ValidationError("INVALID_SCHEMA", "$.arguments")
    payload = render_report(result, output_format)
    parts = _output_parts(relative_path, output_format)
    if (os.link not in os.supports_dir_fd or os.unlink not in os.supports_dir_fd or
            os.link not in os.supports_follow_symlinks):
        raise ValidationError("UNSAFE_PATH", path)
    root, root_links = workspace
    parent = root
    descriptors: list[int] = []
    temporary = None
    own_identity = None
    published = False
    complete = False
    try:
        links = list(root_links)
        _verify_links(links, path)
        for component in parts[:-1]:
            before = os.stat(component, dir_fd=parent, follow_symlinks=False)
            child = os.open(component, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC, dir_fd=parent)
            descriptors.append(child)
            if not stat.S_ISDIR(before.st_mode) or _identity(before) != _identity(os.fstat(child)):
                raise ValidationError("UNSAFE_PATH", path)
            links.append((parent, component, child))
            parent = child
        # Reject an existing destination before staging, including dangling links.
        try:
            os.stat(parts[-1], dir_fd=parent, follow_symlinks=False)
        except FileNotFoundError:
            pass
        else:
            raise ValidationError("UNSAFE_PATH", path)
        _verify_links(links, path)
        temporary = ".deadline-guard-" + secrets.token_hex(16) + ".tmp"
        descriptor = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW | os.O_CLOEXEC, 0o600, dir_fd=parent)
        descriptors.append(descriptor)
        opened = os.fstat(descriptor)
        own_identity = _identity(opened)
        if not stat.S_ISREG(opened.st_mode):
            raise ValidationError("UNSAFE_PATH", path)
        offset = 0
        while offset < len(payload):
            count = os.write(descriptor, payload[offset:])
            if count <= 0:
                raise OSError("write failed")
            offset += count
        os.fsync(descriptor)
        _verify_links(links + [(parent, temporary, descriptor)], path)
        if os.fstat(descriptor).st_size != len(payload):
            raise ValidationError("UNSAFE_PATH", path)
        os.link(temporary, parts[-1], src_dir_fd=parent, dst_dir_fd=parent, follow_symlinks=False)
        published = True
        _verify_links(links + [(parent, temporary, descriptor), (parent, parts[-1], descriptor)], path)
        complete = True
    except (OSError, ValueError, NotImplementedError):
        raise ValidationError("UNSAFE_PATH", path) from None
    finally:
        if temporary is not None and own_identity is not None:
            _remove_owned(parent, temporary, own_identity)
            if published and not complete:
                _remove_owned(parent, parts[-1], own_identity)
        for descriptor in reversed(descriptors):
            os.close(descriptor)
