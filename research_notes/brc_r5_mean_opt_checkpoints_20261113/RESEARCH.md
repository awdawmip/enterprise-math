# R5 — Exact mean-optimal event checkpoints under a fixed minimax radius

Date: 2026-11-13 (Asia/Shanghai). Scope: author-side exact finite optimization on the unchanged R5 frozen 28-coordinate/15-operation certificate auxiliary model, scientific pin `435e77af0d180eac32bd1f9c4c464bc4010b7551`. Continues the signed correction of Draft PR #2210; this is not a formal task Result, independent review, or native BRC/physical-time admission.

## Theorem 1: minimum expected signed event corrections

Consider the full-wall boundary sequence `0<=b<=W`, with strictly increasing integer cumulative counts `x_b=E(b)` (the corpus has W=953 and M=1065). A checkpoint is permitted only at an integer wall boundary s and has event-count coordinate x_s and the exact bitmap of terminals with smaller wall rank. For a query at b, choose its nearest event-count checkpoint and use the already established exact signed correction formula of PR #2210. Its number of terminal membership corrections is precisely `min_s |x_b-x_s|`.

For uniform demand across the W+1 complete-wall query boundaries, define

`J(S)=sum_{b=0}^W min_{s in S}|x_b-x_s|`.

For a fixed number K of checkpoints, the global optimum of J is a discrete one-dimensional K-median problem. Its optimal Voronoi cells are contiguous intervals [i,j] of boundary indices. The minimizing permitted center for one interval is any median index `m=floor((i+j)/2)`; this minimizes `sum_{t=i}^j |x_t-x_m|` even when successive x gaps differ or several certificates share one rational wall. For `F_k(j)`, the optimum covering the first j boundaries by exactly k centers, with `F_0(0)=0`, the recurrence is

`F_k(j)=min_{k-1<=i<j} (F_{k-1}(i)+C(i,j-1))`,

where `C(i,j)=sum_{t=i}^j|x_t-x_floor((i+j)/2)|`. Induction over the last contiguous cell proves global optimality; all objective arithmetic is integer.

The median interval cost has the Monge inequality `C(a,c)+C(b,d)<=C(a,d)+C(b,c)` whenever `a<=b<=c<=d`. A direct exchange proof: let z be the optimum center for the union [a,d] and h be an optimum center within the intersection [b,c]. If z<=h, assign z to the left interval [a,c] and h to the right interval [b,d]; on the exclusive right tail, h is no farther than z. If z>h, assign h to the left and z to the right; on the exclusive left tail, h is no farther than z. The sum of these two feasible interval costs is at most the union-plus-intersection optimum. Since optimal interval costs are no larger, Monge follows. Thus the standard monotone-minimizer divide-and-conquer DP evaluation is exact; the original finite recurrence, not the speed-up, establishes the objective.

## Theorem 2: lexicographic refinement without losing the prior worst-case guarantee

The predecessor's exact minimax radius `R*(K)` is retained. Choose at most K centers satisfying `max_b min_s |x_b-x_s| <= R*(K)`, and among them minimize J(S). Every optimal ordered center set induces contiguous nearest-center regions. A region [i,j] can be assigned one center at an allowed complete-wall index s exactly when `x_j-R <= x_s <= x_i+R`. The interval has such a center iff this discrete range is nonempty. Within the allowed range, clamp its median index to the smallest and largest admissible indices; the result is the exact minimum sum of distances under this radius. Replacing C by this radius-constrained interval cost in the finite recurrence above gives the global secondary optimum. The no-extra-iteration minimum of J is therefore compatible with the same certified worst-case R. The query implementation and stored signed event order are unchanged.

This statement is about the declared complete-wall, uniform-demand observer and the number of signed membership corrections; it does not claim that fewer corrections necessarily reduce CPython wall-clock latency in every workload.

## Frozen 1,065-certificate results

The locally retained original rational input source reconstructed exactly 2,880 prefix nodes, 1,065 certificates and 953 distinct rational activation walls. There are 954 complete-wall query boundaries. In each row, the first checkpoint scheme is the predecessor's minimal-radius greedy cover; the second uses exactly K checkpoints while preserving that same radius and minimizing the uniform average number of corrected events. A third comparison drops the worst-case constraint to optimize only the mean.

| K mask budget | Certified minimax radius | Predecessor greedy total J | Same-radius exact minimum J | Improvement | Unconstrained exact K-median J (maximum radius) |
|---:|---:|---:|---:|---:|---:|
| 15 | 36 | 17,190 | **16,813** | **2.193%** | 16,809 (37) |
| 57 | 9 | 4,486 | **4,384** | **2.274%** | 4,349 (11) |
| 213 | 2 | 1,104 | **1,070** | **3.080%** | 1,069 (3) |

The `K=213, R=2` result is a strict Pareto improvement over the previously published greedy minimax centers: it retains the optimal worst-case bound of two event membership corrections, uses the identical number of bitmap checkpoints, and reduces the exact sum of correction counts over all 954 boundary queries from 1104 to 1070. The tighter optimum is obtained by optimizing **within** the optimal-radius feasible set, not by changing the frozen scientific inputs.

This computation retains the prior 2,520-byte serialized certificate seed; its new checkpoint positions and masks are generated after loading. The evidence is an exact operation-count improvement, not an end-to-end measured latency improvement.

## Actual execution, finite verification and provenance

Executed locally with CPython 3.13.5 and only standard-library integer/rational arithmetic: original exact R5 corpus rebuild `~1.49 s`, the unconstrained divide-and-conquer DP `~0.46 s`, and fixed-radius finite DP `~1.80 s` in the recorded run. The results were checked using 128 tiny exhaustive K-median comparisons (32 eight-boundary cases times four budgets), explicit reconstruction of every selected segment and its integer score, and **1,066,824** independently calculated prefix-activation comparisons for the three budgets and both optimized center variants, including 20 pinned rational parameter probes over all 2,880 prefixes for each variant. Original raw rational/Wavelet oracle was reused without changing the scientific pin. Measured times are machine-local and include Python implementation overhead.

The full executed local script and its JSON record are available as attached conversation artifacts for this run. The repository portable stacked-source verifier `VERIFY_R5_MEAN_OPT_FROM_PINNED.py` is separately provided for independent clean-checkout execution; publishing it does not assert that its own remote bytes have already been executed.

## Next actionable questions

Execute the repository's actual committed verifier from a clean stacked checkout; include a direct seed-only decode and full resident-heap/RSS breakdown. Compare the saved greedy/minimax, lexicographic, and mean-only checkpoint sets at *equal total bytes*, including event directory and wall lookup. Measure complete request-to-result latency and peak allocation on explicit wall-boundary query distributions and nonuniform realistic parameter traces. Verify current owner/claim before any formal Source Result or independent review.
