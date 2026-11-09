# Architecture and data — Deadline Guardian

**Prepared:** 9 November 2026 (Asia/Singapore). **Organisation:** SociusFlow Pte. Ltd. **Status:** engineering documentation draft for review. Requirements below do not establish implementation, production readiness or legal approval.

## System map

| Component | Location | Data and responsibility |
| --- | --- | --- |
| Host-guided workflow | skills/academic-deadline-drift-guard/SKILL.md | User-selected host handles source interpretation; source text is untrusted |
| Canonical contracts | CONTRACT.md, schemas/ | Snapshot/result structures and invariants |
| Local helper | skills/academic-deadline-drift-guard/scripts/ | Validate before/after, deterministic comparison, optional explicit export |
| Examples/tests | examples/, tests/ | Fictional fixtures and regression/security checks |
| Security tooling | scripts/security_check.py | Scoped local checks; not compliance certification |
| User workspace | Explicit CLI --workspace | Original JSON and requested drafts under user control |

The CLI accepts --before and --after local JSON, optionally paired --output and --format. Default prints draft JSON only. Exact interface/errors are in API_GUIDE.md. No HTTP endpoint/authentication store/database/migration/hosted backup is present. DATABASE.md's hosted schema remains hypothetical and unapproved.

Snapshot source text is bounded and used to check literal excerpt consistency; this is not provenance authentication or correctness of the deadline. Result exports contain needed excerpts/references rather than full source bodies. See DATA.md for categories and lifecycle, DELETE.md for local/host copy limits.

Actual host storage region, chat retention, local disk/backups and public repository redistribution are not controlled by the helper. Future connected services require new data-flow and security decisions. Preserve the original ZIP as a historical artefact, not the current install package.
