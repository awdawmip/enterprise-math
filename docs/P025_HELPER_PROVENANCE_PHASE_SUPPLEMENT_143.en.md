# P025 Supplement 143 — Helper provenance is one-sided in runtime and biconditional at saturation

Status: `PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner: `program/p025-helper-cache-stage139`

## 1. Global validity can be localized

Stage 142's future-robust validity condition for the sequential compiler is

\[
e_j\Rightarrow(a_1\wedge\cdots\wedge a_j).
\]

Because helper `e_j` is built recursively, this high-arity condition is equivalent to the local provenance laws

\[
\boxed{e_2\Rightarrow a_1,\quad e_2\Rightarrow a_2,}
\]

and for `j>=3`,

\[
\boxed{e_j\Rightarrow e_{j-1},\quad e_j\Rightarrow a_j.}
\]

Induction down the helper chain recovers the full raw prefix. Conversely, the global prefix condition immediately implies every local dependency.

Thus auxiliary topology localizes the cache-validity law as well as the forward computation law.

## 2. Every legally reachable state is provenance-sound

Helpers start absent and can only be created by

\[
a_1a_2\Rightarrow e_2,
\qquad
 e_{j-1}a_j\Rightarrow e_j.
\]

Raw and helper labels are monotone once present. Therefore every helper that appears in any legally reachable transient state carries its prerequisites with it.

Hence every legal reachable state satisfies the local provenance implications above.

## 3. Runtime converse can fail

The reverse implication need not hold during execution.

For example, with raw seed

\[
\{a_1,a_2,a_3\},
\]

after the first parallel round the state contains `e_2` while `e_3` has not yet been produced. Therefore

\[
e_2\wedge a_3
\]

is true but

\[
e_3
\]

is false.

So runtime legality requires only

\[
\boxed{
e_j\Rightarrow(e_{j-1}\wedge a_j),
}
\]

not the converse.

## 4. Saturation adds cache completeness

At a legally saturated endpoint, every enabled helper rule has fired. Thus, for helpers,

\[
\boxed{
e_2\iff(a_1\wedge a_2),
}
\]

and

\[
\boxed{
e_j\iff(e_{j-1}\wedge a_j)
\qquad(j\ge3).
}
\]

Equivalently, the endpoint cache is both

- **sound**: every stored helper has valid provenance;
- **complete**: every satisfied local prerequisite has its helper materialized.

## 5. Relation-law phase transition

The same internal coordinates therefore obey different exact relation types at different future phases:

- transient/runtime state: one-sided provenance implication;
- saturated endpoint state: local biconditional/cache equality.

This is not a contradiction. Saturation itself is an additional future condition.

## 6. Precision consequence

The helper tree buys two localizations simultaneously:

1. forward high-arity computation is compiled into low-arity local rules;
2. global validity certificates are compiled into low-arity local provenance rules.

But the price remains auxiliary state plus a lifecycle/runtime contract. The law attached to those coordinates cannot be specified without also saying whether the state is transient or saturated.

## 7. Prior-art boundary

Data provenance, inductive invariants, materialized views and fixpoint completion are standard. No generic novelty claim is made. P025 contributes the exact phase-dependent law boundary inside the current precision architecture.
