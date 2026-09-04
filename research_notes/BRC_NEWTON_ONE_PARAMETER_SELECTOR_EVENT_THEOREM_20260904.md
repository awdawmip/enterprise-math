# BRC one-parameter selector event theorem

Date: 2026-09-04
Mode: TASK_RESEARCH
Status: research candidate; no Foundation promotion in this note
Parent: WBRC-T59/T60/T61, low-degree non-split selector research, Sturm-signature root-rank line

## 1. Motivation

Closed quadratic/cubic selector formulas expose exact chamber boundaries in low degree.  A generic parametric Sturm/CAD decomposition is much heavier than needed for one scalar parameter.

For a one-parameter polynomial family, there is a simple degree-independent event theorem:

> the real-root order relative to a fixed probe can change only when the polynomial degree drops, a multiple root occurs, or a root crosses the probe.

This gives a finite algebraic superset of all selector-transition parameters without solving any roots.

Discriminant/resultant continuity is classical prior art.  No generic chamber/CAD novelty is claimed.

## 2. Setup

Let

\[
P_t(x)=a_d(t)x^d+\cdots+a_0(t),
\]

where each coefficient \(a_j(t)\in\mathbb Q[t]\), and assume the family is not identically degree-deficient.

Fix a rational probe

\[
r\in\mathbb Q.
\]

Define the pointwise real-root rank

\[
\nu_t(r)=\#\{\alpha\in\mathbb R:P_t(\alpha)=0,\ \alpha<r\},
\]

counting distinct real roots whenever the specialization has no root at `r`.

## 3. Smallest-real event polynomial

Define the selector event polynomial

\[
\boxed{
E_{\rm real}(t)
=
a_d(t)\,\operatorname{Disc}_x(P_t)\,P_t(r).
}
\]

The three factors correspond to the only ways the rank relative to `r` can change:

1. \(a_d(t)=0\): degree drops and a root may pass through infinity;
2. \(\operatorname{Disc}_x(P_t)=0\): real roots may collide, split, or merge with a complex pair;
3. \(P_t(r)=0\): a real root crosses the probe `r`.

### Theorem: rank constancy on event-free intervals

Let `I` be a connected open interval of real parameter values such that

\[
E_{\rm real}(t)\ne0
\qquad\forall t\in I.
\]

Then

\[
\boxed{
\nu_t(r)\ \text{is constant on }I.
}
\]

Consequently the Boolean smallest-real selector state

\[
\nu_t(r)=0
\]

is constant on `I`.

### Proof interface

On `I`:

- degree is fixed;
- every root is simple;
- real roots cannot be created or destroyed because that would require a multiple root;
- no real root can cross `r` because `P_t(r)` never vanishes;
- no root can escape through infinity because the leading coefficient never vanishes.

The finite multiset of simple roots therefore moves continuously, preserving the number of real roots on each side of `r`.

## 4. Smallest-positive event polynomial

Now assume

\[
r>0.
\]

Smallest-positive selection depends on the number of roots in the open interval `(0,r)`.

Define

\[
\boxed{
E_{+}(t)
=
a_d(t)\,\operatorname{Disc}_x(P_t)\,P_t(r)\,P_t(0).
}
\]

If `I` is a connected interval on which

\[
E_+(t)\ne0,
\]

then both ranks

\[
\nu_t(r),
\qquad
\nu_t(0)
\]

are constant, hence

\[
\#\{\alpha\in(0,r):P_t(\alpha)=0\}
=
\nu_t(r)-\nu_t(0)
\]

is constant.

Therefore

\[
\boxed{
\text{smallest-positive selector state is constant on every }E_+\ne0\text{ interval.}
}
\]

The extra factor `P_t(0)` is necessary because a root crossing zero changes positive/non-positive status even when it never crosses the declared root `r`.

## 5. Event set is sufficient, not minimal

A zero of the event polynomial is a **possible** selector boundary, not necessarily a genuine change.

For example, in

\[
Q_t(x)=x^2+t x+1,
\qquad r=-1,
\]

the discriminant vanishes at

\[
t=\pm2.
\]

The smallest-real selector changes only at `t=2`; it remains stable across `t=-2` because the repeated competitor is still to the right of `r`.

Thus

\[
\boxed{
\text{actual selector boundary}\subseteq\{E=0\},
}
\]

and the inclusion can be strict.

## 6. Recovery of low-degree thresholds

### Quadratic smallest-real

For

\[
Q_t(x)=x^2+t x+1,
\qquad r=-1,
\]

\[
\operatorname{Disc}=t^2-4,
\qquad
Q_t(-1)=2-t.
\]

Hence

\[
E_{\rm real}(t)=(t^2-4)(2-t),
\]

with event points `-2,2`.  The selector is constant on the three complementary intervals, and exact pointwise tests show the stable union is

\[
t<2.
\]

### Quadratic smallest-positive

For the same cofactor but declared `r=1`,

\[
Q_t(1)=t+2,
\qquad
Q_t(0)=1,
\]

so the real event points are again `-2,2`.  The stable union is

\[
t>-2.
\]

### Cubic smallest-real

For

\[
Q_t(x)=x^3-3x+t,
\qquad r=-2,
\]

\[
\operatorname{Disc}=27(4-t^2),
\qquad
Q_t(-2)=t-2.
\]

Again the only real event points are `-2,2`; the stable union is `t<2` away from the typed boundary points.

### Cubic smallest-positive

For

\[
Q_t(x)=x^3+x+t,
\qquad r=1,
\]

\[
\operatorname{Disc}=-4-27t^2\ne0,
\qquad
Q_t(1)=t+2,
\qquad
Q_t(0)=t.
\]

Thus the only real selector event points are

\[
\boxed{-2,0},
\]

which exactly explain the disconnected chamber

\[
t<-2\ \lor\ t\ge0.
\]

The first event is a collision at the declared positive root; the second is a competitor crossing zero.

## 7. Degree-five non-split witness

Consider

\[
P_t(x)
=(x^2+1)(x^2-x-1)(x-t).
\]

The degree is fixed and the first quadratic has no real roots.  The only real discriminant events caused by the moving linear factor occur when `t` meets a real root of

\[
x^2-x-1,
\]

i.e. at the two algebraic roots

\[
\frac{1\pm\sqrt5}{2}.
\]

For a smallest-positive observer with

\[
r=1,
\]

additional event factors are

\[
P_t(1)=0\iff t=1,
\qquad
P_t(0)=0\iff t=0.
\]

Hence the real line is divided by four exact event values:

\[
\frac{1-\sqrt5}{2},\quad 0,\quad1,\quad\frac{1+\sqrt5}{2}.
\]

On each complementary interval the positive selector state is constant, despite the degree-five cofactor and irrational event locations.

This demonstrates that the event theorem scales beyond the low-degree closed selector formulas.

## 8. Exact validation strategy

Validation does not wait for a generic symbolic discriminant engine.

Use benchmark families whose event polynomials/factors are known exactly:

1. the quadratic smallest-real witness;
2. the quadratic smallest-positive witness;
3. the depressed cubic smallest-real witness;
4. the one-real cubic smallest-positive witness;
5. the degree-five product witness with algebraic discriminant-event roots.

For each family:

- isolate/order all real event values exactly or by rational Sturm brackets;
- choose multiple rational parameter samples in every event-free interval;
- compute pointwise selector/root-rank exactly by Sturm;
- verify the state is constant within each interval;
- verify every observed selector change is separated by at least one event value;
- preserve event points that do not change the selector as explicit over-approximation witnesses.

## 9. Relation to parametric chamber computation

For one scalar parameter, isolating the real roots of `E(t)` turns the theorem into a finite exact chamber decomposition problem.

For several parameters the analogous hypersurface union

\[
a_d\,\operatorname{Disc}\,P(r)\,(P(0))
=0
\]

still contains all selector boundaries, but computing connected components of its complement is a genuine semi-algebraic geometry/CAD problem.  That multi-parameter problem is not solved here.

## 10. Hard boundaries

- EVENT_SET is a sufficient boundary superset, not the minimal selector boundary.
- The theorem assumes polynomial coefficient dependence on one real parameter and fixed rational probe endpoints.
- Repeated-root event points themselves require separate boundary semantics.
- Smallest-positive requires the additional zero-crossing factor `P_t(0)`.
- No generic symbolic discriminant/resultant engine is promoted in this note.
- No multi-parameter CAD, complete Puiseux solver, multi-generator algebraic field, signed branch interference, or infinite-state claim is made.
