# PRIVACY POLICY.md — Proposed Privacy Notice

> **Repository reconciliation, 1 November 2026 (SGT):** This remains an unapproved privacy draft, not a statement of verified processing. The repository is already public; no company contact, processor setting or deletion promise has been operationally verified in this work. See [BOOTSTRAP.md](BOOTSTRAP.md) and [DISCOVERY.md](DISCOVERY.md).

**DRAFT — NOT APPROVED FOR PUBLICATION OR REPRESENTED AS AN IMPLEMENTED PRIVACY PROGRAMME**  
**Product:** Academic Deadline Drift Guard | **Proposed publisher:** SociusFlow Pte. Ltd.  
**Draft date:** 1 November 2026, Singapore Time | **Jurisdictional baseline:** Singapore  
**Contact routing:** Proposed privacy contact: `pratheeksha@sociusflow.com` — **recipient, authority, monitoring and DPO appointment must be verified before publication**. This is not a claim that the listed person is formally designated or available.

## 1. Scope and operating distinction

This draft applies to the intended **open-source, no-account v0.1 skill package**, not the wider SociusFlow applications, future hosted versions or the independent AI services used to run it. The skill is a set of local code/instructions; it is **not** presently a cloud platform operated by SociusFlow. The provider of Claude, ChatGPT, Grok or another chosen host may receive, process and retain data submitted to that service under its own policies. **Do not describe the overall user journey as fully offline or fully private.**

This text describes a **proposed architecture**. It must not be copied to a website as a live and verified statement until engineering confirms that implemented behaviour matches it, the data-flow map is reviewed and the company approves the notice.

## 2. Data the skill is designed to handle

The user may choose to provide module names, assessment titles, dates/times, source excerpts, notice versions and user-supplied academic instructions. Such material can contain personal data about the student or others. The user should redact unnecessary names, identifiers, contact information, grades and other personal details, especially information about minors.

**Intended v0.1 design:** The local comparison helper does not transmit data to servers operated by SociusFlow, does not create an account, does not set cookies, does not collect device identifiers, does not gather location/photos/microphone data and does not use SociusFlow analytics, crash reporting or advertising SDKs. These are design commitments to be **verified in implementation**, not assertions about presently tested code. The AI host may independently collect technical and content data.

## 3. Purposes of processing

The student's chosen AI host may process supplied text to extract candidate dates. The local helper is intended to validate records, compare sources, produce an evidence-linked discrepancy report and generate a user-controlled export. No secondary purpose such as model training for SociusFlow, profiling, advertising, selling student information or automatically forwarding files is authorised for v0.1.

If a user voluntarily contacts SociusFlow or files a GitHub report, the company may receive contact information and the contents of that communication solely to respond, investigate security and maintain the open-source project. Users should not include live student records in tickets.

## 4. Disclosures and third parties

The skill itself has no approved outbound transfer or service-provider integration. Its operation within a chosen AI platform is subject to that platform's privacy terms, retention controls and geographic processing. GitHub separately operates repository hosting, issue and contribution services. No blanket claim is made that these services have the same processing terms, residency or deletion controls. The company must assess any contracts or data transfer arrangements before hosting user data itself.

## 5. Retention, files and deletion

- **Locally processed input:** No SociusFlow copy is intended to be created by the helper. In-memory processing ends with the process. Copies saved in the user's own workspace and backups remain under that user's control until removed.
- **Generated reports:** Retained only where the user chooses to save them, until the user deletes them; there is no skill-operated remote deletion mechanism.
- **AI host chats/uploads:** Retention and removal are governed by the selected AI provider; deleting a local report does not delete host records.
- **GitHub issues/PRs:** Public content may remain visible and be copied or indexed even after a user edits/removes it. Avoid posting personal material.
- **Email/contact and security correspondence:** Proposed internal retention targets appear in `DATA.md` and must be approved, configured and documented before asserting operational compliance.

See `DELETE.md` and `DATA.md` for the proposed exact inventory, targets and limitations.

## 6. Security and accuracy

Proposed safeguards include no network capability in the helper, strict validation, limits on inputs, no hardcoded secrets, separation of untrusted source text from agent instructions, and no automated calendar writes. No security audit or certification is claimed. There may be errors in source interpretation. Users must confirm deadlines with the issuing institution before acting on a disputed result.

## 7. Individual rights and enquiries

Where SociusFlow actually possesses or controls personal data, individuals may contact the company about access, correction, withdrawal of consent, retention and deletion, subject to applicable law and valid exceptions. **SociusFlow cannot delete records held independently by an AI host or GitHub merely because a request is addressed to SociusFlow**. For those records users should use the respective provider's controls. Identity verification must be proportionate and must not itself cause unnecessary data collection.

The privacy contact and a functional response process are launch prerequisites; they have **not** been verified for this draft.

## 8. Children and student materials

The initial product discovery and controlled prototype target users aged 18 or over. The public repository may be visible to younger people; the design does not implement an age-gate. Users must not submit identifiable information about others, particularly children, without a lawful basis and appropriate authorisation. Any school integration, marketing to minors, child-account feature or routine processing of children's personal data requires a separate product/privacy assessment and review against relevant PDPC guidance. Do not presume a blanket parental-consent rule applies to every case; obtain professional advice where material.

## 9. International access, changes and publication

Because different AI hosts may process data internationally, users must review the chosen host's terms. A future SociusFlow-operated hosted version will require a new notice addressing actual controllers/processors, recipients, transfers, retention, cookies, sub-processors and account rights. Post material notice changes with an effective date only after formal approval; do not retroactively claim practices were in place.

**Publication gate:** Verify company details; intended website/repository URL; responsible privacy contact and DPO status; actual data-flow and retention implementation; age-risk review; all processors, third parties and policies; user-facing availability; legal approval.

## Official references

PDPC (2022), *Advisory Guidelines on Key Concepts in the PDPA*, https://www.pdpc.gov.sg/ . PDPC (2024), *Advisory Guidelines on the PDPA for Children's Personal Data in the Digital Environment*, https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/advisory-guidelines/advisory-guidelines-on-the-pdpa-for-children%27s-personal-data-in-the-digital-environment_mar24.pdf . Apple (2026), *App Review Guidelines*, https://developer.apple.com/app-store/review/guidelines/ . Google (2026), *User Data policy*, https://support.google.com/googleplay/android-developer/answer/10144311 . These app-store rules matter if a native app is subsequently built; this skill is not such an app.

## Prototype contract clarification (draft)

DG-DEC-001 adopts a local JSON contract that includes bounded source text alongside extracted records so the future helper can check literal excerpts. Source text can contain personal data and should be minimised before supply. Full source bodies are not intended to be copied into draft result files. This design is not implemented or tested here; it creates no live privacy promise or change to independent host retention.


## Current refinement note — 9 November 2026 (SGT)

DRAFT — NOT APPROVED FOR PUBLICATION OR CONTRACTUAL USE. PROPOSAL: 16+ product eligibility is a company choice, not a Singapore statutory threshold; reconcile the existing initial 18+ research scope before launch. Younger users need separate management/privacy decision and safeguards. DATA.md is the canonical proposed retention schedule; local files remain user-controlled, host copies are independent and optional future support retention of 12 months after closure is unapproved. PDPA withdrawal/retention obligations do not establish an unconditional universal erasure right. This offline package has no hosted account deletion or billing. Keep any future app subscription terms separate from website/AI administrative services terms. Sources: Singapore Statutes Online (2026), Personal Data Protection Act 2012, https://sso.agc.gov.sg/Act/PDPA2012 ; PDPC (2026), Guidance by Topic, https://www.pdpc.gov.sg/organisations/resources/guidance-by-topic .
