# EC49FSY — Native BRC exact lower three-price policy fan

**18 November 2026 · Frozen scientific input:** `awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Continues **EC49FSX PR #2738**, immutable head `8437314e1d7bf0061b21734ffadc66d349092077`. The model has 310 original configurations, 141 distinct named response profiles, 228 physical named queries, uniform prior and all complete adaptive strict-splitting trees.

## Exact unrestricted Bellman theorem

The prices of physical q32, q34 and q140 are respectively `(1-a)t,(1-b)t,(1-z)t`, all others `t>0`. Define `D=141 V(a,b,z)/t` and `S=141 V(b,a,z)/t`, where the latter **physically swaps** q32/q34 prices.

For **all real** `1/2<=a<=2/3`, `7/16<=b<=57/128`, `21/32<=z<=1`:

```
D = 319 - 18a - 75b - 141z
S = min(323 -  89a - 12b - 141z,  # C
        325 -  94a -  9b - 141z,  # T
        324 - 141a -  8b -  93z)  # N
```

Each line is the cost of a complete native tree actually replayed across all 141 named-state paths. The physical vectors `(U,N32,N34,N140)` are D=(319,18,75,141), C=(323,12,89,141), T=(325,9,94,141), N=(324,8,141,93). In swapped coordinates a prices q34 and b prices q32.

The pairwise phase boundaries are exactly `5a=2+3b` (C/T), `48z=1+47a-b` (T/N), and `48z=52a-4b-1` (C/N). Exact **triple-coexistence** locations include `(53/80,7/16,317/480)` and `(2/3,4/9,287/432)`.

The physical price-swap defect obeys the sharp, attained **continuous-prism** bounds

```
441/128 <= D-S <= 259/16.
```

The lower bound is attained at `(a,b)=(1/2,57/128)` for every z in the prism; the upper at `(2/3,7/16,21/32)`.

## Proof of global, continuous optimality

1. For every complete native decision tree `T`, its normalized cost is `U-a N32-b N34-z N140` in direct orientation, with a,b swapped in the other orientation. Each exhibited tree is feasible, so its affine cost is an **upper** bound on unrestricted optimal cost. The unrestricted Bellman value, the minimum of all feasible-tree affine costs, is jointly **concave** on the real parameter domain.

2. Set `z0=1531/2304`. On the lower slab `[1/2,2/3]×[7/16,57/128]×[21/32,z0]`, form the three convex polyhedra where C, T and N respectively minimize the displayed candidate costs. Every polyhedral vertex belongs to an intersection of three facets chosen from the six box boundaries and the three exact pairwise equality planes. Enumeration by **exact rational Gaussian elimination** gives 22 distinct feasible candidate vertices (including some redundant plane intersections). At **all 22**, the exact original-data **unrestricted 228-observation Bellman minimum** matches the corresponding proposed affine-tree value. The companion JSON lists all coordinates and fractions, and the companion Python audit independently recomputes the polyhedral vertex geometry and equality identities. Two load-bearing new intersection values were independently recalculated by a separate original 94-family decoder and independent Bellman routine.

3. On each candidate-optimal convex polyhedron, any interior point is a convex combination of vertices. Joint concavity and the certified exact Bellman values give a lower bound equal to that region's affine candidate, and tree feasibility gives an identical upper bound. Therefore `S=min(C,T,N)` for **every real point** of the lower slab. Four further exact unrestricted Bellman corner values establish `D=319-18a-75b-141z` for all a,b on the lower face `z=21/32`, again by concavity and its complete tree witness.

4. The D witness uses q140 **once on all 141 named paths**. A strict-splitting tree cannot reuse a previously seen deterministic physical observation on the same path, so any tree uses it at most 141 times in aggregate. For increasing z the saturated D witness decreases at maximal slope -141 and remains optimal for all z above the lower face.

5. EC49FSX's pinned native theorem certifies `S=min(C,T)` at and above `z0`. At `z0`, the third feasible N plane is at least this minimum. As z rises, N has slope -93 while both C and T have slope -141, so N never becomes preferable. This glues the lower 3-plane result to the entire upper interval ending at z=1.

6. The exact gap `D-min(C,T,N)` is affine on each of the lower polyhedra, so its extreme values are among the 22 audited rational vertices. Their sharp min and max are `441/128` and `259/16`. The upper slab has EC49FSX's proven range `[441/128,379/24]`, contained in the claimed interval.

## Explicit lower-bound obstruction and next question

The present menu is already beaten at z=5/8: for direct `(a,b)=(2/3,7/16)`, the old D line yields `2977/16`, while the unrestricted original-data Bellman optimum is `2951/16`, an improvement `13/8`, with tree vector `(316,141,43,30)`. For swapped `(a,b)=(2/3,57/128)`, the three-line menu is beaten by `1/32` by an optimal tree using q140 on 87 paths. These verify that the new lower bound is a **proved extension**, not an asserted sharp global threshold.

Next: determine the exact maximal lower extension of the three-policy fan, incorporating unsaturated physical q140 usage 93/87/82 and direct trees with usage 30/40; a discriminating fixed-price slice is a=2/3,b=7/16 and the D/30-use tree crossover at `z=71/111`, which still needs unrestricted-optimality checking.

## Reproducible evidence and status

The JSON machine certificate contains 22 swapped + 4 direct exact primary oracle fractions, two independent original decoder values, full policy vectors, frozen source hashes, and lower-slab counterexamples. The companion script verifies all exact plane intersections, rational values and gap extrema; **it does not substitute for rerunning the original-data Bellman oracle**. The complete source, 228-observation native solvers, full original 141-profile data, five lossless complete trees, run logs and full replay are separately retained in `EC49FSY_NATIVE_BRC_THREE_PRICE_LOWER_FAN_COMPLETE_EVIDENCE_20261118.tar.xz`, SHA256 `1fb630a87854623a436cc4484df4183dee4ed937a339d52c15ed13000d66d0e6` (conversation artifact; **not committed binary to this PR**). Master raw data SHA256: `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`, profile CSV SHA256: `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`.

Status: `AUTHOR_PROVED / EXACT_PRIMARY_26_VALUES / INDEPENDENT_2_NEW_VALUES / FIVE_NATIVE_TREES_REPLAYED / NOT_REVIEWED`. This portable result creates neither formal Task CLAIM nor a native Result, Review, Activity checkpoint, or Foundation admission. P000 and the frozen mathematical input are unchanged.
