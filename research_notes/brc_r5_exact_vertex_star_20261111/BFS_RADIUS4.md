# R5 — Exact radius-four vertex-neighborhood exploration

Date: 2026-11-11 (Asia/Shanghai). In the **fixed** physically lawful 15-dimensional Blackwell fiber from RESEARCH.md, the full adjacency enumeration can be applied recursively using exact rational pivots. Radius is measured in the 1-skeleton graph from the pinned 14-positive-arc vertex X.

The executed SEARCH_BFS_DEPTH4.py checks the exact C matrix and all kernel directions, positive first-boundary steps, observer equality and unique rational vertex coordinate tuples. It enumerates **all** neighbors for vertices of support 14 or 15, the only support sizes encountered up to radius four. The cumulative number of distinct vertices within graph distance at most 4 is **1775**. Of these, **171** have 14 positive arcs and **1604** have 15 positive arcs. Each graph layer was fully expanded, and the exact output is saved in BFS_RADIUS4_OUTPUT.txt.

Layer 0: one 14-arc vertex. Layer 1: 18 new (10 support-14, eight support-15). Layer 2: 152 new (40,112). Layer 3: 594 new (66,528). Layer 4: 1010 new (54,956). The counting covers this bounded ball, not the entire finite fiber. No vertex with 13 or fewer positive arcs appeared in these 1775 exact candidates.

The step uses only rational Blackwell auxiliary calculations, keeps the original frozen scientific pins and prior published witness, and does not alter Source P000. Continued question: reach a 13-arc vertex elsewhere, or derive a global 14-arc support lower bound via exact support-matroid / affine-position certificate. A complete global enumeration may also classify all vertex degrees and larger circuits.
