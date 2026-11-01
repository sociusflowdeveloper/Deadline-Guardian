# API_GUIDE.md — Interface Contracts

> **Repository reconciliation, 1 November 2026 (SGT):** No executable CLI exists. Contract contradictions requiring a T01 decision are listed in DISCOVERY.md; do not implement the illustrative examples as an approved schema. See [BOOTSTRAP.md](BOOTSTRAP.md) and [DISCOVERY.md](DISCOVERY.md).

**Status:** DRAFT CONTRACT; commands and endpoints below are **design proposals, not implemented or tested**.  
**v0.1 decision:** No HTTP endpoints, no webhooks, no OAuth, no SDK calls, no remote writes and no paid APIs.

## 1. Boundaries and services

`user → chosen AI host / agent instructions → structured JSON → offline Python validator/reconciler → draft report → user review → user-controlled output`.

Only the user-selected host handles conversational input. The comparator must not communicate with the host's network APIs. The user's use of a hosted AI model is **not local-only processing**; its independent policies apply.

## 2. Proposed CLI

```bash
python skills/academic-deadline-drift-guard/scripts/reconcile.py \
  --before examples/fictional-before.json \
  --after examples/fictional-after.json \
  --output report.json
```

- `--before`, `--after`: explicitly chosen local `.json` files.
- `--output`: new output file; no overwrites or directory traversal; do not permit write to input path.
- `--format`: optional `json`, `md` or `csv` when implemented; default `json`.
- `--help` and `--version`: documented and deterministic when implemented.
- Exit codes **proposed**: `0` successful draft report; `2` invalid input; `3` unsafe/blocked operation; `4` processing failure. A detected conflict is not a successful resolved export; result contains unresolved status.
- Standard output: concise non-sensitive summary; standard error: error code + field path, no input data or stack trace.

## 3. Versioned JSON snapshot contract (proposed v1)

```json
{
  "schema_version": "1.0",
  "snapshot_id": "synthetic-new",
  "scope": "partial",
  "sources": [
    {
      "source_id": "new-notice",
      "source_type": "notice",
      "label": "fictional notice",
      "observed_at": null,
      "authority_confirmed_by_user": false
    }
  ],
  "records": [
    {
      "item_id": "marketing-report",
      "module_id": "MKT101",
      "title": "Marketing report",
      "due_date": "2026-11-14",
      "due_time": "23:59",
      "timezone": "+08:00",
      "time_precision": "minute",
      "source_id": "new-notice",
      "source_excerpt": "Report due 14 November 2026 at 23:59 SGT.",
      "explicit_cancellation": false,
      "user_confirmed": false
    }
  ]
}
```

All example names and data are fictional. T01 must finalise a strict JSON Schema or equivalent validation and clear rules for duplicate/conflicting records **before** coding the comparator. A source is an asserted provenance reference, not cryptographic verification.

## 4. Reconciliation output (proposed)

```json
{
  "schema_version": "1.0",
  "result_status": "REVIEW_REQUIRED",
  "changes": [
    {
      "module_id": "MKT101",
      "item_id": "marketing-report",
      "status": "CHANGED",
      "before_due_at": "2026-11-12T17:00:00+08:00",
      "candidate_due_at": "2026-11-14T23:59:00+08:00",
      "before_source_id": "old-brief",
      "candidate_source_id": "new-notice",
      "requires_user_review": true,
      "user_confirmed": false
    }
  ],
  "confirmed_changes": []
}
```

`confirmed_changes` stays empty until a separate, explicit review step with a verifiable confirmation input is specified and implemented. The report must preserve source excerpts or stable references, with user-controlled privacy settings. No field is implied to be authenticated merely because it is present.

## 5. Status and error contracts

| Status | Meaning | Safe outcome |
|---|---|---|
| `UNCHANGED` | Same explicit, comparable values | No action |
| `ADDED` | New item with evidence | Proposed addition; review |
| `CHANGED` | Same stable item with different evidenced value | Proposed revision; review |
| `REMOVED` | Explicitly cancelled by cited source | Proposed removal; review |
| `CONFLICT` | Multiple incompatible candidate values | No final value; seek verification |
| `UNVERIFIED` | Incomplete, ambiguous or unsupported | No final value; seek evidence |

Error categories: `INVALID_SCHEMA`, `INVALID_DATE`, `AMBIGUOUS_TIMEZONE`, `DUPLICATE_IDENTIFIER`, `UNSAFE_PATH`, `INPUT_TOO_LARGE`, `UNSUPPORTED_VERSION`, `INTERNAL_ERROR`. No raw input in logs/errors. Partial inputs cannot be interpreted as deletion.

## 6. Host adapter contract

- **Canonical skill:** Uses standard `SKILL.md` with accurate description and explicit tool boundaries.
- **Claude:** Install using current documented capability, manually test real invocation and file access.
- **ChatGPT:** Install only in eligible, documented skill-capable environment; do not claim all ChatGPT accounts support the same mechanism.
- **Grok:** Confirm the particular product/CLI supports the selected skills format and actual file execution; document limitations.
- **Common fallback:** If the host cannot run scripts or save files, display a plain-text evidence table and label it manual/unverified. Never fake a tool result.
- Record host version, date SGT, test transcript identifier, exact outcome and reviewer in the compatibility matrix.

## 7. HTTP API change-control trigger

Any proposed `/v1/*` route or remote integration requires: approved `SPEC.md` revision; authentication; server-side owner/tenant authorisation on **every** route; request schemas and size limits; error mapping; rate limits; audit/data-retention rules; abuse prevention; RLS where applicable; backup and deletion propagation; API versioning, idempotency, observability and rollback. No placeholder endpoints may be published as implemented.
