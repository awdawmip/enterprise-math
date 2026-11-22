# R762JP — Rainbow-tree parity repair; 44→42 all-Port theorem

Date 2026-11-23 Asia/Shanghai. Status AUTHOR_PROVED / EXACT_INTEGER_CHECKED / NOT_REVIEWED. Continuation of R762JO. Scientific input remains frozen; P000 is unchanged.

## Statement

Let A={0,...,5}; let P=C(A,2) be 15 pair-Ports, and S=C(A,3) be 20 support labels. An event of s joins two of the three Ports in C(s,2), with parallel edges permitted. An Euler witness means exactly specified local support multiplicities, connected graph on the active Ports and positive even degrees.

**Theorem.** Choose any three distinct labels D ⊂ S, assign c_s=1 to those labels, and independently assign c_s∈{2,3} to every other label. An Euler witness with ALL 15 Ports active exists, and the circuit may start at any p∈P.

**Corollary.** In the (6 triples,12 doubles,2 singles,0 missing) 44-event class, for every choice of six triple supports T, singleton supports U and any j∈T, reducing j from count 3 to 1 leaves three singles, twelve doubles and five triples, totaling 42 events. Therefore N_{p,P}(n−2e_j)>0 for every j∈T and p∈P. This does not require the 44-event witness as input: adding two parallel j-edges reconstructs one.

## Complete proof

Form G=J(6,2)=L(K6), with 15 Port vertices, degree 8 and 60 edges. Each graph edge belongs to exactly one of the 20 support triangles, so the edges have 20 colors.

**Cut claim.** Every nonempty proper X⊂P has edge boundary |∂X|≥8, with equality only when |X|=1 or 14. If B is the unsigned 6×15 incidence matrix of K6 then BBᵀ=4I6+J6 and adjacency(G)=BᵀB−2I15. Thus its eigenvalues are 8 once, 2 five times, −2 nine times. The Rayleigh inequality on the centered indicator of X gives |∂X|≥6|X|(15−|X|)/15. This exceeds 8 when 2≤|X|≤13; singleton and co-singleton cuts have exactly size 8 by regularity.

For any partition Π of P into q≥2 nonempty classes, let g(Π) be the number of support triangles meeting more than one class. Summing the cut lower bound on each class gives at least 4q crossing graph edges. One crossing support triangle contributes at most three graph edges, and exactly two when q=2.

For q=2, g≥4=q+2. For q=3, g≤4 would force exactly twelve crossing edges, each class having cut 8, which would force each class to be a singleton (no class can contain 14 vertices in a three-part partition); contradiction. Hence g≥5=q+2. For q≥4, g≥ceil(4q/3)≥q+2 (check q=4,5, then use 4q/3≥q+2 for q≥6). Thus g≥q+2 for every partition. After deleting ANY three support colors, at least q−1 distinct remaining colors cross every partition.

**Rainbow tree.** The remaining 17 colored triangle classes admit a spanning tree with 14 distinct colors. This follows from graphic/partition matroid intersection: for arbitrary edge subset F with q connected components, graphic rank is 15−q, and rank of the color partition matroid on E\F is at least q−1 because at least q−1 distinct colors cross the component partition. The matroid-intersection min–max theorem gives a common independent set of size ≥14, namely a rainbow spanning tree R.

**Parity realization.** Choose one arbitrary edge for each of the three singleton labels, yielding an even-weight GF(2) endpoint-boundary b. For each flexible support s of count 2 or 3, and any designated triangle edge e=(u,v), there are exactly count_s local edges with either zero parity or parity ∂e, preserving a connection between u,v:
- count 2: two parallel copies of e give parity 0; the other two sides of the triangle give parity ∂e and connect u to v through the third Port.
- count 3: one copy of each triangle side gives parity 0; three parallel copies of e give parity ∂e.

Designate e_s as the tree edge for the 14 distinct tree-colored flexible supports; use parity zero for the three flexible supports not in R. Since a tree's 14 edge boundaries form a basis for the even-weight GF(2) vectors on 15 vertices, uniquely choose which tree edges sum to b. Realize their supports with parity ∂e_s, all other flexible supports with parity zero. Total parity vanishes. Every tree edge's endpoints remain connected within its own support's edge realization, so the full multigraph is spanning and connected. All degrees are positive even, all support counts remain exact. Euler's theorem gives the asserted circuit for any start. QED.

## Recalculation, provenance, next unit

The Python standard-library checker R762JP_RAINBOW_PARITY_VERIFY.py enumerated all C(20,3)=1140 deleted-color sets, obtained a verified rainbow tree for every set, and produced exact 42-event witnesses for each of three distinguished deleted-triple choices: 3420/3420 PASS. Its independent 2^15−2=32766 cut enumeration found 30 singleton/co-singleton cuts of size 8 and minimum cut 14 for all other proper vertex subsets. Deterministic witness stream SHA-256: 987329223570b86051911fcbb85b907501e29c8cc14fb5f8d5d7fabed3a49c92. The proof does not depend on the heuristic candidate order of the tree finder. Evidence summary R762JP_EVIDENCE.json.

Predecessor: awdawmip/enterprise-math@f712e0bbe7ef895d94d2eb6b8b28847d653f91da:research_notes/portable_direct/R762JO_COMPLETE_T6D13_Z1_44_TO42.md (author-check only).

**Remaining problem:** extend the (6,12,2,0) reduction to inactive Port sets M≠∅, or construct a valid counterexample. When a support retains only two active Ports, a triple support can have forced odd parity and a double support forced zero parity; the all-active rainbow repair requires modification. The overall author-side k=0 bound remains 44. Native signed Cell/path/branch/time dynamics and BRC fidelity require a separate typed lift. No Task CLAIM or protected PROGRESS/Review is asserted.
