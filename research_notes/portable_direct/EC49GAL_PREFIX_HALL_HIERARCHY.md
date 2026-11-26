# EC49GAL — Prefix-conditioned Hall hierarchy and individual answer-weight supports

2026-11-26. Informed portable continuation of GAK at 85ae5037e8d70fb0a455c17060e499bb1827c6df:research_notes/portable_direct/EC49GAK_ANSWER_WORD_HALL_GATE.md. Frozen BRC16943 fourth.json SHA256 228f907796e82fe17b7984123d636a81d6d6a1bc94e357629a6a98071b390923 and ga_nodes.txt c69d3222a0378363f8e2e238cedc6a4839edfd867435155fef83d8268c3812f0, parent GAK archive manifest checked. Fixed binary unit-cost physical observer on full joint states (u,h), query positive iff r in u and j not in h. No native dynamics claim. P000 unchanged.

## Exact individual weight supports

For residual competitor population S, state x in S, let P_x contain the sets of rivals excluded by a positive query at x, and N_x the sets excluded by a negative query at x. For any family A let U_i(A) be the inclusion-maximal unions of at most i of its members, U_0={empty}. Recurrence U_{i+1}=maximal(U_i union {a union b: a in U_i, b in A}) is exact: replacing a dominated partial union by a superset preserves coverage at every subsequent step. Empty query families and zero budgets are allowed.

The exact set J_k(x;S) of negative counts in padded length-k words of individually identifying paths is
  {j in 0..k : exists a in U_{k-j}(P_x), b in U_j(N_x) with a union b = S minus {x}}.
Necessity: an identifying path separates x from every competitor, its queries cover all rivals, with at most k-j positives and j negatives after padding. Sufficiency: execute the chosen queries along x's path, omit any that have become constant, stop when x is isolated and pad with arbitrary bits to reach the prescribed weight. Off-path branches may remain unresolved. This is a one-target path theorem, not simultaneous feasibility. GAK same-fiber intervals contain these exact supports. We retain all rivals, including non-targets.

For target T subset S, define c_k(A)=sum_{j in A} binom(k,j) for any subset A of the k+1 weight classes. The maximum relaxed matching capacity is
  U_0(S,T,k)=|T|-max_{A subset {0,...,k}} (#{x in T:J_k(x;S) subset A}-c_k(A)).
Proof: apply Hall deficiency identity to the bipartite graph of targets and all binary words with their allowed weights. Neighborhoods are unions of whole weight classes. For any class union A, all eligible targets have neighborhoods contained therein, and conversely the neighborhood of any target subfamily is such a union; maximizing gives equality. Empty supports are counted by A=empty. Padded leaves of an actual decision tree are distinct, hence V_k(S,T)<=U_0. No interval assumption is needed; the finite class-subset enumeration is exponential in k, so this is currently a low-budget tool.

## Prefix-conditioned hierarchy

For l>=0, recursively define U_{l+1}(S,T,k)=min(U_0(S,T,k), max over effective physical partitions (U_l(S0,T intersect S0,k-1)+U_l(S1,T intersect S1,k-1))). At |S|<=1 return |T|, empty T return 0, and k=0 with |S|>1 return 0; empty effective partition family gives zero. Then
  V_k(S,T)<=U_{l+1}<=U_l<=U_0, and U_k=V_k.
Proof: any actual nontrivial identifying tree starts with one effective query and both children use budget k-1; applying the inductive bounds to each child proves soundness. Monotonicity follows by induction on k/l since max, sum and min are monotone. At l=k the recursion reaches the exact boundary values; the min with an upper bound cannot change the exact value. Same proof applies to GAK interval matching as the base upper bound on reachable normalized fiber residuals. Distinct prefix observations are retained until the relaxed boundary. Equality of upper bounds at a particular depth is not a raw-state quotient.

## Executed evidence

gal_path_hall.py (commit 091b19a035002557398585b02286ac34dda119d0, local Git blob 837bdf19feeefe4c9fcba7e8cbe667f8ac8b8de5) checked 23,119 individual class-membership decisions against independent conditional single-target recursion; 360 full capacities against exact subset recurrence; 2,706 original minimal-obstacle target bounds against GAG full missed frontiers. No discrepancy. Complete output gal_path_hall.json SHA256 fb8c407997e9630d1488ec5ebf07f6375d8d3a078d9f1ef7db9eff72a91366ad, 58513 bytes. gal_interval_compare.py (commit c9453a0b72c243f47e597a1296c30d09d16ae864; blob 4fdfb56d0e39cc86508a5ba857c25c47322c228e) compares GAK intervals as base across the same cases; raw output SHA256 95d8582b5af650894da90c63679891c6171b2d9d4cb0682b3ca14fc5bd02f638, 9166 bytes.

For original budget all 180 nodes are NO; bare intervals and bare exact path supports each reject 179, prefix1 and prefix2 each reject all 180. At budget +1 179 YES and one NO (node28); only prefix1/prefix2 reject the NO. Across 360 full-capacity cases, conditioned fiber intervals and exact path supports give identical values at each tested l=0,1,2. At original budgets the prefix2 bound is exact at 27 nodes; remaining gaps: 132 of 1, 21 of 2. For all 2706 obstacle records: interval/path base detects 182; prefix1 detects 201; prefix2 exact path detects 293 (182 rank2,54 rank4,30 rank5,27 rank6); cheaper prefix2 intervals detects 281. Strict exact-path improvement on 12 target records only. All six rank11 obstacles still pass prefix2. Node125 at k=4: exact V=13, interval/path=16, U1=U2=14; an extra exploratory call gives U3=14, U4=13, with 4/52 obstacles rejected at U3 and all at U4. Node28 at k=5: exact=13, U0=15, U1=U2=14, exploratory U3=14,U4=13. Thus first physical query consistency suffices to exclude both previously surviving full-recovery cases; exact individual path cover is not required for these 360 full cases. Use cheap conditioned intervals first; high-order obstacles remain important.

## Fourth-layer root progress (existing GAK solver, not an implementation of new hierarchy)

Recompiled unchanged gak_solver.cpp, g++ -O3 -std=c++17. Input batches retry_gai.py 32 40 250000 and 40 48 250000, excluding the earlier GAI/GAJ/GAK selections; baseline same states with cap 1200000. EM_DENSE=1 EM_FAST=1 with EM_WORD=1 versus without. All 16 outcomes agree, 11 new YES and 5 new NO. YES physical replay completed on 18204 states per mode. NO is exhaustive return -1, no cap hit; two solver configurations share the inherited search kernel, not independent proof review. Raw rows below: id,n,status,calls,envelopePrunes,satChecks,satPrunes,cumulative dense hits,misses,clears,entries,products,wordChecks,wordPrunes. 1=YES,-1=NO,0=OPEN.

Word mode:
1906,1639,-1,20328,0,0,0,71,22,0,22,37,20143,17061
1909,1646,1,12973,0,0,0,1382,405,0,405,1166,12575,8323
1910,1647,1,113544,0,0,0,2229,567,0,567,1712,113098,98646
1911,1648,1,123268,0,0,0,4175,945,0,945,2998,122538,106125
1912,1649,-1,134315,0,0,0,5178,1071,0,1071,3419,133626,114660
1913,1653,-1,44284,0,0,0,5987,1188,0,1188,3864,43846,36040
1914,1653,-1,44284,0,0,0,6354,1188,0,1188,3864,43846,36040
1916,1654,1,17981,0,0,0,6381,1188,0,1188,3864,17815,14262
1918,1656,1,69492,0,0,0,1628,429,0,429,1345,68856,57096
1920,1657,1,22900,0,0,0,2170,507,0,507,1530,22553,17867
1921,1657,1,20152,0,0,0,2610,565,0,565,1732,19797,14663
1922,1657,1,114507,0,0,0,3766,745,0,745,2234,113778,96821
1924,1658,-1,107453,0,0,0,4650,834,0,834,2505,106729,90443
1925,1658,1,178842,0,0,0,6033,1103,0,1103,3347,178150,161574
1926,1661,1,14400,0,0,0,6398,1193,0,1193,3706,14211,11072
1927,1663,1,9840,0,0,0,7087,1334,0,1334,4105,9540,6492

Baseline without word gate:
1906,1639,-1,29940,304,0,0,389,103,0,103,315,0,0
1909,1646,1,29545,245,0,0,4123,941,0,941,3803,0,0
1910,1647,1,169214,3931,0,0,8058,1632,0,1632,7123,0,0
1911,1648,1,192667,8219,0,0,15117,2850,0,2850,12945,0,0
1912,1649,-1,202854,7424,0,0,17802,3158,0,3158,14232,0,0
1913,1653,-1,75658,1747,0,0,21096,3595,0,3595,16727,0,0
1914,1653,-1,75658,1747,0,0,22135,3595,0,3595,16727,0,0
1916,1654,1,30870,651,0,0,22308,3600,0,3600,16753,0,0
1918,1656,1,99928,1992,0,0,5447,1077,0,1077,4720,0,0
1920,1657,1,37211,419,0,0,7969,1499,0,1499,6662,0,0
1921,1657,1,32803,334,0,0,9613,1747,0,1747,7731,0,0
1922,1657,1,173686,5875,0,0,12844,2173,0,2173,9456,0,0
1924,1658,-1,166297,4800,0,0,15201,2418,0,2418,10442,0,0
1925,1658,1,290509,4128,0,0,24620,3903,0,3903,18637,0,0
1926,1661,1,23426,219,0,0,25318,3991,0,3991,19062,0,0
1927,1663,1,14013,172,0,0,27151,4314,0,4314,20518,0,0

Ordinary calls 1048563 vs 1644279; word checks 1041101, prunes 887185. Both modes finish all roots; no matched timing for first word batch, do not claim aggregate speedup. Second word batch 3.34s vs baseline 10.38s (single runs). Ordered histories add 21 YES and 10 NO. New frontier 1933 YES /32 NO /428 OPEN, of 2393, ordered histories 3915/56/724 of 4695. 25<=M14<=27 unchanged. 1905 remains open.

## Control and next
GK current main bc4aed4d46378b21ccf08f123c390bf9b75c428b, required prior-read blobs verified unchanged, P000 and ACTIVE worldview preserved. Source topic read r4-20261126-1033-ec49as-read SUCCEEDED, immutable Source 6e1f3da0f308681a1f8dc8ceb9d347b035d863f6 at 2026-11-26T02:33:57.918587Z, NO_CANONICAL_PUBLICATION_DIRECTORY, no native owner projection. Historical EM-DIRECT-23537B only; current private identity/Activity unconfirmed. No shared CLAIM or replacement identity. Next: cheap prefix1 gate selectively for difficult nodes (avoid unconditional full expansion); exploit last-depth sibling competition for high-rank targets, and continue untouched roots after 1927, preserving 1905 and other unresolved roots. AUTHOR_PROVED / EXACT_FINITE_PREFIX_BOUND_CHECK / PARTIAL_EXACT_ROOT_REPLAY / NOT_REVIEWED.
