# R5 — Exact overlapping bridge graph and triangle-chain repair

Date: 2026-11-15. Frozen scientific pin: 435e77af0d180eac32bd1f9c4c464bc4010b7551.
Evidence: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Prior: research_notes/portable_direct/r5_overlap_bridge_chain_20261115/BRIDGE_RESOURCE_SPECTRUM_AND_PROVENANCE_THEOREM.md at a983257c1163c68a4d729d4343a6ddc1a6cf56e6.
Scope: the inherited auxiliary R5 indexed-center radius-2 one-step replacement observer; these suffixes are not native X6 coordinates.

## Definitions and general theorem

Old indexed cores O0=0125, O1=0135, O2=0235, O3=0245, O4=0246.
New a cores and first bits: (1235,1),(1245,1),(1246,1),(1345,0),(1346,0). New ab additionally contains (1236,1).
For target (C,t,y) and old source (Oj,s,x), define
rho=|C\Oj|+[t!=s]+Hamming(y,x); a source repairs its target iff rho<=2.
Labels (j,s,x) are preserved throughout.

For any finite simple graph G=(V,E), V={0,...,d-1}, nonempty E, and available helper vertices W subset V, encode each edge uv by its two-hot word e_u+e_v and each vertex v by its one-hot word e_v. Let Y_G be all edge words, H_W all singleton words from W, and X=Y_G union H_W. Define E[V\S] as the edges with both endpoints outside S.

**Theorem 1.** For every such G,W:
~~~
kappa_a(X,Y_G;2) = |E| + min_{S subset W} [2|S|+|E[V\S]|].
kappa_ab(X,Y_G;2) = 2|E|.
~~~
The second equality is the inherited joint-closure rigidity for any Y subset X; it is reused at its original scope.

**Exact proof of the first equality.** Every edge word y has a new target (1346,0,y). The old-core distance row (3,2,3,3,2) forces at least one baseline old source at this exact suffix, either (O1,0,y) or (O4,0,y). Other target suffixes are Hamming-distance at least 2, while a one-hot helper is distance 1, so none can supply the forced baseline. Consequently |E| distinct baselines are unavoidable.

For that same y, let B=(1245,1,y), C=(1246,1,y), D=(1345,0,y). The O1 baseline misses B,C; the O4 baseline misses B,D. An additional source at another edge word cannot repair these (new/old core distance at least 1 plus suffix distance at least 2). At Hamming distance 1, any individual one-hot helper source covers at most one of B,C,D: its old core and first-bit terms leave at most one unit, and their exact five-core comparison separates these three types. This separation is uniform across all y.

Given any old library, let F be the set of edges with no additional source at their own suffix beyond the designated baseline. Each edge outside F costs at least one further same-suffix source. For every edge in F, at least one B-type helper and one different C/D-type helper must be chosen, both at incident vertices. The B-source vertex set and the C/D-source vertex set separately cover all edges F, and their source types are disjoint. Thus the number of helper resources is at least 2 tau_W(F), where tau_W(F) is a minimum W-restricted vertex cover (infinity if impossible). Hence the extra-source count is at least
~~~
min_{F subset E} (|E\F|+2 tau_W(F)).
~~~
This equals min_{S subset W}(2|S|+|E[V\S]|): an F-cover S makes every edge outside E[V\S] incident to S, so E[V\S] subset E\F; conversely for any S take F to be all incident edges.

For the reverse inequality, pick an optimal S. Save (O1,0,y) for all y in Y_G; add (O0,1,e_v) and (O4,1,e_v) for every selected v in S; add (O0,1,y) on each edge y whose endpoints are both outside S. The baseline repairs targets 1235,1345,1346. A selected incident helper pair repairs 1245 and 1246, while the one extra local O0 resource repairs both on an uncovered edge. The source count is exactly |E|+2|S|+|E[V\S]|. QED.

This is a **source-aware exact graph incidence kernel**: G and available helper IDs determine the one-step optimum and reconstruct labeled optimal old resources. Cardinality-only graph isomorphisms need not preserve source identity when returning actual witnesses.

## Connected triangle-chain theorem

For integer k>=1, take vertices v_0,...,v_k, w_1,...,w_k. Triangle i has edges v_(i-1)v_i, v_(i-1)w_i, v_i w_i. There are 2k+1 suffix bits, 3k edge targets, and all singleton helper vertices are available. Consecutive triangles genuinely share a vertex, so the associated helper's target neighborhood crosses two triangles; no separating guard block is used. This corresponds to suffix length m-1=2k+1 (m=2k+2) in the inherited family.

**Theorem 2.** For all k>=2:
~~~
kappa_a = 5k;    kappa_ab = 6k.
~~~
For k=1, both equal 6. The exact single-a improvement over retaining no helpers is k for k>=2.

Proof: Any selected vertex of degree <=2 costs two sources and covers at most two edges, so some minimum S omits all w_i and endpoints v_0,v_k. Write s_i=1 if internal v_i is selected and s_0=s_k=0. The additional-source cost is
~~~
2 sum_(i=1)^(k-1) s_i
+ sum_(i=1)^k [3-2(s_(i-1)+s_i)+s_(i-1)s_i]
=3k-2 sum_(i=1)^(k-1) s_i + sum_(i=1)^(k-2) s_i s_(i+1).
~~~
If the selected internal vertices number t and form r runs of consecutive ones, the discount from 3k is t+r (because there are t-r adjacent selected pairs). If t>0, r<=(k-1-t)+1, so discount <=k. Choosing every internal vertex achieves t=k-1,r=1 and discount k. For k=1, no internal vertices exist. Adding the 3k unavoidable baselines gives the assertion. QED.

**Canonical witness multiplicity.** The optimal paired-helper constructions supported solely on internal v_i correspond, for k>=2, to binary strings length k-1 that begin/end with 1 and have no adjacent zeroes. Their count is Fibonacci F_(k-1), with F_1=F_2=1. This counts this explicitly defined witness class, not all optimal libraries.

## Provenance-preserving two-state min-plus kernel

For arbitrary available helpers W, let a,b,c in {0,1} encode selection of v_(i-1), v_i, w_i. Values 1 at unavailable vertices are forbidden. With D_0(a)=2a, update
~~~
D_i(b)=min_(allowed a,c) [
 D_(i-1)(a)+2b+2c+
 (1-a)(1-b)+(1-a)(1-c)+(1-b)(1-c)
].
~~~
The answer is kappa_a=3k+min_b D_k(b). Induction over triangles identifies each transition with the new vertex costs and exactly the three uncovered edges of that triangle. Hence this is an exact constant-state transfer for the size-only observer; keeping argmin predecessor pointers and the selected vertex IDs reconstructs an actual source-labeled library. The state cost is O(k) for a k-triangle chain, with witness output size O(k).

## Verification and open frontier

Companion Python and JSON verify the original exact indexed-core radius-two cover directly, exhaustive graph minima k=1..7 (8+32+128+512+2048+8192+32768 graph subsets), and all 680 helper-availability languages k=1..4 against the min-plus transfer. The single-a results k=1..7 are 6,10,15,20,25,30,35; inherited joint-ab results 6,12,18,24,30,36,42. An independent SciPy HiGHS mixed-integer set-cover check on the actual original labeled resource-target matrix returns the same primal/dual optimum for a and ab at k=1..4; the universal proof is the exact combinatorial argument above. These are declared finite checks and independent review remains pending.

Next mathematical question: whether provenance-aware transfer extends to cycles, unbounded-treewidth incidence graphs and multiple sequential target evolutions; the two-state recurrence applies to this explicit one-step triangle chain. P000/ACTIVE residual fidelity and native X6 three-dimensional-slice semantics remain unchanged.
