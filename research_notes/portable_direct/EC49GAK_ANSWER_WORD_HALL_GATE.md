# EC49GAK — Binary answer-word interval Hall bound

2026-11-26. Informed portable continuation of EC49GAJ, exact parent cf710b66bbbf578b4c4d1199089e16cbea081d13:research_notes/portable_direct/EC49GAJ_FIBER_GATE_AND_MASK_PRODUCT.md. Frozen BRC16943 fourth.json SHA256 228f907796e82fe17b7984123d636a81d6d6a1bc94e357629a6a98071b390923 and ga_nodes.txt c69d3222a0378363f8e2e238cedc6a4839edfd867435155fef83d8268c3812f0; parent archive all manifest entries matched. Static finite observer on original labeled supports/columns, not a native dynamics or Foundation claim. P000 unchanged.

## Theorem: exact necessary answer-word allocation

In a normalized fiber u, let B be mandatory holes, P free columns, p=|P|, b=H-|B| (H=14 here). Its population consists of B union Z, Z subset P, |Z|<=b. Fix a state with z=|Z|. A physical query (r,j) is positive precisely when r belongs to u and j is not a hole. For each j in Z, the state with that hole removed exists in the same fiber. A path identifying the state must query column j with a supported row to distinguish that neighbor: this forces z distinct negative observations. If z<b, each j in P minus Z can also be added while staying in the fiber, and the same reasoning forces p-z distinct positive observations. These counts are of distinct columns, hence of distinct query steps. When z=b, do not assume the latter neighbors exist. The old full-recovery gate p>k already excludes a normalized fiber (base state witness; b=0 has p=0).

Any identifying leaf of a decision tree of depth <=k may be padded to a binary word of length k, with arbitrary padding. Leaves are prefix-free, hence padded words are distinct even when padding varies per leaf. Let weight count the negative answers (one in abstract binary encoding). The state must receive a word with weight in the interval I=[z,k-p+z] if z<b, or [z,k] if z=b. Thus complete recovery (also recovery of any specified target set with the original competitor set retained) requires an injective assignment of target states to words whose weights lie in their intervals. No raw state or observation labels are collapsed.

There are binom(k,j) words of weight j. For any integer window [a,c] inside [0,k], let N(a,c) be the count of targets whose entire interval is contained in that window. Necessarily

    N(a,c) <= sum_{j=a}^c binom(k,j).

Conversely these inequalities are sufficient for the abstract word assignment, not for physical decision-tree feasibility. Proof: in the bipartite graph states to words, neighbors depend only on weight class. For any subset of states, its union of allowed classes decomposes into disjoint maximal consecutive windows. Each state's nonempty interval belongs wholly to one component. The window inequalities bound the number of these states by the number of words in the union; Hall's theorem gives a matching. Empty intervals are individually infeasible; full solver applies p>k first. In particular two distinct fibers with p=k violate the single weight-zero class at their base states. No global assertion of sufficiency for physical recovery: node 125 below is a counterexample.

For full recovery N is computed without state enumeration: add binom(p,z) into D[z,upper(z)] for each fiber and 0<=z<=min(p,b). Then N(a,c)=sum_{l>=a,h<=c}D[l,h]. A two-dimensional suffix/prefix sum plus binomial prefix sums checks every window in O(sum_u(1+min(p_u,b_u))+k^2) word operations after the existing fiber masks/counts have been constructed. Uses exact integer counts within the present k<=15, 25-column model; implementation stores counts as 64-bit integers. No assertion for arbitrary-size machine words. Failure certifies NO; passing retains the complete joint physical residual.

## Relaxed recovery capacity (not only Boolean)

For a target set T with nonempty intervals define g(a,c)=N_T(a,c)-sum_{j=a}^c binom(k,j). Let Delta be the maximum sum of g over any pairwise disjoint, nonadjacent windows (empty choice gives 0). Then the maximum number of targets assignable to distinct words equals |T|-Delta. Proof: the matching deficiency equals max_{X subset T}(|X|-|neighbors(X)|), by the maximum matching/Hall deficiency identity (equivalently add universal dummy words). Each neighbor union is a union of whole weight classes and decomposes into consecutive windows. For a class union J the largest eligible subset consists of all targets with I contained in J; its neighborhood is contained in J. Maximizing eligible count minus word capacity over J gives the same deficiency in both directions. Counts and capacities add over separated components. An empty interval, if present, is excluded and counted as one unavoidable missed target. Dynamic programming over right endpoints gives f(c+1)=max(f(c), max_{0<=a<=c}[f(max(0,a-1))+g(a,c)]) with f(0)=0. The actual physical capacity V_k is at most the relaxed matching capacity. This is an exact calculation of the relaxation, not a quotient for stronger observations.

## Executed verification

Scripts (both earlier blobs read back; capacity script also read back):
- ac88a6fa147e472401b9a68f28afd31e3a965ef7:research_artifacts/portable_direct/EC49GAK/build_gak.py; Git blob 5595e501284d87e38fbdc13ebcaade048fe53442, local SHA256 5df50025a3470bcebae2df985fc67562f83935e7e0e6ee8ffa155a52b79f2353.
- 36d85a5f70881261176f4774752ee581d30b10bc:research_artifacts/portable_direct/EC49GAK/verify_gak.py; Git blob b8c56b976e604ffccea10e19ac43357ea8e09cfb, local SHA256 57d7807efd7fb82dcf24d3e82656677adfa0b261ee8a0a8f5f663b5d65f449d0.
- d589ea30e417d756772335ff981bc5efc89eb277:research_artifacts/portable_direct/EC49GAK/word_capacity.py; SHA256 9bf410444ae685f20e56a9fed5b31c7197f761a5582cdcd740628f2012e70f04.

From GAJ archive run python build_gak.py, g++ -O3 -std=c++17 gak_solver.cpp -o gak_solver; generated C++ SHA256 9fd83afbcdb37eeef76825fc1448fcdf00b09e090943def7edcba914e2007145. EM_DENSE=1 EM_FAST=1 for GAJ mode; add EM_WORD=1 to enable the new gate above low-budget dense solver. Existing cap counts ordinary search calls, not dense calls. Every successful root invokes inherited full physical replay. No change to existing proof/replay or deployment.

Python verifier compared 180 frozen difficulty records at original budget and +1 against independent exact subset recurrence, 360 cases: 179 YES, 181 NO; all 179 interval rejects are NO, all beyond the old state-count and max-free gates. At original budget 179/180 nodes rejected. Only original node 125 passes yet is NO; node 28 at budget +1 also passes yet is NO. Compared all 2706 saved GAG minimal obstruction records, 182 detected (all rank 2; total rank-2 records 183), no rank>=4 minimal record detected. In 140/180 records smallest overload-witness size equals the true minimum obstacle rank. Thus the method often certifies whole-node failure without isolating actual high-rank minimal obstructions. In all 180 original-budget cases the explicit augmenting-path word matching agrees with interval-deficiency DP; relaxation exceeds actual capacity in every case: gap 1 in 155, gap 2 in 23, gap 3 in 1, gap 4 in 1. Node 125 has n=16, k=4, exact capacity 13 vs relaxed 16; its eleven-rank obstacles remain genuine joint restrictions outside this relaxation. Raw verification outputs preserved in companion evidence below / archive.

## Root experiments

Inputs generated by python retry_gai.py 16 24 250000 and 24 32 250000, skipping all previously closed and previously attempted roots; SHA256 e19f07699284a25b67cf88fcdcd3e30741c3bd273351833268a15652e9de2eb5 and 91ecbe87c71baa5f6e9ebf210ccaebf5758f997b98485fc49ef2ebb1df6a77d0. Root ID 1897 and 1901 baseline higher-cap replays use the same state lists, cap 800000; input hashes b8c0adfc2d1e45ee03ca515f8600ee8e03caa785e068f848317743415f256e98 and 7c762dda0f94c5a93d20377840a8981c1f2b32b43dcc20a4831aefb4d84583de respectively.

CSV: id,n,status,calls,envelopePrunes,satChecks,satPrunes,cumulative dense hits,misses,clears,entries,products,wordChecks,wordPrunes. 1=YES,0=cap OPEN,-1=NO.

New gate batch 1 (3.030210433 s):
1890,1608,1,19389,0,0,0,132,39,0,39,54,19164,16286
1891,1610,1,60223,0,0,0,650,172,0,172,428,59904,53468
1892,1613,1,14396,0,0,0,932,228,0,228,636,14195,11787
1893,1615,1,7321,0,0,0,943,228,0,228,636,7200,5729
1894,1615,1,7321,0,0,0,954,228,0,228,636,7200,5729
1895,1615,1,7321,0,0,0,965,228,0,228,636,7200,5729
1896,1615,1,7321,0,0,0,976,228,0,228,636,7200,5729
1897,1616,1,203404,0,0,0,4930,1237,0,1237,3712,202164,175025

GAJ control batch 1 (9.308920973 s):
1890,1608,1,27738,118,0,0,816,194,0,194,709,0,0
1891,1610,1,97213,3363,0,0,4428,851,0,851,4051,0,0
1892,1613,1,23520,468,0,0,6047,1109,0,1109,5446,0,0
1893,1615,1,12249,216,0,0,6093,1109,0,1109,5446,0,0
1894,1615,1,12249,216,0,0,6139,1109,0,1109,5446,0,0
1895,1615,1,12249,216,0,0,6185,1109,0,1109,5446,0,0
1896,1615,1,12249,216,0,0,6231,1109,0,1109,5446,0,0
1897,1616,0,250001,5709,0,0,17417,3075,0,3075,14894,0,0

New gate batch 2 (9.178774112 s):
1898,1623,1,144546,0,0,0,888,261,0,261,651,144062,129711
1899,1625,1,125674,0,0,0,1343,323,0,323,767,125238,112675
1900,1625,1,63227,0,0,0,1936,417,0,417,1051,62803,54646
1901,1626,1,184384,0,0,0,3436,668,0,668,1947,183638,164251
1902,1633,1,54304,0,0,0,4970,1049,0,1049,3051,53618,40844
1903,1635,1,14857,0,0,0,5142,1054,0,1054,3058,14626,11445
1904,1635,1,102622,0,0,0,5808,1132,0,1132,3378,102145,91265
1905,1639,0,250001,0,0,0,11185,2242,0,2242,6995,248255,216148

GAJ control batch 2 (22.795297129 s):
1898,1623,1,209236,3177,0,0,6092,1245,0,1245,5901,0,0
1899,1625,1,186527,956,0,0,11398,2036,0,2036,10501,0,0
1900,1625,1,109609,2617,0,0,13822,2386,0,2386,12086,0,0
1901,1626,0,250001,6690,0,0,17984,2988,0,2988,15050,0,0
1902,1633,1,85178,1745,0,0,21950,3723,0,3723,18027,0,0
1903,1635,1,26126,266,0,0,23178,3890,0,3890,18847,0,0
1904,1635,1,149868,3499,0,0,24727,4006,0,4006,19435,0,0
1905,1639,0,250001,6392,0,0,38330,6041,0,6041,30157,0,0

Extra GAJ higher-cap baseline (separate process each):
1897,1616,1,374563,9878,0,0,15285,2929,0,2929,13564,0,0 (7.260915718 s)
1901,1626,1,309313,8053,0,0,8061,1524,0,1524,7236,0,0 (6.487446507 s)

Both implementations therefore completed actual labeled physical replay on all 24309 new YES states each, including higher-cap baseline for 1897 and 1901. 1905 remains OPEN. At equal cap, total ordinary calls 1266311 new vs 1714014 baseline; word checks 1258612, prunes 1100467. Batch wall 12.208984545 s new vs 32.104218102 s baseline (single sequential runs, different outcomes at cap; no universal speedup claim). This includes core solve and physical replay, excludes one-time compilation and input generation. Higher-cap runs are not included in equal-cap timing. New YES roots 1890–1904 account for 34 ordered histories. Frontier 1922 YES / 27 NO / 444 OPEN of 2393; ordered histories 3894/46/755 of 4695. Bound 25<=M14<=27 unchanged.

## Next and control

Prioritize this inexpensive necessary gate rather than expensive low-depth signature expansion; test a selectively applied first-observation-conditioned window bound or additional labeled row/column capacity certificate to discriminate node 125; continue untouched roots after 1905 and keep 1905 open. Exact mathematical progress, not accepted theorem or formal shared Task closure. GK entries/current policy blobs checked at ae0a3c76a3e27ce01c6baac46a357aa99aa13772; Source b8cc35e065391066f098dc1e1de907a4bcdb0a4a. Original topic read r4-20261126-0944-ec49as-read SUCCEEDED at 2026-11-26T01:45:07.913615Z, NO_CANONICAL_PUBLICATION_DIRECTORY, no native owner projection. Historical EM-DIRECT-23537B; current private identity and Activity unconfirmed. No replacement identity, no shared CLAIM or Result/Review mutation. AUTHOR_PROVED / EXACT_FINITE_WORD_HALL_CHECK / PARTIAL_EXACT_BRANCH_REPLAY / NOT_REVIEWED.
