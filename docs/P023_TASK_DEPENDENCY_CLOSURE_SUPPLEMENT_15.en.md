# P023 — Zero-Cost Task Dependency Closure, Supplement 15

Status: `PROVED RESEARCH NOTE`  
Owner: A2 / P023, with a P018 scheduling bridge  
Depends on: P023-S13 conditional repair and P023-S14 exact task scheduling  
Discipline: closure operators and functional dependencies are established mathematics. The project role is to identify zero-repair task implication as the exact closure notion induced by finite precision and to use it to compress the scheduling state space.

## 1. Zero repair is a dependency relation

Let a finite task family be

\[
\mathcal T=\{E_1,\ldots,E_m\}
\]

on a finite state set `X`.

For a subset of already retained tasks

\[
S\subseteq\mathcal T,
\]

write

\[
C_S=\bigcap_{E\in S}E
\]

for the current joint context, with the empty intersection equal to the universal one-block relation.

A task `F` is already determined by `S` exactly when adding it costs no nonconstant repair:

\[
\boxed{
\rho(F\mid C_S)=1.
}
\]

By P023-S12 this is equivalent to

\[
C_S\subseteq F.
\]

Thus `F` is literally a function of the currently retained precision state.

## 2. Task dependency closure

Define

\[
\boxed{
\operatorname{cl}(S)
=
\{F\in\mathcal T:C_S\subseteq F\}.
}
\]

Equivalently,

\[
\boxed{
F\in\operatorname{cl}(S)
\iff
\rho(F\mid C_S)=1.
}
\]

This is the set of all tasks that can be added for zero extra repair without changing the current joint partition.

## 3. P023-S15-T01 — Dependency closure is a closure operator

Status: `PROVED`.

The map

\[
S\mapsto\operatorname{cl}(S)
\]

is:

1. extensive:
   \[
   S\subseteq\operatorname{cl}(S);
   \]
2. monotone:
   \[
   S\subseteq T
   \Longrightarrow
   \operatorname{cl}(S)\subseteq\operatorname{cl}(T);
   \]
3. idempotent:
   \[
   \boxed{
   \operatorname{cl}(\operatorname{cl}(S))
   =
   \operatorname{cl}(S).
   }
   \]

### Proof

Extensivity is immediate because `C_S` refines every member of `S`.

If `S subseteq T`, then `C_T subseteq C_S`. Hence every task determined by `C_S` is also determined by the finer context `C_T`, proving monotonicity.

For idempotence, every task in `cl(S)` is already a function of `C_S`; intersecting those determined tasks with `C_S` does not refine the context. Therefore

\[
C_{\operatorname{cl}(S)}=C_S,
\]

so the same tasks are determined after closing. ∎

## 4. P023-S15-T02 — Closure does not change the represented precision state

Status: `PROVED`.

For every task set `S`,

\[
\boxed{
C_{\operatorname{cl}(S)}=C_S.
}
\]

Thus dependency closure adds task names, not state distinctions.

This is the exact reason zero-cost tasks may be inserted automatically into a schedule without changing any later conditional repair factor.

## 5. Task bases

Call `S` a **task basis** when

\[
\boxed{
\operatorname{cl}(S)=\mathcal T.
}
\]

By T02 this is equivalent to

\[
\boxed{
C_S=C_{\mathcal T}.
}
\]

So a task basis is any subset of coordinates that already generates the complete declared joint precision.

Tasks outside a basis are mathematically redundant once the basis is retained.

This is a representation theorem, not a statement that those tasks are experimentally cheap to measure.

## 6. P023-S15-T03 — Higher-order dependencies need not be pairwise

Status: `PROVED` by the S13 parity example.

In the even-parity system,

\[
E_3\notin\operatorname{cl}(\{E_1\}),
\qquad
E_3\notin\operatorname{cl}(\{E_2\}),
\]

but

\[
\boxed{
E_3\in\operatorname{cl}(\{E_1,E_2\}).
}
\]

Thus dependency cannot in general be represented by a directed graph of pairwise implications.

The correct object is a closure system / dependency hypergraph.

This matches S13's conclusion that pairwise incidence geometry does not determine higher-order joint precision.

## 7. P023-S15-T04 — The closure system need not be matroidal

Status: `PROVED BY EXPLICIT COUNTEREXAMPLE`.

Use the five-state S14 greedy counterexample:

\[
A=(0,0,0,0,1),
\]

\[
B=(0,0,0,1,0),
\]

\[
C=(0,0,1,2,3).
\]

Task `C` determines both `A` and `B`, so

\[
A\in\operatorname{cl}(\{C\})
\setminus\operatorname{cl}(\varnothing).
\]

But `A` does not determine `C`:

\[
C\notin\operatorname{cl}(\{A\}).
\]

This violates the matroid closure exchange implication

\[
x\in\operatorname{cl}(S\cup\{y\})\setminus\operatorname{cl}(S)
\Longrightarrow
y\in\operatorname{cl}(S\cup\{x\}).
\]

Therefore generic precision dependency closure is not a matroid closure.

Consequently one cannot justify a universal greedy acquisition theorem by importing matroid exchange.

## 8. P023-S15-T05 — Exact scheduler may quotient its state space by dependency closure

Status: `PROVED`.

S14's subset DP appears to have up to

\[
2^m
\]

raw task-subset states.

But if two subsets have the same closure, they induce the same context partition by T02 and hence the same conditional repair costs for every remaining task.

Therefore DP states can be canonically replaced by the closure fixed points

\[
\boxed{
\mathfrak C
=
\{S\subseteq\mathcal T:\operatorname{cl}(S)=S\}.
}
\]

with

\[
|\mathfrak C|\le2^m.
\]

The inequality can be strict, sometimes dramatically so.

At each positive-cost step:

1. choose one task outside the current closed set;
2. pay its current conditional repair depth;
3. immediately replace the enlarged set by its closure, adding every newly determined task for free.

This produces exactly the same optimum as the raw subset DP.

## 9. Five-state example: one generator closes the entire task family

In the same S14 example,

\[
\boxed{
\operatorname{cl}(\{C\})=\{A,B,C\}.
}
\]

So `C` alone is a task basis.

By contrast,

\[
\operatorname{cl}(\{A,B\})=\{A,B\};
\]

the two apparently cheap binary tasks do not determine the four-way task.

The optimal schedule therefore has one positive-cost generator:

\[
\boxed{C}
\]

with binary cost `2`, after which `A` and `B` close for zero cost.

This is the structural explanation of the greedy failure in S14.

## 10. P017 interpretation

L065 gives two concrete two-task closure states.

At `k=11`, root precision determines least-prime precision:

\[
\boxed{
P\in\operatorname{cl}(\{R\}).
}
\]

Hence `{R}` is already a basis for the pair `{P,R}`.

At `k=1737`, neither task determines the other, since

\[
\rho(P,R)=2,
\qquad
\rho(R,P)=8.
\]

Thus both coordinates remain genuinely necessary in any basis for that two-task family.

The closure language therefore captures the basin-dependent structural reason behind L065's order reversal.

## 11. Research-tool rule

Before running an expensive multi-task scheduler:

1. compute the zero-repair dependency closure of the current context;
2. delete all tasks already in closure from the positive-cost choice set;
3. quotient DP states by closure equality;
4. identify small task bases when they exist;
5. do not assume pairwise dependencies are complete;
6. do not assume the closure is matroidal or that greedy basis construction is valid without a separate theorem.

This is an exact state reduction, not heuristic pruning.

## 12. Executable specification

- `src/enterprise_math/precision_dependency_closure.py`
- `tests/test_precision_dependency_closure.py`

Tests verify closure axioms on the S14 finite family, pin the nonmatroid exchange failure, identify `{C}` as the unique minimal basis, and compare the closure-state DP with the full subset DP.

## 13. Prior-art and novelty discipline

Closure operators, functional dependencies, implication closure, and attribute-closure style reasoning are established mathematics and database theory. Enterprise Math does not claim them as inventions.

The project-specific synthesis is the exact identification

\[
\boxed{
F\in\operatorname{cl}(S)
\iff
\rho(F\mid C_S)=1,
}

which makes zero-repair precision dependence the closure operation naturally generated by the existing P023 incidence calculus.
