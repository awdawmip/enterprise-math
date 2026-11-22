# R762IX — Complete 47→45 theorem for (10 triples, 8 doubles, 1 single, 1 absent)

Date: 2026-11-22, Asia/Shanghai. Frozen science: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Status: AUTHOR_PROVED / TWO_EXACT_INTEGER_CERTIFICATES + EXHAUSTIVE_CLASSIFICATION / NOT_REVIEWED.

## Theorem

Within the **composite Port–Euler** model of R762IW (not the native signed P000 dynamics), let 20 three-axis supports have counts (3,2,1,0) with exactly ten supports of count 3, eight of count 2, one of count 1, and one absent. Thus the total is 47. If a legal connected even-degree closed Port multigraph exists on exactly active set V with chosen start p∈V, then there exists a legal 45-event multigraph on the same V with the same p and positive support labels, obtained at the histogram level by changing **one** 3-count to 1 and no other count. Every support count parity is unchanged.

This completes the entire terminal multiplicity class (t,d,s,z)=(10,8,1,1), including both connectivity-essential and non-essential ten-triangle systems and arbitrary realizable active Port sets.

## Reduction lemma proved here (no prior global induction assumed)

Let T be the ten 3-count supports. If some j∈T has exactly two active Port vertices, all its three events in the original graph use the unique permitted edge. Removing two parallel copies preserves underlying connectivity, positive even degree and V; the histogram is reduced to 45. No part of the other-support allocation changes.

Otherwise **each** support in T has all three vertices active. Form the graph G(T) on the 15 Port vertices from the three possible edges of every triangle in T. If some j∈T is not connectivity-essential in G(T), remove j's triangle from this union; its three vertices remain mutually connected in G(T\{j}).

For a three-event support with active triangle vertices (u,v,w), define the mod-2 degree boundary β∈F₂^{V}. It can be any of 0, e_u+e_v, e_u+e_w, e_v+e_w, and **each** of those four boundary choices has a local 3-event allocation connecting all three vertices: for 0, use the three distinct triangle edges; for e_u+e_v, use one uv edge and two uw edges, and relabel for other pairs. Consequently each retained support i∈T\{j} may be reassigned with any chosen even boundary on its own three vertices, while all three Port vertices remain locally connected.

Replace all three events of j with one event on any edge uv of j. Let δ be (old β_j) + (e_u+e_v), in F₂; δ is zero or the two-vertex boundary e_s+e_t on j's triangle. If δ≠0, choose a path from s to t in G(T\{j}); for each of its edges choose one supporting triangle i∈T\{j}, assigning that edge boundary to i. The sum of the assigned boundaries telescopes to δ. Within each i, the sum δ_i of its assigned edge boundaries is again one of the four even local boundaries, so reassign its three edges with boundary old β_i+δ_i using the connected allocations above. Supports outside T retain their original allocations.

The total change in vertex degree boundary is δ + Σ_i δ_i = 0, so every final degree is even. Each retained triple triangle now locally connects all its three vertices, which preserves at least the old reachability relation of that triple. The removed j triangle's vertices are already connected through the retained triple triangles. All other support edges are fixed, so the global connected component relation of the original active graph cannot split. No inactive vertex receives any event; every originally active vertex remains active. Every count is unchanged except n_j:3→1. Hence the 45-event graph is legal and Eulerian from any p∈V.

## Discharge the all-essential branch

If no two-active-Port triple exists and **every** j∈T is essential in G(T), apply the independent exhaustive integer classification in R762IX_TEN_TRIANGLE_CLASSIFY.py: among all C(20,10)=184,756 ten-support families, exactly six are all-essential, precisely the six full axis stars T_a={S: a∈S}. The entire domain, predicate, union-find algorithm and six exact masks are recorded in R762IX_STAR_CLASSIFICATION_ADDENDUM.md.

For a star T_a, all 15 Ports are active if all ten star triangles have three active vertices, since their union covers every Port. The independent constructive star theorem in R762IX_STAR_TEN_TRIPLE_47_TO_45.md applies: under S₅, the ordered pair of the absent nonstar support z and singleton nonstar support q falls into exactly two orbits (intersection 1 or 2). Its 60-entry integral witness for each orbit is explicitly checked, and all 540 axis-labeled all-active cases are exhaustively verified by R762IX_STAR_TEN_TRIPLE_VERIFY.py (Python standard library). Therefore some triple support again reduces 3→1 while preserving V, p, connectedness, even degrees, positivity and parity.

The cases (a triple has two active vertices; a full triple non-essential; all full triples essential) are exhaustive. This proves the stated (10,8,1,1) theorem.

## Proof boundaries and next unit

This is a complete written and computer-assisted argument for the **one specified** 47-event multiplicity class, not for the entire 47-event frontier. The other open terminal classes include (8,11,1,0), (9,9,2,0), (10,7,3,0); the seven-triple (7,13,0,0) and nine-triple/one-absent (9,10,0,1) branches have earlier authored evidence. Global k=0≤46 is **not established by this note**, and the separately asserted k>0 bound and the signed P000 triadic dynamics remain different questions. Independent mathematical Review is pending.

Next: apply the same explicit parity-repair lemma and orbit-compressed integer certificates to the unresolved terminal classes, starting with (10,7,3,0), checking the exact active set and singleton supports without assuming a global result.
