# BRC ordinary-fold selector wall law

Date: 2026-09-04
Mode: TASK_RESEARCH
Status: research candidate; no Foundation promotion in this note
Parent: selector event theorem, simple selector wall-crossing line

## 1. Problem

A simple endpoint crossing has one real root branch and an oriented `+-1` rank jump.  A different generic event occurs when two real roots collide and disappear into a complex-conjugate pair, or the reverse.

For selector bookkeeping this ordinary fold explains why some discriminant events change a root-count observer by two while others are invisible because the collision happens outside the observed interval.

Fold normal forms and root-pair creation are classical prior art.  No bifurcation-theory novelty is claimed.

## 2. Ordinary-fold hypotheses

Let

\[
P(t,x)\in\mathbb Q[t,x]
\]

and suppose at a rational event

\[
(t_0,x_0)
\]

one has

\[
P(t_0,x_0)=0,
\qquad
P_x(t_0,x_0)=0,
\]

\[
P_{xx}(t_0,x_0)\ne0,
\qquad
P_t(t_0,x_0)\ne0.
\]

Assume no other root event occurs in a sufficiently small neighborhood.

Define the exact fold orientation

\[
\boxed{
\kappa
=-\frac{2P_t(t_0,x_0)}{P_{xx}(t_0,x_0)}.
}
\]

## 3. Real-pair side

Taylor expansion gives

\[
P(t_0+\delta t,x_0+\delta x)
=
P_t\,\delta t
+\frac12 P_{xx}\,\delta x^2
+o(|\delta t|+\delta x^2).
\]

Hence to first order the colliding roots satisfy

\[
\delta x^2
=\kappa\,\delta t.
\]

The ordinary-fold hypotheses imply the exact local topology:

\[
\boxed{
\text{two distinct real roots exist on the side }
\kappa\,\delta t>0,
}
\]

while on the opposite side there is no real root near `x0`.

Thus:

- \(\kappa>0\): the pair is born as `t` increases through `t0`;
- \(\kappa<0\): the pair annihilates as `t` increases.

## 4. Fixed-probe root-rank jump

Let

\[
\nu_t(r)=\#\{\text{distinct real roots of }P_t\text{ below }r\}
\]

for a fixed probe `r` with

\[
r\ne x_0.
\]

For sufficiently small parameter variation, both fold roots lie on the same side of `r` as `x0`.

Therefore

\[
\boxed{
\Delta\nu(r)
=
\begin{cases}
2\,\operatorname{sgn}(\kappa),&x_0<r,\\
0,&x_0>r.
\end{cases}
}
\]

The jump is `+2` when a real pair is born below the probe and `-2` when it disappears there.

If the fold happens to the right of the probe, the root-rank observer cannot see it.

## 5. Positive interval-count jump

For `r>0`, define

\[
N_t(0,r)=\#\{\alpha:0<\alpha<r,\ P_t(\alpha)=0\}.
\]

If the ordinary fold point is strictly inside the observed interval,

\[
0<x_0<r,
\]

then

\[
\boxed{
\Delta N(0,r)
=2\,\operatorname{sgn}(\kappa).
}
\]

If

\[
x_0<0
\quad\text{or}\quad
x_0>r,
\]

then both new/disappearing roots lie outside `(0,r)` locally, so

\[
\boxed{
\Delta N(0,r)=0.
}
\]

The endpoint cases `x0=0` or `x0=r` are **not** covered: a symmetric pair can contribute only one positive/interior root at the instant of crossing an endpoint.

## 6. Quadratic annihilation witness

Take

\[
P(t,x)=x^2+t x+1.
\]

At

\[
t_0=-2,
\qquad
x_0=1,
\]

\[
P=P_x=0,
\qquad
P_t=x_0=1,
\qquad
P_{xx}=2.
\]

Thus

\[
\boxed{\kappa=-1.}
\]

The real pair exists for `t<-2` and disappears for `t>-2`.

### Probe to the left

For

\[
r=0,
\]

we have `x0>r`, so

\[
\Delta\nu(0)=0.
\]

This is exactly why the discriminant event is invisible to a smallest-real observer whose declared root lies to the left.

### Probe to the right

For

\[
r=2,
\]

we have `x0<r`, so

\[
\boxed{\Delta\nu(2)=-2.}
\]

Near `t=-2`, both positive quadratic roots lie below `2` on the real side and both disappear after the fold.

Likewise

\[
\boxed{\Delta N(0,2)=-2.}
\]

because the fold point lies strictly inside `(0,2)`.

## 7. Quadratic birth witness

Use the same family at

\[
t_0=2,
\qquad
x_0=-1.
\]

Now

\[
P_t=x_0=-1,
\qquad
P_{xx}=2,
\]

so

\[
\boxed{\kappa=+1.}
\]

The pair is born for `t>2`.

At probe

\[
r=0,
\]

both new roots lie below the probe, giving

\[
\boxed{\Delta\nu(0)=+2.}
\]

For a positive interval `(0,2)` the fold occurs below zero, so

\[
\Delta N(0,2)=0.
\]

## 8. Endpoint fold boundary

Take

\[
P(t,x)=x^2+t
\]

at

\[
t_0=0,
\qquad
x_0=0.
\]

Here

\[
P_t=1,
\qquad
P_{xx}=2,
\qquad
\kappa=-1.
\]

For `t<0` the two real roots are

\[
\pm\sqrt{-t}.
\]

For a positive interval `(0,r)`, only the positive member belongs to the interval.  As `t` increases through zero, the interval count changes by `-1`, not `-2`.

Thus `x0=0` is an essential exclusion from the interior-fold interval formula.

The same issue occurs at `x0=r`.

## 9. Degenerate-fold boundaries

### `P_t=0`

For

\[
P(t,x)=x^2-t^2
\]

at `(0,0)`,

\[
P=P_x=0,
\quad
P_{xx}=2,
\quad
P_t=0.
\]

The roots `+-t` remain real on both sides; there is no ordinary birth/death orientation.

### `P_{xx}=0`

For

\[
P(t,x)=x^3-t
\]

at `(0,0)`,

\[
P=P_x=P_{xx}=0.
\]

This is a higher-order singular event and lies outside the ordinary-fold theorem.

## 10. Event annotation consequence

A one-parameter event table can now separate:

1. `SIMPLE_ENDPOINT_CROSSING`: `P_x!=0, P_t!=0`, jump `+-1`;
2. `ORDINARY_FOLD`: `P_x=0, P_xx!=0, P_t!=0`, local pair jump `0` or `+-2` depending observer location;
3. `TANGENT_ENDPOINT`: simple root but `P_t=0`;
4. `HIGHER_MULTIPLE_EVENT`: `P_x=P_xx=0` or multiple simultaneous conditions;
5. other resultant/degree-drop events.

This is more informative than an untyped discriminant zero.

## 11. Hard boundaries

- The theorem is local and assumes an isolated ordinary fold.
- Endpoint folds `x0=0` or `x0=r` require separate one-sided counting.
- Simultaneous root events are not decomposed here.
- `P_t=0` and `P_xx=0` are explicit refusal conditions.
- Algebraic event parameters can be handled by selected-root evaluation, but this note validates rational event coordinates only.
- No generic singularity classifier, complete Puiseux solver, multi-generator algebraic field, signed branch interference, or infinite-state claim is made.
