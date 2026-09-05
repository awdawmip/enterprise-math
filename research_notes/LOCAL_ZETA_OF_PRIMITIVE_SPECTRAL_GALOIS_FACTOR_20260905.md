# Local zeta factors of primitive spectral Galois components

Status: `FREE_RESEARCH / EXACT GOOD-PRIME LOCAL-ZETA THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- native primitive spectral Galois action;
- good-prime Frobenius factorization theorem.

## 1. Primitive irreducible component

Fix one irreducible primitive spectral component `F_d(u)`:

- for even `d`, take `F_d=Psi_d`, with degree `r=phi(d)`;
- for odd `d>1`, take either `F_d=Psi_d^E` or `Psi_d^O`, with degree `r=phi(d)/2`.

Its native Galois group is

\[
G_d=(\mathbb Z/2d\mathbb Z)^\times/\{\pm1\}
\]

and

\[
|G_d|=r.
\]

## 2. Good-prime Frobenius order

Let `ell` be prime with

\[
\ell\nmid2d.
\]

Define

\[
\boxed{
f=f_d(\ell)
=\operatorname{ord}_{G_d}(\ell)
=\min\{a\ge1:\ell^a\equiv\pm1\pmod{2d}\}.
}
\tag{LZF-1}

The good-prime factorization theorem gives

\[
F_d\bmod\ell
=\prod_{j=1}^{r/f}f_j
\]

with distinct irreducible factors `f_j`, all of degree `f`.

## 3. Point count over finite extensions

Let `X_(d,ell)` be the zero-dimensional reduced scheme

\[
\operatorname{Spec}(\mathbb F_\ell[u]/(\overline{F_d})).
\]

One irreducible degree-`f` factor contributes all `f` of its geometric roots to `F_(ell^m)` iff `f|m`, and contributes none otherwise.

There are `r/f` such factors.  Therefore

\[
\boxed{
N_m:=|X_{d,\ell}(\mathbb F_{\ell^m})|
=\begin{cases}
r,&f\mid m,\\0,&f\nmid m.
\end{cases}}
\tag{LZF-2}

The point-count sequence is thus a pure periodic divisibility signal determined by the finite phase-Frobenius order.

## 4. Exact local zeta function

Define the local zeta function of this finite scheme by

\[
Z_{d,\ell}(T)
:=\exp\left(
\sum_{m\ge1}\frac{N_m}{m}T^m
\right).
\]

Using (LZF-2),

\[
\sum_{m\ge1}\frac{N_m}{m}T^m
=
\frac rf\sum_{j\ge1}\frac{T^{fj}}j
=-\frac rf\log(1-T^f).
\]

Hence

\[
\boxed{
Z_{d,\ell}(T)
=(1-T^f)^{-r/f}.
}
\tag{LZF-3}

At the arithmetic specialization `T=ell^(-s)`,

\[
\boxed{
Z_{d,\ell}(\ell^{-s})
=(1-\ell^{-fs})^{-r/f}.
}
\tag{LZF-4}

This is the usual unramified local factor of the corresponding finite Galois spectral field, derived directly from finite-field phase dynamics.

## 5. Character factorization

Let `G=G_d`, and let

\[
\sigma_\ell\in G
\]

be the native phase automorphism induced by `R_ell`.  Its order is `f`.

The characters of the finite abelian group `G` diagonalize the regular representation.  Hence

\[
\det(1-T\sigma_\ell\mid\mathbb C[G])
=\prod_{\chi\in\widehat G}(1-\chi(\sigma_\ell)T).
\]

An element of order `f` acts in the regular representation with every `f`-th root eigenvalue repeated `r/f` times.  Therefore

\[
\boxed{
\prod_{\chi\in\widehat G}
(1-\chi(\sigma_\ell)T)
=(1-T^f)^{r/f}.
}
\tag{LZF-5}

Taking reciprocals,

\[
\boxed{
Z_{d,\ell}(T)
=
\prod_{\chi\in\widehat G}
(1-\chi(\sigma_\ell)T)^{-1}.
}
\tag{LZF-6}

Thus the local spectral zeta factor decomposes exactly into one-dimensional Galois-character Euler factors.

## 6. Relation to character-weighted rotation modes

The earlier signed/complex finite mode atlas used characters of the primitive phase automorphism group and produced Gauss-type traces.  The native Galois theorem identified those phase characters with characters of `G_d`.

The present theorem shows that the same characters control good-prime Euler factors:

```text
character chi of finite phase/Galois group
    -> signed finite primitive mode coordinate
    -> Frobenius eigenvalue chi(sigma_ell)
    -> local factor (1-chi(sigma_ell) ell^(-s))^(-1)
```

Hence the finite signed-amplitude channel and the arithmetic local-L channel are two uses of one character coordinate system.

## 7. Odd denominator full algebra

For odd `d`, the full primitive algebra is the product of the `E` and `O` Galois fields.  Their good-prime decomposition types are identical, so the local zeta function of the full product algebra is

\[
\boxed{
(1-T^f)^{-\varphi(d)/f},
}
\tag{LZF-7}

namely the product of the two orientation-component local zeta factors.

The reflection sign remains an independent channel even though the unsigned local factor recoalesces the two components.

## 8. Global compatibility boundary

Multiplying the good-prime local factors and adding the finitely many ramified factors gives the Dedekind zeta function of the corresponding primitive spectral field/component.  In the later classical compatibility layer, the Galois characters become the appropriate even Dirichlet characters and the one-dimensional factors become Dirichlet/Artin L-functions.

No new zero-free region, functional equation, RH or GRH conclusion is claimed from this factorization alone.

## 9. Interpretation

The phase polynomial `R_ell` now has one continuous chain of roles:

```text
characteristic zero:
    native Galois automorphism sigma_ell

mod ell at a good prime:
    arithmetic Frobenius alpha -> alpha^ell

finite-field orbit:
    irreducible factor degree f

point counts:
    N_m = r * 1_(f|m)

local zeta:
    (1-T^f)^(-r/f)

character decomposition:
    product_chi (1-chi(sigma_ell)T)^(-1)
```

Freeze:

`GOOD_PRIME_LOCAL_ZETA = PHASE-FROBENIUS ORBIT ZETA`.

`GALOIS CHARACTER CHANNELS = LOCAL EULER-FACTOR EIGENCHANNELS`.
