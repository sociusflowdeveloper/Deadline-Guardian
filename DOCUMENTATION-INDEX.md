# Documentation index and refinement decisions

**Prepared:** 9 November 2026 (Asia/Singapore). **Organisation:** SociusFlow Pte. Ltd. **Status:** engineering documentation draft for review. Requirements below do not establish implementation, production readiness or legal approval.

**Source baseline:** c8fe3ba8fcc869ea6b6fe362f8f4be31569381ee. Existing detailed documents remain canonical; this pass fills missing companion documents rather than replacing their history.

- [SPEC.md](SPEC.md)
- [SECURITY.md](SECURITY.md)
- [CODE_STYLE.md](CODE_STYLE.md)
- [DATABASE.md](DATABASE.md)
- [API_GUIDE.md](API_GUIDE.md)
- [SECURITY-REQUIREMENTS.md](SECURITY-REQUIREMENTS.md)
- [THREAT-MODEL.md](THREAT-MODEL.md)
- [SECURITY-ARCHITECTURE.md](SECURITY-ARCHITECTURE.md)
- [SECURITY-CHECKLIST.md](SECURITY-CHECKLIST.md)
- [PRIVACY POLICY.md](PRIVACY%20POLICY.md)
- [TERMS.md](TERMS.md)
- [DATA.md](DATA.md)
- [IP.md](IP.md)
- [DELETE.md](DELETE.md)
- [PRD.md](PRD.md)
- [ARCHITECTURE-AND-DATA.md](ARCHITECTURE-AND-DATA.md)
- [AI-AGENT-INSTRUCTIONS.md](AI-AGENT-INSTRUCTIONS.md)
- [DESIGN-SYSTEM.md](DESIGN-SYSTEM.md)

## Open decisions

PROPOSAL: 16+ eligibility is a company product choice, not a statutory threshold. Existing SPEC initial 18+ user research remains intact pending explicit reconciliation. Younger users require a separate decision/safeguards. DATA.md is canonical for proposed retention: user-controlled local files remain until users delete them; optional future support correspondence target 12 months after closure, unapproved and not evidence support data is currently collected. No remote account deletion, operator backup or provider erasure promise is made.

App subscription terms must remain separate from website/AI administrative service schedules. This package has no paid API/billing or verified sale readiness. Source licence remains unchanged; rights/host/privacy/release gates remain open.

## Review and status

Owner: Admin for age/commercial/rights; engineering for local/host evidence; designated privacy reviewer for notices/retention. Documents are draft or scoped engineering requirements, never certification. Update affected contracts/threat/data/design docs before behaviour changes. Revert documentation through a reviewed PR without touching original ZIP, LICENSE, user files or historical verification.
