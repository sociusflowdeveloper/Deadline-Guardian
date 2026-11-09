# Threat model — Deadline Guardian

**Prepared:** 9 November 2026 (Asia/Singapore). **Organisation:** SociusFlow Pte. Ltd. **Status:** engineering documentation draft for review. Requirements below do not establish implementation, production readiness or legal approval.

## Assets and trust boundaries

Assets: source snapshots, evidence excerpts, draft reports, academic accuracy, local filesystem and public package integrity. Actors: legitimate student, malicious source author, compromised AI host/package, unauthorised local user and privileged OS operator. Source documents and host-generated JSON are untrusted; local deterministic validation/comparison is separate from uncertain extraction.

| Threat | Observed design/control | Residual evidence or limit | Owner / priority |
| --- | --- | --- | --- |
| Source prompt injection | Skill treats documents as data; helper consumes bounded JSON | Actual host behaviour remains unverified | Engineering P1 |
| Wrong/missing/cancelled deadline falsely confirmed | Explicit draft/conflict/unverified states, confirmed_changes empty | Literal excerpts do not prove authenticity or semantic truth | Product/engineering P1 |
| Path traversal, symlink or accidental overwrite | Workspace-bound validator/exporter and refusal of existing output | Privileged/malicious OS cannot be isolated by this tool | Engineering P1 |
| Formula/HTML/link injection in report | CSV/Markdown display sanitisation | Readers must still treat evidence as untrusted | Engineering P1 |
| Oversized resource abuse | Bounded input/schema and local execution | No server rate limiter exists or is needed in current offline scope | Engineering P2 |
| Personal data leaked in host chats/public issues | Fictional fixtures and no helper telemetry/network | Independent host retention, user backups and public copies outside helper control | Privacy/Admin P1 |
| Secret/licence/package compromise | Local security checks, no dependency service keys, unchanged Apache licence | History scans bounded; ownership/brand/host clearance remain open | Admin/engineering P1 |
| User loses or over-retains exports | Explicit local output and user-controlled deletion | No operator backup/deletion service or secure-erasure guarantee | User/privacy P2 |

Likelihood/impact are qualitative INFERENCE: misleading academic outcomes and disclosure are plausible/high-impact; local file corruption and package compromise are plausible/material. This is a source-based model, not proof of exploit or a new security audit. Refer to T06_SECURITY_REVIEW.md for historical scoped tests. Revisit on source/schema/export/host change, incidents, younger-user access, network or storage introduction.
