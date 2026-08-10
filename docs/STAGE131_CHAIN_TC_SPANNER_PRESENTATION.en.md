# Stage131 — Source-Dependent Chain Shortcuts as TC-Spanner Presentations

Status: `RESEARCH BRIDGE / NONCANONICAL`

The translation-invariant jump-length model is only one restricted presentation class. A general chain rule presentation may choose different transitive shortcuts at different source positions.

This enlarges the storage/inference-depth frontier and aligns the underlying graph problem with standard transitive-closure spanners.

## 1. Unrestricted exact chain presentation

For chain vertices

`0<1<...<n`,

the semantic closure contains every directed pair

`i->j`, `i<j`.

An exact stored presentation chooses a subset E of those transitive edges whose reachability relation remains the same total order.

Every adjacent edge

`i->i+1`

is forced: there is no intermediate vertex through which that comparable pair could otherwise be reached.

All other edges are optional execution shortcuts.

## 2. Storage and reusable inference depth

Storage is simply

`|E|`.

For any comparable pair i<j, let `dist_E(i,j)` be shortest directed-path length in the stored graph.

The reusable worst-case inference depth is

`diam(E)=max_(i<j) dist_E(i,j)`.

This is stronger than asking only how fast x_0 reaches x_n: it guarantees bounded-round closure from **any** chain premise.

For a translation-invariant jump set, the diameter reduces to the parent coin-count depth because only the distance `j-i` matters.

## 3. Exact TC-spanner identification

A stored chain presentation with

`diam(E)<=k`

is exactly a k-transitive-closure spanner of the directed path/total-order closure in standard graph terminology.

Thus the unrestricted Stage131 shortcut problem is not a new generic graph optimization problem. It is a project-specific precision/presentation interpretation of standard TC-spanner structure.

## 4. Translation-invariant jump sets are a strict subclass

The parent generation stores a jump type ell at **every** valid source position.

An unrestricted presentation may keep the same long shortcut at only the positions where it is useful.

Because long jumps are often valuable only in one region of the chain, source-dependent storage can strictly improve the frontier.

## 5. One-shortcut exact diameter

Start from the n adjacent edges and add one shortcut

`a->b`, `b-a>=2`.

The resulting diameter is exactly

`D(a,b)=max{ b-1, n-a-1, n-(b-a)+1 }`.

The three terms have direct meanings:

1. `b-1`: a source/target pair ending just before b cannot use the shortcut;
2. `n-a-1`: a pair starting just after a cannot use it;
3. `n-(b-a)+1`: the longest pair spanning the shortcut, such as0->n, saves exactly `(b-a)-1` hops.

No other pair is worse.

## 6. Optimal one-shortcut theorem

Let d be the desired diameter.

For `D(a,b)<=d`, the closed formula forces

`b<=d+1`,

`a>=n-d-1`,

and shortcut length

`b-a>=n-d+1`.

The first two conditions imply

`b-a <= 2d-n+2`.

Therefore feasibility requires

`2d-n+2 >= n-d+1`,

or

`3d >= 2n-1`.

Hence every one-shortcut presentation satisfies

`d >= ceil((2n-1)/3)`.

This bound is attainable. Put

`d*=ceil((2n-1)/3)=floor((2n+1)/3)`,

`a=n-d*-1`,

`b=2n-2d*`.

Then all three diameter terms are at most d*.

Thus the exact optimum with n+1 stored rules is

`D_one(n)=floor((2n+1)/3)`.

The executable layer checks the formula against brute-force shortcut placement over many n.

## 7. Smallest strict improvement over translation-invariant jumps

Take n=5.

### Unrestricted one-shortcut presentation

Store the five adjacent rules plus

`1->4`.

Storage6, diameter3.

### Translation-invariant presentation at storage6

The parent exact frontier has `(6,4)` rather than `(6,3)`.

So source dependence strictly improves the resource frontier at the same stored-rule count.

## 8. Exact small-n unrestricted frontiers

The branch enumerates every optional shortcut for n<=6.

Storage/diameter pairs:

### n=3

`(3,3), (4,2), (6,1)`.

### n=4

`(4,4), (5,3), (6,2), (10,1)`.

### n=5

`(5,5), (6,3), (8,2), (15,1)`.

### n=6

`(6,6), (7,4), (8,3), (10,2), (21,1)`.

Comparison with the translation-invariant parent shows strict savings from n=5 onward.

## 9. n=1024 one-shortcut scale

The adjacent basis has

1024 rules / diameter1024.

With only **one** extra source-specific shortcut, total storage is1025 rules and the exact optimal diameter becomes

`floor((2*1024+1)/3)=683`.

An explicit optimal shortcut is obtained from the constructive formula.

By contrast, the only translation-invariant jump-type presentation with exactly one extra positional rule is `{1,1024}`: it helps only the endpoint and still has depth1023.

Thus source-local placement itself is a precision resource.

## 10. Relation to the richer jump families

One source-specific shortcut gives only a constant-factor diameter improvement.

The parent two-length/geometric/binary families replicate useful scales across many sources and achieve much lower depths at higher storage.

The unrestricted TC-spanner class can mix both ideas:

- choose multiple scales;
- place them nonuniformly;
- share shortcuts only where needed.

This is the correct larger search space for Stage131 presentation optimization.

## 11. Semantic interpretation

All shortcuts are semantically derivable from the adjacent chain. Their only role is presentation/execution efficiency.

Hence the chain now exhibits three nested concepts:

1. **semantic basis** — adjacent edges;
2. **restricted execution presentation** — global jump-length families;
3. **unrestricted execution presentation** — source-dependent TC-spanner shortcuts.

Moving outward changes storage/depth possibilities without changing closure law.

## 12. Rooted circuits versus TC-spanner presentations

The full rooted-circuit/transitive table is the diameter1 endpoint of this same graph family.

The adjacent basis is the minimum-edge endpoint.

TC-spanner presentations occupy sparse bounded-diameter points between them.

So rooted-circuit “transitive redundancy” is best understood as one extreme of a broader exact presentation design space rather than as a simple error to delete.

## 13. Prior-art boundary

Transitive-closure spanners are established graph theory. The standard definition asks for a subgraph of the transitive closure with the same reachability and bounded directed distance between every reachable pair.

Stage131 does **not** claim novelty for that generic object or its algorithms.

The project-specific contribution is the mapping:

`TC-spanner edge budget / diameter`

becomes

`stored derived implication budget / inference-round depth`

inside the rooted-circuit precision architecture.

## 14. Next frontier

The source-dependent formulation opens stronger questions:

- exact minimum edges for diameter k on chains and wider posets;
- weighted/nonuniform query costs;
- premise-dependent rule storage cost;
- DAG/circuit sharing instead of flat edge storage;
- multi-premise Horn closures and hypergraph shortcut structures;
- dynamic compilation of shortcuts from observed query workload.

These should consume TC-spanner/shortcut prior art rather than rederive it blindly.

## Owner-local assets

- `src/enterprise_math/stage131_chain_tc_spanner.py`;
- `tests/test_stage131_chain_tc_spanner.py`;
- `docs/STAGE131_CHAIN_TC_SPANNER_PRESENTATION.{en,zh}.md`.

## Prior art / status

TC-spanners, graph shortcuts, directed diameter and transitive closure are standard prior mathematics/CS. The Enterprise Math value is the explicit Stage131 presentation-precision interpretation and the exact one-shortcut specialization.

No repository strict CI, `EXECUTABLE_CHECKED`, or canonical claim. Hard block: `NONE`.