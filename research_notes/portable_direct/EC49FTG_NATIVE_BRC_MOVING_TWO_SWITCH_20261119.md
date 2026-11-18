# EC49FTG — Frozen native BRC16943 three-price two-switch theorem

Date: 2026-11-19. Scientific status: **AUTHOR_PROVED / EXACT_PRIMARY_24 / INDEPENDENT_RAW94_2 / NOT_REVIEWED**.

Predecessor: [EC49FTF, PR #2764](https://github.com/awdawmip/enterprise-math/pull/2764) at `241b2eb767a57b89bdd23dc14c9994641be1ce89`. The immutable scientific input is unchanged: `awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. This is the existing BRC16943 identification/decision-tree model: 310 native configurations, 141 separately named response profiles and all 228 original physical observations; no observer/profile quotient is imposed.

Let `a,b,z` denote query price *discounts* for q32, q34 and q140. All other query prices remain at the positive baseline `t`. The normalized total decision-tree cost `F=141 V/t` is the sum of query costs along all 141 named identification paths. A complete original-index tree with usage vector `(U,N32,N34,N140)` costs `U-a*N32-b*N34-z*N140` in the original pricing D and `U-b*N32-a*N34-z*N140` when q32/q34 discounts are exchanged (S). Minima are unrestricted over all native 228-query identification trees.

## Exact continuous theorem

For every **real** triple in

```
3/4 <= a <= 49/64,
7/16 <= b <= 57/128,
3/4 <= z <= 13/16,
```

the global optima are exactly

```
D = min(329 - 36*a - 68*b - 141*z,
        334 - 141*a - 62*b - 45*z);

S = min(333 - 105*a - 9*b - 141*z,
        332 - 141*a - 8*b - 105*z).
```

The switching sheets are `z_D=(105*a-6*b-5)/96` and `z_S=(1+36*a-b)/36`. A direct-price optimal tree below z_D uses q140 on 45/141 named state paths, and above it on 141/141. A swapped-price optimal tree below z_S uses q140 on 105/141 paths, and above it on 141/141. On a switching sheet both listed witnesses are optimal; other ties are allowed.

There are exactly three nonempty joint full-dimensional strategy regions, with the corresponding gap `G=D-S`:

| Direct and swapped witnesses | Gap |
|---|---|
| Dmid, Smain | `-4 + 69*a - 59*b` |
| Dmid, S105 | `-3 + 105*a - 60*b - 36*z` |
| D45, S105 | `2 - 54*b + 60*z` |

The D45/Smain intersection is empty in this parameter box. Consequently **sharp, attained** bounds are

```
2749/128 <= D-S <= 12213/512.
```

The minimum occurs at `(a,b,z)=(3/4,57/128,13/16)`. The maximum occurs at `(49/64,7/16,4657/6144)`, where `D=337537/2048` and `S=288685/2048`.

## Proof

**Feasibility.** Four complete original-observer-index trees have precisely the path-aggregated usage vectors `Dmid=(329,36,68,141)`, `D45=(334,141,62,45)`, `Smain=(333,9,105,141)` and `S105=(332,8,141,105)`. The Dmid and Smain trees are inherited from EC49FTF; D45 and S105 are new complete original-index trees. Each was replayed against all **141** distinct original native profiles: its queries are among the original **228** physical observations, no query repeats on a profile path, and the terminal leaf equals that same original named profile. Hence each tree contributes a globally feasible affine upper bound.

**Finite exact lower bounds.** The D switching sheet partitions the box into two closed convex polyhedra with 10 and 6 vertices, giving 12 distinct orientation-specific D anchor points. The S sheet partitions it into two polyhedra with 8 and 8 vertices, giving 12 orientation-specific S anchors. At **all 24** rational anchors the unrestricted original-index Bellman recursion (all 228 observations, full 141-profile response arrays, integer-scaled exact rational costs) equals the displayed feasible-tree cost. All rational anchors, expected exact values, visited-state counts and their checked outcomes are in the companion JSON certificate. Two new anchors — D at `(49/64,7/16,4657/6144)` and S at `(49/64,7/16,25/32)` — were also independently reproduced from the original raw-94-family input and a separate exact Bellman implementation.

**Continuous proof.** The unrestricted global Bellman value B(p) equals the pointwise infimum over affine costs of all complete feasible identifying trees, so is jointly concave in p=(a,b,z). In each convex optimality cell a specific complete feasible witness has affine cost L(p). At every vertex v of that cell the exact unrestricted Bellman computation gives B(v)=L(v). For any convex combination p=Σ λᵢvᵢ, concavity gives B(p)≥Σ λᵢB(vᵢ)=L(p); feasibility gives B(p)≤L(p). Equality follows throughout every closed cell, including all irrational parameter choices and ties.

**Sharp bounds.** Intersect the two strategy partitions; the three nonempty joint convex polyhedra have respectively 8, 10, and 6 vertices. Their gap is affine, hence each extreme occurs at a vertex. Exact rational enumeration yields the attained min/max given above.

## Source and validation

Original frozen SHA256: `frozen_original_master.txt = cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`; `EC49FPG_PROFILE.csv = a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`.

Observed: **24/24 exact primary Bellman anchor matches**, **2/2 independent raw94 cross-checks**, **4/4 complete 141-leaf native tree replays**. There is no floating-point step in the proof. The original-data/solver/tree/checker/actual logs are in the self-contained evidence archive `EC49FTG_NATIVE_BRC_MOVING_TWO_SWITCH_COMPLETE_EVIDENCE_20261119.tar.xz`, SHA256 `4b61106ec8a6d34b68ff9136b1ddda16a132aecc43ccc1d4cb5e43a05a27ae89`. The companion GitHub JSON enumerates 24 anchors and the companion Python verifier checks its exact geometry, path replay and optional native Bellman reruns.

**Next problem.** Decrease z below 3/4 and determine the first new optimum replacing D45/S105; extend a above 49/64. The direct 45-use phase and swapped 105-use phase have now been established on positive-volume three-dimensional regions.

Publication here is independent portable research; no formal Task CLAIM, Activity checkpoint, Result, Review or P000 revision is asserted.
