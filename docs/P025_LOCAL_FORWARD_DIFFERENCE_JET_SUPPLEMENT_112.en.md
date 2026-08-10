# P025 Supplement 112 — State-Relative Forward-Difference Jet

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-nonlinear-observable-stage107`  
Depends on: P025 Supplement 111  
Hard block: `NONE`

## 1. Worst-case degree is not realized precision

Stage111 proves the worst-case theorem

\[
\operatorname{ord}(\mathcal O_P)=\deg(P)+1.
\]

That does not mean every node at every state needs this order.

The realized local interaction depends on:

1. the polynomial observable `P`;
2. the node's base rank from always-selected old thresholds;
3. how many candidate thresholds that node actually crosses.

Stage112 computes this dependence exactly.

## 2. Local future-node model

Fix one future node.

Let

\[
R\ge0
\]

be its rank against the old thresholds, and suppose it crosses exactly `c` candidate thresholds.

After relabelling those crossed candidates, its selected rank is

\[
R+x_1+\cdots+x_c.
\]

With future-node selector `y`, the node contributes

\[
\boxed{
yP(R+x_1+\cdots+x_c).}
\]

## 3. P025-T257 — local coefficients are forward differences

For `k` distinct crossed candidate variables, the coefficient of

\[
yx_{i_1}\cdots x_{i_k}
\]

is exactly the `k`-th forward difference of `P` at `R`:

\[
\boxed{
\Delta^kP(R)
=
\sum_{t=0}^{k}(-1)^{k-t}\binom{k}{t}P(R+t).
}
\]

This is independent of which particular `k` crossed candidate labels are chosen; only their count matters locally because each selected threshold raises the rank by one.

For `k=0`, the coefficient is simply

\[
\Delta^0P(R)=P(R),
\]

corresponding to the future-node selector `y` alone.

## 4. P025-D51 — realized local action order

Let

\[
k_*:=\max\{0\le k\le c:\Delta^kP(R)\ne0\},
\]

when this set is nonempty.

Then the node's realized action-interaction order is

\[
\boxed{k_*+1.}
\]

If

\[
\Delta^kP(R)=0
\qquad
\text{for every }0\le k\le c,
\]

then the node is completely invisible to the declared observable under all available local candidate selections, and its realized order is `0`.

Since `Delta^kP=0` for `k>deg(P)`, the universal local cap is

\[
\boxed{
1+\min(c,\deg P).
}
\]

but actual order can be strictly smaller because of finite-difference cancellation.

## 5. P025-CE45 — exact cancellation boundary

Take

\[
\boxed{P(r)=r(r-1)=r^2-r.}
\]

At base rank

\[
R=0,
\]

we have

\[
P(0)=0,
\]

\[
\Delta P(0)=P(1)-P(0)=0,
\]

but

\[
\boxed{
\Delta^2P(0)=2.
}
\]

Therefore:

### One crossed candidate

If `c=1`, all available differences `k=0,1` vanish. The future node is invisible:

\[
\boxed{\text{realized order}=0.}
\]

### Two crossed candidates

If `c=2`, the second difference becomes available and is nonzero. The gated future response has

\[
\boxed{\text{realized order}=3.}
\]

So the same degree-two observable can jump directly from zero response to cubic response solely because the local crossed-candidate geometry changes.

## 6. Exact P025 arithmetic realization

Use again the exact `(q,p,m)=(3,41,2)` dyadic edge

\[
\frac1{22}<\frac{13}{22}.
\]

With no old thresholds, the future node has base rank `R=0`.

- Place one candidate threshold strictly between the two pressures: `c=1`, realized order `0` for `P(r)=r(r-1)`.
- Place two distinct candidate thresholds in the same interval: `c=2`, realized order `3`.

Thus the cancellation boundary is realized inside one fixed arithmetic transition.

## 7. Base rank also matters

For the same polynomial, at

\[
R=1,
\]

we have

\[
P(1)=0,
\qquad
\Delta P(1)=P(2)-P(1)=2.
\]

So with only one crossed candidate the realized order is now

\[
\boxed{2.}
\]

The observable and crossed-candidate count are unchanged; changing only the base old-threshold rank changes required precision.

## 8. State-relative precision law

Stage112 therefore replaces the coarse worst-case rule

\[
\deg(P)+1
\]

by the exact local rule

\[
\boxed{
\operatorname{ord}_{\rm local}(P;R,c)
=
1+\max\{k\le c:\Delta^kP(R)\ne0\},
}
\]

with value `0` when all available differences vanish.

The required local response order is jointly determined by

\[
\boxed{
(\text{observable},\text{current base state},\text{available action geometry}).
}
\]

## 9. Architectural consequence

A precision system should not instantiate worst-case observable order uniformly everywhere.

The degree of the observable determines a ceiling, but the actual state should activate only the forward-difference orders that are both:

- nonzero at the current base rank;
- reachable by the candidate-action geometry.

This is an exact algebraic model of **precision genesis by local future distinguishability**.

## 10. Prior-art / novelty boundary

Forward differences of polynomials and their local cancellations are classical discrete calculus. P025 claims none individually.

The project-side result is their exact use as a state-relative precision compiler over the arithmetic threshold/node pressure-test geometry. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 11. Executable assets

Added:

- `src/enterprise_math/abc_local_observable_jet.py`;
- `tests/test_abc_local_observable_jet.py`.

## 12. Generation boundary

Stages107–112 now form a coherent chain:

1. changing observable can force state refinement;
2. quadratic observable raises closure order from two to three;
3. the high-order response still comes from a low-dimensional common rank generator;
4. rank moments realize arbitrary finite interaction order;
5. arbitrary polynomial observables have worst-case order `deg(P)+1`;
6. realized order is local and controlled by forward differences plus reachable candidate geometry.

This is a natural freeze point. The next generation should test non-polynomial observables or non-total-order relation geometries.