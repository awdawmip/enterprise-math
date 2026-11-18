# EC49FSN — Complete global price-swap asymmetry for q140 discount on [0,1]

2026-11-18 · Original frozen native BRC16943 input `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab` · direct continuation of [EC49FSL2 #2704](https://github.com/awdawmip/enterprise-math/pull/2704) at `d499d8db88bf509be290a29253a2f96f1e0a9774`.

Retain **310 original configurations**, **141 complete joint named states**, and **all 228 physical named observers**, with original joint response partitions and a uniform prior. For an unrestricted complete deterministic adaptive identification tree, let `F(a,b,z)=141 V(a,b,z)/t`. Observer q32, q34 and q140 cost `(1-a)t,(1-b)t,(1-z)t`, respectively; all others cost `t>0`. Define `F_A(z)=F(1/2,7/16,z)`, `F_B(z)=F(7/16,1/2,z)`.

## Exact theorem, every real 0≤z≤1

**F_A(0)=F_B(0)=3481/16; for every real 0<z≤1, F_A(z)>F_B(z).** q32/q34 discount-swap symmetry breaks immediately when q140 receives any positive discount, and does not return anywhere in this exact parameter interval.

F_A has **six** full-dimensional-in-z optimal affine phases; F_B has **nine**. An exact full native tree of the original 141 states is retained for every displayed type. Its affine value is `U-a*N32-b*N34-z*N140`.

| Case | Exact z phase | (U,N32,N34,N140) |
|---|---|---|
| A | 0 – 1/6 | (306, 141, 41, 4) |
| A | 1/6 – 1/3 | (307, 141, 41, 10) |
| A | 1/3 – 11/32 | (309, 141, 41, 16) |
| A | 11/32 – 107/248 | (313, 141, 47, 20) |
| A | 107/248 – 67/144 | (311, 28, 141, 51) |
| A | 67/144 – 1 | (319, 18, 75, 141) |
| B | 0 – 15/112 | (306, 41, 141, 10) |
| B | 15/112 – 1/6 | (303, 32, 141, 17) |
| B | 1/6 – 1/4 | (305, 32, 141, 29) |
| B | 1/4 – 5/14 | (304, 28, 141, 32) |
| B | 5/14 – 2/5 | (309, 28, 141, 46) |
| B | 2/5 – 7/16 | (311, 28, 141, 51) |
| B | 7/16 – 1/2 | (311, 10, 141, 69) |
| B | 1/2 – 265/512 | (315, 10, 141, 77) |
| B | 265/512 – 1 | (321, 12, 85, 141) |

The difference `D(z)=F_A(z)-F_B(z)` is exactly:

| Closed z interval | D(z) | D(left) | D(right) |
|---|---|---|---|
| 0 – 15/112 | 6z | 0 | 45/56 |
| 15/112 – 1/6 | -15/16+13z | 45/56 | 59/48 |
| 1/6 – 1/4 | -31/16+19z | 59/48 | 45/16 |
| 1/4 – 1/3 | -43/16+22z | 45/16 | 223/48 |
| 1/3 – 11/32 | -11/16+16z | 223/48 | 77/16 |
| 11/32 – 5/14 | 11/16+12z | 77/16 | 557/112 |
| 5/14 – 2/5 | -69/16+26z | 557/112 | 487/80 |
| 2/5 – 107/248 | -101/16+31z | 487/80 | 113/16 |
| 107/248 – 7/16 | 113/16 | 113/16 | 113/16 |
| 7/16 – 67/144 | -13/16+18z | 113/16 | 121/16 |
| 67/144 – 1/2 | 657/16-72z | 121/16 | 81/16 |
| 1/2 – 265/512 | 593/16-64z | 81/16 | 63/16 |
| 265/512 – 1 | 63/16 | 63/16 | 63/16 |

Consequently, `D(z)=6z` initially; `D(1/2)=81/16`; `D(z)=113/16` on `[107/248,7/16]` and `D(z)=63/16` on `[265/512,1]`. All intervals join continuously. The endpoints of every affine difference segment are positive apart from `D(0)=0`; therefore the difference is strictly positive throughout `(0,1]`.

## Why this is a complete continuous theorem

For each exact rational parameter boundary of each optimal phase, unrestricted global Bellman recursion was solved over **all 228 original named physical observers**: `T(S)=min_{q strictly splitting S} (|S| p_q + Σ_r T(S_{q,r}))`, with `T(singleton)=0`. Exact primary calculations certify **7 A vertices** and **10 B vertices**. Each Bellman value coincides with the saved complete native tree's exact affine cost at the vertex. The minimum over all feasible fixed-tree affine functions is concave in z. For any interval between certified vertices, concavity supplies a global lower bound by its endpoint chord; one saved native full tree realizes the identical affine chord throughout, hence the optimal value equals that chord at every real point. This is an exact proof, not a rational mesh extrapolation.

All **15** witness trees passed full 141-state original-response replay and path counting. Full witness JSON, precise SHA256, original source, primary/independent solver code, exact Bellman vertex reports, rational geometry, and execution logs are in the self-contained evidence package. A separately decoded native implementation confirmed the A endpoints z=0,1/6 in this calculation; earlier #2704 separately crosschecked z=0 and z=1/32 for both orientations. Independent recalc of the other newly discovered endpoints remains to be completed; no independent reviewer has admitted this result.

This is a **finite original BRC named-observer pricing theorem**; it is not a claim about physical-axis symmetry of the P000 Heartbeat World. Frozen scientific source and P000 are unchanged.

## Research provenance and next question

Research status `AUTHOR_PROVED / EXACT_PRIMARY_FINITE_EXHAUSTIVE / INDEPENDENT_PARTIAL / NOT_REVIEWED`. Portable artifact publication only; no current formal immutable Task, CLAIM, Result, Review or Activity authorization is represented.

Next investigate the **swap-asymmetry zero set in the full three-price cube**, particularly as the pair (a,b) varies through and near the diagonal a=b. Preserve the exact named observer partition, finite source pin and this 15-tree certificate; do not assume a q32/q34 permutation automorphism in the three-price problem.
