# R5 — Exact bounded-radius K-median DP and verified compact sidecar

Date: 2026-11-13. Status: author-side finite proof and local CPython validation, independent unshared scientific material; formal R5 owner/CLAIM and independent review not established.

## Scientific inputs and provenance

Original *frozen* scientific pin: \`435e77af0d180eac32bd1f9c4c464bc4010b7551\`. Frozen auxiliary corpus: 28 rational coordinates; 15 labeled operations; 2,520-byte balanced-parentheses certificate seed; 2,880 trie prefix nodes; 1,065 distinct terminal certificates; 953 distinct rational activation walls; 954 wall boundaries. The sidecar is an *optional derived query cache*, not a change to the original scientific input or the 2,520-byte persistent seed.

Prior exact results: [fixed-radius mean optimum](../brc_r5_mean_opt_checkpoints_20261113/RESEARCH.md) and [direct-address checkpoint directory](../brc_r5_direct_address_checkpoint_20261113/RESEARCH.md). Previous DP implementation enumerates segment endpoints in a backward loop with early stopping. This work formalizes an explicit radius-local edge graph, precomputes its edges once, and benchmarks it against loading a validated sidecar.

## Theorem 1 — Radius-local exact DP

Let \`x_b=E(b)\`, for \`b=0,...,W\`, denote the cumulative number of certificates activated up to the \`b\`-th complete-wall boundary. Assume **strictly increasing integer** \`x_b\`. Let \`K\` be an integer center budget and \`R\` a nonnegative integer radius. Centers must be chosen from the same boundary positions. Among configurations with at most \`K\` centers satisfying \`max_b min_s |x_b-x_s|<=R\`, minimize \`J=sum_b min_s |x_b-x_s|\`.

For any contiguous segment \`[i,j]\` assigned one center \`s\`, the radius condition is
\`x_j-R<=x_s<=x_i+R\`. Feasible centers therefore belong to a *discrete interval* of admissible boundary indices. The optimal segment center is the median index \`floor((i+j)/2)\` clamped to that interval. With prefix sums of \`x\`, the segment objective is computed in constant arithmetic time once its admissible center has been located.

**Locality:** If a segment is feasible, \`x_j-x_i<=2R\`. Because each \`x_{b+1}-x_b>=1\`, it has at most \`2R+1\` points. Thus for each right endpoint \`j\`, only its previous \`2R+1\` starting positions can be considered. The exact recurrence is

\`F_k(j) = min_{i<j, [i,j-1] feasible} (F_{k-1}(i)+C_R(i,j-1))\`

with \`F_0(0)=0\`, other impossible states \`+infinity\`, and \`C_R\` the exact admissible one-center median cost.

The DP yields the global constrained optimum. Indeed, nearest-center partitions of any feasible solution are contiguous on the ordered line; their segment costs lower-bound the actual objective, and the DP considers the corresponding partition. Conversely, centers from every DP partition form a feasible solution, and nearest-center reassignment cannot increase distance or radius. With \`K\` nonempty segments, the same optimum is obtained for **at most K** when \`K<=W+1\`: an existing segment can be split and assigned an additional sample center without increasing either objective.

Precomputing the radius-local edge graph takes \`O((W+1)(2R+1))\` candidate pairs, and each \`K\`-layer DP takes \`O(K(W+1)(2R+1))\` transitions. Preprocessing binary searches for segment feasibility are \`O((W+1)(2R+1)log(W+1))\` with the implementation supplied; a two-pointer version can remove the logarithm. The radius-locality bound is useful for small optimal radii, here \`R=2\`; it is not claimed as a new asymptotic improvement for unbounded R.

## Theorem 2 — Direct-address sidecar and independent linear validator

Let \`s_0<...<s_{K-1}\` be saved checkpoint boundary indices and \`y_j=x_{s_j}\`. Define \`d(b)\` as the nearest \`y_j\`, ties to the smaller center index. The monotone Voronoi lemma gives
\`d(b)= #{j: b>h_j}\`,
\`h_j=max{b: x_b<=floor((y_j+y_{j+1})/2)}\`.
A single sweep in increasing b,j therefore builds the \`W+1\` direct-address entries in \`O(W+K)\`.

For \`K<=256\` and \`W<=65535\`, encode \`K\` in 2 little-endian bytes, \`K\` sorted boundary indices in \`2K\` bytes, and \`d(0),...,d(W)\` in \`W+1\` bytes. The header is deliberately included; frozen R5 \`K=213,W=953\` gives **2+426+954=1,382 bytes**. The optional cache may be constructed after the original seed decode; no original seed byte is replaced.

A loader can check the length, increasing and in-range center indices, nearest-directory equality, and exact maximum/total event distance without rerunning K-median DP. This verifies **representation integrity and the realized R/J bounds** in \`O(W+K)\` once original \`E\` is independently reconstructed. It is not by itself a proof that the centers are globally optimal; that follows from Theorem 1, previous exact DP and their matched deterministic reconstruction.

For a certificate trie prefix v with terminal interval \`[L_v,H_v)\`, saved checkpoint bitmap \`B_j\`, and sorted activation event permutation \`pi(t)\`, the exact count at b is
\`C_v(b)=popcount(B_{d(b)} & [L_v,H_v)) + sign(x_b-y_{d(b)}) sum_{min(x_b,y)<=t<max(x_b,y)} 1_{L_v<=pi(t)<H_v}\`.
This is signed membership correction of the activation set, preserving tied rational wall multiplicities and any query order. The correction loop has at most R events when its directory has radius R.

## Executed evidence

A local, independently written standard-library Python script rebuilt all frozen source rational inputs and the BP seed; then recomputed the \`K=213,R=2\` optimum using the radius-local DP. The computed \`J=1070\` and the direct-address directory SHA-256 were identical to earlier R5 results. The finite graph contains **4,214 admissible segment edges**; it is reused for each DP layer.

Nine within-process repetitions gave median **43.418 ms** to reconstruct optimal centers, versus **0.316 ms** to validate the in-memory sidecar against the same independently built E (about **137.5×** for these two *substeps only*). A full 954 × 2,880 = **2,747,520** boundary-prefix exact count comparison passed, checking signed bitmap corrections against direct integer-rank counts. A changed directory byte was rejected by the validator. Rebuilding the complete rational corpus in this execution took **1,961.613 ms**; independent fresh-process peak RSS, seed-only decode and end-to-end query/output reconstruction remain to be measured.

The exact 1,382-byte cache has SHA-256:
\`94341ccf1aa09eb0eb42c045201b36dc9589008209fe77f446d8a4b93cee68b6\`.
The embedded 954-byte directory independently matches predecessor SHA-256:
\`a947d07d7d494e00e14013eb929b3ffdc9224938ec15289209e68316c50a14b1\`.

Files: \`VERIFY_R5_BOUNDED_DP_FROM_PINNED.py\` is the repository-portable stacked-fixture verifier; \`EXACT_OUTPUT.json\` records observed execution from \`VERIFY_R5_BOUNDED_DP.py\` in the local run; \`SIDECAR_BASE64.txt\` contains exact separately serialized cache bytes. The committed repository-portable script awaits execution on its own exact GitHub bytes; do not attribute local run timings to its unexecuted source.

## Remaining next unit

1. Benchmark direct seed-only decode and trusted sidecar checks in separate fresh processes, including peak RSS and complete rational-query latency, not only the DP and sidecar substeps.
2. Verify that the repository-portable stacked script executes and produces the same byte hashes on another environment.
3. Test workload-dependent cache policies at equal total memory, preserving all source pins and independent owner/CLAIM authority before any native formal Result.
