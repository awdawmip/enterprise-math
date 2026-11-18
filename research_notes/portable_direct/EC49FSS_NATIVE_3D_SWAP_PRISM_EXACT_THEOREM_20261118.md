# EC49FSS — native BRC16943 exact adjacent three-price prism

Date: 2026-11-18. Frozen source: awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Direct parent: EC49FSR PR #2718@a9a657b421b69b4676a7ad6e0c59829b29c75a7f. Scientific status: AUTHOR_PROVED / EXACT_PRIMARY_24_VERTICES / INDEPENDENT_4_VERTICES / NOT_REVIEWED. Portable independent research, not a canonical Task CLAIM, Result, Review or Activity checkpoint.

## Exact original-native identification problem

Retain all 310 original configurations, their 141 distinct original *named joint-response profiles* with uniform prior over profiles, and all 228 physically named deterministic observations. Every complete strict-splitting adaptive identification tree is admitted; no observation is collapsed into an alias. Give q32 price (1-a)t, q34 price (1-b)t, q140 price (1-z)t, and every other observation price t>0. Let F(a,b,z)=141V(a,b,z)/t be the unrestricted optimal total normalized cost.

**Theorem.** For every real point in the closed, positive-volume prism

  1/2 <= a <= 1; 27/64 <= b <= 29/64; 1/2 <= z <= 9/16,

the direct and q32/q34 price-swapped optima satisfy EXACTLY

  D(a,b,z)=F(a,b,z)
    =min(319-18a-75b-141z, 316-141a-43b-30z);

  S(a,b,z)=F(b,a,z)
    =min(315-141a-10b-77z, 323-89a-12b-141z).

The four complete native decision-tree path-use vectors, in the order (total tests, q32 uses, q34 uses, q140 uses), are

| ID | Vector | Feasible affine cost |
| --- | --- | --- |
| A | (319,18,75,141) | 319-18a-75b-141z |
| E | (316,141,43,30) | 316-141a-43b-30z |
| H (swapped) | (315,10,141,77) | 315-141a-10b-77z |
| W (swapped) | (323,12,89,141) | 323-89a-12b-141z |

All four full trees were recomputed, losslessly packed, and replayed for each of the 141 original named states with exact response-following paths and use counts. In the swapped orientation the parameter a is the discount on q34, not q32.

The **moving direct interface** is

  a_D(b,z)=(32b+111z-3)/123

(A below, E above). The **moving swapped interface** is

  a_S(b,z)=(32z+b-4)/26

(W below, H above, provided a_S>=1/2). Throughout the rectangle a_S<a_D. The positive-volume W region appears above z=(17-b)/32; at z=1/2, H is the only positive-volume swapped phase.

## New sharp exchange-defect bound and plateau

Every point in the prism has the strict, sharp inequality

  D(a,b,z)-S(a,b,z) >= 189/64 > 0.

Equality holds on the **entire continuum** a=1/2, b=29/64, z in [1059/2048,9/16].

For the three ordered phases (when the first exists):

  a<=a_S:      D-S=-4+71a-63b;
  a_S<=a<=a_D: D-S=4+123a-65b-64z;
  a>=a_D:      D-S=1-33b+47z.

For fixed b,z, the gap grows with a with slopes 71,123,0; thus its minimum is attained at a=1/2. At a=1/2 the gap is max(4+123/2-65b-64z,-4+71/2-63b); it decreases in z until z=(17-b)/32 and then equals 63(1/2-b). The global minimum occurs at b=29/64 and equals 189/64 on exactly the stated z interval.

## Complete continuum proof and machine certificate

For every fixed feasible full original-native decision tree its exact total cost is affine in a,b,z. The unrestricted optimum, the pointwise infimum of feasible tree costs, is jointly concave and never above any witness plane. The prism cut by the two cost-equality surfaces has four closed convex cells (A,E,H,W), with exact vertex counts respectively 8,8,10,6. The sets of distinct direct and swapped vertices have 12 points each.

The frozen 228-observer, 141-profile Fraction-exact Bellman solver exhaustively recomputed the unrestricted optimum at **all 24 region vertices**. Every one equals its feasible witness plane (certification file contains coordinates, exact values and reached subset counts). On each convex cell, express any point as a convex combination of cell vertices; concavity gives an optimum lower bound equal to the affine witness, and witness feasibility gives the opposite inequality. Thus the four affine formulas hold for every real parameter in the full prism, not merely on a grid.

A second Bellman implementation with an independently reconstructed 94-family raw observation palette reproduced four structurally load-bearing points: D(389/656,27/64,9/16)=517907/2624, S(71/128,27/64,9/16)=24225/128, S(1/2,29/64,9/16)=775/4, and S(925/1664,29/64,9/16)=314123/1664. The independent run reached respectively 9367,8680,9280,8656 distinct subproblems. The exact input SHA256 values are master cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e and profile CSV a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f, unchanged from the pinned science.

The evidence archive contains full original raw inputs, both native decoders, executable Bellman replay, 24-point machine results, all four full named trees with decompressed SHA256, proofs and logs. Independent peer review and mathematical admission remain pending. The result belongs to the specified native BRC identification optimization, not an external physical calibration.

## Provenance and next discriminating problem

This advances EC49FSR's prism ending at z=1/2; the previous direct 24-use and swapped 69-use witnesses meet the new ones at the shared boundary. The newly emerging q140-saturated swapped W face yields a defect plateau and demonstrates that merely extrapolating prior fixed menus misses a real native phase.

The next concrete step is the complete native Pareto fan for z>9/16, especially the (a,b,z)=(1,29/64,5/8) challenger with vector (332,141,62,42). Locate its exact tie surfaces and the next sharp swap-penalty extremum.

Historical researcher source: EM-DIRECT-8454C6, SID MCP-44cfc4e6f2094f96861854ebefc77e84, Activity RA-ED136F89271FD89288F3E58D. The previously verified continuation request was FAILED / CANONICAL_REJECTED: unknown current immutable task publication. No live owner/CLAIM authority is claimed; this material is published only under the existing independent portable research route and does not alter P000 or the immutable frozen science.
