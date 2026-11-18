# EC49FSL — A certified failure of q32/q34 price-exchange symmetry under a third discounted observer

Date: 2026-11-18 · Input pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab` · `AUTHOR_PROVED / EXACT_FINITE_CROSSCHECKED / NOT_REVIEWED`

## Exact counterexample (all original physical observers)

In the pinned BRC16943 finite model, retain the original 310 raw configurations, 141 distinct *joint named* profile states, all 228 native physical named observers and their full response partitions, and uniform prior over the 141 profiles. Let q32, q34, q140 have respective independent discounts `a,b,z` in `[0,1]` (prices `(1-a)t,(1-b)t,(1-z)t`); all other observers have price `t>0`. Write `F(a,b,z)=141V(a,b,z)/t` for the minimum total expected complete identification cost.

With the q140 discount fixed at `z=1/2`, **swapping the q32 and q34 discounts changes the globally optimal cost**:

| (a,b,z) | Exact F | Optimal root | Optimal tree (U,N32,N34,N140) | Max depth |
|---|---:|---:|---:|---:|
| (1/2,7/16,1/2) | 3307/16 | q140 | (319,18,75,141) | 3 |
| (7/16,1/2,1/2) | 1613/8 = 3226/16 | q34 | (311,10,141,69) | 3 |

Consequently,

```
F(1/2,7/16,1/2) - F(7/16,1/2,1/2) = 81/16 > 0.
```

For the **same pair** of q32/q34 prices with q140 at original price `z=0`, the equal-cost symmetry holds at this pair:

| (a,b,0) | Exact F | Optimal root | Optimal tree (U,N32,N34,N140) | Max depth |
|---|---:|---:|---:|---:|
| (1/2,7/16,0) | 3481/16 | q32 | (306,141,41,0) | 4 |
| (7/16,1/2,0) | 3481/16 | q34 | (306,41,141,0) | 4 |

Thus the previous two-discount symmetric lower-envelope identity at `z=0` does not generalize to arbitrary discounted third native observations `z>0`. This is a concrete **exact native finite-model counterexample**, without an asymptotic claim.

## Calculation and independent validation

All four parameter triples were solved by a primary exact rational Bellman recurrence on the original 228×141 native joint-response matrix:

`T(S)=min_{q: strict split of S} (|S|p_q+Σ_r T(S_{q,r}))`, `T({i})=0`.

Independent validation rebuilt a fresh 228-observer response matrix from the frozen original raw family, using `EC49FSA_FSB_INDEPENDENT_CHECK.certify`, then solved the same global finite problem with a separately written Bellman implementation. **All 4/4 optimal values match exactly**. Every resulting witness tree was replayed through all 141 original named states, with all leaves correctly identified, and its exact call-use vector and maximum depth counted from the tree itself. The two separate solvers have different internal DP state counts; both implement exhaustive strict-splitting minimization rather than fixed-root optimization.

A lossless compressed original-native tree for each of the four parameter points is included in `EC49FSL_FOUR_NATIVE_SWAP_TREES_JSON_ZLIB_BASE64.txt`. All four witness SHA256 digests, full rational results and solver effort values appear in the machine report.

## Scientific interpretation and next question

The third observation q140 interacts with the q32/q34 observer families in a way the two-observation price symmetry did not constrain. The economic value of the third discounted *joint native observer* depends on which of q32 or q34 receives the larger discount. This is an observer-partition interaction, not a claim that the primitive axes of the P000 Heartbeat World lose their project-defined orthogonality. No factor-only or Boolean projection replaces the joint native responses.

Next: determine a minimal rational `z>0` witness, characterize the exact **swap-asymmetry boundary** in three-price space, and enumerate the corresponding three-dimensional exposed affine strategy cost cells. Preserve each whole named response partition and the original science pin.

Source ancestry: EC49FSK PR #2703 @ `4e6e2c7263edaf2c9f8c46e20c39128b7547e530`. The original researcher ID and Activity are historical provenance only, not current CLAIM authorization. This is independently saved portable research and awaits independent mathematical review.
