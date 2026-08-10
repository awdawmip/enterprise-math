# P023 — Conditional Repair Task Scheduling, Supplement 14

Status: `PROVED RESEARCH NOTE`  
Owner: A2 / P023, with an algorithmic bridge to P018 adaptive precision  
Depends on: P023-S13 conditional repair, S12 integer symbol depth, P018 finite dynamic-program selection  
Discipline: finite task ordering and dynamic programming are established algorithmic ideas. This supplement derives the per-step cost internally from exact precision incidence rather than assuming an external task price.

## 1. Same final precision, different acquisition cost

Let finite task partitions be

\[
E_1,\ldots,E_m.
\]

Their final joint precision

\[
E_*=\bigcap_iE_i
\]

is independent of task order.

However, the repair alphabet needed to add a task depends on which tasks have already been retained. Therefore the cost of **sequentially acquiring** the same final precision can depend on order.

This is a higher-order incidence effect, not a change in the final quotient.

## 2. Conditional repair profile of an order

Fix an order

\[
\sigma=(\sigma(1),\ldots,\sigma(m)).
\]

Set

\[
C_0=\top_X
\]

to be the universal one-block partition and recursively

\[
C_j=C_{j-1}\cap E_{\sigma(j)}.
\]

Define the exact conditional repair factor

\[
\boxed{
\rho_j
=
\rho(E_{\sigma(j)}\mid C_{j-1}).
}
\]

For an integer base `B>=2`, define the stage symbol depth

\[
\boxed{
c_j=L_B(\rho_j).}
\]

The total sequential depth of the order is

\[
\boxed{
C_B(\sigma)=\sum_{j=1}^m c_j.
}
\]

No probability, expected value, logarithm, or externally assigned observation cost is required.

## 3. P023-S14-T01 — Product-capacity bound

Status: `PROVED`.

At stage `j`, every current context block splits into at most `rho_j` child blocks. Therefore

\[
|X/C_j|
\le
|X/C_{j-1}|\rho_j.
\]

Iterating from the one-block context gives

\[
\boxed{
|X/E_*|
\le
\prod_{j=1}^m\rho_j.
}
\]

The right-hand side is the worst-case sequential repair capacity of that order.

Define the product slack

\[
\boxed{
S_\times(\sigma)
=
\prod_j\rho_j-|X/E_*|.
}
\]

It measures capacity allocated by stagewise worst cases but never simultaneously realized by the final joint task.

## 4. P023-S14-T02 — Integer depth lower bound

Status: `PROVED`.

Let

\[
D_*=L_B(|X/E_*|)
\]

be the minimum base-`B` symbol depth required merely to name all final joint classes.

Since

\[
|X/E_*|\le\prod_j\rho_j
\]

and

\[
L_B\!\left(\prod_j\rho_j\right)
\le
\sum_jL_B(\rho_j),
\]

we obtain

\[
\boxed{
D_*\le C_B(\sigma).
}
\]

Define the scheduling slack

\[
\boxed{
S_B(\sigma)=C_B(\sigma)-D_*\ge0.
}
\]

This is a completely integer measure of how much worst-case sequential coding capacity the chosen task order wastes beyond the final joint-state cardinality lower bound.

## 5. P023-S14-T03 — Exact equality criterion: uniform branching at every stage

Status: `PROVED`.

For one stage, equality

\[
|X/C_j|
=|X/C_{j-1}|\rho_j
\]

holds if and only if **every** current context block splits into exactly `rho_j` realized child blocks under the added task.

Therefore

\[
\boxed{
|X/E_*|=\prod_j\rho_j
}
\]

if and only if every stage has uniform branching across all currently realized context blocks.

### Proof

The new class count is the sum of the local split degrees of all old context blocks. Each degree is at most `rho_j`, so the sum reaches `number_of_old_blocks * rho_j` exactly when every local degree attains the maximum.

If any stage is strict, every later bound only multiplies positive integers, so final product equality can never be restored. ∎

Thus branch-dependent local repair is the exact source of product slack.

## 6. A four-state order-dependence witness

Take four states and three binary tasks

\[
A=(0,0,0,1),
\qquad
B=(0,0,1,1),
\qquad
C=(0,1,0,1).
\]

All three together separate all four states.

For order

\[
B\to C\to A,
\]

the factors are

\[
\boxed{(2,2,1)}
\]

and the binary depth is

\[
1+1+0=2.
\]

This reaches the final lower bound `L_2(4)=2` exactly.

For order

\[
C\to A\to B,
\]

the factors are

\[
\boxed{(2,2,2)}
\]

and the binary depth is

\[
1+1+1=3.
\]

The final precision is identical, but the second order pays one unnecessary binary symbol.

Therefore task order is a real finite-precision optimization variable.

## 7. P023-S14-T04 — Exact subset dynamic program

Status: `PROVED / EXECUTABLE`.

For a set `S` of already retained tasks, let

\[
C_S=\bigcap_{i\in S}E_i.
\]

Define

\[
\operatorname{OPT}(S)
=
\min_{j\notin S}
\left(
L_B(\rho(E_j\mid C_S))
+
\operatorname{OPT}(S\cup\{j\})
\right),
\]

with

\[
\operatorname{OPT}(\{1,\ldots,m\})=0.
\]

Because `C_S` depends only on the set of known tasks, not their order, this is an exact subset dynamic program with at most `2^m` context states.

The same recurrence can minimize the product capacity by replacing addition with multiplication.

This is the correct finite optimizer when no stronger structural theorem eliminates order dependence.

## 8. P023-S14-T05 — Cheapest-next greedy is not generally optimal

Status: `PROVED BY EXPLICIT COUNTEREXAMPLE`.

Take five states and tasks

\[
A=(0,0,0,0,1),
\]

\[
B=(0,0,0,1,0),
\]

\[
C=(0,0,1,2,3).
\]

From the universal context:

- `A` costs one binary symbol;
- `B` costs one binary symbol;
- `C` costs two binary symbols.

Therefore every heuristic that chooses a currently cheapest task must start with `A` or `B`.

If it starts `A -> B`, the depth profile is

\[
\boxed{(1,1,1)}
\]

for total cost `3`; the symmetric `B -> A` case is the same.

But if `C` is chosen first, its four-way observation already determines both `A` and `B`, so

\[
\boxed{C\to A\to B:\quad(2,0,0)}
\]

with total cost `2`.

Hence

\[
\boxed{
\text{locally cheapest next task}
\not\Rightarrow
\text{globally cheapest precision schedule}.
}
\]

The exact DP is genuinely needed in the general finite case.

## 9. P023-S14-T06 — More context can make an expensive task cheap or redundant

This is the scheduling form of S13 context monotonicity.

For any task `F` and contexts `C' subseteq C`,

\[
\rho(F\mid C')\le\rho(F\mid C).
\]

Therefore the cost of a task is **endogenous to the current precision state**.

It is not a fixed property of the task itself.

This explains both order dependence and greedy failure: paying for a richer task early may collapse the later costs of several apparently cheap tasks to zero.

## 10. Relation to P018 adaptive precision

P018 already contains finite dynamic programming for adaptive observation selection, but its cost model is externally supplied and its objective is predicate decision.

S14 solves a different problem:

- the per-step cost is derived internally from exact repair geometry,
  \[
  c(E_j\mid C)=L_B(\rho(E_j\mid C));
  \]
- the objective is to acquire a declared complete joint precision exactly.

The two frameworks can later be combined: externally expensive measurements and internally expensive precision repairs can coexist in one integer Bellman recurrence.

But they should not be conflated.

## 11. Research-tool rule

When several task coordinates must eventually be retained:

1. do not assign each task a fixed precision cost before context is known;
2. compute the current conditional repair factor from realized incidence;
3. detect tasks that become redundant after richer context;
4. use exact subset DP when task count is moderate;
5. search for structural fast paths only after the exact DP provides a falsification oracle;
6. report scheduling slack separately from final joint class count.

This turns task order into a controlled theorem/proof-compression problem rather than a heuristic workflow choice.

## 12. Executable specification

- `src/enterprise_math/precision_task_scheduling.py`
- `src/enterprise_math/precision_task_greedy.py`
- `tests/test_precision_task_scheduling.py`
- `tests/test_precision_task_greedy.py`

Regression pins the four-state order-dependence witness, verifies the uniform-branching equality criterion, checks the exact subset DP against exhaustive permutations, and records the five-state cheapest-next greedy failure.

## 13. Foundation consequence

Required precision is not only task-relative; **the cost of acquiring a multi-task precision is context- and order-relative even when the final quotient is fixed**.

This yields a sharper foundational picture:

\[
\boxed{
\text{precision state}
+
\text{next requested task}
\longrightarrow
\text{conditional repair cost}.
}
\]

A scalar task price independent of current context is therefore not foundationally adequate in the general finite theory.

## 14. Prior-art and novelty discipline

Dynamic programming, decision-tree ordering, and conditional coding ideas are established. Enterprise Math does not claim them as inventions.

The project-specific synthesis is the exact integer cost law derived from precision incidence,

\[
\boxed{
c(F\mid C)=L_B(\rho(F\mid C)),}
\]

its uniform-branching slack theorem, and its integration with the existing future-safe quotient/repair framework.
