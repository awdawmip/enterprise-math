# D25 — Complete low/middle/H2 four-source second-digit criterion

**Date:** 2026-11-03 (+08). **Status:** AUTHOR-DERIVED / EXACT SCOPED ALGEBRA PROVED / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. TASK_RESEARCH logical lane chatgpt-research-onhour-enterprise-math-20260923; maintenance lane chatgpt-hourly-enterprise-math-20260921 and other hourly Research lane chatgpt-research-hourly-enterprise-math-20260923 have different identities. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3.

## Reuse and objective

Consume (without re-proving) the original 216 band theorem, p² Fermat-quotient middle boundary from the other hourly Research lane, high H2 terminating 4F3, the exact scalar Clausen/R bridge, and onhour's just-published middle/H2 Hensel defect at 20261103_onhour_d25_middle_h2_hensel_dual_defect.md. **New unit:** express *all* original 216 coefficient sources through an explicit terminating low Hensel double jet, middle signed Hensel repair, and high H2 hypergeometric observation. This turns the outstanding mother congruence into one exact four-source signed finite certificate.

For **every** prime p=6r+1 >=7, set n=3r, chi=(6/p), and

\[
b_k=\frac{(2k)!(3k)!}{(k!)^5 216^k},\qquad W_{p-1}=\sum_{k=0}^{p-1}(6k+1)b_k.
\]

For 0<=k<=2r define

\[
T_k=\frac{(-3r)_k(-2r)_k(-4r)_k}{2^k(k!)^3},
\]

\[
h_k=\sum_{i=0}^{k-1}\left[\frac1{2(i-3r)}+\frac1{3(i-2r)}+\frac2{3(i-4r)}\right],
\quad
t_k=\sum_{i=0}^{k-1}\left[\frac1{4(i-3r)^2}+\frac1{9(i-2r)^2}+\frac4{9(i-4r)^2}\right].
\]

All these denominators are p-units. Empty sums are zero. Let

\[
A=\sum_{k=0}^{2r}(6k+1)T_k,\quad
B=\sum_{k=0}^{2r}(6k+1)T_kh_k,\quad
C=\frac12\sum_{k=0}^{2r}(6k+1)T_k(h_k^2-t_k).
\]

Define the p-independent middle baseline and the **previously proved** defect

\[
u_s=\prod_{t=1}^{s}\frac{9(2t-1)^3}{t(36t^2-1)},\quad u_0=1,\quad
E_s=\sum_{t=1}^{s}\left[\frac1{2t}+\frac3{6t-1}+\frac3{6t+1}-\frac3{2t-1}\right].
\]

Set

\[
M_0=\sum_{s=0}^{r-1}(-2-6s)u_s,\quad
M_1=\sum_{s=0}^{r-1}[3+(-2-6s)E_s]u_s,
\]

\[
f_s=\frac{(1)_s(5/6)_s(7/6)_s}{2^s(3/2)_s^3},\quad
H=\sum_{s=0}^{r-1}(6s+4)f_s,\quad
\varepsilon=3+\frac{q_p(2)-3q_p(3)}2\pmod p,
\]
where \(q_p(a)=(a^{p-1}-1)/p\pmod p\).

## Theorem 1 — full original 216 mod p³

For every p=6r+1 >=7 prime,

\[
\boxed{
W_{p-1}\equiv A+p(B-2\chi M_0)
+p^2\left[C-2\chi(M_1+\varepsilon M_0)+\frac\chi9H\right]\pmod{p^3}.}\tag{F1}
\]

**Complete proof.** The exact shifted-parameter identities

\[
\tfrac12=-3r+\tfrac p2,\quad
\tfrac13=-2r+\tfrac p3,\quad
\tfrac23=-4r+\tfrac{2p}3
\]

and the original 216 hypergeometric representation give, for each k<=2r, by multiplying finite p-unit rising-factorial terms to second order,

\[
\boxed{b_k\equiv T_k\left[1+ph_k+\tfrac{p^2}{2}(h_k^2-t_k)\right]\pmod{p^3}.}\tag{F2}
\]

Summing with the *original* signed weights gives exactly A+pB+p²C. The exact original middle ratio b_(n-s)/b_n=U_s and the Hensel dual theorem give U_s=u_s(1+pE_s) mod p². The previously proved p² boundary is b_n/p=-2chi(1+p epsilon) mod p². Its signed weight is 6(n-s)+1=3p-2-6s; hence the middle band contributes -2chi p M0-2chi p²(M1+epsilon M0) mod p³. The previously proved original H2 high-band formula contributes p² chi H/9 modulo p³. The final original k>=4r+1 band has p-valuation >=3. Addition of these disjoint original sources proves F1, including all signs and endpoints. QED.

## Theorem 2 — frozen D25 scalar is an exact four-source residue

For the **frozen target classes** p≡13,19 (mod24), consume the accepted first-digit assertion W_(p-1)≡p mod p² and define the p-integral quotient

\[
D=\frac{A+p(B-2\chi M_0)-p}{p^2}\pmod p.\tag{F3}
\]

The numerator is divisible by p² by F1 and the accepted first digit. Exact p-local rational arithmetic is used *before division*, rather than rounding the pieces at insufficient precision. The earlier proven frozen signed Clausen map gives

\[
\boxed{\Delta_p-R_p\equiv D+C-2\chi(M_1+\varepsilon M_0)+\frac\chi9H\pmod p.}\tag{F4}
\]

Proof: subtract p from F1, divide by p², and apply the proven equality (W_(p-1)-p)/p²=Delta_p-R_p mod p. QED.

Thus the **remaining theorem** is that the four-port signed right side of F4 vanishes for every frozen target prime. No zero claim is made from the present algebra alone.

## Executed source-preserving exact computation

A Python standard-library exact checker generated original b_k by the unshifted ratio modulo p³; **independently** generated the low T_k,h_k,t_k, middle u_s,E_s and high f_s. It verified F2 coefficient-by-coefficient and F1/F3/F4 on **all 148 primes 7<=p<=2000, p≡1 (mod6)**. At p=7,13,19,37,43,373 it independently checked the *full original integer-binomial sum*. All assertions passed. Signed residue witness table:

| p | D | C | middle -2chi(M1+eps M0) | high chi H/9 | total mod p |
|--:|--:|--:|--:|--:|--:|
| 7 | 0 | 4 | 5 | 5 | 0 |
| 13 | 3 | 5 | 8 | 10 | 0 |
| 19 | 18 | 1 | 10 | 9 | 0 |
| 37 | 13 | 19 | 22 | 20 | 0 |
| 43 | 3 | 0 | 5 | 35 | 0 |
| 373 | 204 | 82 | 194 | 266 | 0 |

At p=373 these four sources sum to 746=2×373. The full executed program, output JSON, and terminal text are preserved in the same 2026-11-03 evidence bundle d25_onhour_second_digit_complete_hensel_four_source_20261103.zip. The algebraic formula is valid for all stated primes; the finite checks are separate evidence.

**BRC COMPOSE_APPLIED:** raw original low integer-coefficient indices 0..2r, middle n-s with p² unit, and high n+1+s with p² valuation remain independent ports. Hensel first/second logarithmic jets (B,C), signed middle defect E, Fermat quotient epsilon, and high H are retained in a typed p-adic carrier. The scalar four-port sum is the declared final observer, not automatic collapse of distinct sources. P000/ACTIVE Heartbeat World unaffected.

## Highest frontier and continuation

Mother objective frozen Delta_p=R_p mod p on primes p≡13,19 mod24, equivalent to original W_(p-1)=p mod p³. **Completed this author unit:** F1/F2 all primes 6r+1, F3/F4 under frozen first-digit hypothesis, exact checks 148 primes. **Unfinished:** prove the signed four-source F4 cancellation universally; execute native p=373 original-class H0/B0 divided-power benchmark (#1559) including [X]U mod139129, rank, real semilinear Frobenius, signed observer and independent reproduction. **Next exact action:** construct and test a terminating p-dependent signed Green/WZ-adjoint for the four-port F4, including actual 2r/3r/4r edge residues at 13,19,373. Do not redo D24/2304 tail/R binding/other lane Fermat unit/H2 ODE/this lane Laurent and dual.

Historical original dispatch request research-onhour-20261031-0205-dispatch-r15 (#6633) was **not** replayed; prior native failure UPSTREAM_CODE_REVIEW_REQUIRED and missing Research write authorization remain subject to original Source status. Own native session/claim/run **not verified**; no native Source checkpoint, Result, review or admission. Source registration REGISTER_PENDING. This is **author-side published research evidence**, not canonical role-bound task execution. Existing scheduled task and notifications unchanged.
