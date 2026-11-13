# Complete minimum-edit spectrum after any one of R5's 28 gap closures

Date: 2026-11-14. Status: author-side proof and finite exact verification; independently reviewed Result **not** yet claimed. Scientific input is held fixed at `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`. The 15 original integer atoms yield 953 exact rational threshold values, 954 cumulative integer event boundaries and 1,065 activation events. All claims are for this derived one-dimensional **integer-event sampling model**, radius two and center indices among the observed boundaries. Native six-axis space and the separate 2,520-byte / 28-coordinate / 8,192-query benchmark are not being repinned or evaluated.

## New complete classification

For each zero-based cut `c = 0,...,27`, close exactly one of the original 28 separating event gaps `3 -> 2` by translating the suffix left by one. Let `Opt_c(K)` be the minimum-total-distance center sets of cardinality `K` subject to radius-two coverage, and define

`rho_c(K) = min{|S\\T| : S in Opt_c(K), T in Opt_c(K+1)}`.

The exact results for **all 28 perturbations** are:

| Transition | Number of (cut, transition) instances | Minimum deleted old centers |
|---|---:|---|
| `K=212 -> 213`, cuts 5 and 6 only | 2 | **4** |
| `K=212 -> 213`, cuts 8, 9 and 16 only | 3 | **3** |
| `K=213 -> 214`, cuts 8 and 9 only | 2 | **2** |
| `K=213 -> 214`, other 26 cuts | 26 | **3** |
| `K=214 -> 215` through `K=221 -> 222`, every cut | 224 | **2** |
| `K=222 -> 223` through `K=291 -> 292`, every cut | 1,960 | **1** |
| `K=292 -> 293` through `K=953 -> 954`, every cut | 18,536 | **0** |

Thus the **20,748 originally feasible** transition instances plus five additional newly feasible transitions yield exactly **20,753** classified instances. The minimum deletion histogram is

`{rho=0:18536, rho=1:1960, rho=2:226, rho=3:29, rho=4:2}`.

For adjacent budgets, the minimum number of changed memberships (symmetric difference) is `2*rho+1`. Therefore the two new cut-5/cut-6 transitions require nine changed memberships, and the 213->214 transitions at cuts 8/9 require five instead of the original seven.

## Proof: cost-preserving embedding and component gains

1. **Retained old witnesses.** The gap bridge theorem in `RESEARCH.md` at immutable PR #2340 shows that every previously radius-two-feasible center-index set retains its cost and feasibility after closing a single separating gap. At each budget `K>=214`, the exact 28-cut cost spectrum equals the unperturbed optimum. Hence every old optimal solution is still optimal. In particular, previous optimal edit witnesses give `rho_c(K)<=2` for 214..221, `<=1` for 222..291 and `=0` for 292..953.

2. **Component factorization and marginal ordering.** Exactly the two blocks adjacent to the closed gap join; 27 other blocks remain independent. The shortest-center-path dynamic program computes every component's exact optimum `J_i(k)` and all its optimal path languages. The full component marginal sequence `J_i(k)-J_i(k+1)` is verified nonincreasing in **every one of the 28 cases** (19,969 exact adjacent-gain comparisons, including repeated unaffected blocks). Consequently the global optimum at each budget is obtained by selecting the largest component marginal gains, respecting the order within each component. This concavity assertion is **finite-instance checked**, not assumed as a general theorem.

3. **Reduction of the gain-five region.** For an independent component with a gain-`g>3` local budget increase of `h>0`, a feasible old center set cannot be contained in a new optimal one: otherwise inserting those `h` centers would improve total radius-two integer distance by at most `3h`, whereas optimal improvement is `gh>3h`. A component whose center budget decreases must also delete an old center. Thus a global optimal pair in a tied gain-`g>3` level with **only one deletion** must change the allocation in exactly one component, by exactly +1 there. Every component adjacent gain-five optimal-language pair has been checked by the exact asynchronous path-product routine and excludes zero/one old deletion. Therefore **no** globally optimal gain-five transition has `rho<=1`. The preserved old witnesses give the matching `rho=2` for all eight transitions `K=214,...,221` under all cuts.

4. **First budget(s).** The high marginal groups before the gain-five region are fully explicit. Cuts 5 and 6 create a new global minimum budget of 212 and have one initial gain-seven increment, each with exact local minimum deletion **4**; the next increment is the original gain-six block-22 increment, with exact minimum deletion **3**. Cuts 8 and 9 create the same new minimum budget; their first increment is the original block-22 gain-six increment (local deletion **3**), and the next belongs to a gain-five component, for which exact local minimum deletion is **2**. Cut 16 has two tied first gain-six increments, one in the joined block and one in block 22; both exact local minima equal **3**, and the two consecutive global increments successively select these two components. All remaining cuts have a unique first gain-six increment, from original block 22 or the joined block, always with local deletion **3**. These initial allocation patterns leave no other optimal component-allocation route that could reduce the reported deletion count.

5. **Higher budgets.** At `K=222,...,953`, both old optimum costs are unchanged; the preserved witnesses and the nonnesting marginal bound prove exactly the unchanged old results, `rho=1` for 222..291 and `rho=0` afterwards, as established in `NESTING_PHASE_STABILITY.md` in PR #2340.

For each local optimal-language product, the old and new accepted paths represent exactly the corresponding minimum-cost feasible center sets. Synchronizing shared center indices and counting old-only indices computes their true minimum deletion count. Each returned witness is independently checked against the exact nearest-center distances and total cost. A bound-limited negative search is conclusive because all states of the finite product within that bound are memoized and exhausted.

## Reproduction, provenance and verification strength

`VERIFY_R5_28_CUT_EDIT_SPECTRUM.py` is a standalone extension of the exact center-path / optimal-language kernel from immutable PR #2335, using the **same 15 frozen atoms** rather than storing a new data pin. It regenerates all 28 joined-block instances, compares each component's full exact integer cost curve, checks every gain 5/6/7 optimal-language product, and asserts all 28 summaries and the 20,753-cell histogram. The accompanying `R5_28_CUT_EDIT_OUTPUT.json` contains 28 cut-specific outcomes.

Author-side calculations completed with an equivalent locally executed exact-integer/Fraction implementation: `257` local gain-5/6/7 product checks, `19,969` marginal-concavity comparisons, and independent complete center-subset enumeration for `847` small sequences (`2<=n<=7`, `x_0=0`, other coordinates in `1..10`), covering `2,518` adjacent-budget pairs. All agree. The saved source uses the earlier verified exact path kernel; **a separate byte-identical execution of the newly published standalone script is still open**, as is independent mathematical review.

The original 741-transition exact edit spectrum at PR #2335 and the 28-cut exact cost and nesting analyses at PR #2340 are reused under their immutable origin commits; no existing Result or review is modified. The formal Task-ID and current owner/CLAIM remain unresolved by the pending native task-inventory read, so this manuscript is a Draft PR scientific artifact, not a formal Task Result.

## Next useful science

The most direct continuation is to construct a compressed family of **explicit global optimal-center-set witnesses** for all 20,753 cases, including source-port/provenance information where that observer is relevant. Another independent work unit is the full original seed/28-coordinate/8,192-query end-to-end benchmark, with exact input preparation, output recovery, cold-start and memory accounting. Do not use these event-boundary edit distances as a performance claim about that unfinished benchmark.
