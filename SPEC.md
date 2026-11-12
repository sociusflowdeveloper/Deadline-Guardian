# SPEC.md — Academic Deadline Drift Guard

> **Current decision, 1 November 2026 (SGT):** The user has authorised resolving T00 discovery decisions and T01 schema here. Proceed with an offline fictional-data prototype under recorded, unvalidated-demand assumptions. The five interviews are a wider-investment/product-launch gate. Canonical T01 artefacts replace earlier illustrative contracts; application execution and product release remain separate gates. See [DECISIONS.md](DECISIONS.md) and [CONTRACT.md](CONTRACT.md).


**Document ID:** ADDG-SPEC-001
**Version:** 0.2.0-prototype-contract | **Date:** 1 November 2026, SGT
**Classification:** Prototype engineering decisions adopted under user direction; empirical demand, comparator/export execution, host tests and product release remain unverified; T02 validator evidence is recorded separately
**Proposed sponsor:** SociusFlow Pte. Ltd. | **Decision owner:** Managing Director | **Technical owner:** CTO
**Decision:** GO for the constrained offline fictional-data prototype under DG-DEC-001; **NO-GO for public release** until the listed gates are evidenced.

## 1. Problem, user and outcome

**Problem.** A student has an old assessment brief and a newer announcement. A calendar may still show the old deadline, or two notices may disagree. Existing extraction-to-calendar tools do not always show the provenance, distinguish a missing item from a cancellation or require resolution before applying changes.

**Primary user.** A tertiary student comparing course instructions the student is authorised to use. Initial user testing should prioritise people aged 18 or over. Use by or involving minors requires the safeguards in `PRIVACY-POLICY.md` and a new age-risk review.

**Job to be done.** Given two snapshots or a prior record and new notice, produce an evidence-linked list of added, changed, explicitly cancelled, conflicting and unresolved deadlines, without writing to calendars automatically.

**Value proposition.** “Find what changed in your academic deadlines, see the evidence and confirm before changing your plan.”

**Differentiation status:** INFERENCE, not proof of invention or market demand. Competing calendar extraction and scheduling tools exist. Do not claim first-to-market or unique worldwide.

## 2. Discovery questions that must be grilled before code

The original questions below are retained for traceability. Adopted engineering treatments and their assumptions are recorded in DECISIONS.md (DG-DEC-001), pursuant to the user instruction to resolve them here. Five interviews are not a prerequisite to prototype coding under this revision, but remain a wider-investment/product-launch gate. No empirical answer is invented.

| ID | Challenging question | Provisional assumption | What would change the decision? |
|---|---|---|---|
| D01 | Do students actually receive contradictory or revised dates often enough? | UNKNOWN; five target-user interviews proposed | Fewer than three of five report a recent, meaningful problem: reconsider concept |
| D02 | Why would students choose this over an ordinary AI chat? | Provenance, deterministic diffs, explicit unresolved state | If users cannot identify material extra value, stop |
| D03 | Which source is authoritative: lecturer, LMS, email, PDF? | The skill cannot decide without user-supplied policy/verification | Any design that infers source priority silently is rejected |
| D04 | Can a partial page prove an assessment was removed? | No | Only explicit cancellation may produce REMOVED |
| D05 | What about different schools/timezones? | Preserve stated timezone; otherwise UNKNOWN | Any default timezone applied without evidence is rejected |
| D06 | What is the smallest usable input? | Two pasted texts or JSON snapshots | If screenshots/PDF are essential, update feasibility assessment |
| D07 | Is direct calendar sync required for usefulness? | Not in v0.1; export proposal only | If required, re-scope and separately approve credentials/security |
| D08 | What platform must actually work first? | Claude plus a second compatible host | Confirm actual supported host, subscription and install path |
| D09 | Can documents contain other students' personal data? | Yes; minimise and redact, synthetic fixtures only | If routine identifiable minors' data is required, pause for formal review |
| D10 | How will we prevent wrong deadline substitutions? | Evidence references, no silent changes, fail closed | If error rate is unacceptable, do not release |
| D11 | Can we operate without database, analytics or hosted backend? | Yes, local helper plus host-managed prompting | New central storage requires architecture and privacy review |
| D12 | Who holds copyright and approves public use? | Company ownership/permissions not yet evidenced | Unresolved rights = no public release |
| D13 | Is the proposed name free of trade-mark conflicts? | UNKNOWN | IPOS and other relevant searches plus clearance required |
| D14 | How will users delete information? | Delete host chats/uploads using host controls; delete local exports manually | Never promise deletion of host provider records by the skill |
| D15 | Is any expenditure required? | No additional infrastructure assumed; host access may cost money | Any paid tier/API/tool must be separately approved before purchase |
| D16 | Who can accept residual academic accuracy risk? | Managing Director after CTO independent evidence review | Serious wrong-deadline risk = no release |

## 3. Functional scope for v0.1

### In scope

1. Read only explicitly supplied pasted text or schema-valid user-provided JSON; structured extraction from text is agent-assisted and must be visibly uncertain where necessary.
2. Represent one assessment as stable `item_id`, `module_id`, title, date/time precision, timezone, source ID, source excerpt and confidence/confirmation flags.
3. Compare an earlier snapshot and a later candidate snapshot using deterministic rules.
4. Label `UNCHANGED`, `ADDED`, `CHANGED`, `REMOVED` (explicit cancellation only), `CONFLICT` or `UNVERIFIED`.
5. Display both old and candidate values, including exact evidence excerpts and provenance.
6. Default to **no applied changes**. Export proposed changes in Markdown/JSON/CSV where the host supports files; conflicts are never exported as final confirmed deadlines.
7. Run a standalone Python 3.11+ standard-library-only comparison helper with no network access, no database and no secrets.
8. Provide one portable canonical `SKILL.md` with tested, host-specific setup notes.
9. Include synthetic data, automated tests and manual installation evidence.

### Explicitly out of scope

Account creation; server or cloud database; automated LMS/email/calendar access; calendar writes; ongoing monitoring; paid plans; payments; push notifications; analytics; scraping protected portals; extracting answers or essays; grading; training models on student data; enrolment/institution integrations; image/PDF OCR guarantees; timezone guessing; resolving contradictory policy documents; a public site; mobile applications; hosting or deployment.

### Non-functional requirements

- **Safety:** Evidence-linked all nontrivial changed deadline claims; zero silent acceptance of conflicts; no hidden writes.
- **Security:** No shell execution from input; bounded file/text size; path isolation; redaction; no secret use; untrusted source instructions ignored.
- **Portability:** Every supported host is documented separately and backed by manual verification; do not advertise universal compatibility.
- **Performance (proposed acceptance):** Deterministic comparison of 100 synthetic records within 2 seconds on a stated reference machine. Measure rather than assume.
- **Reliability:** Same inputs and version produce same structured result; malformed input yields clear error and no partial authoritative update.
- **Accessibility:** Plain-text readable reports; status meaning not communicated by colour alone; machine-readable export.

## 4. Exact MVP workflows and user stories

**US01 — Changed deadline.** Given old `2026-11-12T17:00:00+08:00` and new `2026-11-14T23:59:00+08:00`, show `CHANGED`, cite old and new excerpts and require confirmation before acting on a draft. v0.1 never creates a final confirmed export.

**US02 — Contradictory notices.** Given two credible candidate notices for the same item with different due dates, show `CONFLICT`, both dates and source IDs, then ask for verification. No arbitrary source priority.

**US03 — Missing in partial document.** Given a partial notice that does not mention an earlier item, show `UNVERIFIED` or preserve previous state, not `REMOVED`.

**US04 — Explicit cancellation.** Given a notice explicitly cancelling a named assessment, show `REMOVED` as a *proposed* change with source excerpt, requiring confirmation.

**US05 — Ambiguous timezone/date.** Given `10/11/26, midnight`, mark date order and timezone uncertain; never silently infer SGT or UTC.

**US06 — Host/provider prompt injection.** Given a source excerpt instructing the agent to email a document elsewhere, ignore the instruction and treat it solely as data.

**US07 — Duplicate titles.** Two modules each contain a “Final report”. Do not merge them without stable matching identifiers.

**US08 — User deletion.** The skill can explain how to delete its local generated files, but cannot falsely claim it has deleted the AI host's conversation or uploads.

## 5. Proposed technical stack and cost boundary

| Layer | Selected for v0.1 | Reason | Financial status |
|---|---|---|---|
| Skill package | Agent Skills `SKILL.md`, Markdown references | Lightweight canonical package | No infrastructure purchase proposed |
| Deterministic engine | Python 3.11+ standard library | Small attack surface and portable tests | No package subscription proposed |
| Model and interface | User-chosen compatible Claude/ChatGPT/Grok host | Avoid separate product backend | Host eligibility/pricing NOT VERIFIED |
| Persistence | None on SociusFlow services; user-managed files only | Data minimisation | No hosting costs proposed |
| Database | None | No multi-user state | Not applicable |
| API | Local CLI/JSON contract only | No HTTP attack surface | No paid API approved |
| CI | GitHub Actions, bounded tests and scans (to be configured) | Reproducibility | Quotas/pricing NOT CONFIRMED |
| Payments | None | Open-source prototype | Not applicable |
| Deployment | GitHub public repository only after gate | No web server | No deployment performed |

No Supabase, Firebase, S3, Vercel, Cloudflare, Stripe or AI API keys are required for v0.1. Their absence is intentional; **do not implement placeholder authentication**.

## 6. Proposed repository tree

```text
Deadline-Guardian/
├── README.md
├── PRODUCT-DESCRIPTION.md
├── SPEC.md
├── SECURITY.md
├── CODE-STYLE.md
├── DATABASE.md
├── API-GUIDE.md
├── PRIVACY-POLICY.md
├── TERMS-OF-USE.md
├── DATA.md
├── IP.md
├── DELETE.md
├── AI_WORKING_RULES.md
├── TICKETS.md
├── RELEASE_CHECKLIST.md
├── AGENTS.md
├── ARCHITECTURE_DECISIONS.md
├── SOURCES.md
├── .gitignore
├── LICENSE                  # already present; rights approval evidence remains open
├── skills/
│   └── academic-deadline-drift-guard/
│       ├── SKILL.md         # not created in this pre-repo pack
│       ├── references/
│       └── scripts/reconcile.py
├── DECISIONS.md             # DG-DEC-001 authority and assumptions
├── CONTRACT.md              # canonical T01 semantics
├── schemas/                 # snapshot/result v1 JSON Schemas
├── examples/                # strictly fictional contract cases
└── tests/
```

## 7. Ticket execution and agent loop controls

T00 decision preparation and T01 contract authoring were expressly authorised together in this session, with a separate T01 author and independent review. Actual application coding remains ticket-limited. Work is split into tickets in `TICKETS.md`. **One fresh coding agent per ticket** means a new task-limited context with only approved specifications, necessary code and current ticket; no cross-ticket autonomous continuation. Each ticket must:

1. Read the approved `SPEC.md`, relevant security/data contract and its ticket.
2. State `CONFIRMED`, `INFERENCE` or `ASSUMPTION` for material uncertain technical assertions.
3. Make only in-scope changes on a new branch; produce small, testable work.
4. Run relevant checks and capture actual command, exit result and current commit.
5. Compare changed files against the ticket and this SPEC; list deviations.
6. Require independent agent review of proactive loops, followed by authorised human review before merge.
7. If desired behaviour changes: **propose a change to the plan first**, secure decision-owner approval, then resume code. Never silently make the code define scope.
8. Return `PASS`, `FAIL`, or `BLOCKED` with evidence. Lack of evidence is never PASS.

## 8. Done condition: hard stop for every agent

**Ticket done** only when all acceptance assertions for that ticket are met with reviewed evidence, tests pass on the changed head commit, security and data boundaries remain intact, and any plan deviations have approved SPEC revisions. Stop the agent loop on passing criteria; no unrequested extensions.

**Prototype done** only when: all P0 and P1 implementation tickets pass; all required synthetic regression tests pass; the helper makes zero network requests and silent writes; a complete report with traceable evidence is shown; one actual host and a second compatible host are tested separately; and technical/security review has documented results.

**Public release done** only after an independent review plus explicit Managing Director go/no-go; IP and trade-mark review; approved privacy/legal publication language; published `LICENSE` with rights confirmation; repository scanning; actual CI success; installation verification; safe sample data; documented rollback; and no open P0/P1 defects. **Nothing in this document proves any of these occurred.**

## 9. Stop-ship conditions

- Incorrect, fabricated or silently substituted deadline; conflicts accepted without user confirmation.
- Hidden network traffic, unsafe file access, credential reading, prompt-injection execution or data exfiltration.
- Real student records or secrets entering public repository, issue, example or CI artefact.
- Missing provenance for a claimed changed date; ambiguous dates normalised without evidence.
- Unresolved code/IP ownership, trade-mark challenge, material privacy or minors' safety concern.
- Missing independent review, failed CI, unverified compatibility claims, or absent authorised release decision.

## 10. Proposed owners and review metrics

| Responsibility | Proposed role | Proof required |
|---|---|---|
| Product and release decision | Managing Director | Dated recorded approval with exact commit/version |
| Implementation, CI and security | CTO | PRs, passing tests, threat review, rollback |
| 5-user discovery and positioning | CMO | Non-identifying interview summary and competitor log |
| Decision/rights register | COO/secretariat | Sign-off ledger and rights/licence record |
| Personal data handling review | Designated DPO, if formally appointed | Recorded review; no assumption of appointment |

Review triggers: fewer than 3/5 user interviews validate problem; any false deadline that would mislead a user; new backend/integration; a meaningful competitor match; a legal or platform-policy change. Baseline metrics: 0 silent overwrites, test pass rate, 5 discovery interviews, host test matrix, issue turnaround after launch. Proposed performance targets are not measured achievements.

**Confidence in product hypothesis:** 0.78, subject to user research and technical tests.
