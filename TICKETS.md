# TICKETS.md — Single-Agent Work Packages

> **Current decision, 1 November 2026 (SGT):** The user has authorised resolving T00 discovery decisions and T01 schema here. Proceed with an offline fictional-data prototype under recorded, unvalidated-demand assumptions. The five interviews are a wider-investment/product-launch gate. Canonical T01 artefacts replace earlier illustrative contracts; application execution and product release remain separate gates. See [DECISIONS.md](DECISIONS.md) and [CONTRACT.md](CONTRACT.md).


**Status:** B00 and T00/T01 documentation merged through PR #1 at f2b2929f8c11b9c8d6dcef91987cf92d5a7e3226. T00 prototype choices are adopted under DG-DEC-001; interview validation remains open. T01 contract artefacts are technically accepted after independent review; see T01_VERIFICATION.md. T03 comparator and T04 draft exporters are implemented on this branch; product release remains pending.
**Sequence:** T00 → T01 → T02 → T03 → T04 → T05 → T06 → T07 → T08 → T09. Parallelise only independent, read-only reviews; do not create conflicting branches.

**Universal ticket contract:** A **fresh agent** is assigned one ticket and only its exact scope. It must read `SPEC.md`, `SECURITY.md`, `CODE_STYLE.md` and `AGENTS.md`; create one PR; report changed files, exact commands/results, actual current commit and any deviations. Compare code against the plan after each ticket. Changes to requirements must go through a proposed SPEC/ADR revision approved before code. At least one *different* independent review agent inspects proactive loops; an authorised human approves merges and release. A failing or unverified check blocks completion.

| Ticket | Priority | Owner (proposed) | Dependency | Deliverable | Acceptance / done condition |
|---|---|---|---|---|---|
| T00 — Validate problem | P1 | MD + CMO | None | Recorded D01–D16 prototype decisions and competitor update; five interviews retained for wider investment/launch | Prototype decision adopted under explicit unvalidated assumptions; empirical validation separately OPEN |
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
| B00 — Extract and reconcile repository documents | MERGED and documentation verified via PR #1 | Root documentation, BOOTSTRAP.md, DISCOVERY.md and CODEX_HANDOFF.md; no application code |
| T00 — Prototype decision | Adopted under DG-DEC-001; empirical validation OPEN | D01–D16 resolved; three primary competitor READMEs checked; interviews not performed |
| T01 — Freeze contract | Technically accepted for constrained prototype; PR merge pending | Canonical semantics, two schemas and fictional cases; no application execution claimed |
| T02 | IMPLEMENTED; independent review and CI evidence recorded with its PR | Strict validator, workspace confinement, tests and safe CLI; see T02_VERIFICATION.md |
| T03 | IMPLEMENTED; PR #4 CI successful; human merge gate pending | Run 41325807541 for 8eb634b201026ecc0f5e0e19f7dcd1b7a816807e; see T03_VERIFICATION.md |
| T04 | IMPLEMENTED on stacked feature branch; PR checks/approval pending | See T04_VERIFICATION.md for local tests, independent review and limits |
| T05–T09 | Pending dependency and release gates | Skill package, full security/IP/host checks and release decision remain open |
