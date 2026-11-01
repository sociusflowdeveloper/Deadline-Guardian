# ARCHITECTURE_DECISIONS.md — Technical Decision Register

> **Repository reconciliation, 1 November 2026 (SGT):** The repository exists and is public; this is an observed state, not an approved product release. The no-backend design remains a proposal. See BOOTSTRAP.md for immutable baseline evidence. See [BOOTSTRAP.md](BOOTSTRAP.md) and [DISCOVERY.md](DISCOVERY.md).

**Version:** 0.1 draft, 1 November 2026 (SGT). All decisions are **PROPOSALS pending owner approval**. No technical system has been deployed.

| ID | Proposed decision | Alternatives rejected for v0.1 | Consequence / reopening trigger | Status |
|---|---|---|---|---|
| ADR-001 | Agent Skills package + one canonical `SKILL.md` | Vendor-specific duplicated prompts | Test each host individually; differences documented | PROPOSED |
| ADR-002 | Python 3.11+ standard-library-only deterministic comparator | Node backend, LLM-only diffing | Requires local runnable environment; host fallback | PROPOSED |
| ADR-003 | No user accounts, authentication, backend, database or storage | Supabase, Firebase, PostgreSQL, S3 | Any hosted feature requires new security/privacy design | PROPOSED |
| ADR-004 | No direct calendars, emails, LMS, scraping or background jobs | Google/Microsoft connectors, polling | Future scope needs consent, tokens, least privilege | PROPOSED |
| ADR-005 | JSON v1 strict schema, source references and fail-closed ambiguity | Natural-language-only result | Schema approval precedes code | PROPOSED |
| ADR-006 | Explicit confirmation for every consequential changed deadline | Last-source-wins auto-merge | Slightly more friction but safer | PROPOSED |
| ADR-007 | GitHub public release only after IP/legal/security gates | Immediate open publication | Delays discoverability; protects rights and students | PROPOSED |
| ADR-008 | No pricing/payments or developer-paid infrastructure | Hosted paid SaaS | Host user's own plan may have costs; must not assume access | PROPOSED |
| ADR-009 | Synthetic fixtures and opt-in user research only | Live school document snapshots | Fewer realistic tests, safer initial risk | PROPOSED |

## Spending and provider checks

Python standard library has no third-party package subscription. GitHub public hosting, CI quotas and compatible Claude/ChatGPT/Grok access may have account, usage, plan or eligibility limitations. No current prices have been verified, no spend approved and no financial projections claimed. CTO should document availability and cost before requiring a paid account; CFO/Managing Director approves all non-zero commitments. Do not assume the company's existing Cloudflare, Supabase or Google Workspace accounts belong to this independent skill.

## Hosted service readiness register

| Topic | v0.1 | Future evidence gate |
|---|---|---|
| Auth / server authorisation | No users or server routes | Identity provider, owner checks, administrative role review |
| Database, RLS, N+1, indexes, pool | Absent, by design | Schema, query test suite, pool sizing, RLS negative tests |
| Migration / backups | JSON version; no central persistence | Reversible migrations, restore drills, documented backup expiry |
| DevOps | GitHub review and CI only, not yet set up | Environment isolation, observability, incident drills |
| Payments | None | Pricing, contracts, refund process, payment provider review |
| Privacy/PDPA | Data minimisation, disclosure and DPO review pending | Processing map, notices, lawful bases, transfers, deletion |
| AI-specific risks | Host interpretation limited, offline validator | Evaluation of providers, training/retention controls, abuse tests |
| Mobile/store/site | No app/site | Separate app-store accessibility, deletion and site QA gates |

## Rollback strategy

Before release: revert the PR without modifying production systems. After public distribution: remove affected release/download link, publish advisory and corrected tag/version, notify maintainers; recognise that users may retain copies and cannot be remotely controlled. Verify a reproducible previously safe commit and document affected versions. Rollback does not excuse disclosing a known security vulnerability appropriately.

## B00 repository reconciliation (implemented documentation change)

Keep `sociusflowdeveloper/Deadline-Guardian` as the exact target, maintain extracted documents at its root, retain the existing ZIP/LICENSE/.gitignore, and keep code work behind T00/T01. This records the user-authorised bootstrap scope, not acceptance of ADR-001–009. No service or paid dependency is added.
