# Perfect Prime AP HCM0 — actual-layer Pascal/Hausdorff normal form

Task: `RS-PERFECT-PRIME-AP-SIGNED-SECANT-HCM0-HAUSDORFF-LIFT`  
Publication: `TP2-7A2D91C5E40B836F19D2`  
Researcher: `EM-HCM0-HL-FB0860`  
Claim: `CLM-HCM0HL-6F8E2D4389B17C04A521`  
Date: 2026-09-04  
Status: **NONTERMINAL ALL-m STRUCTURAL THEOREM — HCM0 REMAINS OPEN**

## 1. The arithmetic feature lost by the false arbitrary-shift extension

The actual Cauchy shifts are

\[
c_s=b s=m^2s,
\qquad s=0,1,\ldots,n,
\qquad n=m-1.
\]

The arbitrary-shift three-support conjecture is false, but the actual spacing has two exact structures simultaneously:

1. polynomial translation by one layer is an **integer translation by `m`** after scaling the interpolation nodes `Y_j=mj` to `j`;
2. the diagonal quadrature weights move by an exact **Hausdorff moment index shift of `m`**.

These two facts are frozen below as the actual-layer normal form.

## 2. Exact semigroup for interpolation transfer

For a polynomial `f`, put

\[
\phi(z)=f(mz),
\]

and represent `\phi` by its values on the integer nodes

\[
0,1,\ldots,n.
\]

Let `R_M` be the exact polynomial-translation matrix on this value space:

\[
(R_M y)_i=\phi(i+M)
\]

when `y_j=\phi(j)`. Equivalently, if `\lambda_j` is the Lagrange basis on `0,...,n`,

\[
R_M(i,j)=\lambda_j(i+M).
\]

Then

\[
R_MR_N=R_{M+N},
\qquad R_0=I.
\tag{2.1}
\]

The pure-shift interpolation matrix from the previous checkpoint satisfies

\[
P_{c_s}(i,j)=\lambda_j\!\left(-ms-\frac{i+1}{m}\right).
\]

Therefore exactly

\[
\boxed{P_{c_s}=P_0R_{-ms}.}
\tag{2.2}
\]

For two actual layers `s_e,s_d`,

\[
\boxed{
P_{c_{s_d}}^{-1}P_{c_{s_e}}
=R_{m(s_d-s_e)}.
}
\tag{2.3}
\]

No approximation or large-spacing limit is used.

## 3. Exact Hausdorff shift of the right quadrature weights

Recall

\[
F_j(c)=\frac{n!}{\prod_{i=0}^{n}(i+1+c+mj)}.
\]

It also has the beta-integral form

\[
F_j(c)=\int_0^1 u^{c+mj}(1-u)^n\,du.
\tag{3.1}
\]

Define the positive sequence

\[
\mu_r=F_r(0)
=\frac{n!}{\prod_{i=0}^{n}(i+1+mr)}.
\]

For an actual shift `c_s=m^2s`,

\[
\boxed{F_j(c_s)=\mu_{j+ms}.}
\tag{3.2}
\]

After `v=u^m`,

\[
\mu_r=\int_0^1v^r\,d\nu_m(v),
\]

with strictly positive density

\[
d\nu_m(v)
=\frac1m v^{1/m-1}(1-v^{1/m})^n\,dv
\quad(0<v<1).
\tag{3.3}
\]

Hence `mu` is a strict Hausdorff moment sequence:

\[
\boxed{
(-1)^k\Delta^k\mu_r
=\int_0^1v^r(1-v)^k\,d\nu_m(v)>0
}
\tag{3.4}
\]

for every `r,k>=0`.

The signed diagonal form is therefore

\[
D_{c_s}
=\operatorname{diag}\left(
(-1)^j\binom nj\mu_{j+ms}
\right)_{j=0}^{n}.
\tag{3.5}
\]

## 4. Exact actual-layer quotient form

The signed quadrature identity gives

\[
D_c=P_c^TA_cP_c,
\qquad
A_c=P_c^{-T}D_cP_c^{-1}.
\]

For `s_d>s_e`, let

\[
M=m(s_d-s_e)\ge m=n+1.
\]

Starting from

\[
Q_{c_{s_e},c_{s_d}}
=(P_{c_{s_e}}-P_{c_{s_d}})^TA_{c_{s_d}}
(P_{c_{s_e}}-P_{c_{s_d}}),
\]

use (2.3) to obtain the exact value-space normal form

\[
\boxed{
Q_{c_{s_e},c_{s_d}}
=(R_M-I)^TD_{c_{s_d}}(R_M-I)
}
\tag{4.1}
\]

on the quotient by constants.

Thus every actual quotient form is controlled by only:

- an integer extrapolation difference `R_M-I`, with `M` a positive multiple of `m`;
- one shifted strict Hausdorff moment diagonal (3.5);
- the fixed alternating binomial signature `(-1)^j binom(n,j)`.

This is strictly stronger structure than arbitrary nonnegative Cauchy shifts possess.

## 5. Pascal total nonnegativity of the translation-difference map

Use the Newton basis

\[
\binom zk,\qquad k=0,1,\ldots,n.
\]

For integer `M>=1`, Vandermonde's identity gives

\[
\binom{z+M}{r}-\binom zr
=\sum_{a=1}^{r}\binom Ma\binom z{r-a}.
\]

After quotienting constants, the map

\[
\Delta_M:\mathbb P_n/\mathbf1\to\mathbb P_{n-1}
\]

has the `n x n` upper-triangular Toeplitz matrix

\[
\boxed{
T_M[k,r-1]=
\begin{cases}
\binom M{r-k},&k<r,\\
0,&k\ge r,
\end{cases}
\qquad 0\le k\le n-1,\ 1\le r\le n.
}
\tag{5.1}
\]

Its diagonal is `M`, hence

\[
\det T_M=M^n>0.
\tag{5.2}
\]

Moreover `T_M` is a row/column submatrix of the upper-triangular Toeplitz matrix

\[
\mathcal P_M(i,j)=\binom M{j-i}.
\]

But

\[
\mathcal P_M=(I+N)^M,
\]

where `N` is the one-superdiagonal shift. The bidiagonal matrix `I+N` is totally nonnegative, products of totally nonnegative matrices remain totally nonnegative by Cauchy–Binet, and every submatrix inherits total nonnegativity. Therefore

\[
\boxed{T_M\text{ is totally nonnegative for every integer }M\ge1.}
\tag{5.3}
\]

For the actual layers, `M=m(s_d-s_e)>=m`, so this applies uniformly in `m`.

## 6. New minimal form of the three-layer problem

Equations (3.5), (4.1), and (5.1) convert the actual three-layer base-`m` slice into a **signed Pascal/Hausdorff pencil**.

The positive ingredients are now explicit:

1. `T_M` is totally nonnegative;
2. `mu_r` is a strict Hausdorff moment sequence;
3. layer change shifts the moment index by exactly `m`;
4. all non-positivity is isolated in the fixed alternating signature
   `J=diag((-1)^j)`.

The remaining load-bearing question is not generic Cauchy-shift sign regularity. It is:

`M4_SIGNED_PASCAL_HAUSDORFF_MIXED_DISCRIMINANT`:

> determine whether the fixed alternating binomial signature, when sandwiched between the actual integer-translation Pascal maps and the shifted Hausdorff moment diagonals above, has the required mixed-determinant signs for every layer triple and every `m`.

This is compatible with the exact `m=7` arbitrary-shift obstruction: small non-block shifts do not give the integer `M=m r` / moment-index `j+ms` alignment used here.

## 7. Boundary

Proved all-`m` here:

- actual-layer interpolation semigroup (2.2)–(2.3);
- strict Hausdorff moment shift (3.2)–(3.4);
- quotient normal form (4.1);
- Pascal total nonnegativity (5.3).

Still open:

- the signed Pascal/Hausdorff mixed-discriminant theorem;
- full actual-layer all-support sign regularity;
- HCM0;
- parent determinant nonvanishing.

No Result-ID is frozen.
