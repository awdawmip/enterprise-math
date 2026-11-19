# R284AK — Strictly positive nonsymmetric two-sided factors with an unbounded principal-rank gap

**Date:** 2026-11-19. **Status:** AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED.  
**Predecessor:** R284AJ Positive Gram Rank (the AJ1 two-layer determinant identity), itself continuing R284AI and R284AH.  
**Frozen scientific input:** 43ec6098b1330ae86d0a7863be336c5d97f6ef34, unchanged.  
**Scope:** exact rational auxiliary named-edit Port observations, preserving P000 and ACTIVE six-axis X6 worldview as an external typing constraint; no claim of native X6 dynamics or global observer equivalence.

## 1. Main theorem — a new counterexample to Gram-rank-only extrapolation

Let \(k\ge2\), \(m=2k\), \(r=k+1\). There exist **strictly positive integer** matrices \(U,V\in\mathbb Q^{m\times r}\), both full column rank, for which \(C=UV^T\) has rank \(r\) but largest nonsingular principal submatrix of order exactly \(2\). For independently named diagonal edits, set

\[
M_C(u,v)=\begin{pmatrix}D_u&I_m\\C&D_v\end{pmatrix},
\qquad x_i=u_iv_i .
\]

Then the exact first nonzero total degree of its determinant is

\[
\boxed{\nu(M_C)=4k-4, \quad \operatorname{corank}M_C(0,0)=k-1.}
\]

The generic rank-defect lower bound is \(2k-2\), so the extra delay is \(2k-2\), arbitrarily large. All entries of \(C\) are positive, and the support graph of \(\left(\begin{smallmatrix}0&I\\C&0\end{smallmatrix}\right)\) is one strongly connected component with a full two-cycle packing.

This shows the positive Gram conclusion in R284AJ (\(\nu=2(m-\mathrm{rank}\,C)\) for \(C=UU^T\)) depends essentially on the symmetric Gram structure.

## 2. Construction and exact rank

Let \(a=(1,\ldots,1)\in\mathbb Q^{k+1}\). Let \(e_j\), \(1\le j\le k\), denote the standard vectors on the final \(k\) coordinates and write \(b_j=a+e_j\).

Define \(U\) by \(k\) consecutive rows equal to \(a\), followed by \(b_1,\ldots,b_k\). Define \(V\) by \(b_1,\ldots,b_k\), followed by \(k\) rows equal to \(a\). Every factor entry is \(1\) or \(2\).

The \(k+1\) vectors \(a,b_1,\ldots,b_k\) are independent: subtracting \(a\) from the latter gives independent standard vectors. Consequently each factor has column rank \(k+1\); since \(V^T\) has full row rank, \(UV^T\) has exact rank \(k+1\).

Write \(J=1_k1_k^T\). Multiplication gives

\[
\boxed{C=
\begin{pmatrix}
(k+2)J&(k+1)J\\
(k+3)J+I_k&(k+2)J
\end{pmatrix}.}\tag{AK1}
\]

Every entry is positive.

## 3. Complete principal-minor certificate

Let \(S\subseteq\{1,\ldots,2k\}\). If \(S\) contains two top-block indices, the corresponding rows of \(U_S\) are identical; hence \(\det(C[S,S])=0\). If \(S\) contains two bottom-block indices, the corresponding rows of \(V_S\) are identical and the same conclusion follows. Every subset of three or more indices has one of these properties; therefore **all principal minors of order at least three vanish**.

All one-index minors equal \(k+2\). A pair wholly inside a single block has determinant zero. For one top index \(i\) and one bottom index \(k+j\), formula (AK1) yields

\[
\det C[\{i,k+j\},\{i,k+j\}]
=(k+2)^2-(k+1)(k+3+\delta_{ij})
=\boxed{1-(k+1)\delta_{ij}}.\tag{AK2}
\]

For \(k\ge2\) this is \(1\) if \(i\ne j\) and \(-k\) if \(i=j\), both nonzero. Thus the maximum nonzero principal order is precisely \(d(C)=2\).

The identity proved in R284AJ, valid as a polynomial even at zero edits, is

\[
\det M_C(u,v)
=\det(\operatorname{diag}(x)-C)
=\sum_{S\subseteq[m]}(-1)^{|S|}\det C[S,S]
\prod_{\ell\notin S}x_\ell.\tag{AK3}
\]

Substituting the complete minor classification gives the closed expression

\[
\boxed{\begin{aligned}
\det M_C(u,v)
={}&\prod_{\ell=1}^{2k}x_\ell
-(k+2)\sum_{i=1}^{2k}\prod_{\ell\ne i}x_\ell\\
&+\sum_{i,j=1}^{k}\bigl[1-(k+1)\delta_{ij}\bigr]
\prod_{\ell\notin\{i,k+j\}}x_\ell,\qquad x_i=u_iv_i .
\end{aligned}}\tag{AK4}
\]

The last term has total edit degree \(2(2k-2)=4k-4\). Its \(k^2\) monomials are distinct and have nonzero coefficients; hence there is no cancellation across named monomials. This proves the main theorem for every \(k\ge2\), without finite-enumeration assumptions.

At zero edits, the two-layer off-diagonal matrix has rank \(m+\mathrm{rank}(C)=3k+1\) and order \(2m=4k\), giving the stated corank \(k-1\). Because \(C>0\), all named bipartite directions are present and the graph has a full cycle cover.

## 4. Exact full-rank criterion for nonsymmetric two-sided factors

For arbitrary full-column-rank \(U,V\in\mathbb Q^{m\times r}\), \(C=UV^T\), and any set \(S\) of size \(r\),

\[
\boxed{\det C[S,S]=\det(U_S)\det(V_S).}\tag{AK5}
\]

Because \(\mathrm{rank}(C)=r\), the largest nonsingular principal size \(d(C)\) equals \(r\) **if and only if** the row matroids of \(U\) and \(V\) have a common \(r\)-element basis.

A common basis is an exact certificate that \(\nu(M_C)=2(m-r)\). When no common basis exists, \(d(C)<r\) and the determinant response is delayed. For orders below \(r\), the Cauchy–Binet sums may have algebraic cancellations even when both restricted row ranks are full. Thus a failed common-basis test identifies a genuine obstruction but need not give the exact value of \(d(C)\); our repeated-row construction resolves it using the explicit two-index coefficients (AK2).

This criterion generalizes the Gram case: if \(V=U\), the factors have the same row bases and the rank-\(r\) principal minors are squares of nonzero determinants.

## 5. Positive stable feedback Port realization

Use the R284AB/R284AJ gated-feedback complement without changing its assumptions. Let \(q=2m=4k\), \(K=q+1\), \(N_C=\bigl(\begin{smallmatrix}0&I_m\\C&0\end{smallmatrix}\bigr)\), \(R=\max_i\sum_j(N_C)_{ij}\), and

\[
c=\frac1{16(K+R+1)},\qquad 0\le t_i\le c,\qquad
H(t)=cJ_K+c\,\mathrm{blockdiag}(N_C,0)+\mathrm{diag}(t_1,\ldots,t_q,0).
\]

Every entry of \(H(t)\) is strictly positive, and every row sum is strictly less than one. Subtract its final row from each preceding row to obtain

\[
\boxed{\det H(t)=c\det(cN_C+\mathrm{diag}(t))
=c\det(\mathrm{diag}(t_it_{m+i})-c^2C).}\tag{AK6}
\]

In (AK4), the size-two minor coefficients are scaled by \(c^4\) and the outer factor contributes another \(c\). Thus the first nonzero total edit degree remains \(4k-4\).

With \(g=1/16\), \(\delta=1/(256K)\), define

\[
A_{\mathrm{Port}}=
\begin{pmatrix}
I_K-\delta J_K&-H(t)&0\\
-\delta J_K&I_K-\delta J_K&-gI_K\\
-gI_K&0&0
\end{pmatrix}.
\]

The internal nonnegative feedback block is strictly substochastic (\(\delta K+g<1\)); its strongly connected support is inherited from positive \(H\) and \(\delta J\). The exact gated determinant identity is

\[
\boxed{\det A_{\mathrm{Port}}=(-1)^K g^{2K}\det H(t).}\tag{AK7}
\]

This is a signed *observation complement* built from positive, stable feedback weights. Its auxiliary channel count is not an extra native spatial axis. P000 remains a six-axis Cell relational ontology. The scalar determinant observer is not used as a lossy replacement for path, branch or full future-operation information.

## 6. Reproducibility and checks

Published checker: R284AK_nonsymmetric_matroid_gap_checker.py. Published deterministic result: R284AK_exact_verification.json.

Actual exact local execution uses SymPy Integer and Rational arithmetic. For \(k=2,3,4,5\), it checks every one of \(2^{2k}\) principal subsets, amounting to **1,360** principal determinant comparisons. It checks **54** cross-block coefficients, **12** full \(4k\)-order direct pencil determinants against (AK4), and **four** complete gated Port determinants of orders \(27,39,51,63\), including positive-entry and row-sum assertions. All pass; no numerical approximation or randomized sample is used. Finite tests check the implementation and examples; the quantified theorem follows from §§2–5.

Original dependencies and provenance: R284AB gated complement, R284AJ AJ1–AJ3 and the frozen scientific input named above. Independent mathematical review: NOT_REVIEWED. This document is independent portable research, not a formal CLAIM, Result, Review, P000 revision or Foundation promotion.

## 7. Next useful problem

For a general strictly positive nonsymmetric rational factorization \(C=UV^T\), when the maximum-rank common-basis test fails, determine whether \(d(C)\) can be certified in polynomial time or with bounded-parameter graph/factor structure without enumerating all principal sets. Distinguish common-row matroid independence from signed cancellation in lower-order Cauchy–Binet sums. Compare exact bit complexity with R284Y matching minors and R284AE Schur graded response. For observer compression, state the future edit operations and prove typed fiber invariance before dropping a branch or joint Port relation.
