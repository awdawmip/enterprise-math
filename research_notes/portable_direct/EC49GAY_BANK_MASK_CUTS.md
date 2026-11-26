# EC49GAY — Factorized labeled bank-mask Hall cuts
2026-11-26. Informed portable continuation of EC49GAX. Frozen BRC16943. Predecessor: 64cf625454c36c7296ee0c043c623236b410deb1 (GAX evidence and inherited note); no scientific input rebase. Historical provenance EM-DIRECT-23537B, current private own session unconfirmed.

## Exact bank-cut factorization
Let T be a finite set of labeled unit-credit targets, and let independent banks C_i have nonnegative integer resource capacities. On the declared joint Hall observer, target t has eligible positive-capacity resources E_i(t) in bank i; if t is outside the physical side S_i, E_i(t) is empty. Keep all original labels and physical competition states. For W_i subset C_i define F_i(W_i)={t in S_i: E_i(t) subset W_i}. For the joint resource cut W=disjoint union W_i, the exact contained-neighborhood target set is
F_T(W)=T intersect (intersection_i [(universe minus S_i) union F_i(W_i)]).
Proof: E(t) subset W iff each E_i(t) subset W_i, since bank resources are disjoint and t outside a side has no incident edge there. Taking intersection preserves common target identity; summing separate bank counts would duplicate or misattribute it. Consequently the Hall deficit for cut W is |F_T(W)|-sum_i c_i(W_i), and the maximum of these deficits is |T|-H, by the GAW cut formula. For k=|T|-L>0, a cut with |F_T(W)|>=k+sum_i c_i(W_i) certifies H<=L; any k+sum_i c_i(W_i) distinct labels of that set give a valid witness. A miss of a selected cut is not a feasibility certificate.
In particular put all W_i empty. Z=F_T(empty) consists exactly of isolated targets in the combined positive-capacity resource graph. Then H=H(T minus Z), since isolated targets are never matched; H<=|T|-|Z|. If |Z|>=k, prune before constructing combined adjacency, and otherwise remove Z from the abstract matching targets before exact GAV threshold fallback, without removing any physical competition states. For two banks the bitset test is T & (~a | dead_a) & (~b | dead_b), restricted to the finite T. The zero-cut test applies to arbitrary k>0. Once side masks are cached, evaluation of any specified cut uses bank-wise bitset intersections and one population count; machine-word cost O(number_of_banks * ceil(universe_bits/word_bits)), with side-mask construction and storage accounted separately.
For GAX's <=3 certificate, enumerate all positive-capacity W of total capacity <=3-k in increasing capacity: empty, unit singleton, capacity-two singleton, or two distinct unit classes. This is complete by GAW/GAX. Factorized masks avoid reconstructing a combined target histogram or witnesses in the Boolean-only path. The original labels remain available for witness extraction from F_T(W). Current implementation uses binomial bank capacities and existing GAQ side profiles; no physical BRC dynamics or new full-state equivalence claimed.

## Reproducibility and verification
Source inputs unchanged from GAX (actual local SHA256):
ga_nodes.txt c69d3222a0378363f8e2e238cedc6a4839edfd867435155fef83d8268c3812f0
gap_target.json 392de76fa357280c5bcf949b8280871e70bf2e1381b4cb2ed2d12db7593374a5
witness_records.json c75076272328a0d67c4a991cdb02045099e79ddccba71aea32d4824a97b495e7
fourth.json 228f907796e82fe17b7984123d636a81d6d6a1bc94e357629a6a98071b390923
gak_solver.cpp 9fd83afbcdb37eeef76825fc1448fcdf00b09e090943def7edcba914e2007145
Incoming GAX zip CRC passed; manifest references 11 omitted Python __pycache__ files; all remaining listed entries matched. These compiled caches are derived and not inputs to the new executions. Do not describe the predecessor manifest as a fully passing manifest. GAX sparse_hall.py actual local Git blob agrees with remote 36a2ad74a756eb3339b9baf0e405abc46c045966.

In extracted GAX archive run:
python mask_hall.py > mask_hall.json
python mask_verify.py > mask_verify.json
New code: 4785f9e3c795d8e09ad0e7986c790373e8a68f45:research_artifacts/portable_direct/EC49GAY/mask_hall.py, blob f30c26a0b365bf90401480322bd7271bc113311a; SHA256 0d3300a3fb79113d947ad7f34b13085c9ac8f60128bd4e0805424f8420b3add8.
Compact evidence: 0009cfbfe349ec03e99ee5b1f9f0f235aad35141:research_artifacts/portable_direct/EC49GAY/mask_compact.zlib.b64, blob 0119a9e9ba2939e3b0dafa78e3d88100ea7897ee; SHA256 ae08cd385b7889256aa25a6ca5f93a28f8523f6a6d4fab2a1135f1a90e0af9f0. Decode base64 then zlib then JSON; each mode has one full row list, shared stats/search and a 2-element ns list. Reconstruct each run by replacing ns with its scalar value. Equality to all six raw runs was checked. Raw mask_hall.json SHA256 37ddadb2c39b87cc7f935acbed74f97f1bebcde66ebe22860fd4648f1ec7f522.
Verifier: a2d346f7509d0e54e12577b9945d00c9b7200e22:research_artifacts/portable_direct/EC49GAY/mask_verify.py, blob 151d2c945261d8d27c533feb7d54c36570253daf; SHA256 64591a284493bebb2a926e745cb14a0dcbbaf5ee5d1fac9a7214f99d70c1fbd3. For every actual paired call in the frozen cases, reconstruct full combined eligibility and compute the exact exhaustive cut reference; compare with mask threshold. All 14498 agree. Raw output:
{"calls": 6513, "cut_calls": 14498, "exact_cut_checks": 14498, "fallbacks": 6513, "lower_stop": 5818, "one_hits": 1261, "processed": 74606, "sparse_tests": 17293, "targets": 76893, "upper_stop": 695, "zero_hits": 6724, "zero_removed": 8281}
SHA256 cea42d6badd3b87b7ffe8d1cca3f63b5f2b9cc80758ae05123a59e166d742941.

Six timed runs, baseline/zero/sparse/sparse/zero/baseline, each 180 nodes, 360 budget cases, 87058 directed cross calls, identical exact root capacities and adjacency and search stats: scalar_misses=358275, allocation_nodes=41334, paired_calls=14498, paired_prunes=8680. Baseline: 14498 matching calls, 167894 targets, 95919 augment attempts, 5818 lower stops, 8680 upper stops; times ns 1252511837 and 1316428590. Zero-only: 6724 direct cuts, 7774 fallbacks, 8395 isolated targets removed from fallback calls, 89611 fallback targets, 77155 augment attempts, 5818 lower and 1956 upper stops; times 1140803559 and 1189316744. Sparse mask: 6724 zero + 1261 unit cuts (no capacity-two hits), 6513 fallbacks, 8281 isolated targets removed from fallbacks, 76893 fallback targets, 74606 augment attempts, 17293 extra sparse cut tests, 5818 lower and 695 upper stops; times 1143043051 and 1289714318. Mean 1.2844702135s baseline, 1.1650601515s zero, 1.2163786845s sparse. In this local comparison zero-only is the preferred fast path, despite more matching calls than sparse. Timing covers root scalar warmup and graph construction, excludes input read, coloring and C++ integration. No universal speed guarantee. Original competition states remain unchanged. No new physical root integration of GAY.

## New fourth-layer roots
From frozen fourth.json IDs 2002/2003 OPEN. python fourth_input.py 2002 2004 600000 > gay_roots.in. SHA256 4760cfbf54a9ee20a58b89082bf7621fecb70bbf97c963363c2a0e9d094abded.
g++ -O3 -std=c++17 gak_solver.cpp -o gay_solver.
Word configuration EM_DENSE=1 EM_FAST=1 EM_WORD=1; raw CSV:
2002,1787,-1,40413,0,0,0,1515,367,0,367,1295,39900,32597
2003,1787,1,58426,0,0,0,2059,473,0,473,1701,58119,50740
SHA256 689b4f65acf00c998cefab592575450238190846e5b55dc32dd981e98f8a6952.
Baseline EM_DENSE=1 EM_FAST=1; raw CSV:
2002,1787,-1,65671,2233,0,0,5561,1099,0,1099,5162,0,0
2003,1787,1,88611,1961,0,0,7990,1495,0,1495,7309,0,0
SHA256 03fcba687226de1d1365fc8e2f5718004f46fa0fe1361d4491edb425e89d524e.
Two configurations agree; NO below cap, YES explicitly replayed all 1787 physical labeled states in each configuration via GAK's internal independent filtering replay. Evidence frontier now 1966 YES,51 NO,376 other (2393). Including GAR historic report lacking raw evidence:1972 YES,53 NO,368 other. M14 unchanged 25<=M14<=27. Next fresh roots 2004 onward; optimize remaining 695 upper stops using larger cut capacity or side-window unions rather than blanket sparse tests. Keep GAR/GAS recovery separate.

## Control and scope
Original r4-20261126-2330-ec49as-read SUCCEEDED Source b5bd8b79c1a9d8cd2c7290537612bd0fa5870eee, NO_CANONICAL_PUBLICATION_DIRECTORY, no native owner projection. No formal claim, no replacement session, no result/review mutation. Independent portable scientific material only. Activity association pending. Global canonical entries verified main snapshot 7f15f2c50ea9de7d54d9a321f57d40a690e52dd9; applicable P000/ACTIVE/portable and BRC method rules fetched. 
AUTHOR_PROVED / EXACT_FINITE_FROZEN_CUT_CHECK / EXACT_FINITE_FROZEN_CONFLICT_REPLAY / PARTIAL_EXACT_ROOT_REPLAY / NOT_REVIEWED.
