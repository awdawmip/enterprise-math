# P025 Supplement 131 — Implication-basis storage versus derivation depth

Status: `PROVED_WIP + EXECUTABLE_CHECKED / NOVELTY_UNVERIFIED`  
Owner: `program/p025-closure-basis-stage130`

## 1. Why Supplement 130 is not the end

The full rooted-circuit table is direct and one-round complete, but iterative forward chaining can make some rooted circuits globally redundant.

For the closure law

\[
a\Rightarrow c\Rightarrow b,
\]

the rooted circuits are

\[
a\Rightarrow c,\qquad c\Rightarrow b,\qquad a\Rightarrow b.
\]

Deleting `a -> b` leaves the same semantic closure because it can be reconstructed in two rounds through `c`.

Thus `minimal premise for one root` and `globally indispensable implication rule` are different notions.

## 2. Basis semantics

A finite single-head implication basis `B` consists of rules

\[
A\Rightarrow b.
\]

Starting from seed `S`, fire all currently enabled rules in parallel, repeat until no new labels appear, and denote the result by `cl_B(S)`.

`B` is sound and complete for `cl_Omega` when

\[
\operatorname{cl}_B(S)=\operatorname{cl}_\Omega(S)
\quad\text{for every }S\subseteq P.
\]

For a complete basis define its worst-case parallel derivation depth

\[
d(B)=\max_{S\subseteq P}
\min\{t:\text{parallel forward chaining reaches }cl_\Omega(S)\text{ by round }t\}.
\]

Storage can be measured by rule count or total premise literals.  These are representation costs, not semantic state dimensions.

## 3. Chain family: exact scalable separation

Let

\[
x_0\Rightarrow x_1\Rightarrow\cdots\Rightarrow x_n.
\]

The exact closed states are the empty set and the suffixes

\[
\{x_i,x_{i+1},\ldots,x_n\}.
\]

### Full rooted-circuit table

Every pair `i<j` gives a rooted circuit

\[
x_i\Rightarrow x_j.
\]

Hence the direct table has

\[
\boxed{\binom{n+1}{2}}
\]

rules and closes every seed in one parallel round:

\[
\boxed{d=1}.
\]

### Adjacent/Hasse basis

Keep only

\[
x_i\Rightarrow x_{i+1},\qquad 0\le i<n.
\]

This basis has exactly

\[
\boxed{n}
\]

rules, remains sound and complete, but seed `{x_0}` requires exactly `n` rounds:

\[
\boxed{d=n}.
\]

For single-head implications, these adjacent consequences are unavoidable for a minimum-rule representation of this chain closure; the adjacent basis therefore realizes the natural minimum-storage extreme.

## 4. Exact finite Pareto fixture

For four labels `x0,x1,x2,x3`, three explicit complete bases give

\[
\boxed{(\#\text{rules},d)=(3,3),(4,2),(6,1)}.
\]

The middle basis is the adjacent basis plus shortcut `x0 -> x2`.

Thus one semantic closure admits genuinely different relation-law coordinate charts with different execution costs.

## 5. Architectural consequence

A closure law should not be assigned a single scalar `relation precision` without specifying what the future runtime is allowed to do.

At least three resources are distinct:

1. semantic closure/state information;
2. stored implication-law size;
3. derivation/operation depth needed to reconstruct future consequences.

The full circuit table pays more storage to make semantic closure a one-round lookup.  A smaller iterative basis pays less storage but requires more future computation.

This is the relation-law analogue of earlier P025 chart/update Pareto boundaries.

## 6. Prior-art boundary

Horn bases, transitive reduction, forward chaining, derivation depth and shortcut tradeoffs are classical.  No generic novelty claim is made.  The project-side use is the exact placement of this tradeoff inside future-relative precision accounting.
