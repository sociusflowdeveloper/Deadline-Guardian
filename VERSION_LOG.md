# Version log

Maintained change history. All dates use Asia/Singapore. Prototype versions are engineering identifiers, not approved product releases. Every change-bearing PR must update this file; see AGENTS.md. Historical entries below are reconstructed from inspected Git history, not newly asserted approvals.

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
