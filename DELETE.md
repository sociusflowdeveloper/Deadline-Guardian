# DELETE.md — Deletion and Account Closure Specification

> **Repository reconciliation, 1 November 2026 (SGT):** There is no account or implemented deletion mechanism. Do not run deletion actions on user files. The original public ZIP may have copies outside maintainer control. See [BOOTSTRAP.md](BOOTSTRAP.md) and [DISCOVERY.md](DISCOVERY.md).

**Status:** PROPOSAL | **v0.1:** No user accounts, no SociusFlow-hosted user data and no account-deletion endpoint.  
**Important:** This file distinguishes local file deletion from deleting independently hosted AI conversations. It does **not** assert that anything was deleted.

## 1. v0.1: what a user can delete

| Data or resource | Owner/control | User action | What the action does not do |
|---|---|---|---|
| Downloaded skill package | User/device or GitHub fork | Remove local folder / uninstall from host if installed | Does not remove repo copies or provider chats |
| Source `.json` or text | User's workspace | Delete user-chosen source files and recycle-bin copies | Does not remove host-uploaded attachments |
| Generated `.json`, `.csv`, `.md` | User's workspace | Delete output files and any backups/synchronised copies | Does not erase other systems' imports |
| AI host conversation and uploads | Host provider | Use that host's documented chat/file deletion controls | Not controlled by SociusFlow skill |
| Public GitHub issue/PR | GitHub and maintainers | Edit or request removal through provider/maintainer | Mirrors, caches and copies may remain |
| Voluntary feedback to company | SociusFlow if actually received | Send request to pratheeksha@sociusflow.com (user-selected privacy address confirmed 9 November 2026 SGT; monitoring remains unverified) | Legal/legitimate retention exceptions may apply |

The helper must not create persistent caches, silent backup directories or unrequested telemetry. **Implementation tests are required**. Secure erasure from storage media, provider backups and third-party copies cannot be guaranteed simply by deleting a local file.

## 2. No misleading 'delete account' interface

The skill has no accounts. Do not create a fake “Delete account” button or promise deletion from Claude, ChatGPT, Grok or GitHub. In v0.1, the correct instruction is **“Delete your locally saved files and use the AI provider's deletion controls separately.”** The UI/documentation must show this distinction clearly.

## 3. Mandatory future account-deletion feature (only if accounts are introduced)

Before shipping account registration, add a discoverable authenticated **Delete account and data** route and, if distributing via Google Play, a functional external deletion request page. This is a future specification, **not currently implemented**.

### Future flow

1. User opens `Settings → Account → Delete account and data` (or equivalent visible menu).
2. Explain irreversible consequences, what will be deleted, what must be retained lawfully, retention windows, backups, subscriptions and third-party destinations.
3. Verify the requester with appropriate reauthentication without unnecessary barriers.
4. Present an explicit confirmation. A forgotten password route must not permanently block legitimate requests without a proportionate alternative.
5. Queue an idempotent, auditable deletion operation; immediately revoke active sessions/tokens after the appropriate confirmation and stop processing unrelated to deletion.
6. Delete/irreversibly anonymise authorised account content, projects, sources, exports, shared copies, relevant attachments and sub-processor records, subject to documented lawful retention exceptions.
7. Confirm terminal states and communicate outstanding backup/subprocessor retention honestly. If completion is asynchronous, show status and expected bounds **only after capacity is established**.
8. Document failures and retries; never mark a partially completed deletion as complete. Privacy/DPO review must sign off.

### Proposed API contract — NOT APPROVED

`POST /v1/account/deletion-requests`: authenticated, same-user only, second-factor/reauth, CSRF protection where relevant, confirmation nonce, idempotency key, request ID and explicit irreversible confirmation. `GET /v1/account/deletion-requests/{id}`: owner-only state, least-detail response. No privileged deletion of other users except a separately approved safeguarded process. No web API is implemented in v0.1.

### Test cases for future implementation

- [ ] User can easily discover a working deletion path within the app.
- [ ] If on Google Play, a working public external deletion request page is registered.
- [ ] Auth/ownership checks prohibit cross-account deletion.
- [ ] Session revocation and multiple-device logout verified.
- [ ] All primary storage, object storage, search indexes, analytics, backups and subprocessors mapped.
- [ ] Backups are inaccessible to the active application and expire under documented policy.
- [ ] Retries are idempotent and partial failures are visible for remediation.
- [ ] Users receive accurate confirmation; logs retain only justified minimum audit data.
- [ ] Subscription and payment consequences accurately disclosed.
- [ ] Policy, app-store forms and actual behaviour reconcile.

## 4. External rules: conditional on distribution model

Apple's rules require apps supporting account creation to allow users to initiate deletion within the app; deactivation alone does not suffice. Google Play's rules for in-app account creation require a discoverable in-app deletion path and external web resource, with associated user data deletion subject to justified exceptions. **Neither rule creates a requirement to build a fictional account for a standalone GitHub Agent Skill.**

**Sources:** Apple (2026), *Offering account deletion in your app*, https://developer.apple.com/support/offering-account-deletion-in-your-app/ ; Google (2026), *Understanding Google Play’s app account deletion requirements*, https://support.google.com/googleplay/android-developer/answer/13327111 ; PDPC (2022), *PDPA Key Concepts*, https://www.pdpc.gov.sg/ .

## T04 local report lifecycle

Explicit draft exports are now implemented on this branch. There is no automatic deletion command. Users control the requested output and any backups/synchronised copies; code rollback does not delete those files. T04 uses private transient staging for complete-file publication, attempts staging cleanup on completion/handled failures and never overwrites an existing destination. Cleanup failure, abrupt termination or hardware failure can leave a private staging file for the user to remove. None of this removes AI-provider conversations/uploads or guarantees secure erasure. See T04_VERIFICATION.md for tested cases and limits.


## Current refinement note — 9 November 2026 (SGT)

DRAFT — NOT APPROVED FOR PUBLICATION OR CONTRACTUAL USE. PROPOSAL: 16+ product eligibility is a company choice, not a Singapore statutory threshold; reconcile the existing initial 18+ research scope before launch. Younger users need separate management/privacy decision and safeguards. DATA.md is the canonical proposed retention schedule; local files remain user-controlled, host copies are independent and optional future support retention of 12 months after closure is unapproved. PDPA withdrawal/retention obligations do not establish an unconditional universal erasure right. This offline package has no hosted account deletion or billing. Keep any future app subscription terms separate from website/AI administrative services terms. Sources: Singapore Statutes Online (2026), Personal Data Protection Act 2012, https://sso.agc.gov.sg/Act/PDPA2012 ; PDPC (2026), Guidance by Topic, https://www.pdpc.gov.sg/organisations/resources/guidance-by-topic .


## Privacy contact confirmation — 9 November 2026 (SGT)

**CONFIRMED — user decision, 9 November 2026 (Asia/Singapore):** the public privacy contact is pratheeksha@sociusflow.com. This confirms the selected address only. Actual mailbox monitoring, response-process readiness and formal statutory DPO appointment remain UNKNOWN and require separate evidence.
This current decision supersedes earlier proposed/unknown address-selection wording; historical dated records remain evidence of their original state. Privacy/deletion requests may use the selected address; no monitored-mailbox claim or response-time promise is made.
