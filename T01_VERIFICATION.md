# T01 technical acceptance and verification

**Date:** 1 November 2026 (Asia/Singapore). **Contract:** v1.0; **SPEC:** 0.2.0-prototype-contract; **Decision:** DG-DEC-001.

## Technical acceptance

**ACCEPTED for constrained prototype implementation** by the engineering assistant under the user's explicit direction to resolve T00/T01 here, following authoring by a separate T01 agent and independent review by `review_t01`. This is technical contract acceptance, not a human signature, empirical demand-validation result, merged specification, legal clearance or product release approval. PR review/merge authority is unchanged.

Independent review found record identity, evidence, precision, cancellation, conservative conflicts and draft-only controls consistent. A cross-regex newline portability concern was hardened with true-end matching and four rejection fixtures. The final reviewer reported no remaining material schema/semantic blocker and accepted this constrained scope. The integrating assistant reran the checks after those corrections.

## Executed checks

1. `python /tmp/check_t01_contract.py` (scratch review helper): exit 0. Two schemas parse; 37 fictional cases, comprising 22 accepted input pairs and 15 expected rejected input pairs; complete sample report structure passes.
2. Independent parent inventory/link/record-definition check via Python: exit 0. Snapshot/result record definitions are identical, all 37 case IDs unique, and expected status cases cover ADDED, CHANGED, CONFLICT, REMOVED, UNCHANGED and UNVERIFIED. Relative links were checked with zero broken targets; final repository count is recorded in the PR.
3. Independent review additionally checked the documented precedence and same-instant offset arithmetic. Expectations are specification fixtures, not generated comparator results.

The scratch helper uses an explicit subset of the schema keywords and calendar/reference/duplicate/excerpt assertions; it is **not a full JSON Schema 2020-12 validator** and is **not included as production code**. Neither the default nor provided primary Python runtime has jsonschema installed; no package was installed or added to the product. Full dialect/metaschema validation has not been executed. The scratch helper path is session-local; do not advertise it as a shipped command. Durable inputs and expected outcomes are in schemas/ and examples/ for later implementation tests.

## Frozen schema identities

| Artefact | SHA-256 |
|---|---|
| `schemas/snapshot-v1.schema.json` | `0c6831326c58760cfd90adac06c9c84bb43111d76e9d4bdb9989dc4e24ce606b` |
| `schemas/result-v1.schema.json` | `7430a9ff5180c1a64e8eb9d237e98ac6008aa0b34a5eeccbad027ed182461be7` |

Any schema change invalidates these hashes and requires renewed contract/fixture review. JSON structural schemas alone cannot enforce calendar validity, cross-record identity/reference/evidence relationships or actual comparison semantics.

## Not verified and next implementation boundary

No production validator/comparator/exporter, input-byte/JSON-decoder security path, filesystem confinement, network isolation, runtime performance, CI success, host installation, legal/IP clearance or product release is claimed. These remain T02 onward. A successful draft may contain unresolved conflicts and cannot be imported as a confirmed final deadline.

T02 can now start in a fresh ticket-limited implementation context using this contract. It must enforce structural **and** semantic rules without adding a runtime dependency and derive real regression tests from the fixtures. T00 interviews are no longer an implementation blocker under DG-DEC-001; they remain open before wider investment/public product launch.
