# R284FX — Exact q=11..14 noisy reset-free four-phase capacities

Date: 2026-11-23 (Asia/Shanghai).
Mode: informed portable TASK_RESEARCH; unshared scientific work.
Status: AUTHOR_EXACT_FINITE_COMPUTATION / FINITE_PROOF_CONDITIONAL_ON_PINNED_FLOW_LEMMAS / NOT_INDEPENDENTLY_REVIEWED.
Frozen scientific lineage: R284CO -> R284FM/R284FP/R284FT -> R284FV -> R284FW. The present calculation introduces no P000/ACTIVE-worldview change, no new shared Task, and no formal Result.

## Precise theorem

Within the exact four-fixed-binary-codeword, reset-free cyclic omission model of R284FV (at most q omitted bit attempts per publication, omission residuals persist for unbounded generations, at most u=1 read flip, stateless correct stable reads, and no third-phase successful read or successful new-to-old rollback during a non-atomic publication),

**n_min(q,1) = 4q + 10 for each q in {11,12,13,14}.**

Thus the newly established sharp capacities are respectively 54, 58, 62, 66 bits. Together with the already-published q=2..10 results, the exact **finite** established range is 2<=q<=14. The all-q conjecture remains open.

## Complete finite lower bound

The analytical R284FP theorem gives n>=4q+8 for q>=3, u=1. Consequently only widths 4q+8 and 4q+9 need excluding before invoking the R284FE upper-bound construction.

Normalize phase-0 bits to zero. Remove constant columns. Every remaining coordinate is exactly one of the seven nonzero patterns p in {1,...,7} of its phases (1,2,3); coordinate permutations give a complete unique nonnegative 7-histogram x with sum n. The finite domain has binomial(n+6,6) elements. The scan applies (i) all six codeword distance necessary conditions and (ii) the six exact 8-vertex residual-cut conditions from R284FM. For every survivor, the existing R284FT integral-flow prefix oracle checks all legal per-edge omission histories and the count-lattice monotone write-order paths on the first and second publication edges.

| q | n | all histograms | six distances pass | six stable cuts pass | first-edge survivors | first-two-edge survivors |
|---:|---:|---:|---:|---:|---:|---:|
| 11 | 52 | 40,475,358 | 750,841 | 7 | 1 | **0** |
| 11 | 53 | 45,057,474 | 1,143,793 | 66 | 10 | **0** |
| 12 | 56 | 61,474,519 | 1,144,185 | 7 | 1 | **0** |
| 12 | 57 | 67,945,521 | 1,695,590 | 66 | 10 | **0** |
| 13 | 60 | 90,858,768 | 1,696,040 | 7 | 1 | **0** |
| 13 | 61 | 99,795,696 | 2,453,336 | 66 | 10 | **0** |
| 14 | 64 | 131,115,985 | 2,453,848 | 7 | 1 | **0** |
| 14 | 65 | 143,218,999 | 3,474,409 | 66 | 10 | **0** |

Exactly 679,942,320 seven-pattern histograms were exhaustively enumerated, not sampled. All cut and flow capacities are integers; no floating-point tolerance, finite residual-history truncation or probabilistic estimate enters the claims.

The unique first-edge survivor at n=4q+8 is F0 and the ten at n=4q+9 are precisely F1--F10, with A=2q+5 and B=2q+3 as specified in R284FW. This checks the *candidate completeness* conjectured there at four more q-values. R284FW's existing uniform second-edge barrier independently explains the failure of these eleven families at every q>=2; in this run the exact prefix oracle independently returned zero on both candidate widths.

The upper bound n<=4q+10 follows from the previously proved R284FE two-block repeated Gray construction; therefore the finite sharp equalities follow conditional on the mathematical correctness of those pinned lemmas and the finite exact implementations.

## Reproduction, independent local run and evidence scope

Source implementation was read from the current GitHub repository:
- R284FV_stable_cut_scan.cpp, git blob 66f5cab9d6882f74fb63ae1500dd0b0ff0941a8b.
- R284FV_prefix_count_lattice.py, git blob 77ceb62e51e87737d53193b86e5e40799f8716d4.
- R284FW_ALL_Q_PARAMETRIC_FIRST_EDGE_SURVIVOR_SECOND_EDGE_OBSTRUCTION_20261123.md, git blob 18f9befb076f784d5aad4b11e0717109d0e850ee.

The author transcribed and executed the original R284FV C++ scanner with only the temporary output prefix changed (R284FV to R284FX), compiled by g++ -O3 -std=c++17. The author also executed the original standard-library Python integral-flow/checker logic with the same temporary output-name adaptation and a q-range extension, for all 8 (q,n) pairs above. Stable counts were 7/66, first-edge survivors 1/10, and first-two-edge survivors 0/0 for each q; original R284FW families matched the observed survivors.

The companion repository shell driver `R284FX_q11_q14_repro.sh` reproduces the scan using the unmodified original C++ file and an exact one-line q-interval edit to the original Python checker (which otherwise explicitly asserts q<=10). Its published contents were read back from the immutable source commit; the recorded run above was the equivalent local adaptation, not an assertion that a GitHub workflow or the shell driver itself ran remotely.

This computation is an exhaustive **finite** author-level check. Formal Result and independent mathematical review have not taken place. As in R284FV, a source implementation defect in the seven-pattern enumeration, flow oracle or upper-bound proof would affect the derived optimality claim.

## Next discriminating unit

Prove q-uniform completeness of F0--F10 after the stable-cut and first-edge filters at n=4q+8 and 4q+9. A useful specific route is symbolic parameter elimination of the finite six-cut disjunctions, followed by a proved first-edge count-lattice classification. Candidate counts remaining constant for q=5..14 supply a concrete test of this route; constancy in a finite interval alone is not a proof of eventual stability. Then combine the uniform classification with R284FW's already-proved uniform prefix obstruction and R284FE's upper bound.

Preserve the original frozen scientific inputs, all source attribution, and the source/Activity/CLAIM/Review distinction.
