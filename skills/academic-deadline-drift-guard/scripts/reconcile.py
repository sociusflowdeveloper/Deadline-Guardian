#!/usr/bin/env python3
"""Offline v1 comparison CLI with explicit draft-only file export."""

from __future__ import annotations

import argparse
import json
import sys

# Do not create a bytecode cache in the user's workspace merely by invoking CLI.
sys.dont_write_bytecode = True

from validator import ValidationError, open_workspace, read_snapshot
from comparator import compare_snapshots
from exporter import export_report

VERSION = "0.3.0-prototype-t04"


class _SafeParser(argparse.ArgumentParser):
    def error(self, _message: str) -> None:
        raise ValidationError("INVALID_SCHEMA", "$.arguments")


def main(argv: list[str] | None = None) -> int:
    """Validate before then after; emit draft JSON or redacted errors."""
    parser = _SafeParser(description=__doc__, allow_abbrev=False)
    parser.add_argument("--version", action="version", version=VERSION)
    parser.add_argument("--workspace", required=True, help="explicit existing local workspace")
    parser.add_argument("--before", required=True, help="relative .json input within workspace")
    parser.add_argument("--after", required=True, help="relative .json input within workspace")
    parser.add_argument("--output", help="explicit new relative output file within workspace")
    parser.add_argument("--format", choices=("json", "csv", "markdown"), help="draft file format; requires --output")
    try:
        arguments = parser.parse_args(argv)
        if (arguments.output is None) != (arguments.format is None):
            raise ValidationError("INVALID_SCHEMA", "$.arguments")
        with open_workspace(arguments.workspace) as workspace:
            before = read_snapshot(workspace, arguments.before, "$.before")
            after = read_snapshot(workspace, arguments.after, "$.after")
            result = compare_snapshots(before, after)
            if arguments.output in (arguments.before, arguments.after):
                raise ValidationError("UNSAFE_PATH", "$.output")
            if arguments.output is not None:
                export_report(workspace, arguments.output, arguments.format, result)
        if arguments.output is None:
            print(json.dumps(result, ensure_ascii=True, indent=2))
        else:
            print("EXPORTED_DRAFT: REVIEW_REQUIRED; no confirmed changes.")
        return 0
    except ValidationError as error:
        print(str(error), file=sys.stderr)
        return 3 if error.code == "UNSAFE_PATH" else 2
    except Exception:
        # Do not expose exception details, paths, source contents or tracebacks.
        print("INTERNAL_ERROR $", file=sys.stderr)
        return 4


if __name__ == "__main__":
    raise SystemExit(main())
