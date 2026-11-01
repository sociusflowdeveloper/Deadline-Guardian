# CODE_STYLE.md — Engineering Standards

> **Repository reconciliation, 1 November 2026 (SGT):** No Python application, test suite, package manifest or workflow was present at the inspected baseline. Commands in this file are future implementation checks, not executed application tests. See [BOOTSTRAP.md](BOOTSTRAP.md) and [DISCOVERY.md](DISCOVERY.md).

**Status:** PROPOSAL, no code yet | **Runtime:** Python 3.11+ standard library | **Language:** British English for user-facing text.

## 1. Principles

- Prefer the smallest deterministic, auditable implementation that satisfies `SPEC.md`.
- Keep **extraction/interpretation** separate from **validation** and **comparison**. The model may propose records, but the Python comparator is the authoritative algorithm for status labels.
- No external package dependency, remote API, cloud SDK, database, environment secret, telemetry or hidden state in v0.1.
- Make unsafe or ambiguous inputs explicit errors or `UNVERIFIED`. Do not fabricate deadlines, timezones, source authority or source excerpts.
- No silent network access or automatic calendar writes, even if the host technically permits them.

## 2. Layout and names

- One canonical skill in `skills/academic-deadline-drift-guard/SKILL.md`; helper in `scripts/reconcile.py` and focused internal modules only if justified.
- Python naming: `snake_case` functions/variables/files, `PascalCase` types/exceptions, `UPPER_SNAKE_CASE` constants.
- Keep functions small, side effects isolated and dependencies injected; pure functions for matching, validation and reconciliation.
- Prefer `dataclasses`, `typing`, `enum`, `datetime`, `zoneinfo`, `json`, `csv`, `pathlib`, `argparse` and `unittest` where appropriate.
- No dynamic evaluation (`eval`/`exec`), unsafe deserialisation, shell=True, subprocess from untrusted input, broad filesystem crawling or runtime package installation.
- Date/time strings must be RFC 3339-compatible for exact instants, with explicit offset. Date-only values preserve precision. Use calendar dates, not free-text approximations in machine fields.
- Stable `item_id` and `module_id` must be explicit; do not fuzzy-merge similar titles without review.

## 3. Input and output discipline

- Strictly validate top-level version, snapshot metadata and record fields; reject unknown schema versions and unsafe path traversal.
- Preserve source excerpt verbatim except necessary escaping in display formats. Do not 'correct' source text silently.
- Use consistent statuses: `UNCHANGED`, `ADDED`, `CHANGED`, `REMOVED`, `CONFLICT`, `UNVERIFIED`. `REMOVED` requires explicit cancellation evidence.
- Separate `proposed_changes` from `confirmed_changes`; all default unconfirmed. One confirmed source is not a substitute for explicit user confirmation.
- JSON must be deterministic in ordering and normalisation; compare structured values, not formatted human prose.
- Never print student input on standard error or exception traces. Error output should show field paths and category, not private field contents.
- For CSV exports, prevent spreadsheet formula execution in text columns.
- File writes require explicit output destination, reject replacing input paths and use atomic output where possible.

## 4. Documentation and review

Every public function must have an intelligible contract; document assumptions, failure modes and relevant examples. Avoid claiming host support until tested on that actual host. Use short prose and precise examples. Each PR must link its ticket, affected SPEC requirement, tests, data/security implications, rollback and any source contract changes.

## 5. Tests and quality gates

- `unittest` tests for every status and every trust-boundary case in `SPEC.md`, including at least 12 canonical fictional fixtures.
- Golden-file outputs reviewed for stable, human-readable evidence.
- Negative tests: invalid time, timezone missing, empty items, duplicate IDs, contradictory candidates, partial source, hostile embedded instructions, invalid path, oversized source, CSV formula payload.
- Static checks: `python -m compileall`, tests with `python -m unittest discover`, `git diff --check`, chosen formatter/linter only after approval (no paid tools assumed).
- Review all coverage gaps, not simply a green overall status. Record exact commands and results at final commit.

## 6. Error and logging style

Public errors use predictable machine codes, e.g. `INVALID_SCHEMA`, `AMBIGUOUS_DATE`, `UNSAFE_PATH`, `INPUT_TOO_LARGE`, `INTERNAL_ERROR`; never expose stack traces to end users. No persistent logging of inputs. CI jobs must use synthetic fixtures and redact sensitive material.

## 7. Source changes and release versions

Use semantic versioning after first approved release. A breaking schema change requires an ADR, migration plan and fixture update. No ticket can add a dependency, network call, account, background job or new data type without approved changes to `SPEC.md`, `SECURITY.md`, `DATABASE.md`, `DATA.md`, `API_GUIDE.md` and the privacy review.
