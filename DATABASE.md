# DATABASE.md — Data Model and Backend Readiness

> **Current decision, 1 November 2026 (SGT):** The user has authorised resolving T00 discovery decisions and T01 schema here. Proceed with an offline fictional-data prototype under recorded, unvalidated-demand assumptions. The five interviews are a wider-investment/product-launch gate. Canonical T01 artefacts replace earlier illustrative contracts; application execution and product release remain separate gates. See [DECISIONS.md](DECISIONS.md) and [CONTRACT.md](CONTRACT.md).


**Decision:** NO DATABASE for v0.1. **Status:** Adopted no-database prototype design; local validation implemented, no persistence. This file documents a logical, transient schema and future backend controls, rather than inventing deployed tables.

## 1. v0.1 architecture

Student provides material to their chosen AI host; the skill instructs the model to extract *proposed* structured records; an offline Python helper validates and compares them; the user reviews a report and may save an export to their own files. SociusFlow does not create user accounts, database rows, session IDs, cloud buckets or backups in this design.

| Database concern | v0.1 disposition | Trigger for design change |
|---|---|---|
| Tables / persistence | No physical tables; memory and user-managed JSON only | Hosted history or multi-device sync |
| Indexes | Not applicable; bounded in-memory map indexed by `(module_id, item_id)` | PostgreSQL query planning |
| Relationships | JSON snapshot → records → source evidence | Backend relational schema |
| N+1 queries | Not applicable, no database | Explicit query budget, join/batch tests |
| Connection pooling | Not applicable, no database sockets | Pool sizing and managed-pool configuration |
| Migrations | JSON `schema_version` and safe refusal of unknown versions | Versioned SQL migrations, rollback strategy |
| Backups / restore | No operator-controlled copy | Encrypted backups, point-in-time recovery, restore drill |
| Authentication | Not applicable, no account | Identity provider and server-side sessions |
| Authorisation / RLS | Not applicable, no shared records | Per-owner checks on each request + database RLS tests |
| DevOps | GitHub CI and signed/traceable release process proposed | Infrastructure, monitoring and operations plan |
| Payments | None | Separate pricing/payment compliance and security review |
| Compliance | Minimise input, use synthetic fixtures, host disclosure | Data protection impact and DPO review |
| AI | Host interpretation may be unreliable, deterministic validation | Model/version provenance, evaluation and abuse monitoring |

## 2. Canonical transient records

Use CONTRACT.md and schemas/snapshot-v1.schema.json as the only normative definition. Source records include bounded full text, and each deadline excerpt must be an exact non-empty substring of its referenced source. Source identity is asserted, never authenticated by the schema.

Match assessments by `(module_id, item_id)`. A snapshot may hold multiple source candidates for one assessment; `(module_id, item_id, source_id)` triples must be unique. Conflicting candidates are retained and never overwritten. No source rank or observed timestamp resolves authority.

Use split date/time/offset fields. Date-only, timed-with-unknown-offset, unknown and cancellation forms have separate rules; cancellation has null due fields. Missing records do not imply removal, even in complete snapshots. Results are deterministic drafts only and confirmed_changes is always empty.

There are no SQL tables, migrations or central storage. JSON Schema covers structure; CONTRACT.md lists the semantic checks future code must enforce.

## 3. Hypothetical hosted schema (NOT APPROVED)

If a hosted account service is separately authorised, **new architecture and policy approvals are compulsory**. Candidate PostgreSQL tables (design sketch, not implemented):

- `accounts(id UUID PRIMARY KEY, auth_subject UNIQUE, created_at, deleted_at)`
- `projects(id UUID PRIMARY KEY, owner_account_id FK, title, created_at)`
- `sources(id UUID PRIMARY KEY, project_id FK, kind, encrypted_payload_ref, created_at, expires_at)`
- `deadlines(id UUID PRIMARY KEY, project_id FK, stable_item_id, due_at, precision, status)`
- `reviews(id UUID PRIMARY KEY, deadline_id FK, actor_account_id FK, decision, evidence_ref, created_at)`
- `deletion_jobs(id UUID PRIMARY KEY, account_id, status, requested_at, completed_at)`

Proposed indexes: `projects(owner_account_id)`, `sources(project_id, expires_at)`, `deadlines(project_id, stable_item_id)` with uniqueness where warranted, and `reviews(deadline_id, created_at)`. **Never implement these without a new data-flow, RLS, access control, retention and deletion design.**

### Hosted-system gates

- [ ] Compare Supabase/Firebase/own PostgreSQL with cost and risk before selection; no provider presumed.
- [ ] Design least-privilege service identities and owner-scoped SQL/RLS with negative cross-tenant tests.
- [ ] Enforce server-side authorisation on every endpoint, including exports, deletes and signed links.
- [ ] Plan N+1 detection, query budgets, bounded pagination and explain plans for indexes.
- [ ] Define pooler settings, connection limits, transaction lifetimes and failover behaviour.
- [ ] Use reversible versioned migrations; test backward compatibility and failed migration rollback.
- [ ] Encrypt storage/backups, test restore and track backup deletion expiry.
- [ ] Approve log/data retention and privacy notices before any user record is stored.
- [ ] Evaluate AI prompt retention and model provider data processing before third-party transfer.
- [ ] Require secure account deletion and notification mechanisms per `DELETE.md`.

**No database has been created, connected, migrated, backed up or tested.**
