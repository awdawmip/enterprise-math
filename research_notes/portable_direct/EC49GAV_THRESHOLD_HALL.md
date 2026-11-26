# EC49GAV — Exact threshold-only joint Hall matching

2026-11-26. Informed portable continuation of EC49GAU, frozen BRC16943. Historical provenance EM-DIRECT-23537B; current private research identity not confirmed. No shared CLAIM or formal Result.

## Threshold observer theorem

Let G=(T,C,E) be a finite labeled unit-credit target/resource graph, with nonnegative integral class capacities c_j. Let n=|T|, fix a target order, and write h_i for the maximum matching cardinality on the first i targets with all original capacities. For an integer threshold L,

h_i <= H(G) <= h_i+n-i.

The lower bound is a feasible matching in G. For the upper bound restrict any full matching to the processed prefix; at most n-i other credits remain. Thus H(G)>L is settled once h_i>L, while H(G)<=L is settled once i-h_i>=n-L. These certificates are monotone: on adding a target, h_i increases by zero or one, and i-h_i likewise increases by zero or one. At i=n one of the two conditions must hold. For a negative threshold return false; for L>=n return true.

Compute h_i incrementally by capacitated augmenting paths. Starting from an optimum for the previous prefix, a new optimum either has the old cardinality or is one larger. In the latter case the symmetric difference with a larger matching gives an augmenting path from the new target (an augmenting path from an old unmatched target would contradict previous optimality). Each capacity class has interchangeable slots; visiting that class once per search and exploring all its occupants is sufficient to search its outgoing alternating edges. A free slot terminates the path, and reassignment backwards updates a valid matching. Otherwise no augmenting path exists and h_i is unchanged. This supplies the exact prefix maxima and the stopping proof. In the executed code, class masks and free-slot mask accelerate searches; sorting by degree changes only the order. The code still constructs the complete input eligibility masks; it saves matching work, not all input processing. The Boolean result alone is sufficient for the specific cross-bank pruning observation C<=H<=L used in GAQ. An H>L result is not proof of a physical conflict; it merely leaves the physical test open. No deletion of physical competition states or claim about other target weights/observers. Keep complete original states and re-evaluate changed goals.

A useful next extension is a compact explicit upper certificate: after a failed augmentation, the alternating reachable target set and resource set give a Hall-deficient subset (all its neighbors are saturated). For the processed prefix, take the union of reachable sets from all unmatched prefix targets in its maximum matching; all incident resources are saturated, every matched target in the reachable set occupies one of them, and exactly the unmatched prefix targets account for the surplus. Hence their joint deficiency equals i-h_i. If that meets n-L, the same subset certifies the whole-graph upper threshold without replaying all augmentations. The current execution does not yet export these witness sets.

## Actual exact calculation

Source predecessor c067b7a9242afe9eafa6c799cd0416aef2a443cf:research_notes/portable_direct/EC49GAU_CAPACITY_PEELING.md. Verified 344 entries of its reproduction archive SHA256SUMS, frozen ga_nodes.txt SHA256 c69d3222a0378363f8e2e238cedc6a4839edfd867435155fef83d8268c3812f0 and gap_target.json SHA256 392de76fa357280c5bcf949b8280871e70bf2e1381b4cb2ed2d12db7593374a5. Reuse GAQ HallOracle, GAU independent exhaustive capacitated Hall-cut reference and inherited exact physical inputs. The new work is a finite integer matching observer, not new BRC arithmetic or physical interpretation.

Run python threshold_hall.py > threshold_hall.json in the extracted GAU archive. Executed code blob 64e59360facf56a8e737be20f76ac352f49ebe9d at 85f10d9f98984773c8ed93371b7831802d6f631d. Seed 49261128: 3000 arbitrary finite graphs, 1..8 classes, 0..32 targets, capacities 0..6. For every integer L=-1..n, compared with exact exhaustive Hall cut: 53534 threshold tests, all agree.

180 frozen nodes, two budgets per node, 366 goals, 87058 directed conflict checks per mode. All graph adjacency entries and all existing per-case search counters match GAP/GAQ. Both modes: 41334 allocation nodes, 358275 scalar cache misses, 14498 paired calls, 8680 paired prunes. New mode: 167894 input target records, 95919 actual prefix augmentation attempts, 5818 lower-threshold stops (no Hall prune), 8680 upper-threshold stops (Hall prune). 42.8693% fewer prefix target processing attempts than processing all input targets. Baseline word mode 1.325234033 s; threshold mode 1.183414400 s (one sequential run, 10.7015% less wall time, factor 1.11984); includes exact root warmup and graph construction, not coloring or C++ integration. No universal speed claim.

Compact evidence 9a242e063ec8078da7f16294fbb7ed1549553964:research_artifacts/portable_direct/EC49GAV/threshold_compact.zlib.b64, Git blob da35b27f5250b9a3c3c7210f1c5c319e4b0a08e2. Base64 decode and zlib decompress; JSON SHA256 266301217bab08c22e8a17999e5f33ee30bc4dcbbd2e16b55dc56e4152d1cbd7. Contains per-case counters for all 360 cases and aggregate summary. Complete raw output retained in reproduction package, SHA256 34c14d86d3544498d292264467fc80ac11a8df6a8e5b347b3284c2d26b2ad989.

## Four fresh fourth-layer roots

Inherited fourth.json, gen.py, fourth_input.py and gak_solver.cpp. python fourth_input.py 1994 1998 600000 > gav_roots.in, input SHA256 c455211b81cab97a3f1577001ce49968b4c0537fca1b464328348eff31ae1be2. g++ -O3 -std=c++17 gak_solver.cpp -o gav_solver. EM_DENSE=1 EM_FAST=1 EM_WORD=1 and EM_DENSE=1 EM_FAST=1 baseline. GAK solver automatically replays every actual labeled state for YES; exhaustive NO is -1, timeout/budget stop is 0. No new threshold code integrated in C++.

Word raw CSV:
1994,1759,1,10857,0,0,0,254,85,0,85,170,10684,8742
1995,1761,-1,41395,0,0,0,503,150,0,150,318,41125,34922
1996,1761,-1,41395,0,0,0,615,150,0,150,318,41125,34922
1997,1764,1,13256,0,0,0,1827,464,0,464,1301,12847,8848

Baseline raw CSV:
1994,1759,1,23626,452,0,0,1428,330,0,330,1219,0,0
1995,1761,-1,59314,1280,0,0,2736,560,0,560,2335,0,0
1996,1761,-1,59314,1280,0,0,3078,560,0,560,2335,0,0
1997,1764,1,22159,457,0,0,7101,1392,0,1392,5879,0,0

Both configurations agree; 3523 physical YES states replayed per configuration, two complete NOs. These IDs are beyond GAU and GAR's reported batch and marked OPEN in frozen fourth.json. From GAU durable evidence: 1963 YES, 48 NO, 382 other structures, total 2393. If adding the eight GAR historically reported but incompletely preserved roots, 1969 YES/50 NO/374 other; distinguish these totals. M14 bound remains 25<=M14<=27. No attempt to reconstruct unavailable GAR/GAS raw evidence as if original.

## Control/next

Current RS-EC49AS read r4-20261126-2031-rs-ec49as-read SUCCEEDED, source 9c87d27e47ea4ef94b0321ad6f20db5076098928, NO_CANONICAL_PUBLICATION_DIRECTORY, native operational view not evaluated; no formal execution authority or new identity inferred. Existing historical identity retained as provenance only. Activity association pending. Next: derive and export compact Hall-deficiency witnesses, consider root-specific threshold order that brings earlier certificates, and compare on frozen cases; continue next fresh root IDs 1998 onward after checking evidence and other authors. GAR/GAS original artifact recovery remains open. AUTHOR_PROVED / EXACT_FINITE_THRESHOLD_CUT_CHECK / EXACT_FINITE_FROZEN_CONFLICT_REPLAY / PARTIAL_EXACT_ROOT_REPLAY / NOT_REVIEWED.
