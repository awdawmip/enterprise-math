# EC49FNR — Exact geodesic obstructions in a native-BRC triple-stable cache-exchange graph

Date: 2026-11-13. Researcher source: own registered `EM-DIRECT-862128` / `RA-2CB3A13B7FF34C81C69A623C`. Status: **author-side exact finite postprocessing, NOT_REVIEWED**. No claimed formal Task, CLAIM, Result, independent review or Foundation promotion.

## Scientific input and exact proposition

This continues [EC49FNQ PR #2306](https://github.com/awdawmip/enterprise-math/pull/2306) at immutable commit `f51011eaada023e9732431809ea7e2b9691e79f2`. The original native-BRC scientific pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab` is unchanged.

Input: the exact 1000 rows for configurations 32000–32999, each a seven-whole-cache-key set `K_i` and the triple `v_i=(C_i,m_i,g_i)`: ordered signed native microstep-prefix optimum, number of optimum admissible root-demand assignments, and positive gap to next distinct root-allocation cost. Input vector at the [immutable EC49FNQ path](https://github.com/awdawmip/enterprise-math/blob/f51011eaada023e9732431809ea7e2b9691e79f2/research_notes/r4_ec49as_exact_right_neighborhood_20261030/EC49FNQ_STABLE_TRIPLE_PLATEAUS_20261113/EDGE_VECTOR_EC49FNP.u8x11.xz.b64); decode Base64 and XZ to 11,000 bytes, SHA256 `4d6540181b8c25a324aa701f551602ed53156be46b70170f1c104230c6443e9b`. The vector is inherited **verbatim**; no new native optimization was performed.

Define `d_J(i,j)=|K_i\\K_j|`, the minimum one-key swap count in the full Johnson graph on seven-key sets; in this family `d_J≤3`. Let `G` be the induced graph on precisely the 1000 indexed vertices, joining two vertices when they differ by one whole cache key **and** their complete triples `v` agree. For vertices in the same connected component let `d_G` be the shortest triple-stable path length.

**Finite theorem, conditioned on the exact pinned rows.** Of the 16,558 unordered distinct pairs in the same stable component, **16,550 (99.951685%) are isometric:** `d_G=d_J`. Exactly **eight** have a genuine shortest-path detour, and every such pair has `d_G=d_J+1`. The joint distance distribution is:

| Full Johnson distance d_J | Stable distance d_G | Pair count |
|---:|---:|---:|
| 1 | 1 | 11574 |
| 2 | 2 | 4814 |
| 2 | 3 | 4 |
| 3 | 3 | 162 |
| 3 | 4 | 4 |

There are precisely four (2,3) obstructions, and in **each** all four possible two-step Johnson-geodesic intermediate key sets fail the triple-stability restriction: exactly one is absent from this chosen 1000-vertex set, and the other three exist but carry a different `(C,m,g)`. The four pairs are `32275–32703`, `32276–32719`, `32315–32353`, `32318–32353`. The four (3,4) pairs are `32703–32951`, `32703–32953`, `32719–32961`, `32719–32963`.

The calculation sharpens EC49FNQ's diameter-four result: a connected same-signature pair almost always admits a shortest possible whole-key-swap path in the 1000-vertex graph; all failures are these eight explicit pairs, and their additional cost is exactly one exchange. This quantifies graph-level path detours, **not** the original native-prefix objective cost `C` or its perturbation.

## Proof and verification

**Johnson lower bound.** Each edge removes exactly one key of `K_i\\K_j`, so at least `|K_i\\K_j|` edges are necessary to reach `K_j`. Since all key sets have equal size, such a number of swaps suffices in the full Johnson graph.

**Finite graph proof.** Exhaustively enumerate all 499,500 unordered vertex pairs, identifying one-key swaps. An independent six-key-subset inverted index gives the identical 27,942 exchange edges; filter by exact triple equality to obtain 11,574 stable edges. Compute the successive exact first-hit reachability layers at distance one, two, three, four; they are disjoint and cover every stable connected pair (verified independently using BFS connected components). Tally each pair's `(d_J,d_G)`. The joint histogram above proves the result; independent BFS and layer-expansion implementations agree. The original EC49FNQ graph audit also verified 244 components and stable diameter four.

**Four-intermediate lemma.** If `d_J=2` for seven-element sets `K,L`, then every two-swap shortest path passes through precisely one of the four sets `(K\\{a})∪{b}`, where `a∈K\\L` and `b∈L\\K`. Therefore a triple-stable two-swap path exists exactly when at least one of these four sets belongs to the selected vertex set and has the endpoint triple. For each of the four explicit 2→3 exceptions, the verifier checks these four possibilities and proves the one-absent/three-wrong pattern.

The full enumeration is exact integer/set arithmetic. The `C,m,g` values remain conditional on the original pinned native-BRC optimizer evidence; this work independently computes the graph invariant but does not independently optimize all 1000 native tries.

## Reproduction and next scientific problem

Run `python3 VERIFY_EC49FNR.py <path-to-immutable-EC49FNQ-vector.b64>`. It validates the 11,000-byte raw SHA256, checks all 27,942 edges twice, performs an exact layer-based path audit, verifies the eight pairs and the four geodesic barriers, and independently reconstructs the connected-pair total. `RESULT_EC49FNR.json` records the claimed output.

Next: use the eight obstructions as **discriminating boundary cases** for a root-cost-function perturbation certificate that could predict triple-stability before exhaustively reevaluating all root allocations. In particular distinguish missing intermediate configurations from present configurations with changed root allocations, and measure the predicted effect of single native cache-key replacements. This is a scoped research question rather than a general theorem claim.

Source/authority boundary: the exact Task label `RS-EC49AS` was read-only checked as `NO_CANONICAL_PUBLICATION_DIRECTORY` at Source `616f084ec3398ccb656e3e89d41e13b45cf737a2`; no CLAIM or formal Result was made. GitHub preservation and Activity bookkeeping are separate from mathematical review. No credentials included.
