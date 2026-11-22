# R762IY addendum — Two-leaf GF(2) repair for nine-triple star-minus-one families

Date: 2026-11-22 (Asia/Shanghai). Model and frozen pin are as in R762IY_STAR_LEAF_47_TO_45.md. Status: AUTHOR_PROVED / EXACT_CONSTRUCTIVE_FINITE_CHECK / NOT_REVIEWED.

## Theorem: the 60 star-minus-one families of (9,9,2,0)

Let A be the six axes, Ports its 15 two-subsets, and supports its 20 three-subsets. Fix a center axis c and one omitted star support L={c,a,b}. Suppose precisely the other nine c-containing supports T={S:c∈S}\\{L} have event count 3, while each of the other eleven supports has count 1 or 2 (exactly two of those eleven have count 1). This is the 47-event histogram (t,d,s,z)=(9,9,2,0).

**If a legal connected even-degree Port realization exists with prescribed active set V and start Port p, there exists a legal 45-event realization on precisely V**, keeping all positive support types and every support-count parity and reducing one of the nine triple supports from 3 to 1.

For these star-minus-one triple systems, either a triple has only two active Ports and parallel-pair deletion works, or all nine triple triangles have their three Ports active. In the latter case the union of the nine triple supports contains exactly 14 distinct Ports; thus V is either all fifteen Ports or all except the single peripheral leaf v_L={a,b}. Both cases are included.

## Analytic two-leaf construction

Relabel c=0. Choose **any** J={0,r,s} in T and let v_J={r,s}; the omitted star L={0,a,b} has leaf v_L={a,b}. The eight retained three-event star supports T\\{J} form a connected triangle-edge graph on W=Ports\\{v_J,v_L} with 13 vertices. Indeed, on the five central Ports 0i, their edges are K5 minus the two edges corresponding to J and L, which remains connected. Every other peripheral Port ij attaches via its surviving triangle to 0i and 0j.

Prescribe the active set from the original realization: v_J is active, while v_L may be active or inactive. Replace J by one edge joining v_J to a central Port. If v_L is active, allocate the (one or two) events of L so that one edge joins v_L to a central Port and any second edge lies between central Ports. If v_L is inactive, allocate every L event between central Ports, never touching v_L. All other required active Ports lie in W.

Each leaf v among {v_J,v_L} belongs to **three** nonstar supports on the five axes different from 0. There is a positive nonstar support Q_v containing v but not the other leaf: if the two leaves share one axis, exactly two such supports exist for each; if the leaves are disjoint, all three are private. Choose a different private support for each leaf that is required active. All ten nonstar supports have positive multiplicity (one or two), so these choices exist.

Allocate all nonstar supports except the chosen private supports along any allowed edge that avoids the possibly inactive v_L. For each active leaf v, compute the parity b_v of its degree after the existing edges. If b_v=0, allocate all m events of Q_v along the edge between Q_v's other two Ports, avoiding v; if b_v=1, allocate one Q_v event from v to one of those two Ports and its remaining m-1 events along the opposite edge avoiding v. The chosen Q_v does not contain the other leaf, so this changes only its own target leaf parity. This makes the parity at every missing-star leaf zero and leaves any inactive v_L at degree zero.

Since the overall boundary of an undirected multigraph is even and both leaf parities are zero, the remaining degree defect on W is an even GF(2) vector. The eight retained star triangles span a connected edge graph on W, so their edge boundaries generate every even vector there. Route the parity defect along W paths and group the contributions by triangle. Every locally even triangle boundary (zero or two endpoints) is realized by **three edges that connect all three triangle Ports**: the 3-cycle for zero, or one edge between the two odd Ports plus two parallel edges joining one odd Port to the third Port. Thus the eight retained triple supports can be reassigned to cancel all remaining odd degrees without changing counts or connectivity.

The resulting multigraph has exact event count 45, all required Ports positive with even degrees and connected, with no incidence at any prohibited Port. Therefore it has an Euler circuit from the original p. The proof is constructive for arbitrary specified V allowed by the premises.

## Coverage and role in the unresolved frontier

There are six center axes and ten choices of omitted star L for each, giving **60 distinct axis-labeled triple-support sets**; exactly the 60-member all-essential orbit already found in R762IW/R762IX. For each, the active-set possibilities in the full-triple case are V=15 Ports or V=14 Ports excluding v_L. The previous parallel-pair and nonessential-triangle lemma handles the other two structural branches.

The independent `R762IY_TWO_LEAF_VERIFY.py` covers both relative positions of J and L (adjacent or disjoint as edges on five noncentral axes), both active-set choices, and all C(11,2)=55 placements of the singleton supports among eleven nontriple supports: **2×2×55=220 exact certificate tests**, each with the support-count vector, positive even degree, active set and connectedness verified. All 220 passed; the number of distinct used edge types ranged **31–36**. Axis permutations extend the checker representatives to all 60 star-minus-one families, but the written construction itself already covers them universally.

The 180-member other all-essential nine-triangle orbit remains unresolved for (9,9,2,0), as do some eight-triple structures in (8,11,1,0). **No global k=0≤46 claim** is made by this addendum. Next: study the 180-member orbit's exact active-Port admissibility and connection-repair obstructions, preferably first as a structural theorem rather than a large integer-program batch.

Scientific status: author-proved composite Port–Euler observer result; predecessor all-essential classification relies on the existing exact finite enumeration; independent Review not performed. No protected Task CLAIM or PROGRESS.
