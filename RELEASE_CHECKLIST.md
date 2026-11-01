# RELEASE_CHECKLIST.md — Pre-Repo and Release Evidence Ledger

> **Repository reconciliation, 1 November 2026 (SGT):** Distinguish public repository existence from product release approval. Existing LICENSE presence is confirmed, while rights clearance, tests, CI, compatibility and release authority remain open. See [BOOTSTRAP.md](BOOTSTRAP.md) and [DISCOVERY.md](DISCOVERY.md).

**Snapshot:** 1 November 2026 SGT | **State:** DOCUMENTS DRAFTED; BUILD AND PUBLIC RELEASE NOT APPROVED.  
`[x]` means this document exists in the **pack** (not approved, implemented or effective). `[ ]` means open. `N/A v0.1` means architecturally absent **only if the scope remains unchanged**.

## 1. Plan first

- [ ] D01–D16 grilled with stakeholders and answers accepted; discovery completed.
- [x] `SPEC.md` drafted with what, why, in/out scope and rationale.
- [x] Exact stop/done criteria documented in `SPEC.md`.
- [x] Small ticket backlog drafted in `TICKETS.md`.
- [ ] One fresh agent actually used for every implementation ticket.
- [ ] Code checked against plan after each ticket; evidence captured.
- [ ] Any scope changes approved in plan **before** implementation.

## 2. Repo documents

- [x] `SPEC.md` draft.
- [x] `SECURITY.md` draft.
- [x] `CODE_STYLE.md` draft.
- [x] `DATABASE.md` design / explicit no-database decision.
- [x] `API_GUIDE.md` proposed contracts / no HTTP endpoints.
- [x] `PRIVACY POLICY.md` **unapproved publication draft**.
- [x] `TERMS.md` **unapproved legal draft**.
- [x] `DATA.md` proposed data inventory and retention.
- [x] `IP.md` clearance plan; actual clearance **open**.
- [x] `DELETE.md` no-account deletion guidance + future account spec.
- [x] `AI_WORKING_RULES.md`, `AGENTS.md`, `TICKETS.md`, `ARCHITECTURE_DECISIONS.md`, `SOURCES.md`.
- [x] Apache-2.0 `LICENSE` exists at the inspected baseline; preserved unchanged.
- [ ] Supporting company rights/licensing approval evidence inspected.

## 3. Security gates

- [ ] No secrets in code, Git history, `.env`, client JS or CI logs **verified**.
- [ ] No real user or school data in public artefacts **verified**.
- [ ] Untrusted input and injection paths tested; zero unauthorised network or file actions.
- [ ] Input size, date/schema, path and CSV-output validation tested.
- [ ] Offline design, no telemetry and no stack traces **verified**.
- [ ] GitHub secret scanning, push protection, dependency and Actions permission settings inspected and configured where available.
- [ ] Private security reporting configured; contact fallback verified.
- [ ] Peer review and final-commit CI evidence recorded.
- **N/A v0.1:** Database credentials, API auth, server-side owner checks, RLS, admin routes, S3/Firebase/Supabase buckets and rate limits for HTTP endpoints, because **none exist**. If added, every item becomes a mandatory `[ ]` release gate before launch.

## 4. Stack and spending

- [x] Proposed architecture: `SKILL.md` + Python stdlib + GitHub, no hosted backend.
- [ ] Two named AI hosts' skill support and install pathways actually verified.
- [ ] Current provider/CI quotas, costs and paid-tier need verified; any spending explicitly approved.
- [x] Planned repo layout specified in `SPEC.md`.
- [ ] Implementation repo tree created and compared with plan.

## 5. Backend readiness

- **N/A v0.1:** Physical indexes, N+1 queries, DB pooling, SQL migrations, central backups, user auth, RLS, server routes, web app runtime and payments.
- [x] Future architecture gates for the above documented in `DATABASE.md` / `SECURITY.md`.
- [ ] DevOps: branch protection, PR checks, pinned workflows, release and rollback tested.
- [ ] Privacy/compliance: notices, company contacts, minor safeguards and processor facts approved.
- [ ] AI: prompt-injection, hallucination, source attribution and provider limitations tested.

## 6. Legal / app store

- [x] Draft privacy notice: actual behaviour must be verified before publication.
- [x] Draft terms: liability and age clauses need counsel approval.
- [x] Data schedule: proposed per-category retention; internal systems not configured.
- [ ] Trade-mark clearance on IPOS (and other relevant jurisdictions) evidenced; proposed name NOT cleared.
- [x] Delete spec: no accounts in v0.1; user-directed deletion documented.
- **N/A v0.1:** In-app account deletion (no app/account); **conditional if app/account introduced:** Apple in-app deletion and Google Play in-app + external route, if their rules apply.
- [ ] Company IP ownership and licence selection confirmed.

## 7. Before sharing a site / public documentation

- **N/A v0.1:** No website/mobile app is proposed. A GitHub README is not a deployed mobile application.
- [ ] GitHub README accessible and rendered: heading hierarchy, layout/overflow, images, links, clickable verified contacts, working installation steps.
- [ ] Search/discoverability basics: accurate description, repo topics, licence and screenshots with no misleading compatibility claims.
- [ ] Performance and demo assets compressed and accessible if added.
- [ ] Broken links checked, including privacy/security references.
- **Conditional if website built:** mobile widths, keyboard/navigation, touch controls, menus, error/success states, 404, browser compatibility, image optimisation, search metadata and performance recorded.

## 8. AI working rules

- [x] Adviser-over-yes-man principle and accuracy-first challenge prompt documented.
- [x] `CONFIRMED / INFERENCE / ASSUMPTION` tagging mandated.
- [x] Second independent agent review mandated for proactive loops.
- [x] AI text provenance and no watermark-removal evasion documented.
- [ ] Actual agent/reviewer compliance confirmed through reviewed ticket reports.

## 9. Absolute public release gates

- [ ] Discovery decision and prioritisation recorded.
- [ ] All P0/P1 tickets accepted with evidence; no open stop-ship defects.
- [ ] Real tests/CI pass on final head commit; no imaginary checks.
- [ ] Host compatibility matrix includes actually tested versions and known limits.
- [ ] IPOS and broader IP/rights checks complete; approved licence present.
- [ ] Security and privacy review, minors' risk and legal publication approval complete.
- [ ] External vulnerability reporting available; owner and rollback plan assigned.
- [ ] Authorised Managing Director decision is recorded: **GO** for exact commit, else **NO-GO**.

## Owner/decision record (empty by design)

| Item | Decision | Owner/approver | Date SGT | Evidence |
|---|---|---|---|---|
| Scope approval | PENDING | Managing Director | — | — |
| CTO security sign-off | PENDING | CTO / independent reviewer | — | — |
| DPO/privacy review | PENDING | Designated DPO (if appointed) | — | — |
| IP and legal clearance | PENDING | Company + qualified adviser | — | — |
| Public release | NO-GO pending evidence | Managing Director | — | — |
