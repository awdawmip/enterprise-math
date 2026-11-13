# BRC N=4 / S23 — exact all-positive-integer-budget classification at s=1/8

Date: 2026-11-04. Status: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific input: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Scope: source-tagged classical Chernoff discrimination observer, not physical-native BRC-Shor dynamics. P000, joint provenance and the ten-label minimax mother question are unchanged.

## Exact model and result

Fix `s=1/8`, `h=1/42`, `v=2h=1/21`. Set `a=s(1+v)/2=11/168`, `b=s(1-v)/2=10/168`.
The source-labeled observation T has distributions `P_T=(a,1-s,b)`, `Q_T=(b,1-s,a)`. The coarsened B observation has `P_B=(a,1-a)`, `Q_B=(b,1-b)`.
Costs: `c_T=15/8`, `c_B=1`. Define `f_X(t)=-log sum_y P_X(y)^t Q_X(y)^(1-t)` and, for integer counts m,n>=0,

`C(m,n)=max_{0<=t<=1} [m f_T(t)+n f_B(t)]`,

with ONE shared Chernoff optimizer t. Feasibility is `15m+8n<=8K` for integer K>=1.

**Theorem (complete classification for ALL K>=1).** The UNIQUE maximizing allocation (m,n) is:

| K | m | n |
|---|---:|---:|
| 1..14 | 0 | K |
| 15..19 | 8 | K-15 |
| 20..29 | 0 | K |
| 30..39 | 16 | K-30 |
| 40..44 | 0 | K |
| every K>=45 | 8 floor(K/15) | K mod 15 |

In particular, after K=45 the optimizing allocation follows an exact period-15 block law indefinitely; the only intervening pure-B re-entry windows occur at K=20..29 and K=40..44. The extension beyond K=100 is newly established here.

## Reused exact analytic/arithmetic facts

Let `C_T=f_T(1/2)`, `C_B=max_t f_B(t)`, `E=C_T-(15/8) C_B` and `d=C_B-f_B(1/2)>=0`.
The independently stored *author-side* predecessor exact-Fraction certificate (see SOURCES.md and reused code) establishes simultaneously:

(A) `E>0`;
(B) `53 E < C_B/8`;
(C) `32 E -14d > 2772/10^12 >0`.

The predecessor bounds originate from exact rational enclosures of square roots, atanh, exp and -log and strong-curvature optimizer bounds. These are symbolic inequalities certified by integer/Fraction assertions; their proof, not a finite K scan, supplies the numerical premises. The present VERIFY.py actually executes that predecessor verifier before applying new exact assertions. All claims remain author-side and await independent review.

## NEW uniform elimination lemma (all budgets, all integer m)

Write `K=15L+r`, `L=floor(K/15)`, `0<=r<=14`. Let `A=(8L,r)`, a feasible allocation of exactly K cost units. For any other feasible (m,n), put `u=K-(15/8)m-n>=0`. The shared-exponent information inequality is

`C(m,n) <= m C_T+n C_B = K C_B+m E-u C_B`.

The valid center-exponent lower bound is

`C(A)>=8L C_T+r f_B(1/2)=K C_B+8L E-r d`.

Thus the *true optimized* information difference satisfies

`C(A)-C(m,n) >= (8L-m)E+u C_B-r d.`   (1)

Suppose 8 does not divide m. Since K,n are integers and the cost fraction has denominator 8, `u>=1/8`. If m<=8L, (1) is >= `C_B/8-14d`. If m>8L, feasibility implies

`m<=floor(8K/15)=8L+floor(8r/15)<=8L+7`.

In either case, (1) is at least `C_B/8-7E-14d`. By (B) and (C),

`C_B/8-7E-14d > 53E-7E-32E =14E>0`.  (2)

Therefore for EVERY positive integer K, EVERY feasible non-multiple-of-eight T count is strictly worse than A; (2) gives a uniform positive separation independent of K. This removes the predecessor's K<=100 restriction (m<=53).

## NEW eventual exact winner theorem

Only m divisible by 8 remains. Write m=8j. Necessarily 0<=j<=L. For each j, using every affordable B sample strictly improves C because B is nondegenerate and `f_B(t)>0` for `0<t<1`. Thus the best with m=8j uses `n=K-15j`.

As a function of real j,

`H(j)=max_t [j(8f_T(t)-15 f_B(t))+K f_B(t)]`

is convex (supremum of affine functions). Consequently every integer j in [0,L] has `H(j)<=max(H(0),H(L))`; if H(L)>H(0), strict convex interpolation gives `H(j)<H(L)` for all j<L.

For L>=4,

`H(L)-H(0) = C(8L,r)-K C_B >=8L E-r d >=32E-14d >2772/10^12>0.` (3)

Thus A=(8L,r) is the UNIQUE global optimum for every K>=60, with a strict endpoint gap >2772/10^12 against pure B and the strict uniform bound (2) against every non-8-divisible m. The proof holds simultaneously for infinitely many K without sampling K.

For K=1..30, the independently published predecessor proof at `9b2a85e7248c47c82d25e64d85ad872aa59e8c69` supplies the unique optimal allocations. For K=31..100, the predecessor at `37b9a50e9c04c661c730ef7c241d5a5de11318d9` supplies the unique allocations; only K=31..59 is needed to join the present K>=60 theorem. Together they yield the stated all-K table. QED.

## Verification and boundaries

`VERIFY.py` re-executes the prior exact rational enclosure verifier (source present in the same PR branch), then checks (A)-(C) and the *new* positive bound `C_B/8-7E-14d>0`, along with an integer-slack sanity check for K=60..200. All scientific enclosures and comparisons use `fractions.Fraction` and integer square roots. Floating values appear solely in the final human-readable report. The finite sanity cases do not prove the all-K statement: (1)-(3), convexity and the cited finite-prefix proofs do.

Reused predecessor verifier: `research_notes/brc_n4_s23_s18_residue_endpoint_k31_100_20261104_research1/VERIFY.py` at commit `37b9a50e9c04c661c730ef7c241d5a5de11318d9`, blob `43cfd010e5803a5359e7b727528002ea4f3f22ca`.
No new native CLAIM, Result, independent mathematical review, physical BRC-Shor experiment, or unconditional minimax decoder solution is asserted. The unrestricted ten-label decoder mother objective retains the previously recorded [1/2,2/3] open bound.
