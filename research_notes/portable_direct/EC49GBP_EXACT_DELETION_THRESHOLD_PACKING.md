# EC49GBP — exact deletion threshold via disjoint deficit packing
2026-11-27. AUTHOR_PROVED / EXACT_FINITE_FULL_FROZEN_D0_D1_D2_REPLAY / PARTIAL_EXACT_ROOT_REPLAY / NOT_REVIEWED.
Predecessor 81746986338df1e24a1be48aaba1a2648b14b61e:research_notes/portable_direct/EC49GBO_DELETION_HORIZON_ENVELOPE.md. Same BRC16943 labeled integer-mask matching observer and frozen inputs; no native physical reinterpretation. New result replaces the existential multicover condition of GBO with a constructive packing min-max equality.

## Theorem
For fixed W subset C let R=C\W and s(W)=c(W)-f_A(W). Let rho(W) be the minimum number of original labeled targets whose deletion makes W a strict suffix-minimum row (in P(s+f_D)); infinity if impossible. If R contains a zero-capacity port then rho(W)=infinity, since extending W by that port alone cannot strictly increase raw weight after any deletion. Otherwise
rho(W)=max over pairwise disjoint nonempty subsets V_1,...,V_k of R of sum_i [1+s(W)-s(W union V_i)].
Empty packing is allowed and has value zero. W belongs to GBO R_d iff rho(W)<=d. The formula works for W=C, duplicate masks, empty neighborhoods and arbitrary nonnegative integer capacities. The term 1 is essential for strict dominance.

Proof: Ignore targets already contained in W; for every other original label x project its neighbor mask to nonempty E_x\W in R. Let f_I(V) count projected labels of retained family I contained in V. The strict inequalities after deletion are precisely f_I(V)<=c(V)-1 for all nonempty V subset R. Any admissible deletion must pay at least f_Aproj(V)-c(V)+1 for each chosen block V. Disjoint blocks count disjoint projected labels, so their sum is a lower bound. To attain it, greedily insert projected labels into an initially empty family I whenever all inequalities remain valid. Empty I is feasible by positive capacities. A rejected label must lie in a nonempty tight set T satisfying f_I(T)=c(T)-1; later accepted insertions cannot destroy tightness because counts are monotone and feasibility maintained. For intersecting nonempty tight sets X,Y, supermodularity of f_I and modularity of c imply both X union Y and X intersection Y tight: the sum of the two deficits equals zero and feasibility makes each nonnegative. Thus the inclusion-maximal nonempty tight sets at the end are pairwise disjoint. Every rejected label lies in one, and in at most one since projected masks are nonempty. For each maximal tight set V, the number of rejected labels it contains equals f_Aproj(V)-c(V)+1 = 1+s(W)-s(W union V). These blocks achieve the actual greedy deletion count, which therefore equals the packing lower bound and is optimal. This supplies a primal witness (deleted labels) and a dual certificate (disjoint tight blocks) when the greedy construction is used. The implementation here computes the value by DP rather than producing all witnesses. This is related to capacitated hypergraphic sparsity, not an assertion of novelty of classical matroid theory.

## Algorithm
For fixed W with positive outside capacities, define P(empty)=0. For nonempty V subset R, choose its lowest bit i and set
P(V)=max(P(V\{i}), max_{i in T subset V}(P(V\T)+1+s(W)-s(W union T)).
By splitting a packing according to the block containing i or leaving i unused, induction gives rho(W)=P(R). O(3^|R|) operations and O(2^n) reusable memory; all W cost O(4^n), plus raw cut construction O((n+|A|)2^n) in this implementation. No claim that this dominates GBO for d=1 or is polynomial in port width. Unlike enumerating all deletion subsets, cost does not depend exponentially on target count. Every horizon is obtained from one threshold table. For fixed small d, pruning negative blocks and capping DP at d+1 are candidate future improvements.

## Executed evidence
Code 03ccff5134e92b1710af28ff96abfdd01a8952ec:research_artifacts/portable_direct/EC49GBP/horizon.cpp (remote and executed local Git blob 502ccf460b63b50c9b041a14e9989a41cb1744ba; SHA256 999466b14c35f61f31f7134e22c3ebd11aa6bf895620de10b0e2e7777d147153).
Frozen witness_records.json from GBJ reproduction archive SHA256 c75076272328a0d67c4a991cdb02045099e79ddccba71aea32d4824a97b495e7, matching GBO. Fourth.json SHA256 228f907796e82fe17b7984123d636a81d6d6a1bc94e357629a6a98071b390923.
Input conversion: for each r in json.load(open('witness_records.json')): c=r['caps'];a=list(r['opts'].values());print(len(c),len(a),*c,*a). Frozen.in SHA256 95b400c2fdf75a965bd5059f6b3b987dfc4bac589d9504a1610abe482b4546b5. Run g++ -O3 -std=c++17 horizon.cpp -o horizon; ./horizon < frozen.in. Reference uses independent suffix-minimum computation for explicit deletions; random exhausts every labeled subset (up to 8 labels); frozen exhausts deletion sizes 0,1,2 with distinct mask combinations respecting multiplicity. Assertions enabled. All higher frozen thresholds are theorem-based DP values, not independently exhaustively replayed at d>=3.
Raw stdout (SHA256 4435bfbedca5e92454973b9381451c39aff6f2243596b33f5bc99d17680ba846):
```
random_records=1000 exhaustive_states=58041 threshold_rows=21072 mismatches=0
frozen_records=14498 deletion_states=282914 threshold_rows=3609728 records_with_new_d2=14498 mismatches=0
min_deletion=0 rows=435542
min_deletion=1 rows=453829
min_deletion=2 rows=590673
min_deletion=3 rows=533080
min_deletion=4 rows=437234
min_deletion=5 rows=375858
min_deletion=6 rows=311441
min_deletion=7 rows=193389
min_deletion=8 rows=130930
min_deletion=9 rows=80660
min_deletion=10 rows=38290
min_deletion=11 rows=18180
min_deletion=12 rows=7461
min_deletion=13 rows=2308
min_deletion=14 rows=630
min_deletion=15 rows=182
min_deletion=16 rows=41
seconds=1.67732
```
R0=435542, R1=889371 exactly matches GBO; R2=1480044. Every frozen record has at least one new d2 row. No zero-capacity ports in frozen input; zero capacities tested in random cases. Counts are entries, not byte or timing comparison; 1.67732 seconds includes random/reference and frozen work in this C++ executable, excluding preprocessing/compile, no paired timing against previous Python.

## Physical continuation
Same archive solver SHA256 9fd83afbcdb37eeef76825fc1448fcdf00b09e090943def7edcba914e2007145 and fourth_input.py SHA256 3f0ab92970a8089457ae529cb771cfa63402db391e95c0c37a610c2150a6429f. Initial input generation failed due to missing gen.py in partial extraction; extracted original gen.py and regenerated input, then ran both configs successfully. Commands python fourth_input.py 2036 2038 600000 > roots.in; g++ -O3 -std=c++17 gak_solver.cpp -o solver; ./solver < roots.in; EM_WORD=1 ./solver < roots.in. Input SHA256 c1f090784d38c378e06554bc75ee1686efa4e8d6fe3f06f226475c1f9f93795f; base and word stdout SHA256 385b5175b2b8ac2bad1e91a06e7ccb4870c4774130ecf90048e6c7259f0ce65c and 9b0f8d47a5baa4ec83f6786fa2d5aea43723a66385e04688a8a93ea7b28227e0.
```
2036,1856,-1,169088,4212,140,0,0,0,0,0,0,0,0
2037,1867,-1,136828,2495,116,0,0,0,0,0,0,0,0
2036,1856,-1,119008,0,16,0,0,0,0,0,0,118740,103609
2037,1867,-1,96395,0,36,0,0,0,0,0,0,96100,81341
```
Both exclude both roots below 600000 cap. Historical aggregate plus two NO: 1988 YES,63 NO,342 other out of 2393; M14 remains [25,27]. Next root 2038.

## Actual control and continuation
GK entry blobs checked at immutable main e5d1f49796b0666fa87e92547e2a6e686c8df672. Read current P000, ACTIVE worldview, research entry/method, current portable and continuation rules. EM task r4-20261127-1634-ec49as-topic-read SUCCEEDED at dc9ca09450546ac1024ae1efbe66040266c57498 with NO_CANONICAL_PUBLICATION_DIRECTORY; native owner projection was not evaluated. Historical provenance EM-DIRECT-23537B; present private session binding unconfirmed. Independent portable continuation; no shared CLAIM, new identity, Result or Review; Activity association/canonical integration pending. Next: use constructive greedy witnesses or capped packing to make threshold updates query-adaptive; integrate with dynamic factor observer; verify higher horizons independently on selected frozen records; continue root 2038.
