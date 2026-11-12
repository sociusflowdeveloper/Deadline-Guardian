# Dependencies and services

**Status: DRAFT.** Reviewed against repository source on 12 November 2026 (Asia/Singapore). Owner approval, live configuration and operational execution are not established by this document.

Application/helper and tests use Python standard library only; schemas and fixtures are JSON. GitHub Actions uses pinned checkout/setup-python actions in .github/workflows/validate.yml. The optional user-selected AI host is an external processor with separate costs, storage and eligibility, not a package dependency under SociusFlow control. Engineering owns Python/host compatibility evidence; Admin owns rights and privacy review. Replacement host requires actual invocation and data-use assessment. Do not add dependencies, network calls or paid APIs without an approved ADR.

Review lockfiles or supported Python versions, security advisories, licence/attribution and replacement cost before updates. No current provider security settings or region guarantees are asserted.
