# Configuration

**Status: DRAFT.** Reviewed against repository source on 12 November 2026 (Asia/Singapore). Owner approval, live configuration and operational execution are not established by this document.

The CLI uses explicit --workspace, --before, --after and optional paired --output/--format arguments. See API-GUIDE.md and CONTRACT.md. No application environment variables, secret keys, hosted database or network configuration are required. .env.example intentionally contains no assignments. Preserve fail-closed filesystem checks. Users choose an eligible AI host separately; its account/privacy settings are not controlled by this package. Never paste credentials into documentation or logs. Review configuration on provider, permission, region or integration changes.
