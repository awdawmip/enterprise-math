# X6 Unit190 — exact spanning-forest repair of arbitrary frozen A3 coarsening

Date: 2026-11-20. Parent PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905; Task RS-X6-LEGACY-PLANE-RECONCILIATION / TP2-B4A441B23DA3159232C2. Author logical Research lane chatgpt-research-onhour-enterprise-math-20260923 (maintenance conversation excluded). Status: AUTHOR_PROVED / EXACT_FINITE_BIGINT_EXECUTED / UNREVIEWED / NOT_ADMITTED. No Native semantic PROGRESS, Result, review or P000 change is asserted by this note.

## Immutable sources and novelty boundary

Signed six-axis native primitive endpoints and ordered path mass use awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03:definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md (blob b4d49a1bbcccad0521618c6d20f6dcfa242b420a). The true historical A3 producer and consumers are awdawmip/enterprise-math@fd2bcff10ca6e147348b6c1236027fc0d2877df3:src/enterprise_math/weighted_relation_field.py (blob e50bf991e4dc4280063556a7aad1028f9f9404ed): weighted_relation_field, coarsen_weighted_relation_field, merge_weighted_relation_field, recover_totals_from_weighted_field; actual test consumer tests/test_weighted_relation_field.py (blob 51748dfe340c385907c4f2218fa1ae5ae2260522).

Unit187 already determined native finite-horizon fibers for the uncoarsened field. Unit188 already established general coarse-kernel rank 7−k and a sufficient repair using grand total plus 6−k individual coordinates. Unit189 already showed one frozen binary merge is reversed by its discarded internal relation scalar. **New here:** an exact source-field-only inverse for *every simultaneous partition* using a spanning forest of exactly 6−k internal weighted relation entries; explicit integer arithmetic, independence witnesses for every retained forest edge, and all-partition BRC mass testing. The forest-edge carrier is newly constructed from entries of the genuine producer; the frozen consumer has no claimed existing forest-repair API.

## Theorem — universal forest relation repair

Let n=6; m_i be positive integers and z_i arbitrary integers (native signed chart displacements used here as a typed adapter for the source A3 integer totals). Let Z_ij=m_j z_i−m_i z_j be the genuine generated field. Let P=(A_1,…,A_k) be any partition of the six named indices. Write M_A=Σ_{i∈A}m_i, C_A=Σ_{i∈A}z_i. The frozen coarsening returns

\[
W_{AB}=\sum_{i\in A,j\in B}Z_{ij}=M_B C_A-M_A C_B.
\]

In each A choose an arbitrary spanning tree T_A on its named indices and retain the source-field entries E_ij=Z_ij for its oriented tree edges. There are exactly Σ_A(|A|−1)=6−k such entries.

**Claim:** (m,P,W,(E_e)_{e∈∪T_A}) uniquely determines the entire fine generated relation matrix Z. A common shift of the underlying totals proportional to m remains a gauge, consistent with Unit187; this is a fine-*field* reconstruction, not absolute endpoint or ordered history recovery.

**Constructive inverse.** Let K=∏_{i=1}^6 m_i and x_i=z_i/m_i. Within each tree choose root r_A and define D_{r_A}=0 and recursively

\[
D_j=D_i-\frac{K}{m_i m_j}E_{ij}
\]

along each oriented edge i→j. Since i≠j, K/(m_i m_j) is an integer. The resulting integers are precisely D_i=K(x_i−x_{r_A}). Put H_A=Σ_{i∈A}m_i D_i. For i∈A, j∈B set

\[
\boxed{
Z_{ij}=\frac{m_i m_j}{K M_A M_B}
\left[K W_{AB}+M_A M_B(D_i-D_j)-M_B H_A+M_A H_B\right].
}
\]

The expression is an integer for genuine generated fields. It is independent of the root and of the chosen spanning tree. This is an exact rational-intermediate/int-output inverse, including diagonal and within-block entries.

**Proof.** The edge relation gives E_ij=m_i m_j(x_i−x_j), so the path recursion determines D_i=K(x_i−x_root). The group weighted average of x is C_A/M_A and the average of D is H_A/M_A. Thus x_i=C_A/M_A+(D_i−H_A/M_A)/K. The genuine coarse relation gives C_A/M_A−C_B/M_B=W_AB/(M_A M_B). Substituting into Z_ij=m_i m_j(x_i−x_j) gives the displayed formula. Because it equals the actually generated integer Z, integrality and reconstruction follow without assuming every arbitrary putative (W,E) tuple is admissible. All allowed trees give the same Z. □

## Sharpness — why no forest edge can be omitted

Remove one forest edge of block A; its tree separates into nonempty sides L,R. Define p=Σ_{i∈L}m_i and q=Σ_{j∈R}m_j, and form a nonzero integer perturbation Δz_i=q m_i for i∈L, Δz_i=−p m_i for i∈R, Δz_i=0 elsewhere. Then ΔC_A=qp−pq=0 and all other group totals are fixed, so **every coarse W_AB is unchanged**. Each retained internal forest edge lies inside L or R and hence has unchanged relation E_ij. The deleted edge joins L and R and changes its weighted relation by (p+q)m_i m_j ≠ 0. Consequently its data are independent of W and all the other tree edges, over generated integer fields. Exactly 6−k additive independent relations are necessary and sufficient in this forest-edge interface, consistent with Unit188's general rational-rank bound. This does not assert a universal bit lower bound against arbitrary nonlinear encodings.

For a finite signed-native primitive horizon, choose z=0 and z'=Δz. Their total coordinate sums coincide at zero, and ||Δz||_1 is positive and even. At horizon N=||Δz||_1, both z and z' are reachable from the chosen Cell anchor (the zero endpoint uses backtracking pairs). Therefore this independence remains a genuine finite-horizon collision, not merely a formal unbounded algebraic example.

## BRC endpoint mass preservation and its boundary

At a fixed primitive event horizon N, the fine generated field Z is exactly reconstructed from (W,E), so the full BRC path-mass distribution **grouped by fine relation fields** is also reconstructed. Unit187 supplies the additional ranked endpoint lift needed if a future operation requires one particular native endpoint inside a fine-field fiber. The forest source data alone do not recover path order, as shown by Unit189's two differently ordered paths to a common endpoint. The capacities m_i are A3 relation weights, distinct from primitive signed-X6 path branch counts.

## Executed independent certificate

The standalone JavaScript BigInt checker enumerated all 203 partitions of six named axes, three source capacity vectors [1,1,1,1,1,1], [1,2,1,2,1,2], [2,3,5,7,11,13], and exact ordered primitive-walk endpoint masses at horizons N=0,…,4. Across 837,375 generated field/partition/horizon states it independently checked the genuine frozen coarsening sum against its direct aggregated-totals formula and tested both chain and star spanning forests against the full fine field. It compared 802,865 exact fine-field BRC mass aggregates, and constructed 1,632 individual omitted-edge independence witnesses. All violation counts were zero; event masses were 12^N. The checked horizons have 1,12,73,304,985 reachable native endpoints respectively.

- Executed pure-JS checker, identical source saved at research_checks/X6_UNIT190_FOREST_RELATION_REPAIR_CHECK_20261120.js, commit ab616697577b2a2c66a79d71f6b66eabed9e2012, Git blob bde83813d0aa34a20b01bccf7e4d8d9139198e89.
- Exact results: research_checks/X6_UNIT190_FOREST_RELATION_REPAIR_RESULTS_20261120.json, commit 7d93bb44423f24de4cba44022016ce68645aa26d, Git blob 75b0e68fe068cd4adb3acaf1ca3f00557becf094.

This is a **source-equivalent independent checker**, not a direct runtime import of the original source and not a repeat or substitute for the already completed original R063 six-file native benchmark. The general theorem rests on the integer/rational identity above; finite exhaustive checks exercise the implementation only.

## Mother task and next discriminating work

The inherited 28-LP reconciliation still needs verified LP011 historical native argmax and LP019 invalid positive N-BRC subtraction offending commit:path:line plus true typed consumer. Their provenance remains unresolved. Original Units149–152 and author Units175 onward need legitimate same-lane Native semantic association; independent Driver review remains UNREVIEWED/NOT_ADMITTED. Earlier original Native authenticated frontiers were through Unit174; this note does not refresh protected authority. Current original request onhour-20261120-1524-x6-own-unit187-native-continuation-prepare-v1 was read as FAILED/NATIVE_INPUT_SCOPE_METADATA_BUDGET_EXCEEDED; do not replay. The research continuation can be read without a new protected mutation.

Next scientific action with information gain: test *historical true downstream consumers* of coarsened weighted relation fields whose outputs are path order or signed event phase dependent, to determine the smallest extra provenance record beyond the now fully repaired fine endpoint field. Alternatively, prioritize the exact LP011/LP019 original offending source evidence if newly located. Frozen pins and original R063 completion are preserved.
