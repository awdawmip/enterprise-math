# D25/LIFT GH-44–GH-46: inverse-Gauss symmetric-square boundary and first omitted Clausen coefficient

Date: 2026-10-28. TASK_RESEARCH **author derivation and exact computation only**; UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. This is not a native Task CLAIM, OPEN, Source checkpoint, Result, independent mathematical review or proof of the GH-3 target congruence.

Parent: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION (OPEN); Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Own research logical lane: chatgpt-research-hourly-enterprise-math-20260923, never the control-maintenance conversation. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 is unchanged. P000's ACTIVE X6, discrete six axes, three-dimensional slice and the original W/S Hasse sources remain separate from the auxiliary scalar arithmetic.

## Exact prior inputs and notation

For p=4d+3 prime, p>=7, work over F_p or Z_(p), as stated. For the exact rational identity in GH-46 allow any integer d>=1, with p=4d+3 merely a parameter. Write D=u d/du and define the GH-38–GH-43 sequences by

\[
a_0=c_0=\beta_0=1,\quad
\frac{a_{r+1}}{a_r}=\frac{(8r+1)^2}{16(4r+3)(r+1)},\qquad
\frac{c_{r+1}}{c_r}=\frac{(4r+1)^3}{(4r+2)(4r+3)(4r+4)},
\]
\[
\frac{\beta_{r+1}}{\beta_r}=
\frac{16(r+1)(4r+3)}{(8r+13)^2}.
\]

Set B_d(z)=sum_{r=0}^d a_r z^r, V_d(u)=sum_{r=0}^d beta_r u^r and v_n=[u^n]V_d(u)^2, extended by zero for n outside [0,2d]. Original GH-39 high coefficients are b_n=[z^n]B_d(z)^2 with the ordered source labels (i,j) retained. The GH-40 inverse-point observer is

\[
W_{d-1}(u)=\sum_{n=0}^{d-1}(8n+11)v_nu^n,\qquad u_*=1/9.
\]

All modular denominators required below are p-units in the stated prime class. These observers are not the original Hasse B0, original W/S, six ports, native X6 cell state or Frobenius eta/kappa.

## GH-44 — exact inhomogeneous symmetric square and linear inverse-moment algorithm

GH-41 proved the *rational affine* equation

\[
\mathcal A_0V_d=K_0+Eu^{d+1},\quad
\mathcal A_0=u(D+3/4)(D+1)-(D+5/8)^2,\quad
K_0=-25/64,\ E=p(d+1)\beta_d/4.
\]

Define S_0=u(D+2)(D+3/2)(D+7/4)-(D+5/4)^3. Directly differentiating V_d^2 and using the affine equation to eliminate second and third derivatives yields, **over Q[u] including the upper boundary**,

\[
\boxed{\mathcal S_0(V_d^2)=
-\frac{25}{64}(6D+5)V_d+
\frac{p(d+1)}4\beta_du^{d+1}(6D+2d+7)V_d.}\tag{44.1}
\]

A useful direct coefficient-check proof is to expand both sides, insert the exact beta recurrence above, and check every degree n=0,...,2d+1; the boundary factor p(d+1)beta_d/4 is essential. Modulo p the boundary term vanishes but the affine source remains, giving

\[
\boxed{(4n+5)^3v_n
=8(n+1)(2n+1)(4n+3)v_{n-1}
+25(6n+5)\beta_n\pmod p,}\tag{44.2}
\]

where v_{-1}=0, beta_n=0 for n>d. For n<=2d, 4n+5 is invertible modulo p: the possible multiples p or 2p give nonintegral n, and 3p corresponds to n>2d. Thus (44.2), together with the first-order beta recurrence, evaluates all v_n and W_{d-1}(1/9) using O(d) field operations rather than an ordered pair convolution. This is a distinct evaluator of the same existing observer, not a vanishing theorem.

At n=d, 4d+3=p cancels the preceding coefficient, and 4d+5=2, 6d+5=1/2 in F_p. Consequently

\[
\boxed{v_d=\frac{25}{16}\beta_d\pmod p.}\tag{44.3}
\]

For 1<=s<=d, beta_{d+s}=0, so the upper recurrence is homogeneous and telescopes to

\[
\boxed{v_{d+s}=\frac{25}{16}\beta_d
\frac{(1)_s(3/4)_s(5/4)_s}{(3/2)_s^3}\pmod p.}\tag{44.4}
\]

The terminal n=2d+1 coefficient vanishes as required because 2(2d+1)+1=p.

## GH-45 — terminating deformed Gauss symmetric square and a second-digit central law

Use GH-43's *actual reversed forward polynomial*

\[
\Gamma_d(u)=u^d B_d(u^{-1})/a_d=\sum_{r=0}^d\gamma_ru^r,\qquad
\frac{\gamma_{r+1}}{\gamma_r}=
\frac{(r+1-p/4)(r+3/4-p/4)}{(r+13/8-p/4)^2}.
\]

Put h=p/4, K_h=-(5/8-h)^2 and
\(\mathcal A_h=u(D+1-h)(D+3/4-h)-(D+5/8-h)^2\).
The coefficient recurrence cancels all positive powers through d; the degree d+1 coefficient is killed by d+3/4-h=0. The constant equals K_h. Therefore

\[
\boxed{\mathcal A_h\Gamma_d=K_h\quad\hbox{exactly in Q[u].}}\tag{45.1}
\]

The general affine symmetric-square Leibniz identity is

\[
\mathcal S_h(G^2)=6K(u)DG+[2DK(u)+(5-8h)K(u)]G,\qquad
\mathcal A_hG=K(u),
\]
with
\(\mathcal S_h=u(D+2-2h)(D+3/2-2h)(D+7/4-2h)-(D+5/4-2h)^3\).
It follows by expanding the three derivatives of G^2 and substituting the affine equation; it is an algebraic identity, valid without assuming a homogeneous second-order solution. For the constant source (45.1),

\[
\boxed{\mathcal S_h(\Gamma_d^2)=K_h(6D+5-8h)\Gamma_d.}\tag{45.2}
\]

Let g_n=[u^n]Gamma_d^2. Equating the coefficient of degree n yields

\[
(n+1-2h)(n+1/2-2h)(n+3/4-2h)g_{n-1}
-(n+5/4-2h)^3g_n
=-(5/8-h)^2(6n+5-8h)\gamma_n.
\]

Set n=d and substitute p=4d+3; after clearing powers of 2 this gives the **exact rational boundary law**

\[
\boxed{(2-p)^3g_d
=p(1-p^2)g_{d-1}
+\frac{(5-2p)^2(1-p)}2\gamma_d.}\tag{45.3}
\]

Reduction in Z_(p)/p² gives

\[
\boxed{g_d\equiv\frac{25}{16}\gamma_d+
p\left(\frac18g_{d-1}-\frac{15}{32}\gamma_d\right)\pmod{p^2}.}\tag{45.4}
\]

For the GH-42 exact reverse first-jet correction write
\(H_r=\sum_{j<r}(4/(8j+13)-1/(4j+4)-1/(4j+3))\bmod p\),
\(\gamma_r=\beta_r(1+pH_r)\bmod p^2\),
and retain the **first omitted** central ordered-pair jet
\(j_d=\sum_{i+j=d}\beta_i\beta_j(H_i+H_j)\bmod p\).
Then

\[
\boxed{\frac{v_d-25\beta_d/16}{p}+j_d
\equiv\frac{25}{16}\beta_dH_d+\frac18v_{d-1}
-\frac{15}{32}\beta_d\pmod p.}\tag{45.5}
\]

The quotient is in the p-local rationals, well-defined by (44.3). It cannot be formed by arbitrary residue division. It preserves the signed, ordered and valuation-one boundary contribution, without upgrading GH-42's truncated moment or the native Hasse ports.

## GH-46 — exact first omitted *forward* Clausen coefficient, no primality required

The rational classical Clausen identity used in GH-39 gives [z^d]B_d(z)^2=c_d. Since Gamma_d is the exact reversed B_d, \(\gamma_d=1/a_d\) and

\[
g_d=c_d/a_d^2,\qquad
g_{d-1}=b_{d+1}/a_d^2,\qquad
b_{d+1}=\sum_{\substack{i+j=d+1\\0\le i,j\le d}}a_ia_j.
\]

Substituting these exact rational equations into (45.3) and multiplying by a_d² proves for **every integer d>=1** (including composite p=4d+3)

\[
\boxed{(2-p)^3c_d=p(1-p^2)b_{d+1}+
\frac{(5-2p)^2(1-p)}2 a_d,\quad p=4d+3.}\tag{46.1}
\]

Unlike the simple finite truncation at degree d, this records the very next omitted ordered-pair coefficient and its exact resonance with the last original rank. This is not an independent special-value certificate and does not prove T_d(9)=0.

## Executed exact evidence and continuation

A Python standard-library checker ran exact modular arithmetic on **all 154 primes** 7<=p<2000, p=3 mod4, checking (44.2) coefficientwise including terminal rank, central and upper coefficients, O(d) W algorithm versus independent convolution, shifted (45.2) modulo p², (45.3)–(45.5), original/reversed coefficient agreement and (46.1) modulo p². An independent Fraction checker verified the *full rational* GH-44/GH-45 symmetric-square operator identities and GH-46 for **all d=1,...,12**, including composite parameters. The finite check is not universal theorem admission. Selected (p; beta_d, v_d mod p; g_d, b_{d+1} mod p²; W(1/9) mod p) samples: 19:(17,4,194,280,5), 43:(40,41,213,208,11), 67:(36,6,2686,2202,6).

BRC COMPOSE_APPLIED: retain index/source (i,j), exact signed F_p and rational weights, rank threshold d, finite precision, H_r and j_d, forward/reverse maps, and future differentiated observers. A scalar W or total v_d does not retain the original independent W/S and six Hasse ports.

The source-bound new units are GH-44, GH-45, GH-46 with hypotheses and boundaries above. Next precise open unit: use the inhomogeneous square equation to derive an **independent** CM/Frobenius, character-sum or nonlocal WZ special-value certificate for W_{d-1}(1/9) relative to B_d(9)Q_d(9), not another T=T convolution rewriting. GH-3 all-prime vanishing, p² next-digit original W/S, R23/R36, [X]U mod p², eta/kappa, native p=373 and independent Driver review remain unresolved. Source-verified CLAIM/OPEN/checkpoint and activity registration await a valid native research execution authority; Git evidence is not canonical Source admission.
