# Version log

Maintained change history. All dates use Asia/Singapore. Prototype versions are engineering identifiers, not approved product releases. Every change-bearing PR must update this file; see AGENTS.md. Historical entries below are reconstructed from inspected Git history, not newly asserted approvals.

## T06 local package security verification — 2 November 2026

- State: scoped independent local security assessment and regression/scan artefacts on a separate stacked PR; final evidence in T06_SECURITY_REVIEW.md. No public release, platform-setting change, host certification or human approval implied.
- Changes: bounded standard-library security scan, adversarial local tests, CI invocation and reconciled release/threat records. Runtime helper version and v1 schemas are unchanged unless separately recorded corrective findings require a reviewed fix.
- Verification: actual commands/counts, independent review, findings/severity and scan scope/limits in T06_SECURITY_REVIEW.md; subsequent current-head CI results recorded in PR. No secret matches or real student records are printed into reports.
- Completeness: 85/100 after reviewed local T05/T06 evidence; unchanged rubric. Stop at this coherent milestone, exceeding requested 80/100. T00 interviews and T07–T09 remain open.
- Rollback: close PR before merge; reviewed revert of test/scan/workflow/documentation changes after authorised merge. No product data, hosting or installed personal skill to reverse.

## T05 repository skill package — 2 November 2026

- State: implemented as a repository package, stacked on T04 PR #5; final local verification and independent review in T05_VERIFICATION.md, with PR CI/authorised human approval recorded separately. No personal skill installation, actual host invocation, merge or release is asserted.
- Changes: canonical SKILL.md, minimal bundled contract/fictional-use references, explicit safe triggers/workflow/host limits and package integrity checks. Existing runtime remains 0.3.0-prototype-t04; no schema/algorithm revision or new dependency.
- Verification: T05_VERIFICATION.md records actual validation/run commands, review findings and limits. T04 CI run 41327827882 succeeded at d1a0f620f03a6b6bbaa388e3a38e9e1d9751e780; earlier preparation records are retained.
- Completeness: 75/100 after T05 local evidence/review, unchanged weights. Next ticket: T06 independent full local package security review before the 80-point target can be met. Subsequent T05 CI is recorded in its PR.
- Rollback: close this PR before merge; reviewed revert after authorised merge removes the packaging/docs/checks while retaining T04 helper. No provider installation or user data migration to reverse.

## 0.3.0-prototype-t04 — 2 November 2026 — T04

- State: implemented on a feature branch stacked on T03 PR #4. Local verification: 66 tests run, 65 passed and one inherited UNIX-socket capability skip; compile/whitespace checks passed. Independent technical review found no material defect; details in T04_VERIFICATION.md; current-head CI and human approval remain separate gates. No merge or product release is claimed.
- Changes: explicit new-file draft exports in JSON, CSV and Markdown; destination confinement, no overwrite, safe rendering and negative write tests. Stdout-only default remains available. No new dependency, network, account, automatic calendar change or confirmed deadline.
- Organisation: current README/API/ticket/data/security/deletion documentation reconciled; completeness assessed against unchanged weights at 65/100 after local checks/review, exceeding the requested 60/100 by completing the coherent T04 ticket.
- Verification: T04_VERIFICATION.md records actual commands/results, failed reproductions, capability skips and independent review. T03 PR #4 CI run 41325807541 is CONFIRMED successful at commit 8eb634b201026ecc0f5e0e19f7dcd1b7a816807e; T03 remains unmerged. Historical T03 entry/verification are retained as prepared.
- Remaining: stacked PR review/CI/merge order, T05–T09, demand interviews and rights/privacy/release clearance. Stop this implementation session at T04; next owner is a fresh T05 context after prerequisite gates.
- Rollback: close the T04 PR before merge; reviewed revert after authorised merge restores T03 stdout behaviour. Previously requested exports remain user-managed files; reverting code does not delete them or provider copies.

## 0.2.0-prototype-t03 — 2 November 2026 — T03

- State: implemented on feature branch; local verification and independent technical review recorded; PR checks tracked in T03_VERIFICATION.md. Not merged or released at preparation.
- Changes: deterministic comparator and draft JSON stdout; all six provisional statuses, frozen precedence, evidence retention, identity matching and offset-safe comparison. No file exporter or calendar writes.
- Organisation: mandatory version-log rule in AGENTS.md/CODE_STYLE.md and PR template; reconciled current README/API/ticket status; weighted product score in COMPLETENESS.md. Historical source ZIP, licence and contract semantics preserved.
- Verification: see T03_VERIFICATION.md for actual commands, results, limitations and independent review. No CI or human approval is implied by local checks.
- Remaining: T04–T09, demand interviews and release clearance. Next owner: fresh T04 engineering context after T03 prerequisite gates.
- Rollback: close this PR before merge; after authorised merge, use a reviewed revert of this change set. No stored product data or migration.

## Policy change — 2 November 2026 — PR #3

CONFIRMED Git history: merge 2ced101; source commit 5c2b372. Added LANGUAGE_POLICY.md and preferred-language/code-hygiene instructions. Documentation change; no runtime version increment inferred.

## 0.1.0-prototype-t02 — 1 November 2026 — T02 / PR #2

CONFIRMED Git history: merge f5bc17c; implementation 6c8bd58; CI action update a0c66ca. Added strict standard-library validation, confined local input reads, validation-only CLI and regression suite. Historical verification is T02_VERIFICATION.md; do not reinterpret its results as current comparator evidence.

## Planning baseline — 1 November 2026 — B00 / T00 / T01 / PR #1

CONFIRMED Git history: merge f2b2929; extracted documentation ec91efb; prototype decisions and contract 7e50349. Unzipped working documentation, adopted constrained prototype assumptions and froze schema/semantic contract. No runtime release version existed. Five interviews, IP/legal and product-release gates remained open.


## DOC-BASELINE — 9 November 2026 (SGT)

- Scope: user-requested documentation baseline; no runtime version or schema change.
- Added eight missing launch/security/product/architecture/agent/design companion files and documentation index; extended thirteen-rule security baseline, existing privacy/terms/data/deletion drafts and agent pointer without removing historical content.
- Reconciled proposed 16+ eligibility as a pending company choice (not law), category retention, offline deletion limits and separate future commercial terms.
- Verification: all eighteen required paths covered; Markdown links for new companion docs resolve to inspected tree/additions; changed files Markdown only. No runtime unittest/security scan/host tests rerun in this documentation pass; no new technical score or security certification claimed.
- Review/merge/release: draft PR for review; not approved or released. Existing rights, host, privacy, demand and release gates remain.
- Baseline: c8fe3ba8fcc869ea6b6fe362f8f4be31569381ee. Rollback: reviewed documentation revert; preserve source ZIP, LICENSE, user data and historical verification.


### Privacy contact refinement — 9 November 2026 (SGT)

**CONFIRMED — user decision, 9 November 2026 (Asia/Singapore):** the public privacy contact is pratheeksha@sociusflow.com. This confirms the selected address only. Actual mailbox monitoring, response-process readiness and formal statutory DPO appointment remain UNKNOWN and require separate evidence.
Updated draft privacy/terms/data/deletion/index contact statements only; historical records, licences and runtime remain unchanged. Verification: changed files are Markdown; confirmed address and UNKNOWN operational limitations reviewed. No email sent or mailbox/provider setting changed.


## DOC-BASELINE-2026-11-12 — 12 November 2026 SGT

Documentation adoption only: populated trigger profile; canonical API/style/privacy/terms/architecture names with compatibility pointers; register and operational/privacy/rights requirements. Python helper, contracts, historical evidence, skill package, original ZIP and Apache licence unchanged. Verification: exact commands/results belong to this PR; no deployment or host invocation is asserted here. Current product NO-GO and score remain unchanged. Rollback: reviewed revert, no migration.

### DOC-BASELINE verification evidence

On 12 November 2026 SGT the local Python suite ran 76 tests successfully (one history test skipped without local Git). Initial PR CI passed all 76 tests, security scan and compilation on Python 3.11/3.13, then failed only on copied Markdown trailing spaces; those spaces were removed, preserving CI. Candidate d1d9b4b6bc91bf83ccf8f45411c341d4783e2d5a passed both validation jobs in Actions run 43170825169. Independent integration-agent review inspected the documentation/file inventory and accepted scope. Any later candidate still requires fresh CI before merge. Host/privacy/rights/release gates remain open; no installation or product release occurred.
