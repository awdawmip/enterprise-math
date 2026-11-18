# R5 — 七节点双正向 Set 的十九态构造与一步有限约束

Date: 2026-11-16. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NUMERICAL_MILP_PROBE / NOT_REVIEWED.
Frozen scientific pin: `435e77af0d180eac32bd1f9c4c464bc4010b7551`.
Scope: auxiliary canonical genuine-source **seven-cycle** with budget 2 and only `Set_0(1)`, `Set_1(1)`. This is not an untyped claim about native six-axis heartbeat dynamics.

## Statement A — exact constructive all-horizon upper bound

Let `X={0,...,127}`, `q(u)=sum_{i mod 7} u_i u_{i+1}`. An output centre `r` is genuine-source-feasible for snapshot `u` iff

`G(r,u) := (u & ~r)==0 and 0<=q(r)-q(u)<=2`.

Let `U_a(u)=u | (1<<a)` for `a=0,1`. A deterministic Moore controller has 19 states labelled by these distinct centres:

```text
23,31,39,43,59,90,91,108,109,110,111,116,117,118,119,124,125,126,127
```

The two named transition maps `f_0,f_1` are given in `VERIFY_R5_K7_TWO_POSITIVE_UPPER.py`. States 23,31,39,43,59 are fixed under both maps. State 90 maps to 91 under `f_0` and to 90 under `f_1`; state 91 is fixed. The remaining twelve states form three independent four-state commuting reset squares: 108–111, 116–119 and 124–127.

**Theorem:** For every integer horizon `H>=0`, the 19-state controller faithfully serves all 128 initial source snapshots through every positive Set word of length at most H. Hence

```text
N_H(7,{Set_0(1),Set_1(1)},2) <= 19.
```

**Proof:** Consider the relation `R_0={(u,r): G(r,u)}`. Inductively retain

`R_{n+1}={(u,r) in R_n: (U_a(u),f_a(r)) in R_n for a=0,1}`.

This finite decreasing sequence stabilizes at `R_*`. By induction on word length, every pair in `R_*` satisfies genuine-source feasibility for *every* finite word; the converse follows by the maximal forward invariant relation property. The accompanying standard-library program computes 263 initial feasible pairs, reaches the greatest fixed point of **202 pairs in two pruning rounds**, and verifies that its projection onto raw `X` is all 128 snapshots. It separately checks that both internal Set maps are idempotent and commute. Thus the stated construction satisfies the unbounded-horizon contract. All calculations are exact integer/Boolean operations.

## Statement B — exact one-step Boolean MILP reduction (distinct undominated centres)

For any finite raw system `X`, source labels `C`, named actions `U_a` and source predicate `G`, a horizon-one controller using **at most one internal state for each centre in C** and at most M states exists iff the following 0–1 system is feasible. Define binary `x_r` (centre present), `y_{r,a,t}` (state r's successor on action a has source centre t), `z_{u,r}` (raw u can initialize state r). Require:

```text
sum_r x_r <= M
sum_t y[r,a,t] = x[r]                  (all r,a)
y[r,a,t] <= x[t]                        (all r,a,t)
z[u,r] = 0 if not G(r,u)
sum_{r:G(r,u)} z[u,r] >= 1              (all u)
z[u,r] <= sum_{t:G(t,U_a(u))} y[r,a,t] (all u,r,a)
all x,y,z in {0,1}
```

Proof in both directions: Read an existing controller's source labels, transitions and one viable initialization per raw u to obtain binary variables. Conversely a binary solution chooses exactly one successor target for every present state/action and each raw state's `z=1` starting point; the inequalities give initial and one-action source correctness. The reduction is exact for its declared distinct-label class, with no idempotence/commutation assumption on internal operations. Source-mask domination can be eliminated for this class when replacement preserves distinctness; when M equals the static minimum, distinctness is automatic even for an otherwise unrestricted controller.

## Scoped seven-node computational frontier

With `C` the **57 inclusion-nondominated genuine-source masks** on the seven-cycle, SciPy 1.17.0/HiGHS reported:

- static source cover optimum **17** with solver gap zero (128 raw states, 57 centres);
- the exact one-step distinct-nondominated-centre 0–1 model infeasible at **M=17**, and at **M=18**;
- a feasible **M=19** distinct-centre controller, whose concrete output and transition table was separately verified *without SciPy* for all future words as above.

Thus `N_1>=18` follows from the static-17 fact and the M=17 model infeasibility **under the stated correctness of the MILP infeasibility result**, while the unconditional constructive inequality `N_H<=19` has the independent integer fixed-point witness. The M=18 numerical obstruction currently covers the **distinct, nondominated-output** class. An unrestricted 18-state controller may duplicate a source label or contain a dominated label; its existence is not settled by that restricted computation. A solver-independent infeasibility certificate would strengthen the lower-bound evidence.

The separate `REPRODUCE_R5_K7_ONE_STEP_DISTINCT_MILP.py` reproduces the precise model, and `EXACT_R5_K7_TWO_POSITIVE_WITNESS.json` records the independently verified full-horizon upper witness. The code does not use the solver to validate the construction.

## Provenance and next discriminating question

Inherited comparison: R5 six-cycle, two positive Set commands, 10-state static and 11-state one-step/full-horizon optimum at `99ffd23b3812fb6aa76c463167a63a1fe2870bc5`, file `research_notes/portable_direct/r5_two_raise_pairwise_20261116/R5_TWO_POSITIVE_SET_PAIRWISE_CERTIFICATE_THEOREM.md`; frozen R5 prior seven-node single-control static 17/dynamic 17 at `bffcb11580db5949f44bf888e8b821a52e766550`. New work concerns **both positive controls** on seven nodes.

Next: decide whether an unrestricted 18-state controller exists (one duplicated source output is the first essential case, because 17 distinct labels are needed to cover the static universe); develop an exact finite exclusion/constructive witness beyond the nondominated-distinct model. The bounded two-clone mixed-integer formulation is an exploratory route; no completion result has been established for that search.

This is independent author-side research preservation. No formal R5 Task/CLAIM, protected Activity/Result/Review write, Foundation promotion or independent review is asserted.
