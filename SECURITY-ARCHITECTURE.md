# Security architecture — offline package

**Prepared:** 9 November 2026 (Asia/Singapore). **Organisation:** SociusFlow Pte. Ltd. **Status:** engineering documentation draft for review. Requirements below do not establish implementation, production readiness or legal approval.

## Components and boundary

User-selected academic sources -> independently chosen AI host extraction -> user-supplied local JSON snapshots -> validator.py -> comparator.py -> draft stdout or explicitly requested exporter.py output. reconcile.py coordinates the bounded local CLI. The skill instructions and bundled references guide the host but do not grant OS isolation or authenticate academic truth.

No HTTP API, company accounts, company-hosted database, credential store, telemetry, calendar mutation or network integration is part of the inspected scope. Native server authentication/RLS is therefore N/A to this current package, with explicit reassessment required if hosting is introduced.

## Control placement

- validator.py: schema/semantic validation, bounded inputs and safe workspace/path access.
- comparator.py: deterministic draft differences with unresolved states retained.
- exporter.py: explicit new output, no input overwrite, safe representations and staging cleanup attempts.
- reconcile.py: fixed redacted error categories and exit codes 0/2/3/4; no silent confirmation or background file write.
- schemas/ and CONTRACT.md: frozen data contracts; skill references must remain in parity.
- GitHub/CI: fictional fixtures, review and local security verification; public visibility does not prove publication clearance.

## Uncontrolled external systems

AI-provider chat/upload retention, host execution privileges, local disk encryption, synchronised backups and user sharing are outside this helper's direct enforcement. Document provider-specific settings only after actual verification. No promise of provider deletion, protected host installation or secure erasure is made.

## Recovery and future changes

Preserve user originals; reports are drafts, not backups of every input. Code rollback does not delete saved reports. Any hosted account, database, remote write, billing or personal-data collection needs new scope/ADR, least-privilege auth, server-side checks, RLS/equivalent isolation, quotas, migration/restore/deletion design and separate release approval.
