# Full-bootstrap quality fixture completion

Status: `VALIDATED_TEST_ONLY_REPAIR / NO_NEW_MATHEMATICS`.

Scope: three explicitly assigned test files in `D:/em/integration-owner-control-20260907`. No production checker, dispatcher, authority registry, publication, or earlier frozen 38-test source changed. The earlier provenance independent audit remains evidence about its original snapshot; this note records the subsequently authorized test-fixture correction.

## 1. Actual failure and classification

The original quality runner used Python 3.12.14, frozen Git tree `8258a5be611c521cfe5b22ff011efcde88e8ddce`, shard `0/8`, and the workflow's separate-heavy-job exclusion of `tests/test_p017_mirror_cross.py`. Its 291 tests reported 10 failures and 1 error in 33.133 seconds. Original log: `C:/Users/Administrator/AppData/Local/Temp/em-quality-8shard-20260907-bk6lbjux/shard_0.log`, SHA256 `33f0dcf7c2f62c8dd9b03b174abed05b917bad1884a91f3638477a0c2a6fb39f`.

A separate actual reproduction first called `research_control_bootstrap.install(Path.cwd())`, then ran the three modules serially in that same Python process: 33 tests, 10 failures and 1 error, in 0.354 seconds. Log SHA256 `9ca292bdcdc65508e8c1e6663b249af2a202a74ff94eaac311ceebafd041ce27` (`TEMP/owner-quality-fixture-baseline-20260907.log`). These are three distinct test-data/expectation omissions, not newly demonstrated production authorization failures:

1. `test_control_semantic_verification_requests_unittest.py` still assumed an open request had a future publication object. The current request is `CLOSED_NONEXECUTABLE_HISTORY`, with `RESOLVED_NO_TASK_REQUIRED_CURRENT_VALUES_ALREADY_CANONICAL`, zero pointer changes and `future_authorized_publication: null`. `check_control_semantic_verification_requests._check_closed_request` expressly requires that null. This particular null is a closed no-change request, **not** a selected task publication being quarantined.
2. `test_research_runtime_unittest.py` omitted two canonically owned paths from an exact expected set: `tools/research_dispatch_core.py` and `tools/research_driver_queue.py`. Both are already in `research_runtime_state_machine.json` and documented by `docs/RESEARCH_RUNTIME_STATE_MACHINE.md`. The former implements the dispatch facade; the latter only discovers review work. Neither becomes a new independent live entrypoint or acquires review authority through this test change.
3. `test_taskbook_publication_provenance.py` omitted the mandatory nonempty semantic-integrity registry and its exact source/record dependencies. After complete bootstrap, persistent operational wrappers correctly reject that missing fixture registry before reaching the intended orphan, binding and strict-error assertions. An isolated module run without those wrappers had not exposed this test-order dependence.

## 2. Repair and preserved boundaries

The semantic-request integration tests now assert the actual closed-history state, all four nonexecutive flags, null future publication, zero changes and false task/governance/migration grants. A separate explicit temporary OPEN-request fixture retains the former positive `GOVERNANCE`, V2 contract, immutable publication-tool and permitted-publisher requirements. The real `requests.check` accepts it. Separate mutations reject wrong kind, wrong contract, wrong tool, an unauthorized publisher, and each attempt to turn the request into an executable/authoritative task. This fixture does not reopen the repository request or create a publication.

The runtime test adds exactly the two existing owned paths. Exact set equality, executable-runtime binding, all documentation checks, and every owner/session/registration/terminal assertion remain unchanged.

The provenance module installs the complete real bootstrap on the repository in `setUpModule`. Each temporary fixture contains an independent synthetic semantic-preservation fault with real publication/book/source bytes, exact Git-blob pins, distinct source and observed identity projections, a missing source-reference witness, separate migration provenance, and all authority grants false. The pre-migration source artifact is outside the published-taskbook scan, while the actual published fixture book has ordinary immutable V2 provenance. The source registry's nonempty requirement is retained; no empty-registry shortcut is used.

As in the original author test, only re-installing unrelated global review policy on the minimal temporary root is stubbed during `gate.audit`. The complete bootstrap has already installed its actual persistent wrappers. No strict validator, quarantine validator, error collection, selection or result is mocked. The added regression independently calls the real semantic validator, confirms provenance acceptance, `operational.selection(...) is None`, absence from current records, a `BLOCKED` definition with no publication, and source-pin drift rejection. All original 13 tests and their orphan/path/id/blob/state/manifest/fork/audit-only/extra-error/stale-error assertions remain present and now execute past the missing-registry boundary.

## 3. Validation and exact replay

Interpreter: `C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe`, Python 3.12.14. No dependency installation or production mutation.

Combined regression, with real full bootstrap preceding test imports:

```python
from pathlib import Path
import unittest
from control_plane import research_control_bootstrap
research_control_bootstrap.install(Path.cwd())
suite = unittest.defaultTestLoader.loadTestsFromNames([
    'tests.test_control_semantic_verification_requests_unittest',
    'tests.test_research_runtime_unittest',
    'tests.test_taskbook_publication_provenance',
])
result = unittest.TextTestRunner(verbosity=2).run(suite)
raise SystemExit(not result.wasSuccessful())
```

Run using the interpreter above with `-X utf8 -B -`, cwd the integration checkout. Result: **36 tests / 2.934 seconds / OK / exit 0**. Log `TEMP/owner-quality-fixture-final-20260907.log`, SHA256 `a83b2b3a5d72eb8f3537fd9e61944f9f84bdf3e0e606109424c6511395f16610`.

To preserve the original failure and avoid a changed test-file inventory, the shard replay used a fresh TEMP clone of the original frozen repository, materialized exactly tree `8258a5be611c521cfe5b22ff011efcde88e8ddce`, overlaid only the three final test files below, and applied only the same heavy-job exclusion. It did not overwrite the original shard clone or log. Replay directory: `C:/Users/Administrator/AppData/Local/Temp/owner-quality-shard0-repair-20260907-j7yjcsgr`; its `inputs.json` binds the base tree, old failure-log digest, interpreter, exclusion and three overlay hashes.

Actual command from its `replay` directory, with `PYTHONPATH=src`, `PYTHONUTF8=1`:

```text
<Python3.12.14> -X utf8 -B scripts/run_unittest_shard.py --index 0 --count 8
```

Result: **294 tests / 34.019 seconds / OK / exit 0**. The increase from 291 is exactly two semantic-request tests and one provenance semantic-fixture test. Replay `shard_0.log` SHA256: `1918b06f778f6ff6741f23cf3074ef31b00fc0c97cdbe01e2355118e2d4b4bfe`. `git diff --check` passes for these test changes. This is a successful repaired shard-0 replay and combined regression, not a claim that all eight shards or the complete merge gate have finished.

## 4. Frozen test bytes

| File | SHA256 |
| --- | --- |
| `tests/test_control_semantic_verification_requests_unittest.py` | `e89e0dbe7252aa64ed7dc4ce6b6f6a0af1fd9fb0e893e1b0d58b80e2f312fa8a` |
| `tests/test_research_runtime_unittest.py` | `c050ba63181954f2e7fa19ade46fa376d26dfcee334bab94c4fd121a4f3f8267` |
| `tests/test_taskbook_publication_provenance.py` | `38eb1a691b1af455cec4cee53a84409dd529b4a986e2c01c887d99a929038794` |

Auxiliary control-maintenance work package `/root/exact_solver`; no Researcher-ID allocation, official claim, publication, approval or promotion is asserted. No commit or push performed.

Global-Knowledge-Sync: main@ad23151 / GLOBAL_KNOWLEDGE_V1
