# Free Research — Breusch Remainder as Parity-Fold Energy Decay

Status: `FREE_RESEARCH_CALIBRATION / UNCONDITIONAL CLASSICAL INPUT / PARITY ENERGY RATE DERIVED / NOT A NATIVE INDEPENDENT PROOF / NOT WORKING TRUTH / NOT FOUNDATION`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`
Parent: `FREE_RESEARCH_PNT_PARITY_FOLD_ZERO_ENERGY_EQUIVALENCE_V15_20260904.md`
Researcher-ID: `EM-FREE-PI-PRIME-20260904`

## 1. External theorem used

Robert Breusch proved by elementary real methods that, for every `epsilon>0`,

\[
\psi(x)
=x+o\!\left(x(\log x)^{-1/6+\epsilon}\right).
\]

Equivalently, for every fixed

\[
0<\gamma<1/6,
\]

the normalized error

\[
r(x):=\psi(x)/x-1
\]

satisfies

\[
\boxed{r(x)=o((\log x)^{-\gamma}).}
\tag{1.1}
\]

This theorem is classical prior art. The point of the present note is only to identify its exact image in the V15 finite parity-fold carrier.

---

## 2. Folded endpoint moment bound

Let

\[
u_a=\Lambda(a)/a,
\qquad
A_N=\sum_{a\le N}u_a,
\qquad
p_N(a)=u_a/A_N.
\]

For the symmetric parity fold, each value is either

\[
r(q_{ab}(N))
\qquad(ab\le N)
\]

or

\[
\frac{r(q_a(N))+r(q_b(N))}{2}
\qquad(ab>N).
\]

The first-mass and two-history laws

\[
A(X)=\log X+O(1),
\qquad
C_2(X)=\frac12\log^2X+O(\log X)
\]

imply the following logarithmic endpoint estimates.

For every fixed `0<sigma<1`,

\[
\boxed{
\mathbb E_{a\sim p_N}
(1+\log q_a(N))^{-\sigma}
=O((\log N)^{-\sigma}),
}
\tag{2.1}
\]

and

\[
\boxed{
\frac1{A_N^2}
\sum_{ab\le N}u_au_b
(1+\log q_{ab}(N))^{-\sigma}
=O((\log N)^{-\sigma}).
}
\tag{2.2}
\]

The integrability threshold `sigma<1` is sharp for the limiting logarithmic endpoint densities: both have nonzero density at the absorbing boundary `log endpoint=0`.

A direct proof splits the endpoint logarithm at `eta log N`. On the bulk, the integrand is at most `(eta log N)^-sigma`; on the boundary, bounded discrepancy gives mass `O(eta)+O(1/log N)`. Integrating the tail distribution, or choosing dyadic `eta`, yields (2.1)--(2.2).

For each fixed integer `Z`, the stronger finite-boundary estimates are

\[
\Pr\{q_a(N)<Z\}=O_Z(1/\log N)
\]

and

\[
\Pr\{ab\le N,\ q_{ab}(N)<Z\}=O_Z(1/\log N).
\]

---

## BPE-T01 — Scalar rate implies folded second-moment rate

Assume

\[
r(x)=o((\log x)^{-\gamma})
\]

for some `0<gamma<1/2`. Then

\[
\boxed{
\mathbb E_{a,b\sim p_N}
|\widetilde F_N(a,b)|^2
=o((\log N)^{-2\gamma}).
}
\tag{3.1}
\]

### Proof

Fix a large integer `Z`. For endpoint values at least `Z`, write

\[
|r(m)|\le\epsilon_Z(1+\log m)^{-\gamma},
\qquad
\epsilon_Z\to0.
\]

Equations (2.1)--(2.2), with `sigma=2gamma<1`, bound the contribution of all large endpoints by

\[
O(\epsilon_Z^2(\log N)^{-2\gamma}).
\]

The contribution of endpoints below `Z` is

\[
O_Z((\log N)^{-1}),
\]

using Chebyshev boundedness of `r`. Since `2gamma<1`,

\[
(\log N)^{-1}
=o((\log N)^{-2\gamma}).
\]

First let `N` tend to infinity, then let `Z` tend to infinity. This proves (3.1).

The stopped average is handled by

\[
\left|\frac{x+y}{2}\right|^2
\le\frac{|x|^2+|y|^2}{2}.
\]

---

## BPE-T02 — Scalar rate implies parity-fold variance and Dirichlet rates

Since variance is bounded by the second moment,

\[
\boxed{
\widetilde{\mathcal F}_N(r)
=o((\log N)^{-2\gamma}).
}
\tag{4.1}
\]

For the shared-first degree-three energy,

\[
\begin{aligned}
\widetilde{\mathcal G}_N(r)
&=
\mathbb E_{a,b,c}
|\widetilde F_N(a,b)-\widetilde F_N(a,c)|^2\\
&\le
2\mathbb E|\widetilde F_N(a,b)|^2
+2\mathbb E|\widetilde F_N(a,c)|^2.
\end{aligned}
\]

Therefore

\[
\boxed{
\widetilde{\mathcal G}_N(r)
=o((\log N)^{-2\gamma}).
}
\tag{4.2}
\]

The same conclusion holds for the full pair-`S_3` Dirichlet form, since every transposition difference is bounded by the corresponding two second moments.

---

## BPE-C01 — Breusch exponent in the V15 carrier

Apply BPE-T01--T02 with every

\[
\gamma<1/6.
\]

Then, for every `delta>0`,

\[
\boxed{
\widetilde{\mathcal F}_N(r),
\widetilde{\mathcal G}_N(r)
=o((\log N)^{-1/3+\delta}).
}
\tag{5.1}
\]

Conversely, the V15 scalar readout

\[
|r(N)|
\le
\sqrt{\widetilde{\mathcal G}_N(r)}
+O(1/\log N)
\]

turns the energy exponent `1/3-delta` back into the scalar exponent

\[
1/6-\delta/2.
\]

Thus Breusch's exponent has the exact V15 interpretation

\[
\boxed{
\text{degree-three parity energy exponent }1/3
\xrightarrow{\text{square-root scalar readout}}
\text{prime-error exponent }1/6.
}
\tag{5.2}
\]

---

## 6. Relation to the conditional profile exponent

The parity-scattering profile has critical energy exponent

\[
\beta_*=0.4818928032\ldots,
\]

while the classical calibration supplies every energy exponent below `1/3`.

There is no contradiction:

- `1/3` is an unconditional exponent imported from Breusch's scalar theorem and mapped into the new carrier;
- `beta_*` is the larger spectral threshold that would be available if the still-open finite profile recurrence were proved directly;
- the corresponding conditional scalar threshold is `beta_*/2=0.2409464...`, whereas the classical elementary theorem used here gives every scalar exponent below `1/6`.

The gap

\[
1/3<\beta_*
\]

measures the remaining strength that must come from a genuinely native block recurrence rather than from the external classical calibration.

---

## 7. Boundary

Proved, conditional only on the cited classical theorem:

1. the symmetric folded second moment decays with every exponent below `1/3`;
2. the folded variance and shared-first three-history Dirichlet energy have the same rate;
3. the square-root scalar readout exactly explains the passage from `1/3` to `1/6`.

Not proved:

1. an independent Enterprise-native derivation of (5.1);
2. the stronger conditional exponent `beta_*`;
3. any external novelty for the classical remainder;
4. any RH-scale estimate.

This note is a prior-art calibration and a consistency theorem, not the desired independent native closure.
