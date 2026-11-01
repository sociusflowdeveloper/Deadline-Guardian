# T00 discovery and T01 decision pack

**State:** IN PROGRESS, not accepted. **Date:** 1 November 2026 (SGT).
**Owner:** Managing Director for decisions; CMO for research; CTO for contract review.

This is preparation for T00, not five completed interviews or schema approval. No real student data is needed in repository records. Use anonymous participant codes and summarised opt-in responses; never upload actual briefs or contact details.

## Five-user interview kit

Ask five consenting tertiary students aged 18 or over:

1. In the last term, when did an assessment deadline change or conflict with another notice?
2. How did you notice it, and what practical consequence did it cause?
3. How do you currently check which notice to trust?
4. Would an old-versus-new evidence table help beyond your current workflow? Explain using a fictional example.
5. Would you use pasted text and a local JSON helper without calendar sync? What would prevent you?

| Participant | Recent meaningful example (redacted) | Existing workaround | Added value demonstrated | Local workflow acceptable | State |
|---|---|---|---|---|---|
| P01 | Not collected | Unknown | Unknown | Unknown | OPEN |
| P02 | Not collected | Unknown | Unknown | Unknown | OPEN |
| P03 | Not collected | Unknown | Unknown | Unknown | OPEN |
| P04 | Not collected | Unknown | Unknown | Unknown | OPEN |
| P05 | Not collected | Unknown | Unknown | Unknown | OPEN |

Existing acceptance criterion: at least three of five report meaningful pain, otherwise document stop/pivot. A hypothetical response or another agent's opinion cannot count as an interview. No unsolicited outreach is authorised by preparing this kit.

## D01–D16 decision register

All recommended answers below are PROPOSALS. Acceptance requires a dated decision-owner record; blanks do not imply approval.

| ID | Proposed treatment | Required evidence / decision | Current state |
|---|---|---|---|
| D01 | Validate recent deadline changes | Five interviews, at least three meaningful cases | UNKNOWN |
| D02 | Test value of evidence-linked deterministic comparison | User evaluation against current workaround | UNKNOWN |
| D03 | Never infer source authority | MD accepts user-verified authority only | PENDING |
| D04 | Missing item never means cancellation | MD accepts explicit cancellation only | PENDING |
| D05 | Preserve stated timezone; absent means unknown | CTO specifies date-only/offset semantics | PENDING |
| D06 | Two pasted texts or schema-valid JSON | MD accepts constrained input workflow | PENDING |
| D07 | No calendar sync | MD accepts local draft report only | PENDING |
| D08 | Python CLI first; hosts tested later | MD selects actual target host(s) and access | PENDING |
| D09 | Fictional fixtures; adult initial testing | Privacy owner reviews any personal-data research | PENDING |
| D10 | Fail closed on ambiguity or unsupported evidence | CTO defines cases and reviewed fixtures | PENDING |
| D11 | No hosted storage or telemetry | MD accepts no-backend boundary | PENDING |
| D12 | Preserve existing Apache-2.0 text | MD supplies ownership and licensing evidence | UNKNOWN |
| D13 | Working name only | Record actual similar-mark searches and analysis | UNKNOWN |
| D14 | User controls local and host deletion separately | MD accepts honest scope; provider facts verified later | PENDING |
| D15 | No paid service or new spending | MD accepts zero new infrastructure commitment | PENDING |
| D16 | MD decides release after independent evidence review | Dated exact-version release decision | PENDING |

Decision record template: ID; accepted/rejected/revised answer; evidence; approver; date SGT; affected SPEC/ADR revision. Discovery evidence and release authority remain separate. Any explicit acceptance of unvalidated assumptions must be recorded as such and must not be reported as validated demand.

## Contract conflicts to resolve in T01

| Topic | Existing conflict or omission | Proposed resolution for CTO/MD review |
|---|---|---|
| Record identity | DATABASE says IDs are unique but permits repeated candidate identities | Match by `(module_id, item_id)`; permit different-source candidates, reject exact duplicate identity/source pairs |
| Date fields | PRODUCT_DESCRIPTION uses `due_at`; API_GUIDE uses split date/time/timezone | One canonical split-field snapshot schema; define derived output independently |
| Time precision | SPEC example has seconds; minute-precision input and IANA support are underspecified | Freeze precision and accepted offset syntax before coding; no silent DST or timezone guessing |
| Cancellation | Cancellation records currently appear to require an active due date | Define nullability and cancellation evidence rules explicitly |
| Evidence verification | Excerpts exist without canonical source body or offsets | Specify what can actually be validated; an asserted quote is not authenticated source evidence |
| Uncertainty | Invalid input rejection versus UNVERIFIED record is unclear | Distinguish malformed schema from permitted missing precision/unknown fields |
| Export confirmation | Product narrative suggests reviewed final exports; API keeps confirmed changes empty | v0.1 produces drafts only unless a separate confirmation contract is approved |
| Missing prior record | Partial versus complete snapshot removal not fully specified | Missing is UNVERIFIED in either scope unless explicit cancellation evidence exists |
| Paths | Explicit path selection versus workspace isolation lacks a root contract | Require a documented workspace root and safe no-overwrite rules; specify symlink handling |

T01 deliverables after decisions: reviewed schema, status decision table and at least 12 fictional fixtures covering all six statuses, contradictory candidates, partial absence, invalid dates, ambiguous timezone, duplicated identity, cancellation and hostile source text. These are requirements, not created fixtures or passing tests.

## Next acceptance boundary

Before T02: record T00 outcome, accepted D01–D16 answers or explicitly accepted assumptions, approved T01 schema/version and one authorised ticket. Review T00 when actual interview records or a recorded management decision arrive. No deadline for participants or founder assignment has been communicated by this document.
