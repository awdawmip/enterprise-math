# R5 — Twenty additional nine-state f=8 endpoint classes

**Status:** AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
**Evidence scope:** frozen integer-center *scalar observer* only; portable research, not formal Task CLAIM/RUN, native X6 equivalence, independent Review or mathematical admission.

## Frozen model and direct predecessor

- Frozen scientific input: enterprise-math commit `435e77af0d180eac32bd1f9c4c464bc4010b7551`.
- Original exact centers: `EXACT_R5_ALL_101_BUDGETS.json`, SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`.
- Prior exact certificate: `047036218649faaef1f72ad0d81d509268aab405:research_notes/portable_direct/r5_nine_pair_endpoint_quotient_20261118/RESEARCH.md`. It exhaustively partitions 30,876 unordered pairs into 2,026 complete observation-signature classes at U-1 and proves C8=8335 for 26 classes covering 5,383 pairs. Its prior 26 completed classes were not rerun in this continuation.
- Fixed named context H=(18,24,82,34,17,144,208). For x<y outside H, the nine named Bellman slots are (18,24,82,34,17,x,144,208,y).
- Physical query budgets k=214,...,314, each of cost k; at most f=8 unmarked arbitrary errors; correct real response satisfies |z-N_h(k)|≤tau/2.
- Entire fifth interval: L=25845652773852463277015040000 ≤ tau < U=58182461585441404127941754880.

## Incremental theorem

For the **20 previously unsolved U-1 signature classes** recorded in `RESULTS_R5_NINE_NEW20.json`, each representative's exact nine-counter Bellman value is 8335 at U-1. Their disjoint existing signature classes contain a total of **3,560 unordered pairs**. For every such pair and every real L≤tau<U,

\[
\boxed{C_8(H\cup\{x,y\};\tau)=8335.}
\]

Consequently the earlier 26 plus these 20 disjoint classes establish the equality for **46 of 2,026** right-endpoint classes, covering **8,943 of 30,876** unordered pairs (28.96%). The remaining 1,980 classes (21,933 pairs) have not been solved by this certificate.

## Exact argument and validation

1. The predecessor's exact signature quotient is computed on all 101 original queries with nine distinct *named* response-support bits; identical signatures at U-1 induce identical Bellman games for any f. To avoid a spurious extension of the older eight-state quotient, the full nine-slot signature is always recomputed. The previously established 2,026-class partition is reused, not reconstructed from an assumed product of 53 single-state classes.
2. An independent local reconstruction of the pair quotient from the same pinned table and endpoint returned `PAIRS=30876 GROUPS=2026 REDUNDANT=28850 MAX_GROUP=308`. The twenty representative keys, class IDs and class sizes are recorded per row and do not intersect the predecessor's 26 representatives.
3. For each representative, generate all inclusion-maximal correct response supports as closed center windows, retain the minimum physical k for *identical* support families, then solve the finite minimax recurrence:
   `V(e)=0` if at most one named slot is live; else `V(e)=min_k [k+max_S V(T_S(e))]`, where `T_S(e)_i=min(9,e_i+1[i not in S])`.
   The nine independent 4-bit counters each start at 0; the correct-response adversary is represented by maximal supports. Actions with a positive-cost self-loop cannot occur in a finite worst-case optimal strategy. Child exploration is reordered by residual budget for speed, without changing admissible actions or pruning correctness. All 20 C++ runs terminated with exit code 0 and exactly 8335; detailed memo sizes, physical action-family counts and exact input SHA-256 are in `RESULTS_R5_NINE_NEW20.json`.
4. A separate integer doubled-endpoint sweep independently matches the closed-window support families for every representative and all 101 budgets: **2,020 crosschecks passed**, plus regenerated Bellman input SHA-256 and action-family counts. Original command output: `PASS_R5_NINE_NEW20_END_POINT_RECHECK new_classes=20 new_pairs=3560 total_46_classes=8943 supports_checked=2020`.
5. Every nine-state family contains an eight-state subset H∪{x} whose exact f=8 cost is 8335 throughout [L,U), by the prior all-249 theorem. Thus C8(nine;tau)≥8335. Increasing tau can only enlarge the adversary's correct-response options. The original centers are integers, so every real tau<U is no harder than U-1. Since the nine-state U-1 exact cost equals 8335, the matching upper bound holds for all tau in [L,U).

## Reproduce

1. Obtain the immutable frozen table at the input pin; check its exact SHA-256 above. Use the predecessor's `build_pair_binary.py` and `pair_quotient.cpp` if independently regenerating the complete partition.
2. Place this directory's `RESULTS_R5_NINE_NEW20.json`, `EXACT_NINE_NEW20.cpp`, `VERIFY_R5_NINE_NEW20.py` and the pinned original table in the same directory. `python VERIFY_R5_NINE_NEW20.py` runs independent exact support checks and input-digest checks; `python VERIFY_R5_NINE_NEW20.py --solve` compiles and repeats the 20 minimax runs. Optional `--partition-tsv R5_NINE_PAIRS_U.tsv` checks exact representatives/class sizes using a freshly regenerated prior quotient.
3. Each result entry retains x, y, exact class ID/size, action family count, memo state count, input digest, exact value and original solver timing. Timing and memo counts describe this implementation, not a theorem invariant.

## Remaining problem

Search the **1,980 unsolved U-1 nine-state signature classes**, preferably using a proof-driven prioritization of classes with new joint pair interference, or construct a lower-cost full-256 adaptive policy. Any exact U-1 nine-state value greater than 8335 would improve the full-256 lower bound at that endpoint, but would not automatically establish the increase throughout [L,U). The full-256 f=8 bracket remains 8335≤C8*≤8343, and independent mathematical review is still NOT_REVIEWED.

Author-side provenance: R5 portable research; original prior identity `EM-DIRECT-4C3E47` is retained as historical attribution. No formal CLAIM/RUN or independent review is implied by GitHub branch preservation.
