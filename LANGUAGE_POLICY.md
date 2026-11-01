# Language and code hygiene policy

**Effective engineering instruction:** 2 November 2026 (Asia/Singapore).
**Scope:** Deadline Guardian only. This policy implements the user's instruction to use only relevant, preferred languages. It does not introduce a feature, dependency or runtime.

## Preferred languages and formats

| Purpose | Preferred choice | Boundary |
|---|---|---|
| Application logic, CLI, validation and automated tests | Python 3.11+ | Standard library only for the current prototype; follow the canonical contract. |
| Schemas, fictional fixtures and machine-readable draft data | JSON | Strict JSON; no comments, executable expressions or substitute serialisation formats. |
| Requirements, agent instructions and technical documentation | Markdown | British English; examples must distinguish implemented behaviour from proposals. |
| GitHub Actions configuration | YAML (`.yml` or `.yaml`) | Declarative workflow configuration with minimal permissions and immutable action pins. |
| Existing CI command glue | Short, fixed POSIX-compatible shell commands | Invoke Python/Git tools only as needed; no application logic, hidden installers or interpolation of untrusted data. |

Python is the sole approved **application programming language** for this prototype. JSON, Markdown and YAML serve their listed data/documentation/configuration purposes. Shell is limited to CI glue, not a second application implementation. A listed format does not authorise a feature that SPEC.md or CONTRACT.md excludes.

Do not introduce JavaScript/TypeScript, HTML/CSS frontends, SQL, Rust, Go, Java or another language/runtime/framework merely because an agent knows it or a template includes it. GitHub Actions' internal implementation languages are upstream dependencies, not permission to add those languages to product source. Preserve required standard files such as LICENSE and .gitignore, and the unchanged historical ZIP; their presence is not a policy violation.

## Relevance and hygiene rules

- Use the smallest existing language/tool set that satisfies the authorised ticket. Prefer existing modules and Python standard-library facilities over new packages or build systems.
- Add a file, module, dependency or abstraction only for a concrete requirement. Do not add unused imports, dead functions, duplicate implementations, scaffolding, placeholder services, vendored code or generated bundles without a justified need.
- Keep one canonical implementation of each responsibility. Extend the established validator/comparator seams rather than creating another implementation in a different language.
- Remove code made obsolete by the same change where safe, checking callers and tests first. Do not remove unrelated or historical work under the label of cleanup.
- Keep source code, fictional data, documentation and workflow configuration in their established directories. Do not commit caches, local environments, secrets, real student documents, compiler output or unrequested exports.
- Keep interface/schema versions, names and language conventions consistent. Do not change behaviour through a formatting or cleanup PR.
- Do not add a formatter, linter, dependency manager or automatic rewrite merely to enforce a style preference. Use the documented checks; tool additions need a demonstrated benefit and explicit scope.

## Exceptions and review

A genuine new-language/runtime/dependency requirement must first be documented in an ADR and affected specification: unmet need, alternatives using the preferred stack, maintenance/security/licensing/cost implications, migration/rollback, owner and approval. Obtain the relevant decision-owner approval before introducing it; a package being available is not approval. Keep exception scope narrow. Ordinary work within this policy needs no repeated approval.

Each implementation PR must confirm: only relevant preferred languages/formats were added; no unused or duplicate code/dependency was introduced; scope and contract are preserved; appropriate tests/compile/whitespace checks ran. Documentation-only changes need proportionate link/diff review, not invented application test results.

**Enforcement status:** Repository instructions and PR-review criteria. No automated language-allowlist scanner, formatter or new lint gate is installed by this policy change.
