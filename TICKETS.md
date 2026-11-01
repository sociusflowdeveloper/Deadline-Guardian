# TICKETS.md — Single-Agent Work Packages

> **Repository reconciliation, 1 November 2026 (SGT):** B00 documentation bootstrap is in progress. T00 preparation has started with an interview kit and decision register; T00 is not passed. T01 and implementation tickets retain their dependencies. See [BOOTSTRAP.md](BOOTSTRAP.md) and [DISCOVERY.md](DISCOVERY.md).

**Status:** T00–T09 remain an unaccepted product backlog. B00 documentation bootstrap is implemented locally; T00 preparation is in progress. No product ticket is accepted, tested or closed.  
**Sequence:** T00 → T01 → T02 → T03 → T04 → T05 → T06 → T07 → T08 → T09. Parallelise only independent, read-only reviews; do not create conflicting branches.

**Universal ticket contract:** A **fresh agent** is assigned one ticket and only its exact scope. It must read `SPEC.md`, `SECURITY.md`, `CODE_STYLE.md` and `AGENTS.md`; create one PR; report changed files, exact commands/results, actual current commit and any deviations. Compare code against the plan after each ticket. Changes to requirements must go through a proposed SPEC/ADR revision approved before code. At least one *different* independent review agent inspects proactive loops; an authorised human approves merges and release. A failing or unverified check blocks completion.

| Ticket | Priority | Owner (proposed) | Dependency | Deliverable | Acceptance / done condition |
|---|---|---|---|---|---|
| T00 — Validate problem | P1 | MD + CMO | None | Five redacted user interview records, competitor update, answered D01–D16 | ≥3/5 report meaningful pain or document stop/pivot; decisions recorded |
| T01 — Freeze contract | P1 | CTO | T00 | Approved JSON schema v1, statuses, matching rules, 12+ fictional fixtures | Duplicate/ambiguous/partial/cancellation rules reviewed; no code |
| T02 — Build validator | P1 | Fresh engineering agent | T01 | Local CLI validation and schema errors | Invalid date, oversized input, paths fail closed; no network, no secrets |
| T03 — Build comparator | P1 | New engineering agent | T02 | Pure deterministic change engine | Six statuses correct on fixture set; no silent authority selection |
| T04 — Build exporter | P1 | New engineering agent | T03 | Evidence report and optional JSON/CSV/Markdown export | Explicit destination, no input overwrite, CSV formula safety, unconfirmed by default |
| T05 — Author Agent Skill | P1 | New skill agent | T04 | Canonical `SKILL.md`, instructions and fictional usage | Specification-valid metadata; safe triggers; host limitations explicit |
| T06 — Security and tests | P0 | Fresh independent security agent | T02–T05 | Threat cases, scan report, test summary | No exfiltration, secrets, hidden writes; defect severity recorded |
| T07 — IP, legal and data gate | P0 | MD + secretary + DPO/counsel as needed | T00, T05 | Rights register, IPOS search evidence, legal wording review, licence decision | No unknown rights, material compliance gaps or unapproved publicity claims |
| T08 — Manual compatibility | P1 | Separate QA agent | T05, T06 | Claude and second eligible host setup, transcripts and limitations | Real invocation checked; no fake cross-host guarantees |
| T09 — Release decision | P0 | Managing Director | T06–T08 | Release register with commit, reviewer approvals, rollback and GO/NO-GO | All stop-ship gates closed with evidence; otherwise NO-GO |

## Ticket hand-off template

```text
Ticket ID:
Agent identity/context (new for this ticket):
Approved SPEC revision and commit:
Permitted files:
Forbidden changes:
Acceptance criteria:
Actual commands, exit codes, test evidence:
Code-versus-plan differences:
Threat/data impact:
Independent reviewer / findings:
Status: PASS | FAIL | BLOCKED
Next authorised step:
```

## Definition of done for all tickets

**PASS** only if the exact acceptance tests for the ticket pass; resulting PR is reviewed; the final commit has recorded evidence; no unauthorised scope changes; all security/privacy controls remain intact. **FAIL** if a test or requirement fails. **BLOCKED** if permission, data, rights, review or environment evidence is missing. Agent must stop on PASS/FAIL/BLOCKED rather than looping on speculative improvements.

## Change request method

Raise issue with `reason`, `new requirement`, `risk`, `cost/effort`, `affected documents`, `rollback`, `decision owner`, `approval date`; update `SPEC.md` and affected documents on an authorised PR **before** implementation. Re-run impacted tests and obtain independent review. Never silently change implementation to redefine the agreed plan.

## Current work record

| Ticket | State | Evidence / remaining work |
|---|---|---|
| B00 — Extract and reconcile repository documents | IMPLEMENTED locally, review pending | Root documentation, BOOTSTRAP.md, DISCOVERY.md and CODEX_HANDOFF.md; no application code |
| T00 — Validate problem | IN PROGRESS, interview evidence absent | Interview kit and D01–D16 register prepared; five actual interviews and decision-owner answers outstanding |
| T01 — Freeze contract | BLOCKED by T00 and schema decisions | Contract conflicts documented in DISCOVERY.md; no approved schema or fixtures claimed |
| T02–T09 | BLOCKED by prerequisites | No implementation, security tests, host tests or release approval claimed |
