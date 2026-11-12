# Testing and acceptance

**Status: DRAFT.** Reviewed against repository source on 12 November 2026 (Asia/Singapore). Owner approval, live configuration and operational execution are not established by this document.

Python 3.11+ on supported POSIX: python -m unittest discover -s tests -v; python -B scripts/security_check.py --history; python -m compileall -q skills/academic-deadline-drift-guard/scripts scripts tests. CI covers Python 3.11 and 3.13. Critical journeys: strict snapshot validation, ambiguous/conflicting deadlines stay drafts, safe explicit exports, rejected unsafe paths and hostile source text, no network or secret reads. See tests/ and T02–T06 historical verification records. Actual host invocation, rights/privacy clearance and release approval remain independent gates.

Record candidate SHA, commands, exit codes, scope, reviewer and unrun checks in the PR. Documentation changes require path/link and baseline register checks. A passing command proves only its exercised scope. Roll back via a reviewed revert PR; never remove evidence to hide a failure.
