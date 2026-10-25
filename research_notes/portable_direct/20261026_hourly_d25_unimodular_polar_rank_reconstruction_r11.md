# D25/LIFT — Unimodular critical polar-jet recovery of signed reflection and infinity boundary

2026-10-26 · Parent Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT · Publication: TP2-B6F4FC938FF94941C1B7 · **Frozen scientific Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged).**

Status: **AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.** This is an auxiliary corrected-Clausen finite rational/finite-field theorem, not a native CM experiment, formal Source checkpoint, Result, independent review or D25/LIFT all-prime proof.

## Input and precise carriers

Consume without re-crediting the previously proved corrected factorial lifts, reciprocal Green operators, critical Wronskian finite part, and Toeplitz infinity compensation in:
- research_notes/portable_direct/20261026_hourly_d25_reciprocal_second_order_rank_defects_r11.md
- research_notes/portable_direct/20261026_hourly_d25_critical_point_residue_r11.md
- research_notes/portable_direct/20261026_hourly_d25_toeplitz_infinity_compensation_r11.md
- research_notes/portable_direct/20261026_hourly_d25_green_finite_part_strict_sign_r11.md

For every integer m≥1, L=m+1, U=2m, define exact rationals

\[
a_j=(-1)^{j-L}\frac{m!(j-m-1)!(2m)!}{(2m-j)!(j!)^2}\quad(L\le j\le U),\qquad
h_\ell=\frac{2\,m!\,(2m)!((\ell-1)!)^2}{(\ell+m)!(\ell+2m)!}\quad(1\le\ell\le U).
\]

The initial 2 in h multiplies m!, and is not a factorial of 2m!. Let v_j=2^{-j}a_j, g_\ell=2^\ell h_\ell,
\(F(z)=\sum_{j=L}^U v_j z^{-j}\), \(G(z)=\sum_{\ell=1}^U g_\ell z^\ell\), \(H=FG\), \(W=FG'-GF'\).
The auxiliary complex z coordinate is not a native P000 spatial plane.

Set \(n_0=1-2m\), \(N=3m-1\). For r=0,...,N−1 let n=n_0+r and define the difference-rank mass and sum moments

\[
E_r=\sum_{\ell-j=n}a_jh_\ell,\qquad
D_r=\sum_{\ell-j=n}(j+\ell)a_jh_\ell
\]
over the stated finite j,ell ranges.

## Theorem A — exact, unimodular high-pole transform and integer inverse

Write t=1−2z (so z=(1−t)/2) and introduce two *different* transfer observables:

\[
T_H(t)=\frac{z^{3m}H(z)}{(1-2z)^{3m}},\qquad
T_W(t)=\frac{z^{3m+1}W(z)}{(1-2z)^{3m}}.
\]

The following are exact rational identities:

\[
\boxed{2^{3m}t^{3m}T_H(t)=\sum_{r=0}^{N-1}E_r(1-t)^{m+1+r},\quad
2^{3m}t^{3m}T_W(t)=\sum_{r=0}^{N-1}D_r(1-t)^{m+1+r}.}\tag{A1}
\]

Let b_k=2^{3m}[t^{k-3m}]T_H and d_k=2^{3m}[t^{k-3m}]T_W for k=0,...,N−1. These are only the high-pole coefficients from t^{-3m} through t^{-2}; neither simple pole nor finite part is needed.

\[
\boxed{b_k=(-1)^k\sum_{r=0}^{N-1}\binom{m+1+r}{k}E_r,\quad
d_k=(-1)^k\sum_{r=0}^{N-1}\binom{m+1+r}{k}D_r.}\tag{A2}
\]

The square integer matrix is unimodular:

\[
\boxed{\det\left((-1)^k\binom{m+1+r}{k}\right)_{0\le k,r<N}
=(-1)^{N(N-1)/2}.}\tag{A3}
\]

For either input x=b or x=d, **a constructive integral inverse** is

\[
\boxed{
c_k=\sum_{q=0}^k\binom{m+q}{q}x_{k-q},\qquad
X_r=(-1)^r\sum_{k=r}^{N-1}\binom{k}{r}c_k.}\tag{A4}
\]
Choose X=E for x=b and X=D for x=d. No division or prime-dependent linear-system solver occurs inside the inverse. The only prefactor in extracting the normalized pole is 2^{3m}; thus the construction works over Q and modulo every odd prime with the source denominators defined. In particular p=6m+1≥7 has all relevant factorial arguments at most 4m < p, so it preserves the specified corrected-Clausen source port modulo p.

**Complete proof.** Each H cell is v_jg_\ell z^{\ell-j}=2^{\ell-j}a_jh_\ell z^{\ell-j}, so multiplying by z^{3m} and substituting z=(1−t)/2 gives the common factor 2^{-3m} and (1−t)^{3m+\ell-j}. A W cell has the extra factor (j+\ell)z^{-1}; multiplying by z^{3m+1} yields the same transform of D. The possible differences run from 1−2m to m−1, i.e. precisely N consecutive exponents m+1,...,4m−1. This proves A1 and coefficient extraction proves A2.

Without row signs, the evaluation matrix of the degree-k polynomials binom(x,k), with leading coefficients 1/k!, at consecutive x=m+1+r has determinant Vandermonde/consecutive factorials = (prod_{i<j}(j−i))/(prod_{k=0}^{N−1}k!)=1. The row signs give A3. To prove the explicit inverse, factor the exact polynomial \(B(t)=\sum_r X_r(1-t)^{m+1+r}\) as \(B(t)=(1-t)^{m+1}R(t)\), \(R(t)=\sum_rX_r(1-t)^r\), deg R<N. The binomial series \((1-t)^{-m-1}=\sum_{q\ge0}\binom{m+q}{q}t^q\) recovers all N coefficients of R from the first N coefficients of B, with no missing tail because deg R<N. Finally \(X_r=[y^r]R(1-y)=(-1)^r\sum_{k=r}^{N−1}\binom{k}{r}c_k\). QED.

## Theorem B — reconstructing the *actual* signed port and complementary infinity correction

The previously fixed original lower signed middle-rank scalar and independent Toeplitz infinity observer are exactly

\[
\boxed{S_m=-\frac1{216}\sum_{r:n_0+r\le0}
(1-6(n_0+r))2^{n_0+r}E_r,}\tag{B1}
\]
\[
\boxed{C_{\infty,m}=\sum_{r:n_0+r>0}(6(n_0+r)-1)2^{n_0+r}E_r.}\tag{B2}
\]

Hence **the higher critical pole jet of T_H alone computes both the original lower triangle and its necessary upper-triangle correction**, without equating the earlier Wronskian finite part to the reflection tail (the latter shortcut is already false at p=13).

The *paired* jets of T_H and T_W also determine both first source-rank moments, for each n=n_0+r,

\[
\boxed{
\sum_{\ell-j=n}j\,a_jh_\ell=\frac{D_r-nE_r}{2},\qquad
\sum_{\ell-j=n}\ell\,a_jh_\ell=\frac{D_r+nE_r}{2}.}\tag{B3}
\]

Thus the paired jet is a sufficient carrier for **difference-dependent affine (j,ell) readouts**. It does not reconstruct individual cells or nonlinear future observers. Once E,D are recovered, A1 also calculates the otherwise unobserved simple pole and Laurent finite part: they are *derived* coordinates, not extra independent inputs. Proof: regroup the signed Toeplitz sums by n=ell−j for B1/B2; use j+ell=2j+n=2ell−n for B3. QED.

**Information-loss witness, carefully scoped.** For m≥2, the cells (j,ell)=(m+1,1) and (m+2,2) both have n=−m but have distinct j+ell equal to m+2 and m+4. On an unrestricted labelled-cell carrier, perturbing the two weights by +δ and −δ preserves every E_r and the entire T_H jet, yet changes D_{n=−m} by −2δ. Therefore the product jet alone is not a source-faithful quotient for all affine rank observers. This witness does not assert that the fixed one-parameter hypergeometric family admits arbitrary cell perturbations.

## Exact author verification, non-admission and continuation

The companion stdlib checker constructs original a,h directly, computes both signed triangular sums **independently of reconstructing E**, builds high-pole b,d, inverts them by the displayed *integer* formulas, compares first j moments and both original observers, and recovers the later simple-pole/finite-part coordinates. Results: exact Q arithmetic for m=1,...,15; finite-field arithmetic for **all 80 primes** 7≤p≤997, p≡1 (mod6): PASS.

At m=2, p=13, N=5, the exact product pole coefficients are
\[
(b_0,\ldots,b_4)=
(391/2240,-36229/50400,338683/302400,-343/432,4681/20160).
\]
Inverting gives E=(-1/90,383/2160,139/18900,253/302400,1/6300) at differences n=−3,...,1. Therefore
\[
S_2=-87161/32659200\equiv2\pmod{13},\qquad
C_{\infty,2}=1/630\equiv11\pmod{13}.
\]
The paired W jet recovers the previously known finite part 23/115200, *not* a new FP value.

**BRC: COMPOSE_APPLIED**, with declared future observer scope (difference mass and rank-first moments), signed rank/source provenance, valuation-safe reductions, and exact residual preservation. The bridge is constructive finite algebra rather than a proof of the original CM/JT2 target.

The current Research lane uses only the stable logical ID chatgpt-research-hourly-enterprise-math-20260923; maintenance chatgpt-hourly-enterprise-math-20260921 is separate. A new read-only native D25 continuation call returned INVALID_ARGUMENT / CONTROL_QUOTA. Existing Source reports a durable prior checkpoint but no currently authorized Research run, with the historical predecessor-CLAIM mismatch tracked at enterprise-math issue #1558. This author note grants no Source ownership; no new native CLAIM/OPEN/checkpoint, RA registration, formal Result, review or original-class CM experiment was performed. Existing session/staging and frozen science pin remain untouched.

**Next exact science unit:** apply A4 to the *full corrected Clausen parameter/Hasse differential operator* and low/middle/high p^4 Taylor reflection bridge, check whether second-rank moments remain necessary, and seek a non-tautological signed telescoper. The D25/LIFT/JT2 parent remains OPEN: real same-class H0/B0, divided-power [X]U mod p², Frobenius direction/normalization, kappa mapping, and independent review remain outstanding.