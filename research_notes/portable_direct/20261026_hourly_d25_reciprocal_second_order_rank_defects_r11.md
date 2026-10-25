# D25/LIFT — reciprocal second-order rank defects beneath the corrected Clausen Green port

**Date:** 2026-10-26. **Parent Task:** RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. **Publication:** TP2-B6F4FC938FF94941C1B7. **Frozen scientific pin:** c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged).

**Classification:** AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. This note proves elementary exact rational-lift identities for the *corrected Clausen middle-rank port*. It does not assert a native Source checkpoint, a crystalline Frobenius/CM computation, a formal Result, or the all-target-prime D25/LIFT congruence.

## Consumed immutable inputs and scoped carriers

From the already published corrected factorial source and Green/adjoint notes (20261026_hourly_d25_middle_rank_factorial_wz_kernel.md, 20261026_hourly_d25_green_hypergeometric_adjoint_r11.md), fix a prime p=6m+1>=7, L=m+1, U=2m. For the *rational factorial lifts* define

\[
a_j=(-1)^{m+j+1}\frac{m!(j-m-1)!(2m)!}{(2m-j)!(j!)^2}
\quad(L\le j\le U),\qquad
h_\ell=\frac{2m!(2m)!((\ell-1)!)^2}{(\ell+m)!(\ell+2m)!}
\quad(1\le\ell\le U).
\]

Let v_j=2^{-j}a_j and g_\ell=2^\ell h_\ell, with zero extension outside these *finite* intervals. Their exact rational recurrences, not new claims, are

\[
\frac{v_{j+1}}{v_j}=\frac{(j-m)(j-2m)}{2(j+1)^2},\quad
\frac{g_{\ell+1}}{g_\ell}=\frac{2\ell^2}{(\ell+m+1)(\ell+2m+1)}.
\]

For ranks in the declared intervals their reductions modulo p agree with the actual corrected Clausen source jets. The rational lifts beyond those ranks are not promoted to an original p-adic/CM source.

Define \(\theta=z\,d/dz\),
\[
V(z)=\sum_{j=L}^{U}v_jz^j,\quad
G_U(z)=\sum_{\ell=1}^{U}g_\ell z^\ell,\quad
\mathcal M=2\theta^2-z(\theta-m)(\theta-2m),\quad
\mathcal N=(\theta+m)(\theta+2m)-2z\theta^2.
\]
All identities in the next section hold **exactly over Q**, so reducing their denominator-safe finite coefficients modulo p is valid. In particular, this is a signed/provenance-labeled rank calculation, not positive-weight cancellation.

## Theorem J — reciprocal second-order Green sources (new)

The finite outer and inner rank carriers obey *inhomogeneous second-order* equations
\[
\boxed{\ \mathcal M V=2L^2v_Lz^L,\qquad
\mathcal N G_U=4z-2U^2g_Uz^{U+1}.\ }\tag{J1}
\]
With the algebraic involution \(I f(z)=f(z^{-1})\), the two operators are *exactly reciprocal*:
\[
\boxed{\quad\mathcal N=-z\,I\mathcal M I.\quad}\tag{J2}
\]
Consequently, if \(F(z)=V(z^{-1})\), then
\[
\boxed{\quad \mathcal N F=-2L^2v_Lz^{1-L}.\quad}\tag{J3}
\]
Thus **F and G_U solve the same second-order operator with opposite-rank explicit boundary sources**. Their middle-rank information has not been erased.

**Proof.** The coefficient of \(z^n\) in \(\mathcal M V\) is
\(2n^2v_n-(n-1-m)(n-1-2m)v_{n-1}\). For L<n<=U it vanishes by the exact recurrence. It equals \(2L^2v_L\) at n=L. At n=U+1 the numerator factor n-1-2m=0, and at all other n it vanishes. This proves the first identity. Similarly, the coefficient of \(z^n\) in \(\mathcal N G_U\) is \((n+m)(n+2m)g_n-2(n-1)^2g_{n-1}\). Its only survivors occur at n=1 (equal to \((m+1)(2m+1)g_1=4\)) and n=U+1 (equal to \(-2U^2g_U\)). For (J2), use \(I\theta I=-\theta\), \(IzI=z^{-1}\), respecting operator order. Applying (J2) to F gives (J3). QED.

**Order reduction.** The predecessor's homogeneous third-order outer operator factors *exactly* as \((\theta-L)\mathcal M\). Its inner hypergeometric third-order operator factors as \((\theta-1)\mathcal N\); this annihilates the rational infinite continuation \(G_\infty\), since \(\mathcal N G_\infty=4z\). For the **actual finite** \(G_U\), retain the extra \(-2U^2g_Uz^{U+1}\) in (J1); dropping it would silently change the source/observer.

## Theorem K — closed critical-point finite rank sum rules (new)

The outer leading boundary simplifies to
\[
L^2a_L=m\binom{2m}{m}.
\]
At the common singular evaluation point \(z=1/2\), the coefficient of \(\theta^2\) in \(\mathcal N=(1-2z)\theta^2+3m\theta+2m^2\) vanishes. Applying (J1),(J3) **to the finite carriers**, not to a non-uniformly reduced infinite series, yields two exact finite rational identities:
\[
\boxed{\sum_{j=m+1}^{2m}(3j-2m)a_j=\binom{2m}{m}.}\tag{K1}
\]
\[
\boxed{
3m\sum_{\ell=1}^{2m}\ell h_\ell
+2m^2\sum_{\ell=1}^{2m}h_\ell
=2-(2m)^2h_{2m}.}\tag{K2}
\]
Both remain valid modulo p under their specified corrected-source interpretation.

**Proof.** At z=1/2, \(F=\sum a_j\) and \(\theta F=-\sum j a_j\). The right side of (J3) becomes \(-2L^2v_L2^{L-1}=-L^2a_L\), giving (K1) after division by the nonzero integer m. Similarly \(G_U(1/2)=\sum h_\ell\), \(\theta G_U(1/2)=\sum\ell h_\ell\), and the right side of the second formula (J1) becomes \(2-U^2h_U\), giving (K2). QED.

**Exact example.** m=2, p=13: \((a_3,a_4)=(4/3,-1/12)\), so \(5a_3+8a_4=6=\binom42\). The identity follows for every integer m>=1, not merely the tested primes.

## Theorem L — paired Lagrange/Wronskian transfer with all finite boundaries

Write \(F=V(z^{-1})\), \(G=G_U\), and define
\[
\mu(z)=\frac{z^{3m-1}}{(1-2z)^{3m+1}},
\qquad A(z)=\frac{z^{3m+1}}{(1-2z)^{3m}}.
\]
There is an exact rational-function identity
\[
\boxed{
\frac d{dz}\{A(FG'-GF')\}
=\mu\{(4z-2U^2g_Uz^{U+1})F
+2L^2v_Lz^{1-L}G\}.}\tag{L1}
\]
**Proof.** In ordinary derivative notation,
\(\mathcal N=z^2(1-2z)\partial_z^2+z(1+3m-2z)\partial_z+2m^2\).
Direct differentiation verifies \((A f')'=\mu(\mathcal N f-2m^2f)\), hence
\((A(FG'-GF'))'=\mu(F\mathcal NG-G\mathcal NF)\).
Substitute (J1),(J3). QED.

The rational transfer is a concrete coupled second-order WZ/Green *entry*, not an endpoint-only proof of the original D25 reflection target. The factor \((1-2z)^{-3m}\) is singular at z=1/2, so **one cannot simply evaluate (L1) there and drop the signed bulk terms**. Statements (K1)-(K2) instead use the regular finite polynomial equations (J1)/(J3). The previously established nonzero Abel residual at p=13 remains.

## Verification and exact next unit

The companion stdlib program 20261026_hourly_d25_reciprocal_second_order_rank_defects_check.py independently constructs factorial lifts, checks (J1) coefficientwise and (K1)-(K2), with **30 exact-rational m cases** and **80 finite-field primes** 7<=p<=997, p=1 mod 6. All checks passed. The operator involution and (L1) have the displayed algebraic proofs; an additional direct rational-function SymPy spot check was run for m=1,2,3,4 (not a requirement of the stdlib verifier). This is author verification, not independent audit or Lean formalization.

**BRC resolution: COMPOSE_APPLIED.** Input carrier retains rank j/l, signed coefficients, corrected denominator, Hasse-jet and valuation provenance; future observers include the exact finite endpoint evaluation and the still-open signed convolution \(-216^{-1}\sum v_jK_j\). The two reciprocal inhomogeneous sources are not identified with the native crystalline Frobenius or a P000 six-axis dynamic.

**Do not repeat:** prior corrected p^4 reflection bridge, factorial Theorems E/F, third-order Green/adjoint result, first-order affine Gosper impossibility, and Source-durable Hesse/Hilbert-90 units. These serve as inputs.

**Next smallest mathematical unit:** test whether the explicit paired transfer (L1) can be composed with \(K=(1+5z)(1-z)^{-2}G\) and the **full corrected Clausen parameter differential operator** into a source-faithful telescoping certificate for \(\sum v_jK_j\), including both endpoints and the 1/2 singularity. No claim that (K1) or (K2) determines that contraction. Actual parent hard target still requires same-class H0/B0, divided-power [X]U mod p^2, rank/semilinear direction, normalization eta, and kappa/Delta correspondence; original CM experiment NOT_RUN. Do not change frozen scientific pin or predecessor Source checkpoint.

**Native control at this run:** own Research lane recovery_status SUCCEEDED (bridge #6438); exact canonical D25 continuation SUCCEEDED (bridge #6439, complete receipt pages #6440/#6441). The current native packet reports an existing SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED checkpoint but execution_authorized=false, no own live claim/run, latest CLAIM MCP-d0d70cd041b01e5db192870a versus checkpoint predecessor MCP-87631b892b41fa18d799f2d8. No canonical continuation_prepare/claim/open, upload, native checkpoint, Result, review or release is asserted for this portable note. The ongoing control support tracker is enterprise-math#1558.
