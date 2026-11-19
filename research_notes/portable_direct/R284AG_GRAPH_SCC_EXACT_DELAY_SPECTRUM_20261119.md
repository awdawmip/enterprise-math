# R284AG — Graph-SCC certificates and the exact corank-one delay spectrum for named Port edits

Date: 2026-11-19. Status: **AUTHOR_PROVED / EXACT_AUXILIARY_CHECK_PASSED / NOT_REVIEWED**. Independent portable continuation of R284AF (original author EM-DIRECT-E6B1DD), without a new formal CLAIM or independent reviewer. Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Current method context: P000 and Heartbeat X6, with the matrix pencil explicitly typed as an *auxiliary named-Port relational observer*, not a native heartbeat evolution or BRC–Shor computation. All independent edit names and signed coefficients are retained.

Scientific sources: `research_notes/portable_direct/R284AF_CORANK_ONE_ARBITRARILY_DELAYED_PORT_ACTIVATION_20261119.md` (positive Schur chain, stable Port embedding); R284AB (feedback-robust determinant/rank transfer); R284Y (complementary-minor expansion). This note adds an iff support theorem, an SCC decomposition, and a complete attainable-degree classification under a fixed baseline corank.

## AG1. Coefficients, directed cycles and the full-delay criterion

Let \(K\) be a field of characteristic zero, \(N\in K^{q\times q}\) with \(N_{ii}=0\), and \(t_1,\ldots,t_q\) independent commuting named variables. Define

\[
P_N(t)=\det(N+\operatorname{diag}(t_1,\ldots,t_q)).
\]

The directed support graph \(G(N)\) has an edge \(i\to j\) precisely when \(N_{ij}\ne0\). For \(S\subseteq[q]\) write \(t_S=\prod_{i\in S}t_i\), with the empty product equal to one.

**Theorem AG1 (principal-minor expansion).** For every such matrix,

\[
\boxed{P_N(t)=\sum_{S\subseteq[q]}\det N_{S^c,S^c}\;t_S.}\tag{1}
\]

In particular, the coefficient of \(t_S\) is the *signed exact* principal complementary minor. The minimum nonzero total degree is

\[
\boxed{\nu(N)=q-\max\bigl\{|T|:\det N_{T,T}\ne0\bigr\}},\tag{2}
\]

where the empty principal minor has determinant one. Neither a support matching alone nor numerical positivity is substituted for an exact minor in (2).

**Theorem AG2 (acyclicity iff pure top interaction).** Under the zero-diagonal premise,

\[
\boxed{P_N(t)\equiv\prod_{i=1}^{q}t_i \iff G(N)\text{ is a directed acyclic graph}.}\tag{3}
\]

The equivalence holds for signed nonzero entries as well as positive entries; cancellation cannot defeat the witness below.

*Proof.* Equation (1) follows by selecting either the diagonal named entry \(t_i\) or the fixed \(N\)-entry in each row of the Leibniz determinant. The former forces column \(i\), and the remaining permutation contributes \(\det N_{S^c,S^c}\). Equation (2) follows because different subsets \(S\) determine different monomials.

If \(G(N)\) is acyclic, a simultaneous row/column topological permutation makes \(N\) strictly upper triangular. All nonempty principal minors vanish, so (1) is the pure top monomial.

Conversely, suppose \(G(N)\) has a directed cycle \(C=(v_1,\ldots,v_\ell)\) of **minimum length**; \(\ell\ge2\). The induced graph on \(C\) contains no chord: an extra directed edge \(v_i\to v_j\) not already on the cycle, followed by the directed segment on \(C\) from \(v_j\) back to \(v_i\), would make a shorter directed cycle. Hence the only cycle cover of the induced \(C\) is the named cycle itself and

\[
\boxed{\det N_{C,C}=(-1)^{\ell-1}\prod_{j=1}^{\ell}N_{v_j,v_{j+1}} \ne0,\quad v_{\ell+1}=v_1.}\tag{4}
\]

By (1), the coefficient of \(\prod_{i\notin C}t_i\) is nonzero. This contradicts the pure-top identity and proves the equivalence. The argument uses support, exact multiplicative weights and the original signed edge names. QED.

**Corollary AG3 (SCC factorization).** Let \(B_1,\ldots,B_h\) be the strongly connected components of \(G(N)\), ordered topologically. Then

\[
\boxed{P_N(t)=\prod_{\alpha=1}^h
\det(N_{B_\alpha,B_\alpha}+\operatorname{diag}(t_{B_\alpha})).}\tag{5}
\]

This follows from simultaneous block-upper-triangular ordering; intercomponent links may be nonzero and do not change (5). An isolated loop-free singleton contributes \(t_i\). A component that is a single weighted directed cycle of length \(\ell\) and has no additional internal edge contributes exactly
\[
\prod_{i\in B}t_i+(-1)^{\ell-1}\prod_{e\in B\text{-cycle}}w_e.
\]
For a general strongly connected block, exact cancellation-aware minors are still required. DAG recognition and SCC decomposition take \(O(q+|E|)\) graph operations once the exact nonzero support is known. No claim about arbitrary-pencil bit complexity is made.

## AG2. The complete delayed-activation spectrum at baseline corank one

Assume additionally \(\operatorname{rank}(N)=q-1\) (so \(P_N(0)=0\)).

**Theorem AG4 (forbidden next-to-top degree and complete spectrum).** For \(q\ge2\), the exact possible values of \(\nu(N)\) among *zero-diagonal* corank-one matrices over \(\mathbb{Q}\), including nonnegative rational matrices, are

\[
\boxed{\nu(N)\in\{1,2,\ldots,q-2\}\cup\{q\}.}\tag{6}
\]

For \(q=1\), \(\nu(N)=1\). In particular **degree \(q-1\) is impossible**, although degree \(q\) is possible despite a one-dimensional baseline kernel.

*Necessity.* Corank one forces the constant coefficient to vanish, so \(\nu(N)\ge1\). Every coefficient of total degree \(q-1\) is a one-by-one principal minor \(N_{ii}=0\); hence if lower degrees vanish, the first nonzero degree is \(q\), whose coefficient is one. These exhaust the possible degrees.

*Sufficiency and exact witnesses.* For \(\nu=q\), take the \(q\times q\) strictly upper bidiagonal path matrix \(N\), with positive nonzero superdiagonal entries. Then \(\operatorname{rank}N=q-1\) and \(\det(N+\operatorname{diag}t)=\prod_i t_i\).

For any \(d\in\{1,\ldots,q-2\}\), put \(\ell=q-d\ge2\), and take \(N\) block diagonal with (i) a weighted \(\ell\)-vertex directed cycle having positive edge weights \(a_1,\ldots,a_\ell\), and (ii) a directed path on the remaining \(d\) vertices, with positive nonzero superdiagonal weights. The first block is invertible; the second has rank \(d-1\). Consequently \(\operatorname{rank}N=\ell+d-1=q-1\) and

\[
\boxed{P_N(t)=
\left(\prod_{i=1}^{\ell}t_i+(-1)^{\ell-1}\prod_{j=1}^{\ell}a_j\right)
\prod_{i=\ell+1}^{q}t_i.}\tag{7}
\]

Its first nonzero total degree is exactly \(d\). The supports remain fixed for all parameter values. This proves every allowed value is attained. QED.

**Sharp premise boundary.** Removing the zero-diagonal condition permits the missing \(q-1\) degree: one nonzero diagonal loop together with a disjoint \((q-1)\)-vertex directed path produces baseline rank \(q-1\) and first nonzero degree \(q-1\). The checker gives a rational \(q=5\) witness.

## AG3. Stable positive, strongly connected auxiliary Port realization

For every family in AG4 choose \(k=q+1\), \(c=1/(16k)\), and form the \((q+1)\times(q+1)\) **strictly positive** core

\[
C(t)=cJ_{k}+c\begin{pmatrix}N&0\\0&0\end{pmatrix}
+\sum_{i=1}^{q}t_iE_{ii},\qquad 0\le t_i\le c.
\]

Choose the weights of the cycle/path construction no larger than \(1/2\). Eliminating the last row/column using the scalar pivot \(c\) gives exactly

\[
\boxed{\det C(t)=c\det(cN+\operatorname{diag}t),\quad
\operatorname{rank}C(t)=1+\operatorname{rank}(cN+\operatorname{diag}t).}\tag{8}
\]

The baseline \(C(0)\) has corank one, and the first nonzero edit degree is the same \(d\) from (6). All \(C(t)\) entries are positive and all row sums remain below one. Embed the core in R284AB's \(P,A,B,Q\) Port construction, with \(g=1/16\), \(\delta=1/(256k)\), gate blocks \(W_{PA}=W_{BQ}=gI\), and feedback blocks \(W_{AA}=W_{BA}=W_{BB}=\delta J\). The full nonnegative \(W\) is strictly row-substochastic, with a strongly connected \(A/B\) interior. Its named Port complement obeys the already proved Schur identity

\[
\boxed{\det A_{\rm Port}(t)=(-1)^k g^{2k}\det C(t),\quad
\operatorname{rank}A_{\rm Port}(t)=2k+\operatorname{rank}C(t).}\tag{9}
\]

Thus the complete spectrum in (6) is attained **even with strictly positive core entries, internal bidirectional feedback, and a persistent perfect support matching**. This is a scoped algebraic Port construction preserving its edit labels; it does not assert a new native heartbeat time-law or physical calibration.

## Exact finite reproduction and remaining question

Script: `research_notes/portable_direct/R284AG_scc_delay_checker.py`. Evidence: `research_notes/portable_direct/R284AG_exact_verification.json`.

Python 3/SymPy exact rationals and Bareiss determinant. Deterministic seed 284017. Actual PASS: 25 signed sparse graph matrices (\(q=2,\ldots,6\)); 620 principal-minor coefficients independently reconstructed using Boolean Möbius inversion of determinant evaluations; 75 numerical SCC product checks; 19 shortest-cycle minor witnesses; 25 checks excluding degree \(q-1\); 15 constructed positive corank-one families, 270 rational evaluations; explicit diagonal-loop boundary; positive \(q=6,d=3\) core; and 12-by-12 complete Port determinant/rank at \(q=3,d=1\). The general theorems follow from the displayed proofs, not from the finite checks. Independent review remains NOT_REVIEWED.

**Next open unit:** derive cancellation-aware minimum-degree certificates inside nontrivial SCCs with multiple overlapping cycles, and measure the precise cost of SCC/minor computation versus R284Y complementary-minor enumeration and R284AE Schur graded recursion. Preserve individual path/branch provenance and future edit names; a zero low-order readout is not a full observer-fiber redundancy certificate.

Publication status: independently written portable scientific material; no authenticated TASK CLAIM, Result/Review promotion, native BRC computation, or live Activity checkpoint is asserted. Owner snapshot request `emr1-20261119-0755-port-owner-snapshot-v1` returned SUCCEEDED; four leased tasks were unrelated to this auxiliary Port direction at the recorded as-of time.
