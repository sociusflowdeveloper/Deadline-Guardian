# T01 — Frozen prototype contract v1.0

**Date:** 1 November 2026 (Asia/Singapore). **Engineering disposition:** adopted for the constrained, fictional-data prototype under the user's instruction to work through T00 decisions and T01 schema approval here. This is a delegated engineering decision, not a fabricated human signature, validated-demand result, merged specification or product-release approval. Independent review and the parent decision record identify final acceptance.

**Canonical files:** [snapshot schema](schemas/snapshot-v1.schema.json), [draft result schema](schemas/result-v1.schema.json), [fictional contract cases](examples/contract-cases.json). Schema dialect: JSON Schema 2020-12. These files define requirements. T02 implements snapshot validation and confined input reads; see T02_VERIFICATION.md for its evidence. Comparator and exporter remain unimplemented.

## 1. Scope and precedence

The local helper will use Python 3.11+ standard library only, no network, credentials, hosted accounts, telemetry, paid provider or external write integration. The two schemas plus this semantic contract supersede inconsistent illustrative field examples in earlier documents for prototype implementation. Structural schema conformance alone is insufficient; all semantic rules below are mandatory. The source ZIP remains an unchanged historical document.

## 2. Snapshot structure and bounds

Every snapshot has exactly `schema_version`, `snapshot_id`, `scope`, `sources`, `records`; every defined field is required and unknown fields are rejected recursively. `schema_version` is `1.0`; scope is `partial` or `complete`. IDs are 1–64 ASCII letters/digits or `._:-`, beginning with a letter/digit. IDs are case-sensitive and must not encode personal data; syntax cannot prove absence of personal data.

Each snapshot is at most 1,048,576 bytes of strict UTF-8 JSON before decoding and has at most 100 sources and 100 records. Reject byte-order marks, duplicate JSON object keys, non-finite numeric literals, invalid UTF-8 and excessive nesting (maximum 16 container levels, root object level 1). Do not recursively discover files. Empty sources and records are allowed; records require existing source references. `true`/`false` are JSON booleans, never coercible strings/numbers.

Each source has `source_id`, `source_type` (`text`, `notice`, `brief`, `other`), `label` (1–200 characters), `text` (1–16,000 characters) and `authority_confirmed_by_user=false`. Source IDs must be unique within their snapshot. Full text is a user-supplied fictional extract for provenance checking, not an authenticated institutional document. Source text may contain normal tab/newline/carriage-return; other C0 controls and DEL are rejected. Labels and titles reject all C0 controls and DEL. Lengths count Unicode code points, independently of the input-byte cap.

Each record has exactly the fields in the snapshot schema: stable `module_id` and `item_id`, `title`, split date/time/timezone, precision, source ID, excerpt, cancellation flag and `user_confirmed=false`. Match identity by `(module_id, item_id)`, never by title or timestamp. Several records with the same identity may represent separate candidate notices; the `(module_id, item_id, source_id)` triple must be unique. Duplicate triples are errors, even if identical. Source IDs are snapshot-local; before/after may use the same ID without implying the same source.

Every record's `source_excerpt` is 1–2,000 characters and must be an exact, case-sensitive substring of its referenced source's `text`. Never normalise or repair either string to make it match. This verifies internal quoting only: it does not prove institutional origin, source authority, that the proposed date is semantically supported, or that a cancellation is genuine. Extraction and cancellation assertions remain provisional and require human source review. Embedded commands and hyperlinks are literal data; never follow them.

## 3. Date, precision and cancellation

| State | `time_precision` | `due_date` | `due_time` | `timezone` |
|---|---|---|---|---|
| Date only | `date` | ASCII `YYYY-MM-DD`, actual Gregorian date, year 0001–9999 | null | null |
| Minute, known offset | `minute` | Actual ISO date | ASCII 24-hour `HH:MM`, 00:00–23:59 | Explicit numeric `+HH:MM` or `-HH:MM` |
| Minute, missing offset | `minute` | Actual ISO date | Valid `HH:MM` | null; record is ambiguous |
| Unknown/ambiguous date | `unknown` | null | null | null |
| Explicit cancellation | `none` | null | null | null |

Cancellation requires `explicit_cancellation=true` and precision `none`; all other states have cancellation false. A cancellation excerpt is required like any other evidence. An ambiguous source such as `10/11/26, midnight` is represented as unknown with the original excerpt, never guessed into a machine date. Malformed machine dates are errors, not uncertain records.

Numeric offsets range from -14:00 to +14:00; at absolute 14 hours minutes must be 00. `+00:00` is explicit UTC. `-00:00`, `Z`, IANA names, free-text abbreviations, second precision, leap seconds and `24:00` are not accepted in v1.0. A caller may supply numeric `+08:00` only where the source context supports it; company location is never evidence. IANA/DST conversion needs a later contract revision. Null offset does not become UTC.

Calendar validity is a semantic check: regex alone cannot reject 30 February. Date arithmetic must be overflow-safe at year bounds. To compare two known-offset minute values, subtract offset minutes using ordinal-day integer arithmetic; this avoids creating an out-of-range datetime around years 0001/9999. Preserve original date/time/offset in output even if two representations denote the same instant. Date-only values compare only to date-only values; they are not midnight instants.

## 4. Comparison decision table

Validate both snapshots completely before comparison. A rejected snapshot produces no partial report. Process the union of item identities, sorted lexicographically by `(module_id, item_id)`. Within an identity, retain each original record, sorting by `source_id`; do not discard agreeing sources.

A definite active value is a valid date-only value or a minute value with known offset. Date-only and minute values have different precision and are incomparable, not automatically conflicting. Two minute values compare by their represented instant. Two date-only values compare by calendar date. A cancellation is a separate explicit value. A snapshot has a **definite conflict** if it contains cancellation plus any non-cancellation record (including unknown precision or unknown offset), two different date-only dates, or two different known-offset instants. An unknown record beside a definite active date is uncertainty rather than a definite conflict. A cancellation beside any non-cancellation assertion remains a conflict to avoid silently selecting cancellation. Conflicts remain visible even when additional unknown records exist.

Apply these rules in order for each identity:

| Precedence | Condition | Status / reason |
|---:|---|---|
| 1 | Before contains a definite conflict | `CONFLICT` / `PRIOR_CONFLICT`; preserve it even if the later snapshot contains one candidate |
| 2 | After contains a definite conflict | `CONFLICT` / `MULTIPLE_VALUES` |
| 3 | Before is non-empty and contains unknown precision, timed null offset or a date/minute mixture | `UNVERIFIED` / `PRIOR_UNCERTAINTY` |
| 4 | After absent | `UNVERIFIED` / `MISSING_CANDIDATE`; even when scope says complete |
| 5 | After contains unknown precision or timed null offset, possibly beside a definite value | `UNVERIFIED` / `AMBIGUOUS_CANDIDATE`; never silently ignore the uncertain candidate |
| 6 | After contains a date/minute mixture | `UNVERIFIED` / `INCOMPARABLE_PRECISION` |
| 7 | After is cancellation; before absent | `UNVERIFIED` / `CANCELLATION_WITHOUT_BASELINE` |
| 8 | Before and after are cancellation-only | `UNCHANGED` / `ALREADY_CANCELLED` |
| 9 | After is cancellation; before is one definite active value | `REMOVED` / `EXPLICIT_CANCELLATION` |
| 10 | Before is cancellation-only; after active | `UNVERIFIED` / `REAPPEARED_AFTER_CANCELLATION` |
| 11 | Before absent; after one definite active value | `ADDED` / `NEW_ITEM` |
| 12 | Before/after each resolve to a definite active value of different precision | `UNVERIFIED` / `INCOMPARABLE_PRECISION` |
| 13 | Comparable active values agree | `UNCHANGED` / `SAME_VALUE` |
| 14 | Comparable active values differ | `CHANGED` / `VALUE_CHANGED` |

Several agreeing sources resolve to one value while all records stay in the report. If both snapshots have no records, `changes=[]`. `authority_confirmed_by_user` is fixed false in v1.0 and cannot select a winning source. Before cancellation plus unknown active content is conflicting, not resolved by authority. Missing evidence, inconsistent metadata or unresolved values never produce a confirmed final deadline.

## 5. Draft result

Result fields are exactly `schema_version`, `result_status`, `before_snapshot_id`, `after_snapshot_id`, `changes`, `confirmed_changes`. Version is `1.0`; status is always `REVIEW_REQUIRED`, including an empty report. `confirmed_changes` is always empty. A change contains identity, status, `reason_code`, arrays `before`/`candidates`, source references, `requires_user_review=true`, `user_confirmed=false`. All six statuses remain provisional; unchanged status is not source authentication.

Copy raw record values unchanged into the appropriate side; references contain side (`before`/`after`), source ID and exact excerpt, unique per side/source/excerpt in sorted side/source/excerpt order. Every record has a corresponding reference and no fabricated reference is allowed. Do not copy entire source bodies into the report. Each change identity must match its records and be unique. Output schema structure cannot enforce these cross-field invariants; the implementation must.

No confirmation file, accepted-source input, calendar `.ics`, final import or automatic update is approved by this contract. Export formats are draft report representations only, subject to T04 controls. Escape Markdown/HTML and neutralise CSV formulas at rendering time without modifying canonical raw JSON evidence strings.

## 6. Local CLI path boundary

Require an explicit user-selected existing workspace directory and relative `.json` input paths beneath it, using case-sensitive suffix `.json`. Reject absolute paths, `.`/`..` components, NUL, backslashes and every symlink component. Reject non-regular files and paths resolving outside that root. Use bounded reads; do not scan directories or read environment secrets. Open file descriptors safely and verify file identity to prevent symlink/rename races; lexical checks alone are insufficient. Platform support and negative tests must be demonstrated before claiming path confinement.

The eventual `--workspace`, `--before`, `--after` interface has no default discovery directory. T02 implements validation of paths and files only, without output writes. T04 may introduce an explicit new output path under that workspace, no existing target, no input overwrite, exclusive creation and no unsafe temporary-file race; output failure leaves inputs unchanged. No export implementation is provided here.

## 7. Error priority and taxonomy

1. Workspace/path/file access checks: `UNSAFE_PATH` (including missing/unreadable/non-regular input); byte cap: `INPUT_TOO_LARGE`.
2. Strict JSON decoding/container depth: `INVALID_SCHEMA` (invalid bytes, BOM, duplicates, non-finite constants, parse/depth failure).
3. A parseable object with a present string `schema_version` other than `1.0`: `UNSUPPORTED_VERSION`; missing/non-string version remains `INVALID_SCHEMA`.
4. Structural schema errors, counts and character/precision rules: `INVALID_SCHEMA`.
5. Semantic errors in fixed order: invalid calendar dates `INVALID_DATE`; duplicate source IDs or identity/source triples `DUPLICATE_IDENTIFIER`; unknown source references `UNKNOWN_SOURCE`; missing literal excerpt `INVALID_EVIDENCE`.
6. Unexpected internal failures: `INTERNAL_ERROR`, no traceback or input echo.

Validate before side then after side, following the above priority within each. Within one category report the first lexicographically sorted field path. Invalid counts are structural (`INVALID_SCHEMA`); the byte cap specifically is `INPUT_TOO_LARGE`. A valid uncertain record is not an exception: it becomes UNVERIFIED under comparison rules. Exit codes remain 0 draft report, 2 invalid input, 3 unsafe path, 4 internal failure. A conflict can return a successfully generated draft, never a successfully resolved deadline.

## 8. Acceptance and evidence

T01 provides structural schemas, semantic rules, deterministic status precedence and 37 fictional cases, not implementation tests. The 37 cases include every status, unknown/invalid dates, offset equivalence, active/cancel conflicts, prior conflict, absence in complete snapshots, duplicate identity/source, unknown source, wrong excerpt, hostile text, module separation and invalid fields/version and trailing-newline identifier/date/time/offset attacks.

The default Python environment has no `jsonschema` package. Do not add it as a runtime dependency merely to validate these files. Executed checks: `python /tmp/check_t01_contract.py` parsed two schemas, checked 37 fictional input pairs (22 accepted, 15 rejected at their specified structural/semantic/version gate), and checked one complete sample draft result. These used a scratch standard-library subset checker plus explicit semantic assertions; they are not a complete JSON Schema 2020-12 validator or proof that a future comparator passes. A later T02/T03 test suite must execute all expectations and trust-boundary negatives against actual production code.

Rollback before merge: revise/close the contract PR. After an authorised merge: reviewed revert of these contract artefacts and related spec revision, retaining historical source ZIP/LICENSE; there is no production data migration.

## Final T01 technical acceptance

Independent author/reviewer work and the parent integration checks are recorded in [T01_VERIFICATION.md](T01_VERIFICATION.md). The integrating engineering assistant accepts v1.0 for constrained prototype implementation under DG-DEC-001. This does not imply full JSON Schema library validation, application test success, human PR approval or a product release.
