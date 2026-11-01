# Bounded Codex execution prompt

> **Current decision, 1 November 2026 (SGT):** The user has authorised resolving T00 discovery decisions and T01 schema here. Proceed with an offline fictional-data prototype under recorded, unvalidated-demand assumptions. The five interviews are a wider-investment/product-launch gate. Canonical T01 artefacts replace earlier illustrative contracts; application execution and product release remain separate gates. See [DECISIONS.md](DECISIONS.md) and [CONTRACT.md](CONTRACT.md).

**State:** Prepared hand-off, not an executed implementation. **Target:** `sociusflowdeveloper/Deadline-Guardian` only.

Use this prompt for a fresh coding session. Python standard-library implementation is suitable for Codex with low-to-medium reasoning using DG-DEC-001 and the accepted T01 contract. Do not interpret this hand-off as a change to repository approval gates.

```text
Work only in sociusflowdeveloper/Deadline-Guardian. Use British English and Asia/Singapore timestamps. Read AGENTS.md, SPEC.md, SECURITY.md, CODE_STYLE.md, DATABASE.md, API_GUIDE.md, DATA.md, TICKETS.md, AI_WORKING_RULES.md, DISCOVERY.md and BOOTSTRAP.md before editing.

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
