# Bounded Codex execution prompt

> **Current decision, 1 November 2026 (SGT):** The user has authorised resolving T00 discovery decisions and T01 schema here. Proceed with an offline fictional-data prototype under recorded, unvalidated-demand assumptions. The five interviews are a wider-investment/product-launch gate. Canonical T01 artefacts replace earlier illustrative contracts; application execution and product release remain separate gates. See [DECISIONS.md](DECISIONS.md) and [CONTRACT.md](CONTRACT.md).

**State:** Prepared hand-off, not an executed implementation. **Target:** `sociusflowdeveloper/Deadline-Guardian` only.

Use this prompt for a fresh coding session. Python standard-library implementation is suitable for Codex with low-to-medium reasoning using DG-DEC-001 and the accepted T01 contract. Do not interpret this hand-off as a change to repository approval gates.

```text
Work only in sociusflowdeveloper/Deadline-Guardian. Use British English and Asia/Singapore timestamps. Read AGENTS.md, SPEC.md, SECURITY.md, CODE-STYLE.md, DATABASE.md, API-GUIDE.md, DATA.md, TICKETS.md, AI_WORKING_RULES.md, DISCOVERY.md and BOOTSTRAP.md before editing.

1. Inspect status, current default-branch SHA, applicable instructions and open PRs. Preserve unrelated work, the historical ZIP, existing LICENSE and existing .gitignore rules. Work through a feature branch and PR, without direct main pushes, force pushes, branch deletion, merging or deployment.
2. Read DG-DEC-001 in DECISIONS.md. T00 prototype decisions are adopted with unvalidated-demand assumptions; five interviews remain a wider-investment/product-launch gate, not a T02 prerequisite. Confirm the actual T01 independent review/check record. Do not invent interviews, ownership or release approval.
3. CONTRACT.md and schemas/ are the canonical T01 contract; examples/contract-cases.json supplies fictional acceptance expectations. Preserve these decisions and work exactly one implementation ticket in each fresh context/branch/PR. Any change requires an explicit versioned contract revision.
4. For an authorised T02 session only: implement strict offline JSON validation using Python 3.11+ standard library. Enforce the approved exact field sets, input byte/count/excerpt limits, actual date validity, record/source references, identity rules and workspace path contract. Reject unknown versions and unsafe paths. Do not add comparison/export features from later tickets.
5. Derive meaningful tests from the approved contract. Demonstrate invalid inputs fail for the expected reason and produce only non-sensitive error categories/field paths. No raw input or stack traces in user-facing errors. Source text remains data; no eval, shell execution, HTTP, credentials, model APIs, remote integrations, telemetry, backend or spending.
6. Run focused tests, unittest discovery, compile checks and git diff --check as appropriate. Record commands, exit status and actual results against the reviewed head. Do not create fake green CI or compatibility claims.
7. Obtain a different agent's review with the exact requirements and diff. Resolve material findings, inspect the integrated change and rerun affected checks. Human approval and required checks still govern merge/release.
8. Update documentation with implemented behaviour and actual evidence. Return ticket ID, approved spec/schema revision, files, actual SHA if available, tests, independent findings, remaining gates and rollback. Stop on PASS/FAIL/BLOCKED for that ticket. Never claim secure, legally cleared, multi-host supported, deployed or complete without evidence.
```

T03 comparator, T04 exporter and T05 skill authoring require their own later sessions and prerequisites. No custom skill is created or installed by this bootstrap.

## Historical hand-off after T02

T02 now has implemented input validation and its own verification record. The T02 prompt above is retained for traceability, not a direction to rebuild completed code. The next fresh implementation context is T03 only: deterministic comparison against CONTRACT.md and the expected six-status fixtures, preserving validation/path controls and draft-only output. Do not add exports, a SKILL.md, network access or calendar writes in T03.

## Historical hand-off after T03 implementation

T03 now provides deterministic comparison and draft JSON stdout on this branch. Use VERSION_LOG.md, COMPLETENESS.md and T03_VERIFICATION.md for current state; the earlier T02/T03 prompts above are historical. The next implementation ticket is T04, in a fresh context after T03 review/CI and authorised merge gates. Preserve contract v1.0. Implement explicit safe draft export only; test exclusive writes, workspace confinement, no input overwrite, formula-safe CSV and escaped Markdown. Update VERSION_LOG.md in the same PR and revise completeness only from evidence. Do not add SKILL.md, integrations or release claims.

## Historical hand-off after T04 implementation

T04 adds explicit local draft JSON/CSV/Markdown exports; VERSION_LOG.md and T04_VERIFICATION.md hold current evidence. T03 PR #4 CI succeeded and remains unmerged; review stacked changes separately and integrate in dependency order. Stop this session at the completed T04 implementation. The next coding ticket is T05 in a fresh context after prerequisite review/CI gates: canonical SKILL.md, safe triggers, fictional usage and honest host limitations. Use the skill-creator workflow before writing any skill. Do not claim host compatibility without actual T08 invocation evidence or release without T09 approval. Keep the version log and current scorecard updated in every change-bearing PR.

## Historical hand-off after T05 implementation

T05 adds the canonical repository skill and local packaging evidence; it does not install the skill into a personal profile or establish Claude/second-host compatibility. Read T05_VERIFICATION.md and the version log. The next fresh ticket is T06: independent security/threat checks for all local helper and skill surfaces, recorded scan limits, adversarial tests and a review report. No new host integration, account, network capability or release is authorised. Keep T07 rights/legal, T08 actual hosts and T09 release separate.

## Current hand-off after T06 local evidence

Stop this implementation session after the reviewed local package security milestone. Use T06_SECURITY_REVIEW.md for scope, actual results, findings and residual risks; use the stacked PRs for exact-commit CI. Do not turn a local technical assessment into host certification or release approval. The next required owners are MD/CMO for five adult-user interviews, MD/secretariat/DPO or qualified adviser for T07 rights/privacy clearance, separate authorised QA for real T08 host invocation, and MD for T09 exact-commit release decision. No person was appointed or approval manufactured by this hand-off. Merge dependency order and passing checks remain required.
