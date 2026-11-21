# R762II — 63-event absolute kernel for six-axis composite Port Euler existence

Date: 2026-11-22 (Asia/Shanghai). Research state: **AUTHOR_PROVED / EXACT_FINITE_CROSSCHECKED / NOT_REVIEWED**.

Scientific pin preserved: Task `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, frozen `a72226e2430ffa4786321ac86e7f0c599d5f0389`. Direct predecessor: R762IH at `5f39e2e5faac0b3e8fb358d810eb8d0477e5d612:research_notes/portable_direct/R762IH_PORT_67_EVENT_KERNEL.md`. This is an exact theorem about the **composite 15-Port observer**; no P000 native force/time/rotation or physical residual assertion is made.

## Theorem (uniform 63-event subwitness)

Let the 15 Port vertices be the unordered axis pairs \(\binom{[6]}2\). Each of the 20 triple supports \(S=\{i,j,k\}\) permits one named event on any one of the three edges of the triangle with Port vertices \(ij,ik,jk\). A legal closed history from a specified active Port \(p\) is an Euler circuit through all assigned named events in a connected even-degree Port multigraph.

For every nonzero finite support histogram \(n=(n_S)\), every base Port \(p\), and **every** connected Euler realization of \(n\), there exists a subhistogram \(h\le n\), obtained solely by deleting pairs of events of the same support, and a connected Euler realization of \(h\), such that:
1. \(h_S>0\) if and only if \(n_S>0\), and \(h_S\equiv n_S\pmod2\).
2. The active Port vertex set and the chosen starting Port \(p\) are preserved.
3. \(h_S\le4\) for every support, and \(\boxed{\sum_S h_S\le63}\).

Conversely, the removed event pairs can be reinserted on a previously occupied edge of their support, preserving Euler legality. Thus \(N_p(n)>0\) if and only if *some* support-preserving, parity-preserving subhistogram \(h\le n\) with at most 63 events has \(N_p(h)>0\).

The reduction is **witness-dependent**: it is not a claim that a canonical 63-event histogram can be computed by individually capping input counts. The exact existence predicate and the specified start are preserved, not history multiplicities, event order, signed Cell displacement, BRC positive weight, original native time/force semantics, or history counts.

## Proof

**Step 1: R762IH's pair reduction, reused at its exact scope.** For each support triangle, remove two parallel occurrences when at least three copies occupy one side; otherwise, when the support total is at least five, every triangle side is present and a doubled side can be removed, its endpoints remaining connected via the other two sides. Parity, vertex set, support presence and connectivity survive. Further remove two copies from a support with final count four when either a side has at least three copies, a doubled side has a two-side alternative route, or a doubled side is not a bridge of the underlying simple Port graph. At termination, every remaining four-count support occupies exactly two sides with multiplicities \((2,2,0)\), and **both positive sides are bridges**. Let \(k\) be the number of these critical supports; let \(v\le15\) be the active Port count; let \(t=o+e\le20\) be the number of positive supports, partitioned into odd-count \(o\) and positive even-count \(e\). Then \(k\le e\), and there are \(2k\) different bridges, because a Port edge uniquely determines its support (the union of its two axis-pair labels is a triple). Hence \(0\le k\le7\), and
\[
|h|\le3o+2e+2k=3t-e+2k\le3t+k. \tag{1}
\]

**Step 2: count remaining support types after deleting bridges.** Remove exactly the \(2k\) critical bridge edges from the simple Port graph \(G\). Its \(v\) vertices split into \(2k+1\) components with nonempty vertex sets \(A_1,\ldots,A_{2k+1}\). All graph edges of a noncritical positive support lie inside these components: a noncritical edge cannot coincide with a deleted critical bridge, and an edge outside these components would contradict their construction. Each of the \(t-k\) noncritical supports has at least one occupied simple edge, and different supports have different Port edges. With \(L(K_6)\) the ambient pair-Port graph,
\[
t-k\ \le\ \sum_{j=1}^{2k+1}e_{L(K_6)}(A_j). \tag{2}
\]
Moreover \(\sum_j (|A_j|-1)=v-(2k+1)\le 14-2k\).

**Step 3: graph packing bounds.** For arbitrary component sets of sizes \(s_j\), the trivial estimate
\[
\sum_j e_{L(K_6)}(A_j)\le\sum_j\binom{s_j}{2}
\le \binom{v-2k}{2}
\le \binom{15-2k}{2}.\tag{3}
\]
The middle inequality follows from \(\binom a2+\binom b2\le\binom{a+b-1}2\) for \(a,b\ge1\), applied repeatedly. Thus for \(k=5,6,7\), respectively, (2)–(3) imply \(t\le15,9,7\).

For \(k=4\) the bound (3) would be 21; exploit the actual Port geometry to obtain the sharper **15**. Let \(f(s)\) be the largest number of edges induced by any \(s\)-vertex subset of \(L(K_6)\). We prove \(f(7)\le15\). A set of seven Port vertices corresponds to a simple seven-edge graph \(H\subset K_6\). Its induced Port-edge count is the number of pairs of incident edges of \(H\), namely \(W(H)=\sum_{i=1}^6\binom{d_i(H)}2\). If maximum degree \(\Delta\le3\), the sum of degrees is 14 and convexity of \(x\mapsto\binom x2\) bounds \(W(H)\le4\binom32+\binom22=13\). If \(\Delta=4\), delete a degree-four vertex, leaving three edges. The deleted vertex contributes six wedges, the remaining graph contributes at most three, and restoring incidences at its four neighbors adds at most six: \(W(H)\le6+3+6=15\). If \(\Delta=5\), deleting the degree-five vertex leaves two edges: \(W(H)\le10+1+4=15\). Thus \(f(7)\le15\), attained by a 5-star with two adjacent extra leaf edges. Also \(f(6)\le14\): because the ambient \(L(K_6)\) is connected, every nonempty proper six-Port subset has an adjacent outside vertex; extending to seven adds at least one induced edge.

When \(k=4\), nine components split at most fifteen Port vertices, so \(\sum(s_j-1)\le6\). If the largest component has seven vertices, all others are singletons and (2) has right side at most 15. If the largest has six, at most one further component has size two, giving at most \(f(6)+1\le15\). If the largest has five, the remaining surplus is two, giving at most \(\binom52+\binom32=13\). If the largest has at most four, convexity and the six-unit surplus give at most \(\binom42+\binom42=12\). Therefore \(\sum_j e_{L(K_6)}(A_j)\le15\), so \(t-4\le15\), or \(t\le19\).

**Step 4: global bound.** Apply (1) in each critical-support case:
- \(k=0,1,2,3\): \(t\le20\), so \(|h|\le60+k\le63\).
- \(k=4\): \(t\le19\), so \(|h|\le3(19)+4=61\).
- \(k=5\): \(t\le15\), so \(|h|\le50\).
- \(k=6\): \(t\le9\), so \(|h|\le33\).
- \(k=7\): \(t\le7\), so \(|h|\le28\).

The maximum is 63. Each removal preserves the graph's relevant Euler properties, and reverse parallel-pair insertion restores the original support histogram. QED.

## Reproducible verification

The companion `R762II_CHECK.py` enumerates all \(2^{15}=32768\) Port-vertex subsets, computes their exact induced \(L(K_6)\) edge counts, and verifies \(f(7)=15\). It independently maximizes the sum of per-component extremal counts by integer dynamic programming for each \(k\in\{0,\dots,7\}\). Executed with Python 3 standard library and returned `PASS R762II`; the tabulated maxima for \(k=0,\dots,7\) are \(60,61,62,63,61,50,33,28\) events. This finite validation checks the extremal combinatorics; the unbounded theorem follows from the graph-theoretic proof and R762IH's pair-reduction lemma.

## Scope and next open question

The upper bound is now **63**, improving R762IH's **67**. Sharpness of the absolute bound is not established: the prior 13-event example is a lower-bound witness for the *uniform per-support cap four*, not for a 63-event absolute kernel. A next discriminating unit is to use the quotient-component triangle-coloring constraints to exclude three critical supports when all twenty supports are present, or to construct a histogram-only exact Euler assignment/certificate algorithm. P000's `TRIADIC_CLOSURE_E` remains the frozen mother foundation; no native lifting is inferred.

Control provenance: historical Researcher `EM-X6-A681A5`, SID `MCP-773502d89b7a4bd58a37e97a2dd52ba5`. The original current continuation read `r3-20261122-0420-x6-cont-v1` ended `FAILED / SOURCE_TREE_TRUNCATED`; current live CLAIM and session execution authority were not established. This GitHub note is an independent portable research artifact, without protected PROGRESS, formal Result or independent Review.
