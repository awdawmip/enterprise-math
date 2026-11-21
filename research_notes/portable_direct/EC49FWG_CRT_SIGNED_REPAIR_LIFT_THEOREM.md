# EC49FWG — Exact CRT lifting of signed ten-cycle repair graphs

Date: 2026-11-22 (Asia/Shanghai). Scientific status: AUTHOR_PROVED / EXACT_FINITE_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED. Independent portable research; no official CLAIM, Result or Review.

## Frozen input and provenance

Scientific pin: BRC16943, unchanged. Parent EC49FWF: awdawmip/enterprise-math@a9255c8a590baa84c01805f8f41b1b271b3442d6:research_notes/portable_direct/EC49FWF_SIGNED_REPAIR_GRAPH_THEOREM.md. Earlier exact mod-110 CRT reduction: EC49FWA@44f3d0c2b34267dddac7816edc8706da1f00f1ee. P000/ACTIVE and the Bernoulli-to-projective parent reduction retain their frozen meanings.

For primitive integer direction (a,b) and a base point with (b-a)h0-a n0=-1 mod 110, define the original frozen auxiliary certificate word
\[
W(t)=U(t\bmod10)V(t\bmod11),\quad t\in\mathbf Z/110,
\]
where U(t)=1 if and only if (h0+at,n0+(b-a)t) belongs to the frozen 44-cell P10, and V(t)=1 if and only if 9(h0+at)+10(n0+(b-a)t) is nonzero mod 11. When 11 divides (a+b), V=1 identically. Otherwise V is the 11-position word with a single excluded position z. Let F=|V|, so F=11 or 10.

For a binary cyclic support S, define d_m(S)=min_c |S triangle (c-S)| and optimal centers C_m(S). When d_10(U)=2, each optimal center gives a directed mismatch pair p->q, p occupied and q unoccupied. Let G10 be the union of these edges. EC49FWF proves exhaustively that G10 is a forest of shape P2, 2P2 or 2P3 for the frozen nonreflective directions.

## Theorem 1 — Full CRT signed-graph lifting

For every frozen primitive direction with d_10(U)=2:

(1) **Exact minimum:** d_110(W)=2F.

(2) **All minimizing centers:** if F=10, C_110(W) consists exactly of centers whose mod-10 residue is in C_10(U) and whose mod-11 residue equals 2z. If F=11, every mod-11 center combines with every optimal mod-10 center.

(3) **All-center graph for F=10:** the full directed signed graph is precisely TEN disjoint copies of G10. Its graph shapes are accordingly 10P2, 20P2, or 20P3. It remains a forest.

(4) **All-center graph for F=11:** the full graph is the 11-fold complete bipartite blow-up of G10. Replace each original vertex p by the eleven mod-11 sites (p,u); every oriented edge p->q is replaced by every one of the 121 edges (p,u)->(q,v), u,v in F11. Therefore, whenever d_10=2, the full graph contains four-cycles: **the global all-optimal-centers forest property of EC49FWF is not preserved by full CRT coupling**.

**Proof.** CRT separates intersections:
\[
|W\cap(c-W)|=|U\cap(c_{10}-U)|\cdot|V\cap(c_{11}-V)|.
\]
For U with d_10=2, max intersection equals |U|-1. If V=1, intersection always equals 11. If V has one excluded z, the unique center c11=2z gives intersection 10; every other center gives 9. Positivity of |U|-1 yields exactly the centers in (2) and d_110=2F. At any minimizing center, the V-factor is preserved under reflection and
\[
W\triangle(c-W)=(U\triangle(c_{10}-U))\times V.
\]
Each base signed edge p->q lifts exactly to the edges
\[
(p,u)\longrightarrow(q,c_{11}-u),\qquad u\in V.
\]
For one-hole V the involution u->2z-u has five two-element orbits on the ten allowed positions. Because G10 is bipartite, each pair induces two disjoint copies of every base tree, hence ten copies. For constant V, the eleven allowed c11 generate all possible u,v pairs; every base edge gives K11,11, which contains a four-cycle. QED.

For d_10(U)=0, d_110=0, the same mod-11 center rules lift optimal symmetries, and the signed mismatch graph is empty.

## Theorem 2 — Minimum repair cost and information multiplicity

Fix any ONE optimal full center c in the nonreflective case. The 2F mismatching sites comprise exactly F disjoint two-element reflection orbits, each with one occupied and one empty endpoint. The minimum number of single-site flips required to make W symmetric about c is therefore exactly **F**. The complete family of minimum repairs has cardinality **2^F**: independently choose which endpoint of each mismatched orbit to flip.

Exactly TWO of these 2^F repairs retain the factorized form U' x V with the same mod-11 factor V: flip the entire allowed V-fiber at either of the two P10 mismatch sites. Proof: one flip per mismatching orbit is necessary and sufficient; factor preservation forces all F bits in any ten-coordinate fiber to change together. At minimum cost, only one of the two mismatching ten-coordinate fibers can be toggled. QED.

Thus the compact base signed edge plus the mod-11 factor reconstructs the full family of mismatches, while selecting one repaired state discards 2^F-way choice information. For F=10 this is 1024 choices; for F=11 it is 2048. A one-bit P10 repair is not a one-bit full-C11 repair.

## Concrete witness and complete class counts

For a/b=1/10, F=11, d10=2 and the base graph is P2; the full 110-word has d110=22, eleven optimal centers and an all-center signed graph K11,11: **22 vertices, 121 edges**. This is a fully specified counterexample to unrestricted forest lifting. For a/b=1/7, F=10, d10=2 with two optimal centers, d110=20 and the full graph is 20P2. For a/b=1/2 both defects vanish.

The parent 72-class exact census is: perfect d10=0: 8; d10=2 with one center: 24; two centers: 24; four centers: 16. Every primitive mod-10 class has 110 one-hole mod-11 primitive lifts and 10 constant mod-11 lifts. Consequently the complete 8640 primitive mod-110 classes split into: perfect 880 one-hole / 80 constant; one-center nonreflective 2640 / 240; two-center nonreflective 2640 / 240; four-center nonreflective 1760 / 160. These are residue-direction class counts, not natural-height densities.

## Exact verification and next question

Companion runnable self-contained JavaScript verifier EC49FWG_CRT_SIGNED_REPAIR_LIFT_VERIFY.js reconstructs P10 from its previously verified four slope fibers, checks 44 cells, all 72 primitive mod-10 directions, and independently scans complete 110-site masks, all optimal centers, and all signed mismatch edges for eight rational anchors. It checks the K11,11 edge set directly. Result: ALL PASS. A separate Python checker reconstructed the same 72-class census and tested all eight 110-site masks and CRT graph components with exact modular integer arithmetic, also returning ALL PASS.

Theorem 1 is an analytic CRT proof contingent on the inherited frozen P10 identity; Theorem 2 is a direct orbit proof. No global Farey asymptotic, native X6 dynamics, or independent proof review is asserted.

Next: determine the minimum exact modifications that preserve ALL optimal-center symmetries simultaneously, including equality-orbit constraints outside the signed mismatch graph; then test whether the lifted graph observer yields a quantitative moving-Farey interval bound. A mismatch-edge vertex cover alone is insufficient without enforcing previously equal reflected pairs.

## Control and attribution

Prior researcher EM-DIRECT-7A9ACD / Activity RA-3F60061B277C73CFD4378C57 remain original-provenance labels until current logical-session authority to mutate that Activity is confirmed. Native exact task read for topic RS-EC49AS reports NO_CANONICAL_PUBLICATION_DIRECTORY at Source 505ce43b94366e00d5fdf5bea41b93126435e6b4, not shared CLAIM authority. Preserve original events, attribution, and review status.