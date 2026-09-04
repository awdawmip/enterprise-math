# Dyadic annihilation filter: uniqueness, closed weights, and stability

Status: `FREE_RESEARCH / TOOL-HARVEST STRENGTHENING / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Parent: `#1159`, `WALLIS_SINE_DYADIC_ANNIHILATION_HIERARCHY_20260904.md`

## 1. Unique maximal-order linear filter

Fix `m>=0`. Consider a linear combination of dyadic samples

\[
L_m f(q)=\sum_{j=0}^{m}w_{m,j}f(2^j q).
\]

To preserve a constant limit and annihilate the first `m` even-power errors, require

\[
\sum_{j=0}^{m}w_{m,j}=1,
\]

and for every `n=1,...,m`,

\[
\sum_{j=0}^{m}w_{m,j}4^{-jn}=0.
\]

This is the interpolation problem of evaluating a polynomial of degree at most `m` at zero from its values at the distinct nodes

\[
x_j=4^{-j},\qquad j=0,...,m.
\]

Hence the weights are unique.

Equivalently, the recursive Richardson operator

\[
\mathcal A_m
=\prod_{r=1}^{m}\frac{4^r\mathcal E-I}{4^r-1}
\]

is the unique `m+1`-sample linear dyadic filter that preserves the constant mode and kills all modes `q^-2,...,q^(-2m)`.

## 2. Closed Lagrange weights

The Lagrange weight at zero is

\[
w_{m,j}
=\prod_{\ell\ne j}\frac{-x_\ell}{x_j-x_\ell}.
\]

Separating `ell<j` and `ell>j` gives

\[
\boxed{
w_{m,j}
=(-1)^{m-j}
\frac{4^{j(j+1)/2}}
{D_jD_{m-j}},
}
\tag{DAF-1}
\]

where

\[
D_s:=\prod_{r=1}^{s}(4^r-1),\qquad D_0:=1.
\]

Examples:

```text
m=1: (-1/3, 4/3)
m=2: (1/45, -4/9, 64/45)
m=3: (-1/2835, 4/135, -64/135, 4096/2835)
```

These coincide with the recursive annihilation hierarchy.

## 3. Exact response on every even-power mode

For `g_n(q)=q^(-2n)`,

\[
L_m g_n
=\lambda_{m,n}g_n,
\]

with

\[
\boxed{
\lambda_{m,n}
=\prod_{r=1}^{m}\frac{4^{r-n}-1}{4^r-1}.
}
\]

Thus the interpolation and refinement-operator descriptions are exactly the same object.

## 4. Absolute-weight sum

Taking absolute values in (DAF-1),

\[
\sum_{j=0}^{m}|w_{m,j}|
=
\frac1{D_m}
\sum_{j=0}^{m}
4^{j(j+1)/2}
\frac{D_m}{D_jD_{m-j}}.
\]

The finite q-binomial identity gives

\[
\sum_{j=0}^{m}
4^{j(j+1)/2}
\frac{D_m}{D_jD_{m-j}}
=
\prod_{r=1}^{m}(4^r+1).
\]

Therefore

\[
\boxed{
\kappa_m
:=\sum_{j=0}^{m}|w_{m,j}|
=
\prod_{r=1}^{m}\frac{4^r+1}{4^r-1}.
}
\tag{DAF-2}
\]

The first values are approximately

```text
m=1  1.6666666667
m=2  1.8888888889
m=3  1.9488536155
m=4  1.9641387419
m=5  1.9679787004
```

and the sequence increases to about `1.96926...`.

## 5. Uniform condition-number bound below two

Write

\[
\frac{4^r+1}{4^r-1}
=1+\frac{2}{4^r-1}.
\]

The first two factors multiply to

\[
\frac53\frac{17}{15}=\frac{17}{9}.
\]

For `r>=3`,

\[
\frac{2}{4^r-1}
<\frac{8}{3}\,4^{-r}.
\]

Hence

\[
\sum_{r=3}^{\infty}\frac{2}{4^r-1}
<\frac1{18}.
\]

Using `log(1+t)<=t`, the remaining product is strictly below `exp(1/18)`. The elementary bound `exp(x)<1/(1-x)` for `0<x<1` gives

\[
\prod_{r=3}^{\infty}\frac{4^r+1}{4^r-1}
<\frac{18}{17}.
\]

Therefore

\[
\boxed{
\kappa_m<\frac{17}{9}\frac{18}{17}=2
\qquad\text{for every }m.
}
\tag{DAF-3}
\]

So the arbitrary-order dyadic annihilation filter has a uniformly bounded `l1` condition number.

## 6. Perturbation stability

Suppose the samples carry perturbations

\[
\widetilde f(2^jq)=f(2^jq)+\varepsilon_j.
\]

Then

\[
|L_m\widetilde f(q)-L_m f(q)|
\le
\sum_{j=0}^{m}|w_{m,j}|\,|\varepsilon_j|.
\]

Consequently

\[
\boxed{
|L_m\widetilde f(q)-L_m f(q)|
<2\max_{0\le j\le m}|\varepsilon_j|.
}
\tag{DAF-4}
\]

Thus increasing extrapolation order does not create an exponentially ill-conditioned numerical combination.

For exact #1159 dyadic nested-radical data this is not needed for correctness, but it is important for executable high-precision implementations.

## 7. Tool extraction

Extend `T5_PRECISION_REFINEMENT` with a generic component:

```text
DYADIC_ANNIHILATION_FILTER(level=m)
  scales: q,2q,...,2^m q
  weights: w_(m,j) from (DAF-1)
  exact annihilation: q^-2 through q^(-2m)
  condition number: kappa_m < 2
```

Specialized #1159 sine/Dirichlet logic then supplies the one-sided alternating error certificate; the filter itself is general.

Freeze:

`MAXIMAL_ORDER_LINEAR_DYADIC_FILTER = UNIQUE_LAGRANGE_EXTRAPOLANT`.

`ALL_LEVELS_CONDITION_NUMBER < 2`.
