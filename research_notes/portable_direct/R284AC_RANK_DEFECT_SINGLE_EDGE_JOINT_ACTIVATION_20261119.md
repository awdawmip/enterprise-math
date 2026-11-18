# R284AC — Rank-defect law and sharp joint-only activation by independent single-edge Port edits

Date: 2026-11-19. Status: **AUTHOR_PROVED / EXACT_INTEGER_AND_FRACTION_CHECK_PASSED / NOT_REVIEWED**.
Continuation: R284AA, R284AB (feedback-robust gate/core Schur factorization), with R284Y–Z retained for distinct path routing. Frozen scientific pin **43ec6098b1330ae86d0a7863be336c5d97f6ef34**; the historical pin is not changed by reading current operational rules. Scope: auxiliary rational named-Port observer in the unchanged Heartbeat X6 research framework, with an explicitly typed, finite collection of edge updates. No native physical dynamics, BRC–Shor calculation, Task CLAIM or independent Review is asserted.

## 1. Lower-order invisibility is controlled by core rank defect

Let \(k\ge2\), let \(C_0\) be a \(k\times k\) matrix over a characteristic-zero field with rank \(r<k\), and let
\[
 C(t)=C_0+\sum_{j=1}^m t_jE_{a_jb_j},
\]
where each \(t_j\) is an independently named scalar and each \(E_{a_jb_j}\) affects **one specified physical core edge**. In particular, the edit names are not conflated with their values, and different terms retain their individual row/column associations.

**Theorem AC1 (rank-defect vanishing order).** Every coefficient of total edit degree strictly less than \(k-r\) in \(\det C(t)\) is zero. Thus, when \(k-r>1\), every first-order sensitivity can vanish even though an allowed joint operation changes the determinant.

**Proof.** Expand the determinant by multilinearity in its rows (or columns) and collect the coefficient of any squarefree monomial \(t_{j_1}\cdots t_{j_d}\). If the selected \(d\) edited cells repeat a row or a column, the coefficient is zero. Otherwise the coefficient, up to the permutation sign, is the complementary \((k-d)\times(k-d)\) minor of \(C_0\). If \(d<k-r\), that minor has order \(k-d>r\) and therefore vanishes. Each parameter enters one matrix entry, so the determinant is multi-affine in those parameters and there are no higher powers to consider. QED.

This is an exact algebraic observation law for the specified edits, not a numerical small-error estimate.

## 2. An exact positive witness with arbitrary corank

Write \(J_k\) for the all-ones matrix and take integers \(1\le r<k\), \(m=k-r\). Fix \(c>0\) and set
\[
 C_0=cJ_k+c\sum_{i=1}^{r-1}E_{ii},\qquad
 C(t)=C_0+\sum_{j=1}^{m}t_jE_{r-1+j,r-1+j}.
\]
These are \(m\) **distinct independently editable single entries**, not a correlated dense edge bundle. All entries of \(C_0\) are positive, and \(C(t)\) remains positive on \(0\le t_j\le c\).

**Theorem AC2 (sharp pure joint activation and exact rank).**
\[
 \boxed{\det C(t)=c^r\prod_{j=1}^{k-r}t_j},\qquad
 \boxed{\operatorname{rank}C(t)=r+\#\{j:t_j\ne0\}}.
\]
Consequently, the determinant is zero on **every proper coordinate face** \(t_j=0\), yet it is nonzero for all \(t_j>0\). The first nonzero multi-edit interaction has order exactly \(k-r\), matching AC1.

**Proof.** Subtract the last row (which is \((c,\ldots,c)\)) from each of the first \(k-1\) rows. Their resulting nonzero entries are confined to distinct diagonal columns: \(c\) in columns \(1,\ldots,r-1\), and \(t_1,\ldots,t_m\) in columns \(r,\ldots,k-1\). The last row remains all \(c\). Expansion of the determinant yields \(c\cdot c^{r-1}\prod_jt_j\), with positive sign. The nonzero transformed rows are independent coordinate vectors, and the last row has a nonzero component in column \(k\), so the rank equals \(1+(r-1)+\#\{j:t_j\ne0\}\). QED.

**Theorem AC3 (maximality with strictly positive baseline).** Suppose \(C_0\) is entrywise positive, and \(m\) distinct independently named *single-entry* edits have the following joint-only property: the determinant polynomial is identically zero whenever any one of the \(m\) edit parameters is fixed to zero, but is not the zero polynomial when all parameters are allowed. Then \(m\le k-1\). This bound is attained by AC2 with \(r=1\).

**Proof.** Multi-affinity plus vanishing on all faces forces the determinant polynomial to be exactly \(a\,t_1\cdots t_m\) for some nonzero \(a\). Hence \(m\le k\). If \(m=k\), for \(a\ne0\) the \(k\) edited cells must form a perfect permutation matching of the \(k\) rows and columns. Consider the coefficient of the product of any \(k-1\) of these \(k\) parameters. It is, up to sign, the single complementary entry of \(C_0\), strictly positive and so nonzero. But the assumed face vanishing forces that coefficient to be zero. Contradiction. The \(r=1\) construction realizes \(m=k-1\). QED.

The quantifier in AC3 concerns **independently parameterized single matrix entries** and identically vanishing coordinate faces. Arbitrary correlated edit bundles or nonlinear parameter dependence have a different coefficient algebra.

## 3. Robust embedding in a strongly connected, strictly stable Port network

Reuse the exact R284AB geometry: four disjoint sets \(P,A,B,Q\) of \(k\) named ports each, \(S=A\cup B\), with nonzero transition blocks
\[
 W_{PA}=D_g,\quad W_{BQ}=D_h,\quad
 W_{AA}=L,\quad W_{AB}=C(t),\quad W_{BA}=D,\quad W_{BB}=U .
\]
Choose
\[
 c=\frac1{64k},\quad \delta=\frac1{256k},\quad
 L=D=U=\delta J_k,\quad
 0\le t_j\le c,\quad \frac1{16}\le g_i,h_i\le\frac18 .
\]
All entries within the recurrent internal support are positive. The \(A\)-row sums are bounded above by \(k\delta+kc+c\), and \(B\)-row sums by \(2k\delta+1/8\); both are less than one for every \(k\ge2\). \(P\)-row sums are at most \(1/8\), and \(Q\)-row sums are zero. Thus the full \(4k\)-state \(W\) is nonnegative and strictly row-substochastic, and the internal \(2k\)-vertex graph is strongly connected (indeed all four internal blocks are positive).

With \(G=I-W_{SS}\) and the complementary \((3k)\times(3k)\) matrix
\[
 A_{\rm Port}=(I-W)[(S,P),(S,Q)]
 =\begin{bmatrix}G&-W_{SQ}\\-W_{PS}&0\end{bmatrix},
\]
R284AB's exact Schur identity applies even with all these genuine feedback edges:
\[
 \boxed{\det A_{\rm Port}(t)
 =(-1)^k\Bigl(\prod_{i=1}^kg_i h_i\Bigr)c^r\prod_{j=1}^{k-r}t_j},
\]
\[
 \boxed{\operatorname{rank}A_{\rm Port}(t)
 =2k+r+\#\{j:t_j\ne0\}}.
\]
Every support edge needed for the \(k\) identity terminal routes remains strictly positive on *every* coordinate face; the complementary matrix has a perfect support matching throughout. The rank switch is caused by an exact **joint-weight interaction**, not by the appearance/disappearance of an edge. The complete named path and edge provenance must therefore be retained when testing future edit combinations.

For \(k=3,r=1,c=1/192,\delta=1/768\), the two single-edge edits \(t_1E_{11}\) and \(t_2E_{22}\) each leave the determinant zero when applied alone; together, \(\det C=c t_1t_2\). At \(t_1=t_2=c\), \(g_i=h_i=1/16\), the **exact** values are
\[
 \det C=\frac1{7077888},\qquad
 \det A_{\rm Port}=-\frac1{118747255799808},\qquad
 \operatorname{rank} A_{\rm Port}=9 .
\]
For \(k=4,r=2\), two independently named core edges likewise give a pure \(t_1t_2\) effect.

## 4. Scope-precise consequence for algorithms and future observations

For a rank-\(r\) core, sampling only independent edit activations of arity \(<k-r\), with all other independent edits at the declared baseline, is insufficient to decide whether the full jointly edited complementary determinant is identically zero: AC2 is an explicit witness that passes every such zero test but becomes nonsingular when all \(k-r\) edits act.

This is a **lower bound for bounded-interaction coordinate-face sampling**, not for all algorithms. The typed rank-defect/factorization certificate detects this particular family by inspecting \(C_0\), its independent single-edge edits and the exact product formula, in \(O(k)\) symbolic factors after the structural pattern has been verified. General matching-minor enumeration can inspect more candidate supports and does not share this sampling restriction.

In the language of the project's residual-faithful observers, individual-edge or pairwise zero readings do not certify the safe erasure of an allowed higher-arity joint update. The result is algebraic and source-labelled; no native X6 spatial compression or Heartbeat-time trajectory is being inferred.

## 5. Explicit finite validation and source provenance

Files:
- \`research_notes/portable_direct/R284AC_unit_edge_joint_interaction_checker.py\`
- \`research_notes/portable_direct/R284AC_unit_edge_joint_interaction_verification.json\`

The executable uses integer-scaled \(D=256k\) Port matrices, exact fraction-free Bareiss determinants, and independent rational Gaussian rank elimination. Tested **every** binary edit mask for each pair \(2\le k\le6\), \(1\le r<k\), under two gate arrangements: **228 complete Port determinants**, **228 core determinants**, **456 rank calculations** (core and full Port), and **228 strict substochasticity checks**. All checks returned PASS; no floats, randomness or network calls. This is finite implementation validation separate from the symbolic all-\(k\) proofs above.

Read lineage: R284Y matching minors; R284Z path pairing; R284AA stable nonnegative gate witness; R284AB feedback-robust determinant/rank lemma. Original verified researcher lineage \`EM-DIRECT-E6B1DD\`, session \`MCP-8487128c846440d1952bfc6fa44aeb86\`. Source publication is independent portable research, not a new formal CLAIM/Review. A task-inventory read as of 2026-11-18 20:29:28 UTC had two global LEASED items, but did not exhaust the catalogue; new scoped LEASED query \`r1-20261119-0501-r284ac-leased-owner-check-v1\` began as QUEUED. No owner takeover is attempted.

## Next independent mathematical unit

Classify which **higher-order mixed-minor coefficients** remain detectable by bounded-width graph separators or directed disjoint-path certificates, and build a symbolic recognition algorithm that adaptively requests joint probes only at the arity permitted by the exact rank defect and declared future edit set. Compare the number and bit cost of determinant/minor operations against R284T's joint coefficient certificate, keeping observer indices, branch labels, and admissible future edits unchanged.
