# P025 Supplement 111 — Polynomial Observable Interaction-Order Theorem

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-nonlinear-observable-stage107`  
Depends on: P025 Supplement 110  
Hard block: `NONE`

## 1. General polynomial observable

Let

\[
P(r)=c_0+c_1r+\cdots+c_dr^d,
\qquad c_d\ne0,
\]

be a nonzero polynomial of degree `d>=0`.

Define the node-rank observable

\[
\boxed{
\mathcal O_P:=\sum_jP(r_j).
}
\]

The threshold/node operation algebra and the Stage109 common merged-rank generator remain fixed.

## 2. P025-T254 — universal upper bound `deg(P)+1`

Each old-node selected rank is affine in the candidate-row selection bits. Composing with `P` gives a Boolean polynomial of degree at most `d`.

Each future-node term has the form

\[
y_jP\left(R_j+\sum_i x_iC_{ij}\right),
\]

so the future selector `y_j` raises total degree by at most one.

Therefore

\[
\boxed{
\deg \mathcal O_P(x,y)\le d+1.
}
\]

All irreducible Boolean finite differences of order `d+2` or higher vanish identically.

For `d=0`, candidate-threshold actions do not affect the constant observable, while adding a future node contributes the constant `c_0`, so the worst-case order is `1`.

## 3. P025-T255 — exact top coefficient

Use again the exact P025 dyadic edge

\[
\rho_0=\frac1{22}<\frac{13}{22}=\rho_1.
\]

For `d>=1`, choose `d` distinct rational candidate thresholds strictly between the two pressures. Use no old thresholds.

Then the old node lies below all candidates and the future node lies above all candidates. On the selected variables,

\[
\mathcal O_P
=
P(0)+yP(x_1+\cdots+x_d).
\]

The old constant `P(0)` disappears under any mixed action difference.

Taking the `d` threshold differences kills every polynomial term of degree below `d`. The leading term contributes

\[
\boxed{c_d d!}.
\]

The final future-column difference removes the outer gate `y`. Hence

\[
\boxed{
\Delta_{x_1}\cdots\Delta_{x_d}\Delta_y\mathcal O_P
=c_dd!\ne0.
}
\]

For `d=0`, the one future-node difference is simply `c_0`.

## 4. P025-T256 — exact worst-case order

Combining the upper and lower bounds:

\[
\boxed{
\operatorname{ord}(\mathcal O_P)=\deg(P)+1
}
\]

in the worst case for every nonzero polynomial `P`.

Thus Stage110's moment theorem is a special case rather than an isolated pattern.

## 5. Lower-degree terms do not affect the top interaction

The exact highest-order coefficient depends only on the leading coefficient:

\[
\boxed{\text{top coefficient}=c_dd!.}
\]

Lower-degree terms can strongly change lower-order responses and can create state-relative cancellations, but they cannot change the worst-case top order.

For example,

\[
P(r)=5-3r+2r^3
\]

has exact worst-case interaction order `4` and top coefficient

\[
2\cdot3!=12.
\]

## 6. Consequence for observable families

If a declared observable family contains polynomials of unbounded degree, then the required response-jet order is unbounded even though:

- the operation algebra is fixed;
- the common merged-rank incidence generator is fixed in kind.

Hence no universal finite jet order can be attached to the operation system without also bounding the observable algebra.

## 7. Architectural consequence

A precise future-compatibility contract must declare not only which operations may occur, but which observable algebra must remain predictable.

The minimum response order is a property of the pair

\[
\boxed{(\text{operation algebra},\text{observable algebra})}
\]

relative to the available generator geometry.

It is not a property of operations alone.

## 8. Prior-art / novelty boundary

Polynomial degree, leading finite differences and the `c_d d!` coefficient are classical algebra. P025 claims none individually.

The project-side result is their exact deployment as a family of arithmetic precision pressure tests under one fixed operation system and common incidence generator. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 9. Executable assets

Added:

- `src/enterprise_math/abc_polynomial_rank_observable.py`;
- `tests/test_abc_polynomial_rank_observable.py`.

## 10. Next frontier

Worst-case degree is not the precision actually needed at every state. Stage112 will compute the local interaction order from forward differences of `P` at the node's base old-threshold rank and from the number of candidate thresholds that the node actually crosses.