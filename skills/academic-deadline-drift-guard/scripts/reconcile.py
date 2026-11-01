#!/usr/bin/env python3
"""T02 validation-only CLI; comparison and exports are not implemented yet."""

from __future__ import annotations

import argparse
import sys

# Do not create a bytecode cache in the user's workspace merely by invoking CLI.
sys.dont_write_bytecode = True

from validator import ValidationError, open_workspace, read_snapshot

VERSION = "0.1.0-prototype-t02"


class _SafeParser(argparse.ArgumentParser):
    def error(self, _message: str) -> None:
        raise ValidationError("INVALID_SCHEMA", "$.arguments")


def main(argv: list[str] | None = None) -> int:
    """Validate before then after; emit only a safe summary/error, never data."""
    parser = _SafeParser(description=__doc__, allow_abbrev=False)
    parser.add_argument("--version", action="version", version=VERSION)
    parser.add_argument("--workspace", required=True, help="explicit existing local workspace")
    parser.add_argument("--before", required=True, help="relative .json input within workspace")
    parser.add_argument("--after", required=True, help="relative .json input within workspace")
    try:
        arguments = parser.parse_args(argv)
        with open_workspace(arguments.workspace) as workspace:
            read_snapshot(workspace, arguments.before, "$.before")
            read_snapshot(workspace, arguments.after, "$.after")
        print("VALIDATED_INPUTS: review required; comparison not yet implemented.")
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
