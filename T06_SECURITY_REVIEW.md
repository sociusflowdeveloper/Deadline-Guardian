# T06 local package security review

Date: 2 November 2026, Asia/Singapore. Scope: frozen v1 contract and local T02–T05 helper/package. This is engineering evidence, not certification or a product-release approval.

## Scope and method

The fresh T06 security agent inspected the runtime, contract, package, CI and existing tests independently of the implementation authors. Its turn was interrupted by a usage limit before its report was saved; the integrator completed this record from inspected source and fresh executed checks. Final independent review is recorded below when available. No production runtime or schema was changed.

New maintainer scanner: `python -B scripts/security_check.py --history`. It scans current non-ignored repository files and available reachable local Git blobs; bounded ZIP members are read in memory, never extracted or executed. Output includes counts, categories and hashed locations, never matched credential values. Exit 0 means heuristic checks passed with limits, 1 means findings need review, 2 means incomplete. The scanner uses fixed local Git subprocesses, separate from the application's no-process/no-network boundary. It is a trusted-maintainer review aid, not a sandbox for arbitrary malicious repositories.

## Fresh executed evidence

- `python -m unittest discover -s tests -q`: exit 0, 76 tests run, 75 passed, one inherited UNIX-socket capability skip.
- `python -B scripts/security_check.py --history`: exit 0; 62 current files, 117 reachable local history blobs, 38 archive-member inspections including duplicate current/history copies; no heuristic matches. Checkout was not shallow. Counts describe the preparation run before this report/final commit, not all remote copies or future commits.
- `python -m compileall -q skills/academic-deadline-drift-guard/scripts scripts tests`: exit 0.
- `git diff --check`: exit 0; staged/committed checks must also pass before publishing.

The seven new tests check hostile source content with blocked socket/HTTP/process/environment access and instrumented file reads; only selected inputs are opened, the private sentinel is absent from output and no workspace files change. They check invalid candidate plus requested export yields no report/file, runtime AST policy with independent negative controls, synthetic credential recognition without value/path disclosure, ZIP traversal names scanned without extraction, bounded/nested archive failure and explicit shallow/no-history scope. Existing validator/comparator/export/package tests cover malformed/oversized inputs, ambiguous dates, conflict precedence, unsafe paths, symlink/replacement races, private exclusive writes, CSV formulas, Markdown injection, redacted errors and copied-folder commands.

## Findings and residual risk

No material local application defect was confirmed by these inspections/checks. This is limited negative evidence, not proof of absence.

| Residual issue | Likelihood / impact | Control and owner | Disposition |
|---|---|---|---|
| Model extraction or source authority wrong | Plausible / high academic impact | Draft-only labels, exact evidence and human institutional-source verification; user and technical owner | Remains; real host behaviour is T08 |
| Same-user/privileged filesystem mutation or crash | Possible / local data exposure or leftover file | Descriptor checks, exclusive 0600 staging/publication and best-effort cleanup; local operator | Not an OS sandbox; inspect files after failure |
| Unknown credential patterns, ignored/unreachable/remote data | Unknown / potentially high | Bounded pattern scan plus manual review; repository maintainer | Not complete secret or personal-data clearance |
| Host retention, rights, minors and publication wording | Unknown / high | Stop sensitive use and release until T07/T08 and privacy review; MD/secretariat/DPO as applicable | OPEN |
| GitHub reporting/settings and external deployment | Unknown / potentially high | Verify configuration and current checks separately; repository administrator | OPEN; no setting changed |

The AST policy is conservative and syntactic: aliasing/dynamic tricks and arbitrary API use can evade it. Patterns are heuristic, not a commercial scanner replacement. CI's shallow checkout scans only available history and reports that limit. Full remote history, external copies, platform push protection/private reporting, provider controls and real host prompt-injection resistance were not verified. The inherited UNIX-socket negative case remains locally skipped; other socket blocking tests execute.

## Decision and rollback

Local technical evidence supports review of T06; formal ticket PASS remains subject to independent review and current-head checks/human approval. Public product release remains NO-GO. Stop for a confirmed severe defect, data leak, unresolved rights or unsafe minor processing. T07–T09 and five demand interviews remain open.

Rollback: close this PR before merge; after authorised merge use a reviewed revert of scanner/tests/workflow/docs. No user-data migration, platform configuration or runtime change to reverse.

## Final independent technical review

CONFIRMED: `/root/review_t06_final` independently reran the 76-test suite (75 passed, one inherited skip), scanner, compilation and whitespace checks, and inspected the full T06 diff. No material application security regression was identified. It confirmed there is no runtime/skill change. Additional limits: ZIP recognition uses a local-header signature; Git list/subprocess output is captured before object-count limits, so scanner memory bounds are not a guarantee for hostile huge repositories. Use only on the trusted maintainer checkout. Current-head PR CI and authorised human merge/release decisions remain separate.
