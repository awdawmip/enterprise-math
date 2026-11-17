# R5 — exact fixed-batch identification for all error counts (256 states)
Date: 2026-11-18. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

Frozen source commit: 435e77af0d180eac32bd1f9c4c464bc4010b7551.
Frozen 256×101 integer count input SHA256: 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b.
Exactly 256 named hypotheses h=0..255, allowed query budgets k=214..314, good real reading within eta of the integer center N_h(k), and at most f unlabeled arbitrary errors.
Fifth noise chamber: L=25845652773852463277015040000 <= tau=2eta < U=58182461585441404127941754880.

THEOREM. For every integer f>=0 and real tau in [L,U), the exact minimum total cost of an observation-independent *fully prepaid fixed query batch* is C_batch(f,tau)=735(2f+1).
An optimal batch repeats each of physical budgets 216,223,296 exactly 2f+1 times. In particular C_batch(8)=12495. The strategy class excludes observation-dependent early stopping.

PAIR LEMMA. For distinct a,b and fixed list of queries, let d(a,b) count positions with |N_a(k)-N_b(k)|>tau. Guaranteed decoding after <=f arbitrary corrupted readings is equivalent to d(a,b)>=2f+1 for every unordered pair. For sufficiency each separated reading is bad for at least one candidate, so a common transcript would need >2f combined errors. Conversely, with d<=2f, choose a common good reading for every overlapping interval; on separated positions choose readings good for a on one group and for b on a complementary group, with each group size <=f. Thus an identical transcript is permitted under both candidates.

LOWER CERTIFICATE. Five witness pairs have these *exact* separating-query sets at both tau=L and tau=U-1:
(16,32): 296..312, dual weight 296;
(0,64): 223..290, dual weight 223;
(0,1): 214..221, dual weight 213;
(1,2): {214} union 216..221, dual weight 1;
(2,8): 215..221, dual weight 2.
At each allowed k, the sum of weights of those witness pairs separated by k is <=k. For k=214,215,216..221,223..290,296..312 these weighted sums are 214,215,216,223,296 respectively; elsewhere zero. With q=2f+1, every witness pair needs at least q separating occurrences, so summing their five weighted requirements yields cost >=q*(296+223+213+1+2)=735q. This is a 101-budget exact integer dual inequality.

UPPER CERTIFICATE. At the hardest integer tau=U-1, the three budgets 216,223,296 separate every one of 32640 unordered pairs. Exactly 2448 pairs are separated by one, 12192 by two, and 18000 by three of these budgets. Repeating each q times gives d(a,b)>=q. Cost equals 735q. As all N_h(k) are integers, these separation relations hold at every real tau<U. The five witness-pair sets agree at L and U-1 and can only shrink as tau rises; the lower certificate therefore holds throughout the chamber. This proves the all-f theorem without enumerating f.

ADAPTIVITY CONSEQUENCE. Source-pinned previous R5 results: 735+950f<=C_adaptive(f,tau)<=735+951f for 0<=f<=30; the upper bound extends to all f>=0. Therefore for 0<=f<=30 the fully prepaid batch costs between 519f and 520f more than the adaptive optimum, and for all f>=0 the saving is at least 519f. For f=8, C_adaptive in [8335,8343] implies exact savings interval [4152,4160].

VERIFICATION. Run the accompanying Python standard-library checker with the unchanged frozen integer source file EXACT_R5_ALL_101_BUDGETS.json. It checks SHA256, 5 witness separation sets at both thresholds, the 101 per-query weighted inequalities, and all 32640 pairs for the upper witness. The actual local run printed PASS_R5_256_FIXED_BATCH_ALL_F_FIBER_CERTIFICATE. Results and scope are in RESULTS.json. The upstream 954-event source-to-count derivation was not rerun.

This is a claim only about the specified scalar indexed-center observer with all named h and all 101 allowed future budgets. Signed X6 branch/path/provenance and full native state are not collapsed or deemed redundant. It is an independent GitHub research publication, not an authenticated formal CLAIM, Result, Review or Foundation admission.

NEXT FRONTIER. Determine the exact complete-256 adaptive 8-error optimum still in [8335,8343], retaining hypothesis-specific error counters and the verified shared-bit low/high fiber construction. A separate intermediate question is the optimal fixed query order with observation-dependent early stopping.
