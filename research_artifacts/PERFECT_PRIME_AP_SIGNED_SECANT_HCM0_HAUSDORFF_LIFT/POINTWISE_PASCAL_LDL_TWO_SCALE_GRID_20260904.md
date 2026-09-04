# Perfect Prime AP HCM0 — pointwise Pascal LDL and two-scale actual grid

Task: `RS-PERFECT-PRIME-AP-SIGNED-SECANT-HCM0-HAUSDORFF-LIFT`  
Publication: `TP2-7A2D91C5E40B836F19D2`  
Researcher: `EM-HCM0-HL-FB0860`  
Claim: `CLM-HCM0HL-6F8E2D4389B17C04A521`  
Date: 2026-09-04  
Status: **NONTERMINAL ALL-m STRUCTURAL THEOREM — HCM0 REMAINS OPEN**

## 1. Pointwise Pascal kernel

Put `n=m-1` and let

\[
\mathcal P_n(r,k)=\binom rk,
\qquad 0\le r,k\le n,
\]

be the square lower Pascal matrix. For `0<v<1` define

\[
K_n(v)=\mathcal P_n^T
\operatorname{diag}\left((-1)^r\binom nr v^r\right)_{r=0}^{n}
\mathcal P_n.
\tag{1.1}
\]

Equivalently, since `binom(r,a)` is the coefficient of `x^a` in `(1+x)^r`,

\[
\sum_{a,b=0}^{n}K_n(v)_{ab}x^ay^b
=\sum_{r=0}^{n}(-1)^r\binom nr v^r(1+x)^r(1+y)^r
=\bigl(1-v(1+x)(1+y)\bigr)^n.
\tag{1.2}
\]

## 2. Exact all-n LDL factorization

Define the unit lower triangular matrix

\[
L_n(v)_{a,j}
=\binom{n-j}{a-j}
\left(\frac{v}{v-1}\right)^{a-j}
\qquad(0\le j\le a\le n),
\tag{2.1}
\]

and the diagonal matrix

\[
D_n(v)_{j,j}
=(-1)^j\binom nj v^j(1-v)^{n-2j}.
\tag{2.2}
\]

### Theorem 2.1

For every `n>=1` and `0<v<1`,

\[
\boxed{K_n(v)=L_n(v)D_n(v)L_n(v)^T.}
\tag{2.3}
\]

### Proof

The generating polynomial of column `j` of `L_n(v)` is

\[
\ell_j(x)
=\sum_{a=j}^{n}L_n(v)_{a,j}x^a
=x^j\left(1+\frac{v}{v-1}x\right)^{n-j}.
\]

Hence the bivariate generating polynomial of the right side of (2.3) is

\[
\sum_{j=0}^{n}D_j\ell_j(x)\ell_j(y).
\]

Set `t=v/(v-1)`. This becomes

\[
\sum_{j=0}^{n}\binom nj
\left[(1-v)(1+tx)(1+ty)\right]^{n-j}
\left[-\frac{vxy}{1-v}\right]^j.
\]

By the binomial theorem it equals

\[
\left((1-v)(1+tx)(1+ty)-\frac{vxy}{1-v}\right)^n.
\]

A direct simplification using `t=-v/(1-v)` gives

\[
\left(1-v(1+x)(1+y)\right)^n,
\]

which is exactly (1.2). ∎

## 3. Closed leading-principal-minor formula

Because `L_n(v)` is unit lower triangular, the leading `k x k` principal determinant is the product of `D_0,...,D_{k-1}`. Therefore, for `1<=k<=n+1`,

\[
\boxed{
\det K_n(v)[0{:}k,0{:}k]
=(-1)^{k(k-1)/2}
\left(\prod_{j=0}^{k-1}\binom nj\right)
 v^{k(k-1)/2}
 (1-v)^{k(n-k+1)}.
}
\tag{3.1}
\]

In particular all these minors are nonzero on `0<v<1`, and the pointwise inertia is fixed with alternating diagonal signs in the explicit LDL coordinates. No numerical spectral premise is used.

## 4. Matrix-valued Hausdorff representation of the actual right form

From the preceding actual-layer checkpoint,

\[
\mu_r=\int_0^1v^r\,d\nu_m(v),
\qquad
 d\nu_m(v)=\frac1m v^{1/m-1}(1-v^{1/m})^n\,dv.
\]

For layer `s`, define

\[
D_s=\operatorname{diag}\left((-1)^r\binom nr\mu_{r+ms}\right)_{r=0}^{n}.
\]

Then in the Newton/Pascal basis

\[
\boxed{
\mathcal H_s:=\mathcal P_n^TD_s\mathcal P_n
=\int_0^1 v^{ms}K_n(v)\,d\nu_m(v).
}
\tag{4.1}
\]

Thus the actual signed quadrature form is an exact matrix-valued Hausdorff moment of a pointwise kernel whose entire leading flag has the closed sign law (3.1).

If `K_n^{<n}(v)` denotes the leading `n x n` block, and `T_M` is the Pascal translation-difference matrix from the preceding checkpoint, the actual quotient form is

\[
\boxed{
Q_{c_{s_e},c_{s_d}}
=T_M^T
\left(\int_0^1 v^{ms_d}K_n^{<n}(v)\,d\nu_m(v)\right)
T_M,
\qquad M=m(s_d-s_e).
}
\tag{4.2}
\]

The unresolved mixed-discriminant problem is therefore an integral mixture of explicit Pascal conjugates of the pointwise LDL kernel, not an arbitrary symmetric-matrix pencil.

## 5. Exact one-dimensional coding of the actual atom lattice

The actual atom coordinates satisfy

\[
z_{j,s}=mj+m^2s=m(j+ms).
\]

Set

\[
k=j+ms.
\]

Because `0<=j,s<=m-1`, the map

\[
(j,s)\longmapsto k
\]

is a bijection from the `m x m` atom lattice onto

\[
\{0,1,\ldots,m^2-1\}.
\]

Moreover the accepted positive Cauchy/Beta factor collapses to the same Hausdorff moment sequence:

\[
\boxed{
c_{j,s}
=\frac{n!}{\prod_{r=1}^{m}(mj+m^2s+r)}
=\frac{n!}{\prod_{r=1}^{m}(mk+r)}
=\mu_k.}
\tag{5.1}
\]

The remaining digit sign/binomial factor is exactly the coefficient of a two-scale finite-difference polynomial:

\[
\boxed{
(-1)^{j+s}\binom nj\binom ns
=[x^{j+ms}]\,(1-x)^n(1-x^m)^n.}
\tag{5.2}
\]

So the actual signed atom system is not merely `m^2`-spaced. It is a one-dimensional strict Hausdorff moment sequence sampled with the **two-scale difference mask**

\[
(1-x)^n(1-x^m)^n.
\]

This structure is absent from the arbitrary-shift counterexample `(0,2,5)`.

## 6. Consequence for the next proof target

The unresolved all-support sign problem can now be stated without generic Cauchy language:

`M5_TWO_SCALE_HAUSDORFF_PASCAL_REGROUPING`:

> Starting from the strict Hausdorff moments `mu_k`, the totally nonnegative integer translation matrices `T_{mr}`, the pointwise Pascal LDL (2.3), and the two-scale mask `(1-x)^n(1-x^m)^n`, construct a sign-preserving regrouping of every actual mixed determinant cell, or isolate the first exact cell where such regrouping fails.

A positive theorem at this level would strictly subsume the already proved two-support theorem and the finite triple-support evidence while using the actual arithmetic feature that survives the arbitrary-shift obstruction.

## 7. Boundary

Proved all-`m` here:

1. the pointwise Pascal kernel generating formula;
2. the explicit LDL factorization (2.3);
3. the closed leading-principal-minor formula (3.1);
4. the matrix-valued Hausdorff representation (4.1)–(4.2);
5. the actual atom bijection `k=j+ms`, moment collapse `c_{j,s}=mu_k`, and two-scale difference mask (5.2).

Still open:

- sign-preserving regrouping for arbitrary actual supports;
- HCM0;
- all-`m` full shifted HCM;
- parent determinant nonvanishing.

No Result-ID is frozen.
