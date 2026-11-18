# X6 Unit139 — exact coincident-label Voronoi dual adjacency and site-identity boundary

Date: 2026-11-19 (Asia/Hong_Kong). Parent: PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905; Task `RS-X6-LEGACY-PLANE-RECONCILIATION` / `TP2-B4A441B23DA3159232C2`. Original TASK_RESEARCH lane `chatgpt-research-onhour-enterprise-math-20260923`; author contribution `EM-X6-FB6990`. **AUTHOR PROVED / EXACT FINITE EXECUTED / UNREVIEWED / NOT_ADMITTED**.

## Immutable source and layer

Keep P000 signed six-axis native Cell input pin `59538f585d037d09ef687b28715c4bc1a3f9fe03`, historical comparison `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. New check targets the exact original/current carrier-only program `scripts/tool_discovery_carrier_voronoi_delaunay_dual_cell_check.py` at Git blob `900e246b0dafaa35d2452191e3df508a2d15a389`. Source lines 157–209 implement `dual_adjacent` / `dual_edges` under Cartesian Euclidean squared distance. The source treats labels as distinct for edges but does not assert that site coordinates are injective. This unit extends Unit138's distinct-site rank-one interface analysis to a *different*, previously excluded input domain: distinct labels with coincident coordinates. It does not change primitive X6 distance or native N-BRC.

## Universal source-level theorem (finite labelled point inputs)

Let `S = [(label_i,p_i)]` have distinct labels, each `p_i \in Q^2`, with coordinates permitted to coincide. Let `Q=S/~` be the finite set of **distinct positions**, where `i~j` iff `p_i=p_j`. For each distinct position `p`, write `L_p` for its nonempty preimage label set. Let `E_Q` be the undirected edge set obtained by running the same source `dual_edges` on one uniquely labelled site for each distinct position.

Then the original source returns **exactly the clique blow-up graph**
\[
E_S =
\bigcup_{p}\binom{L_p}{2}\;\cup\!
\bigcup_{\{p,q\}\in E_Q}\{\{i,j\}:i\in L_p,\ j\in L_q\}.
\]
Thus every two distinct labels at the same position are reported adjacent even though their Voronoi regions coincide on a two-dimensional neighborhood, rather than sharing a one-dimensional face as *distinct* cells.

**Proof.** For coincident labels `a,b`, source `dual_adjacent(a,b)` has zero displacement vector and zero perpendicular vector. Its parameterized bisector `x_of(t)` is the constant position `p`. For any third site `c`, its `f0 = d(p,p)^2-d(p,p_c)^2 <= 0`, `f1=f0`, so the source neither rejects nor adds a bound. The final predicate is true. For labels at distinct sites `p,q`, every duplicate of a third site repeats an *identical* linear bisector inequality; the other labels co-located with `p` or `q` impose the tautology `0<=0` along their bisector. Removing these repeated inequalities cannot change the result. Therefore the returned edges between different position classes are precisely complete bipartite expansions of the corresponding quotient edges. Combined with the coincident-label cliques this proves the formula. Since each distinct position has a nonempty open nearest-site neighborhood, all its co-located labels share the same full-dimensional Voronoi region; a pair of such labels does not meet the source docstring's intended distinct-region one-dimensional shared-face semantics.

**Smallest decisive witnesses.** A pair `A=(0,0), B=(0,0)` returns `AB` as a source edge while the geometric regions are identical. With `A=B=(0,0), C=(2,0)`, the source reports `AB, AC, BC`, a triangle; the position quotient consists of two positions linked by one edge. Thus the program's edge graph is a *labelled coincidence expansion*, not unqualified codimension-one site adjacency, whenever coordinates are noninjective.

## Independent exact executable finite certificate

A source-equivalent `Fraction` replica of lines 157–209 was run under Python normal, `-O` and `-OO` on **all ordered labelled n-tuples** of 9 positions in `[-1,1]^2`, for n=2,3,4:
\[
9^2+9^3+9^4 = 7371 \text{ cases}.
\]
Of these, `3771` cases contain repeated positions, with `4626` total occurrences of coincident-label pairs (counted per case). Exact counts by n and distinct-position count: n2: 9/72; n3: 9/216/504; n4: 9/504/3024/3024. All 7371 source graphs match the independently constructed quotient-graph clique expansion, with zero mismatches; every coincident pair is present. All three modes emit the identical compact JSON certificate, SHA256 `5afde96fb64aecca18949b7bc952f0467b46cd52435c8e66f471c0fc631ae625` (including the output newline).

This is complete **only for the stated finite lattice input family**; the universal claim follows from the exact algebraic proof. Original complete historical executable and R063 six-file/512-case benchmark were not run. The replica code and JSON certificate are stored as `research_checks/X6_UNIT139_COINCIDENT_LABEL_CARRIER_BLOWUP_CHECK_20261119.py` and `research_checks/X6_UNIT139_COINCIDENT_LABEL_CARRIER_BLOWUP_RESULTS_20261119.json`.

## Consumer impact and minimal source change

The source's `dual_adjacent` docstring promises one-dimensional shared-face adjacency. As written it additionally allows coincident label cliques. A downstream consumer that requires genuinely distinct Voronoi sites must either (1) reject noninjective input at the appropriate validation boundary, preserving the original coordinate/label list in the error; or (2) explicitly quotient positions and carry full `L_p` provenance through graph reconstruction. **Do not silently merge labels:** multiple labels at the same geometric point may represent distinct source events or observations. The isolated finite witness justifies a scoped validation test; it does not by itself authorize altering the frozen tool or treating its carrier metric as native signed X6.

Mother-objective carryover: still unresolved are complete 28-LP current consumers, old exact LP011 signed-native dominance misuse and LP019 positive natural N-BRC cancellation caller provenance; independent Driver revision / admission and original R063 native-object benchmark remain separate. Existing Units1–138 and their verified GitHub certificates are consumed, not re-evaluated. Preserve existing Source/RA role; Native semantic Unit138 request `onhour-20261119-0006-x6-own-unit138-native-progress-v1` remains to be reconciled, and Unit139 Native PROGRESS requires fresh owner confirmation.

**Author status: SOURCE_EXACT_CODE_REPLICA / UNIVERSAL_PROOF / FINITE_CERTIFICATE_EXECUTED / UNREVIEWED / NOT_ADMITTED.**
