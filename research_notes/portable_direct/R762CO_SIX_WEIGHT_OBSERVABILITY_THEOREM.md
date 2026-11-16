# R762CO — Six-source triad N-BRC: sharp observation-depth and source-alphabet bounds

**Status:** AUTHOR_PROVED_AND_EXACT_CHECKED; independent review `NOT_REVIEWED`.
**Task:** `RS-X6-TRIADIC-CLOSURE-DYNAMICS`; immutable publication `TP2-8B7E13C5904A2D6F1142`.
**Research continuity:** R762CL → R762CM → R762CN (PR [#2597](https://github.com/awdawmip/enterprise-math/pull/2597) at `4a348cf419c8849b51b155f5f373b4cba198b76f`), reused without recomputation.
**Frozen scientific inputs:** `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`: P000 V5, native signed X6 Cell torsor and triadic-balance definition.

## Exact typed carrier and observation

Keep six *named* X6 native-axis tokens represented combinatorially by the six edges of K4, in the fixed order `01,02,03,12,13,23`. These are six native axes, not a reduced spatial dimension. A candidate triad assembly is an unordered 3+3 partition `A|Aᶜ` of those six labels; there are `C(6,3)/2=10` such assemblies: four star/face (`F`) and six path/path (`P`).

Assign positive integer **source multiplicities** `w=(w_01,w_02,w_03,w_12,w_13,w_23)`. Exchange one token `x∈A` with `y∈Aᶜ`, attaching exactly `w_x w_y` positive N-BRC microbranches to the resulting candidate transition. This gives a symmetric 10-by-10 integer matrix `T_w`, each row with nine distinct target states. The weights measure source *counts*, neither signed force amplitudes nor physical coupling strengths.

Let `v_F,v_P` be the indicator columns of the F/P state classes. Define the depth-`h` exact observation on an initial state `i` as

```text
O_h(i) = (kind(i); ((T_w^t v_F)(i), (T_w^t v_P)(i)) for t=0,...,h).
```

An observer may query complete positive source-count totals after any candidate-exchange length; it does not query named token contents, the exchange label or microscopic branch IDs. All results below are confined to this declared observation language and candidate graph.

## Theorem A — two distinct source values cannot fully distinguish all ten states

For *every* assignment of only two positive weights `a,b` to the six K4 edges, a nonidentity K4 vertex permutation fixes the weight assignment. It commutes with `T_w` and preserves the current F/P readout, hence identifies at least two distinct F states under `O_h` for **every** `h≥0`. Two positive weight levels can never provide full ten-state future observability.

**Proof.** Color each edge by which of the two weights it receives. Passing to the color complement, at most three edges carry the chosen color. A graph of 0 or 1 edges has a nontrivial vertex symmetry; a 2-edge graph consists of adjacent or disjoint edges and has an explicit swap symmetry; a 3-edge graph on four vertices is a star, a 4-vertex path, or a triangle plus an isolated vertex, each admitting a nonidentity automorphism. Complementing does not change the automorphism group. Thus a nonidentity vertex permutation preserves all weights. Its induced permutation carries each microbranch of weight `w_x w_y` to one with identical weight, preserving F and P. The four F assemblies are indexed by the four K4 vertices, so the action on F is faithful. Some two distinct F assemblies in a nontrivial orbit therefore have identical future aggregate readouts. QED.

## Theorem B — three levels suffice at depth 2, optimally

For `w^(2)=(1,1,2,3,2,3)`, the number of distinguishable `O_h` classes is

```text
h=0: 2        h=1: 9        h=2: 10 .
```

The only depth-one collision is the two F states `01,02,12` and `01,03,13`, both with one-step `(F,P)=(11,24)`; their two-step counts are `(521,676)` and `(505,732)` respectively.

The full exact integer certificate (canonical triple, type, F1, P1, F2, P2) is:

| Triple | Type | F1 | P1 | F2 | P2 |
|---|---|---:|---:|---:|---:|
| 01,02,03 | F | 11 | 21 | 466 | 654 |
| 01,02,12 | F | 11 | 24 | 521 | 676 |
| 01,02,13 | P | 15 | 17 | 450 | 670 |
| 01,02,23 | P | 20 | 15 | 440 | 757 |
| 01,03,12 | P | 15 | 21 | 450 | 806 |
| 01,03,13 | F | 11 | 24 | 505 | 732 |
| 01,03,23 | P | 12 | 24 | 504 | 752 |
| 01,12,13 | F | 11 | 25 | 530 | 726 |
| 01,12,23 | P | 12 | 23 | 504 | 733 |
| 01,13,23 | P | 20 | 16 | 440 | 816 |

**Proof.** Enumerate the ten unordered partitions and their nine unique cross-triple swaps as specified; multiply exact integer transfer matrices by the two F/P indicator columns twice. The table is the resulting finite certificate. Depth one distinguishes nine rows and depth two separates the only remaining collision. Theorem A supplies optimality of **three distinct source values** across all future horizons. QED.

## Theorem C — minimum maximum positive integer weight for depth-one full recovery is 4

With all `1≤w_e≤3`, exhaustive enumeration of all `3^6=729` **labeled**, not symmetry-restricted, assignments yields at most nine distinct `O_1` signatures. The witness

```text
w^(1)=(1,1,1,2,3,4)
```

has ten distinct `O_1` signatures. Its exact ten one-step `(F,P)` pairs, in the row order of the table above, are

```text
(9,18),(9,23),(12,23),(15,21),(12,20),
(9,26),(20,16),(9,27),(20,15),(15,17).
```

Their current F/P types together distinguish all ten rows. The **optimal maximal integer multiplicity is exactly 4**, when one future count step is allowed. Only three distinct weight values are actually needed for one-step recovery: `(1,1,2,4,2,4)` is another ten-class depth-one witness. The lower bound is a complete finite-domain enumeration using the included exact Python checker, with all 729 cases and their actual K4 arrangements, not a numerical sample. QED.

## Theorem D — total-only, one-step observer requires a larger weight range

For a partition `A|Aᶜ`, the total one-step mass is exactly

```text
D(A) = (Σ_{x∈A}w_x)(Σ_{y∈Aᶜ}w_y).
```

This expands the nine positive cross-partition swap weights. With independent formal variables `w_e`, all ten degree polynomials are distinct: their squarefree monomial supports are the distinct cross-cut edge sets of the ten 3+3 partitions. Thus generic positive specializations distinguish ten states by total-only mass, excluding the explicit finite union of proper polynomial-equality hypersurfaces.

For positive **integer** weights, the minimum possible maximal multiplicity for ten *different total degrees* is **13**, attained by

```text
w^D=(1,2,3,5,8,13).
Degrees in canonical order: (156,192,231,256,207,240,255,252,247,220).
```

**Lower-bound proof.** If two source weights coincide, swap one of those two edge tokens across a suitable 3+3 partition. The two different partitions have the same triple sum, and thus the same total degree. Therefore six distinct weight values are necessary. Reordering all weights permutes the set of ten degrees. Uniformly subtracting `c` from all weights, while keeping them positive, adds the *same* scalar correction to all degrees: for total `S` and one triple sum `s`, shifting by `c` changes `s(S-s)` by `3cS+9c²`. Normalize the minimum to 1. The exhaustive finite certificate checks all strictly increasing 6-tuples beginning with 1 and maximal value ≤12, and none has ten distinct degrees; the displayed 13-maximal vector establishes sharpness. QED.

This quantifies the difference between the two-channel F/P positive BRC observer and the coarser total-mass readout on exactly the same candidate graph.

## Verification and exact all-future certification

The companion standard-library Python program constructs 10 states and 90 directed swaps and performs only integer arithmetic. It exhausts all `1+64+729+4096=4890` assignments in `{1,...,B}^6`, for `B=1,2,3,4`. For every assignment it compares F/P signatures at depths 0 through 9, verifying that the partition stabilizes by depth 2, and checks weighted symmetry. The Cayley–Hamilton identity for each 10-by-10 integer transfer matrix proves that equality of both observation sequences at depths 0,...,9 implies equality at *every* future depth. Thus the reported depth-9 class histograms are full-horizon results for this declared finite model.

| Maximum allowed weight B | Exact full-horizon histogram (classes: assignments) |
|---|---|
| 1 | 2:1 |
| 2 | 2:2, 3:26, 5:36 |
| 3 | 2:3, 3:96, 4:6, 5:216, 6:144, 7:216, 10:48 |
| 4 | 2:4, 3:228, 4:24, 5:720, 6:720, 7:1440, 10:960 |

The checker also enumerates all 64 binary color patterns and their K4 symmetries; for the total-only bound it exhausts all strictly increasing normalized six-weight tuples of maximum ≤12. The second companion file is an exact JSON witness/census record, generated from the checker. **Review:** NOT_REVIEWED.

## Exact continuation of the mother objective

The frozen P000 premise retains six signed native spatial axes, pairwise `PERP_E` at the native 120-degree angle, and three-force minimal stable nonzero balance. This paper treats integer *source multiplicities* in a conditional K4 candidate-triad assembly; it does not identify these weights with forces or assert that any of the nine token swaps is a licensed `TRIADIC_CLOSURE_E` Cell/Link/Port event.

Next: obtain the true native event predicate, actual named signed Port observations and V17/V29/V39 transport. Restrict the candidate transition operator to licensed typed events, retaining provenance and R762CH/CK path-area data. Recompute future observer equivalence, produce either a native event-permission descent certificate or a precise separating counterexample, and preserve signed/joint information until this reduction is justified.
