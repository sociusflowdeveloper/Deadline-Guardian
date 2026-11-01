# T02 — Strict offline validator implementation

**Date:** 1 November 2026 (Asia/Singapore). **Ticket:** T02 only.
**Contract:** v1.0 / DG-DEC-001 / SPEC 0.2.0-prototype-contract.
**Remote base supplied by parent:** merged PR #1, `f2b2929f8c11b9c8d6dcef91987cf92d5a7e3226`.
**State:** IMPLEMENTED; author checks passed; independent review and final-head PR/CI evidence remain separate.

## Implemented seam

- `skills/academic-deadline-drift-guard/scripts/validator.py`: pure strict snapshot validation, strict byte/JSON decoding and descriptor-relative local input.
- `skills/academic-deadline-drift-guard/scripts/reconcile.py`: validation-only CLI; no comparison, report generation or output writes.
- `tests/test_validator.py` and `tests/__init__.py`: contract-derived tests with fictional input only.

The pure `validate_snapshot` API validates structure and calendar/reference/duplicate/excerpt semantics without mutation or I/O. `decode_snapshot` adds the raw 1 MiB byte cap, strict UTF-8, BOM/duplicate-key/non-finite-number/depth refusal. `load_snapshot` adds the explicit local-file boundary. Calling the pure API alone does not establish byte or filesystem guarantees.

Validation order is decoding/depth, version, structure, calendar dates, duplicate IDs/triples, source references and exact excerpts. Errors use a code and known field path without echoing source values or unknown JSON keys. Structural checks continue on present known fields even when another required field is missing, so the lexicographically first error path is preserved.

The file API requires POSIX descriptor-relative operations with nofollow, directory, close-on-exec and nonblocking flags. It opens every workspace ancestor/input component without following symlinks, rejects non-regular input, reads at most the byte cap plus one byte, and checks parent-child identity plus file revision after reading. A detected rename/replacement/in-place change fails closed. This is an explicit selected-file boundary, not an OS sandbox or protection against a malicious kernel/filesystem administrator. Unsupported platforms fail closed.

## CLI usage actually executed

From the repository root:

```bash
python -B skills/academic-deadline-drift-guard/scripts/reconcile.py \
  --workspace . \
  --before examples/fictional-before.json \
  --after examples/fictional-after.json
```

Exit 0; output: `VALIDATED_INPUTS: review required; comparison not yet implemented.`

`python -B skills/academic-deadline-drift-guard/scripts/reconcile.py --version` exited 0 and printed `0.1.0-prototype-t02`. Help/version do not open input files. CLI syntax errors are redacted rather than repeating arguments. Invalid input exits 2, unsafe paths exit 3, unexpected internal failures exit 4. A validation success message does not mean dates were confirmed or reconciled.

## Author verification

Executed against the current local implementation:

1. `PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -v`: exit 0; 39 test methods, 38 passed and one explicitly skipped. The fixture test exercises all 37 T01 validation expectations, comprising 22 accepted input pairs and 15 expected rejected pairs. It does not execute comparison-status expectations reserved for T03.
2. `python -m compileall -q skills/academic-deadline-drift-guard/scripts tests`: exit 0.
3. Real CLI fictional-example command and version command above: exit 0.
4. `git diff --check`: exit 0 for the existing tracked diff. Because implementation files were new/untracked during authoring, each new Python file also received `git diff --no-index --check /dev/null FILE`: all four returned exit 1 with empty diagnostics because no-index also reports newly added-file differences. An explicit Python whitespace scan of all four new Python files then exited 0 with no trailing-whitespace findings; no-index exit 1 is not recorded as a passing git-check exit.

Covered negatives include strict JSON failures, numeric overflow, 16-container depth enforcement, exact byte limit, malformed/invalid dates, type/coercion rejection, field/count/string bounds, mixed missing/invalid error ordering, timezone/cancellation precision, unsafe paths, file/directory/workspace symlinks, FIFO/nonregular/missing files, symlink swap between stat/open, parent rename, file replacement and in-place mutation during reading. The real CLI test verifies no changes to selected input/workspace contents. Hostile source content stays literal data; validation succeeds with socket/process creation patched to fail. This is a focused negative test, not proof of whole-machine network isolation.

The initial suite failed because this execution environment denies creating a local UNIX-domain socket. The nonregular-file test was split: FIFO/directory cases run and pass; the local socket-file case explicitly skips on PermissionError. This limitation is not a product success or a hidden test pass. A CI host that permits local sockets should execute that case.

## Scope comparison and residual gates

No production dependency, network client, model API, credential use, database, account, automatic extraction, comparator, exporter, `SKILL.md`, calendar write or paid service was added. Existing schema, licence and source ZIP are unchanged by T02. No runtime claims for Windows/macOS or any AI host are made; this author run used the provided Linux/Python 3.12 environment. CI Python-version coverage is pending actual workflow results.

The implementation is purpose-built equivalent validation for this fixed snapshot contract, not a general JSON Schema engine. Full JSON Schema library/metaschema conformance is not claimed. Exact excerpt matching proves only internal quotation consistency, not source authenticity or the truth of a deadline/cancellation.

Independent reviewer `review_t02` found the same mixed missing/invalid error-ordering gap, confirmed its correction and the 39-test result, and reported no remaining blocker for T02. Integrated test reruns, actual implementation head and PR checks must still be recorded by the parent before T02 is marked VERIFIED/accepted. T03 is the next separately ticketed comparator task. Product release remains blocked by the remaining security, host, rights/privacy and MD-release gates.

## Rollback

Before merge, revise or close the T02 PR. After any separately authorised merge, revert that PR through review. No user files, production data, network integration, schema migration or licence change requires recovery.

## Author file identities

- `skills/academic-deadline-drift-guard/scripts/validator.py` SHA-256: `1359f4eb30d0bac59bbc5954d446dc72c4d67f91658ec06af106acff9e90112a`
- `skills/academic-deadline-drift-guard/scripts/reconcile.py` SHA-256: `9e99a127aec52d773c44dfbdd8aa832f9583c16b37647e17e63b16013a0f1a84`
- `tests/__init__.py` SHA-256: `c781483382292b39dd64ec37caa419ed29bed508387edc8563612c16f364e856`
- `tests/test_validator.py` SHA-256: `e5c9ed068464085f46932bb1d0359d1f038d9d8ff510c77bb0bf10380fea103f`

## Parent integration verification

The integrating agent reran unittest discovery: 39 methods, 38 passed, one environment socket skip, exit 0. Fifty independent real CLI probes (including all 37 fixture pairs, traversal, symlink, FIFO, directory, BOM, duplicate JSON keys, byte-limit and argument-redaction cases) passed on Linux/Python 3.12.14. Compilation passed. The final git diff --check includes intent-to-add entries for new implementation/test/workflow files and the updated documentation; exit 0 after removing introduced Markdown trailing whitespace.

The separate reviewer inspected the pinned, read-only, bounded CI configuration and final code hashes. Actual remote head/check results are recorded in the T02 PR; this file does not preclaim remote CI success.
