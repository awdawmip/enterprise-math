# R762JQ — 44→42 parity construction with one inactive Port

Date: 2026-11-23 (Asia/Shanghai). Status: AUTHOR_EXACT_FINITE_CHECKED / NOT_REVIEWED.
Continuation: R762JP analytic all-active theorem (Draft PR #2983). Frozen six-axis composite Port–Euler observer; original signed P000 inputs unchanged.

## Exact domain

Let A={0,...,5}, P=C(A,2), S=C(A,3). There are 15 pair-Ports and 20 support triangles. An event s joins two distinct pair-Ports within C(s,2), allowing parallel copies. The histogram (t,d,s,z)=(6,12,2,0) has total 44 events. Fix ONE inactive pair-Port m and require all other 14 Ports to have positive even degree, with zero at m and connected active graph. An Euler circuit can then start at every active Port.

As in R762JP, choose three labels D which have multiplicity one **after** deleting two parallel events from one of the original six triple labels j∈D. The other two labels of D are the original singleton supports. The other 17 labels have multiplicity 2 or 3, with five of them triple. For any such D, any j∈D, and any five additional triples among S\D, the following sufficient criterion applies.

## Structural parity criterion

A support s containing the inactive Port m leaves exactly two active local vertices. All its c_s edges must join that same pair of active Ports, hence its degree boundary is forced by c_s mod2. All remaining supports have three active local vertices; call them FULL supports. If among the FULL supports **outside D** there is a support-rainbow spanning tree R of the 14 active Ports, then an exact 42-event Euler witness exists for **every** allowed assignment of 2 and 3 multiplicities to the remaining labels.

Proof: Fix all local edges of the singleton labels and all copies of two-active-vertex support labels. They produce some even-weight endpoint-boundary b∈GF(2)^14. For every FULL support of count2, realize endpoint parity either zero with two parallel edges or the boundary of any chosen local edge via the complementary two sides of its triangle. For every FULL support of count3, realize zero boundary via all three sides or chosen-edge boundary via three copies of that edge. Use the 13 distinct colors of R as the adjustable supports, with designated tree edges; use zero-parity realizations for remaining flexible FULL labels. The 13 tree-edge incidence vectors form a GF(2) basis for the even vectors on 14 vertices, so choose the unique subset summing to b. Every adjustable support still connects the endpoints of its tree edge even when its two-edge path replaces the edge. All 14 active Ports are therefore connected, parity vanishes, all positive supports remain present, and Euler's theorem applies. This also preserves the start Port. QED.

## Exact exhaustive 14-Port rainbow-tree classification

All pair-Ports are equivalent under S6. Fix m={0,1}. Four support labels {0,1,c} for c∈{2,3,4,5} contain m and are two-active-Port supports. The other 16 FULL support labels comprise:
- six A-wing supports {0,c,d} with c,d in {2,3,4,5};
- six B-wing supports {1,c,d};
- four core supports wholly in {2,3,4,5}.

The independent Python-standard-library checker R762JQ_ONE_INACTIVE_VERIFY.py enumerates ALL C(20,3)=1,140 deleted-color sets D and computes maximum size common independence of the graphic and color partition matroids using an explicit alternating-path augmenting algorithm. Every produced rainbow tree is checked for 13 edges, distinct support colors and connectivity.

- For **1,100** sets D, a full 13-color rainbow tree exists. For each of their three distinguished possible j, the checker constructs and verifies an explicit 42-event Euler witness: **3,300/3,300 PASS**. The parity construction in fact works for **every choice of the five additional triple labels**, even though the checker selects a single canonical assignment for each D.
- For the remaining **exactly 40** sets D, the rainbow spanning-tree criterion fails. These 40 are precisely the 3-element subsets wholly inside one six-label wing: 2·C(6,3)=40. This exception has a structural obstruction *to the sufficient criterion only*: omitting three A-wing colors leaves three A-wing colors, whereas the four Port vertices (0c), c=2..5, require at least four distinct rainbow tree-edge colors to connect to the rest in any rainbow spanning tree of the flexible FULL graph; the analogous statement holds for B-wing. This does not establish impossibility of an Euler circuit because the four non-FULL labels {0,1,c} also provide compulsory links.

Computed exact canonical witness stream SHA-256: 01e9b2fdeb37ea8ca69da71b50967086042860f73ce03b664d02561b4f7db809. All 15 singleton inactive-Port positions follow from axis permutation symmetry. Program checks all support multiplicities, all active degrees positive/even, the inactive degree zero, 42-event count, and graph connectedness.

## Supplemental 40-exception feasibility probe (not a full quantifier)

For the 40 exceptional D and three possible j∈D (120 cases), the previous R762JM SciPy/HiGHS candidate construction with connectivity cuts produced **120/120 valid 42-event integer candidates** with one canonical assignment of the other five triple supports (the lexicographically first five labels outside D). This evidence demonstrates the 40 exceptions of the rainbow-tree sufficient criterion can still admit Euler compression; it does NOT prove the universal 44→42 theorem for all assignments of those five triples. Exact script R762JQ_EXCEPTION_PROBE.py includes independent integer degree/connectivity checks. Solver output is not itself used as proof; each concrete candidate is independently checked.

## Evidence status and remaining target

This is a **finite exact classification of the sufficient rainbow-tree method** plus a mathematically valid general construction for its 1,100 successful D patterns, and 120 checked exceptional examples. It does not yet solve the 40 exceptional D for every remaining multiplicity choice or for all inactive sets M of size>1. The project-wide k=0 author-side upper bound remains 44. P000 signed Cell/branch/time/BRC source-residual equivalence remains a separate typed lift, and the older R762IR antecedent still needs independent mathematics review.

Next mathematical step: develop a compulsory-bridge (the four {0,1,c} supports) and local GF(2) parity certificate to cover the 40 exceptional D for every choice of remaining triple-support inventory, then continue to inactive Port sets of size≥2. No Task CLAIM, protected PROGRESS, or formal Result/Review admission is asserted.
