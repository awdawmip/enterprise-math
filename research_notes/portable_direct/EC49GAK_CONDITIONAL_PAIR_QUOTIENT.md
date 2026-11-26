# EC49GAK — Conditional child-pair quotient and adjacent-budget proof reuse

2026-11-26. Continuation of GAJ, immutable parent cf710b66bbbf578b4c4d1199089e16cbea081d13:research_notes/portable_direct/EC49GAJ_FIBER_GATE_AND_MASK_PRODUCT.md; artifact parent 9aaec86b43b648c3c9e733a83c2aa9b7b8e3c129. Frozen BRC16943 fourth.json SHA256 228f907796e82fe17b7984123d636a81d6d6a1bc94e357629a6a98071b390923, ga_nodes.txt c69d3222a0378363f8e2e238cedc6a4839edfd867435155fef83d8268c3812f0. Parent local archive manifest checked. Static binary unit-cost observer, same physical 10x25 queries and normalized capped hole-set fibers, P000 unchanged.

## Proof and scope

Let N(S) be the exact GAJ canonical state (active support mask plus sorted pairs of mandatory/free support masks for each column). N retains the full fiber relations up to column permutation. In particular, the set of available physical row/column observations is equivariant under that permutation; cardinalities, feasibility and physical witness recoverability are preserved. For a nonconstant first query q, define K(q) as the unordered pair {N(S_yes(q)),N(S_no(q))}, retaining both entries even if equal. In the full-recovery Boolean recursion, the contribution of q at depth k is F_(k-1)(N(S_yes)) AND F_(k-1)(N(S_no)). Consequently equal K gives identical contributions. Retain one actual q per exact K, with full equality on canonical keys after hashing; no hash-only equivalence. At replay, use the retained physical query and canonical-to-physical column map for each child separately. The child permutations need not agree between queries or between answers. This quotient concerns existence of a full recovery tree, not labeled tree enumeration or arbitrary target weights. A known exact NO child at k-1 eliminates its query; a known NO at k also eliminates it. Both filters preserve all feasible answers. Previous GAJ local masks and envelope gates unchanged.

Budget monotonicity: F_d(S)=1 implies F_(d+1)(S)=1, and F_d(S)=0 implies F_(d-1)(S)=0 for d>=1. A stored success at k-1 can supply the same first physical query at k; a stored exact failure at k+1 supplies failure at k. A cap interruption never enters the memo as NO. The success witness may have children stored only at shorter budgets. Replay first uses the exact remaining-budget key, otherwise descends to an available shorter key and charges only that shorter budget. Existence of such a positive child key follows from the original successful proof (including transitive reuse of an earlier shorter proof); an exact NO at a larger budget would contradict monotonicity. A single-fiber -3 proof is valid at all larger budgets. Induct on proof depth to reconstruct a full tree, then independently filter the original labeled population at each physical answer. No state is erased on the basis of a marginal count; the two full canonical conditional states are retained. This extends GAH/GAJ's exact Boolean branch carrier rather than proposing a new Foundation theorem.

## Execution

Code 2731a1a96defbe85975cb8de9024425659bcbc48:research_artifacts/portable_direct/EC49GAK/build_gak.py, remote blob 4943358e4d41ce9234068b02352fb0ea81fcee75 equals local Git blob; SHA256 49539a2a7673479aafead0eea20f23702a8dd67a74658298ede94800fbd84b80. Rebuild in GAJ archive: python build_gak.py; g++ -O3 -std=c++17 gak_solver.cpp -o gak_solver. Generated source SHA256 aa0cf3e4d39219b44de9969ac882848f2eae3960e017942b647d8247e6324c5b. All modes EM_DENSE=1 EM_FAST=1; EM_PAIR=1 enables both exact child-pair dedup and known-NO child filter; EM_DEPTH=1 enables adjacent-depth reuse and shorter-budget replay. Both enabled on gai_nodes.in: all 360 first three CSV fields match GAJ, 2126 physical states replayed, 2241 exact duplicate query pairs skipped. Raw gak_nodes.csv SHA256 fdf615c173d890f3118547024f18b0721d8b78a54a3d9cde7dfd5db27dc64499. Prior independent Python recurrence applies to the same frozen 360 inputs, not a new independent review.

Fresh roots: python retry_gai.py 16 24 250000 > gak_fresh.in; SHA256 e19f07699284a25b67cf88fcdcd3e30741c3bd273351833268a15652e9de2eb5. All eight were OPEN before this run. Raw CSV fields: id,n,status,calls,envelopePrunes,satChecks,satPrunes,cumulative dense hits,misses,clears,entries,products,depthNo,depthYes,dups,knownNo. Both enabled:
```
1890,1608,1,22303,111,0,0,523,119,0,119,562,0,51,23127,103416
1891,1610,1,80316,2846,0,0,3505,680,0,680,3654,0,149,79216,436764
1892,1613,1,20789,439,0,0,4942,935,0,935,5040,0,73,27497,102515
1893,1615,1,10703,190,0,0,4958,935,0,935,5040,0,28,13660,57390
1894,1615,1,10703,190,0,0,4974,935,0,935,5040,0,28,13660,57390
1895,1615,1,10703,190,0,0,4990,935,0,935,5040,0,28,13660,57390
1896,1615,1,10703,190,0,0,5006,935,0,935,5040,0,28,13660,57390
1897,1616,1,248900,7245,0,0,14592,2681,0,2681,14411,0,470,208921,1350392
```
Baseline GAJ mode:
```
1890,1608,1,27738,118,0,0,816,194,0,194,709,0,0,0,0
1891,1610,1,97213,3363,0,0,4428,851,0,851,4051,0,0,0,0
1892,1613,1,23520,468,0,0,6047,1109,0,1109,5446,0,0,0,0
1893,1615,1,12249,216,0,0,6093,1109,0,1109,5446,0,0,0,0
1894,1615,1,12249,216,0,0,6139,1109,0,1109,5446,0,0,0,0
1895,1615,1,12249,216,0,0,6185,1109,0,1109,5446,0,0,0,0
1896,1615,1,12249,216,0,0,6231,1109,0,1109,5446,0,0,0,0
1897,1616,0,250001,5709,0,0,17417,3075,0,3075,14894,0,0,0,0
```
Pair-only:
```
1890,1608,1,22669,113,0,0,528,119,0,119,562,0,0,24012,103718
1891,1610,1,81574,2968,0,0,3510,680,0,680,3654,0,0,82396,437811
1892,1613,1,21067,457,0,0,4947,935,0,935,5040,0,0,28896,102533
1893,1615,1,10778,190,0,0,4963,935,0,935,5040,0,0,14055,57276
1894,1615,1,10778,190,0,0,4979,935,0,935,5040,0,0,14055,57276
1895,1615,1,10778,190,0,0,4995,935,0,935,5040,0,0,14055,57276
1896,1615,1,10778,190,0,0,5011,935,0,935,5040,0,0,14055,57276
1897,1616,0,250001,7382,0,0,14586,2677,0,2677,14399,0,0,216277,1349239
```
Depth-only:
```
1890,1608,1,27290,113,0,0,811,194,0,194,709,315,113,0,0
1891,1610,1,95587,3231,0,0,4408,849,0,849,4049,1084,292,0,0
1892,1613,1,23177,444,0,0,6018,1107,0,1107,5444,190,117,0,0
1893,1615,1,12127,212,0,0,6062,1107,0,1107,5444,63,50,0,0
1894,1615,1,12127,212,0,0,6106,1107,0,1107,5444,63,50,0,0
1895,1615,1,12127,212,0,0,6150,1107,0,1107,5444,63,50,0,0
1896,1615,1,12127,212,0,0,6194,1107,0,1107,5444,63,50,0,0
1897,1616,0,250001,5611,0,0,17317,3070,0,3070,14889,1155,769,0,0
```
Baseline, pair-only, depth-only, combined respectively normal calls 447468,418423,444563,415120; wall seconds 5.07,4.09,5.54,4.85; peak RSS KiB 123352,126084,124300,125916. These are sequential single-run observations, not a robust speedup claim; calls exclude dense work and different completion coverage changes comparisons. Combined skipped 393401 duplicate pairs and 2222647 known-NO candidates; reused 855 adjacent success proofs. Depth-only reused 2996 NO and 1491 YES. In combined mode NO proofs are also consumed at query enumeration, so its depthNo counter is not total NO reuse. Baseline separately run for just 1897 with cap 1000000: 1897,1616,1,374563,9878,0,0,15285,2929,0,2929,13564,0,0,0,0; 5.05s, 184152 KiB. Input SHA256 72fe905b0f676b25f50d5c3c8e91ba142eafe2fcb057fab29e5a337801eb5e7f, obtained by extracting last case and changing cap. Full labeled replay succeeds for all 12907 states in combined and in baseline (seven original plus 1897 separately); separate pair/depth ablations also replay 11291 states each.

## Frontier
Eight new exact YES, 21 ordered histories (2,1,3,2,6,1,3,3). Fourth-layer frontier 1915 YES / 27 NO / 451 OPEN of 2393, ordered 3881/46/768 of 4695. 25<=M14<=27 unchanged. No closed roots reopened except immediate same-batch proof verification and ablation. Next: reduce full child normalization cost by cheaper exact column-class refinement and measure high-depth candidate-generation time; target fresh OPEN roots. Preserve exact pair equality, physical labels, and cap-unknown states.

## Control
GK immutable read a6babd6a414e645b42cc21d14bfef8d1e35eb908; Source b8cc35e065391066f098dc1e1de907a4bcdb0a4a. r4-20261126-0936-ec49as-read SUCCEEDED at 2026-11-26T01:36:48.965292Z, NO_CANONICAL_PUBLICATION_DIRECTORY, not an owner projection. Historical EM-DIRECT-23537B; current private identity and Activity unconfirmed. Independent portable research, no new identity or shared CLAIM/Result/Review mutation. AUTHOR_PROVED / EXACT_FINITE_PAIR_DEPTH_PHYSICAL_REPLAY / PARTIAL_EXACT_BRANCH_REPLAY / NOT_REVIEWED.
