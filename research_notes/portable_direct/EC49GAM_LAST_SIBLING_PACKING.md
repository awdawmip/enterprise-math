# EC49GAM — Last-sibling packing upper bound with common physical prefixes

2026-11-26. Informed portable continuation of GAL: 637df0b22938a0f629ce27b0ea6746ed87f0cc4d:research_notes/portable_direct/EC49GAL_PREFIX_HALL_HIERARCHY.md. Frozen BRC16943: fourth.json SHA256 228f907796e82fe17b7984123d636a81d6d6a1bc94e357629a6a98071b390923; ga_nodes.txt c69d3222a0378363f8e2e238cedc6a4839edfd867435155fef83d8268c3812f0. Parent GAL reproduction archive manifest verified locally. Fixed binary unit-cost physical observer on full joint states (u,h), positive iff r in u and j not in h. No change to P000 or native dynamical claim.

## Theorem: a last-sibling capacity relaxation

Let S be a finite set of distinct, jointly distinguishable states under a fixed family of binary queries Q, T subset S, k>=1. Use GAL's exact individual padded answer-weight support J_k(x;S). For a pair P={x,y}, define H_d(P;S) for d=k-1 as the set of j in 0..d for which a common path, with at most d-j positive and j negative answers, can reduce S to exactly P, and a query splits P. Such a path may be padded symbolically before the last query; this is an abstract word representation, not an additional physical observation.

To compute H_d, let A+={S minus q: q in Q, P subset q}, A-={S intersect q: q in Q, P disjoint q}. With GAL's inclusion-maximal union layers U_i, j belongs to H_d iff there are a in U_{d-j}(A+), b in U_j(A-) with a union b=S minus P and some q splits P. Necessity follows by collecting every exclusion along the common path; sufficiency follows by executing the selected queries, deleting constants, and padding the remaining budget symbolically with the prescribed bit counts. Exclusion commutes along a fixed answer path. All non-target rivals stay in S. This extends GAL's individual support to exact pair-isolation support, not to a simultaneously realizable tree.

Construct binom(d,j) abstract prefix slots of class j. Each slot can be empty, carry a singleton x with j or j+1 in J_k(x;S), or carry a pair P with j in H_d(P;S). Groups assigned to different slots must be disjoint. Let F be the family of unions obtainable from such assignments. Define B_k(S,T)=max{|U|: U subset T, U in F}.

Claim V_k(S,T)<=B_k(S,T)<=U_0(S,T,k), where V and U_0 are GAL's true weighted-indicator capacity and exact individual-word Hall relaxation. Proof: pad distinct identifying leaves of a decision tree to length k. Partition their words by their first d bits. Two targets occupying the same prefix must both be original depth-k leaves (otherwise a shorter identifying leaf would contain the other path); the physical path to their common predecessor has residual exactly that pair, since both final branches are identifying leaves. A single target has an eligible singleton class by J_k. Therefore the identified target set is a feasible assignment. In the other direction, each singleton slot can choose an allowed final bit; each pair slot can assign its two states opposite final bits via the separating query, after its common isolating path. Its two padded full-word weights both satisfy the corresponding J_k support. Slots have distinct prefix words; this gives an injective assignment in GAL's relaxed word matching, proving the second inequality. The family F is downward closed: when removing one member of a pair, the remaining singleton is eligible in that same class (the common path and split prove it), and removing a whole group just empties a slot. No claim is made that different abstract slots share a consistent physical prefix tree. Consequently min(B_k,U_l) is a sound stronger bound, and these two distinct relaxations need not be comparable for l>=1.

Exact DP: initialize F_0={empty}. For each slot whose eligible groups are G, take F_new=F_old union {U union g: U in F_old,g in G,U intersect g=empty}. This is exact by induction. Encode F as a bitset whose position is the n-bit state mask. Let A_g mark positions disjoint from g; F_new=F_old OR the OR over g of ((F_old AND A_g) << g). Mask addition equals bitwise union on disjoint supports. In particular for a single state i, A_{2^i}=(2^(2^n)-1)/(2^(2^i)+1), an integer alternating block pattern. Query target capacities from this downward-closed family by deleting one target at a time until an attainable mask is reached. No arithmetic rounding. The DP takes O(2^(k-1) n^2 ceil(2^n/w)) word operations after eligibility construction, with a straightforward group-mask cache of O(n^2 ceil(2^n/w)) words; the eligibility cost and target readouts are additional. This is a small-population structural tool, not a global complexity improvement.

## Executed verification

sibling_packing.py at 991618f66404bb598095118401976c55ed14c100, blob c24f9db211695048662568f7312b753823ff39ca; sibling_verify.py at c7f92d2c9768891bb53322fc68806c65addfd262, blob 5dc6d59879e32a3ddbab719c7dd084e76f25a420. Both blobs matched executed local sources. Run from GAL archive: python sibling_packing.py > sibling_packing.json; python sibling_verify.py > sibling_verify.json.

On all 180 frozen nodes and both original and +1 budgets (360 cases), true capacity <= packing <= GAL exact individual matching. No discrepancy. Independent direct common-path recursion verifies 24652 pair support masks (109422 weight-class membership decisions); independent explicit subset-set DP tests 6640 target capacities over 100 seeded generic distinguishable models. All pass. Raw packing JSON 91540 bytes, SHA256 f79f88d4e6c52e4e03f18b48d3a07486abb08b165a166555a1075b83015a1c78. Checker output {"packing_target_checks": 6640, "pair_checks": 24652, "pair_class_checks": 109422, "synthetic_models": 100}.

The new bound is strictly smaller than GAL U0 in 32/360, U1 in 32/360, U2 in 19/360. Packing alone is exact on 211/360; U2 is exact on 206/360; min(packing,U2) exact on 225/360. At original budgets exact cases increase from 27 (U2) to 46 (combined). Among 2706 previously saved inclusion-minimal obstacles, packing rejects 234 (182 rank2,39 rank5,13 rank6), including nine rank5 records missed by U2. Combined rejection count 302 versus 293 for U2. All 2706 are known exact obstructions, so these are detection counts, not false-negative claims for the exact tree. At node 39, T=mask13448={3,7,10,12,13}, k=4, GAL U2=5 and packing=4, exact=4. Further such strict records: (46,13448),(72,13448),(75,17224),(84,17224),(97,17224),(98,13448),(147,17224),(159,13448). Node125 still has packing=16 at k=4 versus U2=14 and V=13, and none of its six rank11 obstacles is detected by this relaxation. It admits every subset under packing. The next structural restriction should couple prefix slots through actual shared earlier queries (rather than marginally eligible groups); retain full pair and group compatibility.

Complete new numeric readouts stored at 143d3c4fccda84b68ba5034c02f79baef628c935:research_artifacts/portable_direct/EC49GAM/packing_readouts.zlib.b64. Decode base64 then zlib; resulting 4866 bytes SHA256 e0c17ccfe067a2e046b652887b3dd6e98fed688ff9ab7e7a0006e72cfc00dee4. First 360 records in GAL node order, original/+1 budget, each big-endian struct >BBI: bound, number of eligible pairs, number of attainable subsets. Remaining 2706 bytes are packing capacities in GAL original obstacle order. Full pair labels in raw output are reproducible from frozen inputs; full local JSON retained in reproduction archive.

## Fourth-layer exact root progress (unchanged GAK solver, NOT the new packing bound)

Fresh retry_gai.py 48 56 250000 from original 471 OPEN index order, following GAL's 32..48, no closed-root replay. g++ -O3 -std=c++17 gak_solver.cpp. EM_DENSE=1 EM_FAST=1 EM_WORD=1 versus EM_DENSE=1 EM_FAST=1 without word gate, baseline cap 1200000. All eight outcomes agree; 3 YES, 5 NO (exhaustive -1, not budget exhaustion); positive roots replayed all 5009 physical states in each configuration. Input SHA256 9ae4052320a81bb7992f724b3443772cff081308c0599ee271f1a5c652abf362; baseline input 914da4c847963c2f4d7a4cd3d06ef62c372b33f04242e211f3faf07ce0de39f4. Raw CSV (id,n,status,calls,envelopePrunes,satChecks,satPrunes,cumulative dense hits,misses,clears,entries,products,wordChecks,wordPrunes):
```
1930,1669,1,4831,0,0,0,51,29,0,29,30,4725,3839
1931,1670,-1,13966,0,0,0,141,69,0,69,79,13762,11497
1932,1670,-1,13966,0,0,0,199,69,0,69,79,13762,11497
1933,1670,1,242527,0,0,0,2361,537,0,537,1490,241717,218289
1934,1670,1,160079,0,0,0,3834,771,0,771,2308,159298,137459
1935,1670,-1,192034,0,0,0,5035,901,0,901,2682,191154,164447
1936,1671,-1,15229,0,0,0,5161,923,0,923,2704,15002,12432
1937,1671,-1,25312,0,0,0,5274,932,0,932,2713,25072,22099
```
Baseline:
```
1930,1669,1,14036,195,0,0,1030,260,0,260,989,0,0
1931,1670,-1,19817,419,0,0,2177,478,0,478,1966,0,0
1932,1670,-1,19817,419,0,0,2482,478,0,478,1966,0,0
1933,1670,1,348945,4074,0,0,12439,2311,0,2311,10705,0,0
1934,1670,1,237165,5541,0,0,16049,2769,0,2769,12838,0,0
1935,1670,-1,270017,5055,0,0,19867,3163,0,3163,14884,0,0
1936,1671,-1,22036,616,0,0,20732,3262,0,3262,15368,0,0
1937,1671,-1,35455,1236,0,0,21370,3304,0,3304,15555,0,0
```
Calls 667944 vs 967288; actual local sequential single-run wall 5.67s vs 16.05s. Different caps but neither hit its cap; timings apply to these runs only. Both use same inherited search kernel; independent proof review remains pending. Ordered histories add 10 YES, 7 NO. Frontier now 1936 YES /37 NO /420 OPEN of 2393, and ordered histories 3925/63/707 of 4695. 25<=M14<=27 unchanged.

## Control and next

Global canonical main 288dc9e62fd8c54ad6c0a3358bbd9d407abe0c80, required normative blobs re-read/verified unchanged, source P000 V5 and ACTIVE worldview retained. Topic query r4-20261126-1130-ec49as-read SUCCEEDED, immutable Source 21650707bc936a8c4b456c32eaf9026f2bfcb33a at 2026-11-26T03:27:06.800337Z, NO_CANONICAL_PUBLICATION_DIRECTORY; no native owner projection. Authenticated service identity-only read supplies no research authority. Historical EM-DIRECT-23537B only, current private identity and Activity unconfirmed; no shared CLAIM or substitute identity. Next use true common-prefix consistency of groups and exploit cheap first-query conditioned GAK intervals in C++ where worth their cost; continue untouched roots at original OPEN indexes 56 onward and return to 1905 and other earlier unresolved cases. AUTHOR_PROVED / EXACT_FINITE_SIBLING_PACKING_CHECK / PARTIAL_EXACT_ROOT_REPLAY / NOT_REVIEWED.
