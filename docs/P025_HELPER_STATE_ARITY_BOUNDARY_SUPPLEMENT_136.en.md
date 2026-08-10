# P025 Supplement 136 — Premise arity, derivation depth, and auxiliary state are separate resources

Status: `PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner: `program/p025-closure-basis-stage130`

## 1. Pure k-way raw closure

Fix raw labels

\[
a_1,\ldots,a_k,z,
\qquad k\ge2,
\]

and let the only nontrivial semantic consequence be

\[
\boxed{
a_1\wedge\cdots\wedge a_k\Rightarrow z.
}
\]

Equivalently, the exact states are all subsets except those containing every `a_i` while omitting `z`.

## 2. Fixed-alphabet theorem

For this closure, the complete rooted-circuit table has exactly one nontrivial circuit:

\[
\boxed{
\{a_1,\ldots,a_k\}\Rightarrow z.
}
\]

There is no sound nontrivial rule with any antecedent `a_i` as root, because the closure never creates raw antecedents.  A sound rule adding `z` must have a premise that already semantically forces `z`; with `z` excluded from its own premise, that requires every raw antecedent.

Consequently, on the **fixed raw alphabet**, every sound complete single-head implication basis must contain a rule of premise arity `k`.

Allowing more forward-chaining rounds does not help: before `z` appears, there is no new semantic label that can be generated and used as an intermediate consequence.

Hence

\[
\boxed{
\text{fixed alphabet}\quad\Longrightarrow\quad
\text{required max premise arity}=k
\text{ for every derivation-depth budget}.
}
\]

## 3. Auxiliary-state compilation

Now extend the internal alphabet by helper labels

\[
e_2,\ldots,e_{k-1},
\]

and use the Stage-135 binary chain

\[
a_1a_2\Rightarrow e_2,
\quad
 e_{j-1}a_j\Rightarrow e_j,
\quad
 e_{k-1}a_k\Rightarrow z.
\]

Starting from any seed containing only raw labels, forward chaining under the extended system and then projecting back to the raw alphabet produces **exactly the pure k-way closure above**.

The internal resources are

\[
\boxed{
\#\text{helpers}=k-2,
\qquad
\max\text{ premise arity}=2,
\qquad
\text{raw-seed depth}=k-1.
}
\]

Thus binary compilation is possible, but it is purchased with auxiliary state plus derivation depth.

## 4. Corrected interpretation of Stage 135

Stage 135 must not be read as

> more depth alone always lowers relation-law arity.

The correct statement is:

> a high-arity direct law can sometimes be compiled into lower-arity iterative laws when the runtime is permitted to introduce and retain suitable intermediate state.

Without auxiliary semantic/scratch coordinates, some high-arity laws remain irreducibly high-arity at every depth.

## 5. Three-axis law compiler

Relation-law representation therefore has at least the resource vector

\[
\boxed{
(\text{max premise arity},
\text{derivation depth},
\text{auxiliary-state dimension}).
}
\]

These are independent of the semantic raw closure itself.  A compiler may move along this resource frontier while preserving the declared raw future language under projection.

This also separates **semantic state precision** from **internal computational state**: helper labels need not be exposed as user-level observables merely because the implementation retains them.

## 6. Prior-art boundary

Auxiliary gates, Tseitin-style/intermediate variables, Horn compilation and circuit depth/arity tradeoffs are classical.  No generic novelty claim is made.  The project-side result is the exact hypothesis boundary preventing a false inference from Stage 135 and the explicit three-resource precision accounting.
