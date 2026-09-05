# Möbius duality: decimation trace versus resultant incidence inversion

Status: `FREE_RESEARCH / EXACT FINITE-ALGEBRA CONSISTENCY THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- primitive even-decimation trace formula;
- prime-specific normalized resultant kernels;
- locally finite divisor-incidence algebra.

## 1. Prime one-step shifts

For each prime `p`, let `S_p` act on arithmetic functions by

\[
(S_pf)(n)=\begin{cases}f(n/p),&p\mid n,\\0,&p\nmid n.\end{cases}
\]

Equivalently its incidence kernel is

\[
S_p(m,n)=\mathbf 1_{\{n=mp\}}.
\]

The prime shifts commute.

On any finite divisor-closed set they are nilpotent, so all formal geometric inverses below are honest finite sums.

## 2. Resultant reachability kernel

The prime-specific normalized primitive spectral resultant kernel is

\[
K_p(m,n)=\mathbf 1_{\{n=mp^a,\ a\ge1\}}.
\]

Therefore

\[
\boxed{K_p=S_p+S_p^2+S_p^3+\cdots=S_p(I-S_p)^{-1}.}
\tag{MDR-1}
\]

Hence

\[
\boxed{I+K_p=(I-S_p)^{-1},}
\tag{MDR-2}
\]

and locally finitely

\[
\boxed{I-S_p=(I+K_p)^{-1}.}
\tag{MDR-3}
\]

Thus the one-step prime direction can be reconstructed from the pairwise resultant reachability channel.

## 3. Divisor zeta and Möbius operators

The ordinary divisor-incidence zeta operator is

\[
\mathcal Z
=\prod_p(I-S_p)^{-1}.
\]

Its kernel is

\[
\mathcal Z(m,n)=\mathbf 1_{m\mid n},
\]

so it implements convolution by the constant-one arithmetic function.

Its inverse is the Möbius incidence operator

\[
\boxed{
\mathcal M
=\mathcal Z^{-1}
=\prod_p(I-S_p).
}
\tag{MDR-4}
\]

Using (MDR-3), the same operator is reconstructed solely from spectral resultant kernels:

\[
\boxed{
\mathcal M
=\prod_p(I+K_p)^{-1}.
}
\tag{MDR-5}
\]

For every `n`, the boundary coefficient is

\[
\boxed{\mathcal M(1,n)=\mu(n).}
\tag{MDR-6}
\]

Indeed expansion of `prod_p(I-S_p)` chooses each prime at most once: squarefree `n` receives `(-1)^omega(n)` and nonsquarefree `n` receives zero.

## 4. Independent phase-decimation realization of Möbius

The primitive even-decimation trace channel independently gives

\[
\mathcal T_n(1)
=2(\varphi(n)-c_n(1)).
\]

Since `c_n(1)=mu(n)`,

\[
\boxed{
\mu(n)=\varphi(n)-\frac12\mathcal T_n(1).
}
\tag{MDR-7}
\]

The derivation of (MDR-7) uses primitive finite rotation modes and the two-step spectral decimation polynomial `R_2`; it does not use pairwise resultants.

## 5. Cross-observer consistency theorem

Combining (MDR-6) and (MDR-7),

\[
\boxed{
\varphi(n)-\frac12\mathcal T_n(1)
=
\left[
\prod_p(I+K_p)^{-1}
\right](1,n).
}
\tag{MDR-8}
\]

Thus the same Möbius inversion is encoded by two structurally different finite spectral observers:

```text
primitive phase-decimation trace
    -> trace defect
    -> mu(n)

primitive pairwise resultants
    -> p-adic reachability kernels K_p
    -> incidence inverse product
    -> mu(n)
```

Neither observer is definitionally reduced to the other before this equality.

## 6. Typing consequence

This equality is a consistency bridge, not a carrier identification.

- `T_n(1)` is a trace of an integer polynomial acting on a primitive finite spectral algebra;
- `K_p` is a p-adic valuation readout of pairwise primitive resultants;
- `mu(n)` is the common arithmetic invariant extracted from both.

Hence

`TRACE_CHANNEL != RESULTANT_CHANNEL`,

while

`TRACE_MOBIUS_READOUT = RESULTANT_INCIDENCE_MOBIUS_READOUT`.

This is another explicit case where preserving distinct carriers produces a nontrivial cross-check rather than forcing premature recoalescence.

Freeze:

`MOBIUS = PRIMITIVE_DECIMATION_TRACE_DEFECT`.

`MOBIUS = SPECTRAL_RESULTANT_INCIDENCE_INVERSE`.

`THE_TWO_FINITE_REALIZATIONS_COINCIDE`.
