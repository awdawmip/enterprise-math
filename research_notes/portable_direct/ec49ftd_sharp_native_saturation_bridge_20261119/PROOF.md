# EC49FTD — exact sharp q140 saturation bridge (native BRC16943)

2026-11-19 · AUTHOR_PROVED / EXACT_PRIMARY_12_VERTICES / INDEPENDENT_RAW94_2 / FOUR_FULL_NATIVE_TREE_WITNESSES / NOT_REVIEWED. Independent portable scientific work; no formal CLAIM, Result or Review claimed.

**Frozen scientific input.** \`awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`. It contains 310 original configurations, 141 individually named joint-response profiles, and all 228 original indexed physical observers. Keep observer indices, outcomes, branches and profile identities unchanged. Original source SHA256: \`frozen_original_master.txt = cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e\`; \`EC49FPG_PROFILE.csv = a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f\`. Previous native exact solver and source: [EC49FTA PR #2750](https://github.com/awdawmip/enterprise-math/pull/2750), [EC49FTC PR #2757](https://github.com/awdawmip/enterprise-math/pull/2757). No new X6 dynamics are asserted here.

For a positive baseline price t, discounts a,b,z apply respectively to q32,q34,q140, and all other query discounts are zero. For S, interchange only a and b, not the named queries/outcome maps. The costs D and S are global optimal standardized identification costs \`141 V/t\` over all 228 native observations.

## Theorem

**For every real parameter triple**
\[
\frac23\le a\le\frac34,\quad
\frac7{16}\le b\le\frac{57}{128},\quad
\frac{49}{64}\le z\le1,
\]
the unrestricted native Bellman optima are exactly
\[
\boxed{D=\min\{319-18a-75b-141z,\;326-32a-68b-141z\}},
\]
\[
\boxed{S=\min\{327-97a-9b-141z,\;325-92a-12b-141z\}}.
\]
The original-price switch is \`2a=1+b\`, and the swapped-price switch is \`5a=2+3b\`. Both optimal strategies admit full q140 saturation: q140 is queried on every one of the 141 named-profile paths. Consequently the gap is independent of z and obeys the **attained sharp bounds**
\[
\boxed{\frac{5867}{384}\le D-S\le\frac{351}{16}}.
\]
Equality at the lower/upper ends occurs at \`(a,b)=(2/3,57/128)\` and \`(3/4,7/16)\`, respectively, throughout the stated z interval.

**The uniform lower z boundary is sharp.** At \`(a,b)=(3/4,7/16)\`, the saturated optimal S tree \`SQ\` has cost \`327-97a-9b-141z\`. A valid original-index counterexample tree \`T\` uses \`(U,N32,N34,N140)=(332,8,141,105)\` and costs \`332-141a-8b-105z\` in S. At this (a,b), \`T-SQ=36(z-49/64)\`. Both tie at z=49/64, and T is strictly cheaper for every z<49/64. Every fully saturated tree has slope -141 in z and is no better than SQ at z=49/64 by the exact Bellman certificate; hence none can be optimal below z=49/64 at this (a,b). At z=3/4, exhaustive native Bellman confirms T attains 144 while SQ costs 2313/16, an improvement of 9/16.

## Witnesses and exact finite proof

Four complete feasible original-index identifying trees, 141 individually replayed leaves each, have usage tuples \`(U,N32,N34,N140)\`:
\`\`\`
D1 = (319,18,75,141)   D2 = (326,32,68,141)
SQ = (327,9,97,141)   SR = (325,12,92,141).
\`\`\`
Their fixed affine costs give upper bounds valid for all real parameters. Their original-path JSON SHA256 are:
\`\`\`
D1 c610116426be1fe39da788d8e36f3629e9de02831f0f377d7548914d7cde0495
D2 fa138a5158b6cb45ddb8271f86e4b43f59305360469cff27337c81f5d1b9a3d2
SQ 66425d046a0332de7c98e042953200fed50c7340f993df48e3520ab51cd7b7bc
SR 740b522ce31fac8332df0392b94bed9923e9821c1981c04899021e254ef97db3
\`\`\`
The complete named trees and the full frozen raw-source archive are retained in the independently supplied self-contained EC49FTD evidence package. The companion reproducibility script can regenerate and replay these four trees from the pinned native solver; the companion exact certificate records the 12 native Bellman values.

At z0=49/64, separate the (a,b) rectangle by the respective candidate-plane equality line. The D subdivision has six vertices (four box corners plus \`(23/32,7/16)\`, \`(185/256,57/128)\`); the S subdivision has six vertices (four box corners plus \`(2/3,4/9)\`, \`(427/640,57/128)\`). **All twelve unrestricted 228-query exact-rational Bellman solutions equal the minimum of the corresponding feasible tree costs at these vertices.**

The global optimal value B is the pointwise infimum of affine costs of feasible trees, hence concave in the discounts. On each convex subdivision cell a single witness affine cost L attains the candidate minimum. Vertex equality and concavity give \`B(x)>=L(x)\` throughout that cell; witness feasibility gives \`B(x)<=L(x)\`. Thus \`B=L\` at every *real* (a,b) on z=z0, not only at the finite checked vertices.

A deterministic query is never needed twice on one path of an irredundant identifying tree, so \`N140<=141\`. For an optimal tree T* with \`N140(T*)=141\`, and z>=z0,
\`\`\`
C_z(T) = C_z0(T) - (z-z0)N140(T)
       >= C_z0(T*) - 141(z-z0) = C_z(T*).
\`\`\`
Thus each saturated candidate optimal at z0 stays optimal up to z=1. Every candidate plane has slope -141, leaving both switch sheets fixed and making D-S independent of z.

Across the joint D/S subdivision the gap is affine on each cell. Its extrema are attained among the eight unique arrangement vertices (four corners, two D-switch intersections and two S-switch intersections). Exact values include the minimum \`5867/384\` at \`(2/3,57/128)\` and the maximum \`351/16\` at \`(3/4,7/16)\`.

## Validation scope

Primary: 12 exact Bellman evaluations on all 228 indexed physical observations, using integer-scaled rational DP. Separate checker: two exact independently decoded raw-94-family Bellman computations at \`D(3/4,7/16,49/64)=10515/64\` and \`S(2/3,57/128,49/64)=28871/192\`. Four original-index trees and a fifth strict lower-face challenger were re-simulated on all 141 paths. Source hashes were checked locally. Concavity and saturation prove full continuous parameter coverage. Independent mathematical peer review and formal Source admission remain outstanding.

**New frontier:** sharpen the nonuniform function \`z_sat(a,b)\` below 49/64 where possible; bridge \`3/4<a<31/32\` by identifying new native tree-fan pieces and exact policy-transition vertices. Retain frozen input and named original observers.
