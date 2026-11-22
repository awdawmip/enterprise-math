# R762JD — Three additional 46→44 full-support Port–Euler terminal classes

Date: 2026-11-22 (Asia/Shanghai).
Frozen scientific pin: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389 (unchanged).
Status: AUTHOR_PROVED / EXACT_FINITE_WITNESSES_CHECKED / NOT_REVIEWED.
Science scope: composite 15-Port/20-triangle-support Euler observer only; original signed X6 path, triadic closure, phase, ordering and structural residual not asserted preserved.
Dependencies: R762IR nonessential-triangle GF(2) repair; R762JA uniform 46 upper bound; R762JB six-triple compression; R762JC seven-triple compression.

## New precise statements

For a multiplicity vector n in {1,2,3}^20, let N_{p,V}(n)>0 mean existence of a connected multigraph with positive even degrees on exactly the active Port set V, using one of three Port edges for each event of a three-axis support, and admitting an Euler circuit beginning at p in V. Define t=#supports of multiplicity 3, d=#supports of multiplicity 2, s=#supports of multiplicity 1, z=#supports of multiplicity 0.

**Theorem R762JD.** For each histogram among

- (t,d,s,z)=(8,10,2,0);
- (9,8,3,0);
- (10,6,4,0),

a legal original 46-event history N_{p,V}(n)>0 implies there exists j with n_j=3 and N_{p,V}(n-2e_j)>0. The 44-event witness has the same positive support types, same support-count parity, same exact active Port set V, and any original designated starting Port p.

## Proof

All 20 support types are present, so the inactive Port set is necessarily a matching of K6 (if two inactive pair-Ports share an axis, their unique containing support has only one active Port and cannot carry any event).

Case I: Any triple support has an inactive Port. Then only two of its Port vertices are active, so all three copies of that support event use the single allowed edge; deleting a pair preserves positivity of that support, degree parity, exact activity and connectivity.

Case II: All t triple triangles are fully active and one triple triangle is not component-essential in the union of their complete 3-edge Port triangles. The R762IR GF(2) path repair transfers the difference in the three-event versus one-event local boundary through the other complete triple triangles. Three event copies can realize either zero boundary via a triangle cycle, or a prescribed two-vertex boundary via one edge between those vertices and a two-parallel-edge connection to the third. The replacement keeps each full triangle's internal connectivity. Hence the new global graph is connected and all active degrees remain even.

Case III: All t fully active triangles are component-essential. Exact enumeration of every size-t support family, modulo all 720 permutations of the six axes, yields the finite data below. For each S6 orbit representative, enumerate all inactive K6 matchings disjoint from the union of its full triangles and each possible choice of s singleton supports outside the triple family. Reduce the smallest-index triple from 3 to 1. For each representative (triple family, inactive matching, singleton supports), a HiGHS integer program finds a 60-component allocation to the three possible edges of each support. The checker then independently validates the proposed integers: exact original-minus-two multiplicity vector, 44 total events, zero inactive degree, positive even active degree, and connectedness by BFS. If the first integer allocation is disconnected, an exact integer edge-crossing cut is added and the candidate is regenerated, then verified.

| histogram | all-essential triangle families | S6 orbits | checked representative configurations | represented labelled configurations | exact check |
|---|---:|---:|---:|---:|---|
| (8,10,2,0) | 4,920 | 16 | 1,650 | 455,400 | 1,650/1,650 PASS |
| (9,8,3,0) | 240 | 2 | 495 | 49,500 | 495/495 PASS |
| (10,6,4,0) | 6 | 1 | 210 | 1,260 | 210/210 PASS |

Further exact execution breakdown:
- Eight triple supports: inactive Port counts {0:1056,1:528,2:66}, connectivity-cut rounds {0:1639,1:11}.
- Nine triple supports: inactive counts {0:330,1:165}, cuts {0:494,1:1}.
- Ten triple supports: inactive counts {0:210}, cuts {0:210}.

All three cases together required **2,355 exact positive-even-degree, connected, 44-event witnesses**. Independent local rerun of the combined checker returned PASS for all three classes on 2026-11-22. S6 symmetry transports the integer certificate of each representative to every labelled configuration. A connected Eulerian graph has a circuit from any p in its active set. Thus all three histograms satisfy the theorem, by the exhaustive cases above.

## Reproducibility and computation boundaries

Companion script R762JD_THREE_FULL_SUPPORT_CLASSES.py imports the same-directory R762JC_SEVEN_TRIPLE_46_44.py, and uses Python+NumPy+SciPy/HiGHS. This is a reproducible exact finite construction/verification pipeline: the integer solver only proposes candidates; assertion-based checks of support totals, graph degrees and connectivity validate each candidate. Source inputs, enumerations, expected counts, and intermediate orbit classification all appear in the scripts. Published artifacts contain the executable regeneration and checker; **they do not embed the whole 2,355-vector certificate table**. They were actually executed locally and the same expected counts verified; no Lean/formal acceptance, independent reviewer sign-off or native signed-P000 lifting is claimed.

Reproduction from the project branch, with dependencies installed, in the scientific directory:

    python R762JD_THREE_FULL_SUPPORT_CLASSES.py

Expected concluding line:

    PASS R762JD ALL THREE CLASSES: 2355/2355 EXACT CONNECTED EULER WITNESSES

## Consequence and remaining research frontier

Combine R762JB, R762JC and R762JD: **all five 46-event terminal histograms with z=0 and 6<=t<=10 are author-proved reducible to 44 events (the t=11,12,13 full-support cases require separate high-triple reduction)**:

(6,14,0,0), (7,12,1,0), (8,10,2,0), (9,8,3,0), (10,6,4,0).

This finite statement proves exactly the five cases with 6<=t<=10. The previously published R762IR theorem (read at immutable Source commit 74e40c74cdebeab4e72cc3d814c35386ca060e44) separately gives an immediate 3-to-1 reduction for ANY legal history with at least 11 triple supports, even when supports are absent. Hence **all eight possible z=0 full-support 46-event terminal histograms (6<=t<=13) admit a 44-event witness**, conditional on the earlier author-proved R762IR lemma. The overall k=0 upper bound remains **46**, since four residual z>0 histograms at t<=10 remain: (8,11,0,1), (9,9,1,1), (10,7,2,1), (10,8,0,2). Larger t are covered conditionally by R762IR. Review the predecessor dependency and exact missing-support activity constraints before any uniform bound promotion.

Neither this publication nor S6 symmetry establishes preservation of full event order, signed native Cell updates, BRC branch labels, phase, time, residuals, or formal Task CLAIM/Result/Review.
