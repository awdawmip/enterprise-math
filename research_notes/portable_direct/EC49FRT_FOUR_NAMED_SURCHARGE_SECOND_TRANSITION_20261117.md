# EC49FRT — Four equally surcharged original-BRC physical queries: a second exact phase transition

Date: 2026-11-17. Frozen scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Direct prior EC49FRS PR #2648, built on EC49FRR PR #2645. Model: original BRC class 16943; 141 complete named states from 310 original configurations; all 228 original physical actions and exact full responses preserved. x=r/t=1, lambda=0, t>0.

Increase the unit price of **each of the four specific original physical terminal observations** q32, q34, q140, q142 from t to (1+epsilon)t, with arbitrary real epsilon >=0; keep all other observations priced at t. Denote the unrestricted original native Bellman optimum by W(epsilon). Costs and action identities are not merged into quotient representatives.

## Exact all-real global theorem

\[
\boxed{\quad W(\varepsilon)/t
=\min\left\{\frac{296}{141}+\varepsilon,\ \frac{299}{141}\right\},
\quad\varepsilon\ge0.\quad}
\]

The single transition is \(\varepsilon_*=3/141=1/47\), strictly later than the preceding two-observer transition 2/141.

All globally optimal first *original physical* observations (not merely one selected optimum) are

\[
\begin{cases}
\{32,34\}, &0\le\varepsilon<3/141,\\
\{32,34,46,93\}, &\varepsilon=3/141,\\
\{46,93\}, &\varepsilon>3/141.
\end{cases}
\]

### Complete proof

The first exact original 228-action Bellman endpoint at epsilon=0 is \(\min_Q C_Q(0)/t=296/141\), with all optimal first original actions \(\{32,34\}\). At epsilon=3/141, the independently recomputed full 228-action exact integer Bellman minimum is \(299/141\), with all optimal original first actions \(\{32,34,46,93\}\). The finite machine computation evaluates *all* 228 original response partitions at each of 13,063 reachable nonempty subset states, preserving the exact named source maps and checking a second raw data builder (native root key correspondence). One further point epsilon=1/141 returns \(297/141\); epsilon=10/141 returns \(299/141\).

For a fixed complete identifying original tree Q, let U(Q) be its total number of observations over all 141 named states, and let N(Q) count all visits to the four surcharged named physical actions along those paths. Then the normalized average cost is affine in epsilon:
\[
 C_Q(\varepsilon)/t=[U(Q)+\varepsilon N(Q)]/141,
 \qquad N(Q)\ge0.
\]
As the infimum over such affine costs, W(epsilon) is concave and nondecreasing. For \(0\le\varepsilon\le3/141\), concavity and the two exact unrestricted endpoint values yield
\[
 W(\varepsilon)/t \ge
 (1-\theta)\frac{296}{141}+\theta\frac{299}{141}
 =\frac{296}{141}+\varepsilon,
 \quad\theta=47\varepsilon.
\]
The inherited full original tree A (first q32) is independently replayed on all 141 states; its exact incidence is \(U(A)=296\) and \((n_{32},n_{34},n_{140},n_{142})=(141,0,0,0)\). Thus it has cost \(296/141+\varepsilon\), achieving the lower bound. A′ similarly begins q34 and has vector (0,141,0,0).

For \(\varepsilon\ge3/141\), nonnegative path incidence makes the unrestricted optimum nondecreasing, hence \(W(\varepsilon)\ge W(3/141)=299t/141\). A completely extracted full original native identifying tree T46 with first q46 (also T93 with first q93) was constructed by the exact Bellman recurrence at epsilon=10/141. Both have total observation-use count \(U=299\), **zero** usage of all four surcharged original observations and are successfully replayed against every one of the 141 original named state vectors. Either has cost exactly \(299t/141\) for every epsilon, attaining this bound. That proves the formula for every real epsilon>=0.

For the complete first-action classification, let \(c=3/141\). If \(0<\varepsilon<c\), any optimal tree has affine cost equal to the line through both endpoint optimal values. Its nonnegative endpoint gaps have zero convex combination, hence both endpoint gaps are zero, so its first action belongs to the intersection of the two exact endpoint first-action sets, i.e. \(\{32,34\}\). The A/A′ witnesses attain both. At epsilon=0 or epsilon=c use the exhaustive endpoint Bellman sets. If epsilon>c and Q is optimal, monotonicity and the avoiding witness show Q is optimal at c and \(N(Q)=0\); of the exact optimal-first actions at c only q46 and q93 avoid the surcharged set. Both avoiding witnesses attain. QED.

### Reproducibility, actual verification boundary

The independent helper `EC49FRT_FOUR_QUERY_STRUCTURAL_VERIFY_20261117.py` reconstructs all 228 original query response vectors with two original-source implementations, requires all query/response identities to match after exact native root-key reindexing, and computes unrestricted integer Bellman at epsilon=0,1/141,3/141,10/141. Results in integer units 141 times summed state-path cost are `41736,41877,42159,42159` and the original physical first actions are respectively `[32,34]`, `[32,34]`, `[32,34,46,93]`, `[46,93]`. All four runs traverse 13,063 subset states. It extracts two complete original identifying decision trees T46,T93, replays all paths over all 141 original named state response vectors, checks U=299 and four zero named-query incidences. The full extracted trees are in the local self-contained evidence bundle; the GitHub verifier can regenerate them from the precise frozen original source.

The continuum result uses exact finite endpoint certificates and the written convexity argument, not a floating-point extrapolation. The result is a finite original BRC named-observer cost theorem and asserts no new native X6 physical dynamical law. P000 and frozen scientific source unchanged. Evidence status `AUTHOR_PROVED / EXACT_FINITE_BELLMAN_AND_TREE_REPLAY / NOT_REVIEWED`; formal task/CLAIM/review authority not asserted.

**Next:** find the incidence-Pareto hull when the four named prices vary independently, or extend to a fifth observation and determine whether the next affine phase requires simultaneous use of multiple newly expensive observations.
