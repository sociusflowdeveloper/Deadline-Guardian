# DATA.md — Data Inventory and Retention Schedule

> **Repository reconciliation, 1 November 2026 (SGT):** T02 validator runs use fictional inputs only; input bounds, error redaction and no-output-file behaviour have focused tests. No real-user processing, provider retention or operator deletion process is verified. Public GitHub distribution already applies to the original ZIP; retention proposals remain unapproved. See [BOOTSTRAP.md](BOOTSTRAP.md) and [DISCOVERY.md](DISCOVERY.md).

**Status:** Local T02–T04 prototype code exists; the wider data/retention policy remains proposed, with no deployed service or real-user processing verified.
**Scope:** Academic Deadline Drift Guard v0.1 plus separately identified optional project communications.
**Rule:** Every new data type, telemetry system, hosted storage area or third party requires a change to this table, the privacy notice, security review and approval **before use**.

## 1. Data inventory

| Data category | Collection / processor in proposed v0.1 | Purpose | Proposed storage and retention | Deletion path | Status |
|---|---|---|---|---|---|
| Pasted academic source text | User's chosen AI host; local helper receives JSON containing bounded source text and extracted records | Interpret candidate deadlines and validate literal excerpt traceability | No SociusFlow-server storage; host retention per provider | Host controls + discard local copy | DESIGN ONLY |
| Uploaded briefs/PDF/images | Not accepted by helper; optional chosen host capability | Host may read for extraction | No skill-operated retention; host policy applies | Host controls | OUT OF SCOPE for validated input |
| Module/assessment titles | In-memory/local, potentially host | Compare records | In memory during process; saved local artefacts until deleted by user | Close process/delete local files | DESIGN ONLY |
| Due date/time/timezone | In-memory/local, potentially host | Detect change/conflict | Same as above | Same as above | DESIGN ONLY |
| Source ID, excerpt, provenance | In-memory/local, potentially host | Evidence for each proposed change | Same as above; redaction encouraged | Same as above | DESIGN ONLY |
| Generated JSON/CSV/Markdown draft report | Explicit user-selected new local destination in workspace | Review/export | Until user removes file; no automatic expiry | Delete output plus own backup/synchronised copies | T04 IMPLEMENTED; fictional checks in T04_VERIFICATION.md |
| Local process memory | Current user device only | Compute results | For process lifetime; operating system may use swap | End process; secure deletion cannot be guaranteed | DESIGN ONLY |
| Local caches/temp files | No persistent cache; T04 uses private exclusive temporary staging in selected output directory | Publish complete draft without overwrite | Staging cleanup is attempted on success/handled failure; cleanup failure or abrupt termination can leave a staging file | User may remove leftover private staging files; no secure-erasure guarantee | T04 failure tests; abrupt termination recovery is user-managed |
| SociusFlow user account/profile | None | None | Not collected | Not applicable | OUT OF SCOPE |
| Passwords, authentication secrets | None | None | Not collected | Not applicable | FORBIDDEN |
| IP address, exact device/location | Not gathered by helper | None | Not collected by skill | Not applicable; host/GitHub policies separate | OUT OF SCOPE |
| Photos, camera, microphone | No local capture; host may process supplied file | None in validated comparator | Not collected by skill | Host controls | OUT OF SCOPE |
| Analytics/cookies/ad IDs | None | None | Not collected; no retention | Not applicable | OUT OF SCOPE |
| App crash logs / stack traces | No service telemetry | None | No persistent logs; output redacted errors only | Not applicable | MUST TEST |
| Payment data | None | None | Not collected | Not applicable | OUT OF SCOPE |
| Public GitHub issue/PR content | GitHub + contributors | Collaboration | Public potentially indefinitely and mirrored | Edit/delete request under GitHub controls; copies may survive | PLATFORM-CONTROLLED |
| Optional feedback email/contact | SociusFlow, only if a user voluntarily writes | Answer feedback | **PROPOSAL: 90 days after closure** unless justified hold | Internal process plus request | NOT APPROVED/IMPLEMENTED |
| Private vulnerability report | GitHub security channel + maintainers | Investigation/remediation | **PROPOSAL: 12 months after closure** unless legal/security hold | Restricted access and retention review | NOT APPROVED/IMPLEMENTED |
| Internal release decision/test evidence | Company-controlled repository, fictional-only | Audit and quality | **PROPOSAL: 24 months** after supersession, unless required longer | Maintainer-controlled archive/deletion | NOT APPROVED/IMPLEMENTED |
| Synthetic test fixtures | Public repository | Demonstrate safe behaviour | Until replaced or repository removed; no live data | Source-control change | DESIGN ONLY |

**Retention distinction:** A proposed retention target is a governance decision, **not proof** that a service is configured to purge information. Local files, provider uploads and copies in user backups cannot be automatically erased by this skill. Do not publish any promise of a deletion SLA without an operational implementation and audit evidence.

## 2. Data flow diagram

```text
Student source material
       │
       ▼
Chosen AI host (independent controller/processor assessment required)
       │ candidate JSON including bounded source text
       ▼
User-controlled local input → offline validator and comparator → local report
                                                  │
                                                  └── user review; no external writes

Optional: GitHub contribution / voluntary feedback → GitHub or company-controlled correspondence
```

## 3. Third-party responsibility map

- **Chosen AI host:** independently defined logging, retention, training settings, security, geographic transfers and user deletion rights. Provider-specific claims must cite current terms and actual workspace setup.
- **GitHub:** hosts source and user contributions; public issues are not confidential. GitHub repository security and privacy settings need independent inspection.
- **SociusFlow:** would control any emails, opt-in feedback or future hosted processing actually received. Do not claim the organisation never receives personal data merely because the helper is offline.

## 4. Data lifecycle controls

Data minimisation at intake; deterministic validation; no hidden logging; source redaction; no network; no default file overwrites; disclosure of external host processing; safe deletion guidance. A future hosted architecture must add encryption at rest and transit, owner-scoped authorisation, backups and restoration, service-provider agreements, breach response, user export/deletion, change logs, retention automation and periodic verification.

## 5. Verification and change control

- [ ] Inspection proves zero outbound communication by helper.
- [ ] Inspection proves no persistent temp files/caches or full-content error logs.
- [ ] All example/test data demonstrably fictional.
- [ ] Host processing disclosures verified for each tested platform.
- [ ] Company contact and deletion handling implemented before external submissions are invited.
- [ ] DPO review completed where relevant; risk assessment for minors documented.
- [ ] Any new personal-data category added to this register before collection.

**Legal reference:** PDPC, *Advisory Guidelines on Key Concepts in the PDPA*, particularly retention limitation and protection obligations: https://www.pdpc.gov.sg/ . Retention periods in this file are project proposals, **not statutory defaults**.

## T01 data-map refinement

The adopted contract includes each supplied source extract as `source.text` (up to 16,000 characters) to check that record excerpts are literal substrings. The helper therefore processes this bounded text locally as well as extracted fields. This is internal quote consistency, not proof of authenticity or semantic correctness. Full source bodies must not be copied into generated reports; reports include only the required excerpts/references. All current fixtures are fictional; real-data processing controls are not yet implemented or verified.

## T04 local export refinement

The user may explicitly persist draft reports under the workspace. Reports contain record titles, due fields and necessary evidence excerpts, never entire source bodies as additional fields. Keep exports out of public issues, CI and repositories. CSV/Markdown apply display sanitisation; JSON is the canonical exact-evidence representation. There is no operator backup, expiry job or hosted retention control. The implementation's private transient staging is part of the requested write, not telemetry or a retained cache. See T04_VERIFICATION.md for actual failure cleanup/race checks and limitations.


## Retention refinement — 9 November 2026 (SGT)

This remains a draft, not an approved privacy notice or live retention commitment. User-controlled inputs/reports/staging remnants and device/cloud backups remain until the user deletes them under their own storage arrangements; no operator expiry job or hosted backup is introduced. Independent AI host chats/uploads follow verified host settings, not a helper deletion guarantee.

PROPOSAL only: if optional support correspondence is introduced, retain for 12 months after closure, subject to documented lawful necessity/holds and privacy review. No support-data collection is asserted. Future hosted categories require separately approved numerical targets and implementation; no fictional 30-day account-deletion or 35-day operator-backup promise applies to this offline package. Business/legal records require a separately justified schedule. PRIVACY-POLICY.md and DELETE.md refer to this file as canonical retention proposal.


## Privacy contact confirmation — 9 November 2026 (SGT)

**CONFIRMED — user decision, 9 November 2026 (Asia/Singapore):** the public privacy contact is pratheeksha@sociusflow.com. This confirms the selected address only. Actual mailbox monitoring, response-process readiness and formal statutory DPO appointment remain UNKNOWN and require separate evidence.
This current decision supersedes earlier proposed/unknown address-selection wording; historical dated records remain evidence of their original state. Privacy/deletion requests may use the selected address; no monitored-mailbox claim or response-time promise is made.
