# T04 safe exporter verification

**Date:** 2 November 2026 (Asia/Singapore). **Ticket:** T04 only.
**Specification:** ADDG-SPEC-001 v0.2.0-prototype-contract; CONTRACT.md v1.0.
**Implementation version:** `0.3.0-prototype-t04`.
**State:** IMPLEMENTED and locally tested. Independent review, current-head CI, merge and release are separate gates; this file alone is not ticket PASS or approval.

## Scope and interface

CONFIRMED: The existing default CLI still prints a deterministic draft JSON result without creating a file. Supplying `--output relative-file --format json|csv|markdown` together requests one new local draft file beneath the explicit workspace; format suffixes are exactly `.json`, `.csv` and `.md`. Supplying only one option fails with redacted `INVALID_SCHEMA $.arguments`. Output is never a confirmed deadline or calendar import. On successful export stdout is a fixed, non-sensitive review-required summary.

CONFIRMED: The pure renderer keeps canonical JSON values unchanged with ASCII JSON escaping. CSV quotes all cells, prefixes formula-like text (including whitespace-leading formula text) with an apostrophe, retains both sides and evidence, and carries review flags. Empty CSV carries an explicit review-required metadata row. Markdown HTML-escapes and escapes literal Markdown structure, encodes line breaks and punctuation used by plain URL/email autolinks, and labels evidence untrusted. CSV/Markdown are display formats, not round-trip canonical schema formats. These transformations do not authenticate sources or make embedded instructions trustworthy. Lone-surrogate text cannot be encoded as UTF-8 Markdown/CSV and fails with redacted `INVALID_SCHEMA $.result` before any file is opened; JSON safely retains such strings using ASCII escapes.

CONFIRMED: The writer opens existing output ancestors through no-follow directory descriptors, retaining the workspace chain. It rejects unsafe path components, incorrect suffixes, missing parents, symlinks and existing destinations. CLI explicitly rejects either selected input path as an output, even if that path were removed after reading. A random staging file is created exclusively with mode 0600, written completely, fsynced and checked; hard-link publication creates the explicit destination only if absent. Ancestor and inode checks occur before/after publication. No network, shell, secret read, host integration or hidden application persistence was added.

## Changed implementation files

- `skills/academic-deadline-drift-guard/scripts/exporter.py`
- `skills/academic-deadline-drift-guard/scripts/reconcile.py`
- `tests/test_exporter.py`

The integrating agent updates version, status, data and deletion documentation in the same PR. No contract/schema semantics changed. T05 packaging remains excluded.

## Executed checks

| Command | Actual result |
|---|---|
| `python -B -m unittest tests.test_exporter -v` (initial 14 tests) | Initial run exposed an encoding-error expectation mismatch; corrected safe-category handling. Subsequent 14-test run passed. Two further negative tests were then added. |
| `python -B -m unittest discover -s tests -q` (final implementation) | Exit 0; 66 tests run, 65 passed, 1 existing UNIX-socket capability skip |
| `python -m compileall -q skills/academic-deadline-drift-guard/scripts tests` | Exit 0 |
| `python -B -m unittest tests.test_exporter -q` (final 16 tests) | Exit 0; 16 passed |
| Integrator real subprocess CLI, all three formats in temporary fictional workspace | Reported exits 0; JSON/CSV/Markdown files created, only input pair and three selected outputs present; JSON confirmed_changes empty. Integrator retains direct evidence. |
| `git diff --check` | Exit 0 at inspected working state |

The 16 exporter tests cover canonical JSON equality/non-mutation, both-side CSV evidence and review fields, spreadsheet formula/control prefixes and quoting, Markdown/HTML/injection syntax, empty drafts, confirmed-content rejection, all three output formats and 0600 mode, existing/input/hardlink targets, unsafe/missing/symlink paths, simulated failed/short writes, destination creation during publication, parent rename during writing, postpublication failure, replacement preservation during cleanup, unsupported publication capabilities and encoding failure before writes. CLI tests verify explicit paired options, all formats, safe errors and preservation of input snapshots. Existing 50 validator/comparator tests continue to run.

## Limits, review and rollback

CONFIRMED: Independent read-only reviewer `/root/review_t04` found no material correctness/security issue; freshly reran 66 tests (65 passed, one inherited capability skip), compile and whitespace checks. The reviewer also rendered all 22 accepted canonical pairs in all three formats, checking canonical JSON round-trip and CSV/Markdown draft-only markers, including empty CSV. Integrator independently reran the same full suite and real subprocess CLI for each format successfully. UNKNOWN pending integration: final PR CI and authorised human review; final source tree/commit is recorded in the PR. Python 3.11/3.13 CI and real host invocation are not asserted by this local Python run.

INFERENCE: Descriptor and inode checks detect the exercised rename/replacement races, but the helper is not a security sandbox against a malicious OS or concurrent same-user/privileged actor. Cleanup is best-effort, inode-checked and not atomic against concurrent mutation. An I/O/permission/crash failure can leave a private staging file or published draft; no unconditional crash-durability or erasure guarantee is made. Users must inspect and remove their own files after a reported failure. Hard-link publication requires a supporting POSIX filesystem; unsupported environments fail closed. File names, evidence and source excerpts are user-selected sensitive data and must not be logged or committed as real student examples.

Rollback before merge: close/revise this T04 PR. After an authorised merge: reviewed revert of T04 implementation and related documentation restores the T03 stdout-only CLI. Existing user-selected exports are not deleted by a code revert; users remove their own files and backup copies. No remote state or migration exists.
