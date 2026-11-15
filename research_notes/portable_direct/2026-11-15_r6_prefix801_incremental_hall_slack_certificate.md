# PREFIX-801 — Incremental Hall-slack certificates for finite provenance-count fibers

Date: 2026-11-15. Research line: R6 independent portable research. Predecessor: PREFIX-800 (commit `455ecc396f836c127e0f4920c659bce8327c9be8`). Frozen science input pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Status: AUTHOR_PROVED / EXACT_INTEGER_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

## Problem and source model

Let (G=(U,V,E)) be a finite named bipartite source graph with $|U|=b$, $|V|=c$, integer capacities $K_{ij}\ge 0$, row margins $r_i$, column margins $s_j$ and $sum r_i=sum s_j$. At a partial assignment $F\subseteq E$, with fixed integer values $t_{ij}\in[0,K_{ij}]$, remove the fixed edges, and define residual margins
$$
R_i=r_i-\sum_{(i,j)\in F}t_{ij},\qquad
S_j=s_j-\sum_{(i,j)\in F}t_{ij}.
$$
For each row subset $A\subseteq U$, set $D_A=\sum_{i\in A}R_i$, (C_{Aj}=\sum_{i\in A:(i,j)\notin F}K_{ij}), and the **Hall slack**
$$
\sigma_A=\sum_{j\in V}\min$S_j,C_{Aj}$-D_A.
$$

PREFIX-800 proves exact integer feasibility iff all residual row/column margins are nonnegative and every $sigma_A\ge0$. This note derives an incremental exact update and demonstrates its cost on precisely the earlier frozen regression families. The count observer is a source-labeled external BRC auxiliary model; no native X6 event/time correspondence is assumed.

## Theorem 801.1 — Constant-locality Hall slack update

Let (e=(p,q)\notin F) have capacity $k=K_{pq}$, and fix $x_e=t\in\{0,\dots,k\}$. For every row subset $A\subseteq U$, put $delta_A=1$ if $p\in A$, otherwise (0). Then the new exact Hall slack is
$$
\boxed{\sigma'_A=\sigma_A+
\min$S_q-t,C_{Aq}-\delta_A k$-\min$S_q,C_{Aq}$+\delta_A t.}
$$
All other column terms in the slack remain unchanged. The associated exact updates are
$$
R'_p=R_p-t,\ S'_q=S_q-t,\
C'_{Aq}=C_{Aq}-\delta_A k,\
D'_A=D_A-\delta_A t .
$$
Consequently an insertion or rollback requires (O$2^b$) integer operations after one (O$bc2^b$) initialization; storage is (O$c2^b+b+c+|F|2^b$) with per-branch stored deltas, or (O$c2^b+b+c$) for reversible recomputation at rollback. Direct Hall recomputation from the full residual capacities costs (O$bc2^b$) per prefix in the simple implementation.

**Proof.** Fix (A). Only the term at column (q) has changed, because the new fixed edge is removed from free capacity precisely when $p\in A$, and only $S_q$ changes. The demand $D_A$ decreases by (t) precisely in that same case. Subtracting the old displayed slack from the new one gives the boxed identity. Each update uses one integer min and additions/subtractions per subset. Reversing it restores the exact previous slack; induction over the assignment depth proves all maintained values equal the direct definitions. This is an algebraic identity over integers, independent of nonnegativity. For feasibility additionally test nonnegative residual margins. QED.

## Corollary 801.2 — Identical pruning tree and exact joint observers

If the incremental update is applied to the same predetermined chord order and variable order as PREFIX-800 and a partial branch is rejected exactly when a residual margin is negative or some $sigma_A<0$, then it visits the same branches, produces the same feasible source tables, and yields the same finite collection of exact joint additive-observer histograms. This follows from Theorem 801.1 and the PREFIX-800 max-flow/min-cut criterion, at every prefix. Source-edge identity and integer capacities are retained.

## Complete finite implementation regression

Reproduction: `PREFIX801_R6_INCREMENTAL_HALL_CHECK.py`, standard-library Python, with deterministic capacity/edge/variable order. Independently evaluate Hall feasibility by direct recomputation and by incremental slacks, enumerate and compare sorted complete integer source tables, check sampled signed joint-observer histograms, and compare all previously published PREFIX-800 exact aggregate counts.

Complete declared families: all $2\times3$ capacities in ({0,1,2}); all $3\times3$ capacities in ({0,1}); and a complete $2\times4$ unit-capacity pattern. All feasible marginal fibers of each listed pattern are enumerated (same universe as PREFIX-800). Actual run:
- 1,242 capacity patterns; 57,395 marginal fibers; 66,595 complete tables; 5,738 signed joint-histogram comparisons.
- Both implementations visited 194,900 nodes, pruned 62,390 prefixes, and completed 66,595 leaves. The exact sorted output tables matched in every fiber.
- Within one standard-library Python process, timed enumeration with full table recovery totaled 2.213928 seconds for recomputation versus 1.686127 seconds for incremental updates (about 23.84% less measured time). Calls were paired per fiber in fixed order; values depend on this environment and implementation. Both algorithms bear the same exponential search tree, but the incremental method avoids the direct (bc) factor in each certificate update.
- Result: `ALL_CHECKS_PASS PREFIX801 INCREMENTAL_HALL`, full machine-readable output `PREFIX801_R6_INCREMENTAL_HALL_RESULTS.json`.

The proof is for arbitrary finite integral capacities and fixed partial assignments. The finite regression verifies implementation on the declared families. The timings include per-fiber initialization and leaf reconstruction; generating all margin families is outside both method timers.

## Next question and scientific scope

Apply incrementally maintained certificates to larger (b) and sparse/dense support, compare measured compute and memory costs against direct row-transfer DP, and test caching by (remaining edge suffix, residual row margins, residual column margins). At a fixed prefix the residual support is determined by the edge order, so this is an exact feasibility-cache key. A subsequent typed X6 Cell/Link/Port source path must separately establish which updates conserve integer positive multiplicity and how signed provenance and event-time constraints enter. Frozen P000 / ACTIVE six-axis and three-dimensional-slice worldview remain unchanged.

Ownership: this note is an independent externally publishable mathematical auxiliary contribution. It creates no shared CLAIM, native Result, or review by itself.