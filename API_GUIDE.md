# API_GUIDE.md — Interface Contracts

> **Current decision, 1 November 2026 (SGT):** The user has authorised resolving T00 discovery decisions and T01 schema here. Proceed with an offline fictional-data prototype under recorded, unvalidated-demand assumptions. The five interviews are a wider-investment/product-launch gate. Canonical T01 artefacts replace earlier illustrative contracts; application execution and product release remain separate gates. See [DECISIONS.md](DECISIONS.md) and [CONTRACT.md](CONTRACT.md).


**Status:** T01 canonical contract adopted for constrained prototype; no CLI implementation or runtime tests yet.  
**v0.1 decision:** No HTTP endpoints, no webhooks, no OAuth, no SDK calls, no remote writes and no paid APIs.

## 1. Canonical contract

The current frozen snapshot/result schemas and all semantic invariants are in [CONTRACT.md](CONTRACT.md), [snapshot v1](schemas/snapshot-v1.schema.json), [result v1](schemas/result-v1.schema.json) and [fictional cases](examples/contract-cases.json). These replace the earlier split-field/derived due_at illustrations. Schemas are contracts, not an implemented validator.

The helper will accept only local structured JSON, never raw PDFs or source instructions. User-selected AI host extraction remains separate and untrusted. Full source text and matching literal excerpts support traceability, not authenticated provenance or a proof that a stated date is true.

## 2. CLI implementation target, not yet runnable

`reconcile.py --workspace WORKSPACE --before BEFORE.json --after AFTER.json` is the future workspace-bound read interface. An explicit output destination and JSON/Markdown/CSV exporters belong to T04; no output overwrite is permitted. --help and --version must be deterministic when implemented. Exact syntax and exit/error contract are frozen in CONTRACT.md. No network, HTTP routes, webhooks or credentials.

The result always remains a draft, requires review, sets user_confirmed=false and has confirmed_changes=[]. A schema-valid successful draft may contain CONFLICT or UNVERIFIED; success never means a resolved deadline.

## 3. Hosts and future integrations

Python CLI is the first test target. Claude and a second eligible host need later real installation evidence before compatibility claims. A host without execution capability may display a manual evidence table, but must not pretend the helper ran. No host account/plan availability was verified in this decision.

Any future HTTP route, calendar/remote write or hosted history requires separately approved scope, threat/data map, authorisation, quotas, deletion, recovery and release controls.
