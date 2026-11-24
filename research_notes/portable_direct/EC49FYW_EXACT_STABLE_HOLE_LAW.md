# EC49FYW — exact four-hole witness and closed stable excess law

2026-11-24. Frozen auxiliary Boolean observer BRC16943: the 50 distinct nonempty row supports F on ten rows from FYV, labeled state (U,H), |H|<=h<m, W(t,j)=1[t in U]1[j not in H], unit noiseless adaptive queries, exact recovery of both U and H. No new native X6 attribution. Parent sources actually reread: 1c89f8f765926749601fdcb739fe74b66aefa2c6:research_notes/portable_direct/EC49FYV_TIGHT_PHASE5_PREFIX_CLASSIFICATION.md (tight phase-5 classification and m<=8 exclusion); 10f0597c6c988fc0adcfbc8fda748367587745bb:research_notes/portable_direct/EC49FYU_UNIQUE_DEFICIENT_PREFIX.md (uniform shifted lower bound); 438163ba045e2d3ea8d27bbb81004694f5069ae0:research_notes/portable_direct/EC49FYT_EVENTUAL_PERIODIC_EXCESS.md (multicover transport with finite inventory threshold); 46fce67764a5b12324d116162c3331fb1e2623f1:research_notes/portable_direct/EC49FYR_GUIDED.cpp (reused search/replay code, identical local source Git blob 8899178876a3a265319a420217f696c0f1c0c0bb).

## Theorem

Q_4(9)=15; Q_4(m)=m+6 for every integer m>=9, and Q_4(m)>=m+7 for 5<=m<=8. Thus 9 is exactly the first column inventory attaining the stable four-hole excess c_4=6.

For all integers h>=4,
c_h=ceil((15h+6)/11), and more strongly
Q_h(m)=m+ceil((15h+6)/11) whenever m>=9+ceil(26(h-4)/11).
For h=4 this is the base witness; for h>4 apply the transport theorem. The stable formula also holds at h=2,3 by the earlier established constants 4,5 respectively; the already established c_1=3 is an exception to this formula. The previously eventual period law has exact offset delta=6, valid at least from h=2, and c_(h+11)=c_h+15 for every h>=2. The general finite inventory threshold stated above is sufficient, not necessarily sharp at h>4.

## Constructive finite base and proof

Reuse FYV: any four-hole strategy reaching budget m+6 has a nine-zero prefix with row multiplicities (2,1,1,0,1,0,1,1,1,1) on nine distinct physical columns; its terminal residual game is solvable at m-3 additional queries. Search the count-vector DAG backward: for each possible edge x -> x+e_t, first require a winning all-zero continuation, then independently solve the positive branch with the residual support set filtered to row t, one confirmed live column, and previous zeros represented by their distinct-column admissibility masks. All nodes preserve joint holes and physical labels through the original replay. A successful path has row order

0,0,1,2,4,8,7,6,9.

At most 14 abstract positive-branch solves were attempted before this path was found (144342 recursive calls, 45677 memo entries). The abstract terminal was accepted using FYV. In finite mode solve every positive branch and the terminal branch with physical inventory retained, then store the nine prescribed actions into the finite memo. For m=9 this took 229075 calls and 62593 entries. For m=13: 1036 calls and 522 entries. Search is a construction aid only; the upper bound is certified by replay across every labeled input, not by trusting a successful search Boolean or any pruning rule. Replay is inherited from FYR, rederives candidates and forced holes from raw negative and positive row masks, checks legal nonrepeated physical queries, and reconstructs both U and H; for saturated states it uses a separate exact finite split solver over physical probe masks. It asserts the recovered U and H equal the actual target and checks every budget. The program was compiled with assertions enabled, g++ -O3 -std=c++17, and run with arguments 9 and 13. All 50*sum_{k=0}^4 binomial(m,k) states are enumerated by the outer loops. Memo policy choices are fixed from the search; the raw replay branches only on observed bits and recomputed candidate state, not the true hidden state.

Actual output for m=9:
```
abstract DAG 1 calls 144342 states 45677 edges 14
0 0 1 2 4 8 7 6 9 
finite DAG 9 calls 229075 states 62593
replay 9 pass 12800 failfresh 0 failsat 0 failbudget 0 max 15 total 185191 reused 8
```
Actual output for m=13:
```
abstract DAG 1 calls 144342 states 45677 edges 14
0 0 1 2 4 8 7 6 9 
finite DAG 13 calls 1036 states 522
replay 13 pass 54650 failfresh 0 failsat 0 failbudget 0 max 19 total 1007089 reused 0
```
The C++17 program is EC49FYW_FOUR_HOLE_DAG.cpp at 8035b3917e9b6f7745064bd72dbe369c0ff3f736, Git blob 730a9fadb5ecb91e6cead0f8ccda27e1f820602d, exact remote byte identity with the executed local file. Example: g++ -O3 -std=c++17 EC49FYW_FOUR_HOLE_DAG.cpp -o fyw; ./fyw 9; ./fyw 13. The unused inherited oldmain function emits a harmless compiler warning; it is not called.

Analytic extension: on m>=9 columns, apply the nine-column algorithm to nine fixed labels (at most four holes and at least five live within them), thereby recovering U and their hole subset. On each of the remaining m-9 labels probe any row in U, or skip those probes if four holes already known. This recovers the labeled state in at most 15+(m-9)=m+6. FYU lower bound at h=4 is ceil((60+6)/11)=6, and FYV independently excludes the same excess for 5<=m<=8, so the first stable inventory is sharp.

## Closing the unbounded stable problem

For h=4+k, k>=1, FYT multicover transport theorem with base excess c=6>=5 gives
Q_(4+k)(m) <= m+6+ceil(15k/11) whenever m>=9+ceil(26k/11).
Algebra: 6+ceil(15(h-4)/11)=ceil((15h+6)/11). FYU gives the matching lower bound for every m>h. The k=0 base was just proved. Therefore c_h is known at all positive integers, with c_1 exception, and there is no remaining unknown stable offset or eventual phase. This settles all eleven residue classes, not just the four-hole case. In particular c_6=9,c_9=13,c_12=17,c_15=21. The next mathematically distinct question is the exact onset M_h=min{m>h:Q_h(m)=m+c_h} for growing h; for h=4 it is now 9. FYV gives M_(4+11a)>=23a+8 for a>=1, whereas the new transport gives M_(4+11a)<=26a+9. The gap in that phase is 3a+1, matching the static prefix pair merging capacity; whether the merges can be realized in a winning tree is open. Small inventories for other h also remain open.

## Control / evidence scope

AUTHOR_PROVED / EXACT_LABELED_INTEGER_REPLAY / PARENT_DEPENDENT / NOT_REVIEWED. No independent review or native X6 transfer asserted. Original researcher registration receipt r4-20261124-0240-ec49fyh-own-session-v1 reread SUCCEEDED, historical provenance EM-DIRECT-23537B / RA-2D7B4AD1AA5CD3F5D9EF1C76. Current exact topic lookup r4-20261124-1730-ec49as-read-v1 SUCCEEDED / NO_CANONICAL_PUBLICATION_DIRECTORY at Source 7ae7551f1c6a9de19e3c12fdfccb0486c97068c4, observed 2026-11-24T09:30:32.630170+00:00; absence is not a full native owner projection. No shared CLAIM, Result, Review, or foundation mutation. Current own private Activity writer binding remains unconfirmed; preserve historical contributions and independent portable science. Next: finite onset, especially whether shared (0,1) probes in FYV phase-5 prefixes can be realized by an adaptive strategy.
