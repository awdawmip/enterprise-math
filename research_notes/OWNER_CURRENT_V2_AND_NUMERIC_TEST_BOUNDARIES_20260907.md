# Current V2 and numerical test boundaries — 2026-09-07

Classification: `NO_NEW_MATHEMATICS_CONTROL_PLANE_TEST_MAINTENANCE`.

This bounded change updates six test modules in the owner integration worktree,
based on `16cc5663c191a73e997e3a973f589197d0694c89`. Production code, mathematical
claims, publication records, result/review data, and the five files frozen by the
preceding parent/publication fixture recovery are unchanged by this assistant.

## Preserved failure evidence

The original `shard_7.log` is retained at
`C:/Users/Administrator/AppData/Local/Temp/em-quality-8shard-20260907-bk6lbjux/shard_7.log`,
SHA-256 `956f976eca7d65e64815fb28b481db710a4812e72369623568563d3b51768538`.
Eight failure blocks concerning these six modules were copied verbatim into
`baseline_failures.txt` in the validation directory below. Their causes were:

- a missing pre-V2 `/composes/canonical_dispatch` key and the obsolete nested
  three-pointer set;
- an old six-pointer-change proposal status instead of the verified current
  architecture state;
- an old pending-governance expectation and pre-cutover runtime migration SHA;
- a claim that the carrier-contact family was resolved despite its live fork;
- the actual BRC error `reduction requires coprimality` for `n=111, m=9`;
- a Decimal residual of `1E-28` against `1E-90` after default-context rounding.

The separate result/review compatibility test with 53 strict audit errors was
not changed or counted as repaired by this work.

## Current assertions

Runtime equivalence now checks the registered V2 pointers
`/canonical_live_dispatch`, `/owner_lease_is_session_liveness`, and
`/stale_valid_owner_action`. It preserves the fresh selector, proves the current
bundle is idempotent, and checks exact task/claim activity evidence in its owning
dispatch contract. Registry assertions bind the current physical cutover
provenance at `9e8dcf5dd44ea4d7eb5aaf7e160a28d5266ebfc9` and the retained archive
manifest, without inventing retired transport fields or CI evidence.

Architecture has six registered pointers and zero changes in
`VERIFIED_NO_POINTER_CHANGE_REQUIRED`. The tests retain all semantic sentinel
digest comparisons and false governance/migration authority flags.

The five unresolved publication families are checked against validated fork
rows, isolated current records, and actual merged dispatch definitions. Every
family remains `BLOCKED` with no publication selection. Previously superseded
carrier-contact generations remain history. The real GEO6 superseded historical
record outside these fork families remains independently validated; that fact
does not grant new task, result, or mathematical authority.

The BRC positive fixture is now `n=19, m=9`, where
`9 * 19 = 14^2 - 5^2` and `gcd(19, 9)=gcd(14, 3)=1`. Its actual scan
representative remains 9. The former `n=111, m=9` state is retained as an explicit
rejection through the same adapter because `gcd(111, 9)=3`. The bounded witness
transport regression and other boundary cases remain intact.

Trace spectral residuals are computed inside a 100-digit Decimal `localcontext`,
matching the coordinate precision. The `1e-90` tolerance is unchanged and the
process's ambient precision is restored on leaving that context.

## Executed validation

Python 3.12.14 on Windows installed
`research_control_bootstrap.install(root)` before importing any tests, then loaded
these six files with the actual quality loader
`scripts.run_unittest_shard.load_file_suite` in one process. **27 tests passed**,
with zero failures, errors, or skips; total time including startup was 11.125
seconds. Module counts were 2, 2, 5, 5, 5, and 8 respectively in the table order.
`git diff --check` passed. Test hashes and the preceding five frozen file hashes
were checked before and after execution and did not change.

Validation directory:
`C:/Users/Administrator/AppData/Local/Temp/owner-six-current-boundaries-20260907-6s4duyxn/`
contains `unittest.log`, `summary.json`, and the eight original failure blocks in
`baseline_failures.txt`. This focused result does not assert whole-shard or full
CI success. No commit or remote write was performed by this assistant.

| Test file | Validated SHA-256 |
| --- | --- |
| `tests/test_runtime_control_migration_equivalence_unittest.py` | `b34313aea1fdd905cd16eaffb07e4276deaf3da3bbe01089f615f1f54cc8ed6e` |
| `tests/test_architecture_publication_cutover_evidence_unittest.py` | `3dbc9929524b5caa7b0f0ef61d80e430aa71cde2d1db47732fe3794133bc33bc` |
| `tests/test_control_semantic_migration_registry_unittest.py` | `d8fa494f160ff12681c1fcf3c125a4a322d497c0657f767d3c4faee5108d9ca5` |
| `tests/test_task_record_audit_fault_isolation_unittest.py` | `52ae9f77e47428e1a29876ebe886525971fc87a12c3ef092198ac1012c5921b5` |
| `tests/test_brc_multiplier_square_content.py` | `84b9accc5ff737fd00460a6aaf5046b455e4e095c5b9ab4a6691ce886be4f170` |
| `tests/test_cyclic_rotation_refinement.py` | `6a0575d6ad2c6d54afe4be37671c6c7b8a3f378cccd6a199696a6622f9b27a87` |
