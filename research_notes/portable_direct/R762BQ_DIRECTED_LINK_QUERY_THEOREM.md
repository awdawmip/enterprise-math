# R762BQ — Exact Link-query complexity and BRC source repair for six-Port triad decompositions

Date: 2026-11-16 (Asia/Shanghai). Status: AUTHOR_PROVED_WITH_EXACT_FINITE_CHECK; independent review NOT_REVIEWED.
Task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, publication `TP2-8B7E13C5904A2D6F1142`. Research output is an **independent conditional incidence candidate**, not a formal Source Result.
Frozen scientific inputs are the task's `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389` P000 V5, P000 triadic balance and X6 torsor. Preserve P000's three-force arity, signed named native axes and native PERP_E=120 degrees. Source conditional predecessor: R762BP, `research_notes/portable_direct/R762BP_BRC_TRIADIC_PARTITION.md` at commit `131bd4d77341d0fc16e9a25c85fe44ac4d5ce726`, and its native Source HANDOFF `emr3-20261116-0042-r762bp-native-source-handoff-v1` (SUCCEEDED, Source `8cdd69ab56c8e1ac5d099ace518fc824ffa1073e`).

## Exact typed BRC carrier and observation interface

Let `B_2` be the 40 labelled permutations `sigma` of six named force Ports with cycle type `(3,3)`. Each cycle is one **directed internal triadic Link incidence**; its three cyclic rotations represent the same directed cycle. An element `sigma` contains two unordered oriented triads. This is a finite explicit positive-rational BRC branch carrier `F=sum_[sigma in B_2] (1/1)[sigma]`: each label, directed Link, provenance and multiplicity is retained. The weights are counting weights, neither signed-force cancellation nor physical mass.

A primitive *named directed-Link membership query* `Q_(a,b)` for `a!=b` returns one Boolean `1{sigma(a)=b}` at unit query cost. No query that directly reveals the entire outgoing neighbor is counted as one Boolean. Suppose `Q_(1,2)=1` is already known; its exact fiber `U` has eight states. For signed variant, signs on 1 and 2 are also already known, while each of Ports 3,4,5,6 carries an independent sign, accessible only by an individual sign-bit query `S_i`.

The observer/future-operation horizon is the entire family of named Boolean Link queries, and optionally these four sign-bit queries. All statements about losslessness and query cost are relative to this declared interface. The underlying branch source is preserved until such queries finish.

## Theorem 1 — Twenty informative named queries yield the exact query graph K4,4

There are 30 distinct ordered potential Links on six Ports. Under `Q_(1,2)=1`, exactly twenty are nonconstant, and **each nonconstant query is true on exactly two of the eight states**. They induce sixteen distinct truth sets; the four duplications are `Q_(2,c)=Q_(c,1)`, for `c=3,4,5,6`. Associate a graph vertex with each branch in U and an edge with each distinct two-state positive set. That graph is **exactly the complete bipartite graph K4,4**.

*Proof.* The cycle containing the fixed arrow `1->2` must be `(1 2 c)`, with `c` one of the remaining four labels. The complementary three Ports form one cycle with two orientations, giving 4*2=8 states. For `2->c` or `c->1` there are precisely two orientations on the complementary triple. For a directed edge `x->y` with distinct `x,y` among Ports 3..6, the third element `c` of the first cycle can be chosen from the two other Ports, and the directed edge fixes the orientation of the complementary cycle: exactly two states. All remaining named queries are constant. To certify the claimed graph, sort the eight states by their complete permutation arrays as in the verifier; the resulting bipartition by indices is `A={0,3,4,7}` and `B={1,2,5,6}`. The sixteen computed positive sets each join one A and one B, and each vertex has degree four. A four-regular simple bipartite graph on `4+4` vertices is K4,4. This last finite check is independently reproducible from the eight explicitly constructed permutations; no geometric or native-physics inference is used.

## Theorem 2 — Four *adaptive* additional Boolean Link queries are necessary and sufficient

Any decision tree recovering the entire labelled `sigma in U` from named Link yes/no answers has worst-case depth **at least four**. Indeed every informative query can eliminate at most two currently possible states when its answer is “no”. An adversary may answer “no” for the first three queries, leaving at least two of the original eight possibilities. No three-query tree uniquely decodes all eight states.

Four queries suffice: ask successively `2->3`, `2->4`, `2->5`, stopping on the first positive answer. If all three are negative, `c=6`. Once `c` is fixed, make one Boolean Link query on a directed edge of the complementary three-Port cycle to distinguish its two orientations (for example, with `c=3`, ask `4->5`). Total worst case: three membership tests plus one orientation test = **four**. This construction and lower bound are exact for the declared oracle.

## Theorem 3 — Five *nonadaptive* additional Link queries are necessary and sufficient

Fix a collection of Boolean Link queries in advance. Record the yes/no vector for each of the eight source states. Each informative query corresponds to a 2-vertex edge in the K4,4 query graph. Two graph vertices share the same incidence vector exactly when both are isolated, or both are endpoints of a connected component consisting of a single isolated edge. Thus a separating panel may have at most one isolated vertex and every other connected component must contain at least three vertices.

With at most four query edges on eight vertices, the graph has at least `8-4=4` connected components. A separating graph on eight vertices can have at most three components (a possible isolated vertex plus components of size at least three). Therefore **at least five queries** are required.

The five-query panel
```
2->3, 2->4, 2->5, 3->4, 5->6
```
gives eight different Boolean answer vectors. In permutation-array order they are `10001,10000,01001,01000,00110,00100,00010,00000`. This proves sufficiency without adaptivity.

**Exact optimum classification.** With five edges the separating query graph must comprise two tree components on respectively 3 and 4 vertices, plus one isolated vertex. Because K4,4 is complete, the count of *distinct truth-set panels* is exactly `8*(18*4+12)=672`. To derive this, choose the isolated vertex in eight ways; assume it lies in the left class. The remaining classes have sizes 3 and 4. A three-vertex tree containing (1 left, 2 right) is chosen in `3*C(4,2)=18` ways, leaving a `K2,2` with four spanning trees. Alternatively (2 left,1 right) is chosen in `C(3,2)*4=12` ways, leaving a `K1,3` with one spanning tree. The symmetric case is equal. When the four duplicate names `(2->c)` and `(c->1)` are treated as distinct observable query names, exhaustive enumeration of `C(20,5)=15504` named panels yields **1944** optimal labelled panels; the accompanying checker exhausts this finite assertion.

## Theorem 4 — Signed source, binary information and oracle costs are different resources

In the additionally sign-decorated candidate, the 8 labelled decompositions in U pair freely with 16 assignments on the four hidden Ports, yielding **128** branch states. An unrestricted fixed-length lossless index therefore requires exactly seven bits (`ceil(log2 128)`). Under the restricted *atomic* query interface of one Boolean Link membership or one individual hidden-Port sign bit per call, every complete decision path must query all four independent sign bits and there exists a sign-fixed slice whose Link-query tree needs four questions. Consequently the exact worst-case **adaptive** minimum is **8 atomic queries**, achieved by the four-query Link strategy followed by four signs. **Nonadaptive** reconstruction requires five Link queries and four sign queries, hence **9 atomic queries**.

This separates an entropy-sized BRC carrier index (7 bits) from the actual cost to recover provenance through the exposed one-bit Link/sign observer (8 or 9 queries). The initial `1->2` observation, and the already-known signs of 1 and 2, are not charged again.

## Exact computational witness and limitations

`R762BQ_DIRECTED_LINK_QUERY_VERIFY.js` deterministically enumerates all 40 oriented two-triad permutations via the least remaining Port, selects the eight states with `1->2`, enumerates all 30 ordered named Link predicates, verifies the 20 nonconstant predicates and 16 distinct 2-state positive fibers, constructs K4,4, enumerates all `C(16,5)=4368` distinct-pattern five-query sets and all `C(20,5)=15504` five-name panels, and solves the adaptive minimax by exact subset dynamic programming (217 memoized nontrivial subsets). The generated evidence JSON contains full permutation arrays and one explicit separating five-query panel. Boolean integers and exact finite enumeration only; no floating arithmetic, trigonometry or physical rotation simulation. Run: `node R762BQ_DIRECTED_LINK_QUERY_VERIFY.js > out.json`; compare `out.json` with the committed evidence.

## Next scientific question

Obtain the task's actual admissible signed `TRIADIC_CLOSURE_E` Cell/Port/Link event rule and the allowed V17/V29/V39 update interface, then restrict the above eight-branch conditional fiber and query family to permitted events. Recompute the query graph, adaptive and nonadaptive reconstruction costs under *native admissible* named Link and sign queries. Prove observer-safe descent only for declared future operations. Preserve previous coordinate observer and parity theorems at their published scopes.

## Control and attribution

Prior R762BP native Source HANDOFF `emr3-20261116-0042-r762bp-native-source-handoff-v1` has been read as `SUCCEEDED / SOURCE_HANDOFF_PUBLISHED`, Source commit `8cdd69ab56c8e1ac5d099ace518fc824ffa1073e`. A fresh R762BQ continuation read was submitted under `emr3-20261116-0120-r762bq-cont-read-v1`; its still-running read status is not an execution CLAIM. The files in this branch are independent author-side scientific preservation. No new authenticated Source Activity, official Task PROGRESS, formal Result or Driver review is inferred from a GitHub commit. Source exposure includes R762BP and earlier R762BO, P000 V5, the incumbent same-task research context.
