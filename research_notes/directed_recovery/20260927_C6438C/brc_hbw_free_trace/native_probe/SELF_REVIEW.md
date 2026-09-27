# Free-trace code-only author review

Status: **STATIC SELF-REVIEW / COMPILE_ONLY / NOT_EXECUTED**. This is an author check, not independent admission. The only Python action in preparation was `python -X utf8 -m py_compile free_trace_probe.py`; no scientific module was imported and no fixture was evaluated.

Candidate pins:

- `free_trace_probe.py`: `2f0981f1dd25e8160bcd80207a6bc92d080e291b545f3be62b95eddffdd36708`.
- `PLAN.md`: `c05b238b7c1f1c72319f6bbe3e41652f2d274f41cc05b6cdaf85e7c6a9e4cb52`.

The binary polynomial step follows the actual characteristic relation `M^2=kM-I`: squaring `(c0,c1)` yields `(c0^2-c1^2,2c0c1+kc1^2)`; appending M yields `(-c1,c0+kc1)`. The initial identity and leading public bit are retained, including a lawful E=0 route. Only public bits control this chain; arithmetic values come from typed modular operations. The complete fixed grid has three inputs and no expected-factor field.

The signed return vectors use principal residues of `M^E v-epsilon*v`. The fixed k is never replaced by a power-dependent trace. Both single-coordinate probes remain separate from their common gcd. The latter performs actual Euclidean divisions on N and each coordinate and verifies proper-factor division; it is not inferred from a trace or combined by a Boolean OR. The plus-return trace-square check follows by applying the same determinant argument to `-M^E`.

Setup, power, readout and validation have separate routes. Full-matrix binary power is solely paid validation; all entries, cyclic residual relations, conic value, determinant and signed common ideals are checked against the saved polynomial result. Standalone gcd receipt caching is exact-key caching inherited from the frozen Route, while joint-gcd divisions stay in the direct arithmetic ledger. Every route constructor and every completed operation remains in the exported evidence; native catalog calls are separate from digit replays. There is no hidden host modular exponentiation, matrix multiplication, remainder or gcd.

The code hashes both proof files and frozen wrapper/runtime sources before native imports, binds the supplied actual guard and record, exclusively creates STARTED, and rechecks source/plan/guard/dependencies at completion. It refuses previous success or failure outputs. Failure capture retains available outer records, routes, completed cases and global native CALLS. It does not claim a complete snapshot of an unreturned primitive/constructor or a resumable transaction.

Boundaries: alternate proper-discriminant and degenerate setup branches are implemented but not exercised by the declared grid. There is no fresh-replay benchmark, saturation recovery strategy, exponent-selection algorithm, randomized success statement, raw HBW trajectory/carry execution, or first-hit histogram claim. The working power registers are constant in number; the retained certificate is not constant in size. No speedup over classical Lucas methods or the earlier conic implementation is predicted.

The source and plan are submitted for separate coordinator and peer static review before any actual execution.

Final pre-execution metadata update: the run binding now uses the coordinator's actual current 8c23cca3 read lease, and PLAN distinguishes it from this author's earlier 7a63984 context. Arithmetic and grid are unchanged.

Global-Knowledge-Sync: main@7a63984 / GLOBAL_KNOWLEDGE_V1.
