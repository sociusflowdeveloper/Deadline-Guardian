# T05 repository skill package verification

**Date:** 2 November 2026 (Asia/Singapore). **Ticket:** T05 only.
**Specification:** ADDG-SPEC-001 v0.2.0-prototype-contract; CONTRACT.md v1.0.
**State:** Repository package authored and locally checked; independent review/forward-test, PR CI, human merge and actual host invocation remain separate evidence gates. This record is not product-release approval or personal installation evidence.

## Scope and plan comparison

CONFIRMED: Added the canonical `skills/academic-deadline-drift-guard/SKILL.md` with only `name` and `description` YAML fields, narrow academic deadline-comparison triggers and explicit exclusions. Its workflow separates authorised source intake, uncertain extraction, validated local comparison, explicit draft export and user source verification. Source instructions/links/filenames remain untrusted data; no LMS/email/calendar access, network integration, account, paid service, final confirmed export or automatic calendar write is authorised. It does not claim source authenticity or infer source priority/timezones.

CONFIRMED: The existing skill folder/scripts were reused; no initializer or runtime edit was needed. Bundled references provide normative contract sections 1–7, byte-identical schemas, the fictional before/after pair, usage and capability-first host limitations. An unchanged Apache-2.0 LICENSE is included for standalone distribution; this is licence preservation, not new rights clearance. Package tests detect schema/example/licence/contract drift. Only the complete skill folder is self-contained; copying SKILL.md alone is insufficient.

CONFIRMED: Host setup notes distinguish conditional Claude/second eligible-host loading from conversation-only manual use and clearly state no real host installation/invocation was performed. The skill cannot erase provider chats/uploads, disable host retention or guarantee minors/privacy clearance. T08 and legal/IP gates remain open. Runtime version remains `0.3.0-prototype-t04`; authoring a package without executable behaviour changes does not alter the runtime version.

The user expressly requested work in this GitHub repository, not personal-account installation. The skill-creator guide was read and its metadata, progressive disclosure, resource and validation guidance applied. Personal-skills checkout/install/reconciliation steps are inapplicable to this repository deliverable; no personal skills directory was modified and no installed-skill claim is made. Existing folder reuse is the reason the initializer was skipped.

## Added files

- `skills/academic-deadline-drift-guard/SKILL.md`
- `skills/academic-deadline-drift-guard/LICENSE` (unchanged root licence copy)
- `skills/academic-deadline-drift-guard/references/contract.md`
- `skills/academic-deadline-drift-guard/references/snapshot-v1.schema.json`
- `skills/academic-deadline-drift-guard/references/result-v1.schema.json`
- `skills/academic-deadline-drift-guard/references/fictional-before.json`
- `skills/academic-deadline-drift-guard/references/fictional-after.json`
- `skills/academic-deadline-drift-guard/references/usage.md`
- `skills/academic-deadline-drift-guard/references/host-limitations.md`
- `tests/test_skill_package.py`
- This verification record; current status/version/score docs are maintained by the integrator in the same PR.

## Actual checks

| Command/check | Result |
|---|---|
| `python /root/.codex/plugins/cache/openai-curated-remote/work-skill-creator/0.1.2/skills/skill-creator/scripts/quick_validate.py skills/academic-deadline-drift-guard` | Exit 0, `Skill is valid!`; developer-side bundled validator only, no runtime dependency added |
| `python -B -m unittest tests.test_skill_package -v` | Exit 0, 3 tests passed |
| `python -B -m unittest discover -s tests -q` | Exit 0, 69 tests run: 68 passed and one inherited UNIX-socket capability skip |
| `python -m compileall -q skills/academic-deadline-drift-guard/scripts tests` | Exit 0 |
| `git diff --check` | Exit 0 at inspected working state |

The package tests verify minimal frontmatter/name/length and local resource links, exact bundled schema/example/licence parity, exact normative contract-section parity and the documented commands as real subprocesses in a temporary copy containing only the skill folder. The default command generated a CHANGED draft with empty confirmed changes and created no file; the explicit Markdown export generated only the requested additional report. All original copied files were byte-preserved, with no dependency on repository-root files. This tests local package execution, not host loading or agent obedience.

## Independent review and limitations

UNKNOWN until integration: independent reviewer/forward-test outcome, final source commit, current-head CI and human merge approval. A model forward-test is not a real Claude/second-host compatibility test. Python/POSIX/hard-link, cleanup, renderer and concurrent-mutation limits from T04 remain unchanged. A textual prompt cannot enforce a host's privileges or guarantee prompt-injection resistance; T06 independent security work and T08 actual host invocation remain necessary. Do not label the full prototype or public product ready.

## Rollback

Before merge, close/revise this T05 PR. After an authorised merge, use a reviewed revert of T05 package files, package tests and related status/version documentation. Existing runtime helpers and prior user exports remain unaffected; no account, personal installation, remote state or migration exists to undo.

## Integrated independent checks

CONFIRMED: Independent reviewer `/root/review_t05` inspected metadata, contracts, safety workflow and resource parity; reran 69 tests (68 passed, one inherited UNIX-socket capability skip), compile and whitespace checks; the bundled metadata validator exited 0. The reviewer separately copied only the skill folder and executed its helper successfully, and checked all package Markdown links. No material issue was identified.

CONFIRMED: A fresh minimal-context agent `/root/t05_forward` used only the package and fictional request, ran its documented CLI (exit 0), returned CHANGED / VALUE_CHANGED with both exact excerpts, kept confirmed_changes empty, and correctly described omission/conflict precedence and ignored embedded external-URL instructions. This is a local agent forward-test, not a Claude/second-host installation or formal prompt-injection certification.

Human merge/release approval and current-head CI remain separate; subsequent CI evidence is recorded in the PR without rewriting its tested source tree.

A final staged whitespace check found an extra blank line at the bundled contract's EOF that the earlier unstaged check did not cover. The integrator removed it and made the parity test ignore only trailing file whitespace; normative contents remain unchanged. Final staged and committed diff checks were rerun before publication.
