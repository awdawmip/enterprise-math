# PREFIX-807 — Exact residual-network certificates for a named source edge's feasible interval

Date: 2026-11-15 (Asia/Shanghai). Enterprise Math / BRC auxiliary source-flow model. Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Continues PREFIX-806. Historical research author `EM-DIRECT-4660FF`, activity `RA-63E1066C3056A93898BE8E18`.

Status: AUTHOR_PROVED / EXACT_INTEGER_REGRESSION / NOT_INDEPENDENTLY_REVIEWED.

## Problem and mathematical universe

PREFIX-806 filters observer-sufficient separator signatures by exact Hall feasibility. When all but one named crossing-edge value have been fixed, determine precisely which values of that final edge extend to a complete legal source table, and give integer witness/cut certificates without testing every candidate individually.

Let `G=(U ⊔ V,E)` be any finite bipartite **named-edge multigraph**; parallel edges retain independent names. Assign integral capacities `K_f>=0`, nonnegative integral vertex demands `d_v`, and a legal table `x∈Z^E` with `0<=x_f<=K_f` and `sum(f incident to v) x_f=d_v`. Fix the values of all edges in `F⊆E` to those in the legal table `x`, and select an unfrozen edge `e=(r,c)`, `r∈U,c∈V`, with `e∉F`.

The directed residual network `D_(e,F)(x)` contains the original bipartite vertices and, for each `f=(u,v)∈E\(F∪{e})`, a forward residual arc `u→v` of integral capacity `K_f−x_f` and a backward arc `v→u` of capacity `x_f`. Preserve named-edge identities when building witnesses; parallel arcs may be aggregated for computing maximum-flow values. Write `MF(a,b)` for the residual integral maximum-flow value from `a` to `b`. Signed additive observer weights are permitted, but do not affect existence of a legal source table.

## Theorem 807.1 — Complete interval and two integral residual-flow certificates

The attainable values of the selected named edge among all legal tables `y` respecting `y_f=x_f` for every `f∈F` are precisely the integer interval

```
{x_e - delta_minus, x_e - delta_minus + 1, ..., x_e + delta_plus},
delta_plus  = min(K_e - x_e, MF_D(c,r)),
delta_minus = min(x_e,       MF_D(r,c)).
```

Both endpoints have constructible complete integral tables as witnesses, and maximum-flow/minimum-cut gives an exact certificate excluding any further variation. This holds for every finite named bipartite multigraph, all integral demands and capacities, any frozen-edge subset, and any signed additive observer family.

**Necessity.** Let `y` be another legal complete table preserving the frozen edges, with `h=y_e−x_e>0`. On each other free named edge, the signed difference `y_f−x_f` is representable by a forward residual movement if nonnegative, or backward movement if negative, bounded by the respective residual capacity. Subtracting the vertex-demand equations for `x` and `y`, after separating the selected-edge increment, shows that these other movements have net residual source `c` and sink `r` of value `h`; any extra circulations can be removed. Therefore `h<=MF_D(c,r)`; the selected-edge capacity additionally gives `h<=K_e−x_e`. A decrease of magnitude `h` similarly needs a residual `r→c` flow of value `h` and satisfies `h<=x_e`.

**Sufficiency, including every intermediate integer.** By integral max-flow there is an integral `c→r` return flow of value `delta_plus`. Decompose it into integer-unit source–sink paths (plus any cycles, which may be discarded). For each `0<=h<=delta_plus`, take exactly `h` unit paths, change the other unfrozen edge counts by their net forward minus backward movements, and add `h` to `x_e`. The return flow cancels the selected-edge variation at every vertex, all edge counts remain integral within their capacities, and every frozen edge stays fixed. This constructs a legal table with `y_e=x_e+h`. The reverse construction using an `r→c` residual flow gives each `y_e=x_e−h`, `0<=h<=delta_minus`. A minimum cut achieves the exact upper bound for each directed return-flow computation. QED.

## Corollary 807.2 — Final separator variable and forced-edge test

In the PREFIX-804/805/806 separator algorithm, hold all but one crossing-edge count fixed. Once a legal complete table for that partial assignment is known, the remaining crossing-edge values form the interval above, with the other crossing edges included in `F`. Two residual flow calculations find all attainable values and endpoint witnesses. This permits skipping impossible crossing allocations while retaining *individual* signed observer exponents and multiplicities for every surviving allocation.

The selected edge is forced in the current frozen fiber exactly when `delta_plus=delta_minus=0`. If deleting it disconnects its endpoints in the free-edge graph, no directed residual return path exists and both deltas vanish. PREFIX-803's bridge-forced transfer theorem follows as a special case.

## Precise observer counterexample

Take the full 2×2 named grid, all four capacities equal to 2, and both row and column demand vectors equal to (2,2). The legal tables have `x_00=0,1,2`, one table for each value. For observer `Q(x)=2*x_00`, the exact Laurent/polynomial histogram is

```
H_Q(z)=1+z^2+z^4.
```

Thus the one-edge **feasible count** has no integer gap but an observed signed/integer weighted readout can have holes. Feasibility-interval compression is not itself an observer-safe quotient; preserve names, coefficients and declared observer weights.

## Standalone implementation and exact regression

The self-contained Python 3 program `PREFIX807_R6_EDGE_INTERVAL_CERTIFICATE_CHECK.py` uses only standard-library exact integers. An independent complete-table enumerator groups all named integer tables by achievable row and column demands. For every fiber and every selected edge, the checker obtains upper and lower values from residual Edmonds–Karp flows, reconstructs legal complete witness tables, and compares the endpoints and gaplessness against independent enumeration.

The one-frozen-edge extension exhausts every frozen-edge selection/value and then tests each other selected edge on the 2×2 capacity-2 and 2×3 capacity-1 families. It covers the partial separator assignment rather than only unrestricted full fibers.

| Grid | Capacity per edge | Patterns | Achievable margin fibers | Full named table occurrences |
|---|---|---:|---:|---:|
| 2×2 | 0,1,2 | 81 | 1,215 | 1,296 |
| 2×3 | 0,1,2 | 729 | 39,366 | 46,656 |
| 3×3 | 0,1 | 512 | 17,840 | 19,683 |
| 2×3 | 0,1 | 64 | 704 | 729 |

Across the run: **1,386** capacity patterns; **59,625** achievable fibers; **68,364** counted full named tables; **405,840** unrestricted edge-range certificates; **37,152** one-frozen-edge certificates; **2,214,960** integer assertions; all passed. There are 373,264 forced and 32,576 nondegenerate unrestricted edge intervals. The exact results are saved as `PREFIX807_R6_EDGE_INTERVAL_CERTIFICATE_RESULTS.json`.

The proof is universal in the declared mathematical model. The test is an exhaustive **finite** regression of the listed simple-grid families, not an empirical performance benchmark; the reference implementation has one named edge per row-column pair, while the theorem also allows parallel named edges.

## Relation to the frontier and next question

PREFIX-806 gives feasibility of a residual separator signature; PREFIX-807 gives an interval and endpoint certificates for one remaining named crossing variable once a legal full reference completion is known. These are complementary structural messages. The new certificate avoids repeated existence queries over the *same final variable* after obtaining a witness, and can be combined with observer-sufficient signature caching and Hall pruning without discarding provenance.

**Next research:** Implement the full separator algorithm using a first feasible completion per partially fixed crossing fiber, two residual maximum-flow interval calculations for its final free edge, and the existing Hall/signature plus Laurent-histogram machinery. Compare complete time, peak memory, observer-support cardinality and actual number of feasibility calls on reproducible sparse/dense families, including the cost of finding the initial witness. Separately seek a native X6 Cell/Link/Port/event-time readout whose permitted updates conserve exactly the required incidence constraints; no native X6 temporal theorem is claimed here.

Frozen scientific pin, P000, native world constraints, and shared CLAIM/Result/Review authority remain unchanged.
