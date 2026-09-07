# Parent and publication fixture recovery — 2026-09-07

Classification: `NO_NEW_MATHEMATICS_CONTROL_PLANE_TEST_MAINTENANCE`.

Scope: four test modules in the owner control integration worktree, based on
`16cc5663c191a73e997e3a973f589197d0694c89`. This note records a local test result;
it does not assert a main merge, whole-suite pass, task publication, or review.

The complete runtime bootstrap installs the current semantic isolation wrappers.
The old temporary fixtures omitted the mandatory nonempty semantic quarantine
registry. Some also lacked a real taskbook, Git blob pin, registry key, or V2
publication transaction. Those failures prevented the tests from reaching their
intended parent-binding and publication-selection assertions.

The compatibility test module now provides private fixture functions that create
actual book and record bytes. Its independent synthetic semantic fault has a
source-backed identity difference, a removed source reference, exact record/book/
source pins, and all authority flags false. The other two fixture consumers import
only these functions, not a `TestCase`. A regression confirms the semantic record
has no operational selection and that changing its source bytes is rejected by
the real semantic validator. No selector, validator, production file, registry,
or repository taskbook was changed to accommodate the temporary fixtures.

Parent closure retains all seven original cases, including bound terminal
children, unbound children, nonterminal cohort precedence, the unproven sidecar,
and missing objective selection receipt. Publication selection retains all eight
cases; retained-history assertions now compare the exact target-task publication
IDs so the unrelated semantic fixture does not alter their meaning.

The legacy PRE_FINAL case separately verifies its unbound projection and the
current runtime's actual rejection of `LEGACY_BASELINE_REGISTERED`. An additional
case uses valid `IMMUTABLE_REGISTERED` registration and a current publication
without a parent binding. It reaches the intended business gate, rejects caller
`COMPLETE`, and refuses the forged parent-completion terminal event. The existing
open-parent, incomplete-runtime, cohort, user-stop, and valid-completion cases
remain intact.

## Executed validation

On Windows with Python 3.12.14, the runner installed
`research_control_bootstrap.install(root)` before importing any test, then used
the actual quality shard loader `scripts.run_unittest_shard.load_file_suite` for
all four modules in one process. The result was **31 tests passed**, with zero
failures, errors, or skips: parent closure 7, PRE_FINAL 10, compatibility 6,
operational publications 8. Test execution took 43.096 seconds; the complete
run including startup took 54.281 seconds. `git diff --check` also passed.

Local evidence directory:
`C:/Users/Administrator/AppData/Local/Temp/owner-control-fixture-recovery-20260907-3wt88l1l/`
contains `unittest.log` and `summary.json`. The original eight-shard failure logs
were not overwritten. The remaining full quality workflow is an owner integration
gate and is not implied by this focused result.

Validated file SHA-256:

| File | SHA-256 |
| --- | --- |
| `tests/test_research_parent_closure.py` | `75570143941ef178c7a47590d1286d67b923d3ff66b3e9b15f6778c632fe42d0` |
| `tests/test_research_pre_final_authority.py` | `c4475ded0d502a9f8785aee35a54adbaded9a418b51cb2f3f69577675eeceed8` |
| `tests/test_research_task_record_compatibility.py` | `f3d1c52c6f8d604ff657e39d91f08402d40d81079b2401da6b6e473c840620b9` |
| `tests/test_research_operational_publications.py` | `65c0e74ad84979758c399ec4939d013b8727aec9ffcd7993cae142c091a46b4b` |

No commit or remote write was performed by this internal maintenance assistant.
