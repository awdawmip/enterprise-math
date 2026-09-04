# BRC exact one-parameter selector chamber compiler

Date: 2026-09-04
Mode: TASK_RESEARCH
Status: research candidate; no Foundation promotion in this note
Parent: one-parameter selector event theorem, Sturm-signature root-rank line

## 1. Goal

A one-parameter selector problem naturally separates into two exact tasks.

### Task A: prove an event superset

Produce a nonzero polynomial

\[
E(t)\in\mathbb Q[t]
\]

whose real zeros contain every parameter value at which the declared selector state can change.

For polynomial selector families this may come from

\[
\operatorname{lc}_x(P_t)\operatorname{Disc}_x(P_t)P_t(r)
\]

for smallest-real selection, with an additional factor \(P_t(0)\) for smallest-positive selection.

### Task B: compile the complement

Once Task A is certified, compute the exact selector label on every connected component of

\[
\mathbb R\setminus Z_{\mathbb R}(E).
\]

This note solves Task B.  It deliberately does **not** infer or prove the event polynomial.

## 2. Exact real-event root state

Let

\[
E(t)=e_0+e_1t+\cdots+e_dt^d
\]

be nonzero.  Multiplicity of an event root is irrelevant for the complement geometry, so first replace `E` by its squarefree part.

Build the rational Sturm sequence of that squarefree polynomial.

A strict rational Cauchy bound gives

\[
-B<\alpha<B
\]

for every real event root \(\alpha\).

Recursively bisect rational intervals using exact Sturm root counts until every occupied interval contains exactly one real event root and the intervals are ordered/disjoint.  If a proposed rational split is itself a root, choose another rational interior split; no numerical perturbation is required.

The resulting event-root state is a finite ordered list

\[
\boxed{
\mathcal R(E)=
(I_1,\dots,I_m),
}
\]

where every \(I_j=[a_j,b_j]\subset\mathbb Q\) contains exactly one distinct real zero of `E`, and the roots satisfy

\[
\alpha_1<\cdots<\alpha_m.
\]

The intervals are only exact selectors for the algebraic boundaries; the chamber endpoints are the roots themselves.

## 3. Exact complement cells

The real event roots partition the parameter line into

\[
m+1
\]

open cells:

\[
(-\infty,\alpha_1),
(\alpha_1,\alpha_2),
\dots,
(\alpha_m,\infty).
\]

Choose one rational sample in every cell:

- before the first root, take a rational value below `a_1`;
- between adjacent roots, use any rational point between `b_j` and `a_{j+1}`; if the isolating intervals share a rational non-root boundary, that common boundary itself is a valid sample;
- after the last root, take a rational value above `b_m`.

Refine root intervals if necessary until a rational separator exists.

This gives exact sample points

\[
q_0,\dots,q_m\in\mathbb Q.
\]

## 4. Selector chamber compilation theorem

Assume an external theorem certifies:

> every selector transition parameter belongs to the real zero set of `E`.

Let

\[
\mathcal L(t)
\]

be any exact pointwise selector observer, for example:

- smallest-real Boolean state from a Sturm/root-rank query;
- smallest-positive Boolean state;
- a finite selector/root-rank label.

Then `L` is constant on every complement cell.  Therefore

\[
\boxed{
\mathcal C_E(\mathcal L)
=
\bigl[(I^{\rm cell}_j,\mathcal L(q_j))\bigr]_{j=0}^m
}
\]

is the complete exact event-cell labeling.

One selector evaluation per cell is enough.

## 5. Boundary events versus semantic changes

A zero of `E` need not be a genuine selector transition.

If two cells adjacent to the same event root receive the same label, then that event is **inactive at the cell-label level**.

This does not automatically remove the event point from the typed boundary:

- the polynomial may have a repeated root there;
- declared multiplicity may fail;
- the selector may be undefined exactly at the event;
- some other observer may care about the collision.

Thus the compiler may report

\[
\boxed{
\text{ACTIVE EVENT}
\quad\text{or}\quad
\text{LABEL-INACTIVE EVENT},
}
\]

but it does not erase typed event points merely because adjacent labels coincide.

## 6. Exact benchmark chambers

### Quadratic smallest-real

Event polynomial may be squarefreed to

\[
E(t)=t^2-4.
\]

Real events:

\[
-2,2.
\]

Cell labels:

\[
\boxed{\text{safe},\ \text{safe},\ \text{unsafe}.}
\]

Hence `-2` is label-inactive and `2` is active.

### Quadratic smallest-positive

The same event roots give

\[
\boxed{\text{unsafe},\ \text{safe},\ \text{safe}.}
\]

Now `-2` is active and `2` is label-inactive.

### Depressed cubic smallest-real

For

\[
x^3-3x+t,
\qquad r=-2,
\]

the event roots are again

\[
-2,2,
\]

and labels are

\[
\boxed{\text{safe},\ \text{safe},\ \text{unsafe}.}
\]

### One-real cubic smallest-positive

For

\[
x^3+x+t,
\qquad r=1,
\]

the real event roots are

\[
-2,0,
\]

and labels are

\[
\boxed{\text{safe},\ \text{unsafe},\ \text{safe}.}
\]

Both events are active; the selector chamber is disconnected.

### Degree-five non-split witness

For

\[
P_t(x)=(x^2+1)(x^2-x-1)(x-t),
\qquad r=1,
\]

an exact squarefree event polynomial may be taken as

\[
\boxed{
E(t)=t(1-t)(t^2-t-1).
}
\]

The four real event roots are

\[
\alpha=\frac{1-\sqrt5}{2},
\quad0,
\quad1,
\quad
\beta=\frac{1+\sqrt5}{2}.
\]

The five cell labels are

\[
\boxed{
\text{safe},\ \text{safe},\ \text{unsafe},\ \text{safe},\ \text{safe}.
}
\]

Thus the two irrational discriminant/collision events \(\alpha,\beta\) are label-inactive, while `0` and `1` are active.

The compiler discovers this from root isolation plus one sample per cell; it never materializes \(\sqrt5\).

## 7. Complexity boundary

For a supplied univariate event polynomial of degree `d`, the chamber count is at most

\[
d+1
\]

because there are at most `d` distinct real event roots.

The expensive symbolic problem of deriving `E` from a bivariate family is outside this compiler.

Likewise, for more than one real parameter the complement of the event hypersurfaces is no longer linearly ordered and connected-component computation becomes a genuine semi-algebraic geometry problem.

## 8. Observer interpretation

This compiler is another observer-driven quotient/construction:

- event polynomial controls where a selector label is allowed to change;
- one pointwise selector label represents an entire event-free interval;
- if richer observers are declared, the event polynomial and interval labels may need refinement.

The output is therefore tied to both:

1. the supplied event-boundary certificate;
2. the supplied pointwise observer.

## 9. Validation plan

The exact checker must:

1. implement squarefree rational event-root isolation using Sturm counts and rational Cauchy bounds;
2. verify each isolated interval contains exactly one distinct event root and no root lies outside the global bound;
3. construct rational samples for all complement cells;
4. compile the four low-degree benchmark label patterns;
5. compile the degree-five pattern with irrational event roots without radicals;
6. compare every compiled cell label against multiple independent rational samples from the same cell;
7. classify active versus label-inactive adjacent event roots;
8. verify event-polynomial multiplication by repeated factors does not change the compiled cell partition after squarefree reduction.

## 10. Hard boundaries

- EVENT_COVERAGE_CERTIFICATE is an input, not inferred by the compiler.
- EVENT_CELL_LABELING does not define selector behavior at the event roots themselves.
- LABEL-INACTIVE does not mean the event is removable for every observer.
- The compiler is univariate; no multi-parameter CAD/component solver is claimed.
- No numerical root solver, complete Puiseux engine, multi-generator algebraic field, signed branch interference, or infinite-state claim is made.
