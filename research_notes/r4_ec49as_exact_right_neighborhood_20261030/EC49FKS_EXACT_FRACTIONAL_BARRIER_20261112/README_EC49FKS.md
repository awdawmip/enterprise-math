# EC49FKS — Four exact rational BRC six-key LP optima and their integrality gaps

Date: 2026-11-12. Author-side exact rational finite theorem. Frozen scientific input: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Source lineage: EC49FKQ and EC49FKR in draft PR #1730. Independent Driver admission pending.

## Exact result

Use the unchanged nine-state BRC model, its 178,850 legal operation words and 24 observer labels, all ordered signed-X6 microstep prefixes, and the four residual six-full-cache-key sets indexed 0–3 in EC49FKQ. All contain K4={(2,1,1),(3,0,1),(3,1,1),(4,2,1)}; the extra pairs are respectively (5,4,1)+(5,5,1), (5,4,1)+(6,4,1), (6,3,1)+(6,4,1), (6,3,1)+(7,3,1).

For a chosen allowed-key set K, build the complete literal ordered signed prefix trie V(K). T_i is the set of terminal-prefix nodes belonging to complete admissible words realizing demand i. Relax the EC49FKQ exact binary ILP to nonnegative real variables:

`min sum_(v in V) x_v`, subject to `x_child <= x_parent` and `sum_(v in T_i) x_v >= 1` for all 24 labels i.

| Set | Legal words | Nonempty trie nodes | Exact LP optimum | Integer ceiling | Active primal terminals |
|---|---:|---:|---:|---:|---:|
| 0 | 4366 | 19962 | **1105/12 = 92 + 1/12** | 93 | 100 |
| 1 | 5578 | 26704 | **269/3 = 89 + 2/3** | 90 | 46 |
| 2 | 5578 | 26704 | **269/3 = 89 + 2/3** | 90 | 46 |
| 3 | 4366 | 19962 | **1105/12 = 92 + 1/12** | 93 | 87 |

These rational values are **exact optima**, with complete feasible rational primal and dual witnesses, not solver tolerances.

## Dual charging proof

Let a_i >= 0 denote the 24 certified demand weights, c(v)=sum_(i:v in T_i) a_i, and f_v the nonnegative flow from child v toward its parent. Compute bottom-up for nonroots:

`f_v = max(0, c(v) + sum_(u child of v) f_u - 1)`.

At each first-microstep root, independently check `c(v)+sum_(u child of v) f_u <= 1`. Thus `c(v)+sum_child f_u-f_v<=1` at every node, taking f_v=0 at roots. For any feasible x, terminal coverage and prefix closure give

`sum_i a_i <= sum_v c(v)*x_v <= sum_v x_v + sum_(child u -> parent v) f_u*(x_u-x_v) <= sum_v x_v`.

The last edge term is nonpositive because x_child<=x_parent. This proves an exact rational LP lower bound equal to the displayed sum of weights.

The matching primal certificate lists only positive weights t_w on terminal-prefix nodes. The verification code reconstructs `x_v=max(t_w : w is a terminal descendant of v)`, defaulting to zero. All 24 terminal demand inequalities and all parent constraints are then checked; `sum_v x_v=sum_i a_i` is computed as an exact Fraction identity. The two witnesses establish exact LP optimality.

## Method-class conclusion

The unstrengthened terminal-cover/parent-closure linear relaxation has the four optima above. Consequently its dual flow/weight certificates cannot establish a lower bound of 94 prefixes in sets 0–3, regardless of how those weights are optimized. Integer rounding supplies independently established lower bounds 93 for sets 0,3 and 90 for sets 1,2.

Prior EC49FKQ solver output reports integer optima 98 for all four; the difference between those reported integer optima and the present exactly established fractional optima is 71/12 for 0,3 and 25/3 for 1,2. Independently checkable integer lower-bound proofs for the four remain the next task. This sharply locates the needed integrality-sensitive reasoning.

## Reproduction, input, and status

Run `python3 -S CHECK_EC49FKS_COMPACT.py` from this directory on the full PR branch checkout. It uses the original unchanged signed-X6 generator at `../EC49FJD_RELEASE_B11_COMPLETE_20261111/EC49FGW_RADIUS5_SCREEN.py`, the compact JSON certificate beside it, and Python 3 stdlib only. It enumerates every admissible word in each six-key set, constructs literal prefix nodes sorted by (length, byte sequence), checks every rational inequality and reconstructs the complete dual flows. The original frozen generator also checks its witness source pin. No SciPy, HiGHS, NumPy, floating tolerance, or incomplete sample is used to verify the certificate.

The independent local exact-check run returned:
- set0: 4366 words / 19962 nodes / 1105/12;
- set1: 5578 / 26704 / 269/3;
- set2: 5578 / 26704 / 269/3;
- set3: 4366 / 19962 / 1105/12;
- terminal status: EC49FKS_ALL_FOUR_RATIONAL_LP_OPTIMA_PASS.

Scientific next step: create finite, exactly checkable disjunctive/cover cuts or another integral certificate excluding <=93 prefixes in all four six-key cases, while independently searching seven-key 93-prefix constructions. Reuse the existing EC49FKR integer certificates for cases 4–8 and the EC49FKQ original complete integer witnesses.

State: author-side exact rational LP theorem and finite verification; branch persistence only; no formal Task CLAIM or Result, independent Driver review or Foundation promotion. P000 and ACTIVE worldview unchanged.
