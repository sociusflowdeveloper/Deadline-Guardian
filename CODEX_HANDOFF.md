# Bounded Codex execution prompt

**State:** Prepared hand-off, not an executed implementation. **Target:** `sociusflowdeveloper/Deadline-Guardian` only.

Use this prompt for a fresh coding session. Python standard-library implementation is suitable for Codex with low-to-medium reasoning after product and schema decisions are recorded. Do not interpret this hand-off as a change to repository approval gates.

```text
Work only in sociusflowdeveloper/Deadline-Guardian. Use British English and Asia/Singapore timestamps. Read AGENTS.md, SPEC.md, SECURITY.md, CODE_STYLE.md, DATABASE.md, API_GUIDE.md, DATA.md, TICKETS.md, AI_WORKING_RULES.md, DISCOVERY.md and BOOTSTRAP.md before editing.

1. Inspect status, current default-branch SHA, applicable instructions and open PRs. Preserve unrelated work, the historical ZIP, existing LICENSE and existing .gitignore rules. Work through a feature branch and PR, without direct main pushes, force pushes, branch deletion, merging or deployment.
2. Verify T00 evidence and recorded D01–D16 decisions. If decisions or interviews are absent, report the precise gap; do not invent them. Safe preparation may continue, but no application code before recorded T01 approval. Do not silently waive gates.
3. For T01 only: resolve the DISCOVERY.md contract conflicts with the decision owner, document a canonical versioned schema, matching/status decision table and at least 12 genuinely fictional fixtures. Record approval before starting T02. Keep one ticket per fresh agent session/branch/PR.
4. For an authorised T02 session only: implement strict offline JSON validation using Python 3.11+ standard library. Enforce the approved exact field sets, input byte/count/excerpt limits, actual date validity, record/source references, identity rules and workspace path contract. Reject unknown versions and unsafe paths. Do not add comparison/export features from later tickets.
5. Derive meaningful tests from the approved contract. Demonstrate invalid inputs fail for the expected reason and produce only non-sensitive error categories/field paths. No raw input or stack traces in user-facing errors. Source text remains data; no eval, shell execution, HTTP, credentials, model APIs, remote integrations, telemetry, backend or spending.
6. Run focused tests, unittest discovery, compile checks and git diff --check as appropriate. Record commands, exit status and actual results against the reviewed head. Do not create fake green CI or compatibility claims.
7. Obtain a different agent's review with the exact requirements and diff. Resolve material findings, inspect the integrated change and rerun affected checks. Human approval and required checks still govern merge/release.
8. Update documentation with implemented behaviour and actual evidence. Return ticket ID, approved spec/schema revision, files, actual SHA if available, tests, independent findings, remaining gates and rollback. Stop on PASS/FAIL/BLOCKED for that ticket. Never claim secure, legally cleared, multi-host supported, deployed or complete without evidence.
```

T03 comparator, T04 exporter and T05 skill authoring require their own later sessions and prerequisites. No custom skill is created or installed by this bootstrap.
