# X6 Unit141 — current carrier duality **call-site** domain closure and exact fail-closed typed adapter

Date: 2026-11-19 (Asia/Hong_Kong). Parent `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`, Task `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. Research identity `EM-X6-FB6990` / own SID `MCP-082892eb480e45dea6d4b9fcc0491034`. **AUTHOR SOURCE-ATTESTED / FINITE EXACT EXECUTED / UNREVIEWED / NOT_ADMITTED.**

## New source-consumer finding, beyond Units138–140

Inspected **the complete current** `scripts/tool_discovery_carrier_voronoi_delaunay_dual_cell_check.py`, Git blob `900e246b0dafaa35d2452191e3df508a2d15a389`, lines 1–563. Its actual `run()` has exactly **two direct** Delaunay-cell-edge versus Voronoi dual-edge equality assertions, at **378–381** (`generic`) and **424–426** (`square`). Their literal coordinate inputs are at 365–370 and 397–402. Both have four pairwise distinct site labels, four pairwise distinct carrier coordinates and affine rank two. For `generic`, `det(B-A,C-A)=12`; for `square`, `det(B-A,D-A)=4`. The remaining `dual_edges` calls at 414, 447–463 are comparisons of a different, explicitly described kind, not hidden primal/dual equalities. Thus the Unit138 rank-one and Unit140 coincident-position counterexamples are **real helper-function domain failures**, but **are not exercised by these two existing direct production-script equality assertions**. This is a bounded file-level call-site result; external importers are not certified.

The original source returned, under this precise caller domain:
- `generic` dual and cell-edge sets both equal `{AB,AC,BC,BD,CD}` (five edges);
- `square` dual and cell-edge sets both equal `{AB,AD,BC,CD}` (four edges), with no fictitious cocircular diagonal.

No modification of the existing current test's valid inputs is necessary. A downstream client which wants to assert this graph equality must **declare its input domain**, and must not infer that labels with identical carrier positions define distinct 1D Voronoi edges.

## Typed certificate and executable check

Define `D(S)` on a finite *labelled Euclidean carrier* site list by: (i) labels injective, (ii) positions injective, (iii) the positions contain a noncollinear triple (affine rank two). The exact checker `research_checks/X6_UNIT141_LIVE_CARRIER_DUAL_CALLER_DOMAIN_CHECK_20261119.py` implements the three predicates before invoking source-equivalent `dual_edges` and `delaunay_cells + delaunay_cell_edges`. Failure raises an explicit `CarrierDomainError`; there is no silent quotient of duplicate-label or duplicate-position fibers. This is a conservative sufficient **admission domain for the two direct current script consumers**, not a proof that every site collection outside it has unequal mathematical Voronoi and Delaunay structures.

On four named labels, assigned independently to the nine integer sites in `[-1,1]^2` (exactly `9^4=6561` ordered assignments), injective carrier coordinates occur in exactly `9·8·7·6=3024` cases. Every four distinct points on a 3-by-3 lattice have affine rank two (a straight line contains at most three of these points), so all 3024 pass the typed domain; **all 3024 source-equivalent comparisons agree**. The remaining `6561-3024=3537` have coincident positions and are explicitly refused. Separately supplied witnesses for rank-one four-site input and duplicate label are explicitly refused. The two original actual caller inputs also pass and return the exact five- and four-edge sets above.

Python `normal`, `-O`, `-OO` were executed on the *same* self-contained Fraction checker: exit 0 each, byte-identical JSON SHA256 `b44d840fe2e02edcdccf9f52d8f544c84e7ac88cfc3b05d2c1bed0da149c7519`. The checker implements only cited source functions, not an import/execute of the entire original historical tool, and does not run the frozen R063 six-file/512-case benchmark. It supplies exact finite evidence, not a global formal proof of all source code paths.

## Type and authority boundaries; concrete next action

This is two-dimensional **Euclidean carrier** mathematics; P000 signed six-axis native Cell source remains frozen at `59538f585d037d09ef687b28715c4bc1a3f9fe03`; historical comparison pin `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. Keeping label/position fibers distinct is necessary before any observer quotient; the guard is a portable proof-of-contract, **not integrated into the existing production source** and not authority to rewrite accepted historical science. Unit140's source helper mismatch persists for unguarded general inputs. If a real downstream importer is located calling this equality outside `D(S)`, update that specific consumer to enforce `D(S)` or provide a mathematically specified fiber-preserving alternative; do not gratuitously patch the present valid two calls.

Continue parent 28-LP source:line downstream coverage, and LP011 old native-axis argmax / LP019 natural positive N-BRC signed-subtraction alleged historical caller search, leaving both `UNRESOLVED_PROVENANCE` until exact evidence. Independent Driver REQUEST_REVISION remains separate. Research activity/checkpoint and Native semantic PROGRESS are independent of this scientific result.

**Result:** `CURRENT_CALLSITE_TYPED_BOUNDARY_CLOSED_FOR_TWO_CHECKS / 6561_EXACT_FINITE_CASES / THREE_MODES_EXECUTED / UNREVIEWED / NOT_ADMITTED`.
