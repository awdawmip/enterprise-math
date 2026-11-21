# X6 R80 — 11–15 Port 的五候选精确最小核心（独立全整数格证书）

Date: 2026-11-21 (Asia/Shanghai).  
Scientific status: **FINITE_EXHAUSTIVE_EXACT_INTEGER_PROOF / AUTHOR_CHECKED / NOT_INDEPENDENTLY_REVIEWED**.  
Frozen scientific pin: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`.  
Sources: R72–R79 for the problem/observer definition; current P000 V5, ACTIVE worldview and portable research contracts. The proof below does **not** invoke the R72 28-vector covering theorem.

## Model and statement

Fix the conditional positive-count BRC star-moment observer, maximum successful degree 4, Port population `p`, and nonzero integer histogram difference `a=(a2,a3,a4)`. The observer has **four** readout channels (moment indices 1–4), one unknown shared additive offset and bounded errors `|e_t| <= eta*w_t`, with arbitrary strictly positive real weights `w=(A,B,C,D)`.

Define
```
q(a) = max(sum_d max(a_d,0), sum_d max(-a_d,0)),
z(a) = (0, 2a2+6a3+12a4, 6a2+24a3+60a4, 14a2+78a3+252a4),
g_ij(a)=|z_i(a)-z_j(a)|/2,
F(a;w)=max_{1<=i<j<=4} g_ij(a)/(w_i+w_j).
```
Then the observer's exact high-degree-histogram recovery threshold is
`eta*(p,w)=min_{a != 0, q(a)<=p} F(a;w)`.
This quantifies only the declared histogram observer and does not collapse complete native event/provenance state.

**Theorem.** For every integer **11<=p<=15** and every `w in R_{>0}^4`,
```
eta*(p,w)=min_{a in S11} F(a;w),
S11 = {(3,-4,1), (3,-7,2), (6,-4,1), (9,-5,1), (10,-5,1)}.
```
The five-vector family is minimal even among *all* feasible integer-difference directions (up to overall sign). Each member is strictly uniquely optimal for some positive weights, so no universally sufficient subset or alternative family omitting one of the five directions is possible for the stated Port range.

| Difference a | q | 6-gap vector g (12,13,14,23,24,34) | Strict-win weights w | eta* | next distinct cost |
|---|---:|---|---|---:|---:|
| (3,-4,1) | 4 | (3,9,9,6,6,0) | (18,12,1,1) | 9/19 | 1/2 |
| (3,-7,2) | 7 | (6,15,0,9,6,15) | (1,12,30,1) | 15/31 | 1/2 |
| (6,-4,1) | 7 | (0,0,12,0,12,12) | (1,1,1,24) | 12/25 | 1/2 |
| (9,-5,1) | 10 | (0,3,6,3,6,3) | (1,1,6,12) | 6/13 | 1/2 |
| (10,-5,1) | 11 | (1,0,1,1,0,1) | (1,1,1,1) | 1/2 | 3 |

## Exact finite proof, independent of the R72 atlas

1. **Complete domain.** Since `q(a)<=15` forces each coordinate of integer `a` into [-15,15], exhaustive enumeration of the even larger [-16,16]^3 cube covers the entire population. Removing zero and filtering yields exactly **12,430** signed nonzero vectors with `q<=15`, and **14,992** with `q<=16`.
2. **Six-coordinate domination.** For each of the 12,430 vectors `a`, compute the six `g_ij` by integer arithmetic. The verifier finds at least one `s in S11` with `g_ij(s)<=g_ij(a)` simultaneously for every pair. Selecting the *first* such `s` in displayed order gives assignment counts **11,498, 42, 810, 18, 62**, whose sum is 12,430. Every `s` has `q(s)<=11`. Since each denominator `w_i+w_j` is positive, `F(s;w)<=F(a;w)` for **all positive real weights**, with no parameter sampling or interpolation. This proves universal sufficiency for every `11<=p<=15`.
3. **Irreplaceability.** For each of the five displayed positive-integer weight profiles, the verifier computes exact costs across *all 12,430 signed differences* by BigInt fraction cross multiplication. Exactly two differences achieve the minimum: `+s` and `-s`. The next distinct objective is strictly higher, as shown in the table. All five are feasible already at p=11, and removing any one raises the optimum at that profile. The five directions are therefore necessary for any universally sufficient representative set, establishing sharp cardinality five (modulo global sign).

The finite proof obligations are completely exposed in the executable script (bounded integer cube, exact `q`, gap formulas, six inequalities, rational comparisons and strict-winner count). The verification is author-checked; independent scholarly validation has not been performed.

## The first new-Port transition

For `w=(1447,167,166,1850)`, a separate complete enumeration including all 14,992 signed differences with `q<=16` gives:
```
eta*(15,w)=1/333, minimizers = ±(10,-5,1), ±(11,-5,1);
eta*(16,w)=1/336, minimizers = ±(15,-6,1).
```
Thus the universal five-core plateau does **not** extend to p=16. This example does not determine the minimum universal family size at p=16.

## Execution and saved evidence

Run `node x6_r80_sharp_five_core_verify.js` (Node.js built-ins only). It prints the exact result JSON and throws on incomplete enumeration, any missing domination, any competing optimal difference or an incorrect 15→16 step. Values are compared as integer cross products, without floating-point tolerance.

- Verifier: [x6_r80_sharp_five_core_verify.js](x6_r80_sharp_five_core_verify.js) at commit `66582b56512908aaaec745aa165530ab0e168dad`, Git blob `55cc8311bb399760aba9e1ce6f450df609af9ee7`.
- Results: [x6_r80_sharp_five_core_results.json](x6_r80_sharp_five_core_results.json) at commit `3805ccc531f70775408f3c0ae12825be23e6706a`, Git blob `18804d4df13004339ede1cd0a63ed8a06b2d0c6d`.
- An independent local author's Python `fractions.Fraction` calculation separately checked the same finite-domain winners and the p=15/16 step; it is a second implementation, not an independent reviewer.

## Scope, provenance, next questions

The result belongs to the **conditional BRC positive-count observer**. It is not a native Heartbeat World six-axis Cell/Link/Port or triadic whole-event time theorem; P000 120° native geometry and the provenance/observer-safety requirements are preserved. The historical R72–R79 source attribution `EM-X6-214D9C` is not a current session credential, Activity write capability or formal CLAIM. The shared X6 task remains with its verified authenticated executor.

Next: find minimal weighted cores for `16<=p<125`, where q-compatible joint domination can be necessary. Separately construct or falsify a typed fiber-preserving map from named native Cell/Link/Port/whole triadic events to this observer, rather than inferring native dynamics from a histogram.
