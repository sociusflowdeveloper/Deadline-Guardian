# Security checklist — each package release

**Prepared:** 9 November 2026 (Asia/Singapore). **Organisation:** SociusFlow Pte. Ltd. **Status:** engineering documentation draft for review. Requirements below do not establish implementation, production readiness or legal approval.

Record candidate SHA/version, environment, operator/reviewer, date SGT and evidence. Unknown is not PASS; N/A needs a reason.

- [ ] SPEC/CONTRACT/API/schema and bundled reference parity checked.
- [ ] Only approved Python standard-library/offline scope; no new network, credentials, database or remote writes.
- [ ] Current/staged/history/archive secret and confidential-data review recorded with scan limits.
- [ ] unittest and scripts/security_check.py commands from repository guidance run on candidate; results and failures recorded.
- [ ] Path/size/symlink/overwrite/race/error/export negative cases remain covered.
- [ ] Draft states, provenance, conflicts and no-confirmed-change guarantees verified.
- [ ] CSV/Markdown rendering remains safe; raw evidence is never treated as instructions.
- [ ] Actual supported host installation/invocation and prompt-injection limitations reviewed.
- [ ] Rights/brand/licences, privacy notice and age eligibility decisions recorded.
- [ ] User-controlled local deletion, host retention and any support-data retention explained.
- [ ] VERSION_LOG.md and COMPLETENESS.md updated with actual evidence; independent review and required CI satisfied.
- [ ] Explicit authorised product-release decision, supported version and rollback recorded.

This PR does not mark gates passed or perform a package/product release. No deploy exists in the current offline architecture. A future hosted deployment requires a separate deployment checklist. Rollback code through a reviewed PR; never delete user files automatically.
