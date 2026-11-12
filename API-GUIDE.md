# API-GUIDE.md — Interface Contracts

> **Current decision, 1 November 2026 (SGT):** The user has authorised resolving T00 discovery decisions and T01 schema here. Proceed with an offline fictional-data prototype under recorded, unvalidated-demand assumptions. The five interviews are a wider-investment/product-launch gate. Canonical T01 artefacts replace earlier illustrative contracts; application execution and product release remain separate gates. See [DECISIONS.md](DECISIONS.md) and [CONTRACT.md](CONTRACT.md).


**Status:** T04 validation/comparison and explicit draft exports implemented on this branch; T05 repository skill packaging is present; host compatibility remains pending.
**v0.1 decision:** No HTTP endpoints, no webhooks, no OAuth, no SDK calls, no remote writes and no paid APIs.

## 1. Canonical contract

The current frozen snapshot/result schemas and all semantic invariants are in [CONTRACT.md](CONTRACT.md), [snapshot v1](schemas/snapshot-v1.schema.json), [result v1](schemas/result-v1.schema.json) and [fictional cases](examples/contract-cases.json). These replace the earlier split-field/derived due_at illustrations. Schemas are contracts; T02 provides a direct standard-library validator against their structure and mandatory semantics.

The helper will accept only local structured JSON, never raw PDFs or source instructions. User-selected AI host extraction remains separate and untrusted. Full source text and matching literal excerpts support traceability, not authenticated provenance or a proof that a stated date is true.

## 2. Draft comparison CLI

`reconcile.py --workspace WORKSPACE --before BEFORE.json --after AFTER.json` is the implemented workspace-bound validation and comparison interface. T04 adds paired `--output RELATIVE_PATH --format json|csv|markdown`; no output overwrite is permitted. --help and --version are tested without opening inputs. Exact syntax and exit/error contract are frozen in CONTRACT.md. No network, HTTP routes, webhooks or credentials.

The result always remains a draft, requires review, sets user_confirmed=false and has confirmed_changes=[]. A schema-valid successful draft may contain CONFLICT or UNVERIFIED; success never means a resolved deadline.

## 3. Hosts and future integrations

Python CLI is the first test target. Claude and a second eligible host need later real installation evidence before compatibility claims. A host without execution capability may display a manual evidence table, but must not pretend the helper ran. No host account/plan availability was verified in this decision.

Any future HTTP route, calendar/remote write or hosted history requires separately approved scope, threat/data map, authorisation, quotas, deletion, recovery and release controls.

## Implemented T04 interface

`python skills/academic-deadline-drift-guard/scripts/reconcile.py --workspace . --before examples/fictional-before.json --after examples/fictional-after.json` validates both snapshots sequentially, then prints deterministic draft JSON to stdout. `--help` and `--version` do not open inputs. Without export options, no file is written. With both `--output` and `--format`, a new draft file is explicitly created inside the workspace.

Exit 0: draft generated, potentially containing conflicts; 2: invalid input/schema/size; 3: unsafe or inaccessible path; 4: unexpected internal error. Errors contain a fixed category and field path, never source content or user filenames. CONTRACT.md remains normative. See T04_VERIFICATION.md for current export checks and T03_VERIFICATION.md for comparator checks and T02_VERIFICATION.md for historical validator evidence.

### Export boundaries

Both export options are required together. Accepted format/suffix pairs are `json/.json`, `csv/.csv` and `markdown/.md`, case-sensitive. Output parent directories must exist. Reject absolute/traversal/backslash/NUL paths, all symlink components, existing targets (including inputs and hard links) and unsupported filesystem capabilities. No automatic directories, discovery, temporary-file races, overwritten inputs or calendar import formats are authorised.

Reports always retain REVIEW_REQUIRED, explicit review/confirmation flags and no confirmed changes; CSV/Markdown are draft report representations, not final deadline imports. JSON preserves exact canonical strings. CSV quotes fields and neutralises formula-leading text; Markdown neutralises markup/HTML and links. Rendering transformations are not corrections to source evidence.

On export failure no deadline is confirmed and inputs remain unchanged. Errors remain fixed categories/paths with exit codes 2/3/4 as applicable; no raw source values or filenames are echoed. T04_VERIFICATION.md records tested write failure/race cases and platform limits.

## T05 package entry point

`skills/academic-deadline-drift-guard/SKILL.md` supplies the agent-facing workflow and bundled references. The existing Python CLI/interface and frozen v1 contracts are unchanged. T05_VERIFICATION.md distinguishes local package checks from T08 actual host invocation and provider eligibility checks. No personal installation or host compatibility is implied.
