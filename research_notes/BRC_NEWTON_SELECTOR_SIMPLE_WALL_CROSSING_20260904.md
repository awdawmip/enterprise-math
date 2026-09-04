# BRC exact simple selector wall-crossing orientation

Date: 2026-09-04
Mode: TASK_RESEARCH
Status: research candidate; no Foundation promotion in this note
Parent: selector event theorem, resultant-event generator, Sturm/root-rank selector line

## 1. Goal

Event polynomials tell where a selector state **may** change.  Chamber compilation labels the intervals on both sides.  At a simple endpoint-crossing event one can do more: determine the exact direction of the selector jump from local derivatives alone.

This note isolates that wall-crossing law.

Implicit-function root motion and oriented root counts are classical prior art.  No generic bifurcation novelty is claimed.

## 2. Simple root crossing a fixed probe

Let

\[
P(t,x)\in\mathbb Q[t,x]
\]

and fix a rational probe

\[
r\in\mathbb Q.
\]

Suppose at a rational parameter `t0`:

\[
P(t_0,r)=0,
\]

\[
P_x(t_0,r)\ne0,
\]

\[
P_t(t_0,r)\ne0.
\]

Then the crossing root is locally a unique differentiable branch

\[
\alpha(t_0)=r,
\]

with

\[
\boxed{
\alpha'(t_0)
=-\frac{P_t(t_0,r)}{P_x(t_0,r)}.
}
\]

The extra condition `P_t!=0` makes the crossing transverse to the fixed probe.

## 3. Root-rank jump law

Let

\[
\nu_t(r)
=
\#\{\text{distinct real roots of }P_t\text{ strictly below }r\}.
\]

Assume no other root event occurs at `t0`.  As `t` increases through `t0`:

- if \(\alpha'>0\), the root moves from below `r` to above `r`, so the rank drops by one;
- if \(\alpha'<0\), it moves from above `r` to below `r`, so the rank rises by one.

Therefore

\[
\boxed{
\Delta\nu(r)
:=
\nu_{t_0+}(r)-\nu_{t_0-}(r)
=
-\operatorname{sgn}(\alpha')
=
\operatorname{sgn}\!\left(\frac{P_t}{P_x}\right)_{(t_0,r)}.
}
\]

The jump is exactly \(\pm1\).

## 4. Smallest-positive interval count

For a fixed positive declared selector endpoint

\[
r>0,
\]

define the number of competing positive roots below it by

\[
N_t(0,r)
=
\#\{\alpha\in\mathbb R:P_t(\alpha)=0,\ 0<\alpha<r\}.
\]

### Right-endpoint crossing at `x=r`

If a simple root crosses `r` transversely and no zero crossing occurs simultaneously, then

\[
\boxed{
\Delta N(0,r)
=
\operatorname{sgn}\!\left(\frac{P_t}{P_x}\right)_{(t_0,r)}.
}
\]

This is the same as the root-rank jump at `r`.

### Left-endpoint crossing at `x=0`

If a simple root crosses zero transversely and no `r` crossing occurs simultaneously, then

\[
\boxed{
\Delta N(0,r)
=
-\operatorname{sgn}\!\left(\frac{P_t}{P_x}\right)_{(t_0,0)}.
}
\]

The sign reverses because the zero-right rank is subtracted from the rank at `r`.

## 5. Exact event orientation state

A rational simple endpoint event may therefore be stored as

\[
\boxed{
(t_0,\ x_0,\ P_t(t_0,x_0),\ P_x(t_0,x_0),\ J),
}
\]

where `x0` is either `r` or `0` and

\[
J=
\begin{cases}
\operatorname{sgn}(P_t/P_x),&x_0=r,\\
-\operatorname{sgn}(P_t/P_x),&x_0=0\text{ for }N(0,r).
\end{cases}
\]

No nearby root approximation is required.

## 6. One-real cubic witness

Take

\[
P(t,x)=x^3+x+t,
\qquad r=1.
\]

### Crossing the declared endpoint

At

\[
t_0=-2,
\qquad x_0=1,
\]

\[
P_t=1,
\qquad
P_x=3x^2+1=4.
\]

Hence

\[
\Delta N(0,1)=+1.
\]

Indeed:

- for `t<-2`, the unique positive root lies to the right of `1`, so `N=0`;
- for `-2<t<0`, it lies in `(0,1)`, so `N=1`.

### Crossing zero

At

\[
t_0=0,
\qquad x_0=0,
\]

\[
P_t=1,
\qquad
P_x=1.
\]

Thus

\[
\Delta N(0,1)=-1.
\]

The positive competitor leaves `(0,1)` through zero as `t` increases, explaining the second transition in the disconnected selector chamber

\[
t<-2\ \lor\ t\ge0.
\]

## 7. Moving-linear-root witness

Let

\[
F(x)=(x^2+1)(x^2-x-1),
\]

\[
P(t,x)=F(x)(x-t),
\qquad r=1.
\]

The moving root is exactly

\[
\alpha(t)=t.
\]

At any endpoint crossing,

\[
P_t=-F(x),
\qquad
P_x=F(x)
\]

on the moving root, hence

\[
\frac{P_t}{P_x}=-1.
\]

### Zero crossing `t=0`

For the positive interval count,

\[
\Delta N(0,1)=+1.
\]

The moving root enters `(0,1)` from the negative side.

### Declared-root crossing `t=1`

\[
\Delta N(0,1)=-1.
\]

The moving root exits `(0,1)` through the right endpoint.

These two oriented jumps explain the central unsafe chamber

\[
0<t<1.
\]

without sampling both neighboring intervals.

## 8. Tangency boundary: `P_t=0`

The transverse hypothesis is necessary.

Take

\[
P(t,x)=x-t^2,
\qquad r=0.
\]

At

\[
t_0=0,
\quad x_0=0,
\]

\[
P_x=1,
\qquad
P_t=-2t=0.
\]

The root branch is

\[
\alpha(t)=t^2,
\]

which touches the probe and returns to the same side.  There is no signed rank jump across `t=0`.

Thus `P_t=0` is a genuine non-transverse boundary where the simple wall formula must refuse to orient the event.

## 9. Multiple-root boundary: `P_x=0`

Take

\[
P(t,x)=x^2+t x+1,
\qquad r=-1.
\]

At the genuine selector transition

\[
t_0=2,
\qquad x_0=-1,
\]

one has

\[
P=0,
\qquad
P_x=2x+t=0.
\]

The crossing root is not simple; this is simultaneously a discriminant event and declared-root collision.  The first-order implicit-function wall orientation is undefined.

Hence `P_x!=0` is also an essential typed precondition.

## 10. Relation to event/chamber compilation

For a one-parameter chamber compiler:

- discriminant-only events may remain label-inactive;
- simple endpoint crossings can be oriented exactly by the derivative ratio;
- multiple/tangent endpoint events still require stronger local analysis or adjacent-cell labels.

Thus the event-root table can carry a typed classification:

\[
\boxed{
\text{SIMPLE ORIENTED CROSSING}
\mid
\text{NONTRANSVERSE/TANGENT}
\mid
\text{MULTIPLE-ROOT EVENT}
\mid
\text{OTHER EVENT}.
}
\]

## 11. Hard boundaries

- The theorem assumes an isolated simple root crossing a fixed endpoint.
- Simultaneous multiple events are not decomposed by the one-root formula.
- `P_t=0` tangencies are intentionally refused.
- `P_x=0` multiple-root crossings require separate local analysis.
- Algebraic event parameters can use a selected-root evaluation algebra, but this note validates the rational-event interface only.
- No generic bifurcation solver, complete Puiseux engine, multi-generator algebraic field, signed branch interference, or infinite-state claim is made.
