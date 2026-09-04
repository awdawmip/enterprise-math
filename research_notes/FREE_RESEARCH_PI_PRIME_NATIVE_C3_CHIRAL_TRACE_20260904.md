# Free Research — Native C3 Chiral Trace and the Prime Orientation Product

Status: `FREE_RESEARCH_FRONTIER / ANCHOR_EXPOSED / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Parents:
- `FREE_RESEARCH_PI_PRIME_BIRTH_SPECTRAL_DETERMINANT_20260904.md`
- `FREE_RESEARCH_PI_PRIME_C3_ROTATION_CHARACTER_20260904.md`

## 1. Native three-sector rotation in the current Enterprise slice

Current three-axis slice addresses are

\[
A_E=\{(a,b,c)\in\mathbb N_0^3:\min(a,b,c)=0\},
\]

with native origin norm

\[
L_E(a,b,c)^2=a^2+b^2+c^2.
\]

Define the cyclic coordinate rotation

\[
\boxed{\rho(a,b,c)=(c,a,b).}
\]

Then:

1. `rho(A_E)=A_E` because cyclic permutation preserves `min=0`;
2. `rho^3=id`;
3. `rho` cycles the three positive axes/sectors;
4. `rho` preserves the exact current native norm because it preserves `a^2+b^2+c^2`.

Hence `rho` is a genuine finite order-three isometry of the **current three-axis Enterprise research slice**. This statement does not identify the slice with full P000 six-dimensional space.

---

## PCT-T01 — Chiral trace formula for the modulo-three character

On the three sector/axis labels, write the same cyclic action as

\[
P=
\begin{pmatrix}
0&0&1\\
1&0&0\\
0&1&0
\end{pmatrix},
\qquad P^3=I_3.
\]

Define the orientation-sensitive probe

\[
\boxed{J:=P^2-P.}
\]

Then

\[
\operatorname{Tr}(JP)=3,
\qquad
\operatorname{Tr}(JP^2)=-3,
\qquad
\operatorname{Tr}(J)=0.
\]

Therefore for every positive integer `n`,

\[
\boxed{
\chi_E(n):=\frac13\operatorname{Tr}(JP^n)
=
\begin{cases}
0,&3\mid n,\\
+1,&n\equiv1\pmod3,\\
-1,&n\equiv2\pmod3.
\end{cases}}
\]

Thus

\[
\boxed{\chi_E=\chi_3}
\]

exactly: the nonprincipal Dirichlet character modulo three is the normalized **chiral trace of repeated native three-sector rotation**.

This removes a possible objection to the previous note: the modulo-three type need not be attached externally to primes. It is read directly from powers of the native sector rotation.

---

## PCT-T02 — Prime rotation type is a native trace readout

For a prime `p`,

\[
\boxed{
\chi_3(p)=\frac13\operatorname{Tr}(JP^p).
}
\]

Hence:

- `p=3`: `P^p=I`, chiral trace zero;
- `p=1 mod 3`: `P^p=P`, chiral trace `+3`;
- `p=2 mod 3`: `P^p=P^2=P^{-1}`, chiral trace `-3`.

The split/nonsplit/ramified classification of `Phi_3` therefore has a literal finite Enterprise-slice rotation observer.

Typed boundary:

`C3_CHIRAL_TRACE = NATIVE_THREE_AXIS_SLICE_ROTATION_OBSERVER`;

`C3_CHIRAL_TRACE != FULL_6D_ROTATION_CLASSIFICATION` unless a six-dimensional lift is separately proved.

---

## PCT-T03 — Harmonic chiral-trace completion

Define the finite chiral trace sum

\[
T_K
:=\sum_{n=1}^{3K}\frac{\operatorname{Tr}(JP^n)}n.
\]

Because the trace pattern is `+3,-3,0` on each residue block,

\[
\boxed{
T_K
=3\sum_{k=0}^{K-1}
\left(\frac1{3k+1}-\frac1{3k+2}\right)
=3S_K.
}
\]

The rational tail estimate from the parent C3 note gives

\[
\boxed{
T_K
<3\mathcal O_3
<T_K+\frac1{3K}.
}
\]

At the analytic completion layer,

\[
3\mathcal O_3=\frac{\tau}{\sqrt3}.
\]

Current native cell radius is

\[
R_{\rm cell}=1/\sqrt3.
\]

Therefore

\[
\boxed{
\sum_{n\ge1}
\frac{\operatorname{Tr}(JP^n)}n
=\tau R_{\rm cell}.
}
\]

and every finite `K>=1` gives the target-free interval

\[
\boxed{
T_K<\tau R_{\rm cell}<T_K+\frac1{3K}.
}
\]

This is the cleanest current coordinate-geometric meaning of the internal pi-like constant on the three-axis slice:

> `tau * native cell radius` is the harmonic completion of the chiral trace of repeated native 120-degree sector rotation.

Only the final infinite equality is analytic-completion strength; `P`, `J`, the trace pattern, and every finite `T_K` are exact finite objects.

---

## PCT-T04 — Prime Euler product written entirely in native rotation traces

The orientation Euler product becomes

\[
\mathcal O_3
=\prod_p\left(1-\frac{\chi_3(p)}p\right)^{-1}
=\prod_p\left(
1-\frac{\operatorname{Tr}(JP^p)}{3p}
\right)^{-1}.
\]

Hence

\[
\boxed{
\frac{\tau R_{\rm cell}}3
=
\prod_p\left(
1-\frac{\operatorname{Tr}(JP^p)}{3p}
\right)^{-1}.
}
\]

This is a genuine `pi -> primes -> native rotation` formula at analytic-completion strength. Each local prime factor is selected by a finite native rotation trace:

\[
\begin{array}{ccl}
p=3 &:& 1,\\
p\equiv1\pmod3 &:& (1-1/p)^{-1}=p/(p-1),\\
p\equiv2\pmod3 &:& (1+1/p)^{-1}=p/(p+1).
\end{array}
\]

The infinite Euler product at `s=1` is conditional and must retain its natural prime-cutoff meaning. No positive Weighted-BRC absolute-product theorem is asserted here.

---

## PCT-T05 — Two native-looking prime reconstructions of `tau`

The project now has two sharply different prime reconstructions.

### Universal multiplicative-birth observer

\[
\boxed{
\tau^2
=6\lim_{M\to\infty}
\det(I-B_M^{-2})^{-1},
}
\]

where `B_M` is the arithmetic prime-birth restriction of the genuine finite Krawtchouk integer spectrum. This observer forgets the three-sector phase and closes at the first stable integer order `2`.

### Three-sector chiral observer

\[
\boxed{
\frac{\tau R_{\rm cell}}3
=
\prod_p\left(
1-\frac{\operatorname{Tr}(JP^p)}{3p}
\right)^{-1}.
}
\]

This observer remembers whether each prime preserves or reverses the native order-three sector phase.

They are not interchangeable:

`PRIME_BIRTH_MAGNITUDE != C3_PRIME_ORIENTATION`.

Together they give a more structured answer than “pi is an Euler product”: the prime extension has at least a magnitude/birth channel and an orientation/chirality channel.

---

## 6. What is now genuinely native, and what remains completion

### Exact finite native-slice layer

- cyclic atlas rotation `rho(a,b,c)=(c,a,b)`;
- `rho^3=id`;
- exact native-length preservation;
- sector permutation matrix `P`;
- chiral probe `J=P^2-P`;
- exact trace character `chi_3(n)=Tr(JP^n)/3`;
- finite rational sums `T_K` and their algebraic tail majorant.

### Analytic completion layer

- `sum Tr(JP^n)/n = tau R_cell`;
- the conditional prime Euler product at weight one;
- equality of that product with `tau R_cell/3`.

Thus the open gap has narrowed substantially. The prime **local geometry** is now native at three-axis-slice strength; only the global completion equality remains analytic.

---

## 7. Next theorem target

The next discriminating target is no longer “find a mod-three interpretation”. It is:

> Derive the harmonic chiral-trace completion `sum Tr(JP^n)/n = tau R_cell` from the finite native cell/rotation transition calculus itself, without importing the standard arctangent evaluation or treating the internal sine completion as a black box.

A successful proof would close the `C3` prime-orientation channel at native finite-refinement strength. A failure would cleanly locate the remaining analytic boundary.

---

## Current classification

- `rho` native sector-cycle isometry: `PROVED / FINITE / THREE-AXIS-SLICE`.
- `chi_3(n)=Tr(JP^n)/3`: `PROVED / FINITE`.
- prime preserve/reverse/collapse readout: `PROVED / FINITE`.
- finite chiral sum + rational tail bound: `PROVED / FINITE`.
- `sum Tr(JP^n)/n = tau R_cell`: `ANALYTIC COMPLETION / NATIVE DERIVATION OPEN`.
- prime product in native trace factors: `ANALYTIC COMPLETION / CONDITIONAL EULER PRODUCT`.
- full P000 six-dimensional lift: `OPEN / NOT CLAIMED`.
