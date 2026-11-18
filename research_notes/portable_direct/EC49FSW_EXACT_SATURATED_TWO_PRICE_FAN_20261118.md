# EC49FSW — Exact q140-saturated two-price BRC fan and b=4/9 transition

Date: 2026-11-18. Source: frozen immutable scientific input `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Prior frontier: [EC49FSV PR #2728](https://github.com/awdawmip/enterprise-math/pull/2728). Status: **AUTHOR_PROVED / EXACT_PRIMARY_12_VERTICES / INDEPENDENT_3_ANCHORS / NOT_REVIEWED**. No Task/CLAIM/Result/Review authorization is asserted; this is independent portable research.

## Native model and theorem

The finite BRC16943 experiment has 310 original configurations, 141 **named joint-response** profiles (uniform prior), and 228 distinct **physical** observations. Do not identify physically different observers that happen to share an outcome partition. Every strict-splitting complete adaptive decision tree is admissible. Price physical q32 at `(1-a)t`, q34 at `(1-b)t`, q140 at `(1-z)t`, and every other physical query at `t>0`. Set `F(a,b,z) = 141*V(a,b,z)/t`, the normalized optimal total cost.

Fix `a=2/3`. For **all real numbers**
```
7/16 <= b <= 57/128
1531/2304 <= z <= 1
```
the unrestricted, exact 228-query Bellman optima are
```
D(b,z) := F(2/3,b,z) = 307 - 75*b - 141*z,
S(b,z) := F(b,2/3,z) = min(787/3 - 9*b - 141*z,
                            791/3 - 12*b - 141*z).
```
The swapped orientation has a **genuine switch of complete optimal tree type at `b=4/9`**, for every z in this interval. In the first open subinterval the optimal witness vector is `(327,9,97,141)`, and in the second it is `(325,12,92,141)`, both feasible and both optimal on the tie line. The direct witness `(319,18,75,141)` is optimal everywhere. Vectors count `(U,n_q32,n_q34,n_q140)` over all 141 named-state paths.

In particular, q140 is used **on all 141 paths** by an optimal tree in both orientations across the closed rectangle. The orientation defect has exact formula
```
D-S = 134/3 - 66*b,    for 7/16 <= b <= 4/9,
D-S = 130/3 - 63*b,    for 4/9 <= b <= 57/128.
```
It is **independent of z, strictly positive, and has exact attained sharp range**
`5867/384 <= D-S <= 379/24`. The maximum is at b=7/16 and the minimum at b=57/128.

The **uniform lower z=1531/2304** is sharp for *joint universal-path q140 optimal saturation over the stated b interval*: the previously verified b=7/16 swapped slice in PR #2728 has no optimal 141-use q140 tree strictly below this point, and admits one starting exactly there. Sharpness does not claim a threshold for arbitrary b outside the interval.

## Complete proof

For any complete tree with use vector `(U,n32,n34,n140)`, the normalized expected cost is the affine form `U-a*n32-b*n34-z*n140`. The unrestricted Bellman value is the pointwise minimum of these affine forms over all native physically indexed feasible trees, hence is **jointly concave in (b,z)**. Three complete trees (vectors above) are exact feasible upper bounds. The two swapped witness lines cross when `(791/3-12b)-(787/3-9b)=4/3-3b=0`, i.e. `b=4/9`.

Split the rectangle at b=4/9, yielding two closed subrectangles. For `b in {7/16,4/9,57/128}`, `z in {1531/2304,1}`, and both D/S orientations, the unrestricted finite 228-physical-query Bellman oracle was evaluated with **exact rational arithmetic**: all twelve values agree with the feasible-tree formulas. On each subrectangle the candidate optimal value is one affine function. By concavity, the unrestricted optimum at every interior point is at least the convex combination of its exact vertex values, hence at least that affine function. The feasible complete tree bounds the optimum from above by precisely that affine function. Consequently the two sides coincide throughout each real subrectangle, including the crossing and all boundary points. Subtraction gives the defect; its negative slopes on each b interval give the sharp bounds.

## Exact 12-vertex oracle certificate

All entries below are exact `141*V/t`. `b` rows in order `7/16,4/9,57/128`; `z` columns in order `1531/2304,1`.

| Orientation | b | z=1531/2304 | z=1 |
|---|---|---|---|
| D | 7/16 | 138619/768 | 2131/16 |
| D | 4/9 | 46073/256 | 398/3 |
| D | 57/128 | 138169/768 | 16973/128 |
| S | 7/16 | 126491/768 | 5635/48 |
| S | 4/9 | 126443/768 | 352/3 |
| S | 57/128 | 42145/256 | 11263/96 |

Independent original-94-family data reconstruction, using a distinct exact Bellman solver and all 228 original physical observations, was separately run on three load-bearing points: `D(7/16,2/3)=2883/16`, `S(4/9,2/3)=493/3`, `S(57/128,1)=11263/96`. The original native solver agrees on all twelve proof vertices. These are finite exact computational certificates; they are not formal proof-assistant admissions or independent scientific review.

## Evidence and limitations

Full local self-contained scientific evidence archive: `EC49FSW_NATIVE_BRC_SATURATED_TWO_PRICE_FAN_EVIDENCE_20261118.tar.gz`, SHA256 `ac1c15e7dd787e1efd3ca8a9d94a4732f982f858e0192c9d806293004340851e`. It contains the pinned original master and profile CSV, full native solver and independent decoder, three complete physical-index decision trees, replay verifier, all exact anchor results, independent checks, and per-file hash manifest. The full archive was created in the originating research environment, not uploaded as a GitHub blob in this PR. The companion source `EC49FSW_REPRODUCE.py` explains how to run it. The companion `EC49FSW_CERT.json` machine-records the theorem and 12 values. No changed P000/worldview or scientific input.

**Next frontier:** allow a to vary in a neighborhood of 2/3, checking whether the b=4/9 transition becomes a sloped two-parameter surface, and exhibit exact native Bellman breakpoints if other policies intrude. Do not extrapolate the exact formula beyond its certified box without new calculations.
