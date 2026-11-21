# R5 — Primitive eighth-root residual: all-threshold order-12 poles and sharp modulus 840

Date: 2026-11-21. Evidence: AUTHOR_EXACT_DERIVATION / EXACT_FINITE_CHECKED / NOT_REVIEWED. Independent portable scientific material only, with no CLAIM/RUN/Result/Review.

## Frozen input and scope

Scientific predecessor: awdawmip/enterprise-math@1482e3a06ae5c2e6a8e18120d3aca48f95645c75:research_notes/portable_direct/r5_seventh_allm_20261121/RESEARCH.md. Reuse the frozen R5 scalar nonadaptive model (256 named hypotheses; prices 214–314; original 32,640-pair separation certificate SHA-256 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b), without reopening the input. The minimal separation sets are

\[
S_0=\{214,\ldots,218\},\quad S_1=\{214,216,\ldots,221\},\quad
S_2=\{215,\ldots,221\},\quad S_3=\{223,\ldots,290\},\quad
S_4=\{296,\ldots,312\}.
\]

For fixed positive integer m, F_m(N) counts nonnegative price-multiplicity vectors of total cost N for which at least one S_i has multiplicity load strictly below m.

## New Theorem A (all thresholds)

Write z for a primitive eighth root of unity (z^4=-1), and set

\[
P_8=\prod_{j=0}^{11}(224+8j),\qquad
H_8(z)=\prod_{\substack{222\le p\le314\\8\nmid p}}(1-z^p)^{-1}.
\]

Define local coefficient L_m(z) by the following exact rational generating function over Q[z]/(z^4+1):

\[
\boxed{\sum_{m\ge1}L_m(z)t^{m-1}=
\frac{\sum_{j=3}^5 c_j(z)\mathcal F(z^6,z^7,z^j;t)}
{(1-t)^2(1-zt)(1-z^2t)} }\tag{1}
\]

where

\[
c_j(z)=\prod_{\ell\in\{3,4,5\}\setminus\{j\}}(1-z^{\ell-j})^{-1}
\]

and

\[
\mathcal F(X,Y,Z;t)=
\frac{1+(1-t)\left[\frac{X}{1-X}+\frac{Y}{1-Y}+\frac{Z}{1-Z}
-\frac{tXY}{1-tXY}-\frac{tXZ}{1-tXZ}-\frac{tYZ}{1-tYZ}
+\frac{t^2XYZ}{1-t^2XYZ}\right]}
{(1-Xt)(1-Yt)(1-Zt)}.\tag{2}
\]

For every positive integer m, L_m(z) is nonzero; all four primitive eighth roots are genuine poles of exact order 12 for the ordinary cost-generating function \(\sum_{N\ge0}F_m(N)x^N\). The coefficient of \((1-x/z)^{-12}\) is \(H_8(z)L_m(z)/P_8\), and consequently

\[
\boxed{F_m^{(8)}(N)=
\frac{N^{11}}{11!P_8}\sum_{\Phi_8(z)=0}H_8(z)L_m(z)z^{-N}
+O_m(N^{10}).}\tag{3}
\]

### Derivation

For each of S_0,S_1,S_2, price 216 is constrained. The remaining twelve multiples of 8 are 224,232,...,312, free for these three events. A term containing S_3 constrains nine of those twelve, and a term containing S_4 constrains three, so all such inclusion–exclusion intersections have order at most ten. Thus only the union of the first three failure events determines the order-12 coefficient.

For local prices 214–221 write a=n_214, b=n_215, v=n_216+n_217+n_218, u=n_219+n_220+n_221. Their failure loads are v+a+b, v+a+u and v+b+u, whose minimum equals v+a+b+u-max(a,b,u). The indicator of minimum < m summed over m>=1 contributes t^(minimum)/(1-t). The v-group and threshold supply \((1-t)^{-2}(1-zt)^{-1}(1-z^2t)^{-1}\). Decompose the u-group rational function into \(\sum_{j=3}^5c_j(z)/(1-z^jw)\); summing the triples a,b,u by their maximum yields (2). These identities are rational identities in the cyclotomic field, requiring no convergence on the complex unit circle. Free nonmultiples above 221 contribute H_8(z); twelve free multiples give the factor P_8^{-1} in the Laurent coefficient. This proves (1) and (3) once nonvanishing is established.

### Threshold recurrence, exact minimum period, nonvanishing

The poles in t of (1) are all 16th roots, of order at most two. The common factor has a double pole at t=1 and single poles at z^-1,z^-2. The additional linear factors come from z^6,z^7,z^j, pair products, and quadratic terms 1-t²z^(13+j) with exponents 1,z,z². A direct comparison shows no denominator collision exceeding order two. For j=3, the quadratic factor 1-t² at t=1 is canceled by the displayed (1-t). The rational function decays at infinity. Therefore its denominator divides (1-t^16)^2 and is strictly proper, establishing

\[
\boxed{L_{m+32}-2L_{m+16}+L_m=0\quad(m\ge1),\quad
L_{r+16k}=C_r+kB_r,\ 1\le r\le16.}\tag{4}
\]

At either primitive 16th root t satisfying t²=z^-1, only the j=4 triple-product factor 1-zt² is singular. Its prefactor c_4(1-t) and all other denominators are nonzero. The pole is genuine; hence the threshold coefficient L_m has **minimal quasi-polynomial period exactly 16**.

The following table is the exact nonvanishing certificate. For m=r+16k, k>=0, the displayed basis coefficient of L_m in \(1,z,z^2,z^3\) equals c+bk, with nonzero c and b of the same sign:

| r | basis | c | b |
|---:|---|---:|---:|
| 1 | 1 | -1/2 | -3 |
| 2 | 1 | 3/2 | 2 |
| 3 | 1 | 9/2 | 7 |
| 4 | 1 | 3 | 4 |
| 5 | 1 | 1 | 1 |
| 6 | z² | 2 | 2 |
| 7 | 1 | -1 | -1 |
| 8 | 1 | -2 | -2 |
| 9 | 1 | -7/2 | -3 |
| 10 | 1 | 3/2 | 2 |
| 11 | 1 | 13/2 | 7 |
| 12 | 1 | 4 | 4 |
| 13 | 1 | 1 | 1 |
| 14 | z | -2 | -2 |
| 15 | 1 | -1 | -1 |
| 16 | 1 | -2 | -2 |

All sixteen affine progressions retain a nonzero coordinate for every k>=0, proving nonvanishing. For example, \(L_1(z)=-(2+3z+4z^2+z^3)/4\).

## New Theorem B (least modulus 840)

For each fixed m>=1, the pinned predecessor established the least cost quasi-polynomial period 420 at remainder O_m(N^11), arising from the genuine harmonics of orders 2–7. All roots of order d>=9 have at most eleven divisible prices in 214–314 (d=9 has eleven; d>=10 has fewer), so their possible pole degrees contribute only O_m(N^10). Theorem A adds a genuine order-eight harmonic of degree 11, without changing the earlier harmonics. Hence

\[
\boxed{F_m(N)=Q_{m,840}(N)+O_m(N^{10}),
\quad\text{least positive cost period }840=\mathrm{lcm}(420,8).}\tag{5}
\]

This is the minimum at the stated asymptotic precision, not the complete exact counting-function period. The 420 predecessor is a pinned author-checked dependency, not an independently admitted theorem.

## Reproducible certificate and observer scope

VERIFY_OCTIC.py works with exact fractions in Q[z]/(z⁴+1), no floating point and no external dependencies. It reconstructs the first 32 coefficients of (1), verifies 48 recurrence instances, independently checks thresholds m=1..12 by event-intersection dynamic programming (not by the maximum formula), and checks all 16 nonzero affine witnesses. OCTIC_RESULT.json contains those exact results. The all-m statements use the rational identity, pole structure, and finite initial coefficients, not sample extrapolation alone.

Cost Fourier phases are retained as a scalar combinatorial observer for the frozen R5 problem. No mapping of these phases to native X6/BRC physical states is claimed; native transport would require its own future-observer preservation proof under P000.

Next: primitive ninth-root classification, including possible new threshold modulus; locate the next precision at which the least cost period must expand beyond 840. Independent review remains pending.
