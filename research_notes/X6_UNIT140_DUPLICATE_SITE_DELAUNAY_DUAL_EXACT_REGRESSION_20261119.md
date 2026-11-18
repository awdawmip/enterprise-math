# X6 Unit140 — actual source-level Delaunay/dual graph inequality for four labelled sites with one coordinate coincidence

Date 2026-11-19 (Asia/Hong_Kong). Parent PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905. Task `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`; TASK_RESEARCH author `EM-X6-FB6990`, logical research conversation `chatgpt-research-onhour-enterprise-math-20260923`. **AUTHOR UNIVERSAL PROOF / EXACT SOURCE-REPLICA EXECUTION / UNREVIEWED / NOT_ADMITTED**.

## Exact code source and P000 boundary

The selected source is `scripts/tool_discovery_carrier_voronoi_delaunay_dual_cell_check.py` in `awdawmip/enterprise-math`, original/current identical Git blob `900e246b0dafaa35d2452191e3df508a2d15a389`. Specifically `delaunay_cells` starts line 134, `dual_adjacent` line 157, `dual_edges` line 201, `convex_hull_labels` line 210, `delaunay_cell_edges` line 242. This is *Euclidean Cartesian carrier geometry*; native X6 signed Cell/P000 frozen input remains `59538f585d037d09ef687b28715c4bc1a3f9fe03`, historic comparison `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. Consumes Unit138 rank-one gap and Unit139 coincident-label clique-blow-up theorem without repeating their proofs.

## Universal source regression theorem

For four distinct **site labels** A, A', B, C at carrier positions
\[
p_A=p_{A'}=p,\quad p_B=q,\quad p_C=r,
\quad p,q,r\in\mathbb{Q}^2\text{ pairwise distinct and noncollinear},
\]
the original unmodified source computes:
\[
\boxed{E_{\rm dual}=K_4,\quad E_{\rm cell}=K_3
\quad\text{on exactly one chosen representative of }\{A,A'\}, B,C.}
\]
Consequently the assertion `dual_edges(sites) == delaunay_cell_edges(sites,delaunay_cells(sites))` fails, and **exactly three** labelled dual edges are missing from the Delaunay cell-edge side. This is independent of scale, translation, labelling order, and triangle orientation, conditional on the stated domain.

**Proof.** Every three *distinct positions* p,q,r admit their unique Euclidean circumcircle. Because A,A' are at p, no labelled site is inside this circle; `empty_circle_certificate` therefore has the four-element boundary `{A,A',B,C}`. `delaunay_cells` emits this maximal four-label boundary. `convex_hull_labels` performs a monotone chain on sorted triples (x,y,label) with non-left turns discarded by `cross<=0`. Two equal-position label points cannot both be vertices of its strict convex hull. It retains exactly one of A,A' and both B,C, returning the three hull edges. By Unit139's direct source theorem, the corresponding three unique positions have all three pairwise dual adjacencies, and the coincident labels add a clique edge and both copies of the two other neighbors. Thus `dual_edges` emits all six K4 edges; the cell edge routine emits only the three K3 edges. The missing three edges are exactly the ones incident to the discarded duplicate label.

**Concrete counterexample**: A=(0,0), A'=(0,0), B=(1,0), C=(0,1). The source returns
\[
E_{\rm dual}=\{AA',AB,AC,A'B,A'C,BC\},
\quad E_{\rm cell}=\{AB,AC,BC\}
\]
for lexicographically named A then A' as the hull representative. This is a *real disagreement between two actual source functions*, beyond the intended-meaning mismatch in Unit139. It does not show a failure for distinct-coordinate sites or for signed X6 native Voronoi adjacency.

## Finite original-function equivalent execution

An independent self-contained Fraction checker reproduces `dual_adjacent`, `dual_edges`, `circumcircle`, `empty_circle_certificate`, `delaunay_cells`, `convex_hull_labels` and `delaunay_cell_edges` with the original comparison/inequality semantics. It enumerates every ordered assignment of four distinct labels to a 3x3 integer-position grid, 9^4=6561 cases:
- Exactly **2736** cases have precisely 3 distinct noncollinear positions and one repeated coordinate. Every one returns 6 dual edges and 3 cell-derived edges, with three missing.
- Exactly **3024** cases have four distinct positions; in this domain all reproduce equality between the two original source edge sets.
- **801** other cases (one/two distinct positions or three collinear positions) are reported separately, not used in the theorem.

All exact assertions pass in Python normal, `-O`, and `-OO`. All three compact JSON outputs have SHA256 `497ebbf2f34f0d0b83e57cea58276a89cfba2944c4999e892520c89183d47801` including newline. The full original historical executable is **not** imported or run; the relevant functions are manually source-equivalent replicas. Original R063 six-file/512-case native benchmark is not rerun.

Files: `research_checks/X6_UNIT140_DUPLICATE_DELAUNAY_DUAL_SOURCE_CONSUMER_CHECK_20261119.py`, `research_checks/X6_UNIT140_DUPLICATE_DELAUNAY_DUAL_RESULTS_20261119.json`.

## Actual downstream contract and continuation

If a production caller needs arbitrary labelled sites including coordinate collisions, source graph equality cannot be used without a typed distinct-position precondition or a provenance-preserving group-labelled quotient and matching graph semantics. A minimal consumer-boundary regression should reject duplicated coordinates before checking 1D Voronoi/2D Delaunay edge equality, or explicitly compare the position quotient graph, retaining full lists of original labels. No automatic rewrite of the historical carrier tool, original accepted Result, or current native X6 kernel is asserted.

Preserve prior Units1–139 author proofs and GitHub Activity #153. Unit138 native PROGRESS is on original request `onhour-20261119-0006-x6-own-unit138-native-progress-v1` until terminal receipt; Unit139/140 native semantic linkage requires current Source authorization after that terminal. The mother's unclosed duties remain 28-LP true downstream coverage, LP011 wrong-native-dominance exact historical caller, LP019 positive natural BRC signed-cancellation exact historical caller, independent Driver REQUEST_REVISION, and separate R063 native benchmark review. No fabricated historical culprit or self-admission.

**Result: SOURCE-EXACT_CONSUMER_INVARIANT_FAILURE / PROVED_ALL_NONCOLLINEAR_3_POSITION_4_LABEL_CONFIGURATIONS / 6561_CASE_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED.**
