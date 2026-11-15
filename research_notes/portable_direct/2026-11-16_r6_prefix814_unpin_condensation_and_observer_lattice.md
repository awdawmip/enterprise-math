# PREFIX-814 — Exact unpinning of named-source residual SCCs and observer-difference lattices

Date: 2026-11-16 (Asia/Shanghai).
Scope: independent auxiliary integer transportation/BRC named-source research, not native X6 event physics.
Frozen scientific input: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`.
Predecessors: PREFIX-809 (cycle connectivity), PREFIX-811 (residual SCC observer lattice), PREFIX-812 (fixed-fiber reachability invariance), PREFIX-813 (one-pin locality).
Source observer semantics: named source-edge counts and explicitly stated integral linear observations. No unrestricted loss of provenance.

## 1. Setting

Let \(G=(U,V,E)\) be a finite named bipartite multigraph. An edge \(e=(u,v)\) runs from row vertex \(u\) to column vertex \(v\), with integral capacity \(K_e\ge0\). Given a feasible seed \(x\) satisfying \(Bx=b\) and \(0\le x\le K\), let \(P\subseteq E\) be the set of fixed named edges, each pinned at its seed value. Denote

\[
F_P=\{y\in\mathbb Z^E:By=b,\ 0\le y\le K,\ y_e=x_e\text{ for }e\in P\}.
\]

The directed movable residual graph \(D_x^{-P}\) has the arc \(u\to v\) when \(e\notin P,\ x_e<K_e\), and \(v\to u\) when \(e\notin P,\ x_e>0\); both arcs may exist for the *same* named edge. All arcs carry their originating edge name. Let \(A\in\mathbb Z^{k\times E}\) be a declared integral observation matrix and

\[
L_A(F_P)=\left\langle A(y-z):y,z\in F_P\right\rangle_{\mathbb Z}.
\]

The full observation value set is not in general an entire coset of this lattice; lattice equality does not prove full support preservation.

## 2. The single-arc SCC insertion theorem

**Theorem 814.1 (exact condensation insertion).** Let \(D\) be an arbitrary finite directed multigraph with SCC condensation DAG \(Q\). Insert one new arc \(a\to b\), with endpoints in old SCCs \(C_a,C_b\).

* If \(C_a=C_b\), the SCC partition is unchanged.
* If \(C_a\ne C_b\) and \(C_b\not\leadsto C_a\) in \(Q\), the SCC partition is unchanged.
* Otherwise precisely the old SCCs in

\[
M=\operatorname{Reach}_Q(C_b)\ \cap\ \operatorname{Pre}_Q(C_a)
\]

coalesce to **one** new SCC; all other old SCCs retain their membership.

**Proof.** A new directed cycle must use the inserted arc. Such a cycle exists exactly when the old graph has a path \(b\leadsto a\), or \(a,b\) are already mutually reachable. If \(C_a,C_b\) are distinct and \(b\leadsto a\), every component on an old \(C_b\leadsto C_a\) path is now mutually reachable with both endpoints via the inserted arc. Their union is exactly \(M\). Conversely, any newly mutually reachable pair outside a pre-existing SCC needs the inserted arc in at least one direction; deleting that occurrence yields an old directed path \(C_b\leadsto C_a\) whose visited components are in \(M\). No component outside \(M\) can join this new SCC. QED.

**Algorithmic implication.** To unpin a named edge \(e=(u,v)\) from \(P\ni e\), start with \(D_x^{-P}\). If \(x_e<K_e\), insert the arc \(u\to v\); if \(x_e>0\), insert the arc \(v\to u\). Process these up to two arc insertions **sequentially**, updating the condensation after the first insertion. The resulting graph is exactly \(D_x^{-(P\setminus\{e\})}\), so Theorem 814.1 gives its new SCC partition without an unrelated task-state or physical-time assumption. A reachability scan may visit the full condensation DAG; no unconditional sublinear or speedup claim is made.

## 3. Exact observer-lattice update and monotonicity

**Theorem 814.2 (source-fiber unpin update).** Under the hypotheses above:

1. \(F_P\subseteq F_{P\setminus\{e\}}\) and therefore \(L_A(F_P)\subseteq L_A(F_{P\setminus\{e\}})\) for every integral observer matrix \(A\).
2. The old SCC partition refines the new SCC partition. An unpin may *merge* SCCs but cannot split them. Only SCCs in the new merged component(s) may change; other SCC cycle generators remain reusable.
3. If the newly inserted named edge is internal to an old SCC, its release may change the integral cycle lattice even though the SCC partition is unchanged. Thus an implementation must also update the fundamental-cycle generators in that SCC, not merely detect SCC mergers.
4. The exact new subgroup is obtained by applying the PREFIX-813 integral named-cycle lemma to the resulting movable residual graph: for each new SCC \(C\), take the integral incidence cycle lattice \(Z_1(H_C;\mathbb Z)\) of **all currently movable, positive-capacity named edges internal to \(C\)**, including pre-existing inter-SCC edges that have become internal, and apply \(A\). The direct sum of these image generators is \(L_A(F_{P\setminus\{e\}})\). For a scalar observer \(w\), its gcd \(g_{\rm unpin}\) divides \(g_{\rm pin}\), using \(0\mathbb Z=\{0\}\).

**Proof.** (1) is immediate from inclusion of feasible integer tables; any difference of tables in the smaller set is also one in the larger. (2) follows from arc insertion without arc deletion and Theorem 814.1. For (3), a newly movable named edge inside an unchanged SCC adds a possible incidence-cycle generator and may enlarge its observer image subgroup. For (4), the resulting residual graph is precisely the movable graph for the relaxed fiber at the same feasible seed \(x\); apply PREFIX-813 Lemma 813.1, whose proof constructs admissible unit residual-cycle table moves and spans the integral named cycle lattice inside each SCC. Changes outside the affected new SCCs do not occur, because their internal named edge sets and residual SCC memberships are unchanged. Inclusion of scalar subgroups of \(\mathbb Z\) gives the gcd divisibility. QED.

**Caution.** An SCC merger does *not* by itself imply additional feasible source tables: two opposite residual arcs of the **same** named edge may form a zero-net reversal, not a nonzero admissible change. Actual new generators must be computed in the *named incidence cycle lattice*, which excludes a one-edge two-arc cancellation as a nonzero cycle.

**Exact certificate procedure:** retain the seed \(x\), capacity/margins and actual pin set; insert only the newly allowed residual arcs of \(e\); apply the condensation insertion rule; retain unaffected SCC forest generators; for each affected SCC build an undirected named spanning forest of all newly internal movable edges and compute the integral fundamental-cycle images. In the scalar case the gcd of fundamental-cycle weights is exact; in the vector case use integer Hermite/Smith normalization, keeping rank and torsion/index data separately. The latter normalization is an algorithmic consequence, not an independently benchmarked performance result here.

## 4. Three exact counterexamples and discriminators

**W814-A (unchanged SCC, strict lattice enlargement).** One row and one column with three distinguishable parallel edges \(a,b,c\); each has capacity 2, total margin 3, and seed \((1,1,1)\). Take \(W=x_a+2x_b\). With \(a=1\) pinned, exchanges \(b\leftrightarrow c\) yield \(L_W=2\mathbb Z\). After unpinning \(a\), exchanges \(a\leftrightarrow c\) yield \(L_W=\mathbb Z\). The movable residual graph remains one SCC both before and after. Hence a partition-only cache is insufficient.

**W814-B (real SCC merger).** In the complete 2×2 unit-capacity bipartite graph with all row and column margins 1, take seed \((x_{00},x_{01},x_{10},x_{11})=(1,0,0,1)\). Pinning \(x_{00}=1\) leaves four singleton residual SCCs; releasing the pin adds the residual arc \(c_0\to r_0\) and joins all four vertices into one SCC. The relaxed fiber admits the other matching table.

**W814-C (SCC merger without any new table).** One row and one column linked by one named edge of capacity 2 with total margin 1: the feasible fiber is the singleton \(x_e=1\), even without pinning. With the edge pinned, the movable residual graph has two singletons; after unpinning it has the two opposite arcs of this one named edge and one SCC. Nevertheless \(L_w=0\) for every observer and there is no second table. SCC coalescence alone cannot be used as a source-multiplicity certificate.

## 5. Exact finite validation

The deterministic Python checker \`PREFIX814_R6_UNPIN_SCC_LATTICE_CHECK.py\` uses only arbitrary-precision integer operations. It exhaustively enumerates capacity configurations, complete integer source tables, and the realized margin fibers for five *declared finite* graph families; for every feasible table and every positive-capacity named edge it:

1. Constructs the pinned residual graph and inserts every admissible unpin arc, comparing the predicted incremental SCC equivalence to independently recomputed graph reachability after each insertion.
2. Checks SCC refinement on every ordered pair of vertices.
3. Brute-enumerates all tables in the original and pinned fiber, obtains three scalar observer difference gcds, and compares them to independently computed named internal-SCC spanning-forest cycle gcds.
4. Checks scalar lattice divisibility, and verifies all three explicit witnesses.

| Suite | Capacity configs | Margin fibers | Source tables | Unpin cases |
|---|---:|---:|---:|---:|
| Complete 2×2, capacities 0..2 | 81 | 1,215 | 1,296 | 4,320 |
| Complete 2×3, capacities 0..1 | 64 | 704 | 729 | 2,916 |
| Complete 3×3, capacities 0..1 | 512 | 17,840 | 19,683 | 118,098 |
| Complete 2×2 with duplicated named (0,0), capacities 0..1 | 32 | 212 | 243 | 810 |
| Three named parallel edges, capacities 0..2 | 27 | 108 | 216 | 540 |
| **Total** | **716** | **20,079** | **22,167** | **126,684** |

Across these cases: **127,656** incremental arc-insertion SCC checks; **4,408,668** ordered-vertex-pair partition comparisons; **380,052** exact scalar observer-lattice comparisons. **16,831** unpin cases merged SCCs. Another **119** cases left the SCC partition unchanged but changed the selected first scalar observer gcd. All exact assertions passed. These bounded checks verify the algorithm and examples; the general theorem strength rests on the proofs.

Reproduce by running \`python3 research_notes/portable_direct/PREFIX814_R6_UNPIN_SCC_LATTICE_CHECK.py\`. Compare the returned JSON to \`PREFIX814_R6_UNPIN_SCC_LATTICE_RESULTS.json\` semantically (JSON object key ordering is irrelevant). No floating point or randomness enters the arithmetic. A measured full end-to-end performance improvement is not established.

## 6. Continuation and authority

The present theorem concerns a finite *auxiliary integer named-source transportation model*. The fixed scientific pin is not updated. It is not a native X6 Cell/Link/Port evolution, a complete future-observation equivalence, an ordered-time event, a physical claim, or a mathematical-admission decision. Source history and observer types are preserved; observing only the subgroup cannot recover all joint source counts or exact Laurent histograms.

Suggested next independent unit: derive an amortized scheme for successive pins/unpins, including changes of feasible seed, and separately compute multidimensional Hermite/Smith invariants and the full finite support when relevant. Benchmark sparse versus dense named graphs with actual full costs. A lawful native X6 event/port bridge requires additional typed interface and temporal preservation proofs.

Status: AUTHOR_PROVED / EXACT_FINITE_REGRESSION / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED. Shared \`RS-X6-NATIVE-TIME-DYNAMICS\` CLAIM not acquired merely by this independent publication.
