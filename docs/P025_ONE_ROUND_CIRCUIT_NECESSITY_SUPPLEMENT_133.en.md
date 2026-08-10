# P025 Supplement 133 — Rooted circuits are mandatory at derivation depth one

Status: `PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner: `program/p025-closure-basis-stage130`

## 1. Setup

Let `cl=cl_Omega` be the finite conjunction closure from Stage 127.  A sound single-head implication basis `B` contains rules

\[
C\Rightarrow b
\]

with `b in cl(C)`, and is complete when iterative forward chaining recovers `cl(S)` for every seed `S`.

Stage 131 showed that some rooted circuits can be removed if additional derivation rounds are allowed.  This supplement fixes the opposite endpoint: **one parallel round**.

## 2. Necessity theorem

Assume `B` is sound and, for every seed `S`, one parallel firing round already produces `cl(S)`.

Then

\[
\boxed{
B\text{ contains every rooted closure circuit.}
}
\]

### Proof

Take an arbitrary rooted circuit

\[
A\Rightarrow b,
\qquad b\notin A.
\]

Starting from seed `A`, one-round completeness requires `b` to be added during that single round.  Hence `B` contains some rule

\[
C\Rightarrow b
\]

whose premise is already enabled at the initial seed, so `C subseteq A`.

Soundness gives

\[
b\in cl(C).
\]

But `A` is inclusion-minimal among premises forcing `b`.  Therefore `C=A`.

Thus the exact circuit rule `A -> b` must occur in `B`. Since the circuit was arbitrary, every rooted circuit is mandatory. QED.

The argument also covers empty-premise circuits recording mandatory labels.

## 3. Converse

Stage 130 proved that the complete rooted-circuit table reconstructs every closure in one parallel round. Therefore, among sound single-head implication representations,

\[
\boxed{
\text{full rooted-circuit table}
=
\text{unique inclusion-minimal one-round complete basis}.
}
\]

Indeed, every one-round complete basis must contain it; extra rules are semantically unnecessary for one-round completeness.

## 4. Why the Stage-131 redundancy is not a contradiction

For

\[
a\Rightarrow c\Rightarrow b,
\]

the rooted-circuit table contains

\[
a\Rightarrow c,
\qquad c\Rightarrow b,
\qquad a\Rightarrow b.
\]

Deleting `a -> b` preserves eventual closure but increases the required depth from one to two.  Hence the rule is

- mandatory under depth-one semantics;
- redundant under unrestricted iterative semantics.

Rule redundancy is therefore **future-runtime-relative**.

## 5. Exact resource endpoint

For a declared maximum derivation depth `D`, let `s_D(cl)` denote the least rule count of a sound complete single-head basis with worst-case parallel depth at most `D`.

This supplement determines the depth-one endpoint exactly:

\[
\boxed{
s_1(cl)=\#\{\text{rooted circuits of }cl\}.
}
\]

Stage 131 supplies examples with strictly smaller `s_D` when `D>1`.

## 6. Architectural consequence

Relation-law compression cannot be evaluated without the declared future execution language.  The same implication may be removable or indispensable solely because the allowed derivation depth changes.

Thus at least these coordinates must remain separate:

1. semantic closure;
2. rooted/direct relation-law content;
3. stored iterative basis size;
4. allowed/required derivation depth.

## 7. Prior-art boundary

Horn implication bases, forward chaining and transitive redundancy are classical. No generic novelty claim is made. The project-side contribution is the exact future-runtime-relative precision boundary and its use as a pressure test for A2/A4/Foundation layering.
