# Perfect Prime AP HCM0 — m=4 all-parameter normalized trace certificate

Task: `RS-PERFECT-PRIME-AP-SIGNED-SECANT-HCM0-HAUSDORFF-LIFT`  
Publication: `TP2-7A2D91C5E40B836F19D2`  
Researcher: `EM-HCM0-HL-FB0860`  
Recovery claim: `CLM-HCM0HL-RECOVER-20260904T205700`  
Date: 2026-09-04  
Status: **EXACT ALL-PARAMETER m=4 THEOREM — ALL-m M6 / HCM0 REMAIN OPEN**

## 1. Statement

Set `m=4`, `n=3`.  Let the initial actual layer be

\[
S=s_0\ge0
\]

and let the two consecutive block lengths satisfy

\[
a>0,\qquad c>0.
\]

Put

\[
r_0=4S,\qquad r=4(S+a),\qquad s=4(S+a+c),
\]

and normalize the two synchronized quotient forms by the trivial gap squares:

\[
\mathcal H_a=(4a)^{-2}Q_{r_0,r},
\qquad
\mathcal H_{a+c}=(4(a+c))^{-2}Q_{r_0,s}.
\]

Then

\[
\boxed{
\operatorname{tr}(\mathcal H_{a+c}^{-1}\mathcal H_a)>3
}
\tag{1.1}
\]

for every real `S>=0`, `a>0`, `c>0`.  In particular this holds for every actual integer three-layer configuration.

Equivalently,

\[
\boxed{
\operatorname{tr}(Q_{r_0,s}^{-1}Q_{r_0,r})
>3\left(\frac{a}{a+c}\right)^2>0.
}
\tag{1.2}
\]

Thus the first dangerous extreme mixed coefficient has the required strict sign for every `m=4` actual three-layer base slice.

## 2. Reduced exact computation

The computation is performed after removing the large common moment denominator, rather than by expanding raw rational matrices.

For `m=4`,

\[
F(x)=\mu_x^{-1}=\frac1{6}\prod_{k=1}^{4}(4x+k),
\qquad
\Delta^3F(x)=128(8x+17).
\tag{2.1}
\]

For a terminal level `r`, define

\[
L_r=\prod_{k=1}^{16}(4r+k).
\tag{2.2}
\]

Because the four moment denominators at `r,r+1,r+2,r+3` partition the contiguous block `4r+1,...,4r+16`, the leading Pascal/Hausdorff matrix can be written as

\[
H_r=L_r^{-1}N_r
\]

with polynomial matrix `N_r`.

Use the frozen rank-one inverse formula for the later matrix.  Since `n=3`, its scalar Sherman-Morrison denominator is

\[
S_s=-\Delta^3F(s)
=-128\,[32(S+a+c)+17]<0.
\tag{2.3}
\]

The normalized translation transition is

\[
V=\overline T_{4a}\,\overline T_{4(a+c)}^{-1}
=\begin{pmatrix}
1&-2c&\dfrac{c(-4a+4c+3)}3\\
0&1&-2c\\
0&0&1
\end{pmatrix},
\tag{2.4}
\]

where `Tbar_M=M^{-1}T_M` and `det Tbar_M=1`.

Therefore

\[
\operatorname{tr}(\mathcal H_{a+c}^{-1}\mathcal H_a)
=\operatorname{tr}(H_s^{-1}V^TH_rV).
\tag{2.5}
\]

Substituting the explicit inverse numerator and `H_r=N_r/L_r` yields a single reduced polynomial numerator; no symbolic matrix inverse is required.

## 3. Positive polynomial certificate

After exact cancellation one obtains

\[
\boxed{
\operatorname{tr}(\mathcal H_{a+c}^{-1}\mathcal H_a)-3
=
\frac{1024\,c\,P_4(a,c,S)}
{9\,[32(S+a+c)+17]\,L_r},
}
\tag{3.1}
\]

where

\[
L_r=\prod_{k=1}^{16}\bigl(16(S+a)+k\bigr)>0.
\tag{3.2}
\]

The primitive integer polynomial `P_4` has:

- total degree `16`;
- exactly `804` nonzero monomials;
- all `804` coefficients strictly positive;
- minimum coefficient `163214609191200`;
- maximum coefficient `15223190061789668997857280`.

Order monomials by SymPy's canonical `Poly(a,c,S).terms()` order and serialize each row as

`deg_a,deg_c,deg_S|coefficient`.

The resulting primitive coefficient table has digest

`sha256:d3f4ab2e04dc270de37880c853a6a9454f5a534e6da8b767c4ee42c26c7b50ae`.

Every factor in the denominator of (3.1) is positive on `S>=0`, `a,c>0`, hence (1.1) follows.

## 4. Why the sign correction matters

Before extracting the sign of the Sherman-Morrison denominator, the reduced numerator is divisible by `c` and every one of its `804` coefficients is negative.  This is not a failure: the unreoriented denominator contains

\[
S_s=-128[32(S+a+c)+17]<0.
\]

Multiplying numerator and denominator by `-1` gives exactly the positive certificate (3.1).  This sign is checked symbolically, not inferred numerically.

## 5. Boundary and significance

Together with the preceding `m=3` all-parameter certificate, M6 is now proved exactly for the first two nontrivial quotient dimensions:

\[
m=3\;(n=2),\qquad m=4\;(n=3).
\]

The result is not a finite parameter scan.  It covers every initial layer and every pair of positive block lengths for `m=4`.

It does **not** establish `M6_ACTUAL_TWO_BLOCK_NEWTON_TRACE_POSITIVITY` for arbitrary `m`, the remaining three-support coefficients, HCM0, or parent determinant nonvanishing.

The next research target is to run the same reduced common-denominator / explicit-inverse derivation at `m=5` and identify a dimension-free source for the observed positive coefficient cone, rather than relying on raw symbolic expansion.
