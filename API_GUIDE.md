# API_GUIDE.md — Interface Contracts

> **Current decision, 1 November 2026 (SGT):** The user has authorised resolving T00 discovery decisions and T01 schema here. Proceed with an offline fictional-data prototype under recorded, unvalidated-demand assumptions. The five interviews are a wider-investment/product-launch gate. Canonical T01 artefacts replace earlier illustrative contracts; application execution and product release remain separate gates. See [DECISIONS.md](DECISIONS.md) and [CONTRACT.md](CONTRACT.md).


**Status:** T02 validation-only CLI implemented and locally tested; comparison/export remain unimplemented.
**v0.1 decision:** No HTTP endpoints, no webhooks, no OAuth, no SDK calls, no remote writes and no paid APIs.

## 1. Canonical contract

The current frozen snapshot/result schemas and all semantic invariants are in [CONTRACT.md](CONTRACT.md), [snapshot v1](schemas/snapshot-v1.schema.json), [result v1](schemas/result-v1.schema.json) and [fictional cases](examples/contract-cases.json). These replace the earlier split-field/derived due_at illustrations. Schemas are contracts; T02 provides a direct standard-library validator against their structure and mandatory semantics.

The helper will accept only local structured JSON, never raw PDFs or source instructions. User-selected AI host extraction remains separate and untrusted. Full source text and matching literal excerpts support traceability, not authenticated provenance or a proof that a stated date is true.

## 2. Validation-only CLI

`reconcile.py --workspace WORKSPACE --before BEFORE.json --after AFTER.json` is the implemented workspace-bound validation interface. An explicit output destination and JSON/Markdown/CSV exporters belong to T04; no output overwrite is permitted. --help and --version are tested without opening inputs. Exact syntax and exit/error contract are frozen in CONTRACT.md. No network, HTTP routes, webhooks or credentials.

The result always remains a draft, requires review, sets user_confirmed=false and has confirmed_changes=[]. A schema-valid successful draft may contain CONFLICT or UNVERIFIED; success never means a resolved deadline.

## 3. Hosts and future integrations

Python CLI is the first test target. Claude and a second eligible host need later real installation evidence before compatibility claims. A host without execution capability may display a manual evidence table, but must not pretend the helper ran. No host account/plan availability was verified in this decision.

Any future HTTP route, calendar/remote write or hosted history requires separately approved scope, threat/data map, authorisation, quotas, deletion, recovery and release controls.

## Implemented T02 interface

`python skills/academic-deadline-drift-guard/scripts/reconcile.py --workspace . --before examples/fictional-before.json --after examples/fictional-after.json` validates both snapshots sequentially. --help and --version do not open input files. Success prints a fixed validation-only summary. There is no --output/--format option in T02 and no generated report.

Exit 0: inputs valid, comparison not implemented; 2: invalid input/schema/size; 3: unsafe or inaccessible path; 4: unexpected internal error. Errors contain a fixed category and field path, never source content or user filenames. See CONTRACT.md for the mandatory priority and semantics and T02_VERIFICATION.md for fresh evidence.
