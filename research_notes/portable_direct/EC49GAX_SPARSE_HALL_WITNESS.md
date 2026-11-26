# EC49GAX — Exact sparse Hall witnesses and threshold fallback
2026-11-26. Portable informed continuation of EC49GAW, frozen BRC16943, predecessor 9f251500a7c0b34f0de998a4e9d31295c3a661b6:research_notes/portable_direct/EC49GAW_MINIMUM_HALL_WITNESS.md. Historical provenance EM-DIRECT-23537B; current private own identity unconfirmed. No shared CLAIM or formal Result.

## Theorem and proof
For a fixed finite unit-credit capacitated matching graph with n labeled targets, nonnegative integer capacities c_j and target eligibility E(t), let k=n-L>0. We want a Hall upper certificate A with |A|-c(N(A))>=k and |A|<=3. Remove zero-capacity resource coordinates from the eligibility masks for this observer only (their presence does not affect any neighborhood capacity sum). Original labeled inputs remain intact. Write b(U) for the integer multiplicity of normalized eligibility mask U and z=b(empty). Let I_1,I_2 be the classes of capacities 1 and 2, respectively. By GAW's minimum-cardinality certificate theorem, the optimum certificate of at most three targets, if one exists, is k plus the least capacity of W with |F(W)|>=c(W)+k and c(W)<=3-k. For k>3 this is impossible. For k=1,2,3, all possible positive-capacity W are exactly:
- empty: z>=k;
- singleton a in I_1 (only k<=2): z+b({a})>=k+1;
- singleton a in I_2 (only k=1): z+b({a})>=3;
- pair a,b distinct in I_1 (only k=1): z+b({a})+b({b})+b({a,b})>=3.
Each condition gives a certificate by selecting c(W)+k distinct original labels whose normalized neighborhoods lie in W. Its original union has capacity <=c(W); hence the requisite deficit is achieved. Conversely every <=3 witness gives W equal to its positive-capacity neighborhood, necessarily one of the above cases. Testing in nondecreasing cost yields the minimum cardinality within this range. For L>=n return the trivial empty witness. A miss is not a lower certificate; use exact GAV threshold augmentation. This specialization uses the existing positive integer BRC-style neighborhood histogram only for the declared Hall observer; it preserves original physical competition and branch labels. No new physical BRC dynamics or universal physical feasibility claim.

Counting and reconstruction need O(n+m+|I_1|^2) integer-mask operations with a histogram, m number of classes, not O(2^m) zeta or O(n^3) target enumeration. Include mask width and hash costs for a bit-complexity bound. For two binomial banks with d>=1 there are exactly four unit-capacity classes except d=1 where all four are unit; hence at most six pair tests, and only d=2 has capacity-two classes (two). d=0 has two unit classes. The positive integer capacities matter; weighted credit is outside scope.

## Actual validation
Local GAW archive SHA256SUMS checked (362 files). Frozen ga_nodes.txt SHA256 c69d3222a0378363f8e2e238cedc6a4839edfd867435155fef83d8268c3812f0, gap_target.json 392de76fa357280c5bcf949b8280871e70bf2e1381b4cb2ed2d12db7593374a5, witness_records.json c75076272328a0d67c4a991cdb02045099e79ddccba71aea32d4824a97b495e7.
Run python sparse_hall.py > sparse_hall.json in extracted GAW reproduction archive. Code commit 734a089f083ff087ce106fdccb1578e3be0c8662:research_artifacts/portable_direct/EC49GAX/sparse_hall.py, Git blob 36a2ad74a756eb3339b9baf0e405abc46c045966 matches local. SHA256 8692e5a5173d7ae02a4e8cdf5cd23c408c41a193605d7f7f7f4ad8e989c6257a.
Seed 49261130, 2000 arbitrary random graphs, 1..8 classes, 0..14 targets, capacities 0..4. 6672 threshold checks k=1..4 with k<=n against exhaustive target subsets of size <=3. Exact minimum and direct validity checked; zero mismatches. Replayed all 14498 GAW labeled witness records: exact detection of 7985 upper witnesses of size <=3, histogram 1:3153,2:4617,3:215, with minimum cardinality and validity checked. 695 larger upper witnesses remain for fallback, and 5818 lower witnesses. All 360 frozen budget cases/366 goals, four runs in ABBA order (baseline/sparse/sparse/baseline), each 87058 cross checks, identical adjacency, capacities and search counts. Baseline 14498 threshold calls, 95919 augment attempts; sparse 7985 direct hits (91.99% of upper stops, 55.08% of all calls), 6513 fallback calls, 82887 augment attempts (13.59% less), 13032 reconstructed witness identities. Each run allocation nodes 41334, scalar misses 358275, paired prunes 8680. Timings (ns) 1380405691,1314878625,1293339964,1214385920. Mean baseline 1.2974 s vs sparse 1.3041 s; no robust speed improvement, histogram/reconstruction overhead offsets saved augmentations. Not integrated into C++. Next: Boolean-only short-circuit on zero masks (in these frozen records 6724 of the 7985 hits have |A|=k, i.e. zero-capacity union); retain labeled witness mode separately; measure again.

## New fourth-layer roots
Inherited frozen fourth.json IDs 2000/2001 OPEN. python fourth_input.py 2000 2002 600000 > gax_roots.in (SHA256 54678978acc7546422bdb9e0e52983fbab5797070639501820bb042bcfff84d2); g++ -O3 -std=c++17 gak_solver.cpp -o gax_solver. EM_DENSE=1 EM_FAST=1 EM_WORD=1 and EM_DENSE=1 EM_FAST=1 baseline. Raw CSV:
word:
2000,1779,-1,140438,0,0,0,2729,749,0,749,2273,139504,115026
2001,1780,1,26945,0,0,0,3632,900,0,900,2850,26446,20119
baseline:
2000,1779,-1,185478,8276,0,0,7627,1539,0,1539,6519,0,0
2001,1780,1,37651,1052,0,0,9324,1785,0,1785,7573,0,0
Both configurations agree, NO search below cap, YES solver labeled replay check as in GAK. Word CSV SHA256 c1fb9c77b1a0a421937734ddfcb0b55421dd149104a0fb20bada8cf8a8d55ac8, baseline 980caf02157333b85aed321713ed3c942107bc4a1140c1b81d7190572905bc3d. Evidence frontier 1965 YES,50 NO,378 other of 2393. Including historical GAR with missing original evidence:1971 YES,52 NO,370 other. M14 remains 25<=M14<=27. No GAX root integration. Next fresh IDs 2002 onward, preserve GAR/GAS missing original evidence distinction.
Raw per-case JSON SHA256 8f27401eb512ae268aef4581514a3cc61414b182a324a1008c87dba49ec18cc9; local reproduction archive contains complete raw output.

## Control
Original r4-20261126-2227-ec49as-read SUCCEEDED, Source f2b13fd86435e3ae495ac777ddcc25130a233f6c, NO_CANONICAL_PUBLICATION_DIRECTORY, native owner projection not evaluated. Independent portable continuation, no adopted identity or shared task-state mutation. Activity association pending.
AUTHOR_PROVED / EXACT_FINITE_SPARSE_WITNESS_CHECK / EXACT_FINITE_FROZEN_CONFLICT_REPLAY / PARTIAL_EXACT_ROOT_REPLAY / NOT_REVIEWED.
