# p-adic spectral layer products and the factor-by-factor Viète--Wallis identity

Status: `FREE_RESEARCH / INTERNAL ANALYTIC COMPLETION THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Cross-family relevance: `#1158` Viète finite rotation refinement.
Depends on:
- internal Euler product `F(x)=S(x)/x=prod_k(1-x^2/(k^2 tau^2))`;
- internal double-angle law;
- #1158/#1159 identity `c_j=C(tau/2^(j+1))` for the dyadic radical states.

## 1. Prime-adic layer of Euler modes

For a prime `p` and integer `j>=0`, define the `p`-adic mode layer

\[
\boxed{
\mathcal L_{p,j}(x)
:=
\prod_{\substack{k\ge1\\v_p(k)=j}}
\left(1-\frac{x^2}{k^2\tau^2}\right).
}
\tag{PVW-1}

Every `k` in this layer is uniquely `p^j r` with `p\nmid r`.  Hence

\[
\mathcal L_{p,j}(x)
=
\prod_{p\nmid r}
\left(1-
\frac{(x/p^j)^2}{r^2\tau^2}
\right).
\]

The full product at scale `x/p^j` splits into `p\nmid r` modes and `p|r` modes.  The latter are the full product at scale `x/p^(j+1)`.  Therefore

\[
\boxed{
\mathcal L_{p,j}(x)
=\frac{F(x/p^j)}{F(x/p^{j+1})}.
}
\tag{PVW-2}

Using `F(y)=S(y)/y`,

\[
\boxed{
\mathcal L_{p,j}(x)
=
\frac{S(x/p^j)}{p\,S(x/p^{j+1})}.
}
\tag{PVW-3}

At removable zeros the identity is understood by analytic continuation/power-series cancellation; the product definition itself is entire in the relevant compact regime.

## 2. Telescoping over all p-adic generations

Multiply (PVW-2) for `j=0,...,J`:

\[
\prod_{j=0}^{J}\mathcal L_{p,j}(x)
=
\frac{F(x)}{F(x/p^{J+1})}.
\]

Since

\[
F(y)=S(y)/y\to1
\]

as `y->0`,

\[
\boxed{
F(x)
=
\prod_{j=0}^{\infty}\mathcal L_{p,j}(x).
}
\tag{PVW-4}

Thus the Euler sine product admits a canonical decomposition by `p`-adic valuation of the finite rotation-mode index for every prime `p`.

This is the analytic completion of the finite `p`-adic generation filtration previously derived from the phase-decimation semigroup.

## 3. Dyadic layer collapses to the cosine companion

Set `p=2`.  From the internal double-angle law

\[
S(y)=2S(y/2)C(y/2),
\]

we obtain

\[
\frac{S(y)}{2S(y/2)}=C(y/2).
\]

Therefore (PVW-3) gives

\[
\boxed{
\mathcal L_{2,j}(x)
=C\left(\frac{x}{2^{j+1}}\right).
}
\tag{PVW-5}

In index-shifted form, for `j>=1`,

\[
\boxed{
\prod_{\substack{k\ge1\\v_2(k)=j-1}}
\left(1-\frac{x^2}{k^2\tau^2}\right)
=
C\left(\frac{x}{2^j}\right).
}
\tag{PVW-6}

Consequently

\[
\boxed{
\frac{S(x)}x
=
\prod_{j=1}^{\infty}
C\left(\frac{x}{2^j}\right).
}
\tag{PVW-7}

This is the mode-layer form of the repeated half-angle identity.

## 4. Factor-by-factor Viète--Wallis identity

Set

\[
x=\tau/2.
\]

The internal Euler/Wallis bridge gives

\[
F(\tau/2)=\frac2\tau
=
\prod_{k=1}^{\infty}
\left(1-\frac1{4k^2}\right).
\]

Equation (PVW-6) gives for each `j>=1`

\[
\boxed{
\prod_{\substack{k\ge1\\v_2(k)=j-1}}
\left(1-\frac1{4k^2}\right)
=
C\left(\frac{\tau}{2^{j+1}}\right).
}
\tag{PVW-8}

The #1158 finite radical states are already internally identified with

\[
\boxed{
c_j=C\left(\frac{\tau}{2^{j+1}}\right),\qquad j\ge1.
}
\tag{PVW-9}

Hence

\[
\boxed{
 c_j
=
\prod_{\substack{k\ge1\\v_2(k)=j-1}}
\left(1-\frac1{4k^2}\right).
}
\tag{PVW-10}

Writing `k=2^(j-1)(2r-1)`,

\[
\boxed{
 c_j
=
\prod_{r=1}^{\infty}
\left(1-
\frac1{2^{2j}(2r-1)^2}
\right).
}
\tag{PVW-11}

This is a generation-by-generation identity, not merely equality of the completed constants.

## 5. Reconstruct the full Viète/Wallis product

Multiplying (PVW-10) over `j>=1`, the `2`-adic valuation classes partition every positive integer exactly once.  Therefore

\[
\boxed{
\prod_{j=1}^{\infty}c_j
=
\prod_{k=1}^{\infty}
\left(1-\frac1{4k^2}\right)
=
\frac2\tau.
}
\tag{PVW-12}

The left side is the #1158 Viète half-root product; the middle is inverse Wallis; the right side is the common internal completion readout.

The previous theorem `Pi_rot=tau=2W_infinity` is therefore strengthened to a layerwise correspondence:

\[
\boxed{
\text{VIETE REFINEMENT LEVEL }j
\leftrightarrow
\text{WALLIS/EULER MODE LAYER }v_2(k)=j-1.
}
\tag{PVW-13}

## 6. Finite spectral interpretation

At finite dyadic length `M=2^m`, the previously derived decimation tree partitions the finite roots by the same `2`-adic valuation of their mode indices.  Layer `j` consists of the roots with fixed `v_2(k)` and has root product exactly two.

Thus (PVW-5)--(PVW-13) are not an unrelated reindexing of an infinite product.  They are the analytic completion of the exact finite dyadic spectral-generation partition.

## 7. General prime interpretation

For general `p`, (PVW-3) is the completed `p`-adic layer factor

\[
\mathcal L_{p,j}(x)
=
\frac{S(x/p^j)}{pS(x/p^{j+1})}.
\]

Unlike `p=2`, this quotient does not collapse to the single cosine companion `C`; it is governed by the `p`-fold internal phase multiplication law.

Thus `p=2` is special only because the two-fold phase quotient is exactly one half-angle cosine factor, which admits the nested-square-root refinement used by Viète.

The underlying prime-adic spectral layer decomposition exists uniformly for every prime.

## 8. Scope

No novelty is claimed for classical sine/cosine product identities or for regrouping an absolutely convergent product.  The theorem-candidate strength is the typed finite-to-infinite identification with the previously derived p-adic Dirichlet spectral generations and the exact factor-level bridge to #1158's internal radical states.

Freeze:

`P_ADIC_MODE_LAYER -> SCALE_QUOTIENT F(x/p^j)/F(x/p^(j+1))`.

`DYADIC_MODE_LAYER -> INTERNAL_COSINE_FACTOR`.

`VIETE_FACTOR_j = INVERSE_WALLIS_PRODUCT_OVER_v2(k)=j-1`.

`VIETE_WALLIS_EQUALITY = LAYERWISE, NOT ONLY COMPLETION-WISE`.
