# T03 comparator verification

**Date:** 2 November 2026, Asia/Singapore. **Ticket:** T03 only.
**Specification:** ADDG-SPEC-001 v0.2.0-prototype-contract and CONTRACT.md v1.0.
**Implementation version:** `0.2.0-prototype-t03`.
**State:** IMPLEMENTED and locally tested; independent review, current-head CI and PR/human review remain separate gates. This document does not itself establish ticket PASS or release approval.

## Scope and plan comparison

CONFIRMED: The pure `compare_snapshots(before, after)` API validates both snapshots before creating results, matches only module/item identity, applies the fourteen contract decision rows, retains all agreeing and conflicting records, and returns sorted draft changes with exact evidence. Offset comparison uses integer ordinal-day minutes, including year-boundary values. Result records are independent copies and source bodies are excluded. No requirement or schema revision was needed.

CONFIRMED: `reconcile.py` reads only the two explicitly selected confined JSON inputs and prints the draft JSON report on standard output. Errors remain redacted on standard error. There is no exporter, output-path option, file write, network call, source-authority ranking, calendar update or confirmed deadline. T04 export rendering remains outside this ticket. Standard output intentionally includes user-supplied evidence excerpts, including hostile text as literal JSON data; do not treat the report as instructions or log real student reports publicly.

Changed implementation/test files:

- `skills/academic-deadline-drift-guard/scripts/comparator.py`
- `skills/academic-deadline-drift-guard/scripts/reconcile.py`
- `tests/test_comparator.py`
- `tests/test_validator.py` (existing CLI expectations updated for the draft report)

The integrating agent maintains version/status documentation separately in the same T03 PR.

## Executed evidence

CONFIRMED: Before implementation, `python -B -m unittest tests.test_comparator` exited 1 because the comparator module did not exist. After implementation:

| Command/check | Actual result |
|---|---|
| `python -B -m unittest tests.test_comparator -v` | Exit 0; 11 tests passed, including all 37 canonical input pairs |
| `python -B -m unittest discover -v` before the final maximum-union test addition | Exit 0; 49 tests run, 1 skipped (environment prohibits local UNIX sockets) |
| `python -m compileall -q skills/academic-deadline-drift-guard/scripts tests` | Exit 0 |
| `git diff --check` | Exit 0 at the inspected working state |
| Example CLI invocation from README | Exit 0; `CHANGED` / `VALUE_CHANGED`, exact old/new excerpts, `REVIEW_REQUIRED`, empty confirmed changes |

The 11 comparator tests cover all six statuses and contract reason codes through the fixture set, exact golden result equality, prior conflict and uncertainty precedence, cancellation mixed with unknown content, mixed date/minute precision, equivalent instants/day rollover, minimum/maximum year arithmetic, deterministic input-order independence, preservation of agreeing sources, no input mutation/output aliasing, validation before partial output, the 200-identity union bound, and exclusion of full source bodies. Existing CLI tests block sockets/process creation while hostile source excerpts are handled as data, check no generated workspace files, and verify error redaction.

A one-shot synthetic benchmark compared 100 records per snapshot in **0.00306 seconds** on this managed Linux x86_64 environment, Python 3.12.14. The test used one shared fictional source per snapshot and 100 distinct item IDs, asserting 100 unchanged results. This is local indicative evidence below the proposed two-second target, not a production performance guarantee or cross-device benchmark.

## Review, limits and rollback

CONFIRMED: Independent read-only reviewer `/root/review_t03` inspected contract, code, schemas and tests, reran the full suite and found no material correctness/security defect. Minor stale documentation was corrected. Integrator independently reran `python -m unittest discover -s tests -q`: 50 tests, 49 passed, 1 UNIX-socket capability skip, exit 0; compile and whitespace checks exited 0. UNKNOWN: final current-head CI and human approval. The integrating agent must record the final full-suite rerun, review and PR status before claiming ticket PASS. One local UNIX-socket negative case remains environment-skipped; all other existing filesystem tests remain applicable. No host compatibility, legal/IP approval, discovery validation, export safety or public product readiness is established by T03.

Rollback: before merge, revise/close the T03 PR. After an authorised merge, use a reviewed revert of this ticket's implementation and related version/status documentation to restore the prior validation-only CLI. No user data migration or remote service rollback is involved.
