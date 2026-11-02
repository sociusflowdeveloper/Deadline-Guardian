# Host limitations and setup boundaries

**Status:** Repository prototype package. No real Claude, ChatGPT, Grok or second-host installation/invocation evidence is provided by this document. Local helper tests do not prove host compatibility. T08 remains a separate gate.

## Capability-first manual setup

| Host path | Conditional action | Unverified boundary |
|---|---|---|
| Claude environment offering user-managed skills and local Python execution | Follow that environment's current supported local skill-loading mechanism; select this entire folder; inspect its instructions/resources and run the fictional smoke check | Account entitlement, exact UI/install path, filesystem/POSIX support and invocation behaviour have not been verified |
| A second eligible host with a documented user-managed skill-loading mechanism and local Python execution | Load the complete folder only through that host's supported mechanism and run the same fictional smoke check separately | No specific host is certified; support/plan/provider settings must be checked before claiming compatibility |
| Conversation-only or execution-disabled host | Read instructions and produce a manual unverified evidence table if useful; ask the user to run the local helper themselves | Never simulate a successful helper result or claim installation/execution |

Do not install into a personal account, change host settings, purchase a plan or enable external integrations merely to use these instructions. Obtain explicit user direction for such separate actions. Do not bypass unavailable execution permissions or substitute a network service for local execution. Record exact host, date, package version, command, output and limitations only when an actual authorised host test occurs.

## Local operating-system limits

Use Python 3.11+ with only the standard library. Confined input operations require POSIX descriptor-relative no-follow support; export additionally needs same-filesystem hard links. Unsupported platforms/filesystems fail closed, including unverified Windows execution. No third-party packages should be installed to work around failure. Descriptor/inode checks are not an operating-system sandbox against a malicious OS or concurrent same-user/privileged mutation. Cleanup is best effort; crash, permission or I/O failure can leave a private staging/report file. No unconditional durability, recovery or erasure guarantee exists.

## Provider and data boundaries

The helper makes no model/API calls and stores no SociusFlow-hosted account records. The chosen AI host may process, retain or transfer user-provided text independently; verify the actual host settings and terms before sensitive use. Do not promise that this skill disables training or deletes chats/uploads. Use fictional/redacted material for the prototype; stop for identifiable minors, confidential third-party data or unclear rights rather than treating an offline helper as a privacy approval.
