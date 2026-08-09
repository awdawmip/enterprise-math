# P023 — Context-Derived Repair Scheduling, Supplement 14

Status: `PROVED RESEARCH NOTE`  
Owner: A2 / P023, algorithmic bridge to P018 adaptive precision  
Depends on: P023-S13 conditional repair; P018 finite dynamic-programming discipline  
Discipline: finite subset dynamic programming and sequential coding bounds are established ideas. The project contribution is to derive the per-task integer cost endogenously from exact precision-incidence repair rather than assume a fixed external observation cost.

## 1. Final precision is order-independent; sequential cost is not

Let

\[
E_1,\ldots,E_m
\]

be finite precision relations on one state set `X`.

The final joint precision

\[
C_*
=
\bigcap_{i=1}^mE_i
\]

is independent of acquisition order.

Choose an order `sigma` and define

\[
C_0=\top
\]

to be the universal one-block relation, and

\[
C_j
=
\bigcap_{r=1}^jE_{\sigma(r)}.
\]

At stage `j`, define the exact conditional repair factor

\[
\boxed{
\rho_j
=
R(C_{j-1}\to C_j)
=
\rho(E_{\sigma(j)}\mid C_{j-1}).
}
\]

This is an endogenous cost: it depends on which tasks have already been retained.

## 2. P023-S14-T01 — Exact class-count recurrence

Status: `PROVED`.

For each current block `B in X/C_{j-1}`, let

\[
s_j(B)
=
\#\{C_j\text{ blocks contained in }B\}.
\]

Then

\[
\boxed{
|X/C_j|
=
\sum_{B\in X/C_{j-1}}s_j(B).
}
\]

By definition

\[
1\le s_j(B)\le\rho_j,
\]

so

\[
\boxed{
|X/C_j|
\le
|X/C_{j-1}|\rho_j.
}
\]

Iterating from the one-block context gives

\[
\boxed{
|X/C_*|
\le
\prod_{j=1}^m\rho_j.
}
\]

The right side is the worst-case sequential repair capacity of that task order.

## 3. P023-S14-T02 — Exact uniform-branching equality criterion

Status: `PROVED`.

At one stage,

\[
|X/C_j|
=
|X/C_{j-1}|\rho_j
\]

if and only if

\[
\boxed{
s_j(B)=\rho_j
\quad\text{for every }B\in X/C_{j-1}.}
\]

That is, every current context block must achieve the same maximal extension degree.

Consequently,

\[
\boxed{
|X/C_*|
=
\prod_j\rho_j
}
\]

if and only if **every stage** has uniform branching.

### Proof

The stage recurrence is a sum of `|X/C_{j-1}|` positive integers each bounded above by `rho_j`. Equality with their maximum possible sum occurs exactly when every term equals `rho_j`.

If any stage is strict, later class counts are each bounded by multiplication by the remaining positive factors, so the strict deficit can never catch back up to the original full product bound. ∎

Thus product slack is structural evidence of branch-dependent conditional precision.

## 4. Integer symbol cost

Fix an integer alphabet base

\[
B\ge2
\]

and reuse

\[
L_B(n)=\min\{\ell:n\le B^\ell\}.
\]

Define the stage depth

\[
\boxed{
d_j=L_B(\rho_j).}
\]

and total sequential depth

\[
\boxed{D_\sigma=\sum_jd_j.}
\]

Because

\[
|X/C_*|
\le
\prod_j\rho_j
\le
B^{\sum_jd_j},
\]

we obtain:

## 5. P023-S14-T03 — Final-state depth lower bound

Status: `PROVED`.

\[
\boxed{
L_B(|X/C_*|)
\le
D_\sigma
}
\]

for every acquisition order `sigma`.

Define the integer **depth slack**

\[
\boxed{
S_B(\sigma)
=
D_\sigma-L_B(|X/C_*|)
\ge0.
}
\]

It measures extra fixed-base worst-case symbol depth introduced by sequential task acquisition beyond the minimum depth needed merely to index the final joint classes.

This is not Shannon redundancy; no probability or expected code length is used.

## 6. P023-S14-T04 — Product slack

Status: `PROVED`.

Define

\[
\boxed{
P(\sigma)
=
\prod_j\rho_j,
\qquad
S_\times(\sigma)
=
P(\sigma)-|X/C_*|.
}
\]

Then

\[
S_\times(\sigma)\ge0,
\]

and

\[
\boxed{
S_\times(\sigma)=0
\iff
\text{every acquisition stage has uniform branching}.}
\]

Unlike `D_sigma`, product capacity retains the exact multiplicative repair alphabet sizes before conversion into base-`B` symbol depths.

## 7. P023-S14-T05 — Exact finite dynamic program for optimal ordering

Status: `PROVED / STANDARD ALGORITHM`.

For a subset `S` of already retained tasks, let

\[
C_S=\bigcap_{i\in S}E_i,
\]

with `C_empty=top`.

Because `C_S` depends only on the subset and not its acquisition history, the minimum remaining symbol depth satisfies the Bellman recurrence

\[
\boxed{
D(S)
=
\min_{i\notin S}
\left[
L_B(\rho(E_i\mid C_S))
+D(S\cup\{i\})
\right],
}
\]

with

\[
D(\{1,\ldots,m\})=0.
\]

Likewise the minimum product capacity satisfies

\[
\boxed{
P(S)
=
\min_{i\notin S}
\left[
\rho(E_i\mid C_S)
P(S\cup\{i\})
\right],
}
\]

with terminal value `1`.

This is a finite subset dynamic program with no probabilistic state.

## 8. Minimal four-state order-dependence witness

Take four states `0,1,2,3` and three binary tasks

\[
A=(0,0,0,1),
\]

\[
B=(0,0,1,1),
\]

\[
C=(0,1,0,1).
\]

The final common refinement has four singleton classes regardless of order.

### Efficient order B -> C -> A

The conditional factors are

\[
\boxed{(2,2,1).}
\]

After `B,C` the state is already fully distinguished, so `A` is redundant.

Hence

\[
P=4,
\qquad
D_2=1+1+0=2.
\]

Since the final joint precision has four classes,

\[
L_2(4)=2,
\]

so both product and depth slack vanish.

### Wasteful order C -> A -> B

The factors are

\[
\boxed{(2,2,2).}
\]

The first two tasks produce three context classes, and `B` still splits one of them. Thus

\[
P=8,
\qquad
D_2=3.
\]

The final precision is still exactly the same four singleton classes, but

\[
\boxed{S_2=1.}
\]

One full worst-case binary symbol has been introduced purely by acquisition order.

## 9. Relation to P018 adaptive precision

P018's existing adaptive decision algorithms assume externally supplied positive integer observation costs and optimize a predicate decision tree.

S14 solves a different problem:

- the goal is to retain an entire declared finite task family;
- the per-task cost is **not fixed**;
- it is generated from current precision context by
  \[
  L_B(\rho(E_i\mid C_S)).
  \]

The two frameworks are compatible. A future bridge may use context-derived repair cost inside a state/predicate-specific adaptive decision program, but that richer optimization is not assumed here.

## 10. Research-tool rule

When several observations/tasks will eventually be retained together:

1. do not assume a fixed independent storage/precision cost for each task;
2. compute conditional repair factors against the current joint context;
3. detect tasks that become redundant (`rho=1`);
4. inspect uniform branching to know whether sequential capacities are exact or slack;
5. when order matters materially, solve the finite subset DP instead of using a greedy static ranking without proof.

## 11. Executable specification

- `src/enterprise_math/precision_task_scheduling.py`
- `tests/test_precision_task_scheduling.py`

The regression pins the four-state order-dependence witness, checks final-depth lower bounds for every task permutation, verifies the uniform-branching equality criterion, and cross-checks the subset DP against exhaustive permutation search.

## 12. Foundation boundary

`S_B` and `S_x` are exact finite scheduling/encoding slack measures for declared mathematical precision tasks. They do not imply a thermodynamic cost, physical memory cost, or ontological information content without an additional realization model.
