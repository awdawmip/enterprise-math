# Free Research — Reduced Core-to-Deep Energy Normalization Bridge

Status: `FREE_RESEARCH_FRONTIER / REDUCED_STANDARD_NORMALIZATION_BRIDGE_CLOSED / MASS_AMPLITUDE_TRADEOFF_EXACT / FULL_ARITHMETIC_ENDPOINT_INTERTWINER_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Parent: `FREE_RESEARCH_STIRLING_NORMALIZATION_GAP_20260904.md`

## 1. Executive advance

The core/full normalization mismatch can be closed exactly on the reduced color-standard representation.

The factorial core has six histories.  After quotienting the irrelevant order of the final two slots for the closing-edge readout, it is

\[
\{1,2,3\}\times\{0,1\},
\]

with two histories for each first color.  The deepest constant-map chamber has three states, one for each color.

Map every core history to the deep state carrying its first color.  Retain each core history with subprobability `1/9`.  Then conditional core atom mass `1/6` pushes to full-packet deep atom mass `1/27`:

\[
\boxed{
2\cdot\frac16\cdot\frac19=\frac1{27}.
}
\]

Thus the three deep colors have total mass `1/9`.

On the standard representation, shrinking amplitude by `1/3` at unit conditional core mass and shrinking measure by `1/9` while preserving amplitude are exactly isometric in `L^2`.

---

## 2. Reduced factorial core

Let

\[
\mathcal C_{m red}
:=\mathrm{Fin}(3)\times\mathrm{Fin}(2).
\]

The first coordinate records the first history action.  The second records the two possible orders of the remaining positions.

The core-to-deep map is

\[
\boxed{
\pi_{m cd}(j,\varepsilon)=j.
}
\tag{2.1}
\]

A color permutation acts on the first coordinate and leaves the final-order bit untouched.  Hence

\[
\boxed{
\pi_{m cd}(\sigma(j,\varepsilon))
=\sigma\pi_{m cd}(j,\varepsilon).
}
\tag{2.2}
\]

The map is `S_3`-equivariant.

---

## CDE-T01 — Exact mass bridge

Give each of the six core histories conditional mass

\[
\mu_{m core}=1/6.
\]

Let each history retain subprobability

\[
r=1/9
\]

under the core-to-deep map.  Since each deep color has two core preimages,

\[
\mu_{m deep}(j)
=2\mu_{m core}r
=2\cdot\frac16\cdot\frac19
=\frac1{27}.
\tag{3.1}
\]

Therefore

\[
\boxed{
\sum_{j=1}^{3}\mu_{m deep}(j)=\frac19.
}
\tag{3.2}
\]

This supplies the missing common normalization: the input core is conditionally normalized to mass one, while the output deep packet is a full-packet subprobability of mass `1/9`.

---

## CDE-T02 — Exact energy isometry

For a color vector

\[
h=(h_1,h_2,h_3),
\]

the conditional core energy is

\[
\begin{aligned}
\mathcal E_{m core}(h)
&=\frac16\sum_{\sigma\in S_3}|h_{\sigma(1)}|^2\\
&=\frac13\sum_{j=1}^{3}|h_j|^2.
\end{aligned}
\tag{4.1}
\]

After the weighted `S_3` mixer, a standard vector has amplitude `h/3`, so

\[
\boxed{
\mathcal E_{m mix}(h)
=\mathcal E_{m core}(h/3)
=\frac19\mathcal E_{m core}(h).
}
\tag{4.2}
\]

The full-packet deep energy with atom mass `1/27` is

\[
\begin{aligned}
\mathcal E_{m deep}(h)
&=\frac1{27}\sum_{j=1}^{3}|h_j|^2\\
&=\frac19\mathcal E_{m core}(h).
\end{aligned}
\tag{4.3}
\]

Hence

\[
\boxed{
\mathcal E_{m mix}(h)=\mathcal E_{m deep}(h).
}
\tag{4.4}
\]

This is the exact amplitude/measure tradeoff:

\[
\boxed{
\text{amplitude }h\mapsto h/3\text{ at mass }1
\quad\equiv_{L^2}\quad
\text{amplitude }h\text{ at mass }1/9.
}
\]

---

## 5. Interpretation

The coefficient match now has a rigorous reduced intertwiner.

- The mixer realizes `1/9` through squared amplitude contraction on the conditional core probability space.
- The deepest chamber realizes `1/9` through subprobability mass attenuation in the full packet.
- The core-to-deep map preserves the color standard amplitude and transfers the contraction from amplitude to measure.

This removes the raw denominator mismatch exposed in the normalization-gap note at the representation level.

It does **not** yet construct the arithmetic endpoint distribution.  The reduced bridge forgets the prime-power labels and lower endpoint `m`; it only closes the finite color/provenance normalization.

---

## 6. Relation to the colored kernel

The actual deepest arithmetic kernel has states

\[
(j,m),\qquad m<Y.
\]

Fiberwise color balance gives

\[
\kappa_Y(1,m)=\kappa_Y(2,m)=\kappa_Y(3,m).
\]

Summing over `m` produces the three equal deep color masses.  The reduced bridge identifies their target standard representation and total subprobability normalization.

The remaining arithmetic task is to distribute each `1/27` color mass over the lower endpoints while proving the desired norm bound for nonconstant prime-winding readouts.

---

## 7. Formal and exact-computation status

Lean file:

- `EnterpriseMath/Relation/CoreDeepEnergyBridge.lean`.

It formalizes:

1. the reduced six-to-three color map;
2. `S_3` equivariance;
3. the exact atom-mass pushforward;
4. total deep mass `1/9`;
5. conditional core energy;
6. full-packet deep energy;
7. equality between mixed-core and deep energy.

Exact checker:

- `scripts/check_free_research_core_deep_energy_bridge.py`.

It verifies with `Fraction`:

1. the six permutation histories and their first-color fibers;
2. the atom-mass pushforward;
3. equivariance under all color permutations;
4. exact energy isometry for independent standard and nonstandard test vectors.

Lean-green status is not asserted until workflow completion.

---

## 8. Updated boundary

Closed:

- the core/full denominator mismatch on the reduced standard representation;
- the exact `1/9` subprobability bridge;
- equivalence of amplitude contraction and measure attenuation;
- `S_3`-equivariant six-to-three color map.

Open:

- lifting the reduced map to the full prime-power labels and lower arithmetic endpoints;
- controlling endpoint-dependent readout variation inside each deep color fiber;
- composing the resulting colored arithmetic kernel across cube-root scales;
- a native quantitative prime remainder.

---

## 9. Next theorem

For the full deepest kernel, prove a conditional-variance decomposition

\[
\mathcal E_{m deep}(H)
=\mathcal E_{\rm color}(\mathbb E[H\mid j])
+\mathbb E_j\operatorname{Var}(H\mid j,m),
\]

or its finite weighted analogue, and bound the endpoint-dependent variance by lower-scale relation energy.

This would lift the reduced color isometry to the complete arithmetic endpoint bundle.