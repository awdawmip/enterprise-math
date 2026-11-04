# D25 — CM(−24) hypergeometric fixed fiber and a two-port first-jet transfer

Date 2026-11-05. **AUTHOR-DERIVED EXACT RATIONAL/POLYNOMIAL IDENTITY / PURE-INTEGER-CHECKED / UNREVIEWED / NOT_ADMITTED**. Follows D25 second-digit reciprocal source repair. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Auxiliary CM/Legendre only.

## Exact fixed-fiber theorem

Set
$$Q(t)=t^4-140t^3+294t^2-140t+1,\quad x(t)=\frac{16t(1-t)^2}{(1+t)^4},\quad B(t)=t^2-6t+1.$$

The following identities hold in Q(t), with exact integer numerator certificates:

$$\boxed{9\cdot16t(1-t)^2-(1+t)^4=-Q(t).}\tag{1}$$

$$\boxed{x(t^{-1})=x(t),\qquad x'(t^{-1})=-t^2x'(t).}\tag{2}$$

$$\boxed{x'(t)=\frac{16(1-t)B(t)}{(1+t)^5},\qquad16t(1-t^2)x'(t)=16x(t)B(t).}\tag{3}$$

Thus the CM quartic Q=0 is **exactly** the fixed hypergeometric fiber x=1/9, retaining four t-branches paired by inversion.

The local coordinate is étale for every p≥5 at each CM root: Q(−1)=576≠0 (mod p), Q(1)=16≠0 (mod p). Moreover, Euclidean division gives Q≡512(1−6t) modulo B, so
$$\boxed{\mathrm{Res}(Q,B)=512^2[1-6(6)+36(1)]=2^{18}.}\tag{4}$$
Hence B shares no root with Q in characteristic p≥5. Formula (3) implies x' is invertible at every geometric Q-root in characteristic p≥5. Equivalently, at Q(a)=0
$$\boxed{9x'(a)=-Q'(a)/(1+a)^4\ne0.}\tag{5}$$

**Proof.** Expand numerators for (1) and (3). The reciprocal palindromicity of N=16t(1−t)^2 of formal degree four and D=(1+t)^4 gives x(1/t)=x(t); differentiating proves the derivative sign (2). Reduce Q by t²=6t−1 to get 512−3072t; the product of (1−6t) over the two roots of B is 1 because their sum and product are 6 and 1. This proves (4) and the étale conclusion, without any CM arithmetic assumption. QED.

## Exact source-preserving triangular first-jet interface

Let L(t)=16t(1−t²), A(t)=1+2t−7t², and define the first-jet operator D_A=L d/dt+A. For **any** differentiable prefactor P(t) and formal or rational x-dependent G(x), the chain rule gives at every Q-root a:
$$\boxed{D_A[P(t)G(x(t))]_{t=a}=
P(a)\frac{16}{9}B(a)G'(1/9)
+[L(a)P'(a)+A(a)P(a)]G(1/9).}\tag{6}$$

This is an explicit triangular transport of the **two distinct ports** (G value, G derivative) to the auxiliary CM Hasse jet, with signed Jacobian and prefactor derivative retained. It is not an assertion that the finite Hasse polynomial H_p(t) equals P(t)G(x(t)) at p² precision: the existing three-band mod-p identity has additional Frobenius and truncation terms. Deriving their **p² source** and the correct P is the next mathematical unit. The reciprocal branches have identical x but opposite derivative orientation by (2); no x-only scalar observation can substitute for the derivative/source port.

## Verification and relation to preceding result

Companion stdlib Python code performs exact integer polynomial checks of (1), reciprocal numerators, derivative numerator, identity L(N'D−ND')=16NBD, and Q mod B =512−3072t / resultant 2^18; **PASS**. This symbolic calculation has no finite-prime cutoff. Previous exact integral anomaly was
t^(m+2) C_m(1/t)−C_m(t)=8p(t²−1)H_m(t),
and the source-corrected second digit T_hat=T−8H has reciprocal covariance. Here (2),(6) supply the **explicit missing coordinate/observer bridge** to x=1/9 and the Jacobi–Green operator, while retaining the unmeasured finite-truncation corrections.

BRC/observer: t↔t⁻¹ gives two labeled CM branches with identical x, opposite tangent/derivative sign. The source-preserving observer consists of (branch, t, x, x', G, G', P, P', Hasse p-adic second digit); collapsing to x alone loses information needed by (6). This is an auxiliary external model, not a claim to identify the P000 six-dimensional native carrier.

Next: lift the existing exact three-band mod-p Gauss→Legendre identity by **one p-adic digit** at x=1/9, retaining Frobenius-band, prefactor, derivative and signed inverse-branch corrections; compare the resulting explicit port to previously established Jacobi–Green–Wronskian W(1) and Euler second digit. The frozen original p373 H0/B0 [X]U/eta/kappa/Delta-R and independent review remain separate and open. No native CLAIM, OPEN, canonical Source checkpoint, Result or mathematical admission is made by this author-side proof.
