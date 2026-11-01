# Deadline Guardian — Academic Deadline Drift Guard

> **Current decision, 1 November 2026 (SGT):** The user has authorised resolving T00 discovery decisions and T01 schema here. Proceed with an offline fictional-data prototype under recorded, unvalidated-demand assumptions. The five interviews are a wider-investment/product-launch gate. Canonical T01 artefacts replace earlier illustrative contracts; application execution and product release remain separate gates. See [DECISIONS.md](DECISIONS.md) and [CONTRACT.md](CONTRACT.md).


**Publisher (proposed):** SociusFlow Pte. Ltd.  
**Status:** T02 VALIDATOR IMPLEMENTED / COMPARISON AND EXPORT PENDING / NO PRODUCT RELEASE
**Prepared:** 1 November 2026 (Asia/Singapore) | **Default legal context:** Singapore

> When an assessment deadline changes, see exactly what changed and where the evidence came from, then review it before modifying your plan.

## This package is not a functioning Agent Skill

These files are **pre-repository planning, risk, API and legal drafts** prepared against the SociusFlow checklist. T02 adds a tested local validation CLI. There is still no tested `SKILL.md`, comparator/exporter, remote API, account, database, effective privacy/terms commitment or approved product release. The repository and original ZIP are already public. Rights, trade-mark, security and product-release evidence remain open.

## Documents

| File | Purpose |
|---|---|
| [PRODUCT_DESCRIPTION.md](PRODUCT_DESCRIPTION.md) | Product research, three contenders and weighted decision |
| [SPEC.md](SPEC.md) | Problem, decisions, scope, done criteria, acceptance and stop-ship |
| [TICKETS.md](TICKETS.md) | Small independently reviewable agent tasks |
| [SECURITY.md](SECURITY.md) | Threat model and complete MVP/future backend security controls |
| [CODE_STYLE.md](CODE_STYLE.md) | Python and Agent Skill conventions |
| [DATABASE.md](DATABASE.md) | No-DB decision, transient records and hosted readiness |
| [API_GUIDE.md](API_GUIDE.md) | Proposed offline CLI and JSON schema |
| [PRIVACY POLICY.md](PRIVACY%20POLICY.md) | Draft privacy notice — not approved for publication |
| [TERMS.md](TERMS.md) | Draft user terms — legal review required |
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
3. Start T02 local validator in a fresh ticket-limited context, followed by comparator and exporter tickets.
4. Require actual tests, independent review, rights/privacy checks and a separate MD decision before a public product release.

**Current disposition:** GO for constrained fictional-data prototype work; NO-GO for public product release. T02 validation code exists; comparison and export remain later tickets.

## Current engineering entry points

- [BOOTSTRAP.md](BOOTSTRAP.md): inspected baseline, extraction manifest, verification and rollback.
- [DISCOVERY.md](DISCOVERY.md): T00 interview kit, D01–D16 decision register and T01 contract blockers.
- [CODEX_HANDOFF.md](CODEX_HANDOFF.md): bounded multi-step execution prompt for the next coding session.

The original `SociusFlow_Deadline_Drift_Guard_Pre_Repo_Pack.zip` is retained as an immutable historical source. Root Markdown files are the maintained working copies; do not edit the ZIP to pretend earlier decisions changed.

## Current prototype decision

The user has authorised resolving T00/T01 here. [DECISIONS.md](DECISIONS.md) records the adopted prototype choices and unvalidated-demand assumptions. [CONTRACT.md](CONTRACT.md), [schemas](schemas/snapshot-v1.schema.json) and [fictional cases](examples/contract-cases.json) freeze the T01 contract. [T01 technical acceptance](T01_VERIFICATION.md) is recorded; T02 validator implementation is available; T03 deterministic comparison is next. The validation-only CLI is runnable on the tested Linux environment; no comparator, host compatibility or release approval is claimed.

## Run T02 input validation

Python 3.11+ is required. The safe filesystem reader is implemented for POSIX environments with descriptor-relative no-follow file operations; tested locally on Linux. Unsupported platforms fail closed. No package installation or API key is needed.

```bash
python skills/academic-deadline-drift-guard/scripts/reconcile.py \
  --workspace . \
  --before examples/fictional-before.json \
  --after examples/fictional-after.json
```

Expected: `VALIDATED_INPUTS: review required; comparison not yet implemented.` Exit 0 means input validation only, not a resolved deadline. The command does not generate a report, save output, compare dates or change a calendar yet.

Run regression checks with `python -m unittest discover -s tests -v`. See [T02_VERIFICATION.md](T02_VERIFICATION.md) for actual results, capability skips and review limits.

## Language and code hygiene

Follow [LANGUAGE_POLICY.md](LANGUAGE_POLICY.md): Python for application/tests, JSON for contracts/data, Markdown for documentation and YAML for CI; short fixed shell commands only for CI glue. Keep only relevant code and dependencies. Additional languages, runtimes or frameworks require an approved need and ADR.
