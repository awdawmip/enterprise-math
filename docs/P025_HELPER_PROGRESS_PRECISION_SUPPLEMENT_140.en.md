# P025 Supplement 140 — Exact progress precision inside a single raw-state fiber

Status: `PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner: `program/p025-helper-cache-stage139`

## 1. Fixed raw projection

Use the sequential `k`-way helper compiler and choose the raw seed

\[
S_{k-1}=\{a_1,\ldots,a_{k-1}\},
\]

with the final antecedent `a_k` absent.

The raw output can never fire, so the raw projection remains exactly `S_(k-1)` throughout execution.  Internally, however, the helper chain advances

\[
\varnothing,
\quad e_2,
\quad e_2,e_3,
\quad\ldots\quad,
 e_2,\ldots,e_{k-1}.
\]

After `e_(k-1)` is created, the state is stable because `a_k` is absent.

## 2. Exact fiber cardinality

There are exactly

\[
\boxed{k-1}
\]

legal internal states along this execution trace, all satisfying

\[
\boxed{\pi(T)=S_{k-1}.}
\]

Thus one raw-projection fiber can contain an arbitrarily long chain of legal runtime-memory states.

## 3. Remaining-round future separates every state

Index the trace states by `t=0,...,k-2`.  From state `t`, the exact number of remaining helper-update rounds before stability is

\[
\boxed{k-2-t.}
\]

These values are all distinct. Therefore, for the declared future language

> return the exact remaining number of internal rounds to stability,

every one of the `k-1` states is semantically distinct.

A natural exact repair coordinate is simply the progress index `t` (equivalently remaining rounds).

## 4. Endpoint/runtime collapse gap

The same fiber therefore exhibits the maximal contrast:

### Raw saturated endpoint language

All `k-1` transient states have the same raw endpoint and can collapse to one class.

### Internal runtime-progress language

All `k-1` states must remain distinct.

Hence

\[
\boxed{
\text{endpoint helper precision}=0
\quad\text{while}\quad
\text{runtime progress precision}=k-1\text{ discrete levels}
}
\]

inside the same raw semantic fiber.

## 5. Architectural consequence

The precision contributed by internal state is not determined by its storage dimension.  The same helper coordinates can be completely quotientable for one future and fully separating for another.

This gives a concrete state-level version of the earlier operation-language principle:

\[
\boxed{
\text{future language can create precision inside a fiber without changing the raw observable state at all.}
}
\]

## 6. Prior-art boundary

Progress counters, remaining-time sufficient state and deterministic execution traces are classical. No generic novelty claim is made. The project-side contribution is the exact finite family showing how endpoint cache becomes a `k-1`-level runtime memory coordinate under a richer future language.
