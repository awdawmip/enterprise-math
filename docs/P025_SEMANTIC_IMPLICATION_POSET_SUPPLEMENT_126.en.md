# P025 Supplement 126 — Semantic Membership-Implication Poset

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-nonideal-boundary-stage125`  
Depends on: P025 Supplement 125; A2/A4 future-state boundaries  
Hard block: `NONE`

## 1. Repair the relation, not the scalar precision

Supplement 125 shows that an external poset cannot safely normalize queries when exact states violate its downward-closure law.

But a nonempty finite exact-state family

\[
\Omega\subseteq 2^P
\]

still contains its own membership implications.

## 2. P025-D49 — semantic implication preorder

Define

\[
\boxed{
x\preceq_\Omega y
\iff
\forall X\in\Omega,
\quad y\in X\Longrightarrow x\in X.}
\]

Equivalently, the membership column of `y` over \(\Omega\) is pointwise bounded by the membership column of `x`.

This relation is reflexive and transitive, hence a preorder.

## 3. P025-T275 — every exact state is downward closed semantically

For every \(X\in\Omega\),

\[
y\in X,\quad x\preceq_\Omega y
\Longrightarrow
x\in X.
\]

Therefore every exact state is automatically a down-set of the semantic preorder.

The closure law that failed for the external order is restored by a relation generated from the actual exact-state semantics.

## 4. P025-T276 — maximality of the semantic preorder

Let \(R\) be any binary relation on \(P\) such that every exact state in \(\Omega\) is downward closed under \(R\). Then

\[
\boxed{R\subseteq\preceq_\Omega.}
\]

Indeed, if \(xRy\), safety of \(R\) says that every state containing \(y\) contains \(x\), which is exactly \(x\preceq_\Omega y\).

Thus \(\preceq_\Omega\) is the **largest membership-implication relation compatible with all exact states**.

This is an endogenous safe relation, not an externally imposed ontology.

## 5. Quotient always-coactive labels

Define

\[
\boxed{
x\sim_\Omega y
\iff
x\preceq_\Omega y
\text{ and }
y\preceq_\Omega x.}
\]

Then `x` and `y` have identical membership columns across every exact state.

Quotienting by \(\sim_\Omega\) gives a genuine finite poset

\[
\boxed{P_\Omega:=P/{\sim_\Omega}.}
\]

Every exact state projects to an order ideal of \(P_\Omega\).

Hence arbitrary Boolean exact states can always be represented as ideals after replacing the external relation by the maximal semantic implication quotient.

## 6. Exact geometry changes

The semantic poset can differ radically from an external order.

### External chain opens into a semantic antichain

Let external labels be `a<b`, but take exact states

\[
\Omega=\{\{a\},\{b\}\}.
\]

Neither label implies the other across \(\Omega\), so the semantic quotient has two incomparable labels and

\[
\boxed{\operatorname{width}(P_\Omega)=2.}
\]

The external width-one assumption was therefore semantically false.

### Always-coactive labels collapse

If every exact state contains `a` exactly when it contains `b`, then

\[
a\sim_\Omega b
\]

and the two labels become one semantic coordinate.

So semantic geometry may become both wider and smaller than the external label geometry.

## 7. Unary safe geometry is not yet the full query quotient

The semantic implication poset captures every **unary** membership implication. It makes antichain normalization safe again.

However it need not be the coarsest representation for conjunction queries. A restricted exact-state family may satisfy a higher-order law such as

\[
a\wedge b\Longleftrightarrow c
\]

without either `a` or `b` individually implying `c` or conversely.

Therefore

\[
\boxed{
\text{semantic implication poset}
\neq
\text{full conjunctive closure in general}.
}
\]

Stage 127 must upgrade from unary implication to the complete closure operator induced by the exact-state family.

## 8. Architectural consequence

Supplement 125–126 gives a new repair principle:

\[
\boxed{
\text{unsafe external relation}
\not\Rightarrow
\text{add scalar precision};
\quad
\text{first infer the safe semantic relation}.}
\]

The relation geometry itself is part of the task-relative state interface.

## 9. Relation to A2/A4

A2 owns safe future quotients and A4 owns arbitrary correspondence/support. Stage 126 is a specialization showing that a Boolean correspondence induces a largest unary implication preorder. It should be consumed as a diagnostic interface, not as a competing relation-algebra mother theorem.

## 10. Prior-art discipline

Logical implication preorders, quotient preorders and membership-column equivalence are elementary / standard formal concept and order-theoretic ideas. No generic novelty claim is made.

The project-side result is the exact use as a repair of the P025 width-saturation boundary. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 11. Executable assets

Added:

- `src/enterprise_math/semantic_implication_poset.py`;
- `tests/test_semantic_implication_poset.py`.

The executable layer verifies reflexivity/transitivity, largest-safe-relation maximality, semantic quotienting of coactive labels, exact-state idealhood, and examples where external chain geometry opens into semantic width two.

## 12. Next frontier

Stage 127 should derive the full conjunctive closure operator of \(\Omega\), prove that two raw conjunctions have identical future truth vectors iff their closures agree, and identify the semantic implication poset as only the unary fragment of that closure system.
