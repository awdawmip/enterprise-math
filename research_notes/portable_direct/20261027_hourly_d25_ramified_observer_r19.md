# D25/LIFT R19 — Ramified p=19 observer zeros retain a genuine fractional E-source

Date 2026-10-27. Research logical conversation \`chatgpt-research-hourly-enterprise-math-20260923\` (not maintenance). Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`; publication \`TP2-B6F4FC938FF94941C1B7\`; frozen scientific Source pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\` unchanged. Parent D25/LIFT/JT2 remains OPEN.

**AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY**. No Source-native CLAIM/open/checkpoint, native original-class H0/B0 experiment, or independent Driver review. This is the actual original-parameter finite ordered low/high carrier, not original fixed-z=2 Clausen Q, full six-channel WZ cancellation, infinity or high/high source.

## New question and genuine source

Consume R17's original four-cutoff-face Ward identity and R18's p19 triple mod-19 root and integral nonlift without recrediting them. New question: at **actual algebraic ramified** zeros of O, is the authentic source G also zero? Which oriented source jets survive cancellation?

Take p=19, m=3, L=-5, N=5, theta=-p/6, original f_r=(1/6)_r(1/3)_r/(r!)² and beta_r=f_r/19² for 6<r<19. For actual ordered (j,ell) with 1<=j,ell<=6, n=ell-j, define Z_n=sum_(ell-j=n) (j+ell-p) f_j beta_(p-ell). Retain the four real E_n cutoff terms (two for n<0, two for n>=0), satisfying the proved exact E_n=(p-n) Z_n-(p-n-1/2) Z_(n+1), Z_6=0. Define O(z)=sum_(n=-5)^5 z^n Z_n; J(z)=zO'(z); G_-=sum_(n=-5)^(-1) z^n E_n; G_+=sum_(n=0)^5 z^n E_n; G=G_-+G_+. The exact R17 finite summation law is

$$
G(z)=\left(p-\frac{p+1/2}{z}\right)O(z)
-\left(1-z^{-1}\right)J(z)
+\left(p-L+\frac12\right)z^{L-1}Z_L,\quad v_{19}(Z_L)=1. \tag{1}
$$

## General ramified rank-jet source lemma (new, with proof)

Let p be an odd prime, 2<=r<p, z0 a p-adic unit, and T(z)=z^k O(z) an integral polynomial. Assume T(z0+x)=sum_i c_i x^i with v_p(c0)=1, c1,...,c_(r-1) in pZ_p, cr a unit, and mod-p exact root multiplicity r at z0. Then Hensel factors T at that residue class into an r-degree *Eisenstein* polynomial and a unit-at-zero cofactor. Every algebraic zero z=z0+x there obeys

$$
v_p(x)=1/r,\qquad \overline{x^r/p}=-\overline{(c_0/p)/c_r}. \tag{2}
$$

If the genuine source identity is G=A(z)O-B(z)J+C(z), J=zO', B(z0) is a unit and v_p(C)>=1 on the disk, every such O-zero satisfies

$$
v_p(J)=v_p(G)=(r-1)/r,\qquad
\overline{G/x^{r-1}}=-\overline{B(z_0)}\,\overline{z_0^{1-k}}\,r\overline{c_r}\ne0. \tag{3}
$$

**Proof.** The exact mod-p multiplicity permits Hensel factorization into the monic degree-r factor reducing to x^r and a factor whose constant term is a unit. The degree-r factor has lower coefficients in pZ_p, and its constant has valuation one, hence is Eisenstein. At any of its roots only c0 and cr*x^r have minimal valuation 1, proving (2). At T=0, J=z^(1-k)T'. The term r*cr*x^(r-1) uniquely has valuation (r-1)/r; lower i terms have valuation >=1 and higher i terms >=1. As p∤r, the leading residue is nonzero. On O=0, the source term -BJ has that fractional valuation, while C has valuation >=1, proving (3). This theorem is scoped to the stated polynomial/source/residue disk, not an all-prime or full Clausen assertion. QED.

## New p=19 exact certificate and true oriented source jets

Define T(z)=z^5 O(z), x=z-13. Reconstructing all ordered f_j beta_(19-ell) cells via exact rational arithmetic yields

$$
(c_0,c_1,c_2,c_3)\equiv(247,304,342,122)\pmod{361}.
$$

Consequently c0/19=13, c1/19=16, c2/19=18, c3=8 modulo 19, with v(c0)=1, v(c1)=v(c2)=1, v(c3)=0. The root is exactly triple modulo 19. All **three algebraic roots** of O reducing to 13 generate totally ramified degree-three extensions, satisfying

$$
v_{19}(x)=1/3,\qquad \overline{x^3/19}=15.
$$

The residue 15 is not a cube in F19, consistent with the ramified rather than ordinary integral lift. Here B(z)=1-z^-1 is a unit at 13 and the finite genuine left boundary C has valuation one. Equation (3) gives the **new authentic obstruction** at every such algebraic zero:

$$
\boxed{v_{19}(J)=v_{19}(G)=2/3,\qquad
\overline{G/(z-13)^2}=12\ne0\in\mathbb F_{19}.} \tag{4}
$$

This stronger no-joint-zero theorem applies **even after allowing algebraic p-adic unit weights** within residue 13. R18 only showed that no ordinary integral z=13+19t lifted the first-digit geometric zero. It does not imply all residue classes, primes, six channels, fixed z=2 or original-class Frobenius are obstructed.

A **separate direct four-face** computation, not obtained by substituting the Ward identity, extracts the oriented Laurent jets at z=13:

| Real source orientation | x^0 | x^1 | x^2 |
| --- | ---: | ---: | ---: |
| G_- | 8 | 4 | 3 |
| G_+ | 11 | 15 | 9 |
| G=G_-+G_+ | **0** | **0** | **12** |

All numbers are mod19. Actual distinct oriented sources cancel at orders 0 and 1 but **not** at order 2. At the algebraic root, x² has valuation 2/3, whereas the full constant and linear terms and every term x^3 onward have valuation >=1. Thus this original source-side independent certificate reproduces (4). The scalar mod19 cancellation is an information-losing observer, not evidence that E vanished.

## Executed check, information scope and recovery

Companion \`20261027_hourly_d25_ramified_observer_r19_check.py\`, Python standard library; actually executed PASS. Rebuilds original rational f, beta, all Z and four cutoff E sources, checks every rank Ward identity, all 11 Taylor coefficients mod361, the exact-multiplicity/Eisenstein conditions, the nonzero 12 coefficient, true oriented E jets, and (without recrediting) all 19 integral lifts. Ramified cubic conclusions are proved algebraically by the lemma; a p-adic field runtime was **not** run. No floats, sorry, admit or custom axioms; author finite and algebraic check is not independent acceptance.

**BRC COMPOSE_APPLIED:** preserve ordered (j,ell), four genuine truncation source faces, orientation, prime valuations and rank jets. The coarse total G(13) mod19 erases the live second jet. The minimum repair for this disk must retain the nonzero x² source. These are auxiliary arithmetic ranks, not X6 spatial axes; no P000 change.

**Control:** reuse Research own recovery #6571 and full continuation #6572/#6573/#6574: session \`MCP-3a7c6c3a67bd4e52b1cdf49064751829\`, Researcher \`EM-ENTERPRISE-C1C79B\`, no own pending/unopened/live run/unpublished uploads; two neutral protected staging dispositions; Source checkpoint \`SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED\`, source sha \`2c880d77e9f78b8ed26ed44c3a3c6c90ffd2117f\`, \`NO_LIVE_CLAIM / NEEDS_DISPATCH / execution_authorized=false\`, predecessor-CAS difference unresolved. Portable Git evidence is not Source checkpoint. Support owned by \`awdawmip/enterprise-math#1558\`; no CLAIM, open, review or session mutation asserted.

**Next smallest science:** return to the fixed original z=2 six signed Hasse anti-diagonal channels (0,2),(1,2),(0,3),(2,2),(1,3),(0,4). Use the bivariate genuine J/E mother to test true cross-channel WZ cancellation, preserving four faces, independently oriented positive infinity and high/high corner, or give source-labeled nonzero residual. Same-original-class H0/B0, [X]U modp², Frobenius eta/kappa, native experiment and independent review remain open, frozen source unchanged.