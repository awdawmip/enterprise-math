# EC49FTF — exact native BRC16943 lower q140-saturation fan

Date: 2026-11-19. Status: AUTHOR_PROVED / EXACT_PRIMARY_23_ANCHORS / INDEPENDENT_RAW94_2 / NOT_REVIEWED.

## Input, type and model

Unchanged frozen science: awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Exactly 310 native configurations, 141 individually named joint response states and all 228 original-index physical observations are retained. Parent: EC49FTE, PR #2762, commit b1a7aef4412c138d42ee8917954a6a69c42a738c. This is a price/decision-tree theorem for BRC16943; no X6 physical dynamics or P000 alteration is proposed.

Let positive baseline query price be t and let the standardized identification cost be F=141V/t. In D, the three observation price discounts a,b,z apply to q32,q34,q140. In S, only a and b are interchanged, so q32 receives b, q34 receives a. All 225 other named observation prices remain undiscounted.

A complete deterministic identifying tree with original-query usage vector (U,N32,N34,N140) has D cost U-a*N32-b*N34-z*N140 and S cost U-b*N32-a*N34-z*N140. Original observation identities, path order and distinct named profiles are never quotient-merged by this bookkeeping.

## Exact continuous theorem

For **all real parameters**

- 3/4 <= a <= 4/5,
- 7/16 <= b <= 57/128,
- 13/16 <= z <= 1709/2080,

the unrestricted exact Bellman optima over all 228 original physical observations and 141 named profiles are

D(a,b,z) = min{329-36a-68b-141z, 333-40a-70b-141z}

S(a,b,z) = min{333-105a-9b-141z, 340-141a-8b-115z}.

There are exactly two relevant strategy switching sheets on this prism:

- D switch: 2a+b=2.
- S switch: 36a=7+b+26z.

On 36a>7+b+26z, the named complete T115 tree is optimal in S and uses q140 on 115/141 paths. On the opposite side, the named Smain tree is optimal in S and uses q140 on 141/141 paths. At the sheet both are optimal. This is an existence statement for these witnesses and allows ties with other optimum trees.

The T115-optimal S region lies entirely inside the Dhi-optimal D region; the Dmid/T115 joint cell is empty.

The exchange-price gap G=D-S has **attained sharp bounds**

2749/128 <= G <= 511/20.

The minimum is attained at (a,b)=(3/4,57/128), all z in the prism. The maximum occurs at (a,b,z)=(4/5,7/16,13/16). The three populated joint cells have exact gap planes

- Dmid & Smain: -4+69a-59b;
- Dhi & Smain: 65a-61b;
- Dhi & T115: -7+101a-62b-26z.

In particular the previously identified uniform saturation threshold z=1709/2080 is now refined by the moving pointwise S switch. The region below this threshold contains a positive-volume q140-partially-saturated optimum.

## Proof

**Feasible decision-tree witnesses.** EC49FTE supplied four complete original-index identifying trees. Replaying each on the exact 141 distinct original profiles gives:
Dmid=(329,36,68,141); Dhi=(333,40,70,141);
Smain=(333,9,105,141); T115=(340,8,141,115).
All paths identify their original named leaf without a repeated observer. Dmid and Dhi are evaluated with D prices; Smain and T115 with S prices. Consequently each displayed affine plane is the cost of a feasible global tree, hence is an unrestricted Bellman upper bound.

**Exact unrestricted vertex lower bounds.** Each orientation's minimum-of-two planes cuts the closed three-dimensional prism into two convex polyhedral cells. Dmid and Dhi each have eight vertices, with 12 distinct orientation-specific D anchor points. Smain and T115 have nine and six vertices, with 11 distinct S anchor points. For all 23 distinct orientation-specific rational points, the original unrestricted Bellman recursion over all 228 original-index observations and all 141 named states was run with integer-scaled exact rational prices. Its returned optimum equals the indicated feasible-tree plane at the corresponding vertex. The 23 points, rational optima and visited Bellman state counts are retained in EC49FTF_EXACT_CERT.json. Two new S anchors at z=13/16 were additionally checked by the independent raw-94-family parser and a separate Bellman implementation: (a,b,z)=(4/5,7/16,13/16), cost 10421/80, and (457/576,7/16,13/16), cost 25189/192.

**Continuous extension.** The unrestricted optimum B(p) is the infimum over the affine costs of all feasible complete deterministic identifying trees, hence is jointly concave in p=(a,b,z). On each convex cell, the relevant concrete feasible tree has affine cost L(p). At every vertex v of the cell, the exact unrestricted Bellman check establishes B(v)=L(v). For any p expressed as a convex combination of the vertices, concavity yields B(p)>=L(p). Feasibility yields B(p)<=L(p). Thus B(p)=L(p) everywhere in each of the four cells, including all real irrational parameter points and switching boundaries. This proves the two stated unrestricted formulas on the whole prism.

**Gap geometry.** Intersecting both orientations' strategy cells yields the following nonempty joint cells: (Dmid,Smain) with 8 vertices, (Dhi,Smain) with 9, and (Dhi,T115) with 6; the fourth combination is empty. On each joint cell G is affine, so its extrema are attained at vertices. Exact rational enumeration of all these vertices establishes lower gap 2749/128 and upper gap 511/20 with the displayed witness points.

No floating-point approximation is used in the proof or certified recursion.

## Reproduction, evidence and future work

Original frozen input SHA256 values: frozen_original_master.txt = cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e; EC49FPG_PROFILE.csv = a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f.

The companion exact certificate and checking program are in this branch. Complete frozen source, all four full original-index tree JSON files, the original and independent exact-rational code, the two completed split verification logs and SHA256 manifest are in the associated self-contained EC49FTF evidence archive, SHA256 ce89d517b36f2b93606df4732ebbd30e5f7b0207ce0db4f4bfe0bf0d3b946eed. Its saved verifier supports exact Bellman anchors in bounded chunks (0:12 and 12:23). The prior EC49FTE original trees are also located through PR #2762.

Next scientific problem: lower z below 13/16 to locate the next non-saturated 105-use strategy and its complete 3D switch, and extend a beyond 4/5 with fresh exact native anchors. No formal CLAIM, Result, independent mathematical Review or P000 change is declared by this independent portable note.