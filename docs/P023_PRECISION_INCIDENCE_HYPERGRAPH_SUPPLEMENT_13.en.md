# P023 — Higher-Order Precision Incidence Hypergraph, Supplement 13

Status: `PROVED RESEARCH NOTE`  
Owner: A2 / P023, with an A4 higher-order relation boundary  
Depends on: P023-S9/S11/S12 and finite joint partitions  
Discipline: hypergraphs, multiway intersections, and conditional extension degrees are established combinatorial structures. The project role is to identify the exact higher-order precision object and to state a reusable no-go theorem for pairwise summaries.

## 1. Why pairwise precision geometry is not enough

S12 gives a complete two-task incidence graph and an exact pairwise repair metric.

For three or more tasks, however, pairwise block intersections need not determine which block tuples have a simultaneous common state.

Therefore a pairwise metric can be correct and still be incomplete as a representation of joint task precision.

## 2. Realized precision hypergraph

Let

\[
E_1,\ldots,E_m
\]

be finite precision relations on the same finite state set `X`.

Define

\[
\boxed{
\Gamma(E_1,\ldots,E_m)
=
\{(B_1,\ldots,B_m):
B_i\in X/E_i,
\ \bigcap_i B_i\ne\varnothing\}.
}
\]

The elements of `Gamma` are realized block tuples, not all formal tuples in the Cartesian product.

## 3. P023-S13-T01 — Hyperedges are exactly joint precision classes

Status: `PROVED`.

The common refinement

\[
E_* = \bigcap_{i=1}^m E_i
\]

has one block for each realized tuple of component blocks. Hence

\[
\boxed{
|X/E_*|
=|
\Gamma(E_1,\ldots,E_m)
|.
}
\]

More strongly, the map

\[
[x]_{E_*}
\mapsto
([x]_{E_1},\ldots,[x]_{E_m})
\]

is a bijection from joint quotient classes to realized hyperedges.

Thus the precision hypergraph is an exact representation of the finite joint task quotient.

## 4. Formal-product defect

The formal candidate count is

\[
\prod_i |X/E_i|.
\]

Define

\[
\boxed{
U(E_1,\ldots,E_m)
=
\prod_i|X/E_i|
-
|\Gamma(E_1,\ldots,E_m)|.
}
\]

This counts formal task-label tuples with no realizing state.

The P017 warning about candidate supersets therefore extends directly to multi-task precision: a formal product can manufacture nonexistent joint states.

## 5. P023-S13-T02 — Pairwise-complete shadows do not determine the joint quotient

Status: `PROVED BY EXPLICIT COUNTEREXAMPLE`.

Take eight states and three binary precision tasks.

System A realizes the four even-parity triples

\[
000,\ 011,\ 101,\ 110,
\]

each twice.

System B realizes all eight binary triples exactly once.

For both systems:

- each individual partition has two blocks of size four;
- every pairwise incidence graph is the complete `2 x 2` bipartite graph;
- every pairwise intersection cell has cardinality two;
- every pairwise directed repair factor is two;
- every pairwise S12 distance is therefore identical.

Yet

\[
\boxed{
|X/(E_1\cap E_2\cap E_3)|=4
\quad\text{in System A},
}
\]

while

\[
\boxed{
|X/(E_1\cap E_2\cap E_3)|=8
\quad\text{in System B}.
}
\]

Thus even the complete collection of weighted pairwise incidence shadows does not determine three-task precision.

This is a hard no-go boundary for any theory that tries to reconstruct joint precision from pairwise distances or pairwise overlap counts alone.

## 6. Conditional extension sets

Suppose tasks `E_1,...,E_m` are already retained and task `F` is added.

For one realized prefix tuple

\[
\tau=(B_1,\ldots,B_m)
\in\Gamma(E_1,\ldots,E_m),
\]

define

\[
\boxed{
\operatorname{Ext}_F(\tau)
=
\{C\in X/F:
B_1\cap\cdots\cap B_m\cap C\ne\varnothing\}.
}
\]

This is the set of `F` labels still possible after the entire known context is fixed.

## 7. P023-S13-T03 — Conditional repair factor is maximum hyperedge extension degree

Status: `PROVED`.

The current context partition is

\[
C=E_1\cap\cdots\cap E_m.
\]

Adding `F` refines each context block according to the distinct `F` blocks it meets. Therefore the exact minimum repair alphabet is

\[
\boxed{
\rho(F\mid E_1,\ldots,E_m)
=
\max_{\tau}
|\operatorname{Ext}_F(\tau)|.
}
\]

This is precisely P023-S9 applied to the current joint context.

For `m=1` it reduces to the maximum left degree of the S12 bipartite incidence graph.

## 8. P023-S13-T04 — More retained context cannot increase the same task cost

Status: `PROVED`.

If `C'` refines `C`, then every `C'` block is contained in one `C` block. Hence the set of possible `F` labels inside a finer context block is a subset of the labels possible inside the old block.

Therefore

\[
\boxed{
\rho(F\mid C')
\le
\rho(F\mid C).
}
\]

This is a purely finite partition theorem: conditioning by more exact context can only lower or preserve the worst-case extra repair alphabet.

No probability or entropy is involved.

## 9. Parity example: higher-order context can erase a task completely

In System A from T02, the third bit is determined by the first two because

\[
E_3=E_1\oplus E_2
\]

on the realized state set.

Hence

\[
\rho(E_3\mid E_1)=2,
\]

but

\[
\boxed{
\rho(E_3\mid E_1,E_2)=1.
}
\]

Once two tasks are retained, the third task needs no nonconstant repair state.

In System B, all eight triples are realized, so

\[
\rho(E_3\mid E_1,E_2)=2.
\]

The two systems are pairwise indistinguishable but have different conditional repair structure.

## 10. P023-S13-T05 — Conditional higher-order repair spectrum

For each realized context tuple `tau`, write

\[
e_\tau=|\operatorname{Ext}_F(\tau)|.
\]

Define

\[
\boxed{
\mathcal R_k(F\mid C)
=
\sum_\tau\binom{e_\tau}{k}.
}
\]

This is the S11 repair spectrum of the quotient projection

\[
X/(C\cap F)\to X/C.
\]

Thus the hypergraph does not only determine the worst conditional repair factor; it determines the full distribution and higher-order repair ambiguity of the task addition.

## 11. Relation to A4

A4 already warns that pairwise support shadows can lose higher-order witness identity.

S13 is the precision-partition analogue:

\[
\boxed{
\text{pairwise block incidence}
\not\Rightarrow
\text{joint realized incidence}.
}
\]

This is not a coincidence. Both are statements about projecting a higher-order finite relation to lower-order shadows.

Therefore future A2/A4 bridges should treat realized higher-order tuples as first-class when the declared task can query them.

## 12. Research-tool rule

For more than two precision axes:

1. pairwise graphs are useful diagnostics and geometry;
2. they are not a sufficient joint state unless a separate theorem proves pairwise completeness;
3. build the realized tuple hypergraph or an equivalent compact representation;
4. compute conditional repair from extension degrees of the current realized context;
5. only then compress higher-order state.

This prevents a pairwise shadow from being silently promoted into a full future-compatible quotient.

## 13. Executable specification

- `src/enterprise_math/precision_incidence_hypergraph.py`
- `tests/test_precision_incidence_hypergraph.py`

The regression pins the even-parity versus full-cube counterexample, including equality of all weighted pairwise incidence shadows and inequality of the three-way joint quotient. It also verifies conditional-repair monotonicity and the higher-order repair spectrum.

## 14. Foundation boundary

The incidence hypergraph is an exact mathematical representation of declared finite tasks. It does not imply that every possible physical observable should be retained simultaneously.

Its foundational role is narrower and testable:

> whenever a future language requires several task coordinates jointly, the safe precision must respect their **realized higher-order incidence**, not merely their pairwise shadows.
