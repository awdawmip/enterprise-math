# Free Research — Native-Sector / Projective C3 Intertwiner

Status: `FREE_RESEARCH_FRONTIER / ANCHOR_EXPOSED / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Parents:
- `FREE_RESEARCH_PI_PRIME_NATIVE_C3_CHIRAL_TRACE_20260904.md`
- `FREE_RESEARCH_PI_PRIME_PROJECTIVE_RADIUS_C3_BRIDGE_20260904.md`

## 1. Goal

The previous two frontiers established separately:

1. the current three-axis Enterprise research slice has a native sector-cycle isometry `rho` of order three;
2. at the exact current cell radius `r=R_cell=1/sqrt(3)`, the derived projective map `T_(1/r)` has order three.

The remaining typed question was whether the two order-three actions can be related by an explicit finite intertwiner rather than merely observed to have the same abstract group type.

This note closes that question at **sector-label/orientation strength**.

---

## NPI-T01 — A distinguished projective three-cycle at the native radius

For

\[
r=R_{\rm cell}=1/\sqrt3,
\qquad a=1/r=\sqrt3,
\]

let

\[
Q:=T_a,
\qquad
T_a(x)=\frac{x+a}{1-ax}.
\]

On the real projective line `RP^1`, direct calculation gives

\[
\boxed{Q(r)=\infty.}
\]

The projective value at infinity is

\[
Q(\infty)=-1/a=-r,
\]

and

\[
Q(-r)=r.
\]

Therefore

\[
\boxed{
r\xrightarrow{Q}\infty
\xrightarrow{Q}-r
\xrightarrow{Q}r
}
\]

is an exact three-point orbit.

This is the same order-three projective action previously obtained as `T_r^2=T_(1/r)`.

---

## NPI-T02 — Explicit equivariant embedding of the native sector labels

Let the three native positive-sector labels be

\[
\Sigma=\{S_{12},S_{23},S_{31}\},
\]

with native cycle

\[
\rho_\Sigma(S_{12})=S_{23},
\qquad
\rho_\Sigma(S_{23})=S_{31},
\qquad
\rho_\Sigma(S_{31})=S_{12}.
\]

Define

\[
\phi:\Sigma\to\mathbb{RP}^1
\]

by

\[
\boxed{
\phi(S_{12})=r,
\qquad
\phi(S_{23})=\infty,
\qquad
\phi(S_{31})=-r.
}
\]

Then NPI-T01 immediately gives

\[
\boxed{
\phi\circ\rho_\Sigma
=Q\circ\phi.
}
\]

Thus the native three-sector cycle and the radius-selected projective `C3` orbit are not merely abstractly isomorphic: they are explicitly equivariantly identified at orientation-label strength.

Because the three projective values are distinct, `phi` is injective. Hence the native sector-cycle representation is conjugate to the restriction of `Q` to the orbit `{r,infinity,-r}`.

---

## NPI-T03 — The chiral trace matrix is the projective-orbit permutation matrix

Order the native sector labels as

\[
(S_{12},S_{23},S_{31})
\]

and the projective orbit as

\[
(r,\infty,-r).
\]

Under `phi`, both actions are represented by the same permutation matrix

\[
P=
\begin{pmatrix}
0&0&1\\
1&0&0\\
0&1&0
\end{pmatrix}.
\]

Therefore the previously defined chiral probe

\[
J=P^2-P
\]

has a dual exact interpretation:

- native side: oriented difference between the two nontrivial sector-cycle directions;
- projective side: oriented difference between forward and reverse motion on the radius-selected three-point orbit.

Consequently

\[
\boxed{
\chi_3(n)=\frac13\operatorname{Tr}(JP^n)
}
\]

is simultaneously a native-sector trace and a projective-radius-orbit trace.

This closes the previous `native rho <-> projective C3` gap at the finite orientation representation level.

---

## NPI-T04 — Prime local factors are now functions of the radius-selected orbit action

For every arithmetic prime `p`,

\[
\chi_3(p)
=\frac13\operatorname{Tr}(JP^p)
\]

can now be read directly from the `p`-fold iterate of `Q=T_(1/R_cell)` restricted to the distinguished orbit

\[
\{R_{\rm cell},\infty,-R_{\rm cell}\}.
\]

Therefore the local Dirichlet factor

\[
\boxed{
\left(1-\frac{\chi_3(p)}p\right)^{-1}
=\left(1-\frac{\operatorname{Tr}(JP^p)}{3p}\right)^{-1}
}
\]

is a finite function of two exact data:

1. the arithmetic prime mode `p`;
2. the `p`-fold action on the native-radius projective orbit.

The global weight-one Euler product is still an analytic completion, but its local orientation selector is now completely finite and geometrically tied to `R_cell`.

---

## NPI-T05 — What is and is not intertwined

The intertwiner `phi` is deliberately scoped to **sector labels / orientation states**.

It does not map an arbitrary native address `(a,b,c)` to a projective coordinate and therefore does not assert

\[
A_E\cong\mathbb{RP}^1.
\]

It does not identify primitive point subtraction, native line length, or full six-dimensional P000 geometry with a Möbius model.

What is proved is exactly:

\[
\boxed{
(\Sigma,\rho_\Sigma)
\cong
(\{r,\infty,-r\},Q|_{\rm orbit})
}
\]

with `r=R_cell`.

This is the correct typed strength for the prime C3 orientation observer, because `chi_3` depends only on the order-three phase/orientation representation.

---

## 6. Consequence for the pi-to-prime geometry

The orientation channel can now be written as one finite chain:

\[
\boxed{
\text{native 120-degree sector cycle}
\xrightarrow{\phi}
\text{radius-selected projective C3 orbit}
\xrightarrow{p\text{-th iterate}}
\chi_3(p)
\xrightarrow{\text{Euler completion}}
\frac{\tau R_{\rm cell}}3.
}
\]

The first three arrows are exact finite geometry/arithmetic. Only the final infinite Euler completion is analytic.

Together with the universal birth channel,

\[
\tau^2=3!\lim_M\det(I-B_M^{-2})^{-1},
\]

the current prime geometry now has an explicit finite local carrier for both:

- **magnitude/birth**: arithmetic-prime eigendirections inside the genuine Krawtchouk integer spectrum;
- **orientation/chirality**: arithmetic-prime iterates on the native-radius `C3` orbit.

---

## Current classification

- projective orbit `{R_cell,infinity,-R_cell}` under `T_(1/R_cell)`: `PROVED / FINITE`.
- native-sector/projective-orbit equivariant embedding: `PROVED / FINITE / ORIENTATION STRENGTH`.
- chiral trace as common permutation representation: `PROVED / FINITE`.
- local prime C3 factor as radius-orbit readout: `PROVED / FINITE`.
- full native address/projective-coordinate equivalence: `NOT CLAIMED / FALSE TARGET TYPE`.
- full P000 6D lift: `OPEN`.
- global weight-one prime product: `ANALYTIC COMPLETION`.
