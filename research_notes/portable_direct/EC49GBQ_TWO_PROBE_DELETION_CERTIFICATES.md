# EC49GBQ — two-probe augmenting certificates for all deletion horizons
2026-11-27. AUTHOR_PROVED / EXACT_FINITE_FULL_FROZEN_ALL_HORIZON_CERTIFICATE_REPLAY / PARTIAL_EXACT_ROOT_REPLAY / NOT_REVIEWED.
Predecessor b9705b257361cbe1713dcacbc6998b3a74c8d1bb:research_notes/portable_direct/EC49GBP_EXACT_DELETION_THRESHOLD_PACKING.md. Same frozen BRC16943 labeled integer-mask matching observer. No new physical attribution. GBP proved the packing min-max value; this unit supplies an augmenting-path construction of actual labeled optimal deletions and disjoint dual blocks without enumerating port subsets in the construction.

## Theorem and constructive proof
Fix W, R=C\\W. If a port of R has capacity zero, strict suffix-minimality is impossible (GBP); if R is empty the threshold is zero. Otherwise project each label x not fully contained in W to its nonempty neighborhood E_x intersect R. Keep original label indices. Write I for accepted projected labels. Call I strictly feasible if f_I(V)<=c(V)-1 for every nonempty V subset R, where f_I counts neighborhoods contained in V. Initially I is strictly feasible. Maintain any complete capacitated matching of I, using distinct capacity slots in each port.
For each projected label x in a fixed order:
1. Augment the matching by x. This succeeds by the ordinary Hall inequalities, since f_I(V)<=c(V)-1 and insertion increases each count by at most one.
2. Attempt to augment once more with a temporary label x* having precisely the same neighborhood as x. This succeeds iff I+x is strictly feasible: Hall for I+x+x* is f_I(V)+2 1_{E_x subset V}<=c(V); for sets containing E_x this is exactly strict feasibility of I+x, and for other sets the old strict feasibility suffices. Thus this second augmentation is a complete test for the greedy rule of GBP.
3. On success, remove x* from its matched slot, retaining the rearranged matching of I+x. On failure, let V be the ports reached by the unsuccessful alternating search from x*. All slots of V were searched and occupied, and each occupying label has its entire neighborhood in V. Hence f_{I+x}(V)=c(V): the inequality in the other direction follows from the full matching of I+x. E_x is contained in V, so f_I(V)=c(V)-1. Delete x from its slot and record its original label as rejected, together with V as a tight witness. A failed augment does not alter assignments (DFS only mutates on the successful return path).
All recorded witnesses remain tight in the final I because accepted labels only increase counts and strict feasibility continues. Intersecting nonempty tight witnesses have tight union: c-f_I is submodular, and its value on every nonempty set is at least one, so equality holds on union and intersection. Merge intersecting recorded witnesses transitively into disjoint blocks V_j. Each rejected label is wholly contained in exactly one of these blocks; no rejected label is counted twice, because it has a nonempty projected neighborhood. Every block is tight for final I. Consequently
|D| = sum_j [f_Aproj(V_j)-c(V_j)+1] = sum_j [1+s(W)-s(W union V_j)].
D is a feasible deletion set and the disjoint blocks certify optimality by the GBP lower bound. Thus rho(W)=|D|, with primal and dual witnesses, without constructing any subset DP or using an exhaustive port-subset search in the witness algorithm. Greedy order can change the witnesses but not rho. Slots and projected labels are auxiliary observer objects, not native spatial axes or time.

## Cost and truncated horizon
Let L=c(R), m the number of projected labels, n the port count. The explicit-slot DFS implementation visits each slot at most once per augment; a recursive call scans up to L slots, so at most O((L+1)^2) work per augment, with at most 2m augments. Merging disjoint witness blocks by repeated scans costs at most O(n^2) mask operations per rejection, including the conservative cost of vector erasure; masks need their actual bit width. Construction is polynomial in m,n,L, pseudo-polynomial in binary encoded capacities; no strong-polynomial claim. Additional input projection, slot creation and output/verification cost must be counted. The reference test below deliberately uses exponential direct checks and packing DP; these are NOT part of the constructive algorithm.
If only rho<=d matters, stop on the (d+1)-st rejection. The current disjoint tight blocks certify a packing lower bound at least d+1 for the processed prefix; including more labels cannot lower those block weights. If no such rejection occurs, finish and return the exact witness. This early-stop theorem does not presume any particular empirical speedup; the full replay below did not benchmark a capped variant.
A polynomial primal check also follows from Hall: for each nonempty port i reserve one of its capacity slots and test full matching of retained I. If this succeeds for each i, then for any nonempty V choose i in V to obtain f_I(V)<=c(V)-1. Conversely strict feasibility implies every such reserved-slot matching exists. This replaces exponential primal verification if needed; the run below uses direct exhaustive inequalities.

## Executed evidence
Code 92561576ce025ddeb7ef4eff58a1c5cdd538d9ae:research_artifacts/portable_direct/EC49GBQ/witness.cpp; remote blob equals local executed Git blob bdbaf989100e23411d179d6e964bffe89073c667; SHA256 7ea70f2097e706c5c7e26a8a89a69e64c9860d77e99e9e696b46f05ac2db8e38. Compile g++ -O3 -std=c++17 witness.cpp -o witness (assertions MUST remain enabled; first augment is invoked in assert). Run ./witness < frozen.in. Reused GBJ archive witness_records.json SHA256 c75076272328a0d67c4a991cdb02045099e79ddccba71aea32d4824a97b495e7, same as GBP. Conversion: for r in json.load(open('witness_records.json')): c=r['caps'];a=list(r['opts'].values());print(len(c),len(a),*c,*a). frozen.in SHA256 95b400c2fdf75a965bd5059f6b3b987dfc4bac589d9504a1610abe482b4546b5. Max frozen ports 10, max labels 16, max total capacity 32, min port capacity 1. Random seed 20261127, n=1..6, m=0..9, c=0..3, arbitrary masks including empty. Each finite W compares rho to independent packing DP, checks all nonempty residual V inequalities for actual retained labels, and directly verifies disjoint blocks and equality of dual weight. Infinite thresholds checked by zero-capacity complement criterion. All witnesses generated and verified in memory, not individually persisted; deterministic replay regenerates them. Raw stdout SHA256 fe586c4c53e8340c84a69b7ac1e9198ac439acccde5172da8deb74f408c1ee6e:
```
random_records=1000 rows=21368 primal_constraints=53942 rejected=11456 dual_blocks=5536 mismatches=0
frozen_records=14498 rows=3609728 primal_constraints=91774090 rejected=12573012 dual_blocks=4545728 mismatches=0
0 435542
1 453829
2 590673
3 533080
4 437234
5 375858
6 311441
7 193389
8 130930
9 80660
10 38290
11 18180
12 7461
13 2308
14 630
15 182
16 41
seconds=10.3548
```
Entire histogram exactly matches GBP, now independently certified for all horizons by matching construction plus primal/dual certificate checks. Counts of rejected labels and blocks are across W, not unique underlying labels. Time includes exhaustive reference and verification; no isolated solver benchmark or speedup asserted.

## Physical continuation
Same fourth.json SHA256 228f907796e82fe17b7984123d636a81d6d6a1bc94e357629a6a98071b390923; same GAK solver SHA256 9fd83afbcdb37eeef76825fc1448fcdf00b09e090943def7edcba914e2007145 and fourth_input.py SHA256 3f0ab92970a8089457ae529cb771cfa63402db391e95c0c37a610c2150a6429f. python fourth_input.py 2038 2040 600000 > roots.in; g++ -O3 -std=c++17 gak_solver.cpp -o solver; ./solver < roots.in; EM_WORD=1 ./solver < roots.in. roots.in SHA256 b47d8abf66c7509b821e76a61e87f72e009be65fb3751376e9b8647351922799; stdout hashes base 08772fa0733e701105796e3c9260008bf956e7476774ef5c250aa285dc3f8691 and word 3a6b003dd4ed9c54286c31a1ece6c24d4226b0639cc8f0c4c5404da98cfe1f6d.
```
2038,1868,-1,227758,2911,186,0,0,0,0,0,0,0,0
2039,1868,-1,144526,1626,182,0,0,0,0,0,0,0,0
2038,1868,-1,145108,0,25,0,0,0,0,0,0,144822,131366
2039,1868,-1,94926,0,21,0,0,0,0,0,0,94657,84288
```
Both configurations exclude both roots below 600000 cap. Historical GBP aggregate plus two NO: 1988 YES,65 NO,340 other of 2393; M14 remains [25,27]. Next root 2040.

## Control and continuation
Verified GK main entry blobs at 0413f6e4daca7088309b445e09e69972bcce3284, EM behavioral rules at 0803f17a9ce72d75c0987b69896e10c6659191d8; P000 V4/V5, ACTIVE worldview, joint relation, residual and portable protocols read. Exact task receipt r4-20261127-1729-ec49as-topic-read SUCCEEDED at 0803f17a9ce72d75c0987b69896e10c6659191d8, NO_CANONICAL_PUBLICATION_DIRECTORY, observed 2026-11-27T09:29:44.030370Z; native owner projection not evaluated, execution_authorized=false. Historical EM-DIRECT-23537B is provenance only, current private binding unconfirmed. Independent portable work; no shared CLAIM, replacement identity, Result or Review. Activity association and canonical integration pending.
Next: implement and benchmark capped two-probe witness, compact capacity-level augment (avoid slot expansion), exploit reuse between different W or branch states and integrate into GBM/GBN; continue root 2040. The full port observer and label map remain retained for declared future operations. No native physical interpretation asserted.
