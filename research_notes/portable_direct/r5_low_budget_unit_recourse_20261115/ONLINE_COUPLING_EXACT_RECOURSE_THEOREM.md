# R5 — exact full-background recourse for cuts 3 and 10 (K=214..221)

Date: 2026-11-15. Frozen scientific input: 435e77af0d180eac32bd1f9c4c464bc4010b7551. Evidence state: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

## Object and quantified statement

Work with the **derived 954-event one-dimensional integer, radius-two, event-index-center observer**. This is a typed observer, not a lossless native X6/three-dimensional slice or BRC identification. Original event labels and all 28 length-three closure variables remain intact. Define Opt_B(K) as the entire family of optimal indexed K-center sets in closure background B, and

R_i(K) = max over B subset I\{i}, max over S in Opt_(B union {i})(K), min over T in Opt_B(K) of |S\T|.

The maxima include every assignment to the other 27 closure variables; K is the number of centers.

**Theorem.** For every integer K from 214 through 221 inclusive,

R_3(K) = 3, and R_10(K) = 4.

The corresponding original gap start event indices are 46 and 123 (zero-based). No claim is made for other budgets or for cuts 8 and 9.

## A directed Hausdorff upper bound from an online rank-coupling game

Let L_old and L_new be finite languages of increasing, exactly K-long center-index sequences represented as paths in two layer-by-layer directed acyclic graphs. Restrict each graph to its globally optimal paths. For a new optimum S=(s_0,...,s_(K-1)) and an old optimum T=(t_0,...,t_(K-1)),

|S\T| <= sum over r=0..K-1 of 1[s_r != t_r].

Every equal-rank equality yields a common center; other common centers only improve the inequality.

Define a perfect-information sequential game. At each center rank, the new player chooses the next center along a globally optimal new path, and the old player, having seen that choice, chooses the next center along a globally optimal old path. The payoff is the number of unequal-rank centers; new maximizes, old minimizes. A strategy for old ensures a legal old optimum against every new optimum, so

R_i(K;B) <= U_i(K;B),

where U is the value of this **online** game and R_i(K;B) uses the fixed background B. The upper bound remains sound even when online play is strictly harder than choosing the old path after seeing the whole new path.

For globally optimal state sets A_r and H_r at rank r in the new and old path DAGs, let A_r(a), H_r(b) be their legal next-state sets. Define

V_(K-1)(a,b)=1[a != b],

V_r(a,b)=1[a != b] + max_(a' in A_r(a)) min_(b' in H_r(b)) V_(r+1)(a',b'),

U = max_(a in A_0) min_(b in H_0) V_0(a,b).

Finite backward induction proves this recurrence. Each optimal vertex and edge is certified by the exact integer forward/suffix shortest-path tables C and D and by equality with the global minimum cost J. The old player can never leave its old optimal path language.

## Exhaustive frozen-instance upper certificate

The previously established all-background optimizer-family support theorem, at 214<=K<=221, gives E(K)={3,8,9,10,27}. Thus the full 28-bit quantifier reduces **exactly** to 32 five-bit masks. Each of cuts 3 and 10 has 16 old/new mask pairs at each budget.

Running the supplied standard-library Python program on the frozen 15-term input reconstructs all 954 events and 28 cuts, computes shortest-path tables for all 32 five-bit masks, and applies the recurrence for each of 8 budgets and both cuts: **256 exact online-game checks**. Every background has the same upper value, not merely the same maximum:

| Budget K | U for every cut-3 background | U for every cut-10 background |
|---|---:|---:|
| 214 | 3 | 4 |
| 215 | 3 | 4 |
| 216 | 3 | 4 |
| 217 | 3 | 4 |
| 218 | 3 | 4 |
| 219 | 3 | 4 |
| 220 | 3 | 4 |
| 221 | 3 | 4 |

This is a finite exact upper certificate using unbounded integer arithmetic. Its scope derives from the optimizer-family support theorem and from the proof of the online upper bound.

## Lower certificates and corrected K=221 witness

Taking the completely open old background B=empty is allowed by the full quantifier. Exact complete center-set witnesses at K=214 and K=215..219 were saved in the preceding R5 research notes and complete JSON artifacts. Their nearest distance to **every** old optimum, computed with exact old-optimum maximum-overlap DP, is 3 for cut 3 and 4 for cut 10. The previous K=220/221 forced-edge certificate gives cut-3 distance 3 at both K, and cut-10 distance 4 at K=220.

A **new** K=221 cut-10 witness, in K221_CUT10_FOUR_SWAP_WITNESS.json, strengthens the previous single-witness lower bound 3 to 4. It is a 221-element sorted unique center set, constructed with changed optimal edge (layer 32, 123->127), under singleton closure of cut 10. Full 954-event independent lexicographic (total old cost, negative center overlap) DP gives old optimum cost 1029, maximum old-center overlap 217, and minimum replacements 221-217=4. Direct full-event checks give maximum new coverage distance 2 and cost 1029; in old coordinates its maximum coverage distance is 3 and its total cost is 1030. This is a distinct witness, not an assertion that the earlier distance-3 witness was incorrect.

Combining lower and upper certificates establishes the displayed equalities for all eight budgets and every background. Review remains NOT_REVIEWED.

## Common-anchor compression (second theorem)

For all 32 effective masks and K=214..221, the complete optimal-path DAG at each rank has a **unique center** at these ranks:

event center 6 at rank 1; 11 at rank 2; 16 at rank 3; 536 at rank K-85; 541 at K-84; 546 at K-83 (ranks zero-based).

The verifier checks the unique center at each specified rank for all 32 masks and eight budgets (1,536 exact anchor certificates). All closures relevant to this band occur between events 16 and 536. Prefix/suffix edge costs, feasibility, and the conditional optimal-path languages outside these shared anchors are unchanged by the closure mask. Every optimum passes both endpoints 16 and 536 at the same ranks, so the path family factors at these anchors into a common prefix language, a mask-dependent core language, and a common suffix language. The old nearest optimum can match any new optimum's outside-center choices exactly.

Consequently the exact full-background, max-new/min-old **set recourse equals recourse restricted to the center-index core strictly between 16 and 536**, with precisely K-89 internal centers (125..132 for K214..221). This factorization preserves the required order of the two optimizations. It is additional exact mathematical compression for the remaining cut-8/9 problem.

## Reproduction and source files

Run VERIFY_R5_ALL_BACKGROUND_ONLINE_COUPLING.py in this directory beside VERIFY_R5_LOW_BUDGET_UNIT_RECOURSE.py, redirect standard output to a JSON file. Expected status: PASS_R5_ALL_BACKGROUND_ONLINE_COUPLING. The author-side execution of the original import-compatible source through an output-equivalent local base-module adapter produced 256 checks and 1,536 common-anchor checks. The complete 37,031-byte JSON output, SHA-256 703409bd9f5d1fd33706735c5c4855f2a6858d47d0e7e706b25020d9e97a0956, is preserved losslessly as EXACT_R5_ONLINE_COUPLING_20261115.json.zlib.b64, with decode and SHA check included below.

Python decode: import base64,zlib,hashlib,pathlib; raw=zlib.decompress(base64.b64decode(pathlib.Path('EXACT_R5_ONLINE_COUPLING_20261115.json.zlib.b64').read_text())); assert hashlib.sha256(raw).hexdigest()=='703409bd9f5d1fd33706735c5c4855f2a6858d47d0e7e706b25020d9e97a0956'.

The K221 witness was separately executed against all 954 event distances and against an independent lexicographic old-optimum DP: PASS_R5_K221_CUT10_FOUR_SWAP_DIRECT_LEX. Its full indexed-center data are included, not only a digest.

Existing lower-witness sources: K214_NONLOCAL_LOWER_BOUNDS.md, K215_219_FORCED_EDGE_LOWER_BOUNDS.md, K220_221_FORCED_EDGE_RECOURSE.md and their corresponding exact programs/artifacts in this directory. The five-bit support theorem: research_notes/portable_direct/r5_global_optimizer_tomography_20261114/RESEARCH.md at the parent PR #2427.

## Remaining objective

Compute exact R_8(K), R_9(K) for K214..221, preserving the global background maximum, new optimum maximum and old optimum minimum. The online rank-coupling bound is loose for cuts 8 and 9 at the low budgets because optimal center ranks drift over long segments; the proven common-anchor core is the appropriate starting reduction. Retain the original 28-cut evidence and the derived-observer/native-X6 distinction.

This author-side scientific note is an independent GitHub preservation, not a new formal CLAIM, Result, independent Review or authorized Source Activity checkpoint.
