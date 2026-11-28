# EC49GCF — Grouped cached-basis repair and nested contraction witness chain

Status: AUTHOR_PROVED / EXACT_FINITE_SYNTHETIC_ALL_BUDGET_REPLAY / NOT_REVIEWED.
Predecessor: GCE 9802dc91512bcb74019fa30d8e721749ffee86af:research_notes/portable_direct/EC49GCE_SUPPORT_CLASS_BLOCK_TRANSITION.md (blob f84d6a537326408ea90100718f87b905c884bcc5); its executed generator/solver 74ed2cc838161931876877645a2ce548caa82765:research_artifacts/portable_direct/EC49GCE/grouped_cached_replay.js was read. Inherits GCC fixed-suffix quota representation and GCE two-endpoint rank formula. Scope: finite labeled auxiliary strict-Hall matroid, not a native physical calculation. BRC16943 historical scientific identifier retained; exact archive pin and bytes not recovered or changed; no frozen-data replay.

## 1. Batch deletion by tight-union repair

Let N=(M/S)|F, S independent, and let H be one entire class of identical nonempty support E. Let Q=F'_W for F'=F minus H. GCC gives an exact independence test |I intersect L_j| <= g_j for all old joint support coordinates, where L_j=F_{V_j} and g_j=r_N(L_j). H is either entirely in L_j or disjoint. Old cached basis B is a basis of Q if E is not contained in W, otherwise a basis of Q union H.

Set I=B minus H and k=|B intersect H|. If k=0, I is already a basis of Q. Otherwise, define D(I) as the union of all L_j with |I intersect L_j|=g_j. Then the complete one-step augmentation set is
    Y(I)=Q minus (I union D(I)).
For a single new label, an integer quota can fail only when that quota was tight before insertion and contains the label. Thus Y(I) is exactly the set of legal augmenting labels, not a heuristic candidate list. While Y nonempty, choose any y in Y and set I=I union {y}; stop after k successful additions or when Y empty. By matroid augmentation, the latter condition implies I is a basis of Q. The former also implies this because r_N(Q)<=r_N(Q union H)=|B| and |I|=|B|. The algorithm needs at most k scans of the full old quota list (and zero if k=0). It performs at most k successful insertions. Each scan produces all candidate labels simultaneously by set union; it need not test each Q label independently. Works for arbitrary cached basis, including a noncanonical basis inherited from an equal-profile merge.

## 2. Nested contraction bases for ALL cardinalities

Let A be the repaired Q basis, a=|A|. Define
    theta=min(|H|, min_{j:H subset L_j}(g_j-|A intersect L_j))),
    Rmax=min(|H|, min_{j:H subset L_j}g_j).
H nonempty has a joint-support coordinate, so the inner families are nonempty. Both follow from the exact old quotas: the first gives the largest number of H labels that can be appended to A without removing any A label; the second is r_N(H). By spanning and free permutation symmetry, theta=r_N(Q union H)-a and theta<=Rmax. These are exact integers.

Fix an arbitrary ordering of H and let R_t be its first t labels. For 0<=t<=theta, take I_t=A. For theta<t<=Rmax, suppose I_{t-1} has been constructed. Define
    C_t=I_{t-1} intersect intersection_{j:H subset L_j, |I_{t-1} intersect L_j|+t-1=g_j} L_j.
Choose any y in C_t, set I_t=I_{t-1} minus {y}. This is well-defined. Indeed by GCE the rank in N/R_{t-1} of Q is a-(t-1-theta)_+, and the rank at t drops by exactly one. Consequently I_{t-1} union R_{t-1} is independent but adding the next H label makes it dependent. Its unique fundamental circuit includes some label in I_{t-1}, since R_t itself is independent. Removing a label of I_{t-1} is legal exactly when it belongs to every previously tight constraint containing H; all other quotas only relax or remain unchanged. This is precisely C_t, so C_t is nonempty. The resulting I_t is independent after contraction and its size equals GCE's exact rank. Induction proves
    I_0 superset I_1 superset ... superset I_Rmax,
    |I_t|=a-(t-theta)_+,
    I_t is a basis of Q in N/R for every feasible R subset H with |R|=t.
The last assertion follows because H labels are freely permutable while Q is fixed; alternatively every quota count depends on H only through t. This includes rank-zero, empty Q, and theta=Rmax cases. The basis chain can be shared across all actual real/aux objective-prefix options of one cardinality without changing their original label witnesses.

## 3. Cost and scope

For u old quotas, u_H containing H, per coordinate deletion costs <=k*u quota visits, theta costs u_H, contraction costs (Rmax-theta)*u_H. Rmax is computed once per state using u_H visits. The additional bitset operations are population counts, union/intersection, candidate selection and copying a chain; their cost depends on label width. A chain may be stored as one starting basis plus its ordered removed labels instead of a full array, although this replay uses an array. Initialization, support closure, Pareto comparisons, witness recovery and storage still matter; no bound of polynomial total state count is claimed. Only fixed future label selections, the all-budget optimum and one attaining original witness per budget are preserved by the objective quotient; arbitrary future support insertions, all tied histories and reverse deletion are outside this observer scope. Raw labels and joint directions remain in the input.

## 4. Executed integration and controlled finite comparison

Reused the exact GCE xorshift generator, seed 20261128, 350 models (2..7 ports, 5..12 labels, capacities 1..4 plus one per singleton auxiliary, weights as predecessor). Compared groupedGreedy (same GCE block order and rank-pair greedy implementation) and groupedCached (new nested basis chain). In the verification pass every generated cached basis is independently checked for subset membership, direct strict-Hall independence after original prefix, and direct rank; every retained coordinate is recomputed; for each model and mode all original labeled subsets are enumerated and each integer budget and attaining original mask is checked. Counts below count reference subsets once per model, although the verification code runs the reference separately for each mode. No disagreement/exception.

350 models; 376960 distinct model/subset reference checks; 5096 model/budget levels; 10192 optimal witness checks; 31416 retained rank checks; 34179 generated chain witness/rank checks; 14711 theta checks; 5661 removed-H basis labels across coordinate visits; 117 repair additions; 454 contraction exchanges.

Metric | groupedGreedy | groupedCached
---|---:|---:
stages | 2146 | 2146
generated | 7160 | 7160
retained | 2986 | 2986
peak states | 12 | 12
new greedy rank calls | 17564 | 0
quota visits (excluding initial direct bases) | 979528 | 182333
dominance comparisons | 1777 | 1777
retained rank entries | 15708 | 15708
cumulative nominal extra basis bits | 0 | 96301

The quota visit count decreases 81.3856%; scan and greedy visits have different bit-operation costs. After the verification pass, five whole-model-batch runs of each solver use the same frozen synthetic inputs, alternate order, disable all direct validation/reference work in the timed region, retain operation counters and compare them to validation-pass counters. Included: per-model precomputation, initialization, stage construction, solving and objective history masks. Not included: generation of the input models, brute reference, per-transition direct validation. Date.now milliseconds, same JS tool isolate:
greedy [469,470,466,460,488], cached [332,350,322,322,309].
Medians 469 vs 322 ms (31.34% reduction, about 1.46x ratio). This is an observed same-environment finite comparison, not a general complexity or hardware-independent guarantee. No actual heap-byte measurement; basisBits is cumulative nominal width of retained masks, not peak memory. Timed solve still has essential invariant assertions and instrumentation.

Exact executed code (verified content): 4808561105e689440db7741a266393d10ec7a05e:research_artifacts/portable_direct/EC49GCF/grouped_basis_replay.js blob 7e747dccf0f585becc3ce3e3d84412bf9f223d95.
Exact output (verified content): 00c8dc11ebc738a505c0ff3e3176942ac82b00bf:research_artifacts/portable_direct/EC49GCF/replay_output.json blob a30fb75aa710f8ce6ccc0925d7908c3e12602052.

## 5. Continuation and provenance

Next: locate the precise BRC16943 frozen archive and recover its provenance before any native replay; measure actual support multiplicity and closure sizes, and compare the two solvers on an authorized auxiliary projection with explicit observer bridge. Implement compact deletion-order chain storage and peak heap measurement if useful; examine incremental quota counters for larger support classes. Historical fourth-layer next root 2046 and M14 interval [25,27] unchanged, not independently replayed.

Global canonical entry blobs fetched at main and matched immutable prior main 416d390e21ce849d5ec1551b6ea7db802fa7b34a (bootstrap 25ae05640c7920104820dba91a1df5e9fafca25e, manual 108cd58e0458070b5f1a8171d2f66c8c3d0aa613). Research entry, task/informed role entry, P000 V4/V5, ACTIVE worldview, Heartbeat companion, residual fidelity, joint relation and portable/current research method and evidence policies read. em_status authenticated transport but grants no research authority; original exact topic read r4-20261128-0832-ec49as-read SUCCEEDED, Source b12429091a908693fee5f82e9e6a57e59b824024, NO_CANONICAL_PUBLICATION_DIRECTORY. Native operational owner projection not evaluated; no active owner asserted absent. Historical EM-DIRECT-23537B provenance not adopted as current authenticated identity. Independent informed portable research, no shared CLAIM, replacement identity, publication of Task, formal Result or review. Activity association and canonical integration pending. No change to P000, frozen science, sharing or scheduling.
