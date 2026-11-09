# Product requirements — Academic Deadline Drift Guard

**Prepared:** 9 November 2026 (Asia/Singapore). **Organisation:** SociusFlow Pte. Ltd. **Status:** engineering documentation draft for review. Requirements below do not establish implementation, production readiness or legal approval.

## Product and users

Read SPEC.md for the detailed canonical problem, stories and exclusions. Proposed value: a tertiary student compares old/new academic snapshots, sees evidence-linked deadline changes/conflicts and explicitly reviews before changing a plan. Demand is not validated by source inspection; five-user discovery remains a wider-investment/launch gate.

## Functional acceptance

- Accept only explicitly supplied local schema-valid JSON; extraction from text remains uncertain and host-controlled.
- Preserve ADDED/CHANGED/UNCHANGED/explicit cancellation/CONFLICT/UNVERIFIED distinctions.
- Never infer cancellation from mere absence or label unresolved evidence confirmed.
- Produce deterministic draft output with confirmed_changes=[] and no remote calendar changes.
- Persist only an explicitly requested new JSON/CSV/Markdown draft within the workspace.
- Reject unsafe paths, overwrites and oversized/malformed data with fixed safe errors.

## Non-functional requirements

Python 3.11+ standard library, offline, fictional fixtures, no secrets/network/database/billing; safe local paths/exports and bounded resource use. Keep package references/contracts in parity. Host compatibility requires real tests rather than a claim based on packaging.

## Measures and commercial gate

Proposed measures: no silent overwrite or confirmation; all canonical/adversarial fixtures pass; users correctly interpret unresolved status; five discovery interviews and actual host matrix completed. Numerical accuracy/retention/revenue claims need observed evidence. Existing score is an engineering estimate, not approval to sell.

PROPOSAL from current refinement: public eligibility 16+, as a company choice, not a Singapore legal threshold. This does not silently replace the existing initial 18+ research preference in SPEC.md; resolve and record eligibility before launch. Admitting younger users requires a separate decision/safeguards. Subscription app terms and website/AI administrative service terms must remain separate; no billing is introduced here.

Owners: Admin for product/commercial/age decisions; engineering for contracts/tests/hosts; privacy reviewer for data/retention; secretariat for rights/decision records.
