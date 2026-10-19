# Free Research — Arithmetic Primes as C3 Rotation-Phase Types

Status: `FREE_RESEARCH_FRONTIER / ANCHOR_EXPOSED / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Parent frontier: `FREE_RESEARCH_PI_PRIME_BIRTH_SPECTRAL_DETERMINANT_20260904.md`
Project interpretation: the three-positive-axis `120 degree` geometry is a research slice of P000 six-dimensional space, not the full spatial ontology.

## 1. Purpose

The birth-block frontier gives every arithmetic prime a new irreducible multiplicative direction, but it does not yet use the specifically Enterprise three-sector `120 degree` rotation structure.

This note adds a separate, exact rotation-phase typing. It uses only the cyclic order-three rotation fiber

\[
C_3=\langle R\mid R^3=1\rangle
\]

and keeps that fiber distinct from native spatial length. No Eisenstein norm is imported as the Enterprise metric; current Foundation explicitly separates carrier geometry from native Pythagorean length.

---

## PCR-T01 — Prime Frobenius action on the 120-degree phase

For every prime `p`, define the power action on the order-three rotation phase by

\[
F_p(R):=R^p.
\]

Then exactly three types occur:

\[
\boxed{
\begin{array}{ccl}
p=3 &:& R^p=1,\quad\text{phase collapses};\\[1mm]
p\equiv1\pmod3 &:& R^p=R,\quad\text{phase/orientation preserved};\\[1mm]
p\equiv2\pmod3 &:& R^p=R^2=R^{-1},\quad\text{phase/orientation reversed}.
\end{array}}
\]

Define the orientation character

\[
\chi_3(p)=
\begin{cases}
0,&p=3,\\
+1,&p\equiv1\pmod3,\\
-1,&p\equiv2\pmod3.
\end{cases}
\]

This is the nonprincipal Dirichlet character modulo three, now typed as the sign of the prime action on the nontrivial `C3` rotation phases.

Interpretation:

`PRIME_BIRTH_DIRECTION` and `C3_ROTATION_PHASE_TYPE` are separate data. The first says a new multiplicative direction is born; the second says how that prime acts on the three-sector rotation fiber.

---

## PCR-T02 — Split / nonsplit / ramified phase resolution

Let

\[
\Phi_3(X)=X^2+X+1.
\]

For a prime `p`, this polynomial records the two nontrivial order-three phases.

Then:

\[
\boxed{
\begin{array}{ccl}
p=3 &:& \Phi_3(X)=(X-1)^2\text{ in }\mathbb F_3;\\
p\equiv1\pmod3 &:& \Phi_3\text{ splits into two distinct roots in }\mathbb F_p;\\
p\equiv2\pmod3 &:& \Phi_3\text{ is irreducible over }\mathbb F_p.
\end{array}}
\]

For `p != 3`, the proof is the cyclic-group criterion: a nontrivial cube root of unity exists in `F_p^*` iff `3 | (p-1)`.

Thus the Enterprise `120 degree` rotation phase sees arithmetic primes as:

- `RAMIFIED/COLLAPSED` at `p=3`;
- `SPLIT/RESOLVED` at `p=1 mod 3`;
- `NONSPLIT/EXTENSION-REQUIRED` at `p=2 mod 3`.

This is an exact finite algebraic geometry of the rotation fiber. It is not a claim about native length.

---

## PCR-T03 — Finite rational orientation completion

Extend `chi_3` completely multiplicatively to positive integers, with `chi_3(n)=0` when `3|n`. Define

\[
\mathcal O_3
:=\sum_{n\ge1}\frac{\chi_3(n)}n
=\sum_{k\ge0}
\left(\frac1{3k+1}-\frac1{3k+2}\right).
\]

The paired terms are positive and equal

\[
\frac1{(3k+1)(3k+2)}.
\]

For `K>=1`, let

\[
S_K:=\sum_{k=0}^{K-1}
\left(\frac1{3k+1}-\frac1{3k+2}\right).
\]

For every `k>=1`,

\[
0<\frac1{(3k+1)(3k+2)}
<\frac1{9k(k+1)}.
\]

Therefore the tail telescopes to the target-free exact rational certificate

\[
\boxed{
S_K<\mathcal O_3<S_K+\frac1{9K}.
}
\]

This gives a finite arithmetic orientation readout without a numerical `pi` target and without prime enumeration. It preserves the full integer population through `chi_3`; multiples of three are zero-labeled data rather than silently deleted.

---

## PCR-T04 — Analytic completion and the current native cell radius

The paired series has the elementary integral representation

\[
\mathcal O_3
=\int_0^1\frac{1-x}{1-x^3}\,dx
=\int_0^1\frac{dx}{1+x+x^2}.
\]

At the analytic completion layer in which #1159's sine-type first positive zero is `tau` (and #1161 proves `Pi_*=tau`), the standard power-series trigonometric evaluation gives

\[
\boxed{
\mathcal O_3=\frac{\tau}{3\sqrt3}.
}
\]

The current three-axis Enterprise slice independently has exact cell radius

\[
R_{\rm cell}=\frac1{\sqrt3}.
\]

Hence

\[
\boxed{
\mathcal O_3=\frac{\tau R_{\rm cell}}3,
\qquad
\tau=\frac{3\mathcal O_3}{R_{\rm cell}}.
}
\]

This is an exact cross-layer identity once the analytic completion is admitted.

Strength boundary: this does **not** yet prove that the native cell covering radius itself causes the Dirichlet `L`-value. Both `sqrt(3)` appearances are compatible with the same order-three/equilateral carrier symmetry, but a G0 causal identification remains open.

Combining with PCR-T03 gives finite algebraic-cell bounds:

\[
\boxed{
\frac{3S_K}{R_{\rm cell}}
<\tau
<\frac{3}{R_{\rm cell}}
\left(S_K+\frac1{9K}\right).
}
\]

The endpoints are rational multiples of the exact algebraic native scalar `1/R_cell=sqrt(3)`.

---

## PCR-T05 — Prime Euler product as global orientation response

For the nonprincipal character `chi_3`, the natural increasing-prime Euler product at `s=1` gives

\[
\mathcal O_3
=\prod_p\left(1-\frac{\chi_3(p)}p\right)^{-1}.
\]

Equivalently,

\[
\boxed{
\frac{\tau R_{\rm cell}}3
=
\prod_{p\equiv1\ (3)}\frac{p}{p-1}
\prod_{p\equiv2\ (3)}\frac{p}{p+1}.
}
\]

The `p=3` Euler factor is one because `chi_3(3)=0`.

The product is not absolutely convergent at `s=1`; this theorem is therefore an analytic-completion statement, not a finite positive Weighted-BRC product theorem. The finite rational series certificate PCR-T03 is the preferred exact finite readout.

Geometric reading:

- split/resolved primes contribute the `+` orientation response `p/(p-1)`;
- nonsplit/reversing primes contribute the `-` orientation response `p/(p+1)`;
- the global ordered response completes to one third of `tau` measured in native cell-radius units.

---

## PCR-T06 — Two independent prime observables of `tau`

The birth-determinant frontier gives

\[
\boxed{
\tau^2=6\prod_p(1-p^{-2})^{-1},
}
\]

while the `C3` rotation-character frontier gives

\[
\boxed{
\tau=\frac3{R_{\rm cell}}
\prod_p\left(1-\frac{\chi_3(p)}p\right)^{-1}.
}
\]

These are different observers:

1. `UNIVERSAL PRIME BIRTH / QUADRATIC STABILITY` — ignores `C3` orientation and uses the first stable positive-integer Euler order `2`;
2. `C3 ORIENTATION RESPONSE` — remembers split vs reversed 120-degree phase and completes at character weight `1`.

Thus extending `pi` to primes does not collapse arithmetic into one scalar. The same `tau` is visible through at least two typed prime projections: universal birth mass and three-sector orientation response.

---

## 7. Relation to classical Eisenstein splitting

The split/nonsplit/ramified trichotomy is the classical prime behavior associated with the order-three cyclotomic/Eisenstein extension. This note does **not** claim novelty for that arithmetic theorem.

Enterprise-specific typing is narrower:

- use the `C3` rotation-phase action as a finite rotation-fiber observer;
- do not import the Eisenstein quadratic norm as native Enterprise length;
- retain current sector-local Pythagorean native metric unchanged;
- interpret the three-axis construction only at research-slice strength under P000.

---

## 8. Next discriminating bridge

The remaining native question is now concrete:

> Can the exact `C3` phase character `chi_3` and the algebraic radius factor `R_cell=1/sqrt(3)` be generated by one finite local rotation/cell transition rule in the current Enterprise slice, so that `O_3=tau R_cell/3` becomes a native completion theorem rather than an analytic cross-layer identity?

A successful construction would have to preserve the exact current native metric and address semantics; replacing them with the classical Eisenstein norm would be a typing failure, not a solution.

---

## Current classification

- `PRIME -> C3 PHASE PRESERVE/REVERSE/COLLAPSE`: `PROVED / FINITE`.
- `PHI3 SPLIT/NONSPLIT/RAMIFIED CLASSIFICATION`: `PROVED / CLASSICAL FINITE ALGEBRA`.
- `FINITE ORIENTATION SERIES CERTIFICATE`: `PROVED / RATIONAL`.
- `O3 = tau/(3 sqrt(3))`: `ANALYTIC COMPLETION / CLASSICAL IDENTITY REWRITTEN IN INTERNAL tau`.
- `O3 = tau R_cell/3`: `EXACT CROSS-LAYER IDENTITY / CAUSAL NATIVE BRIDGE OPEN`.
- `PRIME EULER PRODUCT AT s=1`: `ANALYTIC COMPLETION / CONDITIONAL PRODUCT`.
- `EISENSTEIN NORM = NATIVE ENTERPRISE LENGTH`: `FORBIDDEN / NOT CLAIMED`.
