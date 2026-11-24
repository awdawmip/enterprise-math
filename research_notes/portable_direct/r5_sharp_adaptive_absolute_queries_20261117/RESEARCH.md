# R5 — Exact adaptive absolute-noise query complexity (2026-11-17)

Frozen science pin: 435e77af0d180eac32bd1f9c4c464bc4010b7551.
Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. This is the frozen derived radius-2 indexed-center integer count observer (954 events, 28 candidate cuts, eight effective closure bits), not a new native X6 dynamical quotient. Independent portable research; no Task CLAIM, Result or Review is asserted.

## Exact model and theorem

Let the effective cuts be U=(3,8,9,10,15,17,25,27), with masks b=0,...,255, integer budgets K=214,...,314, and exact positive integer count N_b(K). A query returns arbitrary real y with |y-N_b(K)|<=eta, where eta>=0 is fixed and errors can be adversarial independently at each call. A decoder must recover b for every admissible transcript. Queries may be adaptive, repeated and arbitrarily many.

Define

    D3 = 1744659037213380157479321600000
    D4 = 1882951873548292168718745600000

The exact smallest worst-case call count is

    q*(eta) = 3             when 0 <= eta < D3/2;
              4             when D3/2 <= eta < D4/2;
              impossible    when eta >= D4/2.

The boundary equalities are assigned to the higher class because the admissible noise intervals are closed. Fixed budgets (217,290,305) attain the first threshold, and (217,218,224,305) attain the second. Thus the best adaptive three-query absolute-error radius equals the best fixed three-query radius. This sharpens and completes the previous R5 four-query necessity bound, which only covered eta >= 1752576979999614335377735680000/2.

## Proof: three necessary private observation windows

Define E=214..221, M=223..291, L=293..314. Exact frozen count-coefficient reconstruction verifies, for every b=0,...,255:

* N_b(K)=N_(b xor 1)(K) for K not in E (private cut 3).
* N_b(K)=N_(b xor 64)(K) for K not in M (private cut 25).
* N_b(K)=N_(b xor 16)(K) for K not in L (private cut 15).

Each of the three cuts changes a count somewhere in its own window, and E,M,L are disjoint. On every successful transcript a protocol must query each window at least once: if it omits a window, flipping its private cut yields another state with the same full transcript. Hence a successful protocol of at most three calls uses exactly one budget from each of E,M,L, in any adaptive order.

Consider the early-only 16-state fiber F={0,...,15}. For all 93 budgets outside E, all 16 masks have the same count. The early readout alone must therefore resolve all 16 masks, irrespective of which middle/late readings preceded or follow it.

For K in E define g(K)=min_{b<c in F}|N_b(K)-N_c(K)|. The following is the complete exact-integer eight-budget certificate:

| K | Closest pair in F | g(K) |
|---:|:---:|---:|
| 214 | (2,8) | 13883516118328421520506880000 |
| 215 | (1,2) | 25845652773852463277015040000 |
| 216 | (11,14) | 92195224223274674159616000000 |
| 217 | (4,10) | 1744659037213380157479321600000 |
| 218 | (9,12) | 763097546646694311430717440000 |
| 219 | (9,12) | 53550705027838197293383680000 |
| 220 | (9,12) | 0 |
| 221 | (1,4) | 0 |

Therefore max_{K in E} g(K)=D3, attained uniquely at K=217. Let eta>=D3/2 and assume a three-query decoder guarantees recovery. Before its sole early query, the adversary may reply with observations identical for every state of F, because all previous budgets are outside E. Its choice of early K is consequently the same on this common prefix. Choose the closest pair b,c of F for that K. Since |N_b(K)-N_c(K)|<=D3<=2eta, their allowed error intervals at that early query overlap; use one identical response in the intersection. All remaining middle/late outputs are again exactly identical. Thus b,c can induce identical full transcripts, contradicting certainty. If any branch has two early queries, it necessarily omits M or L, already contradicted by the private-switch argument. This proves every adaptive three-call protocol fails at and above D3/2; fewer than three calls fail even at eta=0.

## Proof: attainability and absolute-error saturation

For fixed budget set Q let d(Q)=min_{b<c}max_{K in Q}|N_b(K)-N_c(K)|. Exact integer comparison of all C(256,2)=32640 mask pairs establishes

    d({217,290,305})     = D3;
    d({217,218,224,305}) = D4;
    min_{b<c} max_{K=214,...,314}|N_b(K)-N_c(K)| = D4.

For eta<d(Q)/2 the error boxes of different masks are disjoint on at least one queried coordinate, giving guaranteed recovery. In the opposite direction, masks 11 and 14 have gap <=D4 at *every* budget, with their unique maximum equal to D4 at K=217. For eta>=D4/2 the adversary can choose one value in the intersection of their two error intervals at each budget; induction produces identical full transcripts through any adaptive or repeated query sequence. Hence no finite-query scheme succeeds above this threshold.

## Evidence, method and scope

Executed standard-library exact integer verifier: VERIFY_R5_ADAPTIVE_ABSOLUTE_COMPLEXITY.py; result: PASS_R5_SHARP_ADAPTIVE_ABSOLUTE_THREE_FOUR_QUERY_COMPLEXITY. It reads the prior compact 101-budget cohort coefficient file, verifies SHA-256 a781cf89e534587009e207e51bbda2f411e4147746f7d6a0b72a1354e80f0d4d and the exact frozen science pin, reconstructs N_b(K) by subset Zeta transform, verifies fiber constancy, 8×120 exact closest-pair comparisons, 256-mask private-switch support, all 32640 pairs for the triple/quadruple/all budgets and the global obstruction pair.

The source coefficient generator is the earlier preserved research_notes/portable_direct/r5_all_budget_cohort_hierarchy_20261116/VERIFY_R5_BUDGET_INTERACTION_HIERARCHY.py. This is exact postprocessing of its pinned coefficients, not an independent rerun of the original 954-event DP. The 8-bit provenance is retained in the calculation. The fiber is observer-sufficient for the declared scalar readout outside E; no claim is made that arbitrary future operations descend through this quotient.

## Next scientific unit

Find a path-exchange/transfer explanation of the unique early-only separation optimum at 217 and the shift to masks (9,12) at 218. Explore joint provenance-preserving observers beyond the current finite scalar-query alphabet. Separately resume the indexed-center max-new/min-old optimizer-set replacement-distance problem using explicit center sets, not count-only information.
