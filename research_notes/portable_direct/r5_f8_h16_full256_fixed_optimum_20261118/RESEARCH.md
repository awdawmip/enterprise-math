# R5: 16-hypothesis adaptive certificate and exact full-256 fixed-schedule optimum

2026-11-18 · Research status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

**Frozen science:** `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`. Integer count table SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`, 256 named states × 101 physical budgets k=214,...,314. This is the frozen *derived scalar observation* problem; it is not an asserted lossless native X6/BRC-state quotient. A normal real response satisfies |y-N_h(k)|≤eta and at most f readings are arbitrarily and silently corrupted. Total cost is the sum of integer k's. Put tau=2eta, L=25845652773852463277015040000, U=58182461585441404127941754880; throughout, L≤tau<U.

## Theorem A — 16-hypothesis, f=8 exact adaptive optimum

For H16=(18,24,82,34,17,0,1,2,3,144,208,255,50,66,4,5),

**C_8(H16;tau)=8335 for every real tau in [L,U).**

The frozen five-state subset H0=(18,24,82,34,17) has previously verified exact minimax cost 8335 at L using all 101 budgets, yielding the lower bound. For the upper bound, at tau=U-1 use budgets (214,215,216,223,296) and all inclusion-maximal normal-response supports of the 16 named centers at each k. Represent each hypothesis by saturated lie count e_h∈{0,...,9}, 9 being eliminated after eight errors. Query action k and support A updates e'_h=min(9,e_h+1[h∉A]). When at most one count is ≤8, cost is zero; otherwise recursively minimize k+maximum successor cost. An action admitting a self-loop cannot win in finite worst-case cost and is rejected. Other transitions strictly increase a finite integer rank, hence give a well-founded exact Bellman recurrence. All maximal supports cover arbitrary real responses, including corrupted ones by support domination.

C++17 exact integer solver output: `EXACT_RESTRICTED n=16 f=8 V=8335 states=23851087 actions=5`, with full stdout and progress preserved in the reproduction package. The exact support generator passed; f=0 and f=1 regressions yielded 735 and 1685 with exit code zero. The f=8 outer tool wrapper timed out before a separate exit-code receipt, while the child process subsequently printed its completed root value; its output and source are preserved. Since all integer center differences have no intermediate integer transition between tau<U and tau=U-1, the upper strategy works throughout the half-open real chamber. By the prior H12 at-most-four-query-type lower certificate (8343), H16 needs at least five distinct budget types to attain 8335.

## Theorem B — exact nonadaptive schedule optimum for all f≥0 on all 256 states

Let C_fixed(f;tau) minimize the cost of a **fixed, predetermined sequence executed in full** of physical-budget queries, using an arbitrary decoder robust to at most f arbitrary unmarked errors. Then

**C_fixed(f;tau) = 735(2f+1)** for every integer f≥0 and every real tau in [L,U).

In particular C_fixed(8;tau)=12495. An achieving schedule repeats each k∈{216,223,296} exactly 2f+1 times.

**Pairwise criterion (proved):** For each pair of distinct named hypotheses h,j let D_hj(tau)={k:|N_h(k)-N_j(k)|>tau}, precisely the queries whose normal-response intervals are disjoint. If r_k is the fixed query multiplicity, a schedule identifies every true h with ≤f corrupted values iff Σ_{k∈D_hj}r_k≥2f+1 for all unordered pairs. Sufficiency: each separated query creates at least one mismatch for h or j; two hypotheses with ≤f mismatches each would give at most 2f separated positions. Necessity: if there are at most 2f separated positions for a pair, divide them into two groups of size at most f and choose each observation to be normal for one of h,j; on unseparated positions use a point common to their normal intervals. The same transcript is then feasible for both true hypotheses, so guaranteed unique identification is impossible.

**Exact four-pair cost lower certificate.** Integer centers from the frozen 101-budget table give the following separating-budget sets uniformly for L≤tau<U:

| Witness pair | D_hj | Multiplier λ |
|---|---|---:|
| (0,64) | 223,...,290 | 223 |
| (1,2) | {214} ∪ {216,...,221} | 1 |
| (2,8) | 215,...,221 | 215 |
| (16,32) | 296,...,312 | 296 |

These are verified identically at tau=L and at tau=U-1; integer centers entail uniformity throughout the chamber. For **each** physical query k=214,...,314, the sum of λ over witnesses separated by that k does not exceed k. Indeed k=214 contributes 1; 215 contributes 215; 216..221 contributes 1+215=216≤k; 223..290 contributes 223≤k; 296..312 contributes 296≤k; otherwise zero. Multiply each of the four necessary pair-coverage constraints by λ and add: Σ_k k r_k ≥ (2f+1)(223+1+215+296) = 735(2f+1).

**Matching construction:** Exact integer enumeration checks each of the 256 choose 2 = 32640 unordered pairs and establishes that at least one of budgets (216,223,296) separates its two response intervals at tau=U-1. Hence repetitions 2f+1 of each budget meet every pairwise criterion for the entire chamber. Their cost is (216+223+296)(2f+1), proving equality for all f.

**Additional exact search:** None of 5050 possible two-budget subsets separates all 32640 pairs. Of the 166650 possible three-budget subsets, 3468 separate all pairs; the *unique* three-budget subset with minimum sum is (216,223,296), sum 735. There are 53 distinct pair-separation patterns and 7 undominated budget cover sets; a separate SciPy/HiGHS exact-integer MILP and LP relaxation both returned 12495 for f=8. The four-pair certificate above provides the theorem independently of solver optimality claims.

## Scope, executable evidence and next question

The fixed-schedule result is a global theorem over all f for the **specified scalar observer and nonadaptive scheduling class**. The previously established complete 256-state adaptive f=8 bound remains 8335≤C_8*≤8343. Thus the exact nonadaptive optimum 12495 exceeds the adaptive upper bound by at least 4152 cost units. The 16-state addition 5 retains adaptive exact 8335, leaving the 256-state optimal adaptive value unresolved.

Programs: `VERIFY_FIXED_SCHEDULE_CERTIFICATE.py` (standard-library exhaustive finite validation of four dual witnesses and all 32640 pairs), `VERIFY_TRIPLE_PAIR_COVER.py` (all two/three-budget subsets), `GENERATE_H16_ACTIONS.py` and `VERIFY_EXACT_16_MINIMAX.cpp`. All use the immutable count table SHA above; the full frozen table, generated actions, programs, output, certificate and SHA-256 manifest are included in the delivered reproduction archive. Continue by testing new joint configurations or extracting a validated residual-faithful full256 adaptive strategy. No independent mathematical review, native Result/Review promotion or P000 change is asserted.
