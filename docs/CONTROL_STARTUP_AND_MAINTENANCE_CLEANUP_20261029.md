# Startup and maintenance cleanup

Bootstrap no longer calls publication isolation twice: integrity isolation already
installs it first. Integrity installation itself no longer scans all quarantine
rows before and after wiring readers merely to compare task-ID sets. Actual
current-record, merged-definition, operational-selection and audit consumers still
validate the relevant records when they consume them. This does not remove task
blocking, owner authority, or publication concurrency checks.

The two maintenance checkers `check_current_control_authority` and
`check_remote_manual_publication_preflight` no longer certify exact documentation
versions, prose markers, recommended headings or implementation source spelling.
They keep their declared configuration and migration-path checks. Actual native
writers retain operation validation. These scripts are used by the reference
integrity workflow; no runtime speedup is claimed for removing their textual lint.
The publication envelope checker's obsolete five-mandatory-headings description
is corrected; its substantive body validation is unchanged.

Validation: 27 focused Source tests passed. The two maintenance checkers also ran
against actual configuration files from Source aef5826d, without the checked docs
or runtime implementation files present; both passed. Required migration paths
were represented by empty fixture files because these checks only test existence.
This is a configuration check, not full runtime or production acceptance.

Still open: global authority-store/taskbook reads and missing-file subprocess
restarts need a larger data-loading change. No full-catalog latency improvement
is asserted from these bounded edits alone. No research records or live claims
were changed.
