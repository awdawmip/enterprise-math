# R762BL — All-20 native X6 coordinate-triad observer: exact cut distance and optimal fault-tolerant subsets

**Status:** AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. **Date:** 2026-11-15. Independent portable-direct mathematics, referencing prior Task `RS-X6-TRIADIC-CLOSURE-DYNAMICS` and R762BK; it is **not** a new formal Task CLAIM or Source PROGRESS.

## Immutable inputs and exact scope

The frozen mathematical premise is `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`: `p000_reality_foundation.json`, `definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md`, and `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`. Earlier exact fixed-Port error theorem: `research_notes/portable_direct/R762BK_NATIVE_STAR_ROW_FAULTS.md` at `47bbce0a01215a635bb531f7081408652a1969bc`. The six native axes, signed unit steps, and P000 triadic force arity are preserved. This note concerns **Cell coordinate observers**, not a force-law assertion or an admission of particular `TRIADIC_CLOSURE_E` events.

For each native signed chart `z=(z_1,...,z_6) in Z^6` relative to one chosen Cell anchor and each three-element set `T` of axes, the native coordinate selection is `O_T(z)=can3((z_i)_(i in T))`, where `can3` subtracts the triple minimum. The 20 distinct named observations retain their axis labels. Define `H` to be any subset of these rows. The Cell-relative code `C_H: Z^6/Z(1,...,1) -> product_(T in H) can3(Z^3)` is measured by **Hamming distance in named entire rows** (one corrupted row may contain three arbitrary integers, constrained only by the normalized triple format). Known erasures and arbitrary adversarial row substitutions are counted separately. All information about Link, Port, ordered paths, branch multiplicity and full spatial common depth remains separately typed; it is not discarded by this code.

## Theorem 1 — General hypergraph cut-distance identity (all signed integers)

Let `G_H` be the three-uniform labelled hypergraph with vertex set `[6]` and edge set `H`. For `∅ != S ⊊ [6]`, put `∂_H(S)={T in H: T intersects both S and [6]\S}`. Then the exact minimum row distance between two distinct relative Cell states is

`d(H)=min_(∅!=S⊊[6]) |∂_H(S)|`.

**Proof.** Two normalized triple observations are equal exactly when the difference `w=z-z'` is constant on their three selected coordinates. Partition the six axes by equal values of `w_i`; since the two relative states differ, this partition has at least two classes. A changed observed row is exactly a hyperedge not wholly contained in an equality class. For any one nonempty proper equality class `S`, every hyperedge crossing `S` is changed; hence the number of changed rows is at least `|∂_H(S)| >= mincut(H)`. Conversely, choose `w=1_S` for any minimizing nontrivial cut. A row changes exactly when it crosses that cut; the minimum is attained. This holds for arbitrary integral chart values, with no finite-alphabet approximation. ∎

For any nonnegative integers `t,e`, **uniform unique recovery** of the relative Cell coordinate from at most `t` arbitrarily corrupted named rows and at most `e` known erased named rows is possible exactly when

`2t+e < d(H)`.

This follows by the standard minimum-distance disjoint-ball argument. Sharpness uses two integral source charts differing by `1_S` on a minimum cut, erases up to `e` of their disagreeing rows and divides the rest into two sets of at most `t` rows; the same normalized received rows then agree with each source outside its error budget. Decoding can enumerate consistent anchored integer chart candidates induced by surviving triples and retain the unique one meeting the row budget; the theorem concerns unique recovery rather than a claim of constant-time decoding.

## Theorem 2 — Complete twenty-row observer

For `H=binom([6],3)` and a cut of size `s`, the crossing count is `20-binomial(s,3)-binomial(6-s,3)`. For `s=1,2,3` this is exactly `10,16,18`. Thus

`d(H)=10`.

All 20 native coordinate-triad observations uniquely recover the full relative six-axis Cell coordinates under `2t+e<=9`, in particular four arbitrary row corruptions with one additional erasure. Five corruptions can be ambiguous: the two states `0` and `e_1` differ in exactly the ten triples containing axis 1; a received packet taking five of these rows from each original is at distance five from both. Recovering the full anchored Cell additionally requires the existing integer common-depth coordinate.

## Theorem 3 — Exact minimum row budget and number of optimum designs

Let `q>=1` be the demanded minimum distance. Since the singleton cut at vertex `i` has size `deg_H(i)`, any candidate must satisfy `deg_H(i)>=q`. Summing six degrees yields `3|H|>=6q`, so `|H|>=2q`.

For `2<=q<=10`, this bound is attained **exactly** by the labelled `q`-regular three-uniform hypergraphs on six vertices. Indeed, if `|H|=2q` and all degrees are at least `q`, all six are equal to `q`. Conversely, if all are `q`, cuts with one vertex have `q` crossing edges; a two-vertex cut has `2q-λ_{ij}>=q`, where `λ_{ij}` counts edges containing both vertices and is at most `q`. A three-vertex cut has `2q-1_{S∈H}-1_{S^c∈H}>=2q-2>=q` for `q>=2`. Complementary cuts cover the remaining cases. Therefore `d(H)=q`. Explicit witnesses for each `q` are in the evidence file.

For `q=1`, two triples cannot span a connected hypergraph on all six vertices: if they overlap, some axis is isolated; if disjoint, they form two components. Three overlapping triples covering the six axes do work (e.g. `125,126,134`). Thus the exact minimum row count is three.

The numbers of **labelled** optimal collections below are computed exhaustively, with a separate mathematical characterization above. For `q>=2` the count equals the coefficient
`[x_1^q...x_6^q] ∏_(|T|=3)(1+∏_(i∈T)x_i)`.

| demanded minimum distance q | least rows | labelled optima |
|---:|---:|---:|
| 1 | 3 | 480 |
| 2 | 4 | 75 |
| 3 | 6 | 330 |
| 4 | 8 | 780 |
| 5 | 10 | 1,044 |
| 6 | 12 | 780 |
| 7 | 14 | 330 |
| 8 | 16 | 75 |
| 9 | 18 | 10 |
| 10 | 20 | 1 |

**Fault-budget consequences:** one arbitrary row error needs at least six rows (330 optima), two need ten (1,044 optima), three need fourteen (330 optima), and four need eighteen (ten optima). For four errors plus one erasure, twenty rows are required. Under full `S_6` covariance of the **row selection itself**, transitivity on three-subsets forces any nonempty invariant design to contain all twenty rows. That symmetry statement concerns the choice of rows, not the selection of a force event.

## BRC observer and provenance interpretation

The quotient `Z^6/Δ` is exact for the declared family of current and future *coordinate-triple* observations and native signed coordinate translations or axis relabellings, since these transformations descend to the quotient. It is not asserted sufficient for time-ordered Link/Port or force-state dynamics. A full Cell coordinate needs the integer common-depth repair, and a provenance-sensitive future operation retains its ordered-source BRC residual. The row-erasure/code distance is an observation fault property rather than an intrinsic force magnitude.

## Reproducible evidence

`R762BL_X6_TRIAD_CUT_VERIFY.js` enumerates all `2^20=1,048,576` row subsets and all 31 complementary nontrivial cuts, computes each minimum distance, and finds every minimal design. It checks the regularity characterization and compares normalized triple equality with the cut formula on 243 anchored integer coordinate states (`29,403` state pairs, `588,060` pair/row comparisons). The JSON evidence contains the full distance histogram, optimal counts, exact hex witness masks and row lists; bit index follows lexicographic triple order. The finite exhaustive classification is exact; Theorems 1-3 have separate general combinatorial arguments. Independent peer mathematical review: `NOT_REVIEWED`.

## Next nonduplicative problem

Compare this all-port coordinate code with the **actually authorized** signed `TRIADIC_CLOSURE_E` Cell/Link/Port event set and V17/V29/V39 permitted observations. Determine which named triples are legal force events; recompute the corresponding cut distance and BRC residual without treating the coordinate-triple observations as force-event permission. Before any source-native Task association, reconcile current owner/CLAIM and the pending R762BK same-SID resume request using its original ID; the console returned `BACKEND_IDENTITY_CHECK_UNAVAILABLE` at 2026-11-15 12:32 UTC, so this material is filed as an independent nonoverwriting GitHub research artifact.
