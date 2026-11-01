# DATABASE.md — Data Model and Backend Readiness

> **Repository reconciliation, 1 November 2026 (SGT):** No database, application or migration exists at the inspected baseline. The transient schema remains provisional and needs the duplicate-candidate decision described in DISCOVERY.md. See [BOOTSTRAP.md](BOOTSTRAP.md) and [DISCOVERY.md](DISCOVERY.md).

**Decision:** NO DATABASE for v0.1. **Status:** PROPOSAL / no implementation. This file documents a logical, transient schema and future backend controls, rather than inventing deployed tables.

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

## 2. Proposed logical records (not SQL tables)

**`Snapshot`**: `schema_version`, `snapshot_id` (non-PII), `scope` (`complete`/`partial`), `sources[]`, `records[]`, `created_at` (optional; never invent).

**`Source`**: `source_id`, `source_type` (`text`/`notice`/`brief`/`other`), `label`, `observed_at` (nullable), `effective_at` (nullable), `excerpt`/hash reference, `authority_confirmed_by_user` (boolean; default false). A user-supplied timestamp is not proof of origin.

**`DeadlineRecord`**: `item_id`, `module_id`, `title`, `due_date` (ISO date), `due_time` (nullable), `timezone` (explicit offset or IANA zone if known), `time_precision` (`date`/`minute`), `source_id`, `source_excerpt`, `explicit_cancellation` (bool), `user_confirmed` (bool, default false). At least one valid source excerpt must substantiate a reported proposed date change.

**`ReconciliationResult`**: `item_id`, `module_id`, `status`, `before`, `candidates[]`, `source_references[]`, `explanation`, `requires_user_review`, `user_confirmed=false`.

### Relationships and invariants

- A snapshot contains zero or more sources and records; each record refers to a source in the same snapshot.
- Record IDs are unique per module per snapshot; repeated identifiers across conflicting same-snapshot sources represent a candidate conflict, not an accidental overwrite.
- A partial snapshot does not prove removal.
- An exact time requires a valid date, timezone and precision; no assumed `+08:00` solely from company location.
- The structured output is provisional until confirmed; once exported, no original files are modified.
- Source excerpts are retained solely in user-controlled artefacts; do not put real excerpts in public fixtures.

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
