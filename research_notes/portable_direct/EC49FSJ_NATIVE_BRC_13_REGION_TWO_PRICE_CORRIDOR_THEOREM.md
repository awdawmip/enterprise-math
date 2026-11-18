# EC49FSJ — Exact 13-region native BRC price corridor and 7/16 slice

Date: 2026-11-18 (Asia/Shanghai). Research continuation from EC49FSI PR #2688 at immutable scientific branch head `b1687edf0341627ceb42e834c211ce153bf7af2b`. Frozen scientific input pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.

## Exact mathematical statement

Use the original class-16943 BRC experiment: 310 configurations collapse to **141 distinct named joint-response profiles**, uniform prior on these profiles, and **all 228 physically named native observations** with their original joint response fibers. Every complete deterministic adaptive decision tree is eligible. Fix `t>0`, let observations q32 and q34 cost `(1-alpha)t` each, q140 cost `(1-z)t`, and all others cost `t`. Write `F(alpha,z)=141*V(alpha,z)/t` for the global optimum.

**Theorem.** For every pair of real numbers
`3/8 <= alpha <= 7/16` and `0 <= z <= 1`,

`F(alpha,z) = min_(U,Q,K) in P (U - Q*alpha - K*z)`,

where the exact set of 13 cost triples `P` is:

| U | Q = N32+N34 | K = N140 | Positive optimal-region area |
|---:|---:|---:|---:|
| 301 | 168 | 15 | 1/94976 |
| 303 | 173 | 17 | 2591/569856 |
| 304 | 169 | 32 | 25/2688 |
| 304 | 177 | 8 | 183/237440 |
| 305 | 173 | 29 | 1/384 |
| 306 | 182 | 10 | 4833/949760 |
| 309 | 151 | 64 | 1/3200 |
| 309 | 169 | 46 | 53/22400 |
| 311 | 151 | 69 | 2053/1382400 |
| 311 | 169 | 51 | 9/12800 |
| 319 | 93 | 141 | 1883/165888 |
| 308 | 66 | 141 | 673/46080 |
| 314 | 81 | 141 | 97/10368 |

The 13 convex positive-area optimal regions have exactly **25 distinct rational vertices**, and exact rational clipping gives total area **1/16**. All 25 vertices were checked with exhaustive exact Bellman dynamic programming over the 228 original named observations; nine original alpha=3/8 boundary vertices reuse EC49FSI's already independently checked results, nine alpha=7/16 boundary vertices were independently rechecked this run, and **seven new interior vertices** were independently checked using a second raw-family reconstruction and Bellman implementation. All 13 cost triples have fully replayed native witness trees on each of the 141 named profiles. Thus the minimum fixed-tree **affine cost-type menu** on the corridor has precisely **13** members, because all 13 gradients are distinct and optimal on nonempty open regions.

**New interior vertices** (alpha,z,F):
`(20/53, 3/53, 12548/53)`,
`(2/5,0,1166/5)`,
`(2/5,2/5,223)`,
`(2/5,31/72,26507/120)`,
`(2/5,1,703/5)`,
`(5/12,193/432,31285/144)`,
`(5/12,1,557/4)`.
The exact machine certificate lists all 25 vertices and each cost-region area.

## Exact 7/16 slice (corollary)

For **all real** `z in [0,1]`, at `alpha=7/16` the global optimum is the following eight affine pieces:

| z interval | (U,Q,K) | Formula |
|---|---|---|
| [0,15/112] | (306,182,10) | 306-182*(7/16)-10*z |
| [15/112,1/6] | (303,173,17) | 303-173*(7/16)-17*z |
| [1/6,1/4] | (305,173,29) | 305-173*(7/16)-29*z |
| [1/4,5/14] | (304,169,32) | 304-169*(7/16)-32*z |
| [5/14,2/5] | (309,169,46) | 309-169*(7/16)-46*z |
| [2/5,7/16] | (311,169,51) | 311-169*(7/16)-51*z |
| [7/16,89/192] | (311,151,69) | 311-151*(7/16)-69*z |
| [89/192,1] | (319,93,141) | 319-93*(7/16)-141*z |

The eight pieces require eight distinct slopes; nine exact breakpoints were separately crosschecked by both raw-data reconstruction paths.

## Proof and exact coverage

A complete informative-query tree T has affine price `C_T(alpha,z)=U(T)-Q(T)*alpha-K(T)*z`, where U, Q and K are integer named-path query counts. Every tree included in the certificate was replayed against all 141 *real* profile response paths, checking leaves, observer identifiers, nonrepetition along a path, and exact U/Q/K. All 13 tree costs provide feasible upper bounds.

For any subset S of remaining candidate profiles, the exact Bellman recursion takes the minimum over **all 228 original observations that split S** of `|S|*price(q) + sum_{child fiber} D(child)`. An informative query strictly shrinks each child subset, so recursion exhausts every finite complete admissible tree. The optimum F, being the pointwise infimum of affine complete-tree costs, is jointly **concave** on the price parameters.

Use exact rational half-plane clipping to define, for each listed plane, the polygon where that plane is no larger than the other 12 planes. The 13 positive-area polygons cover the stated rectangle, interiors disjoint, and their exact areas sum to 1/16. At each polygon vertex, exhaustive exact Bellman equals the minimum of the listed planes. Each point in a polygon is a convex combination of its vertices. Concavity then gives the lower bound by vertex interpolation, exactly equal to the polygon's witness-tree affine cost; feasibility gives the matching upper bound. Hence the theorem holds for **every real parameter pair in the rectangle**, not only at sampled grid points. Distinct gradients on open regions prove minimum cost-type cardinality.

## Reproducibility and evidence

The four companion artifacts are this proof, a structured exact certificate with all vertices, a zlib+base64 JSON object containing all **13 complete named-observation witness trees**, and a portable Python rational proof checker (with optional full Bellman reruns on the frozen original data). The original data hashes are:
- `frozen_original_master.txt`: SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`.
- `EC49FPG_PROFILE.csv`: SHA256 `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`.

The full self-contained local evidence archive additionally contains original frozen data, two source reconstructions, all 29 explored candidate trees, source code, 25 exact Bellman point outputs and run logs. Its manifest is reproducible and independently usable.

**Frontier:** continue `alpha in [7/16,1/2]`, looking for new Pareto-supporting cost planes and interior junctions; then release q32/q34 price equality to reach fully independent three-price geometry.

Author theorem status: `AUTHOR_PROVED / EXACT_FINITE_CROSSCHECKED / NOT_REVIEWED`. This work is independent portable research. The historical topic `RS-EC49AS` had no canonical immutable task publication directory at the last specific task lookup; this publication creates no formal CLAIM, owner or Activity checkpoint.
