# D25/LIFT — Toeplitz residue and infinity compensation for the signed Clausen port

Date: 2026-10-26. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 **unchanged**.

**Status:** AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. This mathematical auxiliary result has no native CLAIM/OPEN/checkpoint, independent review, original CM experiment, or all-prime LIFT proof.

## Exact signed carrier

For an integer m≥1 put L=m+1 and U=2m. Reuse the previously established corrected-Clausen rational lifts
\[
a_j=(-1)^{m+j+1}\frac{m!(j-m-1)!(2m)!}{(2m-j)!(j!)^2}
\quad(L\le j\le U),\qquad
h_\ell=\frac{2\,m!\,(2m)!\,((\ell-1)!)^2}{(\ell+m)!(\ell+2m)!}
\quad(1\le\ell\le U).
\]
The first factor 2 in the numerator of h is an ordinary factor of two. Define v_j=2^{-j}a_j and g_ell=2^ell h_ell, with zero extension beyond their *finite* ranks. Form Laurent polynomials
\[
F(z)=\sum_{j=L}^Uv_jz^{-j},\qquad
G(z)=\sum_{\ell=1}^Ug_\ell z^\ell,\qquad H(z)=F(z)G(z).
\]
The original middle reflection observation has orientation ell≤j:
\[
S_m=-\frac1{216}\sum_{j=L}^U\sum_{\ell=1}^j
(6(j-\ell)+1)v_jg_\ell.
\]
The finite factorial denominators are all prime to p=6m+1 when p is prime, so the rational relations below admit source-faithful reduction modulo p. They are not statements about native crystalline Frobenius data.

## Theorem P — three-residue identity with a necessary infinity boundary

Set
\[
K(z)=\frac{1+5z}{(1-z)^2},\qquad R(z)=\frac{K(z)H(z)}{z}.
\]
The kernel has distinct expansions
\[
K(z)=\sum_{r\ge0}(6r+1)z^r\quad\text{near }z=0,\qquad
K(z)=\sum_{r\ge1}(6r-1)z^{-r}\quad\text{near }z=\infty.
\]
It follows by extracting the coefficient of z^{-1} that
\[
\operatorname{Res}_{z=0}R(z)\,dz=-216S_m,
\quad
\operatorname{Res}_{z=\infty}R(z)\,dz=-C_{\infty,m},
\]
where the **complementary upper triangle** is
\[
C_{\infty,m}=\sum_{j=L}^U\sum_{\ell=j+1}^U
(6(\ell-j)-1)v_jg_\ell.
\]
Since K=6/(z-1)^2+5/(z-1) near z=1, the residue there is
\[
\operatorname{Res}_{z=1}R(z)\,dz=6H'(1)-H(1).
\]
There are no other finite poles. The rational residue theorem therefore gives, for **every integer m≥1**,
\[
\boxed{-216S_m=H(1)-6H'(1)+C_{\infty,m}.}\tag{P}
\]
Proof of the rank orientation: write H(z)=sum_n H_n z^n. At 0, only n≤0 contributes with weight 1-6n, corresponding to ell≤j. At infinity, only n≥1 contributes with weight -(6n-1), corresponding to ell>j. The residue at 1 collects all ranks through their zero and first moments. Thus dropping the infinity boundary is not a legitimate compression of the original signed rank port.

## Theorem Q — positivity and exact lower bound in characteristic zero

For all m≥2,
\[
\boxed{C_{\infty,m}\ge5v_Lg_{L+1}
=\frac{20m\,m!\,(2m)!}{(2m+2)(2m+1)(3m+2)!}>0.}\tag{Q}
\]
Equality holds at m=2, while m≥3 gives strict inequality; m=1 has an empty upper triangle, so C_{\infty,1}=0.

Proof: For each ell≥L+1, the inner sum
\(B_\ell=\sum_{j=L}^{\ell-1}(6(\ell-j)-1)v_j\)
starts with a positive term and alternates. Moreover,
\[
v_{j+1}/v_j=(j-m)(j-2m)/(2(j+1)^2)\in(-1,0)
\]
for L≤j<U, and the extra positive weight 6(ell-j)-1 decreases as j increases. Consequently the absolute summands decrease strictly, so B_ell>0. As all g_ell>0, the ell=L+1 term supplies exactly 5v_Lg_{L+1}; all subsequent ell terms are positive. The factorial bound follows by direct cancellation. **Positive rational does not imply nonzero modulo all primes.**

## Theorem R — rank-two obstruction to replacing the infinity port with one finite-part scalar

The preceding critical-point Laurent finite part had the different upper-triangle observation
\[
\mathrm{FP}_m=\frac{(-1)^{3m}}{2^{3m}}
\sum_{j=L}^U\sum_{\ell=j}^U(j+\ell)
\binom{3m+\ell-j}{3m}a_jh_\ell.
\]
For m≥3, choose two source cells A=(L,L+1), B=(L,L+2). In coordinates a_jh_ell their C_infinity weights are 10 and 44. The FP weights are
\[
O_A=c(2m+3)(3m+1),\qquad
O_B=c(2m+4)\binom{3m+2}{3m},\qquad c=(-1)^{3m}2^{-3m}.
\]
Their determinant is
\[
\boxed{10O_B-44O_A=c(3m+1)(30m^2-8m-92)\ne0\quad(m\ge3).}\tag{R}
\]
Hence, on an unrestricted source-labelled signed-rank carrier, one scalar FP observation does not determine the infinity correction: choosing delta A=O_B, delta B=-O_A preserves FP but changes C_infinity. This is an explicit BRC observer-fiber witness, **not** a claim that the constrained one-parameter hypergeometric family admits independent changes to those two cells.

## O(m) compensation, exact validation, and next action

Using two source-preserving prefix moments
\[
A_\ell=\sum_{j=L}^{\ell-1}v_j,\qquad J_\ell=\sum_{j=L}^{\ell-1}jv_j,
\]
one computes the missing infinity boundary with **O(m)** field operations:
\[
\boxed{C_{\infty,m}=\sum_{\ell=L+1}^U
g_\ell[(6\ell-1)A_\ell-6J_\ell].}\tag{P5}
\]
The one-number mass A alone is insufficient for an arbitrary affine rank weight.

An independent Python-stdlib verification executed exact rational calculations for m=1,...,30: the original lower triangle, all three residues, first-moment expression, upper double sum, two-prefix recurrence, and positivity bound. It checked determinant (R) for m=3,...,30. The finite-field route independently reconstructed factorials and verified the identity for all 80 primes p≡1 (mod 6), 7≤p≤997. Examples:
m=2: C_infinity=1/630 and -216S_2=87161/151200;
p=13: C_infinity≡11 (mod 13);
p=19: C_infinity≡18 (mod 19).
Of the 80 checked primes, C_infinity≡0 occurred at p=7 and p=199, a concrete warning against importing rational positivity into F_p. These are author checks, not independent review.

**BRC: COMPOSE_APPLIED.** Keep signed rank, corrected denominator/Hasse source, valuation, and the separate observers z=0,1,infinity and critical z=1/2. The complex coordinate z is an *external auxiliary analytic model*; no native X6 plane or physical interpretation is asserted. P000 remains fixed.

Consume the immutable preceding reciprocal-Green derivation at commit 8599a0714b634d0fe32442628ffa8f067e230266, path research_notes/portable_direct/20261026_hourly_d25_reciprocal_second_order_rank_defects_r11.md (blob 6c1ece20a378acaf2aff23c970254cfaf91262cb) and the separately labelled, not-yet-admitted local critical-point M–O result. Do not recount those previous findings as new work.

**Next precise research unit:** combine H(1)-6H'(1) from (P) with both inhomogeneous reciprocal Green equations and the full corrected Clausen parameter operator; preserve the independently necessary infinity two-moment correction when using the critical z=1/2 FP. Start with p=13, then seek a uniform statement for target p≡13,19 (mod 24). The original D25/LIFT/JT2 mother objective remains OPEN and still needs same-class CM H0/B0, divided power [X]U modulo p², Frobenius direction/normalization, kappa mapping and independent review.

This is neutral portable research evidence only, not activity registration, native checkpoint or formal Result. The new exact gateway continuation call returned INVALID_ARGUMENT / CONTROL_QUOTA, not NO_DISPATCH; earlier cross-epoch claim repair has no new readback. Preserve historical service session, staging, Source frontier and ownership. No continuation_prepare, CLAIM, OPEN, publish_checkpoint, release or freeze was performed.
