# EC49GAQ — Paired-bank Hall bound for overlap-credit search

2026-11-26. Independent informed portable continuation of EC49GAP at a361d59055232f3231b6076de1bef98926fb09f6:research_notes/portable_direct/EC49GAP_TARGETED_ROOT_CONFLICTS.md. Same frozen BRC16943 population, fixed binary unit-cost physical observations and target-only credit restriction, not a native geometry/dynamics claim. Input hashes verified against the parent archive: fourth.json 228f907796e82fe17b7984123d636a81d6d6a1bc94e357629a6a98071b390923; ga_nodes.txt c69d3222a0378363f8e2e238cedc6a4839edfd867435155fef83d8268c3812f0. All parent archive manifest entries checked.

## Theorem: joint credit-preserving Hall relaxation

At a partial GAP allocation let L,R,X be disjoint target sets, allowed respectively only in competitor set A, only in B, or in either. Each side has its own bank W_A,W_B of 2^d binary words. For each target x and allowed side i let E_i(x) be any superset of all padded words that can identify x on that side's FULL competitor set. Construct a bipartite graph from targets L union R union X to the disjoint union W_A plus W_B, using only their allowed E_i(x). Write H_pair for its maximum matching cardinality. Then the true optimum over completions of this partial allocation C_partial <= H_pair <= min(|L union R union X|, H_A(L union X)+H_B(R union X)), where H_i is the independent bank matching number.

Proof: each actual recovered target can be credited to a successful side once; distinct identified targets on a side occupy disjoint padded words by prefix-freeness. Hence every actual solution induces a matching. Conversely a matching is an exact solution of the abstract word-bank allocation problem: assign matched overlapping targets to the side of their slot and assign unmatched ones arbitrarily. Restricting the matching to each bank bounds it by its independent matching number. Thus H_pair also equals the maximum over all Y subset X of H_A(L union Y)+H_B(R union (X minus Y)). No physical tree is inferred from a word matching. Hall's deficiency formula gives H_pair=|L union R union X|-max_{U subset targets} (|U|-|N(U)|), including the empty U. Equivalently, maximize |{x:E(x) subset W}|-|W| over slot subsets W, since any U has N(U) subset W when W=N(U), and all targets with neighborhoods contained in W can be used as U. With sign-count word types, whole type classes suffice in this dual: a partly included class cannot contain any complete neighborhood class that was not already contained without that partial class, and deleting it weakly improves deficiency. This yields a two-bank type-cut certificate with exact integer binomial capacities; the executed algorithm uses explicit small word masks and augmenting paths instead. For arbitrary nonnegative additive target weights, maximum-weight matching gives the corresponding upper bound by the same injection.

The joint constraint can be strictly stronger. A strict example with nonempty neighborhoods: take L={a,b,c}, R=empty, X={x}, d=1; a,b,c share one left word, x uses the other left word and one right word. Independent sum=3, joint=2, total=4. The strict example concerns a relaxation, not a realized frozen node.

For physical root sides, condition each support fiber to a truncated Boolean family (the code checks exact count, uniqueness and hole cap). With mandatory holes B, p free columns, b=14-|B|, and z chosen holes, GAK gives allowed negative count interval [z,d-p+z] if z<b and [z,d] if z=b. Empty intervals imply zero eligible words. Each side uses these supersets. The cached interval overload DP computes H_i exactly: on any target subset, the Hall deficiency is the maximum sum of positive overloads over disjoint nonadjacent weight intervals. Any overloaded interval on a subset is overloaded on the full eligible set, so cache only those windows. Remove empty-neighborhood targets before computing deficiency. Partial assignment rejects on independent Hall sum, then optionally paired-bank matching at root, then unchanged GAP exact scalar bound/extremes/recursion. Every new rejection is sound; original recursion decides all undecided cases exactly. Worst-case search is still exponential; matching is not a proof of physical feasibility.

## Executed finite test

Run python joint_hall.py > gaq_hall.json in parent GAP reproduction directory. Exact executed script is stored losslessly as joint_hall.py.zlib.b64; decode with base64 then zlib; SHA256 9a9c24a270ea625527080677340453db4dfedf7731863b6f9a8ffa6ad5c6a063. Parent GAP graph/goal file gap_target.json supplies reference adjacency and same root warmup. For every 180 frozen records at original and +1 budget, every adjacency row was checked against GAP and all three modes agreed. 360 cases, 366 goals, 87058 directed checks each. Aggregate measured counters:

mode,allocation_nodes,scalar_misses,size_prunes,hall_prunes,paired_calls,paired_prunes,sum_prunes,extreme_yes,elapsed_ns
base,329958,858358,67541,0,0,0,173544,536,2523538882
hall,329958,832645,67541,101579,0,0,71965,536,2821348406
paired,41334,358275,67541,5021,14498,8680,15531,536,1307392111

Profile constructions 4409 each Hall mode; Hall cache misses 151040 vs 19451. Paired pruning occurs in 181 of 360 cases. Node125 original budget: 2023 directed checks; 1497 size prunes; 4184 allocation nodes in both modes; paired rejects 14 root allocations but overall scalar misses 24301 vs 24310. Existing combined 2-color certificate and six rank-11 exclusions unchanged, not a new reduction of its exact capacity. The full local output gaq_hall.json SHA256 e4f7015d206d50a9f9e8e43851c928f348bf53fde645989cf4d15fea114d8edb; compact evidence gaq_compact.json.zlib.b64 (decoded SHA256 387b1003ac50376349b920b200ba83d0df831fb0bf39e7d3148d3fd2a2973794), rows [node,budget,paired-prunes,paired-scalar-misses] plus complete aggregate counts and times. Single sequential local run including exact root capacity warmup and graph construction, excluding color, IO and C++ integration; independent Hall alone slower, paired variant ~1.93x faster than base. No universal speed guarantee.

## Fourth-layer independent portable execution (existing GAK only)

Compile g++ -O3 -std=c++17 gak_solver.cpp -o gaq_solver. Use frozen retry_gai.py 80 88 250000 for Hall and 80 88 1200000 for baseline. Both EM_DENSE=1 EM_FAST=1; Hall adds EM_WORD=1. Baseline combined invocation stopped before final row due to tool timeout; separate retry_gai.py 87 88 1200000 baseline completed 1981. Retain original partial output and separate result; do not count an incomplete run as completed. Raw Hall rows:
1970,1724,1,63513,0,0,0,1761,477,0,477,1475,62870,51427
1972,1725,1,100408,0,0,0,3004,695,0,695,2228,99755,82486
1973,1726,-1,191304,0,0,0,9039,2248,0,2248,7228,189708,154177
1974,1726,1,158433,0,0,0,11313,2601,0,2601,8338,157267,126509
1975,1729,-1,242721,0,0,0,14326,2853,0,2853,9218,240847,197081
1977,1733,1,22485,0,0,0,14746,2884,0,2884,9322,22118,17141
1978,1733,1,10859,0,0,0,14763,2884,0,2884,9322,10769,9520
1981,1737,-1,236319,0,0,0,18111,3296,0,3296,10813,234575,189980
Baseline first seven:
1970,1724,1,96119,1081,0,0,5365,1156,0,1156,4804,0,0
1972,1725,1,154573,4983,0,0,10342,1991,0,1991,8873,0,0
1973,1726,-1,278520,12038,0,0,24365,4777,0,4777,21057,0,0
1974,1726,1,221978,10332,0,0,30483,5619,0,5619,24966,0,0
1975,1729,-1,358768,14394,0,0,37526,6225,0,6225,28071,0,0
1977,1733,1,34069,396,0,0,38399,6270,0,6270,28281,0,0
1978,1733,1,20680,0,0,0,38530,6275,0,6275,28312,0,0
Separate baseline:
1981,1737,-1,347589,16881,0,0,20681,4061,0,4061,18782,0,0
5 YES, 3 exhaustive NO, 8641 labeled states per mode successfully replayed by existing solver. Hall 1026042 ordinary calls, baseline final rows 1512296 (excluding lost partial computation for final root). Hall elapsed 8.013 s; no reliable total baseline time due to interruption. Frontier 1960 YES /45 NO /388 OPEN of 2393; ordered histories 3975 YES /75 NO /645 OPEN of 4695. 25<=M14<=27 unchanged. GAQ not integrated into C++.

## Control and continuation

Global main pinned 6571113e5d8b73759ca4522a1e47a445c8a91271; current Source 4b3d656422062c2fc8e29910da57e8ffdff13195. Current bootstrap/manual, P000, joint relation preservation, Heartbeat World, ACTIVE worldview, portable and continuation rules read. Original task lookup r4-20261126-1532-ec49as-read SUCCEEDED at 2026-11-26T07:33:24.536199Z with NO_CANONICAL_PUBLICATION_DIRECTORY; native owner projection not evaluated, no execution authority. Historical EM-DIRECT-23537B provenance only; current private identity/Activity association unconfirmed. No shared CLAIM, no replacement identity. Next: exploit two-bank Hall type-cut witnesses (avoid explicit word expansion at higher depth), selective application of paired matching below root, and continue original OPEN indices 88 onward while preserving earlier unresolved indices. AUTHOR_PROVED / EXACT_FINITE_PAIRED_BANK_EDGE_CHECK / PARTIAL_EXACT_ROOT_REPLAY / NOT_REVIEWED.
