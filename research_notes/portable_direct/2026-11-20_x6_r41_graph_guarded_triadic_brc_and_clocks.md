# X6 R41 — 资源冲突图上的原子三元搬运：配置、序列历史、未来 Markov 商及并发时钟

Date: 2026-11-20 (Asia/Shanghai). Research context: `RS-X6-NATIVE-TIME-DYNAMICS`.
Scientific status: `CONDITIONAL_AUTHOR_PROOF / EXACT_FINITE_BRC_ENUMERATION_PASS / NOT_REVIEWED`.
Source: frozen P000 V5 `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`; `definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md`; `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`; `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`. Continue the 2026-11-18 conditional guarded relocation theorem and R37–R40 future-observation/multiplicity line. Earlier source: `research_artifacts/mcp/RS-X6-NATIVE-TIME-DYNAMICS/MCP-456b8f22a648400585024ffbcc1c2c94/5a04daccb6795e494dbc/X6_TIME_GUARDED_TRIADIC_RESOURCE_CONFLICT_20261118.md` at Source `f41c2690daba467ecbde99615a1337e67be46ffd`.

## Declared candidate event system

Let V be m individually identified source Cells in the signed X6 Cell torsor. Each source initially carries an indivisible ordered, positively signed, equal-quantum 3-force frame `F=(i0,i1,i2)` satisfying the *declared* native `TRIADIC_CLOSURE_E` predicate. Source v has three labeled candidate Port/Link transfers `(v,0),(v,1),(v,2)` to the distinct native-axis neighbors `c_v+E_{i_r}`. Every transfer is atomic: the complete triad leaves its source and arrives intact at its chosen target, while a typed log preserves Cell, signed Port, source, token IDs, route and order.

Introduce a simple, fixed **resource-conflict graph** G=(V,E). An event at v is enabled precisely when v has not fired and no previously fired neighbor of v is incident to G. Firing v consumes it, permanently rules out each neighbor as a later source event, and does not change any other guard. Each of its three ports is eligible whenever v is eligible. Edges are shared-resource exclusions, not causal arrows. Disjoint source/target/resource footprints give the edgeless graph and commute. These are explicit candidate dynamical assumptions; P000 admits the frame's atomic triadic type, not a unique inter-Cell transfer law.

A finite history is a **serial word** of distinct `(v,r)` events subject to the graph guard. Its **configuration** forgets serial order but retains the chosen subset and per-source Port. A **parallel round schedule** is an ordered partition of those selected events into nonempty batches, with no within-batch ordering (allowed here because a selected set is independent).

## R41.A — Conflict independence polynomial and exact BRC fibers

Write `i_k(G)` for the number of k-vertex independent sets. All terminal configurations with k fired sources are counted by

```
C_G,k = i_k(G) 3^k,
K_G(x) = sum_{k=0}^m i_k(G) 3^k x^k = I_G(3x).
```

Every such configuration has exactly k! serializations, hence the exact typed BRC serial-history count is

```
H_G,k = k! i_k(G) 3^k,
sum_k H_G,k x^k/k! = I_G(3x).
```

Proof: an executable source set must be independent because an earlier neighbor disables a later one; conversely every order of an independent set obeys every static guard. Choices of the three Ports are independent, and serialization is precisely permutation of the k distinct chosen source events. The source, Port and order are retained in the BRC carrier. These counts are integers and do not represent signed amplitudes, physical probabilities or elapsed real time.

For edgeless G, `K_G(x)=(1+3x)^m` and `H_G,k=(m)_k 3^k`. For a single shared mutual-exclusion edge on two sources, `K_G(x)=1+6x`, whereas the edgeless two-source model gives `1+6x+9x^2`. For the three-vertex path graph, `K_G(x)=1+9x+9x^2`. Thus a precedence-only event poset cannot replace a conflict graph.

## R41.B — Exact minimal future-support state

For a serial configuration I (the fired independent source set), write `N[I]=I union all neighbors of I` and `E(I)=V\N[I]`: the eligible-source set. The complete future **named successful-event language** (labels `(v,r)`, but no prior/current occupancy readout) depends exactly on E(I):

```
L_future(I) = L_future(J)   iff   E(I)=E(J).
```

Proof: if the two E sets differ, a one-symbol `(v,r)` word is enabled on exactly one side. If they agree, the same labels are enabled, and each successor updates E by `E -> E \ ({v} union N(v))`; induction on future word length gives equality. This quotient is a deterministic, update-closed minimal Markov presentation for the specified future language, with exactly `#{E(I): I independent in G}` classes.

For edgeless G, E(I)=V\I: exactly 2^m future classes. The complete *current* occupied-target/Port configuration readout distinguishes `sum_k i_k(G)3^k=I_G(3)` states (edgeless: 4^m); the previously chosen Ports cannot be deleted from that stronger current observer. Coarse future **positive path-count** readout with source and Port names erased gives, from E,

```
C_E(a^j) = j! 3^j i_j(G[E]),  (0 <= j <= |E|).
```

For edgeless G, this is `(m-|I|)_j 3^j` and its all-future count classes are exactly m+1, distinguished already by their one-step counts `3(m-|I|)`. Equality of one scalar current count alone is not asserted to be a safe Markov quotient for a general conflict graph.

## R41.C — Serialized event count vs parallel-round clock

For any *fixed* k-event configuration, the number of r-round schedules is

```
A(k,r) = r! S(k,r)
       = sum_{j=0}^r (-1)^(r-j) binom(r,j) j^k,   1 <= r <= k.
```

Here `S(k,r)` is the integer number of partitions of k labeled events into r nonempty unlabeled blocks; ordering the blocks gives the rounds. Thus the number of all r-round schedules terminating in a k-event configuration of G is `i_k(G)3^k r! S(k,r)`. The empty history has a unique 0-round schedule.

For k=2, the same occupied-target state admits one batch `{e1,e2}` (round count 1) or two sequential batches `{e1},{e2}` (round count 2). Both flatten to micro event count 2; all microscopic orders are valid. Therefore neither the final Cell/Port configuration nor the micro-event count alone determines the parallel-round clock for k>=2. A schedule coordinate (ordered batch partition, or declared schedule readout) is necessary if round duration/number is an output. This is an explicit two-clock nonfactorization witness, not a claim about a physical heartbeat period.

## Exact finite verification

The companion `x6_r41_graph_guarded_brc_verify.js` is a self-contained typed positive-integer branch enumerator. It exhausts all simple conflict graphs on 0..4 named sources (76 graphs), all legal serial histories and source/Port configurations for each graph, validates every coefficient and the k! fiber, and checks the enabled-set successor congruence. For edgeless graphs m=0..5 it independently counts the expected configurations, serial histories, 4^m current states, 2^m named future classes, and m+1 coarse future-count classes. It enumerates surjective assignments of k labeled events to r ordered nonempty rounds for every k<=5 to check the Stirling/round coefficient.

At m=5 edgeless, the configuration counts by k are `[1,15,90,270,405,243]` (total 1024), serialized-history counts are `[1,15,180,1620,9720,29160]` (total 40696), named-future classes 32, and coarse future-count classes 6. All ordered-round schedules over every terminal configuration total 165634. Computation uses exact, bounded small integers (no floating approximations); the universal formulas follow from the proofs, not extrapolation.

Reproduce: `node x6_r41_graph_guarded_brc_verify.js > x6_r41_graph_guarded_brc_results.json`.

## Scope, handoff and next discriminating unit

This line applies to a **static permanent conflict-guard candidate**, with positive equal-unit 3-Port atomic triadic moves. Admissibility of actual `TRIADIC_CLOSURE_E` inter-Cell transfers, rotation/frame change, real link occupation, physical duration and environmental response remains to be obtained from a native update law. The observer type must be selected before quotienting: historical order, current moved-target identity, future named support, path multiplicity and round schedules are distinct.

Next useful test: a shared target whose guard/response depends on the chosen Port or the previous action; determine the smallest exact memory repair and whether the static conflict-graph polynomial fails. Then seek a genuine native Cell/Link/Port successor with a legal full-three-force transition and apply R36/R37/R39/R40 observation certificates under that native map.

No TASK CLAIM, native PROGRESS, Result, independent Review or Foundation promotion is asserted by this portable mathematical return.
