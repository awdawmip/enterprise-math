# Dyadic Dirichlet decimation as a binary spectral-generation tree

Status: `FREE_RESEARCH / EXACT_FINITE_ALGEBRAIC STRENGTHENING / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`

## 1. Normalized spectral continuant

Let

\[
H_q(u):=\frac{D_{q-1}(u)}q,
\]

where

\[
D_0=1,
\quad D_1=2-u,
\quad D_{n+2}=(2-u)D_{n+1}-D_n.
\]

Let

\[
R(u)=u(4-u).
\]

The exact continuant decimation theorem

\[
D_{2n+1}(u)=(2-u)D_n(R(u))
\]

with `n=q-1` gives the normalized functional equation

\[
\boxed{
H_{2q}(u)
=\left(1-\frac u2\right)H_q(R(u)).
}
\tag{DGT-1}
\]

This is an identity of finite polynomials over rational data. No analytic completion is used.

## 2. Exact dyadic generation factorization

Starting from

\[
H_1(u)=1,
\]

iterate (DGT-1). For every `m>=1`,

\[
\boxed{
H_{2^m}(u)
=
\prod_{j=0}^{m-1}
\left(1-\frac{R^{\circ j}(u)}2\right).
}
\tag{DGT-2}
\]

The degree check is automatic:

\[
\sum_{j=0}^{m-1}2^j=2^m-1,
\]

which is exactly the degree of `D_(2^m-1)`.

Thus the whole finite Dirichlet characteristic polynomial is decomposed by decimation generation.

## 3. Binary inverse branches

Solving

\[
R(u)=v
\]

gives

\[
\boxed{
\iota_-(v)=2-\sqrt{4-v},
\qquad
\iota_+(v)=2+\sqrt{4-v}.
}
\tag{DGT-3}
\]

For `0<v<4`, these are two distinct real points in `(0,4)`, one on each side of `2`.

Define generation `j` by

\[
Z_j:=\{u:R^{\circ j}(u)=2\}.
\]

Starting from

\[
Z_0=\{2\},
\]

each generation is obtained by applying both inverse branches to every point of the previous generation.

Therefore

\[
\boxed{|Z_j|=2^j,}
\tag{DGT-4}
\]

and every element of `Z_j` is a distinct real number in `(0,4)`.

## 4. Different generations are disjoint

Suppose `u` belonged to `Z_j` and `Z_l` with `j>l`. Then

\[
R^{\circ l}(u)=2
\]

and applying `R^(j-l)` would require

\[
R^{\circ(j-l)}(2)=2.
\]

But

\[
R(2)=4,
\qquad
R(4)=0,
\qquad
R(0)=0.
\]

Hence no positive iterate of `2` returns to `2`. Therefore

\[
\boxed{Z_j\cap Z_l=\varnothing\quad(j\ne l).}
\tag{DGT-5}
\]

Combining (DGT-2), (DGT-4), and the degree sum shows that the complete dyadic Dirichlet spectrum is exactly

\[
\boxed{
\operatorname{Roots}(D_{2^m-1})
=\bigsqcup_{j=0}^{m-1}Z_j.
}
\tag{DGT-6}
\]

So the spectrum is a binary preimage tree of the distinguished midpoint value `2`.

## 5. Every generation has root product exactly two

For `j=0`,

\[
1-\frac u2
\]

has the single root `2`.

For every `j>=1`, the iterate `R^j` has degree `2^j`, constant term zero, and leading coefficient `-1`. Hence

\[
\Phi_j(u):=1-\frac12R^{\circ j}(u)
\]

has constant coefficient `1`, even degree `2^j`, and leading coefficient `1/2`.

Therefore the product of all roots in generation `j` is

\[
\boxed{
\prod_{u\in Z_j}u=2.
}
\tag{DGT-7}
\]

Consequently the product of all roots of `D_(2^m-1)` is

\[
\prod_{j=0}^{m-1}2=2^m,
\]

recovering the normalization

\[
D_{2^m-1}(0)=2^m
\]

generation by generation.

This gives a new finite explanation for why the normalized determinant has constant value one.

## 6. The shortest root is the all-minus inverse path

The smallest positive point in the binary preimage tree is obtained by always choosing the identity-near inverse branch

\[
v\mapsto2-\sqrt{4-v}.
\]

Starting from `2`,

\[
2
\mapsto
2-\sqrt2
\mapsto
2-\sqrt{2+\sqrt2}
\mapsto\cdots.
\]

Thus for `M=2^m`, the smallest Dirichlet eigenvalue is exactly the depth-`m-1` all-minus path in the full spectral-generation tree.

This recovers WSR-T10 as one distinguished branch of a much larger exact finite object:

\[
\boxed{
\text{nested radical shortest mode}
=
\text{identity-near branch of the full binary decimation tree}.
}
\tag{DGT-8}
\]

## 7. Internal phase conjugacy and 2-adic mode generations

After the internal power-series completion, write the exact mode root as

\[
u_{k,M}=2-2C(k\tau/M).
\]

The double-angle law gives

\[
\boxed{
R(u_{k,M})=u_{2k,M}
}
\tag{DGT-9}
\]

with the phase index understood through the complement symmetry once it passes the midpoint.

For `M=2^m` and `1<=k<M`, write

\[
k=2^{v_2(k)}o,
\qquad o\text{ odd}.
\]

Then the first decimation iterate hitting `2` occurs at

\[
\boxed{
j=m-1-v_2(k).}
\tag{DGT-10}
\]

Indeed

\[
2^j\frac{k\tau}{2^m}
=\frac{o\tau}{2},
\]

and for odd `o`, internal phase addition gives

\[
C(o\tau/2)=0.
\]

Thus

\[
\boxed{
u_{k,2^m}\in Z_{m-1-v_2(k)}.}
\tag{DGT-11}
\]

The generation sizes match the arithmetic count: exactly `2^j` indices in `1,...,2^m-1` have

\[
v_2(k)=m-1-j.
\]

So the dyadic spectral-generation tree is precisely the `2`-adic valuation stratification of the mode indices.

Classification of this section: `INTERNAL_ANALYTIC INDEX READOUT OF EXACT FINITE TREE`.

## 8. Finite determinant / logistic orbit product

Equation (DGT-2) may be read as

\[
\boxed{
\frac{D_{2^m-1}(u)}{2^m}
=
\prod_{j=0}^{m-1}\Phi_j(u),
\qquad
\Phi_j(u)=1-\frac12R^{\circ j}(u).
}
\]

Thus the finite determinant is not merely a product over individual eigenvalues. It is also a product over successive renormalization generations of the spectral parameter itself.

This is an exact finite renormalization identity, not an asymptotic statement.

## 9. Connection to the internal Viète product

Under the internal phase parametrization

\[
u=4S(y)^2,
\]

the decimation dynamics satisfies

\[
R^{\circ j}(u)=4S(2^j y)^2.
\]

Hence

\[
\Phi_j(u)
=1-2S(2^j y)^2
=C(2^{j+1}y).
\]

Therefore the exact finite generation product becomes

\[
H_{2^m}(4S(y)^2)
=
\prod_{j=0}^{m-1}C(2^{j+1}y).
\]

This is the finite doubling-product underlying

\[
S(2^{m+1}y)
=2^mS(2y)
\prod_{j=0}^{m-1}C(2^{j+1}y).
\]

In the small-phase completion limit this is the same scalar mechanism that produces the internal Viète cosine product.

Boundary: this does not identify the #1158 finite orientation carrier with the #1159 Dirichlet matrix carrier.  The bridge is at the scalar refinement/renormalization law.

## 10. Research consequence

The strengthened picture is

```text
finite Dirichlet continuant
    -> exact polynomial renormalization H_(2q)=(1-u/2) H_q(R(u))
    -> dyadic logistic-orbit factorization
    -> binary inverse tree of roots
    -> every generation root-product = 2
    -> v2(mode index) = decimation generation
    -> all-minus path = shortest nested-radical mode
```

Freeze:

`DYADIC_DIRICHLET_SPECTRUM = DISJOINT_LOGISTIC_PREIMAGE_GENERATIONS`.

`GENERATION_ROOT_PRODUCT = 2`.

`DECIMATION_GENERATION = m-1-v2(MODE_INDEX)` for `M=2^m` after internal phase readout.
