# PREFIX-796 / R6 — Capacity-sensitive residual flow: pointwise uniqueness and sharp integer uncertainty

Date: 2026-11-15 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXHAUSTIVE_EXACT_INTEGER_REGRESSION / UNREVIEWED / NOT_ADMITTED.
Frozen science: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Predecessor: PREFIX-795, immutable source 25cb57e4c7f8b1e9e9257e7bcb86b22122f85c2a.
Scope: finite positive-integer BRC complete-path histogram, **not** a validated native X6 event.

## Carrier and observable fiber

For b,c>=2, each named joint cell e=(i,j) has nonnegative integer complete-path multiplicities n_(0,e),n_(1,e). The exact pairwise observer reports K_e=n_(0,e)+n_(1,e), row sums and column sums of x_e=n_(0,e). PREFIX-795 time-ordered local swaps reveal x_e exactly at queried cells; subtract these known contributions and let U denote the unqueried cells. The observer fixes row supplies r_i, column supplies s_j and capacities 0<=x_e<=K_e, so the integer fiber is

    F(K,r,s)={y in Z^U: 0<=y_e<=K_e;
              sum_j y_(i,j)=r_i, sum_i y_(i,j)=s_j}.

Assume F is nonempty and x is the actual state. Define residual directed graph D_x on row nodes R_i, column nodes C_j. Each unqueried e=(i,j) contributes an arc R_i->C_j of capacity K_e-x_e if positive (legal increase), and C_j->R_i of capacity x_e if positive (legal decrease). When 0<x_e<K_e there are two opposite arcs for the **same** cell; traversing both as a two-step backtrack changes nothing.

## Theorem 796.1 — Exact pointwise uniqueness

F(K,r,s)={x} if and only if D_x contains no directed simple cycle of length at least four, equivalently no nonzero residual circulation supported on distinct cells.

**Proof.** A directed simple cycle in the bipartite graph has even length >=4. Increase x_e by 1 on every R->C arc and decrease x_e by 1 on every C->R arc of the cycle. Residual capacity ensures 0<=x'_e<=K_e. At every vertex, incoming and outgoing changes balance, preserving both row and column sums. Hence x' differs from x and lies in F.

Conversely let y in F differ from x. Put y_e-x_e units on the R->C arc where y_e>x_e, and x_e-y_e units on the C->R arc where y_e<x_e. The capacities are adequate and zero row/column marginal differences make this a nonzero nonnegative integral circulation. Every such circulation decomposes into directed simple cycles. Its support has at most one orientation per original cell, so a same-cell two-arc backtrack is impossible. Hence it has a directed cycle with >=4 distinct vertices. QED.

**Capacity-sensitive witness.** In the full 2x2 graph U the undirected 4-cycle survives. Set K_e=1 and x_e=0 for every cell. The row/column totals force this unique x, and D_x has only R->C arrows. By contrast K_e=2,x_e=1 for every cell admits alternating ±1 along a 4-cycle, giving the target-cell set {0,1,2}. The forest iff in PREFIX-795 is a **universal** criterion when capacities can vary; the present theorem determines uniqueness for a particular bounded observation.

## Theorem 796.2 — Sharp coordinate interval and integer max-flow certificate

Fix an unqueried e=(i,j). Remove both directed arcs corresponding to e from D_x. Let

    F_+(e)=maxflow(C_j -> R_i; D_x without e),
    F_-(e)=maxflow(R_i -> C_j; D_x without e).

Then the *exact* range of all possible target coordinate values is every integer in

    [x_e-min(x_e,F_-(e)), x_e+min(K_e-x_e,F_+(e))].

**Proof.** If x_e increases by integer t, the remaining cells must route t units from C_j to R_i in the residual directed network, closing a balanced circulation with the target arc R_i->C_j. Such a flow is legal iff t<=K_e-x_e and t<=F_+(e). Integral max-flow supplies flows for every integer t from 0 to that bound; augmenting along each signed arc produces another feasible integer histogram. Conversely any feasible y with y_e-x_e=t>0 defines an integral residual C_j-to-R_i flow of value t on the other edges, by the same signed-difference construction. This proves the upper interval endpoint and all attainable intervening values. Reverse the orientations for a decrement of x_e; capacity x_e and F_-(e) give the lower endpoint. QED.

**Algorithmic corollary.** Each target's exact integer uncertainty is determined by two standard max flows, excluding the target cell. A pointwise uniqueness detector computes these intervals and tests whether every one is a singleton. It preserves joint positive counts and source identities; there is no signed-amplitude cancellation. Polynomial arithmetic-operation complexity follows from finite integral max flow; no bit-complexity improvement has been claimed without the encoding costs.

## Reproducible exact validation

Checker: research_notes/portable_direct/PREFIX796_R6_CAPACITY_RESIDUAL_CERTIFICATE_CHECK.py.
Results: research_notes/portable_direct/PREFIX796_R6_CAPACITY_RESIDUAL_CERTIFICATE_RESULTS.json.

The Python standard-library checker exhaustively enumerates all 0<=x_e<=K_e<=2 assignments for 2x2 (1296) and 2x3 (46656) grids. For every assignment it enumerates **the entire feasible fiber** with fixed K and row/column totals, compares actual uniqueness with the directed-cycle condition, compares every coordinate's actual min/max to the two max flows, and verifies every intervening integer value occurs. Totals: 618196 exact integer assertions, including four explicit boundary-witness assertions; ALL_CHECKS_PASS. Universality rests on the proofs, not the finite enumeration. No floating point or randomness.

## Boundary, lineage and next mathematical frontier

The result refines the earlier cycle-rank theorem for finite-capacity *actual* observations, and uses the classical mathematics of integer transportation tables and residual flow networks, without asserting priority for that standard theory. It requires an exact initial pairwise observer, named-cell swaps where used, known K and nonnegative integer capacities. Real native X6 Cell/Link/Port operations still need a documented typing, permission, conserved quantity and temporal event update; synthetic swaps do not certify them.

Next: (1) extract the actual permitted native event/readout map, test which coordinates and capacities survive its projection; (2) investigate simultaneous multi-cell uncertainty, for which independent coordinate intervals can overcount due to shared margins; (3) if observations are approximate, derive a propagated uncertainty bound rather than importing exact max-flow uniqueness.

Attribution: Historical EM-DIRECT-E77192 is prior-lineage metadata, not a live capability. Shared RS-X6-NATIVE-TIME-DYNAMICS has separate ownership; Source publication here is not a shared CLAIM/Result/Review or Foundation admission.
