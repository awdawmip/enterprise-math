# Actual typed reuse for the complete six-block repair

Task `RS-RB-SIX-BLOCK-COMPLETE-HALF-SECTION-OBSTRUCTION-REPAIR`; researcher `EM-RB-1EB0B6`; execution `ER-023A3343CE7FA4FA2AEE`.

The actual current-toolbox query and output are retained in `tool-coverage.run.json` and `tool-coverage.json`. The output's Windows process encoding is recorded below. A lexical match alone is not counted as use.

| Existing interface | Resolution | Concrete application and boundary |
| --- | --- | --- |
| Task-local integer polynomial ring in `check_squareclass_rr.py` | REUSE_EXECUTED | Imported exact pinned source, using its unchanged `add`, `scale`, `multiply`, `reduce_curve`, `twice_delta`, and `restrict_to_critical_divisor`. Only two formal variables are appended, preserving every existing index; no new algorithm or tool family is introduced. The old checker main and old enumeration are not executed. |
| Existing complete `L(2O+T_r)` basis and divisor argument | REUSE_APPLIED | Retain `t/(R-r)` with its finite simple pole, and expand all three compensated sectors. The existing independently checked U remains an auxiliary source; U is not treated as a global map or recomputed as progress. |
| `T0_BRC` / `exact_arithmetic.DivisionExpr` and `brc_integer_value` | REUSE_EXECUTED | Four natural integer coefficient normalizations by 24 produce the compact nonzero field-norm certificate. Literal carriers, quotient/remainder and reconstruction traces are preserved; signs and algebraic field generators are not passed as natural BRC inputs. |
| T0 positive weighted/critical-degeneracy branches | NOT_APPLICABLE | The present carrier is a function field and integer polynomial identities, not a nonnegative branch-weight population. There is no branch mass from which phase cancellation or descent can be inferred. |
| T1, T2, T3, T5, T10, T11, T12 lexical matches | NOT_APPLICABLE | No scale enumeration, independent-block feasibility rule, graph circuit/toppling, precision chain, chain-complex reduction, or Bellman path closure is being asserted. |
| SymPy 1.14.0 | Exploratory symbolic calculation only | A pinned local dependency produced an initial reduction and norm discovery. The final certificate independently recomputes the identities with the pre-existing project integer ring. It is not required to verify the final proof artifact. |

The observer retains each ordered target value, each torsion sector and its arithmetic constant, the complete six coefficients, the sign of each valuation, and the distinction between the geometric cover and the prescribed differential. The final contradiction uses a necessary subset of the full ODE on the larger complete `L(6O)` space. This logically discards no valid solution; it is not a count-based projection or a quotient of source/target labels.

The raw `tool-coverage.json` was produced by Python's Windows default process encoding (GB18030-compatible) and is preserved as actually emitted. The first display attempted UTF-8 decoding and failed after the file had already been written; that display failure did not alter the coverage run. `tool-coverage.utf8.json` is the explicitly decoded UTF-8 copy for portable inspection. Mathematical checkers and their logs use `PYTHONIOENCODING=utf-8`.

No new general capability gap or tool-family claim is made. The reusable mathematical output is the necessary fixed-k condition from a prescribed six-point polar divisor, subject to the explicit nondegeneracy hypotheses in `PROOF.md`.
