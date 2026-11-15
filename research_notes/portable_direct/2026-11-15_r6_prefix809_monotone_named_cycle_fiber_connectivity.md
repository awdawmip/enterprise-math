# PREFIX-809 — Monotone cycle connectivity of named BRC source fibers

**Date:** 2026-11-15 (Asia/Shanghai)
**Line:** Enterprise Math research6; independent auxiliary source-count research, successor to PREFIX-808.
**Frozen scientific pin:** `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
**Authority:** `EM-DIRECT-4660FF / TASK_RESEARCH` is the historical Activity contributor; no new shared CLAIM is inferred.
**Model and scope:** finite bipartite *named multigraph* with integer capacities `K_e >= 0`, prescribed integer row/column margins, and any externally fixed named edges. This is a source-counting / residual-preserving BRC auxiliary model, not an established native X6 Cell/Link/Port event-time evolution.

## 1. Precise theorem — monotone signed-cycle connectivity

Let `G=(U,V,E)` be a finite bipartite multigraph in which each named edge `e=(i,j)` has integer capacity `K_e`. Let
`F(R,S;K)={x in Z^E : 0<=x_e<=K_e, sum_{e:i(e)=i} x_e=R_i, sum_{e:j(e)=j} x_e=S_j}`.
Allow a set `Q subset E` of frozen edges with prescribed common values. For **every** pair `x,y in F` satisfying those frozen values, there exists a finite sequence `x=x^0,...,x^m=y` such that:

1. Each transition is an integer **unit signed directed simple-cycle** move in the named bipartite residual graph.
2. Every intermediate table remains in `F` and respects all frozen values. Each edge value stays between its values in `x` and `y`.
3. For each move `C`, `||x^{k+1}-y||_1=||x^k-y||_1-|C|`. The cycle length is even, at least 2 for a named multigraph and at least 4 if no parallel edges occur. Consequently `m <= floor(||x-y||_1/2)`, improved to `m <= floor(||x-y||_1/4)` for a simple bipartite graph.
4. For any finite family of integer signed edge-weight observers `W_l(x)=sum_e w_{l,e}x_e`, the exact observer increment along `C` is `sum_{e in C} epsilon_C(e) w_{l,e}`. Therefore source identities, multiplicity and every declared joint observer can be transported along this path without merging or guessing intermediate counts.

The projection of the feasible fiber to any named selected edge set `T` is connected under **projected cycle moves** induced by such feasible full-table steps. A projected move may affect several coordinates simultaneously or may be zero; the full named cycle remains the sufficient transition witness. This establishes a finite constructive complement to PREFIX-808's integer-projection cut saturation.

## 2. Proof

Let `d=y-x`. For each named edge with `d_e>0`, orient one residual arc **row to column** with multiplicity `d_e`; for `d_e<0`, orient **column to row** with multiplicity `-d_e`. As `x,y` have the same row and column margins, directed indegree equals outdegree at every vertex, counting multiplicity. If `d != 0`, this finite nonzero balanced directed multigraph contains a simple directed cycle `C` (follow positive outgoing arcs until a vertex repeats and take a minimal cycle).

Update `x_e` by `+1` on row-to-column arcs of `C`, by `-1` on column-to-row arcs, leaving all other values unchanged. Every vertex has exactly one incoming and one outgoing arc along `C`; hence its prescribed margin is unchanged. The sign of each update agrees with `y_e-x_e`. Therefore an increased entry is at most `y_e<=K_e` and a decreased entry is at least `y_e>=0`. Frozen edges have `d_e=0` and do not appear. Every changed edge reduces its absolute discrepancy by exactly 1, yielding the claimed strict decrease in `L1`.

Repeat while `x != y`. Since nonnegative integer distance strictly decreases, the process terminates and the cycle-length bounds follow. Observers are integer linear, so their increment is the signed weight sum along each retained named cycle. Projecting the full path gives the last assertion. QED.

**Cycle-search algorithm:** build arcs from the signs of `y-x`, find one directed cycle using depth-first search (one arc per nonzero named edge suffices to locate a cycle), perform its unit move, and repeat. Per step the constructed directed graph has at most `|E|` arcs and `|U|+|V|` vertices; a DFS costs `O(|U|+|V|+|E|)`, plus state updates. This is a constructive termination bound, not a claim about optimal shortest cycle paths.

## 3. Exact counterexamples — observer holes and projection jumps

Consider a complete 2x2 unit-capacity named graph with both row margins and both column margins equal to 1. In row-major edge order, its only feasible tables are
`a=(1,0,0,1)` and `b=(0,1,1,0)`.
Project to the first-row edges `T={(0,0),(0,1)}`: feasible projections are `(1,0)` and `(0,1)`. No change in just **one** selected coordinate can connect them while preserving feasibility. Their connecting cycle simultaneously flips two selected coordinates.

For the integer linear observer `D(x)=x_(0,0)+x_(1,1)`, the feasible values are `{0,2}`, with a hole at 1. Therefore *integral saturation of the selected-edge coordinate projection* does not entail interval saturation of arbitrary integer **linear observer images**. A source-edge vector and its observer aggregation have distinct lattices and distinct admissible movements.

## 4. Independent finite exact regression

The attached executable `PREFIX809_R6_CYCLE_FIBER_CHECK.js` enumerates every integer capacity pattern and every table, then groups them by full row/column margins and checks **every nonidentical ordered pair** within each feasible margin fiber. It reconstructs a directed cycle at each step and asserts capacity, original margins, strict L1 descent, exact endpoint, full signed **two-observer** increments and the simple-graph step bound. It additionally checks the same rules on two distinct parallel named edges, where 2-cycles become possible.

Exact coverage:
- 2x2 all capacities in `{0,1,2}`: 81 patterns; 1,215 margin fibers; 1,296 tables; 164 ordered nonidentical pairs; 166 unit cycle moves.
- 2x3 all capacities in `{0,1}`: 64 patterns; 704 fibers; 729 tables; 54 ordered pairs; 54 moves.
- 3x3 all capacities in `{0,1}`: 512 patterns; 17,840 fibers; 19,683 tables; 4,698 ordered pairs; 4,698 moves.
- Parallel named 2x2 (5 edges, capacities 1): 1 pattern; 22 fibers; 32 tables; 24 ordered pairs; 24 moves including **16 2-cycles**.

Across these declared families: 658 capacity configurations, 19,781 margin fibers, 21,740 complete tables, **4,940** nontrivial ordered-pair checks, **4,942** constructive unit moves, all exact assertions passed. Complete pair enumeration applies to the declared families; no random sampling or floating-point arithmetic is used. The universal conclusion follows from the circulation proof, not the finite regression.

## 5. Future-relevant residual and next research

Exact cycle moves are state transitions in the auxiliary source table, **not yet native heartbeat time events**. A projected observer may show identical readings across a nonzero cycle; its hidden named source/ordering remains available for later operations until an observer-and-future-horizon sufficiency certificate is established. P000, six native spatial axes, independent time dimension, three-dimensional slice semantics and user-protected world model remain intact.

**Next discriminating unit:** For candidate selected-edge sets `T`, compute the set of primitive projected cycle moves and study when a finite, *state-independent* move family connects every feasible projected fiber under capacities, versus when residual capacity/state dependence is essential. Use the exact cut inequalities of PREFIX-808 to pretest neighbor feasibility; compare this with cached-cut evaluation, especially sparse vs dense named source graphs. Distinguish projected single-coordinate moves, joint cycle moves and arbitrary integer-weight observer gaps. For an actual X6 mapping, preserve Cell/Link/Port provenance and independently typed event time before making a native-evolution claim.

**Source basis:** PREFIX-807–808 exact source edge intervals and projection cuts; `p000_reality_foundation.json`, `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json`, `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`, current P000/ACTIVE and portable research protocols. The proof here is self-contained and uses finite integer circulations.

**Scientific status:** `AUTHOR_PROVED / EXACT_FINITE_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED`.
