# R762IJ — 62-event subwitness for the six-axis composite Port Euler model

Date: 2026-11-22 (Asia/Shanghai). Mathematical status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**.

## Source and exact statement

Frozen task RS-X6-TRIADIC-CLOSURE-DYNAMICS, scientific pin a72226e2430ffa4786321ac86e7f0c599d5f0389. Predecessor: R762II at 5ca203b040c2d42b201be366c5cec21ffa84f59a, whose reduction depends on R762IH at 5f39e2e5faac0b3e8fb358d810eb8d0477e5d612.

The 15 Port vertices are the unordered pairs ij of six native axes. A triple support ijk permits any of three edges of the Port triangle with vertices ij,ik,jk. For every nonempty support histogram n admitting a connected even-degree (Eulerian) Port multigraph with a specified active start p, there exists a subhistogram h obtained by deleting pairs of events of the **same** support such that:

- The positive supports, count parity of each support, active Port vertices and specified start p are preserved.
- Each h_S is at most four.
- The total satisfies the **new upper bound**

\[
\boxed{\sum_{S\in\binom{[6]}3} h_S\le 62.}
\]

Conversely deleted pairs may be reinserted on already occupied permitted Port edges, preserving Euler legality. The subhistogram is witness-dependent; there is no claim of an arbitrary histogram-wise canonical cap of total 62. History multiplicity, ordering, Cell signed displacement, BRC weights, native time/force/rotation and arbitrary future observers are not retained by this reduction.

## Proof

The already proved R762IH pair-deletion lemma yields a reduced connected Euler realization with every support count at most four. Every support still occurring four times has exactly the pattern (2,2,0) on two Port triangle sides, and **both occupied sides are bridges** of the underlying simple Port graph. Call these k supports critical. No Port edge belongs to two supports, so their 2k bridge edges are distinct. Write t<=20 for the positive support types, e>=k for even-count positive supports. The count is bounded by

\[
|h|\le3(t-e)+2(e-k)+4k=3t-e+2k\le3t+k. \tag{1}
\]

R762II's induced-edge packing bounds give for k=4,5,6,7 respectively 61,50,33,28. For k=0,1,2 the unconditional t<=20 gives 60,61,62. The sole possibility producing the prior maximum 63 is **k=3,t=20**. We rule it out.

Assume k=3 and every one of the 20 supports is positive. Remove the six critical bridge edges. Exactly seven connected components remain; use these as colors of the 15 Port vertices. The three vertices of each critical support's Port triangle have three different colors: otherwise one of its two positive bridge edges could be bypassed. Six removed bridges connect the seven components as a tree. In the bipartite graph of component-color nodes and three critical-support nodes, each critical support is incident to its three triangle-vertex colors. This incidence graph must be a tree (7+3 nodes, nine incidences, connected), and hence a forest.

Every noncritical positive support has at least one occupied edge entirely within a component, because none of its edges was among the removed critical bridges. Consequently each of the other seventeen Port triangles has an **equal-color pair**.

These are necessary conditions on an equivalence relation among 15 vertices:

1. In each of the 17 noncritical Port triangles, at least one pair of vertices must be identified.
2. In each of the three critical Port triangles, the three colors must be distinct.
3. The critical-to-color incidence graph must be acyclic.
4. At least seven classes must remain during any sequence of identifications.

An exact standard-library Python enumerator (R762IJ_CHECK.py) tests this finite system. Begin with 15 singleton classes. Select an unsatisfied noncritical triangle, branch over each of its three possible pair-identifications, and memoize the resulting full 15-coordinate equivalence partition. Reject whenever fewer than seven classes remain, a critical triangle repeats a class, or the critical incidence graph acquires a cycle. Each rejected condition is monotone under further identification and hence sound. Every satisfying final partition would have to follow one of these branches. The checker accepts a *relaxed* necessary terminal, even without requiring exactly seven final classes; if not even the relaxed terminal exists, the desired Port graph is impossible.

There are C(20,3)=1140 possible sets of three critical supports. The 720 permutations of the six axes partition these sets into exactly seven orbits. The checker derives these orbits and checks a representative of each.

| Critical triples (representative) | Orbit size | Memoized states | Necessary system feasible |
|---|---:|---:|---|
| 012,013,014 | 60 | 1,947 | No |
| 012,013,023 | 60 | 1 | No |
| 012,013,024 | 360 | 1,944 | No |
| 012,013,045 | 180 | 2,677 | No |
| 012,013,234 | 180 | 340 | No |
| 012,013,245 | 180 | 3,394 | No |
| 012,034,135 | 120 | 2,741 | No |

The orbit sizes sum to 1140 and the memoized-state total to 13,044. A second traversal of the noncritical constraints in reverse order independently returns no admissible case. Therefore k=3 with t=20 cannot occur. For k=3 one must have t<=19, giving |h|<=3*19+3=60 from (1). Combining all k cases proves **62**. QED.

## Reproduction and limitations

Run the sibling Python 3 checker using the standard library. Its terminal result is “PASS R762IJ: k=3, all 20 supports is impossible”. The exhaustive search proves a necessary component-coloring obstruction, rather than enumerating Euler circuits, so its negative answer suffices. Dependencies on R762IH's pair-deletion theorem and R762II's packing bounds are cited at their original scope; no new independent review has occurred.

**Unresolved:** sharpness of the absolute 62-event bound, and a histogram-only constructive Euler solution/certificate. The k=2, t=20 critical-support coloring condition may be satisfiable; this checker does not rule it out. A useful next step is to impose full even-degree constraints and actual internal-component connectivity on that case. P000's native TRIADIC_CLOSURE_E interpretation remains a separate type-preserving lift problem.

## Control provenance

An exact native continuation read with request r3-20261122-0523-x6-cont-v1 returned FAILED / SOURCE_TREE_TRUNCATED. Current owner and CLAIM could not be verified. Previous Researcher EM-X6-A681A5 and SID MCP-773502d89b7a4bd58a37e97a2dd52ba5 are historical provenance only, not current execution authority. This is an independently preserved portable source, **not** native PROGRESS, Result, Review or P000 promotion.
