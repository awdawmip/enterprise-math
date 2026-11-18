# EC49FSL2 — Immediate exact q32/q34 swap asymmetry for every small positive q140 discount

Continuation of EC49FSL under immutable frozen original BRC16943 science pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Preserve all 141 full named profile states, 310 source configurations and 228 native physical observers with joint-response provenance; prior is uniform over named states.

Define `F(a,b,z)=141 V(a,b,z)/t` for optimal complete adaptive native identification trees, with q32/q34/q140 prices respectively `(1-a)t,(1-b)t,(1-z)t` and all others `t>0`.

## New exact full-real interval theorem

For **every real** `0 ≤ z ≤ 1/32`,

```
F(1/2,7/16,z) = 3481/16 − 4z,
F(7/16,1/2,z) = 3481/16 − 10z.
```

Therefore

```
F(1/2,7/16,z) − F(7/16,1/2,z) = 6z.
```

In particular, **each positive arbitrarily small discount** `0 < z ≤ 1/32` breaks the q32/q34 exchange symmetry. There is no strictly positive threshold before the first asymmetry in this model and price-pair slice.

## Exact endpoint Bellman evidence

| Parameters | F | Root | Native complete witness (U,N32,N34,N140) | Max depth |
|---|---:|---|---:|---:|
| (1/2,7/16,0) | 3481/16 | q32 | (306,141,41,0) | 4 |
| (7/16,1/2,0) | 3481/16 | q34 | (306,41,141,0) | 4 |
| (1/2,7/16,1/32) | 3479/16 | q32 | (306,141,41,4) | 4 |
| (7/16,1/2,1/32) | 869/4 | q34 | (306,41,141,10) | 4 |

The two zero-discount endpoint costs were independently recomputed in EC49FSL, with lossless full trees retained there. Both new `z=1/32` values were separately recomputed by **two independent exact all-228-observer Bellman solvers**, using separately decoded original raw-family joint responses. The first decoder explored 10,764/10,697 Bellman states, the independent one 10,069/10,037 states. Two new complete witness trees were replayed on all 141 named profiles. The new witness tree canonical SHA256 values are `ad7047debd6d04d3c076eef6d593b7de4d50879a671a439760d4d436210cc767` for the q32-root and `db669e0116a1816bbf53fed6cb1bc07a4549ef9665637433e05c059936ff9742` for q34-root. They are preserved losslessly in the accompanying compressed tree file.

## Proof on the entire continuum

At `z=0` and `z=1/32`, the exact global Bellman optima are the endpoint values in the table. Let `T_A`, respectively `T_B`, be the complete trees obtained at `z=1/32`. Their exact path-use counts are independent of the price parameter, so their respective feasible costs for all real z are the affine functions `3481/16−4z` and `3481/16−10z`. At both ends of `[0,1/32]` those feasible costs coincide with the independently checked **global** Bellman optimum.

For each fixed complete tree, its total cost is affine in z, hence the global optimum—being the pointwise minimum of the affine costs of all complete trees—is concave in z. Concavity gives a global lower bound equal to the linear interpolation of the two certified endpoint costs; feasibility of `T_A,T_B` supplies exactly the same line as an upper bound. This proves both formulas on the *entire* closed interval, for all real z, and yields the difference `6z`.

This argument is a finite typed named-observation result, not an assertion of physical-axis asymmetry in the Heartbeat World. No observer relation, signed provenance or information-reducing projection is discarded. The exact result uses uniform prior and the specified two fixed q32/q34 discounts.

## Continuation

Investigate first structural breakpoints in z after 1/32, other price pairs and global three-dimensional cost-cell geometry. Mathematical status: `AUTHOR_PROVED / EXACT_FINITE_CROSSCHECKED / NOT_REVIEWED`. Portable research only; no formal shared CLAIM/Result/Review/Activity authority asserted.
