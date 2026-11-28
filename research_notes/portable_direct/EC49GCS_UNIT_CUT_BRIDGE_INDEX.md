# EC49GCS — Unit-cut bridge index on the shared rooted quotient
2026-11-28. AUTHOR_PROVED / EXACT_FINITE_SYNTHETIC_BRIDGE_REPLAY / NOT_REVIEWED.
Predecessor: 42c169fef6d0186a2df1f4db0f4e59dbf33f2d7a:research_notes/portable_direct/EC49GCR_SHARED_ROOT_ALLOCATION_QUOTIENT.md. Reuse its exact strict-Hall auxiliary model, same generator and sibling sampling, no changed physical input.

## 1. Unit cuts and sink bridges
Let G be any finite directed multigraph with positive integer capacities, sink t, every vertex able to reach t, and nonempty root set E not containing t. Define lambda(E)=min_{E subset X, t notin X} cap(delta^+(X)). In the GCR quotient this is precisely the rooted credit. Every nonempty rooted cut has positive integer capacity. Auxiliary nodes in the GCR construction are connected to their nonempty support, and any port not reaching t would produce a zero cut contrary to strict Hall. Zero-capacity arcs are omitted.

For each unit-capacity arc e, let D_e be the vertices not reaching t in G-e. Nonempty D_e is called a bridge domain here. If nonempty, e's tail lies in D_e and its head outside: choose a simple original path from a disconnected vertex to t; it must use e, and the suffix from its head avoids e, while the tail cannot reach t without e. No other arc leaves D_e, since an endpoint outside can reach t avoiding e. Thus D_e is the unique maximal vertex set with outgoing cut exactly {e}.

If a rooted cut has capacity 1, it has exactly one outgoing unit arc e. Its vertices cannot reach t in G-e, hence it is contained in D_e. Conversely E subset D_e certifies a capacity-1 cut. Therefore lambda(E)=1 iff some bridge domain contains E; otherwise lambda(E)>=2. This is an exact decision, not a heuristic.

## 2. Laminarity and minimal witness
Nonempty domains of distinct unit arcs are strictly laminar: if x belongs to D_e intersect D_f, take a simple x-to-t path. Both arcs occur. Suppose e precedes f. The prefix from x to tail(e) avoids f; any path from tail(e) to t avoiding f would contradict x in D_f. Thus tail(e) in D_f, and every vertex of D_e must pass tail(e) to reach t, so D_e subset D_f. The suffix from tail(f) avoids e, hence tail(f) notin D_e, making containment strict. The other ordering gives reverse containment.

For a root E having unit credit, choose e* with smallest bridge domain containing E (unique by laminarity). Let R be all vertices reachable from E in G-e*. R subset D_e*, excludes t, and no arc other than e* can leave R. Positivity implies its cut capacity is exactly 1. For every rooted optimum X, its sole outgoing arc f gives E subset D_f and X closed under edges of G-f. If f=e*, then R subset X. Otherwise D_e* is a strict subset of D_f; tail(f) cannot be in D_e*, because that would imply D_f subset D_e* by mandatory passage through tail(f). Every path defining R stays within D_e*, thus avoids f. Hence R subset X also in this case. It follows that R is exactly the least rooted optimum. Projecting its ports gives the canonical least port side by the GCR extension argument. This preserves the full unit-credit witness, not only a number.

The theorem handles multiple roots and parallel arcs by individual edge identity. Distinct bridges can be nested; a mere maximal-tight-component ID does not recover the least cut. Unit-capacity arc deletion on the *positive original quotient* is meant, not deletion from an arbitrary already-augmented root flow.

## 3. Exact hybrid and complexity
Build GCR allocation once. On its positive quotient, for each unit arc compute D_e by reverse reachability from t with that arc omitted. Retain nonempty domains sorted by size. Query a root: test containment until the first match, then forward reachability with that bridge removed. If none matches, use ordinary GCR rooted maxflow; lambda>=2 is already certified. With b unit arcs, B nonempty bridge domains, N vertices and L arcs, preprocessing O(b(N+L)+B log B), explicit domain storage O(BN), query O(B|E|+N+L) worst case plus the fallback. These are elementary bounds, not a claim of a linear-time index. Laminar domains suggest a reverse-dominator-tree compression, which is not implemented or benchmarked. Full preprocessing, scans, memory and fallback frequency must decide whether this route improves real workloads; small root multiplicity can favor direct GCR.

## 4. Replay
Same GCR 350-model generator and sampling from fixed source; allocation independently cold-built, original port enumeration gives exact lambda and least optimum, independently checked against rooted cold quotient maxflow. Additional arbitrary roots on first queried state per model; paths and isolated vertices for n=2..10. Code and output in research_artifacts/portable_direct/EC49GCS/. Results:
```json
{
  "stats": {
    "seed": 20261128,
    "models": 350,
    "originalSubsets": 376960,
    "legalSiblingPairs": 2570,
    "rejectedPairs": 230,
    "states": 5092,
    "roots": 18562,
    "unitQueries": 505,
    "nonunitQueries": 18057,
    "arbitraryRootChecks": 13692,
    "arbitraryTightRoots": 284,
    "unitEdges": 9642,
    "activeBridges": 3989,
    "laminarChecks": 1641,
    "bridgePreprocessEdgeScans": 96417,
    "bridgeQueryMembershipTests": 16601,
    "bridgeQueryReachScans": 553,
    "coldRootSearchScans": 551851,
    "hybridFallbackSearchScans": 547683,
    "coldRootAugments": 43047,
    "hybridFallbackAugments": 42542,
    "allocationScans": 197897,
    "allocationAugments": 9765,
    "cutChecks": 18562,
    "allocationChecks": 5110,
    "structuredChecks": 4070
  },
  "structured": [
    {
      "n": 2,
      "kind": "path",
      "bridges": 2
    },
    {
      "n": 3,
      "kind": "path",
      "bridges": 3
    },
    {
      "n": 4,
      "kind": "path",
      "bridges": 4
    },
    {
      "n": 5,
      "kind": "path",
      "bridges": 5
    },
    {
      "n": 6,
      "kind": "path",
      "bridges": 6
    },
    {
      "n": 7,
      "kind": "path",
      "bridges": 7
    },
    {
      "n": 8,
      "kind": "path",
      "bridges": 8
    },
    {
      "n": 9,
      "kind": "path",
      "bridges": 9
    },
    {
      "n": 10,
      "kind": "path",
      "bridges": 10
    },
    {
      "n": 2,
      "kind": "isolated",
      "bridges": 2
    },
    {
      "n": 3,
      "kind": "isolated",
      "bridges": 3
    },
    {
      "n": 4,
      "kind": "isolated",
      "bridges": 4
    },
    {
      "n": 5,
      "kind": "isolated",
      "bridges": 5
    },
    {
      "n": 6,
      "kind": "isolated",
      "bridges": 6
    },
    {
      "n": 7,
      "kind": "isolated",
      "bridges": 7
    },
    {
      "n": 8,
      "kind": "isolated",
      "bridges": 8
    },
    {
      "n": 9,
      "kind": "isolated",
      "bridges": 9
    },
    {
      "n": 10,
      "kind": "isolated",
      "bridges": 10
    }
  ],
  "mismatches": 0,
  "scope": "GCR same deterministic generator and sibling sampling; independent cold allocation; additional arbitrary roots and structured tests. Preprocess counters include structured tests (conservative); exclude graph build, sorting, and initial full reach scan. No wall time or bytes claimed."
}

```
Preprocessing edge scan totals include the structured tests; membership and forward scans count normal roots only. Cold/fallback counts are adjacency visits in residual BFS, not identical to positive-graph visits. Graph construction, sort, baseline reach scan, allocation validation, and memory overhead are not fully measured. No end-to-end speedup claim; no independent review or native physical attribution. The GCR allocation cost is common to both comparison routes. Frozen BRC16943 bytes not restored or replaced; historical 25<=M14<=27 and next structure 2046 are not recomputed.

## 5. Next and control scope
Next: derive a compact bridge-domain index using reverse dominators and pair it with GCP reuse, then evaluate amortization on actual Pareto state order and higher-credit queries. For lambda>=2, no unit index result substitutes for exact maxflow. Keep labels, supports, capacities and allocation as required for future legal sibling updates; the index is only a scoped unit-credit observer, not an entire-state quotient.
Current global entry snapshot dc1b1f8f6aaa5358387f674c98e9223ae396b382; project control main a98447c988c1e5b4196ffc2cd6547fee3ca62eee; native topic receipt r4-20261128-2132-ec49as-topic-read SUCCEEDED with NO_CANONICAL_PUBLICATION_DIRECTORY at that Source, native owner projection not evaluated. No current private lane identity established, no shared claim, formal result, activity association, or canonical integration. Independent portable research, historical predecessor provenance retained.