# D25 — p² Fermat-quotient boundary and full original 216 middle/high reduction

Date: 2026-11-03 Asia/Shanghai. Status: AUTHOR-DERIVED / ALGEBRAICALLY-PROVED / FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. Logical TASK_RESEARCH lane: chatgpt-research-hourly-enterprise-math-20260923. Parent objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, immutable scientific input pin c47e13e4aba0e006366f989d6334d443f6333ae3. Portable author evidence, not a native checkpoint or Result.

## Theorem A: full second p-adic digit of the original 216 boundary

For every prime p=6r+1>=7, put n=3r=(p-1)/2, chi=(6/p) in {+1,-1}, and

$$
b_k=\frac{(2k)!(3k)!}{(k!)^5 216^k},
\quad L_p=\frac{b_n}p,
\quad q_p(a)=\frac{a^{p-1}-1}{p}\pmod p,
\quad H_n=\sum_{j=1}^n\frac1j\pmod p.
$$

Then in Z/p²Z:

$$
\boxed{L_p\equiv-2\chi\left[1+p\varepsilon_p\right]\pmod{p^2},\qquad
\varepsilon_p\equiv3-H_n-\frac{q_p(216)}2
\equiv3+\frac{q_p(2)-3q_p(3)}2\pmod p.}\tag{A}
$$

**Exact proof.** Since 3n=p+n-1, the original factorials give

$$
\frac{b_n}p=
\frac{((p-1)!)^2}{n(n!)^4 216^n}
\prod_{j=1}^{n-1}\left(1+\frac pj\right).
$$

Let w_p=((p-1)!+1)/p be the Wilson quotient. The identity

$$
(p-1)!=(-1)^n(n!)^2\prod_{j=1}^n(1-p/j)
$$

gives (n!)²=(-1)^{n+1}[1+p(H_n-w_p)] modulo p². Thus

$$
\frac{((p-1)!)^2}{(n!)^4}\equiv
\frac{1-2pw_p}{1+2p(H_n-w_p)}
\equiv1-2pH_n\pmod{p^2}.
$$

The intermediate Wilson quotient cancels. Also 1/n=-2(1+p) modulo p²; the product equals 1+pH_(n-1), with H_(n-1)=H_n+2 modulo p. Multiplying gives the factor -2[1+p(3-H_n)]. Euler's criterion and 216^(p-1)=1+p q_p(216) imply

$$
216^{-n}\equiv\chi[1-pq_p(216)/2]\pmod{p^2}.
$$

Therefore the first formula holds. Use the half-range harmonic identity H_n=-2q_p(2) modulo p, and the exact Fermat-quotient multiplicative law q_p(216)=3q_p(2)+3q_p(3) modulo p, to obtain the second formula. QED.

## Theorem B: exact directed middle lift and full W reduction mod p³

For 2r+1<=j<=n define the original coefficient ratio and its directed inverse product

$$
R_m=\frac{(2m+1)(3m+1)(3m+2)}{36(m+1)^3}\in\mathbb Z_p^\times,\qquad
P_j=\prod_{m=j}^{n-1}R_m^{-1}
$$

(empty product one). Then every middle-band original coefficient obeys

$$
\boxed{b_j/p\equiv L_pP_j\pmod{p^2}.}\tag{B1}
$$

Recall the earlier independently verified H2 fourth-order polynomial carrier, sourced in 20261103_hourly20_d25_character_hypergeometric_h2_ode.md:

$$
F_r(x)=\sum_{s=0}^{r-1}\frac{(1)_s(5/6)_s(7/6)_s}{(3/2)_s^3}x^s,\qquad \theta=x\frac d{dx},
$$

$$
H_2(p)/p^2\equiv\frac{\chi}{9}(6\theta+4)F_r(1/2)\pmod p,\quad H_2(p)=\sum_{k=3r+1}^{4r}(6k+1)b_k.
$$

The complete original sum, with all signs and boundaries, now satisfies

$$
\boxed{
\begin{aligned}
W_{p-1}:=\sum_{k=0}^{p-1}(6k+1)b_k
\equiv{}&
\sum_{k=0}^{2r}(6k+1)b_k\\
&+pL_p\sum_{j=2r+1}^{3r}(6j+1)P_j\\
&+p^2\frac{\chi}{9}[(6\theta+4)F_r(x)]_{x=1/2}
\pmod{p^3}.
\end{aligned}}\tag{B2}
$$

Here L_p is the explicitly computed mod-p² unit from (A), while P_j is evaluated mod p². This strictly removes the middle/high factorial evaluations; the low original factorial source, p-adic lifts, signed observers and all original cutoff ports are retained.

**Proof.** The original recurrence b_(m+1)/b_m=R_m is exact and R_m is a unit for 2r+1<=m<n. Telescoping from n down to j proves B1. The valuation strips for k=0..p-1 are [0,2r], [2r+1,3r] (valuation one), [3r+1,4r] (valuation two), and [4r+1,p-1] (valuation >=3). The latter vanishes modulo p³. Sum B1 over the middle strip and the previously proved H2 formula over the high strip to obtain B2. QED.

For p mod24 in {13,19}, the frozen first-digit result says W_(p-1)-p is divisible by p². The mother target is exactly that the right-hand side B2 minus p vanishes modulo p³. This final cancellation remains open.

## Actually executed exact verification

The executed original factorial/p-free modulo-p² and independent integer-binomial modulo-p³ test is at research_notes/portable_direct/d25_fermquotient_middle_lift_checker_20261103.py (Git blob SHA-1 4e0e2d2f26479ca26c87be52e5eede2fe9b2bf6d), calling the earlier first checker research_notes/portable_direct/d25_h2_quadratic_character_hypergeometric_20261103.py (blob 5cca21c545a8b4da81542e793c5b6cfb6d1ea4b5). Standard-library exact integer computation actually passed all 148 primes p<=2000, p=1 mod6, checking formula A and each middle-index unit B1. A second full original binomial sum independently confirmed B2 for p=7,13,19,37,43,373.

| p | chi | L mod p² | epsilon mod p | signed middle/p mod p² | H2/p² mod p | W mod p³ |
|---:|---:|---:|---:|---:|---:|---:|
| 7 | -1 | 30 | 2 | 31 | 5 | 7 |
| 13 | -1 | 145 | 12 | 149 | 10 | 13 |
| 19 | +1 | 131 | 6 | 254 | 9 | 19 |
| 37 | -1 | 1001 | 32 | 608 | 20 | 37 |
| 43 | +1 | 772 | 34 | 960 | 35 | 43 |
| 373 | -1 | 19771 | 213 | 103721 | 266 | 373 |

This is finite exact evidence, distinct from the all-prime algebraic proof. Original H0/B0, semilinear Frobenius, independent mathematics review and Lean formalization were not executed.

## BRC audit and next executable scientific unit

The original integer factorial coefficients, signed indices, valuation bands, character and Fermat-quotient data, middle transfer, full low block and high fourth-order source polynomial are the retained carrier. B1/B2 are exact observer-preserving transformations for the original W modulo p³, with full directed endpoint and signed carry. A scalar high-band summary by itself is not claimed sufficient for later derivative/Frobenius or higher p-adic readout.

Next derive a truly p-dependent signed Green/WZ adjoint coupling the low plus explicit middle p² carry to the negative of chi*(6theta+4)F_r(1/2)/9. Retain 2r,3r,4r endpoints and test p=13,19,373 before any universal claim. The frozen W_(p-1)=p (mod p³) for p mod24 13,19 remains open.

## Native control

On 2026-11-03, authenticated Gateway 0.6.11 returned UPSTREAM_CODE_REVIEW_REQUIRED, research_authority_granted=false, executor_binding_configured=false, control active quota 5/5. Own prior read-only recovery #6637 had no local open run or pending operation and preserved historical neutral staging; continuation #6638 definitively failed. Source support #1558 remains open. This portable proof neither obtains a new Researcher session nor performs CLAIM/OPEN/Source checkpoint/freeze/review/admission. Stable Research logical conversation, P000, active Heartbeat world, frozen science and existing scheduler settings are unchanged.
