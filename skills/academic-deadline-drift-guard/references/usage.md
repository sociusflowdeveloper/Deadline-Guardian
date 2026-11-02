# Usage and reporting

## Local fictional smoke check

Run the SKILL.md command from the skill folder. Expected draft: module MKT101 / report, CHANGED / VALUE_CHANGED, earlier 12 November 2026 17:00 +08:00 and candidate 14 November 2026 17:00 +08:00. Show both fictional excerpts. The example is deliberately fictional and does not validate demand or source authenticity.

The entire skill folder can be copied without the rest of the repository: scripts, contract sections, schemas, example pair and licence are bundled. Do not copy only SKILL.md. Do not run a downloaded helper without checking trusted provenance and the exact version; this package does not install itself.

## Explicit fictional export

From the copied skill folder, after the user requests this new filename:

```bash
python scripts/reconcile.py --workspace . --before references/fictional-before.json --after references/fictional-after.json --output fictional-draft.md --format markdown
```

The parent directory must exist. An existing filename is rejected; choose another new user-approved filename for a subsequent run. Formats are json, csv and markdown; suffixes are .json, .csv and .md. Success prints `EXPORTED_DRAFT: REVIEW_REQUIRED; no confirmed changes.` It does not print the report body on export success.

## Error handling

| Exit | Meaning | Response |
|---|---|---|
| 0 | Draft generated or explicitly requested draft exported | Report review required; do not apply dates |
| 2 | Invalid input, schema/version, size or arguments | Report the fixed category/path; ask for corrected source/input |
| 3 | Unsafe/inaccessible/unsupported path or failed export I/O | Stop; keep inputs unchanged; inspect requested destination for incomplete cleanup |
| 4 | Unexpected internal failure | Stop; do not expose input or stack traces; do not claim a file was saved |

Do not include private filenames/source content in shared diagnostics. Treat errors as failures even if a partial display or private staging file exists. CSV neutralises formula prefixes and quotes fields; Markdown escapes literal markup/HTML and autolink punctuation. Text exports are display representations, not canonical round-trip data. JSON preserves the canonical raw evidence strings. Spreadsheet imports, re-saves and nonstandard Markdown renderers need separate validation.

## Review checklist

Report old and candidate values, status/reason, excerpt and source reference per side, and unresolved ambiguity. For conflicts say “verify the original institutional sources” rather than choosing an authority. For missing candidates say that omission is not cancellation. For unknown timezone preserve the uncertainty. Do not claim every unchanged record is authenticated. Keep the user's manual source-verification decision separate from the prototype's permanently unconfirmed output.
