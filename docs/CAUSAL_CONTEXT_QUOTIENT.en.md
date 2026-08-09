# Causal Context Quotient — Coarsest Recursive State Under All Finite Composition Futures

Status: `ACTIVE CROSS-ROUTE RESEARCH WIP / ABSTRACT EXACT THEOREM`

Ownership: the general quotient/congruence mother theory should be consumed by A2/P023. This note is the binary-LEGO-composition, arbitrary-dimension specialization. The finite executable specialization is A3 contextual refinement.

## 1. Raw composition system

Let `X` be a possibly infinite raw state set with deterministic binary causal composition

\[
*:X\times X\to X
\]

and declared observation

\[
o:X\to O.
\]

A finite one-hole composition context is generated from the empty hole `[-]` by repeatedly adjoining a raw partner on the left or right.

## 2. CQ-01 — Contextual future equivalence

Define

\[
\boxed{
x\equiv_{ctx}y
\iff
o(C[x])=o(C[y])
\quad\text{for every finite composition context }C.
}
\]

Thus two states are equal exactly when no allowed finite LEGO composition future can distinguish them for the declared observation.

## 3. Observation descends

The empty context is included, hence

\[
x\equiv_{ctx}y\Rightarrow o(x)=o(y).
\]

Therefore `o` is well-defined on contextual classes.

## 4. CQ-02 — Contextual equivalence is automatically a congruence

If

\[
x\equiv_{ctx}x',\qquad y\equiv_{ctx}y',
\]

then

\[
\boxed{x*y\equiv_{ctx}x'*y'.}
\]

For an arbitrary outer context, first replace `x` by `x'` inside the derived context `C[[-]*y]`, then replace `y` by `y'` inside `C[x'*[-]]`. Hence the quotient operation

\[
[x]\star[y]=[x*y]
\]

is well-defined.

Traditional algebraic congruence is therefore a shadow of all-context future indistinguishability rather than the primitive starting point.

## 5. CQ-03 — Coarsest exact recursive quotient

Let `~` be any equivalence that is both observation-safe and composition-compatible. By induction on context construction,

\[
x\sim y\Longrightarrow o(C[x])=o(C[y])
\]

for every finite context `C`. Thus

\[
\boxed{x\sim y\Longrightarrow x\equiv_{ctx}y.}
\]

Every exact recursive quotient refines the contextual quotient. Therefore

\[
\boxed{X/{\equiv_{ctx}}\text{ is the coarsest exact recursive state for the declared composition/observation language}.}
\]

No finiteness assumption on `X` is needed for this theorem.

## 6. Raw algebraic laws descend

If raw `*` is associative, the quotient operation is associative. If raw `*` has an identity, its class is the quotient identity. The causal order is

\[
\boxed{
\text{raw LEGO law}
+\text{all-context future equality}
\to\text{quotient algebra shadow}.
}
\]

## 7. Finite weighted specialization

For finite raw witness spaces with weighted/multivalued joins `J(x,y;z,delta)`, A3's contextual refinement repeatedly splits by current observation and all left/right partner output profiles. The stable partition is the coarsest recursive-safe refinement and induces an exact typed weighted kernel. If the raw weighted join is associative, the typed kernel is associative.

Assets:
- `causal_weighted_context_refinement.py`
- `causal_recursive_join.py`
- corresponding tests

## 8. Relation to Myhill–Nerode

When composition becomes free-word append and the observation is Boolean language membership, the contextual quotient specializes to classical residual-language / Myhill–Nerode equivalence. Enterprise Math does not claim that automata theorem as new; it is a traditional specialization/tool of the causal future-context principle.

## 9. Higher-order interaction discipline

A high-order factorization failure in the currently exposed state language is not automatically an absolute n-body primitive. The correct route is

\[
\boxed{
\text{exposed failure}
\to\text{minimal contextual quotient}
\to\text{typed coherence test}
\to\text{higher primitive only if still necessary}.
}
\]

## 10. Boundary

Still open: infinite weighted/multivalued joins, effective computation of infinite contextual quotients, physical locality constraints, stochastic/quantum continuation, and Lean formalization.
