# Existing publication CLI consumes the canonical control bootstrap

Status: `CONTROL_PLANE_MAINTENANCE / AUTHOR_VALIDATION_PASS / NO_NEW_MATHEMATICS`.

This change repairs the existing `tools/research_task_records.py` entrypoint. It
does not create a second publication command or grant publication, claim,
mathematical review, Working Truth, Foundation, or promotion authority.

## Observed fault and exact source boundary

On public main `bef9cce0ee3f452ac8d7a6f1c4ff7246f1fcdbef`, the direct command
`python -B -X utf8 tools/research_task_records.py audit` returned exit 1 with the
same P000 publication-fork error twice. The raw implementation audit and the
historical-heading compatibility audit both reached the uninstalled strict
current-record selector.

The task `RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE` already has an exact validated
`UNRESOLVED_PUBLICATION_FORK` row in
`research_task_publication_quarantines.json`. Its three heads are:

- `TP2-3F6A92D8C1E740B5A2C9`;
- `TP2-4A84B81FD5CAB8CD0359`;
- `TP2-FBDBDBE1C5BDF65F97A0`.

The row selects no operational publication and grants no authority. There is no
operational resolution for this task. The resolution/quarantine registries,
publication adapter, bootstrap, facade, core implementation, current-authority
router, and all 23 publication records of this task are unchanged between the
earlier failed-publish base `1e338a83e19d45557de1d3e0026b606017d224fc` and `bef9cce`.
This is a missing CLI initialization step, not permission to resolve the fork.

The A3 generation-2 record `TP2-A60A8F985112CCF96B3B`, created by a separate
owner invocation before its post-write audit failed, is not in this main
snapshot or this patch. It was neither republished nor deleted for this repair.

## Minimal implementation

`main()` installs the existing `research_control_bootstrap`, then explicitly
uses the canonical `tools.research_task_records.audit` and `build_record` while
calling the existing core CLI. This distinction matters when the executing
facade is `__main__` or the historical bare `research_task_records` alias:
bootstrap patches the canonical module, not every separately imported facade.
The existing `finally` restoration of the core call bindings remains intact.

No audit error is caught or newly suppressed by this patch. The original
`_STRICT_AUDIT` and `_STRICT_BUILD_RECORD` handles and the core source remain
unchanged. In a fresh process before bootstrap, the original strict audit still
reports the fork. After bootstrap, that function's existing module-global
selector dependency is intentionally the canonical isolated selector; retaining
the function handle is not a claim that all its dependencies remain uninstalled.
The existing exact quarantine validators continue to determine admissible
control isolation. P000 remains absent from current-record selection.

## Actual bounded validation

Python 3.12 was used with bytecode writing disabled and UTF-8 mode enabled.
The same direct CLI audit after the facade change returned exit 0:
`PASS: immutable task publication records valid (273 generations).`
The measured subprocess duration was 10.215422 seconds.

The final focused command was:

```text
python -B -X utf8 -m unittest tests.test_publication_cli_canonical_bootstrap -v
```

It passed 5 tests in 138.225 seconds (138.451735 seconds for the captured outer
process). Nine fresh subprocess invocations used one disposable copy of the
tracked source; fixture publications and deliberate corruption existed only
there. No checkout taskbook, record, resolution, or quarantine was edited.

| Boundary | Actual result |
| --- | --- |
| Direct existing CLI, with registered exact quarantine | Audit and unrelated synthetic publication succeed |
| Bare-first, canonical-first, bootstrap-first then bare | All three audit invocations succeed; strict handle identities and call restoration hold; P000 has no current publication |
| Quarantine row removed for the same three-head fork | Audit rejects the original fork |
| New taskbook loses a required section | Publish rejects it without creating a record |
| Pinned taskbook of quarantined history changes | Audit rejects taskbook blob drift |
| Newly published unrelated record grants Working Truth | Audit rejects the new record; no historical suppression applies |

The first test run is preserved as a failed fixture run. Its incorrect expected
body-error wording and an audit-only fixture's prepared-but-unpublished book
caused four assertion failures. The production rejection was correct. Only the
test expectation and fixture lifecycle were corrected before the final run;
the production facade hash was identical in both runs.

Executed source SHA-256 values:

- facade: `458005975ebd84c402a52975ce75fc24f5a90fae76e8901996222c4cad0370be`;
- test: `6a429271497800e53f6c38ec7e88ecd613424086183ae4d8a144fd4a3ed4f574`.

Local execution evidence is under
`D:/em/TEMP/owner-publication-cli-bootstrap-20260908/`:

- `diagnosis-and-preservation.json`: `662044b930857508a35defc9bff619dc18458b25ca34d7c661266b913915129e`;
- `after-audit-receipt.json`: `1594017508aa5368666ea3eca2f92febc8213784c405b89dba01ff689c75f68e`;
- `focused-run-2-receipt.json`: `a2e281e3403d4e4765ff01de8bf7697e856e25ea96877bb79d900588800e380b`;
- `subprocess-receipts-run-2.json`: `cb9077ea9867b09a3595bd5ebdfcd8603a9f77a456fef9094593c7b7752c9f29`;
- retained first-run subprocess receipt: `9c06ae58e226d2750fc951f6aa0ad7982e3368bebc30559d371fb69e0a8c653b`.

The baseline contains 4,615 tracked entries. The facade is the only changed
baseline path; all other 4,614 files match their baseline Git blob bytes.
The test and this note are the only added paths. These are author execution
receipts, not an independent Driver mathematical review or a statement that
the patch has already passed remote CI or entered main.

Driver-ID: EM-DVR-01E1D9 / CONTROL_PLANE
Global-Knowledge-Sync: main@d5a17f8 / GLOBAL_KNOWLEDGE_V1
