# EC49FRZ — Original BRC joint-discount complete 10-phase theorem

Status: `AUTHOR_PROVED / EXACT_FINITE_BELLMAN_AND_FULL_TREE_REPLAY / NOT_REVIEWED`.
Date: 2026-11-18. Scientific input immutable pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
Lineage: EC49FRV #2660, EC49FRW #2663, EC49FRX–FRY #2666; this is an independent portable continuation, not a formal CLAIM/Result/Review.

## Exact mathematical statement

Keep original BRC class 16943, 141 complete *named* states, 310 source configurations, and **all 228 original physically named observers** with their original complete response partitions. Fix the uniform prior over the 141 named states and baseline observation price `t>0`. Only observations `q32,q34` receive identical discounted price `(1-s)t`, `0<=s<=1`, with the other 226 named observers costing `t`. A strategy is any legal complete adaptive native decision tree separating all 141 names. Define `U(Q)` as total original-observation uses over the 141 state paths and `K(Q)=N32(Q)+N34(Q)`. Thus `141 C_Q(s)/t=U(Q)-sK(Q)`.

**Theorem.** The unrestricted all-tree exact Bellman optimum `F(s)=141V(s)/t` on every real `s in [0,1]` is the following continuous, concave, piecewise-affine function:

| Region | U | K | F(s) |
|---|---:|---:|---|
| [0,1/4] | 296 | 152 | 296-152s |
| [1/4,1/3] | 297 | 156 | 297-156s |
| [1/3,2/5] | 304 | 177 | 304-177s |
| [2/5,1/2] | 306 | 182 | 306-182s |
| [1/2,5/9] | 310 | 190 | 310-190s |
| [5/9,3/5] | 315 | 199 | 315-199s |
| [3/5,2/3] | 321 | 209 | 321-209s |
| [2/3,3/4] | 337 | 233 | 337-233s |
| [3/4,4/5] | 343 | 241 | 343-241s |
| [4/5,1] | 355 | 256 | 355-256s |

Each row has a complete original native tree witness, reaching its displayed affine cost. There are precisely ten distinct strictly optimal affine cost types over the open regions: **ten cost types are sufficient and necessary** for a fixed complete-tree menu covering the full discount diagonal. This theorem extends prior exact results from `s<=3/5` through `s=1`, adding phases after `3/5` and transition abscissae `2/3,3/4,4/5`. All ten exhibited witnesses have first physical named observer q32 and worst depth at most four; no claim is made that q32 is the unique optimal root.

## Finite Bellman proof and complete continuous lift

For a nonempty subset S of the 141 named states let `R_q(S)` be the children induced by original observer q's exact response. For singleton S let `D_s(S)=0`. Otherwise the unrestricted native recurrence is

`D_s(S)= min_{q in {0,...,227}, |R_q(S)|>=2} [ |S| p_q(s)/t + sum_{T in R_q(S), |T|>=2} D_s(T)]`.

Each nontrivial split strictly reduces cardinality, so this is a terminating, exhaustive finite Bellman recurrence. The implementation uses exact rational arithmetic and original named responses for all 228 observations. The 11 vertex results are:

| s | Unrestricted exact `F(s)` |
|---|---|
| 0 | 296 |
| 1/4 | 258 |
| 1/3 | 245 |
| 2/5 | 1166/5 |
| 1/2 | 215 |
| 5/9 | 1840/9 |
| 3/5 | 978/5 |
| 2/3 | 545/3 |
| 3/4 | 649/4 |
| 4/5 | 751/5 |
| 1 | 99 |

The complete 10 witness trees, inherited frozen data, executable native solver, replay/certificate code and true execution log are in the accompanying SHA256-manifested 23-file self-contained evidence archive; the six new upper-half witnesses have (U,K) `(310,190),(315,199),(321,209),(337,233),(343,241),(355,256)`. The four earlier ones from the frozen EC49FRY evidence are `(296,152),(297,156),(304,177),(306,182)`. Each tree was replayed on 141/141 named state paths, with exact observation counts and correct distinct leaf; no tree exceeds depth four.

For each closed interval between consecutive listed vertices, one witnessed complete tree is optimal at both endpoints. The unrestricted Bellman value is the pointwise infimum of affine tree costs, hence concave in the real variable s. Its concavity supplies a lower bound given by the endpoint chord, equal to the exhibited tree's affine cost; the exhibited tree supplies the matching upper bound. Therefore equality holds at **every real s** in the whole interval. This is an analytic continuum proof based on complete finite endpoint computations, not interpolation over a floating-point grid. At s=1 the two prices are zero; the recurrence remains well-founded because observers must strictly split S.

Each distinct affine gradient occurs on a nonempty open interval. A fixed native tree optimal on the full continuum in each region must have the corresponding affine cost type; ten different gradients force at least ten types, and the exhibited ten attain the bound.

## Scope, reproducibility and next question

The theorem is internal to this original frozen named-state BRC identification model, its **uniform named-state prior** and specified price perturbation. The `s` parameter is a **price discount**, not physical heartbeat time. No classical-trigonometric or non-BRC physical dynamics are introduced. Prior state, source names, branch/multiplicity and observer partitions are retained. Full reproduction: run `python code/EC49FRZ_VERIFY_ALL_TEN_PHASES.py --full` from the self-contained archive root (Python stdlib). The verified run reported 10 complete trees × 141 paths plus 11 exact full-228 Bellman vertex computations, all passing. Archive label: `EC49FRZ_NATIVE_BRC_FULL_DIAGONAL_TEN_PHASE_COMPLETE_EVIDENCE_20261118.tar.xz`, 216892 bytes, SHA256 `6bdfe4f316b0bc11f107fe9eeb37f584561534c05f529e6b8f6cc5e522c6b422`. This PR contains a portable theorem and index; the archive also contains the verbatim large source and complete trees.

Next: determine the exact non-diagonal phase walls in `[0,1]^2` for independent `q32,q34` discounts, extending the established `[0,1/2]^2` theorem, and classify minimum native-tree menu and optimal-root changes. Authenticated Source control/owner lookup is currently affected by backend identity-check unavailability; this preservation is independent portable research only. No formal CLAIM, Result, Review or Activity publication is asserted.
