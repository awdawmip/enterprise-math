# EC49GAJ — Exact fiber gate and factored physical query masks

2026-11-26. Continuation of GAI, immutable parent ac821de278362945741ba6195280a4fcc4c87b73:research_notes/portable_direct/EC49GAI_BOUNDED_DENSE_BOOLEAN_SOLVER.md. Original frozen BRC16943 fourth.json SHA256 228f907796e82fe17b7984123d636a81d6d6a1bc94e357629a6a98071b390923 and ga_nodes.txt c69d3222a0378363f8e2e238cedc6a4839edfd867435155fef83d8268c3812f0 verified from GAI archive; parent manifest checked. P000 unchanged; finite static observer scope.

## Exact gate and representation

For a normalized support fiber u with mandatory holes B and free columns P, its admissible hole sets are B union Z, Z subset P and |B union Z|<=14. Normalization deletes free columns when |B|=14 and deletes impossible fibers. Let p=|P|. For p>0, the states B and B union {j} for each j in P all exist. They have identical support u. A physical query (r,c) returns (r in u) AND (c not in holes); to distinguish B from B union {j}, any successful path of B must query column j with r in u. Thus at least p observations are necessary in the whole population, even if other fibers coexist. A single fiber is fully recoverable in p queries: choose a fixed supported row and observe each free column. Consequently any fiber with p>k implies NO; if exactly one fiber and p<=k, return the existing -3 witness, or singleton leaf. This reuses the original FZV gate inside GAI's dense_install, not a new claim of novelty for the lower bound. Both the root call and recursive witness installation use the same gate. Every -3 record is handled by the inherited physical replay, which checks budget, unique final state and all remaining physical column labels.

Factored signatures: on the identical ordered dense state list, define R_r={i:r in u_i} and C_j={i:j not in h_i}. The actual physical response mask is exactly R_r intersect C_j. Hence computing R and C once and using bitwise AND for each query produces the same masks, including constants and complements, and the same first representative in row-major order. The normalization, cache keys and physical reconstruction remain unchanged. For n<=16 the construction uses O(n(R+C)+RC) word operations rather than O(nRC) per-query state scans (R=10,C=25); this excludes state enumeration, sorting/map overhead and subsequent solving. No overall asymptotic or wall-time acceleration is asserted. The raw joint state list is retained, not replaced by independent counts.

## Actual execution and exact coverage

Code 69d04f635646ac4cf19bee6eec36aadd8142837c:research_artifacts/portable_direct/EC49GAJ/build_gaj.py (blob dbcddf561fcd431a558340ba91b9bdafa43cad06, SHA256 38c6c33eefa33882c00e24f21713e22853c4f2d61dc732f43694f66367ca02a0), remote readback equal and local Git blob equal. Rebuild from parent archive: python build_gai.py; python build_gaj.py; g++ -O3 -std=c++17 gaj_solver.cpp -o gaj_solver. Generated solver SHA256 4a2b067f93e623fdcd859fa72b0f86168281eedd0eca161f46e77ff3c566e817. EM_DENSE=1 EM_FAST=1 selects the new gate and factored masks; EM_DENSE=1 alone is GAI; neither uses original baseline. 360 cases from original gai_nodes.in, all first three CSV fields equal to GAI (already checked against independent Python exact recurrence); 179 YES, 181 NO, 2126 physical-state replays in new mode. Final dense counters hits=1366 misses=284 products=1058 vs GAI hits=2761 misses=286 products=1060. Raw gaj_nodes_fast.csv SHA256 534c5786cd6ba8de224c667b654534ee13d3f72be32ba7c1d1ee114846238926. No claim of independent new review.

Root input: python retry_gai.py 8 16 250000 > gaj_fresh.in. This skips the four previously attempted difficult roots and four GAI successes; all eight selected IDs were OPEN. Input SHA256 ef63d0b8672f7092b92c49b1d097be6545b0166baf7fcaa0d8c9bac0e43e18a3. Each mode completes physical replay on all 12806 labeled states. Raw CSV fields id,n,status,calls,envelopePrunes,satChecks,satPrunes,cumulative dense hits,misses,clears,entries,products.

Fast:
1880,1592,1,24751,518,0,0,2030,431,0,431,1995
1881,1594,1,192102,2647,0,0,9726,1852,0,1852,8525
1884,1603,1,17625,367,0,0,10298,1902,0,1902,8775
1885,1603,1,25575,586,0,0,10711,1903,0,1903,8789
1886,1603,1,11570,240,0,0,11057,1918,0,1918,8875
1887,1603,1,11570,240,0,0,11332,1918,0,1918,8875
1888,1603,1,106237,3528,0,0,13759,2235,0,2235,10382
1889,1605,1,34355,0,0,0,14719,2386,0,2386,11030

Baseline:
1880,1592,1,24872,518,44,0,0,0,0,0,0
1881,1594,1,192595,2647,94,0,0,0,0,0,0
1884,1603,1,17764,367,48,0,0,0,0,0,0
1885,1603,1,25707,586,55,0,0,0,0,0,0
1886,1603,1,11679,240,36,0,0,0,0,0,0
1887,1603,1,11679,240,36,0,0,0,0,0,0
1888,1603,1,106517,3528,40,0,0,0,0,0,0
1889,1605,1,34464,0,25,0,0,0,0,0,0

Fresh fast/base normal calls 423785/425277, wall 4.95/4.89 s, peak RSS 96424/96380 KiB. CSV SHA256 fast fc8737ed6ecd629a41e0156353df33c58c7c6cb418aa6f805fee1e487fcd12fb and baseline dc4c4baa464fbe8883246b77f5822570c42db815be5d3be9e194ecf3d0b9f604. Four historical cap-open roots tested for optimization comparison only (not closed roots); all remain OPEN at 250001 calls. Fast:
1773,1451,0,250001,7286,0,0,18732,3711,0,3711,17108
1813,1495,0,250001,3892,0,0,31453,5606,0,5606,27438
1852,1557,0,250001,1895,0,0,34271,5978,0,5978,29520
1865,1575,0,250001,9055,0,0,42926,7140,0,7140,34916
GAI same-run comparison:
1773,1451,0,250001,7286,0,0,18887,3716,0,3716,17113
1813,1495,0,250001,3892,0,0,31727,5612,0,5612,27444
1852,1557,0,250001,1895,0,0,34644,5984,0,5984,29526
1865,1575,0,250001,9055,0,0,43461,7146,0,7146,34922
Fast/GAI wall 12.39/11.98 s, RSS 125788/126768 KiB. Sequential single runs; no robust speedup; fast code reduces dense calls but total work remains dominated by higher-depth search. Dense work not charged to normal-call cap. No production deployment.

Eight new YES account for 20 ordered histories (3,2,2,2,2,6,2,1). Frontier 1907 YES / 27 NO / 459 OPEN of 2393; ordered 3860/46/789 of 4695. 25<=M14<=27 unchanged. All earlier closed structures untouched. Next: avoid repeating capped roots; target remaining fresh roots and investigate high-depth branch-ordering or paired-depth certificate reuse, with total-cost comparison.

## Control
GK main snapshot 7420da5e9c662454701c959adfeae687d7f3222f; entries and relevant policy blobs checked; Source e5df6b9d494cc6df2efb185cc5ced97e9587a845. r4-20261126-0831-ec49as-read SUCCEEDED at 2026-11-26T00:31:29.968384Z, NO_CANONICAL_PUBLICATION_DIRECTORY, not an owner projection. Historical EM-DIRECT-23537B; current private identity and Activity unconfirmed. Independent portable work, no new identity, no shared CLAIM, no Result/Review mutation. AUTHOR_PROVED / EXACT_FINITE_FIBER_GATE_AND_MASK_REPLAY / PARTIAL_EXACT_BRANCH_REPLAY / NOT_REVIEWED.
