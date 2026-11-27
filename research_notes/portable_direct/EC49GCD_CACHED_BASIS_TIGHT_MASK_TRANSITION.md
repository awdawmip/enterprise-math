# EC49GCD — Cached-basis tight-mask transitions for finite suffix rank coordinates

Status: AUTHOR_PROVED / EXACT_FINITE_SYNTHETIC_TRANSITION_REPLAY / NOT_REVIEWED.
Predecessor read: af221487dea117f2c4cab718e7c8f8b378a8cb8a:research_notes/portable_direct/EC49GCC_FINITE_SUFFIX_RANK_PROFILE.md (blob e51e035161cdf2885007f62cc5cc69b6f5baebec). This is a finite labeled strict-Hall auxiliary model, not a native physical computation. BRC16943 historical frozen identifier is retained; archive bytes not re-read, no new physical result and no change of pin.

## Theorem: one tight-constraint sweep suffices for both transitions

Use GCC's finite suffix F, support-union closure W(F), coordinate sets L_V=F_V and ranks g(V)=r_N(L_V), N=(M/S)|F, with S independent. GCC reconstructs independence of any B subset F by |B intersect L_V| <= g(V) for every nonempty V in W(F). Keep one cached basis B_W of L_W for each coordinate W; witnesses are auxiliary computation state, not a canonical key. The canonical rank profile still determines the entire suffix independence language. Labels and their multiplicities are distinct; raw history remains preserved.

Process x in F and put F'=F minus x. For each W in W(F'), let Q=F'_W and B=B_W (a basis of Q plus x if x belongs to L_W, otherwise of Q). Define the tight mask family T(B)={L_V: |B intersect L_V|=g(V)}. Compute simultaneously
    D_x(B)=union {L: L in T(B), x not in L},
    C_x(B)=B intersect intersection {L: L in T(B), x in L}.
The empty union is empty. An empty intersection of the second family gives C_x(B)=B; separately store whether the family was empty. Both objects are label bitsets, not port-coordinate projections. Only one pass over the old rank constraints is required for this B.

Skip x:
* If x is absent from B, B is still a basis of Q.
* If x is present in B, put R=B minus x. Choose any y in Q minus (B union D_x(B)), if nonempty, and use R union y. Otherwise use R.
The rank stays |B| in the first two successful cases and drops by one only when no replacement exists.

Proof: deleting x decreases each constraint count containing x by one. The insertion of y into R can violate only an originally tight constraint not containing x and containing y. Every other constraint has integral slack at least one after removal or never increases. Thus precisely the displayed candidates can replace x. If none exists, R is maximal in Q and is a basis by the matroid property. The existence of an exchange also exactly certifies that x is not a coloop of N restricted to L_W when x is in B. No coloop test by repeated full greedy is necessary.

Take x (only when x is not a loop of N, i.e. singleton {x} is feasible):
* If x belongs to B, return B minus x, a basis of Q in N/x.
* If x is absent from B and there is no tight mask containing x, return B unchanged. B union x is independent; this case implies x was outside L_W, since otherwise the original B was not maximal.
* Otherwise choose any y in C_x(B), and return B minus y.
Proof: the tight masks containing x are exactly the violated inequalities of B union x. Removing a member y of B repairs all violations precisely when y belongs to every such mask. Removing y cannot introduce a new violation. By the fundamental circuit theorem for matroids, a nonloop x dependent on an independent B has a unique circuit in B union x, of size at least two. There exists such y, and C_x(B) is exactly the fundamental circuit minus x. The repaired independent set has full rank of Q union x, since x was spanned by B and B had rank |B|. Subtracting x gives a basis in N/x. When B union x was independent, its full rank is |B|+1, hence B is a contracted basis. If x belongs to B, contraction directly gives rank |B|-1.

Thus every new coordinate rank and its actual basis witness in both children are obtained by a single tight-mask sweep plus set operations, or immediate reuse when the branch is already determined. Loop x forbids take globally. Empty suffix has no stored coordinates. This is an exact transition for every finite suffix, not an approximation.

## Complexity and witness semantics

Write u=|W(F)|, u'=|W(F')|, m=|F|. GCC's earlier generic greedy unknown-rank recomputation takes O(u' m u) coordinate tests in the worst case. This construction takes O(u' u) tightness tests, plus O(u' u) bitset unions/intersections and output operations (each on O(ceil(m/w_machine)) machine words, with popcount cost accounted for). Initial cached bases still require construction, and canonical rank-key comparison remains unchanged. Extra basis storage is up to u*m bits per state, excluding index/container overhead, in addition to rank values. For large m, this can outweigh the benefit; no global polynomial bound or wall-clock acceleration is asserted. A merge of equal canonical profiles may keep the basis cache belonging to either state: the two suffix matroids have exactly the same independent sets. If keeping a history/witness for the selected objective, retain that corresponding original witness; any basis of the common suffix matroid remains valid. Pareto elimination from GCB/GCC remains scoped to maximum value and one optimum witness, not all histories or arbitrary new labels.

## Executed replay

Exact integer JS replay, deterministic seed 20261128, 500 synthetic models; 2..7 ports, 5..12 labels, capacities 1..4 and nonempty support masks. Process labels in increasing bit order. Maintain one actual cached state along a deterministic pseudo-random legal skip/take path; verify BOTH children at every visited stage. Compare against direct original strict-Hall greedy basis rank and independently re-evaluate the returned witness against original cuts. For suffix size <=7, enumerate every suffix subset and compare its reconstructed independence with original cuts. The greedy baseline computes only the unknown branch's rank in GCC, with early exit on failed constraints. Neither full Pareto state exploration nor the frozen archive is replayed. Seed generator uses ordinary LCG and modular draws, not a statistical claim or independent validation. Counts are exact operation counts, not equal-cost machine operations.

Actual code 5bc80307e062f867f11c5a48ca213eed3b0bdee6:research_artifacts/portable_direct/EC49GCD/cached_basis_replay.js (blob 917e095c4e2ae18ed310a8d889fa100d7813c1c6).
Actual output 2c96a9910f745648e9313fa58a665684307117e2:research_artifacts/portable_direct/EC49GCD/cached_basis_replay.json (blob 7168ae21c883784b77f3f263badfe0e87cb35efb).
Both were fetched by exact commit and matched generated content.

500 models, 4,393 visited stages, 22,989 coordinate pairs, 22,989 skip / 21,307 take witness and rank checks, 107,224 suffix language checks, 12,703,705 original Hall cut checks, zero disagreements. Initial bases 5,428. Skip replacement 1,293 and skip coloop 5,810; take exchange 82, free insertion 14,122, already in basis 7,103. Baseline 22,377 fresh greedy calls and 966,457 independence-coordinate visits; cached algorithm 269,953 tight-mask visits (72.07% fewer visits; operations differ). Extra nominal basis bits counted across output-coordinate iterations 230,080 (not peak or actual allocation). No wall clock comparison; initialization, closure generation, bitset costs, DP dominance and witness reconstruction need measurement on same full DP.

## Continuation

Next: integrate cache into GCC all-budget Pareto DP, compare same 350 prior synthetic inputs and full wall clock / memory including initialization and witness handling, then read exact BRC16943 archive pin and measure real union closure before asserting frozen applicability. Consider grouping identical support classes only with a separate label-aware observer certificate. Fourth layer root 2046 and historical M14 interval [25,27] unchanged; no native root replay in this unit.

## Provenance and control

Global main 20c7aa5332d2b6d8c6a6c254972b9f632cb31b44 verified by matching both canonical entry blobs 25ae05640c7920104820dba91a1df5e9fafca25e and 108cd58e0458070b5f1a8171d2f66c8c3d0aa613; applicable research, worldview, P000 V4 projection (canonical blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc), Source V5, joint preservation, residual fidelity, portable and current method read. Native em_status authenticated transport but no research authority; exact task lookup r4-20261128-0630-ec49as-read SUCCEEDED at Source 024ba558f0bb509a5be04ad8cce5b8ae97f0aec9, NO_CANONICAL_PUBLICATION_DIRECTORY for RS-EC49AS, native owner projection not evaluated. Current own private identity not verified; historical EM-DIRECT-23537B provenance not adopted. Independent informed portable research without shared CLAIM, new identity, formal Result/Review, or promotion. Activity association remains pending. No external publication or changed sharing.
