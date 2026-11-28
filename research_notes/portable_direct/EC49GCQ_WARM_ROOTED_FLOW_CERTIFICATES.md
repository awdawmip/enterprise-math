# EC49GCQ — Warm rooted-flow residual certificates
2026-11-28. AUTHOR_PROVED / EXACT_FINITE_SYNTHETIC_SIBLING_FLOW_REPLAY / NOT_REVIEWED.
Predecessor: 1a4f0518d5851c66ae1468b3b7e1edd77ea3ec4b:research_notes/portable_direct/EC49GCP_SIBLING_ROOT_CUT_REUSE.md. Same deterministic auxiliary strict-Hall generator and sibling sampling as GCP (seed 20261128); no native physical calculation or altered science pin.

## Proposition and proof
Let c be positive integer port capacities, E_j nonempty supports, and v,w legal integer count prefixes, on the same finite port/class universe. Root E is nonempty. As GCO, construct the closure network source -> class (capacity v_j), class -> supported port (M), port -> sink (c_p), and source -> root port (M). Fix M=1+sum c independently of v,w, and retain even zero-capacity class arcs. Every minimum cut has capacity <=sum c, so cannot cross an M arc. For a rooted port cut U the minimal cut capacity is sum v + h_v(U), since each inside class can be placed on source side and each outside class must be on sink side. Thus the optimal flow value F_v equals sum v + lambda_v(E); residual source reachability projects to the least rooted minimizer (including ties).

Take any exact old maximum flow f_v. Change the class source capacities to w_j. For each class j trim ell_j=max(0,f_v(s,j)-w_j) units along its source-class-port-sink paths, choosing arbitrary outgoing positive-flow amounts summing to ell_j; conservation at class guarantees existence, and nonnegative flow at each port-sink edge is preserved since the removed amounts were part of its inflow. Root direct flows remain unchanged. No other edge changes capacity. Define L=sum ell_j. This constructs a feasible flow f0 of value F_v-L, not a claimed optimal flow.

Let U be the old least root cut, d_j=w_j-v_j, and Delta_out=sum_{E_j not subset U} d_j (signed). The old cut (including all inside class nodes) is a valid new cut with capacity F_v+Delta_out. Consequently
  F_v-L <= F_w <= F_v+Delta_out,
  0 <= F_w-value(f0) <= G := L+Delta_out.
In slack coordinates max(1,F_v-L-sum w) <= lambda_w(E) <= h_w(U). This is a dual lower certificate conditioned on actual stored feasible old flow, stronger than a worst-case unweighted change estimate when realized trim loss is small. Intersect with GCP's sensitivity bound if desired; neither bound is asserted universally stronger than the other.

If G=0, f0 is already maximum. No augmentations are necessary. One residual reachability scan still recovers the canonical least rooted cut; retaining U without that scan would lose structural information. If G>0, continue exact residual augmentations from f0. Integral capacities/flows imply every successful augmentation raises value by >=1, so at most G successful augmentations are needed. This is a value-sensitive bound, not a bit-polynomial running time claim. Edmonds-Karp shortest residual paths also give its usual polynomial bound independent of numeric magnitude, including from an arbitrary feasible starting flow. After no augmenting path remains, the reachable residual vertices give a minimum cut by capacity saturation and flow conservation, and belong to every minimum source side (no residual edge can leave a minimum source side); the projected port set is the least optimum. Independent of augmentation order and trimming choice, both value and canonical rooted witness are recovered. Matrix implementation scans V columns per visited vertex, retains O(V^2) capacities and flows; sparse implementation can store O(edges), trim in O(incidences), and do a final O(edges) reachability. Cache allocation/copy and old-flow construction costs must be included in end-to-end comparison.

## Executed replay
Same GCP 350 synthetic models, exact integer arithmetic (all tested values safe integers), complete raw label-subset independence for prefix selection, exact full port-cut enumeration for old and new roots. Both cold and warm runs use the same deterministic matrix BFS ordering and fixed network; validate capacities, conservation, max-flow/min-cut equality, least port cut, gap and successful augmentation bound. Old flows are computed independently per query, not claimed as free; fallback counts below condition on an already retained certificate. No timing or physical memory measurement. GCP direct-reuse and repair conditions independently reproduced. Full-network warm and full-network cold comparator on all remaining GCP branches (including one tight repair); not a comparison against a strictly smaller local network. 
```json
{
  "models": 350,
  "seed": 20261128,
  "originalSubsets": 376960,
  "legalSiblingPairs": 2570,
  "rejectedPairs": 230,
  "queries": 18562,
  "gcpReuse": 9677,
  "gcpLocal": 1,
  "gcpFull": 8884,
  "coldAugmentsAll": 63810,
  "warmAugmentsAll": 12206,
  "coldBfsScansAll": 5946966,
  "warmBfsScansAll": 1990619,
  "oldAugmentsAll": 63810,
  "oldBfsScansAll": 5946966,
  "coldAugmentsFallback": 35688,
  "warmAugmentsFallback": 11870,
  "coldScansFallback": 3621377,
  "warmScansFallback": 1482578,
  "fallbackZeroAugments": 136,
  "fallbackCutEquality": 45,
  "allZeroAugments": 9555,
  "allCutEquality": 9464,
  "trimmedUnits": 12469,
  "maxGapBound": 5,
  "boundChecks": 18562,
  "flowCertificates": 74248,
  "changedCutAtEquality": 33,
  "warmWorseAugmentsFallback": 0
}
```
Structured family: extend the GCP two-port example c=(2,1), supports {a},{a,b}, v=(0,2), w=(1,1), root {a}, by n-2 unused ports of capacity 5. Old least cut {a,b}, new least {a}, both slack 1. All added ports have positive slack increment and never enter a least cut. For n>=3 this supplies a proper tight container. Verified n=2..10 by full port-cut and flow replay. The family shows that even a new maximum flow obtained by exact trimming alone does not justify keeping the old least cut.

## Scope, next and provenance
No full Pareto integration, cache cost/eviction, production speedup, or physical BRC16943 replay; frozen archive bytes not recovered or substituted. Inherited physical frontier next structure 2046 and 25<=M14<=27, not recomputed. Next: sparse flow storage with shared topology, compare hybrid GCP+warm against local/full cold under measured wall time and peak memory, then integrate into actual Pareto solver. In particular measure whether old flow materialization costs outweigh savings on low-reuse branches.
Current global main entry blobs matched immutable 60427a91398470fa85116bc5c5898c4bd79ccdc1, P000 V4 projection original blob matched, Source V5 foundation projection and ACTIVE worldview/role/portable/residual/method read. Native status identity_only succeeded (not research authorization). Topic receipt r4-20261128-1928-ec49as-topic-read SUCCEEDED, Source 46aa221e08785c5812b81d9fff9c5f01f3007ada, NO_CANONICAL_PUBLICATION_DIRECTORY, native owner projection not evaluated. Private research identity unconfirmed; historical provenance EM-DIRECT-23537B only. Independent portable continuation, no CLAIM or shared task mutation. Activity association and canonical integration pending.
Reproduce: node research_artifacts/portable_direct/EC49GCQ/warm_flow_replay.js. Output stored alongside.
