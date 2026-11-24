# R5: sharp complete fixed-query mixed-fault and absolute-noise phase diagram

2026-11-17. Frozen source pin: 435e77af0d180eac32bd1f9c4c464bc4010b7551.
Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. Scope: derived 954-event scalar integer observer, 256 effective masks, budgets k=214,...,314; this is not a native BRC/X6 theorem.

## Exact theorem

For mask b, define the exact positive count N_b(k) via the frozen subset-zeta source cohorts. A nonadaptive experiment chooses a finite multiset of budget integers and pays their sum. Each intact real reading has absolute noise at most eta; at most e sample positions are marked erasures and at most f other readings are arbitrary unmarked replacements. Both fault allowances are any nonnegative integers. Uniform identification of all 256 masks is required. Put tau=2*eta and r=e+2*f+1.

In each following half-open interval [lo,hi), the **exact minimum fixed-query total cost is r*C**. Repeating every budget in the displayed tuple r times attains it.

| stage | lo inclusive | hi exclusive | budget tuple | C |
|---|---:|---:|---|---:|
| 1 | 0 | 76289178155959966960189440 | (214,223,294) | 731 |
| 2 | 76289178155959966960189440 | 3133722521542003559403356160 | (214,223,295) | 732 |
| 3 | 3133722521542003559403356160 | 13883516118328421520506880000 | (214,223,296) | 733 |
| 4 | 13883516118328421520506880000 | 25845652773852463277015040000 | (215,223,296) | 734 |
| 5 | 25845652773852463277015040000 | 58182461585441404127941754880 | (216,223,296) | 735 |
| 6 | 58182461585441404127941754880 | 92195224223274674159616000000 | (216,223,297) | 736 |
| 7 | 92195224223274674159616000000 | 267753525139190986466918400000 | (217,223,297) | 737 |
| 8 | 267753525139190986466918400000 | 651779164849779092423599718400 | (217,224,297) | 738 |
| 9 | 651779164849779092423599718400 | 1744659037213380157479321600000 | (217,224,298) | 739 |
| 10 **new** | 1744659037213380157479321600000 | 1752576979999614335377735680000 | (215,218,224,298) | **955** |
| 11 **new** | 1752576979999614335377735680000 | 1882951873548292168718745600000 | (217,218,224,298) | **957** |

For tau >= 1882951873548292168718745600000, no finite fixed or adaptive sequence of the same scalar observations guarantees correct identification, already when e=f=0.

The nine earlier chambers and their exact integer dual certificates were established at immutable commit b369e8452f3a4f0e21167b30684629bb98f625c2 in research_notes/portable_direct/r5_fixed_mixed_fault_noise_first_chambers_20261117/NINE_CHAMBER_THEOREM.md. This increment proves the two previously open chambers and terminal impossibility.

## Proof

A sample at budget k strongly separates masks a and b exactly when |N_a(k)-N_b(k)|>tau: then the two permitted closed real observation intervals do not overlap. A fixed multiset is uniformly identifiable against e erasures and f unmarked adversarial errors **iff** every pair has at least r=e+2*f+1 strongly separating sample positions, including repeated budget positions. Sufficiency: a common record has at most e erased strong coordinates and at most f other corrupted coordinates for each candidate. Necessity: with at most e+2f strong coordinates, erase at most e, partition the remaining strong coordinates into two error sets of size at most f, and use intersecting intervals at all weak coordinates.

**Upper certificates.** Exact 256-choose-2 integer comparisons show:

- For Q10=(215,218,224,298), min over a<b of max over k in Q10 of |N_a(k)-N_b(k)| is 1752576979999614335377735680000.
- For Q11=(217,218,224,298), the same minimum is 1882951873548292168718745600000.

Each pair is strongly separated by at least one member of the tuple when tau is strictly below the respective threshold. Repeating each of the four budgets r times costs 955r or 957r.

**Sharp lower certificates.** Let I_ab(k;tau) be 1 when |N_a(k)-N_b(k)|>tau, otherwise 0. At the inclusive stage-10 lower endpoint, use nonnegative integer pair weights (a,b,weight):
(3,4,215), (4,10,218), (0,64,224), (16,32,298).
At the inclusive stage-11 lower endpoint use:
(11,14,217), (4,10,218), (0,64,224), (16,32,298).

At their respective lower endpoints, the inequality sum_pairs weight*I_ab(k;tau_lower) <= k holds for **each of the 101 budgets**. The weights sum to 955 and 957, respectively. Increasing tau can only remove strongly separating positions. If n_k is any feasible budget multiplicity, then every weighted pair must have sum_k n_k I_ab(k;tau)>=r. Hence

sum_k k*n_k >= sum_k n_k * sum_pairs weight*I_ab(k;tau_lower) >= r*sum_pairs weight.

The lower bound equals each constructive upper bound throughout its declared half-open interval. No floating-point LP result is needed.

**Terminal obstruction.** Across all 101 budgets, max_k |N_11(k)-N_14(k)| equals 1882951873548292168718745600000, attained at k=217. At or above this tau their allowed intact reading intervals overlap for every budget. Their observation transcripts can therefore be identical for any finite adaptive strategy, proving impossibility.

Stage-10 cost jumps exactly at tau=1752576979999614335377735680000, when the pair (11,14) loses its strong separation at k=218.

## Exact validation and preserved inputs

The executed verifier reconstructs 25,856 exact integer source-cohort counts with eight subset-zeta passes; compares them with the independently saved full table; checks 65,280 pair-vs-tuple maxima, 202 integer dual budget inequalities, and the global obstruction. Result: PASS_R5_HIGH_NOISE_ALL_EF_CERTIFICATES. The earlier nine-stage verifier was also rerun and returned PASS_R5_NINE_CHAMBER_ALL_EF_INTEGER_DUALS. The two new chambers each have 8 state pairs attaining its minimum separation.

Input SHA-256: compact cohorts a781cf89e534587009e207e51bbda2f411e4147746f7d6a0b72a1354e80f0d4d; independent full table 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b. The pinned bytes and code plus result JSON are in the local self-contained reproduction archive. The verifier here accepts precisely these immutable inputs, not mutable current HEAD.

Mathematical review is pending. GitHub publication is independent of a canonical Task/CLAIM, Source Activity association, Result and Review.

## Next scientific unit

Study the optimal adaptive worst-case budget with unmarked adversarial corruption, distinguishing real-time selection from fixed multicovers. Preserve source/branch/phase-faithful joint observations and the original K=214..291 optimizer max-new/min-old recourse question. P000 six-dimensional native geometry and BRC provenance are unchanged by this derived scalar theorem.
