# D25/LIFT R49–R50 — exact rank-two observer window and finite Green two-endpoint bridge

2026-10-27 (Asia/Hong_Kong). Portable author research for TASK_RESEARCH logical lane chatgpt-research-hourly-enterprise-math-20260923, separate from CONTROL_PLANE_MAINTENANCE. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; parent D25/LIFT/JT2 OPEN. Frozen scientific source pin c47e13e4aba0e006366f989d6334d443f6333ae3, unchanged. Classification: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. No native CLAIM/open/checkpoint/Result/review.

## Typed original sources; R47/R48 are inputs, not recredited results

The unchanged original rational sources and signed difference are

\[
w_k=\frac{(6k+1)(2k)!(3k)!}{(k!)^5\,216^k},\quad
s_k=\frac{(8k+1)(4k)!}{(k!)^4\,2304^k},\quad d_k=w_k-s_k.
\]

Their separate exact transfers are

\[
a_k=\frac{(6k+7)(2k+1)(3k+1)(3k+2)}{36(6k+1)(k+1)^3},\quad
b_k=\frac{(8k+9)(2k+1)(4k+1)(4k+3)}{288(8k+1)(k+1)^3}.
\]

At rank k a freely variable labelled source state (W_k,S_k) transfers by W_{k+1}=a_k W_k and S_{k+1}=b_k S_k; its signed observer is d_k=W_k-S_k. This free-state observer audit is distinct from the one fixed factorial trajectory. Rank k is an auxiliary arithmetic index, not an X6 spatial coordinate.

Define

\[
P(x)=2688x^4+6160x^3+4456x^2+1166x+85,\qquad
a_k-b_k=\frac{(2k+1)P(k)}{288(k+1)^3(6k+1)(8k+1)}.
\]

## R49 — universal bounded observation window with exactly one target-class exceptional prime

Let p>=7 be prime, p≡1 (mod 6), and assume a_t and b_t, t=k,k+1,k+2, are all *well-defined units* in F_p (numerators and denominators nonzero). Set A_j=product_{t=k}^(k+j-1) a_t and B_j=product b_t, with A_0=B_0=1. The row from the j-th future signed observation is [A_j,-B_j], so the determinant with row [1,-1] at k is exactly Δ_j=A_j-B_j.

**Theorem.** If P(k)≠0 (mod p), the first two observations determine both source amplitudes. If P(k)=0 but P(k+1)≠0, the first three suffice, since Δ_1=0 and Δ_2=a_k(a_{k+1}-b_{k+1})≠0. The **only** unit-admissible failure of both tests in the target prime family is p=79411 and k≡5394 (mod p). There Δ_3=13918≠0 (mod p), so four observations are necessary and sufficient. For 0<=k<p this exceptional rank is exactly 5394. This is a claim about *linear reconstruction from signed observer data for every freely varying labelled state*, not an extra claim about hidden factorial initial conditions.

**Proof/certificate.** Integer shift and 8-by-8 Sylvester resultant give

\[
P(x+1)=2688x^4+16912x^3+39064x^2+39310x+14555,
\]
\[
\boxed{\operatorname{Res}(P(x),P(x+1))=
-48848218842909375002050560
=-2^{31}3^2\cdot5\cdot7^3\cdot79411\cdot18558017.}
\]

Both 79411 and 18558017 are primes, but 18558017≡5 (mod 6). Modulo 7 the polynomial gcd is 1; modulo 79411 the monic gcd is x-5394. Hence the stated target-class shared-root classification; the unit hypotheses exclude spurious vanishing of the 2k+1 numerator factor and allow exact modular reduction. At the exceptional rank,

\[
P(k)\equiv P(k+1)\equiv0,\quad P(k+2)\equiv22144\pmod{79411},
\]
\[
(a_k,a_{k+1},a_{k+2})=(63693,63793,2920),\qquad
(b_k,b_{k+1},b_{k+2})=(63693,63793,61628)\pmod{79411}.
\]

Therefore Δ_1=Δ_2=0 and

\[
\Delta_3\equiv63693\cdot63793(2920-61628)=13918\not\equiv0\pmod{79411}.
\]

Minimality has a concrete observer-fiber witness: states (W_k,S_k)=(1,0) and (0,-1) both yield signed observations (1,63693,24323) through k+2, but at k+3 their outputs differ: 29726 versus 15808 modulo 79411. Three observations fail future-state safety; four repair exactly this declared horizon. QED.

## R50 — exact finite Green two-endpoint identity and p-adic pole inheritance

Reuse R47's second-order recurrence in a source-faithful form:

\[
\alpha_k=a_k-b_k,\quad\beta_k=a_ka_{k+1}-b_kb_{k+1},\quad
\gamma_k=a_kb_k(a_{k+1}-b_{k+1})>0;
\]
\[
\alpha_kd_{k+2}-\beta_kd_{k+1}+\gamma_kd_k=0.
\]

For every finite rational signed observer c_0,...,c_{N-1}, define v_{-2}=v_{-1}=0 and uniquely solve the *adjoint*

\[
\boxed{\gamma_kv_k-\beta_{k-1}v_{k-1}+\alpha_{k-2}v_{k-2}=c_k\quad(0\le k<N),}
\]

omitting negative-index terms. Such v exists over Q because every γ_k is positive rational. Set

\[
C_{N+1}=\alpha_{N-1}v_{N-1},\quad
C_N=\alpha_{N-2}v_{N-2}-\beta_{N-1}v_{N-1}
\]

(negative-index terms omitted for N=1). Then the **complete two-boundary finite Green identity** is

\[
\boxed{\sum_{k=0}^{N-1}c_kd_k=-C_Nd_N-C_{N+1}d_{N+1}.}\tag{R50-G}
\]

**Proof.** With \(\mathcal B_k=\alpha_{k-1}v_{k-1}d_{k+1}+[\alpha_{k-2}v_{k-2}-\beta_{k-1}v_{k-1}]d_k\), direct expansion gives
\[
\mathcal B_{k+1}-\mathcal B_k
=v_k[\alpha_kd_{k+2}-\beta_kd_{k+1}+\gamma_kd_k]
-d_k[\gamma_kv_k-\beta_{k-1}v_{k-1}+\alpha_{k-2}v_{k-2}]
=-c_kd_k.
\]
Summing and using B_0=0, B_N=C_Nd_N+C_{N+1}d_{N+1} proves the identity. The rational adjoint has no automatic p-integrality. Both boundary coordinates and the division data must remain labelled. QED.

**Sharp mandatory pole for one low-rank port.** For every target prime p>=13, let H=floor((3p-1)/4), N=H+1. The two endpoint ranks N,N+1 are in the R48 high-high interval, hence v_p(d_N),v_p(d_{N+1})>=3. Put c_1=1 and other c_k=0. Then Σ c_k d_k=d_1=85/288 is a p-adic unit. If both C_N and C_{N+1} had valuations >=-2, the Green right side would be divisible by p, a contradiction. Thus

\[
\boxed{\min\{v_p(C_N),v_p(C_{N+1})\}\le-3.}
\]

This is a source/observer-specific endpoint pole theorem. It neither proves nor disproves the full W_p=S_p (mod p^3) target or a genuine nonlocal WZ cancellation.

**Executed exact author certificates.** Python stdlib 8x8 integer Bareiss determinant, factorization, finite-field polynomial gcd and exceptional transfer values: PASS. Separate stdlib Fraction Green-adjoint/reconstruction check for p=13,19,37,181,373: PASS, with tuples (v_p(d_N),v_p(d_{N+1}),v_p(C_N),v_p(C_{N+1})):

| p | N | exact tuple |
|---:|---:|---|
| 13 | 10 | (3,4,-3,-3) |
| 19 | 15 | (3,3,-3,-3) |
| 37 | 28 | (4,3,-3,-3) |
| 181 | 136 | (3,3,-3,-3) |
| 373 | 280 | (3,3,-3,-3) |

Proof is symbolic; this finite set of exact checks is a supporting author certificate, NOT a native p=373 H0/B0 run, independent mathematical review, or formalized proof.

## BRC / P000 / continuation

BRC method **COMPOSE_APPLIED** to the signed labelled two-source carrier, modular valuation and finite future observer. The R49 exceptional fiber demonstrates precise information loss under a too-coarse readout and provides the additional safe observation. R50 keeps *two* authentic finite endpoints. No positivity-only compression, hidden plane, X6-native transfer claim or new worldview axiom is introduced. The ACTIVE six-axis Heartbeat World and P000 remain fixed.

**New portable frontier:** R49 resultant classification plus exact p=79411 rank witness; R50 finite Green concomitant plus high-high pole implication. **Do not repeat:** R47 rank-two recurrence or R48 high-high valuations as new work; R45/R46 multiplier/affine obstructions; these current R49/R50 checked certificates absent changed assumptions.

**Next precise unit:** insert the original R23 low-half p²-divided W/S discrepancy into (R50-G) and R36 PF finite-boundary Green observer, while retaining R38–R42 high-rank valuations and the six fixed z=2 Hasse J/E channels, original finite endpoints and positive infinity. Seek a genuine unchanged-input source-labelled WZ cancellation or exact obstruction at p=13,19,181,373; do not use the arbitrary one-port cancellation as a global proof. H0/B0, [X]U mod p², Frobenius η/κ, native p=373 run and independent Driver review remain OPEN.

**Control/read-only limitation at this write:** separate gateway has research_authority_granted=false, executor_binding_configured=false, and an active-job quota block. This gateway's lack of permission is not evidence of no formal task or an outcome for an earlier unknown request. No Research-Activity semantic checkpoint or native Source checkpoint is claimed; existing predecessor mismatch stays with the dedicated controller issue https://github.com/awdawmip/enterprise-math/issues/1558. Preserve old session/request/staging until real same-conversation Source transition and winning claim.
