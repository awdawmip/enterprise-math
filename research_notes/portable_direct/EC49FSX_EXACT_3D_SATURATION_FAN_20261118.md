# EC49FSX — Exact three-price native BRC saturation fan with sharp a-boundaries

**Date:** 2026-11-18. Frozen source: `awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Prior frontier: [EC49FSW PR #2735](https://github.com/awdawmip/enterprise-math/pull/2735) at `feede7bcbbe280b1fa58a5cb377dd7dcfb1e3416`.

## New exact continuous theorem

The BRC16943 finite model has 310 original configurations, 141 **named joint-response profiles** (uniform prior), and 228 distinct **physical named observations**, without identifying query aliases. All strict-splitting complete adaptive decision trees are admissible. Discounts on physical q32, q34 and q140 are a,b,z; respective prices are (1-a)t,(1-b)t,(1-z)t for t>0, and all other queries cost t. Normalize F(a,b,z)=141V(a,b,z)/t, where V is optimal average cost.

For **every real** triple with a in [1/2,2/3], b in [7/16,57/128], and z in [1531/2304,1]:

```
Direct:  D=F(a,b,z) = 319 - 18a - 75b - 141z.
Swapped: S=F(b,a,z) = min(325 - 94a - 9b - 141z,
                          323 - 89a -12b - 141z).
```

Swapping acts on **physical** q32/q34, so the coefficient of a in S counts physical q34 uses. The S-policy switches along the moving boundary **5a=2+3b**. When 5a>=2+3b the optimal S witness has complete path-use vector (325,9,94,141); otherwise the optimal vector is (323,12,89,141). The direct witness has vector (319,18,75,141). Every vector is (total query uses,q32 uses,q34 uses,q140 uses) across all 141 complete named-state paths.

Thus the orientation cost defect has an exact two-part formula:
```
D-S = -6 + 76a -66b  where 5a >= 2+3b;
D-S = -4 + 71a -63b  where 5a <= 2+3b.
```
The **sharp attained bounds** over the full closed three-dimensional box are `441/128 <= D-S <= 379/24`. The lower extreme is at (a,b)=(1/2,57/128), the upper at (2/3,7/16), each for all allowed z.

The **a-interval [1/2,2/3] is sharp** for this displayed two-policy swapped formula on the prescribed b,z rectangle. A complete native witness N_below=(319,12,81,141) has `N_below-C=8a-4`, strictly negative below a=1/2. Another feasible native witness NS_up=(324,8,141,93), already independently pinned in EC49FSV, satisfies `NS_up-T=-1+b-47a+48z`. At b=7/16 and z=1531/2304 this equals zero at a=2/3 and is strictly negative for every a>2/3. These witnesses establish both one-sided boundaries without assuming the competing policies are the unique optimizers.

## Continuous proof by exact original-data certificates

For any feasible complete native decision tree, normalized total cost is the affine function U-a*N32-b*N34-z*N140. Hence unrestricted Bellman value is the pointwise minimum of feasible affine costs and is **jointly concave** in (a,b,z). Each exhibited complete tree is a feasible upper bound.

Fix z0=1531/2304. Partition the a,b rectangle by 5a=2+3b. The T-optimal triangle has vertices `(53/80,7/16), (2/3,7/16), (2/3,4/9)`; the C-optimal remainder is convex. For S, original-data exhaustive exact rational Bellman computation over **all 228 physical queries** at the four rectangle corners and two line-intersection vertices agrees with the relevant feasible affine policy. For D, the four original-data Bellman corner values agree with its feasible affine tree. All ten exact values are in the companion machine certificate.

On each convex polygon, concavity bounds the true optimum below the interpolation of its exact vertex values, which is precisely the proposed affine cost. The feasible tree gives the reverse inequality. Therefore these formulas hold for **all real a,b** in the rectangle at z0, not merely a grid.

Every displayed optimal tree uses q140 once along every named path, i.e. N140=141. No strict-splitting tree can use one physical q140 twice on the same path because the second outcome is determined by the first. Every feasible tree thus uses q140 at most 141 times across paths. For z>=z0, the saturated optimal witness decreases in cost by exactly 141(z-z0), at least as fast as any competitor. Hence it stays optimal for the entire real z interval [z0,1]. The piecewise defect and its sharp extrema follow by rational affine polygon-vertex evaluation.

## Exact ten-vertex source evidence

All rows are normalized exact total Bellman costs at z=1531/2304:

| Orientation | a | b | Bellman optimum |
|---|---|---|---|
| D | 1/2 | 7/16 | 140923/768 |
| D | 1/2 | 57/128 | 140473/768 |
| D | 2/3 | 7/16 | 138619/768 |
| D | 2/3 | 57/128 | 138169/768 |
| S | 1/2 | 7/16 | 137899/768 |
| S | 1/2 | 57/128 | 137827/768 |
| S | 2/3 | 7/16 | 126491/768 |
| S | 2/3 | 57/128 | 42145/256 |
| S | 53/80 | 7/16 | 633959/3840 |
| S | 2/3 | 4/9 | 126443/768 |

Original master SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`; 141-profile CSV SHA256 `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`. Two selected swapped values were independently recomputed from the 94-family raw decoder and a separate exact 228-observation Bellman implementation: (a,b,z)=(1/2,7/16,z0) yielded 137899/768; (53/80,7/16,z0) yielded 633959/3840. Five complete trees (D,T,C,N_below,NS_up) were replayed over all 141 profiles using native named observation indices, and their raw SHA256 values are recorded in the certificate.

**Reproducibility:** `EC49FSX_CERT.json` and `EC49FSX_EXACT_CHECK.py` provide exact formula/vertex checks. The self-contained local archive `EC49FSX_NATIVE_BRC_SHARP_3D_SATURATION_FAN_EVIDENCE_20261118.tar.xz`, SHA256 `0b4090b1aca706c11598e95cd7e367b95b2f4f68f5454ad094c75c75ead68d6d`, includes the pinned full raw source, two native exact solvers, tree bytes, all logs, full replay script and SHA256 manifest. Its current local provenance is recorded rather than asserting remote blob publication. Remote GitHub proof/certificate support this author-level result; the full compressed archive is an accompanying conversation artifact.

**Status:** AUTHOR_PROVED / EXACT_PRIMARY_10_VERTICES / INDEPENDENT_2_VERTICES / 5_FULL_NATIVE_TREES_REPLAYED / NOT_REVIEWED. This portable scientific research does not issue CLAIM, Result, Review or current owner authority.

**Next exact question:** determine the lower joint-q140 saturation surface z*(a,b) below 1531/2304 on the enlarged a,b rectangle; resolve where the 93-use and other non-saturated policy planes overtake the 141-use strategies while preserving all physical-query identities.
