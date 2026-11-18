# EC49FTA extension: q32 discount reaches the full closed interval through a=1

Date: 2026-11-18. Frozen original BRC16943 scientific input: enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. This is an **extension of the same theorem and four original-index witness trees** in EC49FTA_EXACT_TWO_SWITCH_3D_PRICE_FAN_20261118.md; it supersedes that note's upper endpoint 9/16 and its upper gap bound while retaining the original narrower theorem as a valid intermediary. Status: AUTHOR_PROVED / EXACT_PRIMARY_23_WIDE_VERTICES / INDEPENDENT_4_TOTAL_ANCHOR_CHECKS / NOT_REVIEWED.

## Extended exact global-optimality theorem

For every **real** (a,b,z) in the larger closed prism

    133/246 <= a <= 1,
    7/16 <= b <= 57/128,
    1/2 <= z <= 9/16,

the original 141-named-profile, 228-physical-observer unrestricted identification costs remain

    D = min(319-18a-75b-141z, 316-141a-43b-30z);
    S = min(315-141a-10b-77z, 323-89a-12b-141z).

The moving direct-price switch surface remains z_D=(3+123a-32b)/111; the swap-price switch surface remains z_S=(4+26a-b)/32. Their feasible portions belong to the stated prism, and outside these portions the corresponding single policy is optimal.

The **new sharp global bounds** throughout this larger region are

    99683/15744 <= D-S <= 13.

The minimum is realized at (133/246,57/128,277277/503808) and again at the same a,b with z=9/16. The maximum is realized at (1,7/16,9/16). At the maximum the exact native optimum values are D=2229/16 and S=2021/16; difference = 13.

## Continuous proof

The four complete admissible named physical decision trees have unchanged usage vectors D1=(319,18,75,141), D3=(316,141,43,30), P=(315,10,141,77), C=(323,12,89,141). Their pathwise native replay on the original 141 response profiles provides the stated affine feasible-tree costs.

For each orientation separately, split the **new larger prism** by its appropriate equality plane. The exact rational vertices are computed by all intersections of triples of faces among the six box hyperplanes and the single switch hyperplane. This gives 11 distinct direct and 12 distinct swapped-price vertices (23 total). The unrestricted exact native Bellman optimum over all 228 physical observation indices agrees with the claimed min-of-two-planes at every one of these **23 wide-prism vertices**, including the newly evaluated a=1 points and moving direct-switch points a=1175/1968 and a=393/656 on z=9/16. All 23 inputs/actual values are saved in EC49FTA_WIDE_A_TO_ONE_23_BELLMAN_ANCHORS_20261118.csv.

The minimum cost is concave in all discounts because it is the minimum of the affine costs of all admissible decision trees. On either convex strategy cell, exact unrestricted equality at every vertex implies the unrestricted cost is at least its interpolated affine witness; feasibility of that witness gives the opposite inequality. Thus equality holds for every real point in both cells and for all real points in the larger prism.

The overlay of both switch planes has exactly 15 feasible rational vertices. Since D-S is affine on each joint chamber, its extrema occur among these vertices. Exact enumeration yields the stated bounds, with sharp witnesses above.

Four original-94-family independent recalculations were executed across the two rounds: the earlier direct transition (9/16,7/16,931/1776) with D=14959/74; earlier swapped transition (133/246,57/128,277277/503808) with S=96699527/503808; **new sharp maximum** at (1,7/16,9/16) with D=2229/16 and S=2021/16. The first two belong to the original narrower prism; all four values agree with the original 228-observer primary oracle. Full independent coverage remains partial, while primary exact coverage is 23/23 vertices of the enlarged prism.

The original narrow-prism theorem, original CSV and new full native D3 tree remain valid. This extension expands a from 9/16 to 1 and strengthens the upper bound from 4973/444 to **13**. It is a continuous exact 3D result on the full physically meaningful discount interval a<=1.

## Reproduction and next frontier

Use the exact rational geometry program EC49FTA_WIDE_A_TO_ONE_VERIFY_20261118.py, wide 23-point CSV, and the same frozen original 228-observation source/raw-94 independent solver and four full trees in the attached self-contained archive. Run full native Bellman at the selected CSV anchor points for the strongest finite check; the two separate author verification passes both covered the exact values claimed. No formal mathematical admission, task CLAIM or Source Activity checkpoint is implied.

**Next open question:** extend the certified four-plane region in the remaining z direction above 9/16, determine the first native successor policies and the moving q140 saturation transitions for a and b varying over this full price range.