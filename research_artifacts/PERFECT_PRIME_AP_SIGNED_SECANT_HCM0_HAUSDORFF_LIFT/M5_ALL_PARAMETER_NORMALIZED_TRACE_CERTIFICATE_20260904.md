# Perfect Prime AP HCM0 — m=5 all-parameter normalized trace certificate

Task: `RS-PERFECT-PRIME-AP-SIGNED-SECANT-HCM0-HAUSDORFF-LIFT`  
Publication: `TP2-7A2D91C5E40B836F19D2`  
Researcher: `EM-HCM0-HL-FB0860`  
Recovery claim: `CLM-HCM0HL-RECOVER-20260904T205700`  
Date: 2026-09-04  
Status: **EXACT ALL-PARAMETER m=5 THEOREM — ALL-m M6 / HCM0 REMAIN OPEN**

## 1. Statement

Set `m=5`, `n=4`.  Let the initial actual layer be `S=s0>=0`, and let the two consecutive block lengths satisfy `a>0`, `c>0`. Put

\[
r_0=5S,\qquad r=5(S+a),\qquad s=5(S+a+c).
\]

Normalize the synchronized quotient forms by the trivial gap squares:

\[
\mathcal H_a=(5a)^{-2}Q_{r_0,r},
\qquad
\mathcal H_{a+c}=(5(a+c))^{-2}Q_{r_0,s}.
\]

Then for every real `S>=0`, `a>0`, `c>0`,

\[
\boxed{
\operatorname{tr}(\mathcal H_{a+c}^{-1}\mathcal H_a)>4.
}
\tag{1.1}
\]

Equivalently,

\[
\boxed{
\operatorname{tr}(Q_{r_0,s}^{-1}Q_{r_0,r})
>4\left(\frac{a}{a+c}\right)^2>0.
}
\tag{1.2}
\]

Thus the first dangerous extreme mixed coefficient has the required strict sign for every `m=5` actual three-layer base slice.

## 2. Reduced common-denominator form

For `m=5`,

\[
F(x)=\mu_x^{-1}=\frac1{24}\prod_{k=1}^{5}(5x+k),
\qquad
\Delta^4F(x)=3125(5x+13).
\tag{2.1}
\]

At a terminal moment level `r`, the five moment denominators at `r,r+1,...,r+4` partition the contiguous block `5r+1,...,5r+25`.  Define

\[
L_r=\prod_{k=1}^{25}(5r+k).
\tag{2.2}
\]

Then the leading Pascal/Hausdorff matrix has the polynomial-over-common-denominator form

\[
H_r=L_r^{-1}N_r.
\]

For the later endpoint `s=5(S+a+c)`, the Sherman-Morrison scalar denominator has positive sign because `n=4`:

\[
S_s=\Delta^4F(s)
=3125\,[25(S+a+c)+13]>0.
\tag{2.3}
\]

The normalized translation transition is

\[
V=\overline T_{5a}\,\overline T_{5(a+c)}^{-1}
=\begin{pmatrix}
1&-\frac52c&\frac5{12}c(-5a+5c+3)&\frac5{24}c(5a-2)(5c+2)\\
0&1&-\frac52c&\frac5{12}c(-5a+5c+3)\\
0&0&1&-\frac52c\\
0&0&0&1
\end{pmatrix}.
\tag{2.4}
\]

Using the frozen explicit rank-one inverse numerator for `H_s^{-1}`, one gets

\[
\operatorname{tr}(\mathcal H_{a+c}^{-1}\mathcal H_a)
=\operatorname{tr}(H_s^{-1}V^TH_rV),
\tag{2.5}
\]

with only one scalar denominator `S_s L_r` remaining.

## 3. Positive polynomial certificate

Exact cancellation gives

\[
\boxed{
\operatorname{tr}(\mathcal H_{a+c}^{-1}\mathcal H_a)-4
=
\frac{125\,c\,P_5(a,c,S)}
{36\,[25(S+a+c)+13]\,L_r},
}
\tag{3.1}
\]

where now

\[
L_r=\prod_{k=1}^{25}\bigl(25(S+a)+k\bigr)>0.
\tag{3.2}
\]

The primitive integer polynomial `P_5` has:

- total degree `25`;
- exactly `2460` nonzero monomials;
- all `2460` coefficients strictly positive;
- minimum coefficient `5428515344463249557815296000`;
- maximum coefficient `8031350159976034592546056956052780151367187500`.

Order monomials by SymPy's canonical `Poly(a,c,S).terms()` order and serialize each row as

`deg_a,deg_c,deg_S|coefficient`.

The primitive coefficient table has digest

`sha256:14683660903c78414af80ce45dbc557083ddde381554ce418d8c5ba33a528366`.

The exact rational polynomial before primitive normalization has coefficient content

\[
\frac{390625}{36}=\frac{5^8}{36},
\]

and division by the scalar `3125=5^5` in (2.3) produces the prefactor `125/36` in (3.1).

Since every factor in the denominator is positive on the stated parameter region, (1.1) follows.

## 4. Pattern now visible at m=3,4,5

The full-parameter M6 certificates now exist at

\[
m=3,4,5.
\]

Their positive primitive numerator degrees are respectively

\[
9,16,25=m^2.
\]

This degree pattern aligns with the contiguous common denominator block of length `m^2`:

\[
\prod_{j=0}^{m-1}\prod_{k=1}^{m}(m(r+j)+k)
=\prod_{k=1}^{m^2}(mr+k).
\]

This is evidence for a dimension-free positive-block mechanism, but no all-`m` theorem is claimed from the pattern alone.

## 5. Boundary

Proved here:

- exact all-parameter `m=5` normalized trace inequality;
- a 2460-term positive primitive polynomial certificate;
- the corresponding strict sign of the extreme three-support mixed coefficient.

Still open:

- `M6_ACTUAL_TWO_BLOCK_NEWTON_TRACE_POSITIVITY` for arbitrary `m`;
- all remaining actual three-support coefficients;
- all-support layer sign regularity;
- HCM0 and parent determinant nonvanishing.

The next target is to extract a general positive formula from the contiguous `m^2` denominator block plus the explicit rank-one inverse, rather than continue dimension-by-dimension brute expansion.
