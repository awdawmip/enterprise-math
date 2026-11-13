# R714 — BRC exact pair-degree ledger and X6 complete trade moves

Task \`RS-X6-TRIADIC-CLOSURE-DYNAMICS\`; publication \`TP2-8B7E13C5904A2D6F1142\`. Frozen science: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. Consumes R711–R713 (PR #2062). Evidence: proofs of general finite combinatorial lemmas plus a complete exact 6-axis Boolean census. No native V29/V39 applicability is assumed.

## Source model

Let V be a finite set of axis labels. A Boolean triad source population is H⊆C(V,3), with distinct labeled 3-subsets. Define exact unsigned **pair-degree ledger**

D(H)_{ij}=Σ_{t⊇{i,j}} 1[t∈H].

For X6, the incidence matrix A has 15 pair rows and 20 triad columns, and D(H)=A·1_H. Its binary support is the coarser pair shadow ∂₂H from R711–R713. A degree-preserving trade is a pair of disjoint triad sets (P,N) with D(P)=D(N). An admissible *combinatorial* move replaces P by N in H if P⊆H and N∩H=∅; it reverses likewise.

## Theorem R714.1 — exact linear nullity

For n≥5 the rational pair-triad incidence matrix has rank C(n,2) and nullity C(n,3)−C(n,2). For six axes, rank=15 and nullity=5.

**Proof.** Each edge lies in n−2 triples; distinct edges are contained together in one triple iff they share one vertex. Hence AAᵀ=(n−2)I+Adj(L(K_n)). The line-graph adjacency eigenvalues are 2(n−2) (multiplicity 1), n−4 (multiplicity n−1), and −2 (multiplicity n(n−3)/2); these also follow from decomposing the pair-vector space into its constant, vertex-incidence, and orthogonal parts. Thus AAᵀ has strictly positive eigenvalues 3(n−2), 2(n−3), n−4 for n≥5, proving full row rank. QED.

This rank concerns linear integer/rational coordinates; Boolean state multiplicities require their own exact count.

## Theorem R714.2 — eight-source minimum alias

For any finite V, if H≠H′ are Boolean triad populations with D(H)=D(H′), then |H△H′|≥8. This bound is attained for n≥6.

**Proof.** Cancel shared triples and call the disjoint difference sets P,N. Equality of pair degrees implies |P|=|N|=v. Select positive abc∈P. Its three pair edges ab,ac,bc must be covered by distinct negative triples, since a different triple contains at most one of these edges. Thus v≥3. If v=3, all negatives must be abx,acy,bcz with x,y,z outside {a,b,c}. Count with multiplicity the pair incidences crossing X={a,b,c} and V\X. The three negative triples yield 6. The positive abc yields 0, and each of the other two positives at most 2, a maximum of 4. Contradiction. Hence v≥4 and the symmetric difference has at least 8 triples. A matching witness is the standard Pasch trade:

P={012,034,135,245}; N={013,024,125,345}.

Both sides cover exactly 12 identical pairs once, omitting {05,14,23}. QED.

## Theorem R714.3 — six-axis exact finite classification and complete move basis

The deterministic attached Python verifier checks every 2^20=1,048,576 Boolean H using an exact base-5 integer encoding of all 15 degrees (each degree 0..4), enumerated in a 20-bit Gray order. Results:

* **995,085 distinct pair-degree ledgers/fibers**, with size histogram \`1:950564;2:37650;3:5340;4:1080;5:360;6:70;7:20;12:1\`.
* Maximum fiber cardinality **12**. Given the full exact pair-degree ledger, an exact worst-case **4-bit auxiliary index** is necessary and sufficient for H reconstruction (unrestricted fixed-length side code). By comparison, R712 needed 19 bits from the coarser **binary pair shadow**.
* The six axes have **15 unordered Pasch 4↔4 move types**, generating **61,440** legal undirected swap edges over all Boolean populations. With only these moves, **240 ledger fibers** remain disconnected; each such fiber has two singleton move components.
* The disconnected fibers, by |H|, are \`6:15;8:60;10:90;12:60;14:15\`. The 15 size-six exceptional ledger fibers each provide one disjoint **6↔6** trade type. One example:

  A={014,023,045,125,135,234}, B={015,024,034,123,145,235}.

* Adding these **15 additional 6↔6 move types**, applicable with any unchanged subset of the other 8 triads (3,840 exact swap edges), connects **every** Boolean population within each of the 995,085 exact ledger fibers.

**Finite proof certificate.** The verifier enumerates all 4-of-20 candidate Pasch sets and checks their exact pair-degree agreement, then applies every legal move to the entire 2^20 population using disjoint-set union. It traverses the full state population in a Gray-code bijection to compute all ledger fibers, counts disconnected move-components, independently extracts all 15 size-six collision pairs, verifies their equality and disjointness, applies the extra moves exhaustively, and traverses all 2^20 states again to confirm that each ledger fiber has exactly one resulting component. All operations are exact integers; rank is independently checked by exact integer elimination. The finite conclusion is for this exact six-axis Boolean candidate.

## Declared-operation sufficiency

For an **admitted external event stream** whose events include the specific triple address and the signed change (+1 admitted addition or −1 admitted deletion), the ledger evolves by D←D±A_t, and it predicts future pair-degree outputs exactly without storing all H. If an operation must first test whether t∈H, the ledger does not generally decide legality; the Pasch and 6↔6 witnesses have identical ledger but different membership answers. Source identity then remains a BRC residual. This is a scoped dynamical quotient theorem, not a physical-force cancellation rule.

## Native scope and research continuation

P000 fixes signed X6 Cell relations, six native axes, non-Euclidean PERP_E/120° and TRIADIC_CLOSURE_E primitive force arity. The present H is an abstract triad-license carrier with X6 axis labels, NOT a demonstrated valid X6 native event state. Real Cell/Link/Port, V29 PASS/TRANSFER, V39 signed j-flow, rotation-covariant update legality and source provenance require explicit verification.

**Next discriminating test:** using the task's unchanged frozen scientific pin, read exact native Cell/Link/Port + V29/V39 rules; realize a legal H(c,state,t,source), record D(H) and full signed/source ledger; test whether the displayed Pasch and 6↔6 pairs can occur under native constraints and whether a specified legal event distinguishes their sources. If only a subset is native-admissible, recompute fiber and move basis for that subset.

External literature (prior art in trades, not an external novelty claim): Encyclopedia of Mathematics, *Pasch configuration*, https://encyclopediaofmath.org/wiki/Pasch_configuration ; *On 3-Hypergraphs with Equal Degree Sequences*, Ars Combinatoria 82 (2007), https://combinatorialpress.com/ars-articles/volume-082-ars-articles/on-3-hypergraphs-with-equal-degree-sequences/ .
