# Dirichlet parity as deepest-vs-ancestral decimation generation

Status: `FREE_RESEARCH / EXACT DYADIC FINITE IDENTIFICATION / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on `DIRICHLET_DYADIC_DECIMATION_GENERATION_TREE_20260904.md`.

## 1. Dyadic setup

Let

\[
M=2^m=2q,
\qquad q=2^{m-1},
\]

with `m>=2`.

The complete finite Dirichlet spectrum is partitioned into decimation generations

\[
\operatorname{Roots}(D_{M-1})
=
\bigsqcup_{j=0}^{m-1} Z_j,
\]

where

\[
Z_j=\{u:R^{\circ j}(u)=2\},
\qquad R(u)=u(4-u),
\]

and

\[
|Z_j|=2^j,
\qquad
\prod_{u\in Z_j}u=2.
\]

Under the internal phase-index readout,

\[
u_{k,M}\in Z_{m-1-v_2(k)}.
\]

## 2. Odd mode indices are exactly the deepest generation

For an interior mode index `1<=k<M`,

\[
k\text{ odd}
\iff v_2(k)=0.
\]

Therefore

\[
\boxed{
\{u_{k,M}:k\text{ odd}\}=Z_{m-1}.
}
\tag{PDG-1}
\]

Since every generation has root product `2`,

\[
\boxed{
\prod_{\substack{1\le k<M\\k\text{ odd}}}u_{k,M}=2.
}
\tag{PDG-2}
\]

This is exactly the odd-parity squared-eigenvalue product appearing in WSR-T08.

## 3. Even mode indices are exactly the ancestral generations

Likewise,

\[
k\text{ even}
\iff v_2(k)\ge1.
\]

Hence

\[
\boxed{
\{u_{k,M}:k\text{ even}\}
=
\bigsqcup_{j=0}^{m-2}Z_j.
}
\tag{PDG-3}
\]

The product is therefore

\[
\prod_{\substack{1\le k<M\\k\text{ even}}}u_{k,M}
=
\prod_{j=0}^{m-2}
\left(\prod_{u\in Z_j}u\right)
=
2^{m-1}.
\]

Since `q=2^(m-1)`,

\[
\boxed{
\prod_{\substack{1\le k<M\\k\text{ even}}}u_{k,M}=q.
}
\tag{PDG-4}
\]

This is exactly the even-parity squared-eigenvalue product in WSR-T08.

## 4. Parity ratio is a generation imbalance

The root-product ratio is therefore

\[
\boxed{
\frac{
\prod_{k\text{ even}}u_{k,M}
}{
\prod_{k\text{ odd}}u_{k,M}
}
=
\frac q2.
}
\tag{PDG-5}
\]

The former parity determinant constant `q/2` is thus not an isolated odd/even product trick. For dyadic chains it is the imbalance between

```text
all ancestral decimation generations
versus
the single deepest decimation generation.
```

Every generation carries the same multiplicative root mass `2`; the ratio counts how many such generations sit on the ancestral side.

## 5. Parity-curvature interpretation

WSR-T08 uses the radius observer

\[
\operatorname{Curv}_q
=
\prod_{r=1}^{q-1}
\frac{\rho_{2r}^2}{\rho_{2r-1}\rho_{2r+1}}.
\]

Its squared-eigenvalue core contains precisely the ratio (PDG-5), while the two unsquared odd endpoints supply the complement pair

\[
u_{1,M},\qquad u_{M-1,M}=4-u_{1,M}.
\]

The endpoint correction then produces

\[
\sqrt{u_{1,M}(4-u_{1,M})}
=
\sqrt{R(u_{1,M})},
\]

which is one coarse-mode radius by decimation.

Thus the full collapse

\[
\operatorname{Curv}_q(\rho)
=\frac{\rho_{1,q}}2
\]

has the following finite tree semantics:

```text
ancestral/deepest generation mass ratio
    + complement-paired deepest endpoints
    + one decimation step
    -> coarse fundamental radius / 2.
```

This is a sharper structural reading of WSR-T08.

## 6. Extension to non-pure dyadic lengths

Let a general length be

\[
M=2^m s,
\qquad s\text{ odd}.
\]

Iterating the exact normalized decimation equation gives

\[
\boxed{
H_M(u)
=
\left[
\prod_{j=0}^{m-1}
\left(1-\frac{R^{\circ j}(u)}2\right)
\right]
H_s(R^{\circ m}(u)).
}
\tag{PDG-6}
\]

So every finite Dirichlet spectrum splits into:

1. `m` universal dyadic generations `Z_0,...,Z_(m-1)`;
2. an `m`-fold inverse image of the odd-core spectrum of `H_s`.

For pure dyadic lengths `s=1`, the odd core is trivial and the spectrum is exactly the universal generation tree.

Degree check:

\[
(2^m-1)+2^m(s-1)=M-1.
\]

The universal generation factors contribute root product

\[
2^m,
\]

while the residual odd-core pullback contributes the remaining multiplicative mass `s`, consistent with the total root product `M=2^m s`.

This gives a general `v_2(M)` renormalization decomposition of finite Dirichlet spectra.

## 7. Research consequence

The dyadic parity split is now a special case of a deeper valuation filtration:

\[
\boxed{
\text{MODE PARITY}
=
\text{DEEPEST-vs-ANCESTRAL DECIMATION GENERATION}
\quad(M\text{ dyadic}).
}

The exact products `2` and `q` in WSR-T08 are generation-mass identities.

Freeze:

`ODD_MODES = DEEPEST_DECIMATION_GENERATION`.

`EVEN_MODES = UNION_OF_ANCESTRAL_GENERATIONS`.

`PARITY_PRODUCT_RATIO = GENERATION_MASS_IMBALANCE`.
