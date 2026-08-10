# R005-A — Repeated Forest + Squarefree Partial-Steiner Repair Normal Form

Status: `PROVED R005 STRUCTURE + EXACT CROSS-CHECK / NOT CANONICAL / LEAN PENDING`  
Date: `2026-08-10`

## 1. Normal form

On the fourth-root-forced square-basin slice, the residual support hypergraph is the non-forced induced shadow of the ambient closure complex:

`R_k = H_k[NF_k]`.

The new result is the stronger decomposition

`H_k = G_k^rep union T_k^sf`,

where `G_k^rep` is the repeated-prime 2-edge sector and `T_k^sf` is the squarefree rank-3 sector.

## 2. T-A34 — repeated ambient graph is a forest

For `A=k^2`, `U=k^2+2k` and prime `q>C4=floor(U^(1/4))`, define

`f_k(q)=oddFloor(U/q^2)`.

A directed repeated edge `q -> r` exists when `r=f_k(q)` is a distinct prime in the ambient shell and `A<q^2*r<=U`.

For fixed q the possible r interval has width `2k/q^2<2`, so directed outdegree is at most one. The map `f_k` is nonincreasing because `U/q^2` decreases with q.

Any periodic orbit of a nonincreasing map on a total order has period at most two: the minimum orbit value maps to the maximum and the maximum maps back to the minimum. A fixed point is `q^3`, a singleton support rather than a repeated 2-edge. A 2-cycle `p<->q` would put both `p^2*q` and `q^2*p` in the same square basin. Their square roots differ by

`sqrt(pq)(sqrt(q)-sqrt(p)) >= sqrt(p) > 1`,

impossible inside the root interval `(k,k+1)`.

Any undirected cycle would orient to a directed cycle because each edge has one repeated-factor tail and each cycle vertex has total directed outdegree at most one. Therefore `G_k^rep` is a forest.

Exact ambient example at `k=196`: `41 -> 23 -> 73`, since `41^2*23=38663` and `23^2*73=38617` lie in the same square basin. Paths can occur; cycles cannot.

## 3. Squarefree sector

Ambient linearity implies every unordered witness pair lies in at most one squarefree block. Hence the rank-3 squarefree sector `T_k^sf` is a partial Steiner triple system in the standard combinatorial sense. This is prior combinatorics terminology, not a novelty claim.

Thus the ambient arithmetic closure complex is exactly a forest-plus-partial-Steiner mixed linear hypergraph, and the residual object preserves this structure after induction on `NF_k`.

## 4. T-A35 — local obstruction to repair number > 1

For any nonempty linear hypergraph L,

`tau(L)>=2`

iff either:

1. two blocks are disjoint; or
2. three blocks form a Berge triangle: pairwise intersections exist, but the three intersection vertices are distinct.

Proof: if no two blocks are disjoint, choose `E1,E2` with intersection `{x}`. Since no universal hitting vertex exists, choose `E3` omitting x. Pairwise intersection supplies `y in E1 cap E3` and `z in E2 cap E3`; linearity forces x,y,z distinct.

## 5. T-A36 — repeated-only repair is forest vertex cover

If the residual shadow has no squarefree 3-edge, it is a subgraph of the repeated forest. Therefore minimum repair is minimum vertex cover of a forest. Classically, forests are bipartite, so Konig gives equality with maximum matching.

Consequently, in a repeated-only basin:

`tau(R_k)>=2 iff two vertex-disjoint repeated residual edges exist`.

The Berge-triangle obstruction cannot occur in a forest.

## 6. T-A37 — exact squarefree-parameterized repair

Suppose residual `R_k` consists of a repeated forest G plus `s` squarefree residual triangles `T_1,...,T_s`.

For each choice function selecting one vertex from every triangle, let S be the union of selected vertices. S hits every squarefree block. Remove from G every repeated edge already hit by S and call the remaining forest `G_S`.

Then

`tau(R_k) = min_S ( |S| + tau(G_S) )`,

where the minimum ranges over at most `3^s` triangle-choice functions. `tau(G_S)` is computed by ordinary tree dynamic programming.

Hence the exact repair problem is fixed-parameter tractable in the number s of squarefree residual triangles:

`O(3^s * poly(v))`.

This is not a new generic FPT theorem; the R005 result is the arithmetic reduction to this forest-plus-triangle form.

## 7. Search consequence

A first basin with repair number at least two must contain either:

- two disjoint residual blocks; or
- a residual Berge triangle that necessarily uses at least one squarefree 3-edge.

So the next search should target those local obstruction configurations, not arbitrary residual hypergraphs or another undifferentiated composite cutoff.

## 8. Exact cross-check

Current 49 exact no-least basins:

- ambient repeated edges: 148;
- ambient squarefree triangles: 2349;
- residual repeated edges: 45;
- residual squarefree triangles: 5;
- every ambient and residual repeated graph passed the forest check;
- the `3^s` branch+forest-DP repair algorithm exactly matched brute-force transversal number in every basin;
- only 59 triangle-choice branches were needed across the whole current certificate family.

Finite small s is evidence only, not a theorem.

## 9. Prior-art boundary

Forests, vertex cover, matching, Konig's theorem, partial Steiner triple systems, Berge triangles and parameterized branching are prior mathematics. Candidate R005 content is the exact arithmetic reduction from square-basin witness residuals to this mixed closure normal form. Novelty of the packaging remains unverified.
