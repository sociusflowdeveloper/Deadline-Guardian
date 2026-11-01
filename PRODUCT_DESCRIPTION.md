# PRODUCT_DESCRIPTION.md

> **Repository reconciliation, 1 November 2026 (SGT):** Actual repository: sociusflowdeveloper/Deadline-Guardian. The working product hypothesis and two-day estimate remain proposals. Original market/platform references are inherited research, not freshly verified facts. See [BOOTSTRAP.md](BOOTSTRAP.md) and [DISCOVERY.md](DISCOVERY.md).

# SociusFlow Open Agent Skill: Product Discovery and Repository Specification

**Status:** Product PROPOSAL — documentation publicly present; product not approved, implemented, tested or released  
**Research date:** 1 November 2026 (Singapore Time)  
**Product sponsor:** SociusFlow Pte. Ltd. (proposed)  
**Repository:** [`sociusflowdeveloper/Deadline-Guardian`](https://github.com/sociusflowdeveloper/Deadline-Guardian) (existence confirmed; no product release inferred)  
**Recommended skill identifier:** `academic-deadline-drift-guard`  
**Target hosts:** Claude, eligible ChatGPT/Codex environments, and supported Grok skill environments  
**MVP objective:** A working, portable, evidence-led Agent Skill that can be demonstrated using fictional data in two focused development days.

> **Evidence caveat.** There is no reliable method of proving that an equivalent skill does not exist anywhere. The opportunity proposed below is a *differentiated combination of capabilities* based on a bounded review of publicly discoverable projects, not a claim of worldwide novelty. All scores, development estimates and commercial expectations are internal assumptions until validated.

## 1. Decision

**RECOMMENDATION — BUILD CONTENDER A: Academic Deadline Drift Guard.**

Create a free, open-source Agent Skill that compares multiple versions of academic instructions or announcements, identifies changed and contradictory dates, shows the exact supporting evidence, and proposes a controlled update to a student's task/calendar plan. It must **never silently decide which conflicting deadline is correct, submit coursework, or modify a calendar without explicit permission**.

Positioning statement:

> **When assignment dates change, know exactly what changed, where the evidence came from, and what needs confirmation before updating your plan.**

This extends SociusFlow's mission in scheduling, tasks, deadlines and workload management without generating educational answers, essays or creative coursework. The standalone skill delivers value even to users who do not have SociusFlow accounts.

## 2. Market and platform evidence

### Inherited research observations, not reverified during bootstrap

- The open **Agent Skills** format uses an `SKILL.md` file with `name` and `description` frontmatter and optional scripts/references. The same authored skill can be adapted for compatible hosts, but runtime capabilities and installation are host-specific. [Agent Skills specification](https://agentskills.io/specification).
- **Claude** supports custom Agent Skills and filesystem-backed supporting resources. [Anthropic documentation](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).
- **OpenAI** documents reusable skills and their distribution; the current ChatGPT feature has eligibility and workspace limitations. Do not advertise universal ChatGPT account compatibility. [OpenAI skills guide](https://learn.chatgpt.com/docs/build-skills); [ChatGPT availability](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).
- **Grok** has announced custom skills and its developer documentation describes `SKILL.md` discovery. Do not treat Grok web, mobile and CLI as identical until tested separately. [xAI announcement](https://x.ai/news/grok-skills); [Grok skill documentation](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/08-skills.md).
- Simple syllabus-to-calendar conversion **already exists** in public repositories: [`wyc79/calendar-creator-skill`](https://github.com/wyc79/calendar-creator-skill), [`Dsmx1119/Syllabus-Extractor`](https://github.com/Dsmx1119/Syllabus-Extractor), [`ZKey-Taken/syllabus-to-calendar`](https://github.com/ZKey-Taken/syllabus-to-calendar), and in a hosted product [Syllaplan](https://www.syllaplan.com/).
- Other adjacent Agent Skills include [`SkillMedev/skills`' Study System](https://github.com/SkillMedev/skills), the [Claude for Legal deadlines skill](https://github.com/anthropics/claude-for-legal/blob/main/legal-clinic/skills/deadlines/SKILL.md), and existing calendar/scheduling tools. Their existence makes generic planning or date extraction a weak uniqueness claim.

### Opportunity hypothesis (not confirmed)

Students struggle less with *creating the first calendar* than with keeping it correct when a lecturer changes the brief, a portal notice contradicts a PDF, or an instruction omits the timezone. A narrow **source comparison + provenance + conflict-handling** skill may be distinguishable from extraction-only products. Conduct user interviews before claiming demand.

## 3. Three product contenders

### A. Academic Deadline Drift Guard — recommended

**Problem:** Existing academic plans can become wrong after a changed announcement, document version or conflicting instruction.

**Input:** Two or more user-supplied extracts, screenshots or documents containing course, assessment and date information; optional prior structured task list. Files and image interpretation depend on host capabilities.

**Output:** New/changed/removed/conflicting deadlines; quoted supporting excerpts; explicit unknowns; a proposed update log; downloadable structured JSON/CSV when supported.

**Distinctive design:** Evidence-first comparison, version-aware change detection, timezone ambiguity checks, no silent overwrites and user-confirmed resolution.

**MVP feasibility:** High if it starts with pasted text and a small deterministic JSON comparison script; medium once PDF parsing and third-party connectors are included.

**Main risks:** False attribution of a deadline, model extraction mistakes, sensitive school documents, and ambiguity over which source is authoritative.

### B. Workload Capacity Compass

**Problem:** A schedule may be technically conflict-free but impossible to complete given estimated hours, classes, commitments and rest constraints.

**Input:** Deadlines, estimated effort, weekly availability and locked commitments supplied by the user.

**Output:** Workload-capacity shortfall, days exceeding available hours, feasible suggested work blocks, and flagged work that cannot fit before its deadline.

**Distinctive design:** Explicit **capacity arithmetic** and honest infeasibility warnings rather than motivational or generic study tips.

**MVP feasibility:** High with deterministic arithmetic. Differentiation is weaker because planners, timetable optimisers and study-system skills already occupy adjacent ground.

**Main risks:** Inaccurate effort estimates, unrealistic assumptions about study time, and unsafe pressure to overwork. Never recommend reducing essential sleep or health-related commitments to make a schedule fit.

### C. Groupwork Commitment Ledger

**Problem:** Meeting notes and chats often leave group members uncertain about what was agreed, by whom and by when.

**Input:** User-supplied project notes, participant-confirmed action items and meeting summaries.

**Output:** Proposed action register with owner, deadline, evidence, acceptance criterion and unresolved decisions; exports for a task system.

**Distinctive design:** Separates **suggested assignments** from **explicitly accepted commitments**, with no invented agreement or retrospective approval.

**MVP feasibility:** Very high for structured input, but the proposition is close to general meeting-to-task and project-management assistants.

**Main risks:** Incorrect attribution to teammates, unnecessary personal-data collection, and social friction if suggested work is presented as assigned work. Consent and confirmation are essential.

## 4. Weighted decision analysis

### Scoring framework

Scores are **proposed management judgements**, not measured market facts. Each criterion scores from **1 (poor) to 5 (excellent)**. Weights reflect a two-day, student-productivity-first, publicly distributed skill. The total possible weighted score is 100.

| Criterion | Weight | Reason |
|---|---:|---|
| Alignment with SociusFlow mission | 25% | Scheduling, deadlines and workload must remain the central value |
| Differentiation from discovered alternatives | 20% | A public repository needs a specific reason to exist |
| Two-day MVP feasibility | 20% | Minimise dependencies, integrations and operational exposure |
| Cross-host reliability and portability | 15% | Users should not be restricted to a single AI provider |
| GitHub discovery and demonstration potential | 10% | The problem should be easy to explain and show |
| Future commercial adjacency | 10% | It should create a possible, non-coercive route to SociusFlow |
| **Total** | **100%** | |

| Criterion (weight) | A. Deadline Drift Guard | B. Capacity Compass | C. Commitment Ledger |
|---|---:|---:|---:|
| Mission alignment (25%) | 5/5 | 5/5 | 4/5 |
| Differentiation (20%) | 4/5 | 3/5 | 3/5 |
| Two-day MVP (20%) | 4/5 | 4/5 | 5/5 |
| Cross-host portability (15%) | 5/5 | 4/5 | 5/5 |
| GitHub discoverability (10%) | 4/5 | 4/5 | 3/5 |
| Commercial adjacency (10%) | 3/5 | 4/5 | 3/5 |
| **Weighted result (/100)** | **86.0** | **81.0** | **79.0** |
| **Priority** | **1 — BUILD** | **2 — RESERVE** | **3 — RESERVE** |

Formula: `Weighted result = Σ (criterion weight × score / 5)`. Example for A: `25×5/5 + 20×4/5 + 20×4/5 + 15×5/5 + 10×4/5 + 10×3/5 = 86`.

**Sensitivity:** The first-place margin over B is only 5 points. If interviews reveal that students almost never encounter contradictory deadlines, or if competitor discovery finds an equivalent mature source-reconciliation skill, reassess the decision. A 5-point lead does not establish commercial superiority.

## 5. Recommended product requirements: Academic Deadline Drift Guard

### 5.1 User and job to be done

**Primary audience:** Tertiary students managing several modules with changing announcements and assignment deadlines. **Secondary audience:** Student society administrators and group-project coordinators. Secondary use cases must not pull the MVP away from individual deadline accuracy.

**Job:** “Compare these old and new instructions, tell me what actually changed and which dates I must verify, then give me a clean update I can apply.”

### 5.2 Required v0.1 workflow

1. Accept **user-authorised** source material, initially as pasted plain text or structured JSON. Optional file reading relies on the host's available tools and must not be presumed to work everywhere.
2. Identify course/module, assessment/event, due date, due time, timezone and source context **only where stated or legitimately derived from clearly supplied context**.
3. Capture an evidence record per proposed field: source identifier, source type, literal supporting excerpt, document version or supplied timestamp (if available), and uncertainty.
4. Compare the previous known state with candidate new records using a deterministic local script. Detect `ADDED`, `CHANGED`, `REMOVED`, `CONFLICT`, `UNCHANGED` and `UNVERIFIED` statuses. Absence of an item in a partial document is **not evidence of cancellation**.
5. Present a human-readable change report. Where sources disagree, present **both** values and request a decision or verification; do not choose solely because a source was pasted last.
6. Produce a proposed JSON/CSV update file **only after the user has reviewed the disputed entries**. Mark unresolved records as unconfirmed; do not export them as final deadlines.
7. Never write to an LMS, calendar, email or task service, and never send reminders, without the host's actual capability **and** separate explicit user authorisation. No remote write integrations in v0.1.

### 5.3 User-facing example

**Old brief (fictional):** `Marketing report due 12 November 2026, 17:00 SGT.`  
**New portal notice (fictional):** `Marketing report deadline moved to 14 November 2026, 23:59 SGT.`

**Expected result:**

| Assessment | Previous | New candidate | Status | Evidence |
|---|---|---|---|---|
| Marketing report | 12 Nov 2026, 17:00 SGT | 14 Nov 2026, 23:59 SGT | CHANGED — awaiting confirmation | Quote both supplied excerpts |

Then ask the user to confirm the replacement before producing a final calendar update. If another credible notice says 13 November, flag `CONFLICT` with both source excerpts; do not silently promote either value.

### 5.4 Functional boundaries

**IN SCOPE v0.1:** Comparison of two snapshots; one timezone per explicitly stated event; evidence-linked diffs; conflict detection; Markdown/JSON/CSV reporting; synthetic fixtures; concise `SKILL.md`.

**OUT OF SCOPE v0.1:** Autonomous email/LMS monitoring; hidden background polling; account creation; automatic calendar writes; school-wide integrations; scraping portals; direct authentication; essay writing; answer generation; predictive grading; institutional policy interpretation; resolving contradictory instructions without user confirmation.

**v0.2 candidates, only after validation:** Standards-compliant `.ics` preview; optional user-approved import into SociusFlow; encrypted local history; opt-in calendar adapters; user-controlled reminder workflows.

### 5.5 Technical design

**Architecture:** One canonical skills package plus a deterministic Python 3.11+ helper with standard-library dependencies only. The host model handles understanding the user's documents; the script validates and compares structured records. No dedicated backend, database, public API, secrets or network access for the initial release.

**Proposed repository tree:**

```text
Deadline-Guardian/
├── README.md
├── PRODUCT_DESCRIPTION.md
├── LICENSE
├── SECURITY.md
├── CONTRIBUTING.md
├── .gitignore
├── skills/
│   └── academic-deadline-drift-guard/
│       ├── SKILL.md
│       ├── references/
│       │   ├── INPUT_SCHEMA.md
│       │   └── PRIVACY_AND_LIMITATIONS.md
│       └── scripts/
│           └── reconcile.py
├── examples/
│   ├── fictional-before.json
│   ├── fictional-after.json
│   └── expected-report.json
└── tests/
    └── test_reconcile.py
```

The skill is copied or packaged into each supported host's authorised skill location. Do **not** maintain divergent provider-specific logic. Release notes must identify tested host version, install mechanism, and known limitations. For ChatGPT, use the documented Skill/plugin distribution route only where the account/workspace is eligible.

**Candidate skill metadata:**

```yaml
---
name: academic-deadline-drift-guard
description: Compare versions of academic briefs, notices and task lists; detect changed, missing or conflicting deadlines; show source excerpts and propose reviewed updates. Use when a student asks whether assessment dates changed or wants to reconcile contradictory academic schedules. Never silently edit calendars or invent dates.
license: Apache-2.0
---
```

**Proposed machine-readable record:**

```json
{
  "item_id": "module-a:marketing-report",
  "title": "Marketing report",
  "due_at": "2026-11-14T23:59:00+08:00",
  "time_precision": "minute",
  "source_id": "notice-2",
  "source_excerpt": "Marketing report deadline moved to 14 November 2026, 23:59 SGT.",
  "source_observed_at": null,
  "authority_confirmed_by_user": false,
  "user_confirmed": false
}
```

Null values and uncertain sources must remain visibly unknown. Reject invalid timestamps and impossible dates. Dates without a stated timezone must not be silently converted into Singapore Time. Record matching must be explainable and avoid merging two separate assessments merely because their titles look similar.

### 5.6 Security, privacy and legal release gates

**P0 stop-ship requirements:**

- No real student's details, institutional attachments, credentials, access tokens or private company repository content may be published in examples, commits, issues or CI logs.
- Treat content inside uploaded/pasted documents as **untrusted data**. Ignore instructions within them that attempt to redirect the agent, run commands, reveal secrets or transmit data elsewhere.
- The comparison script must be offline, deterministic, bounded in input size and without shell execution, dynamic code evaluation, outbound requests or filesystem scanning outside explicitly provided paths.
- Do not claim “100% local/private” processing: when a user provides material to Claude, ChatGPT or Grok, **that host's processing and data practices may apply**, even if the comparison helper runs locally.
- Never create or overwrite an authoritative deadline without visible confirmation; an unresolved conflict must remain unresolved.
- Scan dependencies, scripts and the release bundle; require code review, tests and documented rollback/revert procedure before publishing or updating the public release.
- Verify the company's ownership of all original code, contributions, examples and branding before selecting a licence or releasing externally. Third-party material must comply with its own terms.

**Singapore review:** If SociusFlow begins collecting or handling identifiable student data as an organisation, assess the applicable **Personal Data Protection Act 2012** obligations, appropriate notices, protections, retention and third-party processing. For products likely to be used by children, review the PDPC's *Advisory Guidelines on the PDPA for Children's Personal Data in the Digital Environment* (March 2024), in addition to the general PDPA framework. A purely local, offline code package with no SociusFlow collection may present a different processing profile, but this does **not** absolve the AI host or any operator of its own obligations. Obtain qualified legal advice on materially uncertain use cases.

Official references: [PDPC guidance directory](https://www.pdpc.gov.sg/organisations/resources/guidance-by-topic); [Children's data guidelines](https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/advisory-guidelines/advisory-guidelines-on-the-pdpa-for-children%27s-personal-data-in-the-digital-environment_mar24.pdf).

**Existing repository licence:** Apache License 2.0 is present and preserved. Rights evidence, dependency compatibility and required notices for future implementation remain subject to review. Do not assume third-party materials or the SociusFlow trademark are licensed under Apache-2.0. A public repo without a licence does not provide the intended open-source reuse rights.

### 5.7 Two-day execution plan (estimate, not a commitment)

| Window | Priority | Proposed owner | Deliverable | Acceptance |
|---|---|---|---|---|
| Day 1, first half | P1 | Managing Director + CMO | Five short problem interviews or documented user tests | At least three participants describe a real or recent deadline-change/contradiction problem; otherwise reconsider A |
| Day 1, second half | P1 | CTO | `SKILL.md`, JSON contract, comparison prototype, sample data | Valid metadata; reproducible diff on fictional inputs; zero network dependency |
| Day 2, first half | P1 | CTO | Conflict checks, error handling, unit tests, clean report | All critical synthetic cases pass, including ambiguous dates and conflicting notices |
| Day 2, second half | P1 | CTO + COO/secretariat | README, disclosure/security review, independent PR review and test evidence | No leaked data; all release gates evidenced; founder decision recorded |
| After tests | P2 | CMO | Public demonstration and explanatory documentation | Demo uses synthetic records and describes actual verified capabilities only |

A two-day **prototype** is plausible; a production-ready, multi-host certified integration is **not** assumed. Proposed working estimate: 12–16 focused engineering hours, excluding stakeholder availability and legal review. Actual cost, time and capacity are unknown until assigned.

### 5.8 Test and acceptance contract

**Required fixtures:** unchanged entry; changed date; changed time only; two contradictory notices; missing timezone; ambiguous date format; same title in different modules; partial extract that omits an item; unparseable source; duplicated notice; instruction-injection text; nonexistent date; optional daylight-saving boundary.

**Release acceptance:**

1. All deterministic `reconcile.py` unit tests pass on the locked source tree and current commit.
2. Each reported change cites the correct fictional source excerpt in the fixture; every conflicting date remains marked unresolved.
3. A missing deadline in a partial extract is never automatically interpreted as cancellation.
4. No live API calls, network requests, emails, calendar writes or background tasks occur in the MVP.
5. The `SKILL.md` package passes the official Agent Skills format validation and manual trigger/no-trigger tests.
6. At least one actual Claude environment and one other named, supported host are manually exercised; document separate results per host rather than claiming universal compatibility.
7. The README includes a 60-second fictional before/after demonstration, installation guidance, supported environments, limitations and privacy caveat.
8. Publication requires documented IP/licence review, secret scanning, independent PR approval and an authorised release decision.

**Unknown until executed:** Real-host compatibility, accuracy on actual university documents, extraction reliability, GitHub interest and user willingness to adopt.

### 5.9 Distribution and commercial strategy

**Repository category:** `agent-skills`, `academic-planning`, `student-productivity`, `deadline-tracking`, `calendar`, `evidence-based`, `education`, `claude`, `chatgpt`, `grok` (apply only verified tags/compatibility claims).

**README hero line:** “Your syllabus changed. Your calendar might not have. Find the discrepancy with evidence before missing a deadline.”

**Discovery motion:** Public installation guide; before/after GIF or plain text comparison; small fictional datasets; one focused explainer for student/developer communities; accessible issue template for incorrect-date reports; respectful contribution process; security contact. Avoid artificial stars, spam and unverified popularity claims.

**Commercial relationship:** The skill must remain useful without SociusFlow registration. A transparent optional footer can link to SociusFlow as a possible later planning tool; no hidden telemetry, forced sign-up or data transfer. A paid API, hosted synchronisation feature or user-data monetisation is **not** approved or assumed.

**Metrics to measure after launch:**

- **Reliability:** Correct change/conflict labelling on a human-reviewed test set; target 0 silently overwritten conflicting deadlines.
- **Utility:** Median user-reported time to reconcile a two-document change; benchmark against a manual workflow.
- **Activation:** Number of real users who complete one verified comparison; collect only opt-in, aggregate feedback where feasible.
- **Adoption:** Stars, forks, issues reporting reproducible bugs, returning contributors and installs *where independently measurable*.
- **SociusFlow adjacency:** Opt-in visits/enquiries from skill documentation, without treating stars as customers.

### 5.10 Governance and decision triggers

**Owner:** Managing Director for build/launch decision; CTO for implementation and security; CMO for demand validation and distribution; COO/secretariat for decision record and release checklist. These are **proposed responsibilities, not assigned or accepted tasks**.

**Proceed to public beta only if:** At least three of five initial target users validate the pain point, the deterministic tests pass, sensitive data and IP ownership are cleared, independent review is complete, and actual host behaviour is documented.

**Reconsider or stop if:** Users rarely experience deadline changes, existing tools solve the task just as well with equal provenance and lower friction, extraction inaccuracies create unacceptable risk, the company cannot demonstrate lawful data handling, or capacity would materially impair core SociusFlow delivery.

## 6. Research limits and final decision

This document is an actionable repository **product description**, not evidence of a completed skill, a licensed code release, an installed integration, a reviewed privacy programme or a successful deployment.

**Proposed decision:** Build a bounded, evidence-first proof of concept for **Academic Deadline Drift Guard**. Preserve Capacity Compass as the second candidate if user research shows the principal pain is workload feasibility rather than deadline changes.

**Confidence in the strategic recommendation:** **0.78**. The format and adjacent competitors are verifiable, but differentiation, user demand, two-day delivery and monetisation remain unvalidated assumptions.

## 7. Research references (accessed 1 November 2026)

- Agent Skills. (2026). *Specification*. https://agentskills.io/specification
- Anthropic. (2026). *Agent Skills*. https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- OpenAI. (2026). *Build skills*. https://learn.chatgpt.com/docs/build-skills
- OpenAI. (2026). *Skills in ChatGPT*. https://help.openai.com/en/articles/20001066-skills-in-chatgpt
- xAI. (2026). *Skills in web, iOS, and Android* (18 May). https://x.ai/news/grok-skills
- xAI. (2026). *Grok skills documentation*. https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/08-skills.md
- wyc79. (n.d.). *calendar-creator-skill*. https://github.com/wyc79/calendar-creator-skill
- Dsmx1119. (n.d.). *Syllabus-Extractor*. https://github.com/Dsmx1119/Syllabus-Extractor
- ZKey-Taken. (n.d.). *syllabus-to-calendar*. https://github.com/ZKey-Taken/syllabus-to-calendar
- Syllaplan. (n.d.). *Turn your syllabus into a calendar*. https://www.syllaplan.com/
- Personal Data Protection Commission. (2024). *Advisory Guidelines on the PDPA for Children's Personal Data in the Digital Environment*. https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/advisory-guidelines/advisory-guidelines-on-the-pdpa-for-children%27s-personal-data-in-the-digital-environment_mar24.pdf
- Personal Data Protection Commission. (2026). *Guidance by Topic*. https://www.pdpc.gov.sg/organisations/resources/guidance-by-topic
