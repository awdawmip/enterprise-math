# P025 Supplement 144 — Scheduler freedom turns helper progress into an ideal lattice

Status: `PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner: `program/p025-helper-cache-stage139`

## 1. Same compiler, different scheduler language

Fix the balanced binary helper compiler from Stage 137 and assume all raw antecedents are already present while every helper and output `z` start absent.

Before `z` fires, compare two internal operation languages:

1. **synchronous parallel** — every round fires all currently enabled helper gates;
2. **asynchronous** — one may choose any one currently enabled helper gate and fire it, then repeat.

The semantic raw input and implication graph are identical. Only scheduler freedom changes.

## 2. Gate-dependency poset

Let `P_gate` be the finite poset on helper gates with

\[
u\le v
\]

when helper `u` is an ancestor prerequisite of helper `v` in the compiler DAG.

If helper `v` has completed, every helper ancestor of `v` must already have completed. Therefore every asynchronously reachable completed-helper set is an order ideal of `P_gate`.

## 3. Converse reachability

Let `I` be any order ideal of `P_gate`. Choose a linear extension of `I` consistent with the dependency order and fire its helpers one at a time in that order.

All raw leaf prerequisites are already present, and whenever a helper is reached in the linear extension all of its helper predecessors already lie in the completed set. Thus every step is enabled.

Therefore every ideal is reachable.

Hence

\[
\boxed{
\{\text{asynchronously reachable helper-progress states}\}
=
J(P_{gate}).
}
\]

This is an exact equality, not only an upper bound.

## 4. Return of antichain-boundary precision

Every ideal is uniquely represented by its maximal antichain boundary. Consequently the worst-case number of boundary generators is

\[
\boxed{\operatorname{width}(P_{gate}).}
\]

Thus the Stage113 `rank -> antichain boundary` transition reappears here as a **runtime scheduling effect** rather than an externally supplied observation geometry.

## 5. Exact fixtures

### Four-way balanced conjunction

There are two independent first-layer helpers. The helper poset is a two-element antichain:

\[
\operatorname{width}=2,
\qquad
|J(P_{gate})|=4.
\]

Synchronous pre-output execution visits only two helper states: none, then both.

### Eight-way balanced conjunction

The six helpers form two independent `V`-shaped subtrees. The helper-poset width is four and

\[
\boxed{|J(P_{gate})|=25.}
\]

Synchronous pre-output execution visits only three helper states, while asynchronous scheduling admits all 25 ideals.

## 6. Architectural consequence

Scheduler freedom is itself a state-precision generator.

With the same raw state, same implication rules, same helper coordinates and same endpoint semantics:

- deterministic synchronous scheduling yields one progress path;
- asynchronous scheduling yields an ideal lattice of legal progress states.

Therefore the runtime state type cannot be inferred from the compiler graph alone. It depends on the declared internal operation language.

This is a direct bridge between the P025 helper-state program and the earlier A2/A4/Stage113 poset-boundary precision program.

## 7. Prior-art boundary

Dependency posets, asynchronous event structures, order ideals and topological firing orders are classical concurrency/order theory. No generic novelty claim is made. P025 contributes the exact compiler-level specialization and the precision-architecture connection.
