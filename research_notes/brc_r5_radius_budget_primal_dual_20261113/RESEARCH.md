# R5: exact checkpoint-budget/radius Pareto thresholds with primal–dual certificates

Date: 2026-11-13. Status: author-side exact theorem and finite verification; Source Task owner/CLAIM and independent review not established.

## Exact provenance and objective

Scientific input **unchanged**: `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`. The pinned R5 15 labeled integer atoms and `k0` coefficients are reconstructed in `VERIFY_R5_RADIUS_BUDGET_DUAL.py` using exact `fractions.Fraction`. The resulting event wall histogram is `{1:869,2:56,3:28}`, with 953 distinct walls, 954 boundary locations, 1065 activated certificate events. The historical 56-byte center list, representing 213 centers and established mean correction cost 1070, is reused without changing bytes.

Prior related author-side work: draft PRs #2220 (mean-optimal selection at fixed budgets), #2267 (exact radius-cover path census), #2268 (12-byte mean-optimal ranks), #2279 (suffix DP pruning), #2283 (two-sided viable states), #2287 (interval support). Those solve other questions and are not being claimed again. This note asks the distinct **cardinality-vs-radius optimum**: given the actual frozen event coordinates and radius R, is it possible to cover all boundaries using fewer than the historical K checkpoints? Can one give a concise exact lower-bound certificate without enumerating subsets?

## Theorem: interval-cover greedy algorithm and a matching dual certificate

Let `x[0] < ... < x[W]` be any nonempty *strictly increasing real* sequence; centers may only be chosen at these same event locations. Let R >= 0. A center index p covers the interval of boundary indices

`I_R(p) = [L_R(p), U_R(p)]`,

where `L_R(p)=min{b:x[b]>=x[p]-R}` and `U_R(p)=max{b:x[b]<=x[p]+R}`. Define `K_min(R)` as the least number of centers covering every boundary.

Start at the first uncovered boundary index u=0. Choose **the rightmost center index p such that L_R(p)<=u**, append p, record the witness w=u, and advance u to U_R(p)+1. Repeat until u>W.

**Conclusion.** The chosen center family has size exactly K_min(R). Its recorded witness indices `w_1<...<w_K` form a packing certificate: no one candidate center's radius-R interval contains any two witnesses. Thus the greedy centers give an upper bound K, the witnesses give an independent lower bound K, and both bounds match. With monotone two-pointer computation of all L/U, this needs O(W+1) ordered comparisons/operations and O(W+1) space. The attached convenient verifier uses bisect (O((W+1) log(W+1)) comparisons), still exactly rather than approximately.

**Proof.** Since the center p=u covers u, the set of eligible centers is nonempty. Both L_R and U_R are nondecreasing in center index. Consequently choosing the rightmost eligible p maximizes U_R(p) among **all** candidate intervals containing u. Thus it extends the covered prefix as far as possible. If the next witness is v=U_R(p)+1, any interval containing both u and v would be eligible at u yet end after U_R(p), a contradiction. No interval can contain two nonconsecutive witnesses without also containing a consecutive pair, because all center-coverage sets are intervals. So any legal cover needs >=K centers. The constructed K greedy centers cover all boundaries, giving <=K. Therefore equality holds. This proof makes no integrality or uniform-spacing assumption.

For any center budget K>=1 and integer event coordinates, the minimal achievable radius `R_min(K)` is the smallest integer R with `K_min(R)<=K`. Monotonicity of K_min follows because every center's coverage interval expands with R; hence exact binary search on integer R is valid. For rational/real x, the same monotonic criterion holds and changes only at finitely many pairwise distances `|x[i]-x[j]|`.

## Original frozen R5: three exact Pareto breakpoints

The executed checker computes the complete **primal centers and dual witnesses** for each tested R. It verifies directly that every one of the 954 event boundaries is covered and that no possible R-cover interval contains two distinct witness indices.

| Historical budget K | K_min(R-1) | K_min(R) | Provably minimal radius R |
|---:|---:|---:|---:|
| 213 | 351 at R=1 | **213 at R=2** | **2** |
| 57 | 63 at R=8 | **57 at R=9** | **9** |
| 15 | 16 at R=35 | **15 at R=36** | **36** |

Consequently all three existing `(K,R)` design points are genuine threshold points of the original frozen checkpoint-cover problem: their budgets cannot be reduced without increasing the radius, and the radius cannot be reduced at the given budget. The comparison is strictly over these 954 event boundaries and allowed center locations, not a claim about native X6 geometry or all possible R5 distributions.

At R=2, the minimum-size greedy selection yields sum of event correction distances **1104**, whereas the earlier mean-optimal 213-center selection yields **1070**. Both use the minimum possible 213 centers and satisfy radius 2; the mean-optimal variant saves 34 events of total correction (3.08%) *within the minimum-cardinality class*. This independently clarifies the multiobjective structure of the existing algorithm: first minimize radius under a fixed budget, then optimize mean correction without compromising either cardinality or radius.

Additional exact K_min values (R=0..13 and R=35,36) appear in `EXACT_OUTPUT.json`. Selected witness lists can be regenerated deterministically by the checker; they are not claims about any unstored private state.

## Scope and verification

Executed locally with standard-library CPython and exact integer/Fraction operations. The original input sweep verifies 538/298/229 zero-pair counts, 953 wall values, multiplicities, 954 boundaries and 1065 events. Exact original 56-byte sidecar SHA256 is verified, and the 213-center legacy list is decoded directly; it has radius 2 and total cost 1070. All greedy upper and dual lower certificates are checked for R=0..36. Independent direct brute-force enumeration on every array with up to 7 boundary points, gaps in {1,2,3}, and integer radius 0..5 covers **6558 instances**; the greedy optimum agrees with exhaustive subset search every time, and 22182 individual dual witness points are checked. The brute oracle's subset search-space upper bound is 665286. This finite verification corroborates, rather than replaces, the proof for general real x.

This theorem addresses a combinatorial auxiliary checkpoint-index problem. Original 28-coordinate word legality and bitmap/wavelet prefix queries remain at the frozen source and earlier proven scope; this work **does not rerun** the 2747520 original boundary–prefix comparisons or claim end-to-end process latency improvements. The verifier stored here mirrors the locally executed equivalent standard-library program, and the original exact output transcript is represented in `EXACT_OUTPUT.json`. A separate execution of the exact committed GitHub file remains a useful independent check.

## Next scientific unit

Use this exact primal–dual certificate as a budget/radius feasibility oracle when jointly selecting number of checkpoints and mean correction for an actual query distribution; build an exact Pareto table for all budget breakpoints, then integrate the pruned/contiguous dynamic-programming decoders with the original 28-coordinate bitmaps and rational-prefix query workload. Compare all 12/17/33/35/56-byte sidecars with cold-start and process-level RSS, while preserving the immutable scientific input pin. Shared Task owner, native CLAIM, Activity checkpoint and independent Result/Review must be established via their own current Source authorities before reporting those statuses.
