# D25 onhour — Hensel-repaired middle/H2 dual cocycle (2026-11-03)

**Status:** AUTHOR-DERIVED / EXACT ALGEBRA PROVED / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. **Not** a native Source checkpoint or frozen Result.

**Role/provenance:** TASK_RESEARCH; own logical conversation chatgpt-research-onhour-enterprise-math-20260923, kept separate from maintenance chatgpt-hourly-enterprise-math-20260921 and another research lane chatgpt-research-hourly-enterprise-math-20260923. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7; frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3; P000 and ACTIVE Heartbeat World unchanged.

## Precise theorem: second-digit duality defect

For **every** prime p=6r+1 >=7, put n=3r=(p-1)/2 and

\[
b_k=\frac{(2k)!(3k)!}{(k!)^5 216^k},\qquad
R_j=\frac{b_{j+1}}{b_j}=\frac{(2j+1)(3j+1)(3j+2)}{36(j+1)^3}.
\]

Retain the original directed middle indices j=n-s, 0<=s<=r-1. Define p-adic units

\[
U_s=\prod_{t=1}^s R_{n-t}^{-1},\quad U_0=1,\qquad
f_s=\frac{(1)_s(5/6)_s(7/6)_s}{2^s(3/2)_s^3},\quad f_0=1.
\]

U_s is exactly the middle-band multiplier already proved in the other Research lane's 20261103_hourly20_d25_fermquotient_middle_second_digit.md; f_s is exactly the high H2 4F3 coefficient from 20261103_hourly20_d25_character_hypergeometric_h2_ode.md. Both earlier results are *consumed*, not re-claimed.

Define in F_p

\[
c_t=\frac1{2t}+\frac3{6t-1}+\frac3{6t+1}-\frac3{2t-1},\quad
E_s=\sum_{t=1}^s c_t,\quad E_0=0.
\]

All denominators are p-units for 1<=t<=r-1. The **new complete two-digit relation** is

\[
\boxed{J_s:=(2s+1)^3 U_sf_s \equiv 1+pE_s\pmod{p^2}.}\tag{D1}
\]

The *repaired dual* \(V_s=(2s+1)^3f_s(1-pE_s)\) consequently satisfies

\[
\boxed{U_sV_s\equiv1\pmod{p^2},}\tag{D2}
\]
\[
\boxed{\binom{U_s}{V_s}\equiv
\begin{pmatrix}R_{n-s}^{-1}&0\\0&R_{n-s}\end{pmatrix}
\binom{U_{s-1}}{V_{s-1}}\pmod{p^2}}\tag{D3}
\]

for 1<=s<=r-1. Thus the **p-adically corrected transfer** has determinant one modulo p²; the explicit correction E_s is unique with E_0=0 and E_s-E_(s-1)=c_s. Equivalently,

\[
\boxed{f_s\equiv\frac{1+pE_s}{(2s+1)^3U_s}\pmod{p^2}.}\tag{D4}
\]

**Proof.** With n=(p-1)/2 the *exact* original middle ratio is

\[
R_{n-t}=\frac{(p-2t)((3p-6t)^2-1)}{18(p-2t+1)^3}.
\]

Put \(R_t^{(0)}=t(36t^2-1)/[9(2t-1)^3]\). The independent hypergeometric carrier has exact successive ratio

\[
f_t/f_{t-1}=t(36t^2-1)/[9(2t+1)^3].
\]

Therefore \(J_t/J_{t-1}=R_t^{(0)}/R_{n-t}\), exactly over the p-local rational ring, and direct factorization yields

\[
\frac{R_{n-t}}{R_t^{(0)}}
=\frac{(1-p/(2t))(1-3p/(6t-1))(1-3p/(6t+1))}
{(1-p/(2t-1))^3}
\equiv1-pc_t\pmod{p^2}.
\]

Hence \(J_t/J_{t-1}\equiv1+pc_t\), and multiplying the finite links proves D1. D2 follows by \( (1+pE_s)(1-pE_s)=1\pmod{p^2}\). For D3,

\[
V_t/V_{t-1}
=R_t^{(0)}(1-p(E_t-E_{t-1}))
\equiv R_t^{(0)}(1-pc_t)\equiv R_{n-t}\pmod{p^2}.
\]

The U ratio is \(R_{n-t}^{-1}\), and D4 is D1 solved using p-units. QED.

## Direct D25 interface and source scope

Consume the original one-sided formula, with chi=(6/p), L_p=b_n/p, B_low=sum_(k=0)^(2r)(6k+1)b_k:

\[
W_{p-1}\equiv B_\mathrm{low}+
pL_p\sum_{s=0}^{r-1}(3p-2-6s)U_s+
\frac{p^2\chi}{9}\sum_{s=0}^{r-1}(6s+4)f_s
\pmod{p^3}.
\]

D1–D4 connect the original middle multiplier and the *separately sourced* fourth-order H2 carrier, preserving every index, p-valuation, sign, and directed cutoff. The corrected V_s is a mathematical mod-p² carrier: it does **not** assert that the original high factorial coefficient b_(n+1+s)/p² equals the corrected quantity modulo p². At the required mod-p high horizon, the established original high relation is retained. The mother equality W_(p-1)=p (mod p³) for primes p mod24 =13 or19 remains **unproved**.

**Actual execution:** Exact Python-standard-library modular checker ran for **all 148 primes 7<=p<=2000 with p=1 (mod6)**, covering **22,952** (p,s) pairs. D1, D2, both legs of D3, and D4 mod p passed. Original integer-binomial values independently checked U_s at p=7,13,19,37,43,373. Examples: (p,s,E_s,J_s)=(13,1,8,105), (19,2,10,191), (37,5,10,371), (373,61,82,30587); all repaired U_s V_s=1 mod p². At p=373 the nontrivial second digit is 30587=1+373*82 (mod139129). Local original checker/result/console are preserved as one evidence bundle: d25_onhour_middle_h2_hensel_dual_defect_20261103_evidence.zip, 2026-11-03.

**BRC COMPOSE_APPLIED:** two previously independent source carriers joined through the exact bilinear observer J_s, with typed finite additive defect E_s and unit-preserving second-digit repair. Future mod-p² first-order transfer retains this index-level correction; no X6 native spatial theorem or H0/B0 evaluation is asserted.

## Continuation / recovery

Mother: frozen Δ_p≡R_p mod p, equivalently W_(p-1)≡p mod p³ for prime p mod24 ∈{13,19}. Immutable scientific pin: c47e13e4aba0e006366f989d6334d443f6333ae3. Completed **this author unit**: D1–D4 with exact finite checks, source-separated. Do-not-repeat: accepted D24, previously proved full one-sided Laurent formula, earlier H2 4F3/ODE and Fermat boundary, 2304 Q4 tail, Green scalar binding. **Next precise action:** use p-dependent repaired dual to build a signed finite WZ/Green adjoint linking B_low second carry, middle U_s, high H2 f_s with original 2r/3r/4r terminal ports; first check edge residuals at 13,19,373, then analyze general p. A candidate low-degree Gosper antidifference for the isolated (6s+4)f_s is not presently established; no universal obstruction is inferred.

Native benchmark #1559 remains OPEN/PENDING_OWNER: p=373 original H0/B0 [X]U mod139129, module rank, actual semilinear Frobenius direction, signed Green/Hesse observer and independent verification still required. Research Source write authority remains unverified in this run. Historical request research-onhour-20261031-0205-dispatch-r15 at bridge #6633 was not replayed (previous final inner FAILED, UPSTREAM_CODE_REVIEW_REQUIRED). Own native session/claim/run **not verified**; no official checkpoint/Result/admission. This GitHub document is author-side source evidence only. No scheduler/notification changes.
