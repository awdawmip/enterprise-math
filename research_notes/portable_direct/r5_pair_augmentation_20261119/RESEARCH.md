# R5: two-label augmentation reveals 36 exceptional joint interactions

Date 2026-11-19, Asia/Shanghai. Research status: AUTHOR_EXACT_FINITE_COMPUTATION / PARTIAL_INDEPENDENT_CROSSCHECK / NOT_REVIEWED. This is independent portable *scalar* research, not a formal CLAIM/RUN or native X6/Port theorem.

## Frozen science and the question

Read the exact scientific input `EXACT_R5_ALL_101_BUDGETS.json` (SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`) and `stages_18.json` from the prior R5 reproduction bundle; preserve science source `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`. The robust endpoint is `tau=58182461585441404127941754879`. There are 256 named hypotheses, query costs k=214..314 and correct-response intervals `2|y-N_h(k)|<=tau`. Up to f arbitrary response errors are unflagged.

Earlier work established, by finite recursion, `V_f(H)=732+946f` through at least f=11 for the six-label set `H=(0,16,32,48,1,64)`. Every one-label extension had `V_8(H+u)=8300`. The current question: what happens when *two* labels are jointly added? All `binom(250,2)=31,125` unordered pairs outside H were considered.

## Complete f=0..5 finite census

Every pair was evaluated using its **joint eight-bit** maximal-support family for all 101 actions. Exact price-aware family deduplication produced 1,571 distinct signatures. The exact Bellman costs for all 31,125 pairs were:

| Error budget f | Baseline cost: count | Exceptional cost: count |
|---|---|---|
| 0 | 732: 7,626 | 733: 23,499 |
| 1 | 1,678: 31,089 | 1,679: 6; 1,680: 30 |
| 2 | 2,624: 31,089 | 2,625: 6; 2,627: 30 |
| 3 | 3,570: 31,089 | 3,571: 6; 3,574: 30 |
| 4 | 4,516: 31,089 | 4,517: 6; 4,521: 30 |
| 5 | 5,462: 31,089 | 5,463: 6; 5,468: 30 |

The **six minor exceptional pairs** are `(2,8),(3,9),(6,12),(7,13),(17,81),(33,97)`. Their values for f=1..5 are `733+946f`. The first four have V0=732; the final two have V0=733.

The **thirty major exceptional pairs** are exactly `(u,80)` with 17<=u<=31 and `(u,96)` with 33<=u<=47. Their values for f=0..5 are `733+947f`.

## Further exact eight-error certificates for all 36 exceptional pairs

There are 13 distinct price-aware signatures among the above 36 pairs. All 13 were separately solved by exact packed-counter Bellman DP at f=6,7,8, with their full eight-label support families freshly constructed from frozen integer centers.

* Six minor pairs: `V_8=8301`, with `V_f=733+946f` for 1<=f<=8.
* Thirty major pairs: `V_8=8309`, with `V_f=733+947f` for 0<=f<=8.

The other 31,089 pairs have complete f=0..5 values; **their f=6..8 values have not been exhaustively certified here**. An unfinished exploratory higher-budget enumeration was excluded from these claims. An exact eight-hypothesis lower-bound witness therefore improves the six-label restricted bound 8300 by nine, although the previously stronger 17-label lower bound 8335 remains intact. For the full 256-label eight-error game, the existing bound stays `8335<=C_8*<=8343`.

## Proof of exact finite reduction

At each k, define maximal joint support masks of the eight closed observation intervals. Every nonempty common intersection is witnessed at the greatest left endpoint of the participating intervals. Using the doubled response coordinate, the candidate endpoints are `2*N_h(k)-tau`, and each mask includes labels j satisfying `|2*N_j(k)-(2*N_h(k)-tau)|<=tau`. Equivalently, at each integer center x=N_h(k), select labels with `x<=N_j(k)<=x+tau`. Remove supports properly contained in others. This is exact integer arithmetic and retains **all joint labels**, rather than inferring joint support from the two seven-label projections.

For a capped mismatch vector e with e_i in 0..f+1, define the live set by e_i<=f and
```
V(e)=0                                            if |live|<=1
V(e)=min_k { k + max_{S in F_k} V(e^S) }           otherwise
e^S_i=min(f+1, e_i + 1_{i not in S}).
```
The minimizing actions must progress in every possible worst-case branch: an action having some maximal support containing all live hypotheses would admit an unchanged worst-case state at positive cost, so it cannot be optimal. Every remaining transition strictly increases at least one live coordinate; the recursion is finite and acyclic. Identical maximal-support families have identical state transitions for all e, so only the lowest physical cost among them is needed. These reductions justify exact finite DP per signature.

## Validation and reproducibility

Full enumeration: 31,125 ordered-canonicalized unordered pairs, 101 original query costs for each pair, 1,571 distinct eight-label price-aware signatures; full DP of those signatures for every f=0,1,2,3,4,5. Independent Python code rederived support masks by doubled left endpoints and recomputed V0 for 436 selected pairs (all rare plus 400 deterministically sampled ordinary pairs), and V1/V2 for all 36 exceptional pairs; all agreed.

The predecessor exact packed solver `SOLVE_R5_SINGLE_AUGMENTATION.cpp` is at Git commit `d08d5d2c5e0028b9ba6cea8342208cc0841b034c`; the n<=9 local revision was used for all 13 exceptional f=6..8 signatures. The full locally reproducible bundle contains the source-pin files, `make_adj.py`, `pair_census.cpp`, `pair_budget_dp.cpp`, `evaluate_rare.py`, `verify_pair_independent.py`, `pair_signature_census.tsv`, `pair_signature_members.tsv`, `pair_budget_f0_f5.tsv`, `pair_rare_f0_f8.json`, plus digest manifest. These are research evidence, not independent mathematical review.

Next useful direction: build joint nine-or-more-label witnesses by augmenting the thirty major pairs and compare with the existing seventeen-label 8335 lower-bound certificate; independently finish f=8 for all remaining 1,558 signature classes. Recompute joint supports on any further addition. Preserve BRC/provenance types upon native transfer; this scalar theorem has not established a native Port quotient.

Historical contribution provenance `EM-DIRECT-4C3E47`; current formal execution identity and owner status remain unconfirmed because the native owner receipt returned `BACKEND_IDENTITY_CHECK_UNAVAILABLE`. Independent source publication and Activity association are separate.
