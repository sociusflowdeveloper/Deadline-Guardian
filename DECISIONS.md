# T00 and T01 decision record

**Record:** DG-DEC-001. **Date:** 1 November 2026 (Asia/Singapore).
**Business owner:** Managing Director. **Decision preparer:** engineering assistant acting under the user's instruction.

## Authority and exact disposition

**CONFIRMED:** The user instructed: “Just do. and just work the T00 discovery decisions and T01 schema approval here.” This authorises the assistant to resolve the bounded prototype choices and schema in this session; it does not evidence interviews, a signed founder resolution, rights clearance, merge authority or a product launch decision.

**Decision:** Proceed to an offline, fictional-data prototype. Adopt the D01–D16 treatments below as engineering decisions under that instruction. Record demand and differentiation as unvalidated assumptions. T00's original five-interview requirement is moved from a prerequisite to coding to a prerequisite for wider investment and public product launch. This is an explicit scope revision, not a claim the interviews happened or T00 empirical validation passed.

**T01:** Adopt the canonical contract in [CONTRACT.md](CONTRACT.md) and the two versioned schema files for prototype implementation. Independent review and the stated subset structural/semantic fixture checks have passed; T01_VERIFICATION.md records technical acceptance and its limits. Full JSON Schema library/metaschema validation has not been executed. Application implementation, runtime safety and host compatibility are separate later tickets.

## D01–D16 adopted treatments

| ID | Engineering decision | Evidence classification / residual gate |
|---|---|---|
| D01 | Build a narrow prototype without waiting for interviews; do not claim validated demand. Require five adult-student interviews before wider investment/product launch. | ASSUMPTION: meaningful pain exists. Interview records: none. Review if fewer than three of five report a recent meaningful problem. |
| D02 | Test the value of an evidence-linked old/new report with unresolved states rather than generic extraction. | INFERENCE from adjacent projects, not proven willingness to use or pay. User comparison against current workaround remains open. |
| D03 | Do not rank lecturers, LMS, email, timestamps or PDFs as authoritative. Preserve all candidates; a user assertion is not authentication. | Adopted safety boundary. Conflicting candidate dates remain unresolved. |
| D04 | Missing records never prove cancellation, even in a declared complete snapshot. REMOVED requires an explicit cancellation record and cited text. | Adopted conservative boundary. |
| D05 | Preserve date-only precision. Exact minutes use stated numeric UTC offsets; absent offset means UNVERIFIED. No SGT, IANA/DST or ambiguous-date inference. | Adopted v1 contract restriction; broader timezone support needs a versioned change. |
| D06 | Helper accepts two schema-valid JSON snapshots with source text and literal excerpts. Host-assisted extraction from pasted text is separate and untrusted. | Adopted minimum executable seam. PDF/OCR and automatic extraction are outside helper scope. |
| D07 | Draft report only. No calendar sync, calendar writes, confirmation API or final confirmed export in v0.1. | Adopted safety/scope boundary. |
| D08 | Python 3.11+ CLI is the first implementation target. Later test Claude and one eligible second host separately; do not promise either now. | Runtime chosen; host eligibility and actual installation remain UNKNOWN. |
| D09 | Fictional fixtures only for engineering; opt-in adult research later, non-identifying summaries only in the public repository. | No student records, minor testing or outreach authorised by this decision. |
| D10 | Strict schemas plus semantic validation, deterministic precedence, source excerpts and no automatic application. Any ambiguous item remains UNVERIFIED or CONFLICT. | Contract controls adopted; implementation safety must still be tested. |
| D11 | No accounts, database, telemetry, network calls, backend or operator-controlled history. | Adopted architecture. User-selected host processing remains separate and may be remote. |
| D12 | Preserve existing Apache-2.0 LICENSE unchanged. Use only newly authored contract material and fictional fixtures here; do not assert existing company ownership has been verified. | Rights evidence UNKNOWN; unresolved rights continue to block a product release. |
| D13 | Deadline Guardian / Academic Deadline Drift Guard remain working names. No domain purchase or clearance claim. | Official trade-mark clearance UNKNOWN; public product branding remains gated. |
| D14 | User deletes local artefacts and uses the chosen host's controls separately. No secure-erasure or host deletion promise. | Adopted honest deletion boundary; actual host-specific instructions require later verification. |
| D15 | No paid services, new subscriptions, infrastructure commitments or model API calls. | No new spend authorised. Existing host/CI eligibility and costs not verified. |
| D16 | MD retains the product-release decision after independent security, privacy, rights, host and test evidence. | Prototype authorisation only. No product release approval. |

## Current primary competitor evidence

README content reviewed on 1 November 2026 (SGT), not installed or runtime-tested:

| Source | Observed documented scope | Decision implication |
|---|---|---|
| [wyc79/calendar-creator-skill](https://github.com/wyc79/calendar-creator-skill) | Syllabus/screenshot inputs, calendar output and editable JSON regeneration | Changed schedules alone are not a unique proposition. |
| [Dsmx1119/Syllabus-Extractor](https://github.com/Dsmx1119/Syllabus-Extractor) | PDF extraction, review/edit and calendar export using a local model pipeline | Extraction plus human review already exists. |
| [ZKey-Taken/syllabus-to-calendar](https://github.com/ZKey-Taken/syllabus-to-calendar) | Syllabus extraction, calendar view and optional calendar integration | Direct calendar integration is adjacent, with unnecessary scope for this prototype. |

**INFERENCE:** A deterministic, evidence-linked conflict report is a testable design hypothesis. This bounded review proves neither global novelty nor market demand. No competitor code, prompt, fixture or branding was copied.

## Owners, next actions and review triggers

- Engineering: freeze T01 schemas and fixtures, record independent review, then hand T02 to a fresh ticket-limited implementation context.
- CMO: proposed owner of five adult-student interviews before wider investment/public product launch. No message or assignment has been sent.
- MD/secretariat: retain rights, naming, release and expenditure decisions; no approval inferred from the existing public repository.
- Stop/review on any falsely authoritative deadline, ambiguity being silently resolved, network or secret access, real personal data in fixtures, or contract change. Interview evidence failing the threshold triggers reconsideration before further investment.

**Rollback:** Revert the decision/schema PR through review to the last recorded contract; no production data or service is affected. Do not rewrite history or delete the existing licence/archive.
