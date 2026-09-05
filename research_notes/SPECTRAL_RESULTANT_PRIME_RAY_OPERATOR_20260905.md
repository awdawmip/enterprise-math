# Prime-ray operator encoded by primitive spectral resultants

Status: `FREE_RESEARCH / EXACT FINITE-ARITHMETIC OPERATOR THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- native primitive spectral resultant law;
- primitive endpoint-mass law;
- ordinary arithmetic Dirichlet-convolution readout only after the finite kernel is established.

## 1. Prime-specific normalized resultant kernel

For a prime `p` and `2<=m<n`, define

\[
K_p(m,n)
:=\frac1{\varphi(m)}
 v_p\left(|\operatorname{Res}(\Psi_m,\Psi_n)|\right).
\]

The native resultant theorem says

\[
|\operatorname{Res}(\Psi_m,\Psi_n)|
=\begin{cases}
p^{\varphi(m)},&n/m=p^a,\ a\ge1,\\1,&\text{otherwise}.
\end{cases}
\]

Therefore

\[
\boxed{
K_p(m,n)=\mathbf 1_{\{n=mp^a,\ a\ge1\}}.
}
\tag{PRO-1}
\]

Every `K_p` is thus a pure `p`-adic reachability kernel on the divisibility poset.

## 2. Virtual level one from endpoint mass

There is no nontrivial primitive polynomial `Psi_1`, but the missing `m=1` row is supplied exactly by primitive endpoint mass:

\[
|\Psi_n(0)|
=\begin{cases}p,&n=p^a,\\1,&\text{otherwise}.
\end{cases}
\]

Set

\[
K_p(1,n):=v_p|\Psi_n(0)|.
\]

Then the same formula holds for every `1<=m<n`:

\[
\boxed{K_p(m,n)=\mathbf 1_{\{n=mp^a,\ a\ge1\}}.}
\tag{PRO-2}
\]

The endpoint mass is therefore the exact spectral boundary datum completing the prime-ray kernel at level one.

## 3. One-step prime shift and reachability resolvent

For arithmetic functions `f`, define the one-step `p`-shift

\[
(S_pf)(n)
:=\begin{cases}
f(n/p),&p\mid n,\\0,&p\nmid n.
\end{cases}
\]

Then `S_p^a` has kernel `1_(n=mp^a)`.  Hence, on finitely supported functions or pointwise at any fixed `n`,

\[
\boxed{
K_p
=\sum_{a\ge1}S_p^a
=S_p(I-S_p)^{-1}
}
\tag{PRO-3}
\]

in the formal locally finite sense.

So the normalized primitive spectral resultant is the reachability resolvent of one prime direction.

## 4. Von Mangoldt convolution

The von Mangoldt function satisfies

\[
\Lambda(p^a)=\log p,
\qquad
\Lambda(n)=0
\]

outside prime powers. Therefore ordinary Dirichlet convolution by `Lambda` has the operator decomposition

\[
\boxed{
(\Lambda*f)
=
\sum_p(\log p)
\sum_{a\ge1}S_p^a f.
}
\tag{PRO-4}
\]

Using the spectral kernel,

\[
\boxed{
(\Lambda*f)(n)
=\sum_{m\mid n}
\left[
\frac{1}{\varphi(m)}
\log R(m,n)
\right]f(m),
}
\tag{PRO-5}
\]

where for `m>=2`, `R(m,n)=|Res(Psi_m,Psi_n)|`, while the `m=1` boundary value is `R(1,n):=|Psi_n(0)|`; diagonal entries are interpreted as zero log-weight.

The logarithm is a derived readout of the already exact integer prime-specific kernel (PRO-2).

## 5. Dirichlet-series multiplier

If

\[
F(s)=\sum_{n\ge1}\frac{f(n)}{n^s}
\]

converges absolutely, then

\[
\mathcal D(S_pf)(s)=p^{-s}F(s).
\]

Thus (PRO-4) becomes

\[
\mathcal D(\Lambda*f)(s)
=
\left(
\sum_p(\log p)\frac{p^{-s}}{1-p^{-s}}
\right)F(s).
\]

In `Re(s)>1`, the multiplier is the standard logarithmic derivative

\[
\boxed{
\sum_p(\log p)\frac{p^{-s}}{1-p^{-s}}
=-\frac{\zeta'(s)}{\zeta(s)}.
}
\tag{PRO-6}
\]

Hence `-zeta'/zeta` is the Dirichlet-transform image of the finite primitive-spectral resultant reachability operator.

This is an interface theorem; no new zero-free region or RH statement is claimed.

## 6. Prime factorization from the resultant neighborhood

For fixed `n`, each prime `p` contributes one unit of `p`-adic valuation for every lower divisor

\[
m=n/p^a\ge2,
\]

and if the chain reaches `m=1` the final contribution is supplied by endpoint mass. Therefore

\[
\boxed{
 v_p(n)
= v_p|\Psi_n(0)|
+\sum_{\substack{m\mid n\\2\le m<n}}
\frac1{\varphi(m)}
 v_p|\operatorname{Res}(\Psi_m,\Psi_n)|.
}
\tag{PRO-7}
\]

Exponentiating over primes gives

\[
\boxed{
 n
=|\Psi_n(0)|
\prod_{\substack{m\mid n\\2\le m<n}}
|\operatorname{Res}(\Psi_m,\Psi_n)|^{1/\varphi(m)}.
}
\tag{PRO-8}
\]

Thus ordinary prime factorization is reconstructed by the primitive spectral resultant neighborhood plus its endpoint boundary mass.

## 7. Mass versus depth provenance

A key typing distinction appears on every prime ray:

\[
\frac1{\varphi(m)}
\log|\operatorname{Res}(\Psi_m,\Psi_{mp^a})|
=\log p
\]

for every `a>=1`.  The normalized resultant mass does not distinguish a one-step jump `p` from a deeper jump `p^a`.

That is exactly appropriate for `Lambda`, because `Lambda(p^a)=log p` is depth-blind.

By contrast, the Euler logarithm

\[
\log\zeta(s)=\sum_p\sum_{a\ge1}\frac{p^{-as}}a
\]

requires the additional depth weight `1/a`.  This depth is scale/provenance data from the ratio `n/m=p^a`; it is not contained in the normalized positive resultant mass alone.

Therefore

\[
\boxed{
\text{PRIME-RAY RESULTANT MASS}
\neq
\text{PRIME-RAY DEPTH PROVENANCE}.
}
\tag{PRO-9}
\]

The distinction is mathematically operative: `-zeta'/zeta` needs the former, while `log zeta` needs both.

## 8. Operator interpretation

The exact finite arithmetic picture is

```text
primitive spectral factors Psi_m,Psi_n
    -> integer resultant
    -> p-adic normalized valuation
    -> prime-power reachability kernel K_p
    -> locally finite prime shift resolvent sum_a S_p^a
    -> von-Mangoldt Dirichlet-convolution operator
    -> derived Dirichlet-series multiplier -zeta'/zeta
```

Freeze:

`NORMALIZED_SPECTRAL_RESULTANT = PRIME_RAY_REACHABILITY_KERNEL`.

`VON_MANGOLDT_CONVOLUTION = LOG_WEIGHTED_SUM_OF_SPECTRAL_PRIME_RAYS`.

`RESULTANT_MASS != SCALE_DEPTH_PROVENANCE`.
