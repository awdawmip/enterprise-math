# R5: cyclic overlapping-triangle bridge, exact availability residual and future-observer lower bound

Date: 2026-11-15. Frozen scientific pin: 435e77af0d180eac32bd1f9c4c464bc4010b7551.
Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Scope: the **auxiliary** R5 indexed-center one-step radius-two replacement observer. Suffix binary indices are not native X6 Cell addresses. P000 and the frozen input are not modified.

## Model and exact prior theorem

Reuse the source-aware graph-incidence theorem proved in research_notes/portable_direct/r5_overlapping_triangle_chain_20261115/OVERLAPPING_TRIANGLE_CHAIN_EXACT_KERNEL.md at commit c177b61d1f8fd899038a91f5ecb6e99390890bce. The five old cores are 0125, 0135, 0235, 0245, 0246. The new single-a cores and first bits are (1235,1), (1245,1), (1246,1), (1345,0), (1346,0); joint-ab adds (1236,1). For a target (C,t,y) and an old resource (O,s,x), the exact distance is |C\O| + [t≠s] + Hamming(x,y), and repair is feasible when it is at most two. Source suffix labels and first bits are retained.

Fix k≥3. Take labeled spine vertices v_0,...,v_(k−1) and leaf vertices w_0,...,w_(k−1). Indices of v are modulo k. For each i, include all three edges (v_i,v_(i+1)), (v_i,w_i), (v_(i+1),w_i). These 3k edges are distinct in a simple graph. Their two-hot words are the new target suffixes and always-available old suffixes. Allowed old one-hot helper suffixes are indexed by a vertex set W. Let A=W∩{v_i}, and u_i=[v_i∉A].

The inherited exact theorem for any finite simple graph G and allowed helpers W gives

κ_a(G,W;2) = |E| + min_(S⊆W) (2|S| + |E[V\S]|),   κ_ab(G,W;2)=2|E|.

Here E[V\S] are edges with both endpoints outside S.

## Theorem 1: closed formula for every helper mask

For every k≥3 and every W:

κ_a(k,W;2) = 5k + q(W),    q(W) = Σ_(i mod k) u_i u_(i+1);
κ_ab(k,W;2) = 6k.

Proof. In the graph objective, deleting a selected leaf w_i saves two units of helper cost and creates at most two newly uncovered incident edges. Thus an optimum uses spine helpers only. For S on the spine let s_i=[v_i∈S]. Each triangle has 3−2(s_i+s_(i+1))+s_i s_(i+1) uncovered edges. Therefore

2|S|+|E[V\S]|
=2Σ_i s_i+Σ_i[3−2(s_i+s_(i+1))+s_i s_(i+1)]
=3k−2Σ_i s_i+Σ_i s_i s_(i+1)
=2k+Σ_i(1−s_i)(1−s_(i+1)).

The last expression is nonincreasing when an allowed s_i changes from 0 to 1, so S=A minimizes it, with value 2k+q(W). Adding the 3k mandatory edge baselines gives κ_a=5k+q(W). The inherited joint-ab rigidity gives 6k. QED.

Constructive source-labeled optimum: store (O1,0,y) for every edge word y; for every v∈A store (O0,1,e_v) and (O4,1,e_v); for each edge whose endpoints both lie outside A add (O0,1,y). Its number of resources is 3k+2|A|+|E[V\A]|=5k+q(W); each single-a target is within distance two of a stored resource, checked directly in the companion verifier. The maximal reduction from the no-helper value 6k is k, attained precisely when unavailable spine vertices are pairwise nonadjacent. Leaf availability affects no one-step optimum cardinality.

When every spine vertex is available, this explicitly specified **canonical** witness family is optimal exactly for selections S whose complement is an independent set of the k-cycle. Hence the number of these canonical optimal source-labeled libraries is the Lucas number L_k=F_(k−1)+F_(k+1). This does not count all possible optimum libraries.

## Theorem 2: scalar readout versus future and source provenance

At fixed k, q(W) is sufficient for the one-step cardinality pair (κ_a,κ_ab). If an available spine vertex v_i becomes unavailable, then Δq=u_(i−1)+u_(i+1); for the reverse update Δq=−u_(i−1)−u_(i+1). This is a constant-time local update when the adjacent availability bits are retained.

Let the future operations be named commands setting any labeled spine vertex available/unavailable, with the ability to observe κ_a after any finite command word. All 2^k spine availability masks are pairwise distinguishable under these future operations. Indeed, to recover the original u_i, set all spine vertices except v_i and its predecessor v_(i−1) available, set v_(i−1) unavailable, and do not modify v_i. The resulting graph has q=u_i. This experiment works for each i. Therefore an exact deterministic quotient for **all** such named future commands and the ensuing cardinality observer requires at least 2^k states, or k binary bits. Retaining the labeled availability mask achieves this lower bound. The result is expressly observer- and operation-scoped.

Even at one step, a q-only quotient cannot always supply a **common labeled optimum source library**. Let W0 allow every spine helper except v0 and W1 every spine helper except v1, with the same optional leaf helpers. Both give q=0 and optimum 5k. Their intersection has adjacent unavailable vertices v0,v1 and therefore requires 5k+1 sources. Any library feasible under both masks must draw from their intersection; hence no single 5k-source labeled optimum is feasible for both. This is an explicit provenance-fiber witness.

## Independent computational checks and next question

Companion standalone Python checker reconstructs the original core distances and reports PASS_R5_CYCLIC_TRIANGLE_RESIDUAL. Exhaustive graph objective: 248 availability masks for k=3..7 (even when every leaf is allowed). Exact source-labeled cover construction: 1016 masks for k=3..9. Cyclic independent-set counts: k=3..10. Named-bit diagnostic cases: 8184. Single-toggle deltas: 4092. Independent original source/target minimum set-cover MILP cross-checks: 12 choices of (k,W), k=3,4,5, for both a and ab, with SciPy/HiGHS reporting status 0 and gap 0. Finite checks supplement the symbolic proof; the solver's numerical certificate is not used as an exact-integer lower bound.

This note inherits the previous graph-incidence theorem at its original scope. No independent review, native X6 equivalence, Task/CLAIM/Result/Review or protected Activity write is asserted.

Next: source-labeled transfer kernels for genuinely branching overlapping networks and sharply restricted future-operation alphabets; determine when the k-bit future-observer lower bound reduces with finite horizon or partial command access.
