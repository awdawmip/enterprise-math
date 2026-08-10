# Finite Disjunction Preserves Profinite Exactness Under Literal Branch Semantics

Status: `RESEARCH BRIDGE / NONCANONICAL`

Finite branching is not itself an obstruction to exact descent. Under the correct local semantics, profinite exactness is closed under a finite labelled union.

## 1. Branchwise exactness

Let the exact labelled branches have integer solution sets

`S_lambda subseteq Z^n`, `lambda in Lambda`,

with Lambda finite.

Let their completed solution sets be

`S_hat_lambda subseteq Z_hat^n`.

Assume each branch is profinite-exact:

`closure(S_lambda)=S_hat_lambda`.

Affine integer branches are a main positive example.

## 2. Literal-union local semantics

Assume the unlabelled completed world law is exactly the labelled union:

`S_hat = union_(lambda in Lambda) S_hat_lambda`.

Equivalently, no coefficient quotient, support projection or other compiler has introduced extra unlabelled solutions outside all branch solution sets.

This is stronger than preserving the written syntax. It is the branch-reflection requirement at the completed semantic level.

## 3. Finite union commutes with closure

Because Lambda is finite,

`closure(union_lambda S_lambda)`

`= union_lambda closure(S_lambda)`.

Using branchwise profinite exactness:

`= union_lambda S_hat_lambda`

`= S_hat`.

Therefore the unlabelled finite disjunction is itself profinite-exact.

So:

`finite labelled union`

`+ literal local branch semantics`

`+ branchwise profinite exactness`

implies

`profinite exactness of the whole union`.

## 4. Why the ghost product escapes this theorem

The intersective ghost has three exact labelled square branches, but its modular product equation is **not** the literal union of those branch equations at composite moduli.

At mod15 the product has a root while all three labelled branches are empty.

Hence the completed/unlabelled solution set is strictly larger than the union of the completed labelled branch sets.

The theorem's local semantic hypothesis fails before branchwise descent is even relevant.

## 5. Infinite unions are different

For infinitely many exact branches, closure need not commute with union:

`closure(union_i S_i)`

can strictly contain

`union_i closure(S_i)`.

The infinite-label escape exhibits the witness-level analogue: every finite precision can choose a branch while no fixed branch survives globally.

A compact/proper witness parameter space can restore an appropriate projection theorem, but an arbitrary infinite discrete witness alphabet cannot.

## 6. Routing consequence

A finite disjunction should not automatically be compiled into a multiplicative polynomial and then reduced coefficientwise. If exact witness identity matters, the semantics-safe representation is the labelled union itself unless a theorem proves the alternative encoding remains branch-reflecting under the chosen coefficient precision.

This is the same design rule seen elsewhere:

> preserve the semantic relation first; compress its representation only after proving the compression respects the future/witness language.

Finite unions and topological closure are standard prior mathematics. The Enterprise Math value is identifying the exact hypothesis under which finite RELATION branching remains safe through profinite descent.