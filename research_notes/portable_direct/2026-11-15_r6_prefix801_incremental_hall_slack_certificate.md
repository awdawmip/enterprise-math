# PREFIX-801 — Incremental Hall-slack certificates for finite provenance-count fibers

Date: 2026-11-15. Research line: R6 independent portable research. Predecessor: PREFIX-800 at commit 455ecc396f836c127e0f4920c659bce8327c9be8. Frozen scientific input pin: f42f2906d77f24085c123f3ccfe9667d41caa96d. Status: AUTHOR_PROVED / EXACT_INTEGER_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

## Mathematical domain

Let $G=(U,V,E)$ be a finite named bipartite source graph, with $|U|=b$, $|V|=c$, nonnegative integer capacities $K_{ij}$ and nonnegative integer row/column margins $(r_i),(s_j)$ satisfying $\sum_i r_i=\sum_j s_j$. A partial source assignment fixes edges $F\subseteq E$ to integers $t_{ij}\in[0,K_{ij}]$. For the remaining edges define the residual margins

$$
R_i=r_i-\sum_{j:(i,j)\in F} t_{ij},\qquad
S_j=s_j-\sum_{i:(i,j)\in F} t_{ij}.
$$

For each nonempty row subset $A\subseteq U$, define its residual demand, free capacity per column and Hall slack by

$$
D_A=\sum_{i\in A}R_i,\quad
C_{Aj}=\sum_{i\in A:(i,j)\notin F} K_{ij},\quad
\sigma_A=\sum_{j\in V}\min(S_j,C_{Aj})-D_A .
$$

PREFIX-800 proves the residual finite integer transportation problem is feasible exactly when all $R_i,S_j$ and all $\sigma_A$ are nonnegative. Feasibility follows from integer max-flow/min-cut, not from a numerical approximation.

## Theorem 801.1 — Exact incremental Hall slack

Let $e=(p,q)\notin F$ have capacity $k=K_{pq}$ and be assigned $x_e=t$ with $t\in\{0,\ldots,k\}$. For every row subset $A$, let $\delta_A=1$ if $p\in A$ and $0$ otherwise. Then the exact updated slack is

$$
\boxed{\sigma'_A=\sigma_A+
\min(S_q-t,C_{Aq}-\delta_A k)
-\min(S_q,C_{Aq})+\delta_A t .}
$$

The remaining state changes by

$$
R'_p=R_p-t,\qquad S'_q=S_q-t,\qquad
C'_{Aq}=C_{Aq}-\delta_A k,\qquad
D'_A=D_A-\delta_A t.
$$

All other margins and free-capacity entries are unchanged. After initializing $D_A,C_{Aj},\sigma_A$ for all $A$, an edge assignment and its reversal each take $O(2^b)$ exact integer operations. Initialization takes $O(bc2^b)$ time and $O(c2^b+b+c)$ working storage. Saving deltas along a depth-first search additionally costs $O(|F|2^b)$ stack space; direct reversal can instead recompute the deltas in $O(2^b)$ time with constant additional stack data per fixed edge. A direct Hall recomputation per prefix is $O(bc2^b)$ in the comparison implementation.

**Proof.** The newly fixed edge contributes to free capacity only in column $q$, and only for row subsets containing $p$. Its fixed integer value reduces the residual column margin $S_q$ for every subset. Its value reduces subset demand $D_A$ precisely when $p\in A$. Substituting these changes in the definition of $\sigma_A$ and subtracting the previous expression gives the boxed identity. Every update is integral and reversible. Inducting on search depth proves that the incrementally maintained state equals direct recomputation at each prefix. The exact feasibility predicate also checks nonnegative residual margins, so a negative residual cannot be mistaken for a feasible cut state. QED.

## Corollary 801.2 — Identical source enumeration

Fix the same edge ordering, integer value ordering and leaf-reconstruction routine as in PREFIX-800. Prune a partial assignment exactly if some $R_i<0$, some $S_j<0$ or some $\sigma_A<0$. Then both the incremental implementation and the direct-recalculation implementation visit precisely the same search nodes and return the same complete named integer source tables. Any joint additive-observer histogram computed from these tables is therefore identical.

**Proof.** Theorem 801.1 establishes equality of every prefix feasibility predicate. Identical ordered branching gives identical prunes by induction; the same deterministic forest-leaf completion therefore returns identical output. QED.

## Finite exhaustive regression and measured computation

The accompanying standard-library Python checker independently computes Hall cuts directly and incrementally. For each supported capacity pattern it enumerates every attainable row/column margin fiber, compares the sorted complete integer source tables, samples two-dimensional signed observer histogram comparisons, and checks the published PREFIX-800 aggregate counts.

Exact coverage:
- $2\times3$ matrices with each $K_{ij}\in\{0,1,2\}$: 729 capacity patterns, 39,366 fibers.
- $3\times3$ matrices with each $K_{ij}\in\{0,1\}$: 512 capacity patterns, 17,840 fibers.
- $2\times4$ matrix with all capacities $1$: one pattern, 189 fibers.

Total: 1,242 patterns, 57,395 fibers, 66,595 complete named tables and 5,738 signed joint-histogram comparisons. Direct and incremental pruning each visited 194,900 nodes, pruned 62,390 prefixes and completed 66,595 feasible leaves. All complete sorted integer table comparisons passed. The recorded status is ALL_CHECKS_PASS PREFIX801 INCREMENTAL_HALL.

In a single Python process, per-fiber timed enumeration (including per-fiber certificate construction and leaf reconstruction, excluding enumeration of the margin-family inputs) took 2.213928 seconds with full Hall recomputation and 1.686127 seconds with incremental slack maintenance: a measured reduction of approximately 23.84%. The order of the two calls is fixed per fiber. These timings describe this particular run and implementation; both algorithms retain the same exponential search tree.

Files:
- research_notes/portable_direct/PREFIX801_R6_INCREMENTAL_HALL_CHECK.py
- research_notes/portable_direct/PREFIX801_R6_INCREMENTAL_HALL_RESULTS.json

## Reuse and next scientific question

The theorem applies to arbitrary finite bounded integer transportation fibers with named source edges. This is an auxiliary source-count observer for BRC research, rather than an established native Cell/Link/Port time-update law. It preserves the frozen P000 six-axis space, three-dimensional research slice and independent event time.

Useful next work is a larger dense/sparse benchmark including full memory/initialization cost, exact partial-feasibility memoization keyed by fixed-edge suffix and residual margins, and a typed bridge from an admissible X6 event to a nonnegative source-multiplicity update. Signed provenance and event time must be carried separately if included. No shared CLAIM, native Result or independent review is asserted by this contribution.
