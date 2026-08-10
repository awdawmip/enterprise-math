# P025 Supplement 138 — Auxiliary-state compilation requires a legality invariant

Status: `PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner: `program/p025-closure-basis-stage130`

## 1. What the helper compiler actually preserves

Let `X_raw` be the raw label state space of the pure k-way conjunction from Stage 136, and let `X_ext` add helper labels.  Write

\[
\iota:X_{raw}\to X_{ext}
\]

for the embedding that initializes every helper as absent, and

\[
\pi:X_{ext}\to X_{raw}
\]

for deletion of all helper coordinates.

Let `F_ext^*` denote saturated forward chaining of the extended helper rules.  The compiler satisfies

\[
\boxed{
\pi\bigl(F_{ext}^*(\iota(S))\bigr)
=
cl_{raw}(S)
\qquad\forall S\subseteq X_{raw}.
}
\]

This is the correct raw-semantic simulation statement.

## 2. It is not a homomorphism on arbitrary internal states

The stronger statement

\[
\pi(F_{ext}^*(T))=cl_{raw}(\pi(T))
\qquad\forall T\in X_{ext}
\]

is false.

For the sequential helper compiler, the final rule is

\[
e_{k-1}a_k\Rightarrow z.
\]

Artificially initialize

\[
T=\{e_{k-1},a_k\}.
\]

Then internal forward chaining produces `z`, so

\[
\pi(F_{ext}^*(T))=\{a_k,z\}.
\]

But

\[
\pi(T)=\{a_k\}
\]

and the pure raw k-way conjunction does not fire from one antecedent:

\[
cl_{raw}(\{a_k\})=\{a_k\}.
\]

Hence

\[
\boxed{
\pi(F_{ext}^*(T))\ne cl_{raw}(\pi(T)).
}
\]

## 3. Correct compiler contract

Auxiliary-state compilation therefore requires more than an output projection. It needs a declared admissible internal-state discipline, such as

1. helpers are absent at raw initialization;
2. helpers are created only by the declared internal rules;
3. only states reachable from legal raw embeddings are admitted when asserting raw semantic equivalence.

Equivalently, correctness is a **restricted simulation/refinement property**, not equality of the unrestricted extended state system with the raw system.

## 4. Precision consequence

Auxiliary state has two very different interpretations:

- **legal derived scratch/cache state** — implementation detail under a reachability invariant;
- **free observable state coordinate** — enlarges the semantic state space and can change raw futures.

These must not be conflated.

Thus the Stage-136 law-compiler resource vector needs a legality coordinate:

\[
\boxed{
(\text{premise arity},
\text{derivation depth},
\text{auxiliary-state dimension},
\text{admissible internal-state invariant}).
}
\]

The last item is qualitative unless a future language assigns an explicit complexity measure to the invariant.

## 5. Relation to partial-operation/future legality

The pattern mirrors the existing Foundation/P023 lesson that enabledness and legal domains are future-observable structure: a hidden-state representation is safe only when its legal-state contract is preserved.  This supplement is only a finite specialization/pressure test and does not claim a new generic simulation theorem.

## 6. Prior-art boundary

Simulation relations, refinement mappings, hidden-state initialization and invariant-restricted implementation correctness are standard transition-system/program-verification ideas.  P025 claims no generic novelty.  The project-side result is the exact counterexample preventing auxiliary-state dimension from being treated as a free precision trade.
