# EC49GAP — Targeted cross-union allocation oracle and root conflict certificates

2026-11-26. Independent informed portable continuation of EC49GAO, pinned parent 7402f391a9bb41dcda5b83e72245a1889ab39277:research_notes/portable_direct/EC49GAO_SHARED_ROOT_LABEL_COLORING.md. Frozen BRC16943 inputs unchanged: fourth.json SHA256 228f907796e82fe17b7984123d636a81d6d6a1bc94e357629a6a98071b390923; ga_nodes.txt c69d3222a0378363f8e2e238cedc6a4839edfd867435155fef83d8268c3812f0. Parent archive manifest checked. Same finite distinguishable population and labeled binary unit-cost physical observations as GAO; no native state/dynamics promotion.

## Targeted cross-union theorem

For two residual competitor sets A,B subset S, target T subset S, remaining budget d, let V_d(A,U) be the maximum number of members of U subset A identifiable by one depth<=d physical tree on the full competitor set A. Let C_d(A,B;T) be the maximum number of distinct targets in the union of two such recovered groups, one from each residual (the two groups need not come from the same physical root). Put L=T intersect (A minus B), R=T intersect (B minus A), X=T intersect A intersect B. Then

C_d(A,B;T) = max_{Y subset X} [ V_d(A,L union Y) + V_d(B,R union (X minus Y)) ].

Proof: each partition assigns each target to at most one side; optimizing each assigned subset independently produces disjoint recovered target groups and hence a valid cross-union. Conversely, for any pair of recovered groups, assign every recovered overlap target to one of its successful sides, assigning other overlap targets arbitrarily. Every recovered target then contributes to at least one of the two assigned-group capacities. Taking both maxima proves equality. All competitors stay in A or B, including those outside the assigned target subset. The same proof applies to arbitrary nonnegative additive target weights with cardinality replaced by total weight; the executed tests use integer unit weights only.

To decide C>limit, first reject if |T intersect (A union B)|<=limit. In a partial assignment (L',R',X') (assigned left, assigned right, undecided, all disjoint), monotonicity gives the upper bound V_d(A,L' union X')+V_d(B,R' union X'). If <=limit the entire allocation subtree can be discarded. Two extreme assignments give lower bounds V_d(A,L' union X')+V_d(B,R') and V_d(A,L')+V_d(B,R' union X'); either >limit proves a cross violation. Otherwise split one overlap bit into the two assignments. At X'=empty the upper bound is exact. Induction proves the threshold algorithm terminates with the exact directed-edge predicate. Each recursive V uses fixed actual binary splits, singleton/zero-budget bases and the leaf-count upper bound min(|U|,2^d). The target mask restricts credit, not competitors. Worst-case overlap search is exponential in |X|, and scalar DP has its own cost; no general complexity improvement claimed.

For GAO root masks q,r use A=q, B=S minus r and d=k-1. A downward-closed observer consisting of simultaneous inequalities |Z intersect T_i|<=b_i is certified by the graph union of these directed tests symmetrized. All diagonal products must satisfy each constraint (either verify by scalar root recursion or use a separately established certificate). GAO's coloring equivalence then yields an exact minimum label count for this observer. Crucially, this construction never enumerates the full recovered target family; exact child scalar values suffice. It can also substitute any sound upper bounds to certify absent directed edges, and any realizable lower bounds to certify present edges, deferring unresolved edges. A conservative extra-edge coloring still certifies the desired bound but may not be minimal. This is a typed observer-specific repair, not permission to combine incompatible physical trees.

## Execution and evidence

From verified GAO reproduction archive run python root_target.py > gap_target.json. Source at 8a312fa0c57312837cd89e004e07eb2860cda984:research_artifacts/portable_direct/EC49GAP/root_target.py, SHA256 d4c84e721359d1caad44c3b77df85e8d406a349a107a57a9661e174a0c12929f. In each of 180 frozen records at original and +1 budget, the capacity threshold comes from exact scalar recurrence (not the saved family); GAO data supplies query mask order and validation only. Node125 additionally tests the six rank11 targets at threshold 10 (known obstructions, not independently discovered here). Separate maximal-family enumeration after graph construction checks every adjacency row; all 366 goal graphs across 360 cases agree. Raw output gap_target.json SHA256 392de76fa357280c5bcf949b8280871e70bf2e1381b4cb2ed2d12db7593374a5 (100335 bytes, includes nondeterministic timing). Stats: 87058 directed threshold calls, 67541 immediate size prunes, 329958 allocation nodes, 173544 sum-bound prunes, 536 extreme-assignment successes, 858358 scalar cache misses. Combined graphs 528 undirected edges; 5348 labels -> 436 classes (284 one-label, 76 two-label; original-budget classes total 255). Exact clique size matches coloring in all 360 cases; separate decode and full partition, edge symmetry, independence, clique checks also passed. These are capacity-specific graphs (plus six targets at one case), not the full GAO family graphs.

Node125: capacity threshold 13, six target masks 29559,30071,30327,30579,30581,30582. Individual edge counts 6,3,3,2,3,3,2; union 14. Same two classes as GAO: [0,255,48059,56797,61680,65280,65535] and [187,221,224,238,45232,47872,53456,56576,57344,60928]. Clique [187,65535] proves minimum two. The scalar-only targeted route therefore reconstructs the exact combined binary-label certificate without full-family construction.

Sequential local accumulated measurements: scalar threshold generation 127589096 ns, targeted graphs 2517013810 ns, separate maximal-family graph reference 4954658978 ns. Targeted plus threshold about 2.645 s versus reference 4.955 s (~1.87x); single run, reference compares the same selected goals, timing excludes color/clique, IO, and C++ integration. Not a general speed claim.

Full graph certificate at f90a8c5e516a902096c1975421934cbbdb1e12ef:research_artifacts/portable_direct/EC49GAP/gap_cert.zlib.b64, file SHA256 d7a191096a3ce9d009228b766c2e9a6381efd3b9280ce88727e7cfe95137d0cd. Decode base64 then zlib: 21696 bytes, SHA256 6326214d71991991717e594a247391b2bbbab848435ae22499773e8175e0eb79. Each row [node,budget,capacity,adjacency_arrays,color_masks,clique_mask], GAO query order, same goals as above. All 360 decoded rows matched raw result.

## Fourth-layer progress (existing GAK solver only)

Compile g++ -O3 -std=c++17 gak_solver.cpp -o gap_solver; source SHA256 9fd83afbcdb37eeef76825fc1448fcdf00b09e090943def7edcba914e2007145. Run python retry_gai.py 72 80 250000 > gap_fresh.in (SHA256 fed8095d9faeb4267d9dbf3c1136d96f6db549e5ef74ab2890873dccee3ed63f); EM_DENSE=1 EM_FAST=1 EM_WORD=1 ./gap_solver. Baseline same indices cap 1200000, omit EM_WORD (input SHA256 ab381d024433acc01c14f1bcabcfbabce729690f8760ea8b3010f9176ba87aa3). Initial Hall run 1965 capped; targeted retry index 75:76 cap 1200000 (input SHA256 c966252e4ff381fab9d124a94fb62d5d50264e55fe396e5b88d7dbb67819dc24) independently proved NO. Actual raw Hall rows:
1962,1710,1,21350,0,0,0,115,48,0,48,50,21131,17850
1963,1713,1,22153,0,0,0,1025,270,0,270,718,21757,16593
1964,1714,1,96918,0,0,0,2122,471,0,471,1368,96334,83006
1965,1717,0,250001,0,0,0,8885,1966,0,1966,6547,248105,209337
1966,1721,1,9404,0,0,0,8885,1966,0,1966,6547,9344,8412
1967,1721,1,9404,0,0,0,8885,1966,0,1966,6547,9344,8412
1968,1723,1,50631,0,0,0,9246,2014,0,2014,6715,50263,41619
1969,1723,1,50764,0,0,0,9435,2031,0,2031,6783,50491,41417
Hall retry:
1965,1717,-1,271162,0,0,0,7298,1747,0,1747,5753,269203,226627
Baseline:
1962,1710,1,41609,1137,0,0,1381,333,0,333,1207,0,0
1963,1713,1,35022,429,0,0,5277,1106,0,1106,4678,0,0
1964,1714,1,154726,2723,0,0,9247,1724,0,1724,7808,0,0
1965,1717,-1,481235,21527,0,0,31235,5402,0,5402,26351,0,0
1966,1721,1,15914,0,0,0,31301,5403,0,5403,26352,0,0
1967,1721,1,15914,0,0,0,31366,5403,0,5403,26352,0,0
1968,1723,1,94655,781,0,0,32816,5574,0,5574,27204,0,0
1969,1723,1,75874,2074,0,0,33204,5603,0,5603,27328,0,0

Final both configurations agree 7 YES, 1 exhaustive NO, 12025 labeled states replayed per configuration. Initial Hall 3.69 s + retry 2.21 s including the capped attempt, baseline 12.08 s; 781787 vs 914949 ordinary calls including cap/retry (or 531786 vs 914949 using final determinations only). New frontier 1955 YES/42 NO/396 OPEN of 2393, ordered histories 3965 YES/70 NO/660 OPEN of 4695. 25<=M14<=27 unchanged. GAP not integrated into C++.

## Control and next

Global snapshot 2817619d91588e4ac66fcaa80e6e37dd840ba22f, Source current 4f69f73cbd8917adf318f7f73420f96c28c99140; current entries/P000/ACTIVE worldview/portable and continuation protocols read; same verified normative blobs reused. Original topic receipt r4-20261126-1430-ec49as-read SUCCEEDED, observed 2026-11-26T06:29:35.895393Z, NO_CANONICAL_PUBLICATION_DIRECTORY, native owner projection not evaluated. Historical EM-DIRECT-23537B only, private session/Activity binding unconfirmed; no shared CLAIM, no replacement identity. Next: plug cheap Hall upper bounds into partial assignment before exact scalar recursion; measure on root-specific observer goals, then continue original OPEN list index 80 onward while preserving earlier unresolved indices. AUTHOR_PROVED / EXACT_FINITE_TARGETED_CONFLICT_CHECK / PARTIAL_EXACT_ROOT_REPLAY / NOT_REVIEWED.
