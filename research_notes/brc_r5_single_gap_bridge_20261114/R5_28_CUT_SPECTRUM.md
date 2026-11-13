# Frozen R5: complete 28 individual gap closures, all feasible budgets

Date: 2026-11-14. This is an author-side exact finite enumeration under the scientific pin `435e77af0d180eac32bd1f9c4c464bc4010b7551` and the integer event-boundary sampling model at radius `R=2`. It extends `RESEARCH.md` in this research directory and the immutable full-budget reference from Draft PR #2335 at `48d57e95ff64cb3f69361dd85d26e9dda0d9445e`.

## Result

There are 954 event-boundary coordinates, 1,065 underlying activation events, and 28 separating gaps of length three (29 original blocks). For each zero-based gap index `c=0,...,27`, independently reduce that gap from 3 to 2 by shifting the entire suffix by -1; keep other gaps unchanged.

**Exact minimum center counts:** 5 perturbed instances have `K_min=212` (cut indices `5,6,8,9,16`), and the other 23 retain `K_min=213`.

The five newly feasible `K=212` cases have exact minimal total costs:

| Zero-based gap index | New `J(212)` | `J(213)` after closing |
|---|---:|---:|
| 5 | 1,077 | 1,070 |
| 6 | 1,077 | 1,070 |
| 8 | 1,075 | 1,069 |
| 9 | 1,075 | 1,069 |
| 16 | 1,076 | 1,070 |

For the previously feasible budgets `K=213,...,954`, the **only** numerical changes are at gap indices **8 and 9**, each at `K=213`, where the optimum decreases by one (`1,070 → 1,069`). Every other (cut, budget) combination retains the exact original `J(K)`.

## Verification, domain and completeness

`VERIFY_R5_28_CUT_SPECTRUM.py` regenerates the frozen 15-atom Gray-subset event pool using exact integers and rational fractions, reconstructs the full coordinates, splits at the 28 old gaps, and computes local optimal cost curves by a minimum-cost center-path DP. For each cut, it merges only the two adjacent blocks with the right block shifted one position, then obtains the global optimum by exact min-plus convolution of the 28 remaining components. This directly recomputes all 28 cases through `K=314`, or 2,856 budget comparisons over `K=213,...,314`, plus the newly feasible `K=212` checks. The generic theorem in `RESEARCH.md` certifies the other 17,920 (cut, budget) cells `K=315,...,954`, without further perturbation computation.

**Completeness of the local center-path DP.** In an integer event sequence at radius two, consecutive chosen centers can have no more than four unchosen observed event positions between them. Otherwise the middle observed position is more than two units from both centers. Therefore it is sufficient to consider forward center arcs `q ∈ {p+1,...,p+5}`. Each arc's cost is the sum of the distances of the intervening positions to the nearer endpoint, subject to maximum distance two. The first and last arc boundary terms cover all remaining positions. Shortest paths with exactly `k` center vertices return the minimum total cost. The `>2` gaps split the old instance into independent blocks; closing one gap only joins the adjacent pair. Min-plus convolution enumerates the full distribution of the global number of centers among independent blocks and is therefore exact.

`CROSSCHECK_LOCAL_DP.py` compares both the local DP and block-convolution outcomes against exhaustive enumeration of all center subsets for 847 distinct integer coordinate sequences with `x_0=0`, `2<=N<=7` and remaining coordinates drawn from `{1,...,10}`. All comparisons passed. The initial comparison exposed and repaired a local convolution-range indexing error before publication: option extents must use `max(front)-m`, not `len(front)-m`. The corrected code passed the crosscheck and reproduced the results stated above.

The scope is integer event-boundary sampling. No claim is made here about endpoint-specific signed ports, the native 28-coordinate prefix-query benchmark, or changing several gaps simultaneously. Consequences for minimum-edit optimal center sets (`rho_K`) remain a distinct next question.
