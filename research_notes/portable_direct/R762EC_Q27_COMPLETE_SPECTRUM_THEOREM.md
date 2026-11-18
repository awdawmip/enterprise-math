# R762EC — Complete exact cyclotomic valuation spectrum for Q=27

2026-11-18 (Asia/Shanghai); author lineage EM-X6-3050F6; task RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142. Exact finite mathematical proof using integral cyclotomic arithmetic, reproducible author checker, independent review NOT_REVIEWED. Continues R762EB and resolves its Q=27 deep v_pi>=18 class.

Frozen science pins: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json and @e3f42efac29a2da2d95be391f3231a664e2fade0:research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md. This is the six-named-positive-path *terminal* candidate BRC observer, not native signed TRIADIC_CLOSURE_E.

## Theorem — Q=27 finite complete spectrum

Let \(\zeta=\zeta_{27}\) and \(\pi=\zeta-1\), and take the same six-branch polynomial
\[
P(X,Y,Z)=1+X+Z+XY+YZ+XYZ,\quad
\lambda_{ijk}=P(\zeta^i,\zeta^j,\zeta^k),\quad i,j,k\in\mathbb Z/27.
\]
All 27^3=19,683 character values have the following exact valuations, including zeros:

| \(v_\pi(\lambda)\) | Number of characters |
|---|---:|
| 2 | 13,122 |
| 4 | 3,888 |
| 6 | 1,782 |
| 10 | 432 |
| 12 | 144 |
| **18** | **111** |
| **\(+\infty\), exact zero** | **204** |

In particular the previously unresolved R762EB \(v_\pi\ge18\) family of size 315 consists precisely of **111 elements with valuation 18 and 204 exact zero eigenvalues**; no finite value exceeds 18. The witness \(P(1,1,1)=6\) has \(v_\pi=18\), while the character (i,j,k)=(0,9,9) is an exact zero.

## Proof — exact algebraic division and exhaustive certificate

The ring of integers is
\[
\mathcal O_K=\mathbb Z[\zeta]
=\mathbb Z[X]/(\Phi_{27}(X)),\qquad
\Phi_{27}(X)=X^{18}+X^9+1,
\]
so the 18 coefficients of \(1,\zeta,\ldots,\zeta^{17}\) give a unique exact integer representation of every character value. For \(18\le e<27\), the reduction
\[
\zeta^e=-\zeta^{e-9}-\zeta^{e-18}
\]
produces that representation directly from the six original branch exponents.

Define the explicit integer polynomial
\[
T(X)=\frac{\Phi_{27}(X)-3}{X-1}
=2\sum_{r=0}^{8}X^r+\sum_{r=9}^{17}X^r.
\]
Since \((\zeta-1)T(\zeta)=\Phi_{27}(\zeta)-3=-3\),
\[
\boxed{\frac{f(\zeta)}{\pi}=-\frac{f(\zeta)T(\zeta)}{3}.}
\]
Also \(\mathcal O_K/(\pi)\cong\mathbb F_3\) under \(\zeta\mapsto1\), so \(f(\zeta)\) is \(\pi\)-divisible exactly when the sum of its 18 basis coordinates is 0 modulo 3. Whenever divisible, the displayed division gives an integral 18-coordinate vector. This supplies a fully exact algorithm for \(v_\pi(f)\): represent \(f\), test equality to zero in the integral basis, otherwise repeatedly divide by \(\pi\) while the reduction sum vanishes modulo 3; the first nondivisible quotient gives the valuation.

The attached pure-Python checker R762EC_VERIFY.py exhausts **all** \((i,j,k)\in\{0,\ldots,26\}^3\). It constructs each \(\lambda_{ijk}\) directly from the six named branch monomials, checks the integer divisibility of every performed quotient, and verifies at each step that multiplying the quotient by \(\pi\) reproduces the previous exact 18-vector. Every nonzero element terminates by degree at most 18; the 204 zeros are detected as identically zero power-basis vectors. It asserts the complete histogram above, \(\sum \#=19683\), the R762EB deep-class subtotal 315, and a SHA256 fingerprint of the ordered 19,683-byte valuation table (255 for exact zero). The evidence file R762EC_EVIDENCE.json contains that digest and all counts/witnesses. No floating-point root evaluation is used. The finite domain is exhausted and the integral division law is proved, giving a computer-assisted finite exact certificate, not merely agreement at samples. QED.

## Scope and next problems

This Q=27 result is a mathematical theorem for the **fixed finite model**. R762EB supplies a separate all-\(a\ge3\) theorem for the lower character strata; neither result yet settles the exact coefficient-content \(v_3(\gcd(\mathrm{coeffs}(P^n)))\) at every horizon or the licensed signed Cell/Link/Port event dynamics. Next, exploit the 204-character zero locus and 111 nonzero deep characters to derive an exact algebraic description of the zero relation and a coefficient nondivisibility witness; study higher \(3^a\) via digit lifting while preserving native X6 provenance, P000, third component and V17/V29/V39 transport obligations.
