# REPO-BASELINE.md

Baseline documentation instructions for every repository.

**Audience:** the repository owner, contributors, and any coding agent working in the repository.
**Jurisdiction assumed:** Singapore. Re-assess legal items if users, customers or data are located elsewhere.
**Status of this file:** a working checklist, not legal advice. Statutory references must be checked against Singapore Statutes Online before reliance.

---

## 1. How to use this file

1. Copy this file into the root of the new repository.
2. Complete the **project profile** (section 3). Every answer is Yes, No or Unknown.
3. Create the **core documents** (section 4). These apply to every repository.
4. For each trigger answered Yes, create the documents listed under that trigger (section 5).
5. Record every applicable document in `docs/DOCS-REGISTER.md` (section 7).
6. Re-run the profile whenever a review trigger occurs (section 9).

## 2. Rules

1. **Trigger-based, not exhaustive.** Create a document only when its trigger applies. Do not create empty or placeholder files.
2. **Unknown counts as Yes** until the question is resolved. Record the open question in the register.
3. **Small projects may merge documents.** A section in `README.md` or `ARCHITECTURE.md` satisfies an item if it covers the stated content. Record the location in the register.
4. **Documents must match reality.** A document describing a practice that is not implemented is a defect. Either fix the practice or correct the document.
5. **Status requires evidence.** Do not mark anything `IMPLEMENTED` or `VERIFIED` without the evidence defined in section 8.
6. **Filenames are conventions.** No law prescribes them. `README.md`, `LICENSE`, `CONTRIBUTING.md`, `SECURITY.md`, `CHANGELOG.md` and `CODE_OF_CONDUCT.md` keep their widely recognised names; everything else uses `UPPER-KEBAB-CASE.md`.
7. **Never commit** secrets, credentials, signed contracts, real personal data, or detailed unremediated security findings.
8. **Public legal documents must be delivered in the product**, at the point of collection or acceptance. A copy in the repository is the versioned source only.

## 3. Project profile

Complete and keep this table current.

| ID | Trigger question | Answer | Notes |
|---|---|---|---|
| T1 | Does it collect, store or process personal data (accounts, forms, logs, analytics)? | Yes | User-supplied academic source JSON can contain personal data; current tests are fictional only. |
| T2 | Does it have user accounts, roles or restricted resources? | No | No hosted accounts, roles or restricted server resources. |
| T3 | Does it take payments or run subscriptions? | No | Offline standard-library helper, no billing. |
| T4 | Does it use persistent storage (database, files, object storage)? | Yes | Explicit user-directed local JSON/CSV/Markdown exports; no central database. |
| T5 | Does it expose or consume an API, or integrate with external services? | Yes | Consumes user-selected AI host workflow and exposes local CLI/schema contract; no HTTP API. |
| T6 | Is it deployed for real users (production)? | No | No hosted deployment or approved product release; local package only. |
| T7 | Does it include material AI functionality? | Yes | Agent-assisted academic source interpretation; helper itself deterministic. |
| T8 | Can users post or share content visible to others? | No | No hosted posting or sharing feature; user-controlled exports are separate. |
| T9 | Are there contributors other than the owner (employees, freelancers, volunteers)? | Unknown | Contributor engagement/IP records not inspected. |
| T10 | Is the code public or open source? | Yes | Public source with existing Apache-2.0 LICENSE; rights clearance remains separate. |
| T11 | Is it directed at, or likely to be used by, children? | Yes | Student-facing academic use creates foreseeable younger-user risk; current real-data release remains blocked. |
| T12 | Are users or data-processing providers located outside Singapore? | Unknown | AI host, user and backup jurisdictions depend on deployment choice. |
| T13 | Is it sold or delivered to a business or government customer under contract? | No | No inspected customer delivery contracts or enterprise service. |
| T14 | Does it have a substantial user interface? | No | Command-line/package workflow; no substantial graphical user interface. |
| T15 | Are coding agents used in development? | Yes | Agent Skill and repository agent workflow. |
| T16 | Is it distributed as a mobile or desktop application? | No | Source/skill package, no mobile store or desktop application distribution. |
| T17 | Does it operate in a regulated area (financial services, healthcare)? | No | Academic deadline comparison; no financial/clinical operation. |

## 4. Core documents: every repository

| # | Item | Must contain | May live in |
|---|---|---|---|
| C1 | `README.md` | Purpose, status, owner, setup, run commands, documentation index | Own file |
| C2 | `SPEC.md` | Users, problem, scope, exclusions, workflows, acceptance criteria | Own file, or README for small projects |
| C3 | `ARCHITECTURE.md` | Components, data flows, integrations, trust boundaries, key decisions | Own file once the project exceeds a single component |
| C4 | `TESTING.md` | Test commands, critical journeys, acceptance process | Own file, or README section |
| C5 | Licence decision | `LICENSE` file, or an explicit statement that no licence is granted | Root |
| C6 | Secrets hygiene | `.gitignore` covering secrets; `.env.example` with names only, no values | Root |
| C7 | `docs/DOCS-REGISTER.md` | The register in section 7 | `docs/` |
| C8 | `docs/decisions/` | One short record per significant decision: context, options, decision, consequences | Create on first significant decision |

## 5. Triggered documents

### 5.1 Engineering

| Trigger | Document | Must contain |
|---|---|---|
| T15 | `AGENTS.md` | Agent instructions, boundaries, permitted commands, verification requirements |
| T9 or T15 | `CONTRIBUTING.md` | Branching, pull requests, review, testing, definition of done |
| T9, when conventions exceed automated formatting | `CODE-STYLE.md` | Naming, structure, conventions |
| T14 | `DESIGN-SYSTEM.md` | Typography, colour, components, interaction and accessibility standards |
| T4 | `DATABASE.md` | Schema, relationships, permissions, migrations, recovery |
| T5 | `API-GUIDE.md` | Authentication, permissions, endpoints, errors, limits |
| T5 or T6 | `CONFIGURATION.md` | Environment variables, ownership, safe defaults |
| T5 | `DEPENDENCIES.md` | Third-party services, purpose, owner, risks, replacement options |
| T6 | `CHANGELOG.md` | Released changes and migration requirements |
| Optional | `ROADMAP.md` | Priorities, clearly distinguished from commitments. An issue tracker may replace it |

### 5.2 Security

| Trigger | Document | Must contain |
|---|---|---|
| T6 or T10 | `SECURITY.md` | Private vulnerability-reporting route, supported versions |
| T1, T2, T3 or T6 | `SECURITY-REQUIREMENTS.md` | Testable requirements and release blockers. Write before implementation |
| T1, T2, T3 or T6 | `THREAT-MODEL.md` | Assets, threats, abuse cases, trust boundaries, mitigations |
| T2 | `ACCESS-CONTROL.md` | Roles, permissions, privileged operations, access reviews |
| T6 | Secrets-management procedure | Provisioning, storage, rotation, revocation, exposure response |
| T6 | Vulnerability-management procedure | Intake, triage, remediation, exceptions, verification |
| T6 | Incident-response plan | Escalation, containment, communication, recovery |
| T6 | Software bill of materials (SBOM) | Machine-generated component inventory. Recommended; sometimes contractually required |
| Any unresolved material risk | Risk and exception register | Risk, accountable owner, treatment, review date |

### 5.3 Deployment and operations (T6)

| Document | Must contain |
|---|---|
| `DEPLOYMENT.md` | Build, environments, approvals, deployment, post-deployment verification |
| `RELEASE-CHECKLIST.md` | Required evidence, approvals, post-release checks |
| Rollback procedure | Restoring a working version, including database compatibility |
| `RUNBOOK.md` | Diagnosing common failures and restoring service |
| Monitoring and alerting plan | Metrics, thresholds, alert routing, response ownership |
| Backup and restore plan (also T4) | Scope, frequency, protection, tested restoration |
| Support policy and user guide | Support channels, hours, user instructions |
| Continuity plan (only where others rely materially on the service) | Recovery priorities, objectives, dependencies |
| Decommissioning plan (at retirement or major migration) | Export, user notice, deletion, credential revocation, shutdown |

### 5.4 Public legal documents and notices

| Trigger | Document | Must contain |
|---|---|---|
| T1 | `PRIVACY-POLICY.md` | Organisation identity, data collected, purposes, disclosures, overseas processing, retention approach, access and correction rights, contact details |
| T2, T3 or T6 | `TERMS-OF-USE.md` | Service rules, eligibility, accounts, user obligations, intellectual property, suspension, termination, liability, disputes |
| T5 (public API) or T8 | `ACCEPTABLE-USE-POLICY.md` | Prohibited conduct, enforcement. May form part of the terms |
| T1, where cookies, local storage or tracking are used | `COOKIE-NOTICE.md` | Technologies used and purposes. May form part of the privacy policy |
| T3 | `PAYMENT-TERMS-OF-USE.md` | Prices, taxes, billing cycles, renewals, failed payments, price changes |
| T3 | `REFUND-AND-CANCELLATION-POLICY.md` | Cancellation process, timing, refunds. May form part of payment terms |
| T8 | `COMMUNITY-GUIDELINES.md` | Content standards, reporting, moderation, appeals |
| T7 | `AI-DISCLOSURE.md` | AI functions, limitations, human oversight, data use. May be integrated into other notices |
| T14, where claimed or required | `ACCESSIBILITY-STATEMENT.md` | Supported accessibility, known limitations, assistance channel. Claims must be verified |
| Dependencies or assets with notice obligations | `THIRD-PARTY-NOTICES` | Required copyright, licence and attribution notices |

Requirements for this group:

- Record the **version accepted and the acceptance event** for terms on account-based or paid products. A footer link alone is weak evidence of acceptance.
- A privacy policy does not by itself establish valid consent for every use. Consent and notification are separate obligations.
- T12 triggers a jurisdiction-specific assessment of cookie consent, age eligibility and consumer terms.

### 5.5 Internal data-protection records (T1)

Keep these in restricted records, not the public repository.

| Record | Purpose |
|---|---|
| Data inventory and processing register | What data exists, why, where, who accesses it, who receives it |
| Data-protection policy | Internal responsibilities and handling rules |
| Data protection officer (DPO) designation record | Accountability, published business contact, escalation |
| Retention and deletion schedule | Retention periods or criteria, deletion method, exceptions |
| Access, correction and withdrawal procedure | Verifying, assessing, responding to and recording requests |
| Consent and notice register | Notice versions, purposes, consent evidence, withdrawals |
| Vendor and subprocessor register | Providers, purposes, locations, contractual safeguards |
| Data-breach response procedure | Detection, containment, assessment, notification, recovery |
| Breach log and request log | Evidence of incidents, decisions, requests and responses |
| Test-data handling procedure | Synthetic data, masking, limits on reuse of production data |
| Overseas-transfer assessment (T12) | Destinations and the protection arrangement relied on |
| Privacy impact assessment (higher-risk features or significant changes) | Risks and controls for proposed processing |

Personal Data Protection Act 2012 (PDPA) provisions these records support, **to be verified before reliance**: DPO designation and policies (ss 11–12); consent (s 13); purpose limitation (s 18); notification (s 20); access and correction (ss 21–22); protection (s 24); retention limitation (s 25); overseas transfer (s 26); data-breach notification (Part 6A).

### 5.6 Contracts and commercial records

Controlled business records. Never commit signed copies.

| Trigger | Document |
|---|---|
| T13 | Customer agreement or master services agreement |
| T13 | Statement of work or order form: scope, deliverables, fees, milestones, acceptance |
| T13 | Change-request form |
| T13, with contractual availability or support commitments | Service-level agreement; maintenance and support agreement |
| T13 | Handover and acceptance record |
| T1 with T13, or any provider processing personal data for you | Data-processing agreement |
| T9 | Employment or contractor agreement covering duties, confidentiality, intellectual property and termination |
| T9 | Intellectual property assignment or licence. Payment alone does not necessarily transfer copyright in commissioned work; record ownership in writing |
| Confidential information shared externally | Confidentiality agreement |
| Paid third-party software, hosting or development | Vendor agreement and due-diligence record |
| T3 | Pricing and unit-economics model: hosting, API, support and payment costs |
| T3 | Purchase, invoice and payment records |

### 5.7 Feature-specific and sector-specific additions

| Trigger | Additional documentation |
|---|---|
| T7 | Model and provider register, evaluation plan, safety tests, data-use assessment, human-review procedure, model-change log |
| T11 | Age and capacity assessment, child-appropriate notices, safeguarding assessment, reporting and escalation route, parental arrangements where applicable |
| T3 | Payment-flow description, fraud controls, reconciliation procedure |
| T17 (financial) | Regulatory-perimeter assessment |
| T17 (healthcare) | Clinical-safety and regulatory assessment, specialised data handling |
| T8 | Moderation procedure, abuse-report handling, appeals, intellectual property complaints route |
| T16 | Store disclosures, permission explanations, signing and update procedure, end-user licence terms |
| T10 | Approved licence, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, contributor intellectual property arrangement if needed |
| T13 (enterprise or government) | Security evidence pack, audit materials, continuity evidence, contractual schedules |

## 6. Where each document lives

| Location | Contents |
|---|---|
| **Repository** | Technical documents, engineering rules, operational instructions, versioned source of public policies |
| **Restricted records** (outside the repository) | Signed agreements, personal data, data-protection records, detailed security findings, approvals, incident evidence |
| **Live product** | Privacy policy, terms, payment and refund terms, notices at the point of collection or acceptance |

## 7. Documentation register

Maintain as `docs/DOCS-REGISTER.md`. One row per applicable document. Record non-applicable triggers once, with the reason.

| Document | Location | Owner | Trigger | Status | Version | Last reviewed | Review trigger | Evidence |
|---|---|---|---|---|---|---|---|---|
| `README.md` | `/README.md` | | Core | | | | Setup or scope change | |

## 8. Status definitions

| Status | Meaning | Minimum evidence |
|---|---|---|
| `NOT-APPLICABLE` | Trigger answered No | Reason recorded |
| `DRAFT` | Written, not approved | The file exists |
| `APPROVED` | Owner has reviewed and accepted the content | Approver and date |
| `IMPLEMENTED` | The described practice operates in the product or process | Link to the code, configuration, or live page |
| `VERIFIED` | The practice has been tested and matches the document | Test result, restore test, signed copy, or review record with date |

Examples: a backup plan is `VERIFIED` only after a successful restore test; a contract only when signed by all parties; a privacy policy only when the data inventory confirms that actual processing matches it.

## 9. Review triggers

Re-run the project profile and update the register when any of these occurs:

- A new category of data is collected, or an existing category is used for a new purpose.
- A new external service, provider or integration is added.
- Accounts, payments, AI functionality or user-generated content are introduced.
- The first production release, and each release that changes data handling or permissions.
- A new contributor, contractor or customer joins.
- Users or providers in a new country are added.
- A security incident, data breach or failed restore occurs.
- Twelve months have passed since the last full review.

## 10. Instructions for coding agents

1. Read this file, `README.md`, `SPEC.md` and `AGENTS.md` before making changes.
2. Before implementing a feature, check whether it changes any answer in the project profile. If it does, stop and report the newly triggered documents before continuing.
3. When a change makes an existing document inaccurate, update that document in the same change and note it in the register.
4. Do not create a triggered document unless its trigger is Yes or Unknown.
5. Do not draft legal documents (section 5.4) or contracts (section 5.6) as final text. Produce drafts marked `DRAFT` and flag them for human and, where appropriate, legal review.
6. Do not set a status to `APPROVED`, `IMPLEMENTED` or `VERIFIED`. Propose the change and cite the evidence; the owner sets the status.
7. Never write secrets, real personal data or signed agreements into the repository.
8. State assumptions explicitly. Mark unknowns as Unknown instead of guessing.

## 11. Limits of this checklist

- It is a general software baseline, not a complete statement of legal requirements for any sector or jurisdiction.
- Customer-facing terms, intellectual property arrangements, and higher-risk or cross-border products warrant review by a qualified lawyer.
- Statutory references reflect the author's understanding at the time of writing and must be verified against current law.

## Repository assessment

Assessment date: 12 November 2026 (Asia/Singapore). Accountable owner: Admin. Unknown answers remain applicable until resolved. This is a documentation adoption proposal; it does not approve legal terms or a product release.
