# P023 — Precision Generator Rank Boundary, Supplement 19

Status: `PROVED RESEARCH NOTE`  
Owner: A2 / P023  
Depends on: P023-S15 dependency closure, S14/S17 acquisition cost  
Discipline: closure systems, generators, bases, and rank-like notions are established mathematics. This supplement records a negative boundary: generic task closure is not matroidal, so coordinate-count “dimension” is not intrinsic without extra hypotheses.

## 1. Why a basis count looks tempting

S15 defines a task basis as a subset `S` of the declared task family `T` satisfying

\[
\operatorname{cl}(S)=\mathcal T.
\]

Equivalently, the tasks in `S` already generate the complete final joint partition.

It is tempting to call the size of a minimal basis the “dimension” of the precision state.

That is not valid in the generic finite theory.

## 2. P023-S19-T01 — Inclusion-minimal task bases can have different cardinalities

Status: `PROVED BY EXPLICIT COUNTEREXAMPLE`.

Take four states carrying two binary coordinates

\[
A=(0,0,1,1),
\qquad
B=(0,1,0,1),
\]

and a bundled four-way task

\[
C=(0,1,2,3)=(A,B).
\]

Then

\[
\boxed{
\operatorname{cl}(\{C\})=\{A,B,C\},
}
\]

because `C` determines both binary coordinates.

Also

\[
\boxed{
\operatorname{cl}(\{A,B\})=\{A,B,C\},
}
\]

because the pair `(A,B)` determines `C`.

But neither `A` nor `B` alone determines the full joint state.

Hence both

\[
\boxed{\{C\}}
\]

and

\[
\boxed{\{A,B\}}
\]

are inclusion-minimal task bases, with cardinalities one and two respectively.

Therefore

\[
\boxed{
\text{cardinality of an arbitrary minimal task basis is not invariant}.
}
\]

## 3. Why this differs from matroid rank

In a matroid, all bases have the same cardinality, forced by exchange.

S15 already gives a direct closure-exchange counterexample, and T01 gives an even more operational consequence: basis cardinality itself is not constant.

Thus generic precision closure has no canonical matroid rank without additional structure.

Any route wishing to use a rank/dimension theorem must first prove an exchange-type axiom for its specific task family.

## 4. A minimum generator number still exists, but it is language-relative

Define

\[
\boxed{
g(\mathcal T)
=
\min\{|S|:\operatorname{cl}(S)=\mathcal T\}.
}
\]

This is a well-defined integer for a finite declared task family.

However, it is not determined by the final joint partition alone.

In the four-state example, if the primitive task language is only

\[
\{A,B\},
\]

then

\[
\boxed{g=2.}
\]

If the bundled coordinate `C=(A,B)` is added to the primitive task language, the final joint partition is unchanged but

\[
\boxed{g=1.}
\]

because `{C}` is now a basis.

Therefore generator number is an invariant of the **task language plus its dependency closure**, not of the semantic final precision state by itself.

## 5. P023-S19-T02 — Three different integer “size” notions must be separated

Fix integer base `B>=2` and final joint precision `E_*`.

### Semantic final-state depth

\[
\boxed{
D_B(E_*)
=L_B(|X/E_*|).
}
\]

This depends only on the final partition. It is the integer symbol-depth lower bound for naming final precision classes.

### Generator number

\[
\boxed{
g(\mathcal T)
=
\min\{|S|:\operatorname{cl}(S)=\mathcal T\}.
}
\]

This counts the smallest number of declared primitive task coordinates needed to generate the final precision. It depends on the task vocabulary.

### Operational acquisition depth

\[
\boxed{
A_B(\mathcal T)
=
\min_\sigma C_B(\sigma).
}
\]

This is the exact S14 minimum sequential symbol depth under the declared primitive task language. It depends on task cardinalities, dependencies, repair factors, and ordering.

These three integers answer different questions and should not be called one universal “precision dimension.”

## 6. P023-S19-T03 — Interface overhead separates semantic depth from acquisition depth

S17 defines

\[
\boxed{
H_B(\mathcal T)
=A_B(\mathcal T)-D_B(E_*)\ge0.
}
\]

This is the minimum overhead forced by acquiring the final precision through the declared primitive task interface.

Adding a direct bundled final task can change `g(T)` and `A_B(T)` while leaving `D_B(E_*)` unchanged.

Therefore:

\[
\boxed{
\text{semantic precision size}
\neq
\text{coordinate generator count}
\neq
\text{acquisition cost in general}.
}
\]

## 7. P023-S19-T04 — Bundling is a coordinate-language change, not a semantic refinement

Suppose a bundled task `C` is a deterministic function of already declared tasks and together with them induces no finer final partition.

Adding `C` to the primitive language does not change `E_*`.

But it may:

- reduce the minimum generator number;
- reduce the optimal acquisition depth;
- alter the set of minimal bases;
- create new zero-cost dependency closures.

Hence task-coordinate design is a representational degree of freedom distinct from the final task semantics.

This is the task-language analogue of S18's distinction between coordinate normalization and state-space quotient.

## 8. Consequence for “precision dimension” proposals

A proposed dimension should state explicitly which of the following it means:

1. final class cardinality/depth;
2. minimum number of primitive generators in a fixed task language;
3. minimum acquisition depth under a fixed primitive interface;
4. geometric/graph dimension of a separate state structure.

Without this declaration, the word “dimension” is ambiguous and can change merely because one bundled coordinate was added to the vocabulary.

In particular,

\[
\boxed{
\text{number of coordinates in one minimal basis}
}
\]

is not an intrinsic foundation-level invariant.

## 9. Relation to P012/P018/P023

- P012 supplies intrinsic geometric dimensions only after a primitive adjacency/geometry is declared.
- P018 supplies precision axes and ambiguity but does not make their raw coordinate count intrinsic.
- P023 supplies the task quotient, dependency closure, and acquisition calculus.

S19 therefore blocks a common category error: confusing the number of convenient observables with the intrinsic size of the precision state they jointly represent.

## 10. Research-tool rule

Before reporting a “precision dimension”:

1. test whether minimal bases have equal cardinality;
2. test closure exchange if a matroid/rank interpretation is intended;
3. compare task families with and without bundled coordinates;
4. report `D_B`, `g(T)`, and `A_B(T)` separately when they differ;
5. treat only `D_B` as invariant under changes of primitive task vocabulary that leave the final partition unchanged.

## 11. Executable specification

`tests/test_precision_dependency_closure.py` includes a four-state family whose inclusion-minimal bases are `{C}` and `{A,B}`, and verifies that adding the bundled coordinate changes minimum generator count from two to one while leaving the semantic final partition unchanged.

## 12. Prior-art and novelty discipline

Closure-system bases and generator numbers are established notions. The nonmatroid counterexample is elementary.

The project-specific value is the explicit separation of semantic precision depth, task-language generator count, and exact conditional acquisition depth inside the Enterprise Math precision calculus.
