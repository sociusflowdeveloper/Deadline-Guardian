# Deadline Guardian — Academic Deadline Drift Guard

> **Current decision, 1 November 2026 (SGT):** The user has authorised resolving T00 discovery decisions and T01 schema here. Proceed with an offline fictional-data prototype under recorded, unvalidated-demand assumptions. The five interviews are a wider-investment/product-launch gate. Canonical T01 artefacts replace earlier illustrative contracts; application execution and product release remain separate gates. See [DECISIONS.md](DECISIONS.md) and [CONTRACT.md](CONTRACT.md).


**Publisher (proposed):** SociusFlow Pte. Ltd.
**Status:** T05 PACKAGE AND T06 LOCAL SECURITY CHECKS / HOST TESTS PENDING / NO PRODUCT RELEASE
**Prepared:** 1 November 2026 (Asia/Singapore) | **Default legal context:** Singapore

> When an assessment deadline changes, see exactly what changed and where the evidence came from, then review it before modifying your plan.

## Prototype package and verification boundary

These files are **pre-repository planning, risk, API and legal drafts** prepared against the SociusFlow checklist. T02 adds a tested local validation CLI; T03 adds deterministic draft comparison; T04 adds explicit local draft exports; T05 adds the canonical repository skill package and local package checks. This is not proof of installation or invocation on Claude or a second host. There is no remote API, account, database, effective privacy/terms commitment or approved product release. The repository and original ZIP are already public. Rights, trade-mark, security and product-release evidence remain open.

## Documents

| File | Purpose |
|---|---|
| [PRODUCT-DESCRIPTION.md](PRODUCT-DESCRIPTION.md) | Product research, three contenders and weighted decision |
| [SPEC.md](SPEC.md) | Problem, decisions, scope, done criteria, acceptance and stop-ship |
| [TICKETS.md](TICKETS.md) | Small independently reviewable agent tasks |
| [SECURITY.md](SECURITY.md) | Threat model and complete MVP/future backend security controls |
| [CODE-STYLE.md](CODE-STYLE.md) | Python and Agent Skill conventions |
| [DATABASE.md](DATABASE.md) | No-DB decision, transient records and hosted readiness |
| [API-GUIDE.md](API-GUIDE.md) | Proposed offline CLI and JSON schema |
| [PRIVACY-POLICY.md](PRIVACY-POLICY.md) | Draft privacy notice — not approved for publication |
| [TERMS-OF-USE.md](TERMS-OF-USE.md) | Draft user terms — legal review required |
| [DATA.md](DATA.md) | Data register, planned retention and host boundaries |
| [IP.md](IP.md) | Name/trade-mark and copyright/licence clearance register |
| [DELETE.md](DELETE.md) | No-account deletion model and future account flow |
| [AI_WORKING_RULES.md](AI_WORKING_RULES.md) | Adversarial, honest, independent AI-agent workflow |
| [AGENTS.md](AGENTS.md) | Entrypoint for any new coding agent |
| [ARCHITECTURE_DECISIONS.md](ARCHITECTURE_DECISIONS.md) | Proposed stack/cost and change triggers |
| [RELEASE_CHECKLIST.md](RELEASE_CHECKLIST.md) | User checklist translated to evidence-led status |
| [SOURCES.md](SOURCES.md) | External primary references and verification caveats |
| [.gitignore](.gitignore) | Defensive ignores for accidental local data/secrets |

## Proposed product flow

`user-provided old/new academic sources → AI-host extraction → local deterministic comparison → evidence-linked proposed changes → explicit user review`

There is **no authorised automatic calendar update, AI model API key, company database, telemetry, account or paid feature** in the MVP proposal. Users of a third-party AI host are subject to that host's own privacy and subscription practices.

## Implementation sequence

1. Use the adopted T00 prototype decision in DECISIONS.md; demand validation remains open.
2. Use the independently reviewed T01 schema/semantic contract.
3. Continue from the implemented T02 validator, T03 comparator and T04 exporters with T07 rights/privacy clearance and T08 actual host verification after prerequisite review/check gates.
4. Require actual tests, independent review, rights/privacy checks and a separate MD decision before a public product release.

**Current disposition:** GO for constrained fictional-data prototype work; NO-GO for public product release. Validation, comparison and explicit local export code exist on this branch; T05 packaging is present, with T06 local security evidence recorded separately; real host invocation, IP/privacy and release gates remain open.

## Current engineering entry points

- [BOOTSTRAP.md](BOOTSTRAP.md): inspected baseline, extraction manifest, verification and rollback.
- [DISCOVERY.md](DISCOVERY.md): T00 interview kit, D01–D16 decision register and T01 contract blockers.
- [CODEX_HANDOFF.md](CODEX_HANDOFF.md): bounded multi-step execution prompt for the next coding session.

The original `SociusFlow_Deadline_Drift_Guard_Pre_Repo_Pack.zip` is retained as an immutable historical source. Root Markdown files are the maintained working copies; do not edit the ZIP to pretend earlier decisions changed.

## Current prototype decision

The user has authorised resolving T00/T01 here. [DECISIONS.md](DECISIONS.md) records the adopted prototype choices and unvalidated-demand assumptions. [CONTRACT.md](CONTRACT.md), [schemas](schemas/snapshot-v1.schema.json) and [fictional cases](examples/contract-cases.json) freeze the T01 contract. [T01 technical acceptance](T01_VERIFICATION.md) is recorded; T02 validator implementation is available; T03 deterministic comparison is implemented on this branch. The CLI validates and compares supplied fictional snapshots on the tested Linux environment. No host compatibility or release approval is claimed.

## Run the offline draft comparator

Python 3.11+ is required. The safe filesystem reader uses POSIX descriptor-relative no-follow operations; unsupported platforms fail closed. No package installation or API key is needed.

```bash
python skills/academic-deadline-drift-guard/scripts/reconcile.py \
  --workspace . \
  --before examples/fictional-before.json \
  --after examples/fictional-after.json
```

Success prints draft JSON to standard output with `result_status=REVIEW_REQUIRED`, all six provisional status labels as applicable and `confirmed_changes=[]`. Exit 0 means a draft was generated, including possible conflicts; it never confirms a deadline. This default invocation does not save a report. The helper never modifies calendars. Explicit safe file export is available as described below.

Run `python -m unittest discover -s tests -v`. See [T02 verification](T02_VERIFICATION.md) and [T03 verification](T03_VERIFICATION.md) for historical checks; see [T04 verification](T04_VERIFICATION.md) for current export checks and limitations.

## Version history and completeness

[VERSION_LOG.md](VERSION_LOG.md) records each change set, evidence, unresolved gates and rollback. Every change-bearing PR must update it under [AGENTS.md](AGENTS.md). [COMPLETENESS.md](COMPLETENESS.md) defines the product score and remaining delivery work. The source ZIP and earlier verification records remain historical.

## Language and code hygiene

Follow [LANGUAGE_POLICY.md](LANGUAGE_POLICY.md): Python for application/tests, JSON for contracts/data, Markdown for documentation and YAML for CI; short fixed shell commands only for CI glue. Keep only relevant code and dependencies. Additional languages, runtimes or frameworks require an approved need and ADR.

## Save a draft report explicitly

Use a new destination inside the selected workspace; its parent directory must already exist. The default command above still only prints draft JSON. Saving a report requires both `--output` and `--format`:

```bash
python skills/academic-deadline-drift-guard/scripts/reconcile.py \
  --workspace . \
  --before examples/fictional-before.json \
  --after examples/fictional-after.json \
  --output draft-report.md --format markdown
```

Formats: `json` with `.json`, `csv` with `.csv`, `markdown` with `.md`. Choose a different new filename for each run; existing targets, symlink components and unsafe paths are rejected. No overwrite or implicit directory creation is supported.

Exports remain unconfirmed proposals, including conflicts and unknown dates. JSON preserves canonical evidence strings. CSV formula neutralisation and Markdown escaping change display representations without changing canonical input evidence. Review reports before acting; exported evidence remains untrusted data. Keep real reports outside public repositories and delete local exports/backups yourself when no longer needed; the helper does not erase AI-provider chats or uploads.

## Repository skill package

Read [the canonical skill](skills/academic-deadline-drift-guard/SKILL.md) and its bundled references before use. The helper accepts schema-valid local JSON; interpreting pasted text is a separate, uncertain agent-assisted step. Follow the package's exact paths, privacy safeguards and host capability limits.

[T05_VERIFICATION.md](T05_VERIFICATION.md) records local package validation and fictional runs. These checks do not install the skill into a personal account or prove an actual Claude/second-host workflow. T08 requires real invocation evidence. The existing source ZIP remains a historical planning pack, not this skill's current install package.

## Local security verification boundary

[T06_SECURITY_REVIEW.md](T06_SECURITY_REVIEW.md) records the local helper/package threat assessment, reproducible scans, adversarial checks and residual risks. Heuristic secret scans and controlled local tests do not certify security, prove every historical copy is clear, validate real student data or establish host prompt-injection resistance. No account permissions, private reporting channel, provider setting or legal approval was changed.

The unchanged weighted scorecard reaches 85/100 only after the reviewed T05/T06 technical evidence. Remaining points depend on real demand interviews, rights/privacy clearance, actual host runs and an authorised release decision. Public product release remains NO-GO.

Run the maintainer security review aid with `python -B scripts/security_check.py --history`. It scans non-ignored current repository files and reachable objects available locally, including bounded archive members, without extracting or executing them. Exit 0 means no heuristic findings in that scope; 1 requires review; 2 means the scan is incomplete. CI uses a shallow checkout and reports that limitation. It does not fetch remote history or scan student workspaces.


## Complete documentation baseline

See [DOCUMENTATION-INDEX.md](DOCUMENTATION-INDEX.md) for the eighteen requested engineering, security, legal/data, product, architecture, agent and design document categories and pending age/retention/commercial refinements. These are draft policies and scoped requirements, not new runtime/security/host evidence or product release approval. Existing API, frozen contract and ticket status remain unchanged.


## Documentation governance

Accountable owner: Admin, SociusFlow Pte. Ltd. Start with [REPO-BASELINE.md](REPO-BASELINE.md) and [the documentation register](docs/DOCS-REGISTER.md). Unknown profile answers trigger requirements until resolved. All newly assessed register entries remain DRAFT until the owner records approval and evidence. Historical release/security records retain their original evidence date.
