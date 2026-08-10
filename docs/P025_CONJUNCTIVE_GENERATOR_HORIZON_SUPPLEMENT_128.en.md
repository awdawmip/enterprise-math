# P025 Supplement 128 — Exact Conjunctive Generator Horizon

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-nonideal-boundary-stage125`  
Depends on: P025 Supplements 126–127  
Hard block: `NONE`

## 1. Closed query classes still need generators

Supplement 127 identifies closure classes as the exact semantic states of conjunction queries. Stage 128 asks the operational question:

> how many raw labels are actually needed to name every closure class?

## 2. P025-D51 — minimum generator size

For a closed set

\[
C\in\operatorname{Fix}(\operatorname{cl}_\Omega),
\]

define

\[
\boxed{
g_\Omega(C)
:=
\min\{|S|:\operatorname{cl}_\Omega(S)=C\}.}
\]

Define the global conjunctive generator horizon

\[
\boxed{
g(\Omega)
:=
\max_{C\in\operatorname{Fix}(\operatorname{cl}_\Omega)}
g_\Omega(C).}
\]

This is the exact worst-case minimum arity required to represent every semantic conjunction-future class.

## 3. P025-T280 — exact arity meaning

Every raw conjunction query is equivalent to some generator of size at most

\[
g(\Omega).
\]

Conversely, by definition some closure class requires exactly

\[
g(\Omega)
\]

labels; no smaller uniform arity cap can represent all query classes.

Therefore

\[
\boxed{
g(\Omega)\text{ is the exact conjunction-operation arity horizon}.}
\]

Unlike raw label count or ambient poset width, this number is defined directly from the actual future equivalence relation.

## 4. P025-T281 — semantic width is only an upper bound

Let

\[
P_\Omega
\]

be the semantic implication quotient poset from Supplement 126.

A minimum-cardinality generator cannot contain two semantically equivalent labels: one would be redundant.

It also cannot contain two distinct unary-comparable classes. If

\[
x\preceq_\Omega y
\]

and both appear in a generator, then every exact state containing \(y\) already contains \(x\), so removing \(x\) leaves the same query extent and closure.

Hence every minimum generator projects to an antichain in \(P_\Omega\). Therefore

\[
\boxed{
g(\Omega)\le\operatorname{width}(P_\Omega).}
\]

## 5. P025-C43 — strict higher-order gap

Use the exact family

\[
\Omega
=
\{\{a\},\{b\},\{a,b,c\}\}.
\]

Supplement 127 gives semantic implication width

\[
\operatorname{width}(P_\Omega)=2.
\]

But the four closure classes are

\[
\varnothing,
\{a\},
\{b\},
\{a,b,c\}.
\]

They have generators

\[
\varnothing,
\{a\},
\{b\},
\{c\}
\]

respectively. Hence

\[
\boxed{g(\Omega)=1<2=\operatorname{width}(P_\Omega).}
\]

The unary width can therefore strictly overestimate true conjunction precision.

## 6. All-ideal scope recovers the poset-width theorem

Let \(P\) be a finite poset and take

\[
\Omega=J(P)
\]

to be the family of **all** order ideals.

Then the closure of a raw query is exactly the least ideal containing it:

\[
\boxed{
\operatorname{cl}_{J(P)}(S)=\downarrow S.
}
\]

Indeed every ideal containing \(S\) contains \(\downarrow S\), and \(\downarrow S\) itself is one of the exact states being intersected.

The minimum generator of an ideal \(I\) is its maximal antichain boundary \(\partial I\). Therefore

\[
\boxed{
g(J(P))=\operatorname{width}(P).}
\]

This recovers Supplements 114 and 120 exactly at their all-ideal scope.

## 7. Degenerate mandatory-state boundary

If the only exact state is the full universe \(P\), then

\[
\operatorname{cl}(\varnothing)=P
\]

and every query is equivalent to the empty query. Thus

\[
\boxed{g(\Omega)=0}
\]

although the semantic implication quotient contains one always-active equivalence class and has width one.

So even at unary width one, higher semantic certainty can collapse operation arity to zero.

## 8. Architectural consequence

The sequence of precision parameters is now:

\[
\boxed{
\text{ambient width}
\to
\text{semantic implication width}
\to
\text{closure generator horizon }g(\Omega).
}
\]

Each step can strictly decrease or change the relevant geometry.

The last quantity is task-relative and exact for conjunction futures; it is not merely a structural upper bound.

## 9. Relation to A2/A4

A2 owns generic future equivalence and A4 owns arbitrary admissible correspondences. Stage 128 supplies a finite Boolean specialization in which the coarsest operation arity can be calculated directly from closure generators.

No claim is made that arbitrary A4 relations admit a poset-width formula.

## 10. Prior-art discipline

Minimum generators of finite closure systems and implication bases are standard closure/FCA territory. No generic novelty claim is made.

The project-side result is the exact P025 pressure-test hierarchy and the strict arithmetic-independent boundary between unary width and full conjunction generator precision. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 11. Executable assets

Added:

- `src/enterprise_math/conjunctive_generator_horizon.py`;
- `tests/test_conjunctive_generator_horizon.py`.

The executable layer enumerates minimum generators, verifies the semantic-width upper bound, reproduces chain/diamond all-ideal width horizons, checks the strict `2 -> 1` higher-order gap and the zero-generator mandatory-state boundary.

## 12. Next frontier

Stage 129 should characterize exactly when the unary semantic implication relation is already complete for conjunctions. The expected condition is that the closure be generated by its singleton consequences (plus the always-active core), equivalently that no irreducible higher-order implication exists.
