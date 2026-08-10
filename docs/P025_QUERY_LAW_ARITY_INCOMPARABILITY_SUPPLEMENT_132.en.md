# P025 Supplement 132 — Query-generator arity and relation-law arity are incomparable

Status: `PROVED_WIP + EXECUTABLE_AUTHORED / NOVELTY_UNVERIFIED`  
Owner: `program/p025-closure-basis-stage130`

## 1. Two different arity resources

For a finite exact-state family `Omega`, let `cl=cl_Omega`.

The Stage-128 **query-generator horizon** is

\[
g(\Omega)
=
\max_{C\in\operatorname{Fix}(cl)}
\min\{|S|:cl(S)=C\}.
\]

It measures how many raw query labels are ever necessary to represent one conjunction-semantic class.

The Stage-130 **direct relation-law horizon** is

\[
h_{\rm circ}(\Omega)
=
\max\{|A|:(A,b)\text{ is a rooted minimal implication}\}.
\]

It measures the largest premise arity of an irreducible direct implication in the one-round circuit presentation.

These quantities answer different questions and admit no universal ordering.

## 2. Arbitrarily large `g` with zero `h_circ`

Let `P` have `w` labels and take the exact-state universe

\[
\Omega=2^P.
\]

Then

\[
cl(S)=S
\]

for every `S`: this is the identity closure.  Consequently there is no nontrivial implication `A -> b` with `b notin A`, so

\[
\boxed{h_{\rm circ}(\Omega)=0.}
\]

But the closed class `P` has only one generator under identity closure, namely `P` itself. Therefore

\[
\boxed{g(\Omega)=|P|=w.}
\]

The gap `g-h_circ` is thus unbounded.

## 3. Relation-law arity can exceed query-generator arity

Take

\[
\Omega=\{\{a\},\{b\},\{a,b,c\}\}.
\]

Its closed classes are

\[
\varnothing,\quad \{a\},\quad \{b\},\quad \{a,b,c\}.
\]

They are generated respectively by

\[
\varnothing,\quad\{a\},\quad\{b\},\quad\{c\},
\]

so

\[
\boxed{g(\Omega)=1.}
\]

However the closure contains the irreducible binary circuit

\[
\boxed{\{a,b\}\Rightarrow c,}
\]

hence

\[
\boxed{h_{\rm circ}(\Omega)=2.}
\]

Therefore `h_circ <= g` also fails in general.

## 4. Incomparability theorem

Across finite exact-state families there is no general inequality in either direction:

\[
\boxed{
g(\Omega)\not\le h_{\rm circ}(\Omega)
\quad\text{and}\quad
h_{\rm circ}(\Omega)\not\le g(\Omega).
}
\]

The two resources must be tracked separately:

1. **query-state arity** — how many labels are needed to name a future-equivalence class;
2. **relation-law arity** — how many antecedent labels can be jointly required by one irreducible implication.

Neither is a proxy for the other.

## 5. Architectural consequence

This adds a fourth separation to the current precision architecture:

- semantic state / closure class;
- query-generator arity;
- relation-law storage and premise arity;
- execution/derivation depth.

A system can have a trivial relation law but expensive queries (identity closure), or very cheap query normal forms but genuinely higher-order relation laws (the `a AND b -> c` fixture).

## 6. Prior-art boundary

Closure generators, implicational dimension and Horn-premise arity belong to classical closure-system/FCA/Horn theory. P025 claims no generic novelty. The reusable contribution is the exact counterexample-backed separation required by Enterprise Math precision accounting.
