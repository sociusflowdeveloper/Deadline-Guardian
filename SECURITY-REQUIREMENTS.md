# Security requirements — offline Deadline Guardian

**Prepared:** 9 November 2026 (Asia/Singapore). **Organisation:** SociusFlow Pte. Ltd. **Status:** engineering documentation draft for review. Requirements below do not establish implementation, production readiness or legal approval.

## Current boundary

CONFIRMED: the inspected repository contains a Python standard-library local validator/comparator/exporter and a skill package. There are no hosted HTTP endpoints, accounts, database or paid API dependencies in this approved scope. API-GUIDE.md and CONTRACT.md are canonical. Do not add fictional authentication/RLS/database gates as implemented components.

## Release gates

| Requirement | Evidence required | Owner |
| --- | --- | --- |
| No secrets or confidential fixtures | Scoped current/history/archive scan with limits recorded | Engineering |
| Safe local file access | Workspace confinement, symlink/traversal/size/overwrite/race denial | Engineering |
| Honest deadline output | Deterministic draft states, provenance/excerpt consistency, no confirmed changes | Engineering/product |
| Untrusted document handling | Prompt-injection resistance in actual supported hosts; local structured inputs validated | Engineering |
| Bounded execution and exports | Input limits, no network, safe errors, CSV formula/Markdown sanitisation | Engineering |
| Rights/privacy/age | Input rights, source/brand/licence clearance, approved notices and eligibility | Admin/privacy |
| Host support | Actual installation/invocation evidence, provider capability/retention review | Engineering |
| Recovery and release authority | User-file lifecycle explained, reviewed PR/CI and explicit product release decision | Admin |

Historical local evidence is in T02–T06 records; this documentation pass does not rerun or expand that evidence. Existing 85/100 estimate is not certification or launch approval. Requirements for a future hosted service must be separately approved and threat-modelled before code.
