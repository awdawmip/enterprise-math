# D25 — Source-faithful Cauchy carry: exact forced Picard–Fuchs system and Gauss endpoint certificate

Date: 2026-11-02. Research lane: chatgpt-research-hourly-enterprise-math-20260923. Classification: AUTHOR-DERIVED / EXACT-PROVED (U1,U2) / FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.

**Task:** RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; original frozen scientific input pin c47e13e4aba0e006366f989d6334d443f6333ae3 is unchanged. Mother goal: original signed Delta_p-R_p=0 (mod p), for all primes p=13 or 19 (mod 24). This is author-side portable evidence, *not* native Source checkpoint/Result or H0/B0.

## U1 — Exact forced Picard–Fuchs equations, with ordered Cauchy source

All equations in this section are identities in Q[[z]]. For m>=0 define

- a_m=(1/2)_m(1/3)_m(2/3)_m/(m!)^3;
- b_s=(1/2)_s/(2^s s!)=binom(2s,s)/8^s; u_s=-1/(4s b_s) for s>=1;
- c_m=(1/3)_m(2/3)_m/(m!)^2;
- U_0=V_0=0, U_m=sum_{s=1}^m u_s, V_m=sum_{s=1}^m (m-s)u_s;
- K_0(z)=sum_{m>=0}a_m U_m z^m, K_1(z)=sum_{m>=0}a_m V_m z^m, D(z)=sum_{m>=0}c_m (2z)^m.

Set theta=z d/dz, L3=theta^3-z(theta+1/2)(theta+1/3)(theta+2/3), and L2=theta^2-2z(theta+1/3)(theta+2/3).

**Theorem U1.** All three equations hold *coefficientwise*:

\[
\boxed{\mathcal L_2D=0,\quad \mathcal L_3K_0=-\tfrac14\theta^2D,\quad
\mathcal L_3K_1=z(\theta+\tfrac12)(\theta+\tfrac13)(\theta+\tfrac23)K_0.}
\]

Proof. Direct hypergeometric ratios give
m^3 a_m=(m-1/2)(m-1/3)(m-2/3)a_{m-1}
and a_m u_m=-2^m c_m/(4m).
Thus [z^m] L3K0=m^3a_m(U_m-U_{m-1})=-m^2 2^m c_m/4.
Because V_m-V_{m-1}=U_{m-1}, the coefficient of L3K1 is m^3a_m U_{m-1}, precisely that of z(theta+1/2)(theta+1/3)(theta+2/3)K0. The c_m ratio proves L2D=0. The constant coefficients agree. QED.

For every prime p=6r+1>=7, truncate at m=2r. The coefficients are p-integral, b_s units for 1<=s<=2r. At the single potential operator boundary degree 2r+1, the factor (2r+1/3)=p/3 annihilates the boundary mod p. Hence the three *polynomial* equations remain valid mod p, including their cutoff edge. These K_i are precisely the first carry kernels of the existing **original** ordered Cauchy omitted triangle, per 20261102_hourly_r11_d25_cm_hensel_cauchy_transport.md. Their source and sign are preserved.

## U2 — An unconditional exact source-moment certificate at z=1/2

For p=6r+1>=7 and 0<=m<=2r, c_m mod p=binom(2r,m)binom(4r,m). Therefore

\[
(\theta^nD_p)(1/2)=\sum_{m=0}^{2r}m^n\binom{2r}{m}\binom{4r}{m}\pmod p.
\]

**Theorem U2.** For **every integer 0<=h<p**, with falling factorial x^{\underline h},

\[
\boxed{\sum_{m=0}^{2r}m^{\underline h}\binom{2r}{m}\binom{4r}{m}
\equiv(-1)^h(1/3)_h(2/3)_h/h!\pmod p.}
\]

Proof. For h<=2r, elementary Vandermonde convolution gives the exact integer identity

\[
\sum m^{\underline h}\binom{2r}m\binom{4r}m
=\binom{6r}{2r}
\frac{(2r)^{\underline h}(4r)^{\underline h}}{(6r)^{\underline h}}.
\]
Reduce 2r=-1/3, 4r=-2/3, 6r=p-1, binom(p-1,2r)=1 modulo p; (p-1)^{\underline h}=(-1)^h h!, a unit for h<p. For 2r<h<p, the left vanishes and the factor (1/3)_{2r+1}=p times a p-unit makes the right zero. QED.

Stirling conversion gives every fixed Euler jet below order p:
\[
(\theta^nD_p)(1/2)=\sum_{h=0}^n S(n,h)(-1)^h (1/3)_h(2/3)_h/h!\pmod p.
\]
In particular for n=0,1,2,3, the values are (1,-2/9,2/81,14/2187), so (L3 K_{0,p})(1/2)=-1/162. For T_j=(theta^j K_{0,p})(1/2), evaluation of the original L3 at 1/2 gives the exact four-port certificate
\[
\boxed{162T_3-243T_2-117T_1-18T_0\equiv-2\pmod p.}
\]
No CM assumption is needed for U1/U2 or this source relation.

## Distinct new finite conjecture C1

Using K0(p)=T0 and the genuine original carry slope L0(p)=T1, exact computation suggests for primes p=6r+1:
\[
\boxed{K_0(p)+6L_0(p)\stackrel{?}{\equiv}3((2/p)-1)\pmod p}
\]
where (2/p) is the Legendre symbol. This was verified for **all 611 primes 7<=p<=10000, p=1(mod6)**; it is NOT a proved universal statement.

For D25 target classes p=13,19 mod24 the character equals -1, so a proof of C1 together with the previously open K0(p)=0 gives L0(p)=-1. On the non-CM example p=31 the verified values K0=L0=0 and (2/p)=1. This discriminates the two branches; it is important not to drop the character source.

Representative exact residues, displayed as (p; T0,T1,T2,T3; K1; theta^0..3 D_p; C1 residual):
- 7; 5,5,5,5; 6; 1,6,4,0; 0
- 13; 0,12,8,3; 6; 1,7,5,9; 0
- 19; 0,18,0,9; 9; 1,4,8,7; 0
- 31; 0,0,25,4; 28; 1,17,5,30; 0
- 37; 0,36,0,10; 18; 1,8,32,22; 0
- 373; 0,372,67,132; 186; 1,207,350,146; 0
- 1171; 0,1170,423,388; 585; 1,260,1012,219; 0

The companion standard-library exact integer program, d25_cauchy_gauss_pf_moments_20261102.py, was run and tested polynomial coefficientwise through degree 2r+1 for all three equations, falling moments h<=6, the explicit jets, the four-port identity and C1 for all 611 primes; zero mismatches. A separate Fraction check for all formal coefficients through m=10 also passed. Source-specific integer/valuation labels and signed pair indices were retained; the Gauss inhomogeneity is an indispensable repair coordinate under the specified PF observation.

**Next science unit:** seek a terminating creative-telescoping/contiguous or character-sum certificate for C1, or a concrete prime counterexample. In parallel keep K0=0 and K1=-1/2 for the CM classes as conjectures, then compose the signed Xi joint interaction and old high-band A2,B2,C2 into the original D25 Delta-R target. Original p373 H0/B0 remains a distinct native experiment (#1559).

**Native control status (authenticated read 2026-11-02):** gateway 0.6.11, UPSTREAM_CODE_REVIEW_REQUIRED, research_authority_granted=false, executor_binding_configured=false, 5/5 jobs. Historical Research #6637 only a read-only recovery success; #6638 was a definite failed continuation. Neither replayed; no actual current Source session/claim/run/checkpoint. Existing support #1558 owns repair. Fixed Research logical ID separate from maintenance, and original source pins and contribution origin preserved. External author-side GitHub persistence grants neither role authority nor mathematical admission.
