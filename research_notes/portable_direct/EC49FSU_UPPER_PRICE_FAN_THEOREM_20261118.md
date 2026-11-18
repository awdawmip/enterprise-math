# EC49FSU — Exact native BRC16943 upper three-price fan

**Date:** 2026-11-18. **Frozen scientific source:** `awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. **Parent frontier:** EC49FST PR #2722@28f6ca385cbb0c5da3309708a930114cfa370046. **Status:** AUTHOR_PROVED / EXACT_PRIMARY_20_ANCHORS / INDEPENDENT_4_ANCHORS / NOT_REVIEWED. Independent portable research; no Task CLAIM, Result, Review or Activity checkpoint is asserted.

## Statement

Work with the **original** 310 configurations, 141 distinct named joint-response profiles under uniform prior, all 228 distinct physically named observations, and unrestricted complete strict-splitting adaptive identification trees. No response-alias quotient is taken. Each query other than q32, q34, q140 costs `t>0`; those three cost `(1-a)t,(1-b)t,(1-z)t`. Write `F(a,b,z)=141 V(a,b,z)/t`.

For **every real** `a∈[2/3,1], b∈[27/64,29/64], z∈[77/128,5/8]`, the unrestricted original 228-observer Bellman optima in the direct and swapped (q32↔q34) price models are exactly

```text
D(a,b,z) = min(
  316-141a-43b-30z,  # E: (U,N32,N34,N140)=(316,141,43,30)
  324-141a-58b-32z,  # J: (324,141,58,32)
  332-141a-62b-42z,  # L: (332,141,62,42)
  324-141a-47b-40z   # M: (324,141,47,40)
)
S(a,b,z) = min(
  318-141a-10b-82z,  # K: (318,10,141,82)
  320-141a- 6b-88z,  # N: (320,6,141,88)
  322-141a-12b-87z   # O: (322,12,141,87)
)
```

In `S`, the q32 discount is `b` and q34 discount is `a`. All seven named planes have distinct gradients and are strictly optimal on positive-area regions of the same `(b,z)` rectangle. The exact areas of D's four regions E,J,L,M are respectively `771/1163264,121/5816320,23/1454080,3/90880`; the areas of S's K,N,O regions are `37/61440,1/12288,1/20480`. Each set sums to the rectangle's area `3/4096`. There are five positive-area overlaps between direct and swapped phase cells.

The **sharp global exchange-gap bounds** on the prism are

```text
917/64 <= D(a,b,z)-S(a,b,z) <= 1065/64.
```

The minimum is attained for every `a∈[2/3,1]` at `(b,z)=(29/64,77/128)`; the maximum for every such `a` at `(b,z)=(27/64,5/8)`. The normalized gap is strictly positive.

## Proof of global optimality on the continuous prism

A complete named-query tree `T` has integer path-use vector `(U,N32,N34,N140)` and total affine cost `U-aN32-bN34-zN140` (with the indicated discount exchange in S). Every tree provides a feasible **upper bound** for the unrestricted optimum; the infimum of all such affine costs is jointly concave in prices.

First set `a=2/3`. Enumerate all vertices of the lower-envelope arrangement of the proposed four D and three S affine planes inside `[27/64,29/64]×[77/128,5/8]`: rectangle corners, pair-plane intersections on rectangle edges and triple-plane intersections in the rectangle. Original 228-observer exact rational Bellman computes the **unrestricted optimum** at all 12 candidate vertices of D and all 8 of S, agreeing in every case with the corresponding minimum feasible plane; all 20 values and reached-subset counts are in `EC49FSU_UPPER_FAN_CERT.json`. In addition, seven full 141-profile, no-repeat strict-splitting tree witnesses were generated, serialized without loss and checked against original observation outputs; their SHA256 and use vectors appear in the certificate. The 20-point exhaustive check is reproducible with the frozen solver and complete raw inputs in the self-contained evidence package.

Each lower-envelope cell is convex and has a single feasible affine plane. The actual optimal value equals that plane at every cell vertex. Joint concavity gives the matching **lower bound** at every interior convex combination; the feasible complete tree gives the upper bound. Thus the exact formula holds throughout the entire continuous two-parameter rectangle, rather than only at the finite anchor set.

Every D witness uses q32 in **all 141 named state paths**; every S witness uses q34 in all 141. A strict-splitting tree uses any fixed named observation at most once per state path, hence at most 141 times in total. The saturation lemma implies that an optimal 141-use tree at a discount `a0` stays optimal at every increased discount `a≥a0`, with both values decreasing by exactly `141(a-a0)`. This lifts the two-dimensional result from `a0=2/3` to the full three-dimensional real prism.

Use exact rational half-plane clipping to construct the four D and three S phase polygons, and all pairwise overlaps. Their five positive-area overlaps cover `3/4096`. On each overlap, `D-S` is affine; comparing its values at **all overlay vertices** proves the exact sharp minimum and maximum above. No floating-point step enters any mathematical proof.

## Verification and provenance

The primary oracle uses `Fraction`/integer-scaled Bellman over all 228 original observations and 141 named states; 12 direct and 8 swapped anchors were evaluated and re-evaluated independently by orientation. Four strategically selected load-bearing points were confirmed by a **different raw 94-family decoder**:

- D `(b,z)=(32/71,44/71)` => `13066/71`.
- D `(17/38,5/8)` => `6991/38`.
- S `(27/64,59/96)` => `16261/96`.
- S `(29/64,5/8)` => `2691/16`.

Original master SHA256: `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`. Named profile CSV SHA256: `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`. The self-contained 22-file local archive includes both inputs, four native Python solver/data modules, all seven packed complete trees, exact geometry, 20 oracle results, executable full verification and stdout logs, with per-file SHA256 manifest. Corresponding source modules and preserved prior trees are also available through EC49FST PR #2722.

### Next scientific question

Classify the next native Pareto phases for `z>5/8`: an original native oracle at `z=21/32` already found a q140-saturating solution with `N140=141`. Determine its first exact stable optimal region, its intersection with the L/M direct phases, and the corresponding swapped-price transitions. Independently review the native Bellman recurrence and proof certificates. Existing P000, worldview, owner authority and frozen scientific inputs are unchanged.
