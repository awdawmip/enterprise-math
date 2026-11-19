# X6 Unit167 — Rooted shortest-word residual in the frozen FCC chirality two-sheet cover

Date: 2026-11-20 (Asia/Hong_Kong). Task `RS-X6-LEGACY-PLANE-RECONCILIATION`; parent `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`; original Researcher `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`, ordinary Research conversation `chatgpt-research-onhour-enterprise-math-20260923`. Status **AUTHOR_PROVED / EXACT_FINITE_EXECUTED / SOURCE_CALLER_BOUND / UNREVIEWED / NOT_ADMITTED**. This is a derived FCC orientation-cover count, **not** native signed-X6 N-BRC or a physical 3D-to-6D identification.

## Frozen original production → consumer chain

* Source `awdawmip/enterprise-math@fd2bcff10ca6e147348b6c1236027fc0d2877df3:src/enterprise_math/euler_fcc_chirality.py`, Git blob `6f8b147c094720c2749f620a40394c4d7b67a386`, lines 35–49 (six edges, four faces), 107–125 (all edge assignments and signed states), 138–160 (vertex gauge and face XOR holonomy), 248–267 (the cover adjacency), 270–275 (gauge relabeling).
* Production consumer `src/enterprise_math/euler_fcc_chirality_connectivity.py`, same frozen commit, blob `ddf9a06abd859f5cc9c109b76e1979147fbed399`, lines 33–85 (neighbor enumeration, connected components and pair distance), 113–159 (64-edge classification and exact expected counts).
* Actual frozen test importer `tests/test_euler_fcc_chirality_connectivity.py`, blob `794037b5d2f2a58b79b0054814d6e7a69b3fe7f1`, lines 28–59 and 61–93. Historical tests verify degree three, flatness/connectivity and gauge adjacency, but do not directly enumerate **rooted geodesic-word multiplicity profiles**. The latter is the incremental question here.
* P000 V5 and X6 signed Cell-space input remain frozen at `59538f585d037d09ef687b28715c4bc1a3f9fe03`; historical comparison remains `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. No source ontology mutation.

## New typed statement

Let vertices of the base tetrahedron be `0,1,2,3` and let its six undirected edge bits be `e_ij in F2`. The derived *cover* has eight states `(i,s)` with `s in F2`; there is one step `(i,s)->(j,s+e_ij)` for each `j!=i`. A face `ijk` carries XOR holonomy `h_ijk=e_ij+e_ik+e_jk (mod 2)`; the four face bits have even parity. Define the **rooted geodesic profile** at a given state as the list of `(number of reachable vertices at graph distance r, sum of shortest-word multiplicities to them)` for each `r>=0`. Its arithmetic type is `N`-valued **derived cover shortest-step counts**, *not* the original six-dimensional signed Cell N-BRC.

**Theorem (complete 64-assignment/8-root classification).** The profile is determined by the face holonomy and, only in the two-odd-face case, by one extra bit telling whether the base root lies on the common edge of the two odd faces:

| Face holonomy and root condition | r=0 | r=1 | r=2 | r=3 |
|---|---|---|---|---|
| All 4 faces even (flat) | (1,1) | (3,3) | — | — |
| Exactly 2 odd faces; root on their common edge | (1,1) | (3,3) | **(3,4)** | (1,4) |
| Exactly 2 odd faces; root off their common edge | (1,1) | (3,3) | **(2,2)** | (2,4) |
| All 4 odd faces (cube) | (1,1) | (3,3) | (3,6) | (1,6) |

The six two-odd face patterns each have eight edge assignments. Each pattern has two base vertices on the odd-face intersection and two off it; the sheet bit does not alter the profile. Across all 64 assignments and eight roots, rooted-instance frequencies are respectively `64,192,192,64` in the displayed order.

**Sharp observer defect.** In the two-odd class, storing the complete labeled face-holonomy pattern but forgetting the base root's membership in the shared odd-face edge leaves two possible geodesic profiles. Already at radius two the counts are `(3,4)` vs `(2,2)`. Exactly one extra Boolean root-incidence bit is necessary and sufficient to recover the *rooted profile from face-holonomy alone*. The full labeled root and graph would also suffice; this is a conditional minimal **profile-repair** statement, not a claim that one bit recovers every native path or Cell address.

## Universal proof over all 64 edge-bit assignments

The face XOR map has kernel precisely the four-vertex gauge coboundaries `e_ij -> e_ij+g_i+g_j`: the kernel has size `2^(4-1)=8`, and face parities span the 8 even four-bit patterns. Thus any two edge assignments with the same face pattern are related by an explicitly source-defined gauge transformation. Its cover relabeling `(i,s)->(i,s+g_i)` is a graph isomorphism preserving the full rooted geodesic profile.

For zero face holonomy, choose the all-zero representative; its cover is two disjoint `K4` graphs, giving the flat profile. For all odd faces, take every edge bit one; its cover is the three-cube, whose distance-r sphere has `C(3,r)` vertices, each with `r!` shortest words: the cube profile follows.

For a face pattern with two odd faces, let `{a,b}` be their common-edge intersection. Choose the representative whose only nonzero edge bit is `e_ab=1`; exactly those two faces become odd. Direct inspection from `(a,0)` gives distance-1 `3` states (each mass one), distance-2 `3` states with masses `1,1,2`, and distance-3 one opposite-sheet state with mass `4`. From `(c,0)`, `c not in {a,b}`, the distance-2 states have masses `1,1`, and distance-3 states have masses `2,2`. Permuting the tetrahedron's vertex labels and flipping all sheet bits proves the four displayed profiles for every choice of root. The two radius-2 profiles differ, proving sharpness of the missing incidence bit.

## Independent executable certificate and source-bound validation

Independently implemented a complete integer graph BFS shortest-count recurrence and a separate complete length-0..3 **walk word enumerator**. The two independent algorithms agree on every reachable endpoint in every root case. A separate gauge transform loop checks all 16 vertex gauges against all 64 edge assignments and eight rooted states. Exact execution, no `assert`-only checks:

* 64 edge-bit assignments, 8 distinct even face-holonomy classes, 8 assignments per holonomy class.
* 512 rooted graph instances, **3,840** independent shortest endpoint-word comparisons, **8,192** gauge-equivariant rooted-profile comparisons.
* Root-profile counts `flat=64`, `two_odd_intersection=192`, `two_odd_complement=192`, `all_odd=64`. Violations `0`.
* Python normal, `-O` and `-OO` all emitted identical JSON certificates. The original frozen test suite and original R063 six-blob native benchmark **were not rerun**.

Independent files: `research_checks/X6_UNIT167_FCC_CHIRALITY_ROOTED_BRC_CHECK_20261120.py` (SHA256 `82369d1192ab6bfb6899708a7674e3e50cb1702c2af9cbc5e9f1a9489875f9fd`) and `research_checks/X6_UNIT167_FCC_CHIRALITY_ROOTED_BRC_RESULTS_20261120.json` (SHA256 `76141103ed07afc5f25a1bb9adc42f4c6b5837150518befc90c0d60c3cc0c61a`).

## Mother-objective disposition and pending work

This authentic producer→consumer check **PRESERVES DERIVED CARRIER/COVER**, distinguishing cover-rooted positive word multiplicity from native X6 signed twelve-direction N-BRC. The frozen tests' named eight-state cover is internally correctly typed; no actual historical LP011 wrong native signed-axis argmax or LP019 wrong positive N-BRC subtraction is demonstrated by this source. Do **not** relabel these correct calls as the alleged source bugs. Retain original R063 17/17+512/512 benchmark, Unit157/P022 prior-art correction and all older authored science.

Original Unit162–164 native request `onhour-20261119-2208-x6-own-units162164-native-progress-v1` has been independently verified SUCCEEDED / SOURCE_CHECKPOINT_PUBLISHED / authenticated_readback; own resume `onhour-20261120-0004-x6-own-run-c920-after164-resume-v1` returned SUCCEEDED/RUN_READY/generation11. Unit165–166 native semantic request `onhour-20261120-0015-x6-own-units165166-native-progress-v1` was queued once; read its original receipt before any further native mutation. Units149–152 historical native association debt, exact LP011/LP019 original bad caller, remaining 28-LP dynamic source/consumer coverage and independent Driver review remain pending. Status `AUTHOR_PROVED/EXACT_FINITE_EXECUTED/UNREVIEWED/NOT_ADMITTED`.
