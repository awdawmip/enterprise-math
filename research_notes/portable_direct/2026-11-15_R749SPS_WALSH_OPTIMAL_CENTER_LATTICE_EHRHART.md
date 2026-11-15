# R749SPS — Exact lattice quantization and Ehrhart theory of the Walsh minimax-center polytope

**Date:** 2026-11-15. **Status:** AUTHOR_EXACT_NOT_REVIEWED. **Frozen scientific pin:** \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. **Predecessor:** R749SPR, PR #2457, immutable commit \`7e876e05511b861a72cc1f03b5a880faba71a3b5\`. Scope: frozen auxiliary 16-atom Walsh source model, retaining all signed atoms and source total-variation observers.

## Exact object

At \((t,s)=(1/10,1/2)\), R749SPR proves \(\rho=\rho^{\rm cal}=9/20\) and identifies the complete calibrated minimax-center polytope \(K\) in coordinates \(X=(H,U,V)=(10h,10u,10v)\), with \(w=z=0\). Its eight inequalities are

\[
\begin{array}{rrrr}
-H-U-V\ge-2,&-H-U+V\ge-2,&-H+U-V\ge-2,&-H+U+V\ge-2,\\
 H-U-V\ge-2,& H-U+V\ge-4,& H+U-V\ge-4,& H+U+V\ge-2.
\end{array}
\]

The new question is how many *distinct exactly optimal* centers exist at a given coefficient resolution, together with an explicit approximation to each continuum optimum.

## Theorem 1 — Three absolute-value constraints

The exact eight-facet set admits the compressed **equivalent** expression

\[
\boxed{K=\{(H,U,V): H+|U|+|V|\le2,\quad H\ge |U+V|-2,\quad H\ge |U-V|-4\}.}
\]

**Proof.** The four constraints with coefficient \(-H\) are equivalent to \(H+\max_{\epsilon,\eta\in\{\pm1\}}(\epsilon U+\eta V)\le2\), hence \(H+|U|+|V|\le2\). The two constraints \(H-U-V,H+U+V\ge-2\) give \(H\ge |U+V|-2\). The two constraints \(H-U+V,H+U-V\ge-4\) give \(H\ge |U-V|-4\). Conversely, expanding the absolute values yields all eight original constraints. This is only a reversible presentation of the whole signed coefficient polytope, not an observer quotient. QED.

## Theorem 2 — Exact optimal-grid count at every positive resolution

For each integer \(n\ge0\), put \(L_K(n)=\#(nK\cap\mathbb Z^3)\). Then

\[
\boxed{L_K(n)=\frac{46n^3+33n^2+17n+3}{3}.}
\]

For \(n\ge1\), this is exactly the number of distinct calibrated minimax centers with \(h,u,v\in\frac1{10n}\mathbb Z\). Every counted center has worst-case TV risk **exactly** \(9/20\) against the full frozen source fiber.

The volume is \(\operatorname{vol}(K)=46/3\), normalized volume \(3!\operatorname{vol}(K)=92\), and the Ehrhart \(h^*\)-polynomial is
\[
\boxed{h_K^*(z)=1+29z+53z^2+9z^3.}
\]
For all integers \(n\ge1\), interior and boundary counts are respectively
\[
\#(\operatorname{int}(nK)\cap\mathbb Z^3)=\frac{46n^3-33n^2+17n-3}{3},\quad
\#(\partial(nK)\cap\mathbb Z^3)=22n^2+2.
\]
Thus at resolution \(n=1\) there are 33 exact optimal centers (9 interior, 24 boundary).

**Proof.** The predecessor's complete three-dimensional polytope has these 11 *integral* vertices:
\[
\begin{gathered}
(-2,-1,1),(-2,1,-1),(-1,-2,1),(-1,-1,2),(-1,1,-2),(-1,2,-1),\\
(0,-2,0),(0,0,-2),(0,0,2),(0,2,0),(2,0,0).
\end{gathered}
\]
Consequently \(K\) is a full-dimensional lattice polytope, so the standard integral Ehrhart theorem states \(L_K(n)\) is a polynomial of degree three in \(n\). Its values at \(n=0,1,2,3\) determine the polynomial for every nonnegative integer \(n\).

For integer \(H,U,V\in nK\), Theorem 1 yields precisely
\[
H_{\min}=\max\{|U+V|-2n,\ |U-V|-4n\},\quad
H_{\max}=2n-|U|-|V|.
\]
When the interval is nonempty, the first lower bound gives
\(|U|+|V|+|U+V|\le4n\), hence \(|U|,|V|\le4n\). Therefore an **exhaustive** exact finite sum is
\[
L_K(n)=\sum_{U=-4n}^{4n}\sum_{V=-4n}^{4n}
\max\{0,H_{\max}-H_{\min}+1\}.
\]
Integer-only evaluation for \(n=0,1,2,3\) returns \(1,33,179,531\). Interpolating the unique cubic yields \((46n^3+33n^2+17n+3)/3\). The executable verifier uses only integer arithmetic, also checks every enumerated point against all eight original inequalities, and independently audits \(n=4,5,6,7\), returning \(1181,2221,3743,5839\).

The leading coefficient of \(L_K\) is \(\operatorname{vol}(K)\). Substitution in the standard identity \(L_K(n)=\sum_{j=0}^3h_j^*\binom{n+3-j}{3}\) gives \(h^*=(1,29,53,9)\) and \(\sum h_j^*=92\). Ehrhart–Macdonald reciprocity gives \(\#(\operatorname{int}(nK)\cap\mathbb Z^3)=-L_K(-n)\); subtraction gives the boundary formula. Injectivity of Walsh coefficient expansion identifies lattice points with distinct probability centers. QED.

## Theorem 3 — Constructive uniform quantization

For **every** real point \(X\in K\) and integer \(n\ge1\), there exists
\(X_n\in K\cap\frac1n\mathbb Z^3\) such that
\[
\boxed{\operatorname{TV}(q_X,q_{X_n})\le\frac{2}{5n},\qquad
q_X=p(1/10,1/2,H/10,U/10,V/10,0,0).}
\]
Both \(q_X\) and \(q_{X_n}\) attain the exact minimax radius \(9/20\).

**Construction and proof.** Carathéodory's theorem in three dimensions writes \(X=\sum_{i=1}^r\alpha_i v_i\), \(r\le4\), where \(v_i\) are integral vertices of \(K\), \(\alpha_i\ge0\) and \(\sum\alpha_i=1\). Apply largest-remainder rounding to the numbers \(n\alpha_i\): first floor, then allocate the remaining \(k\) units to the \(k\) largest fractional parts. This gives \(m_i\ge0\), \(\sum m_i=n\), and
\[
\sum_i|\alpha_i-m_i/n|\le\frac2n.
\]
Indeed the \(k\) largest fractional parts sum to at least \(k^2/r\), so the error is at most \(2k(1-k/r)/n\le r/(2n)\le2/n\). Set \(X_n=\sum_i(m_i/n)v_i\). It belongs to the grid and to \(K\). As all listed vertices have \(\ell^1\)-norm at most four, \(\|X-X_n\|_1\le8/n\).

For \(\Delta X=X-X_n\), exact Walsh orthogonality and atom expansion give
\[
\operatorname{TV}(q_X,q_{X_n})
=\frac1{320}\sum_{j=0}^{15}
\left|\Delta H\chi_{15}(j)+\Delta U\chi_{1}(j)+\Delta V\chi_2(j)\right|
\le\frac{\|\Delta X\|_1}{20}\le\frac2{5n}.
\]
Every constructed \(X_n\) remains in \(K\), so its calibrated source risk remains \(9/20\). QED.

## Verification, provenance and open frontier

The accompanying standalone standard-library script \`R749SPS_WALSH_OPTIMAL_GRID_EHRHART_CERT.js\` was executed with Node.js v22 using integer-only exhaustive loops and assertions. The complete JSON execution output is \`R749SPS_WALSH_OPTIMAL_GRID_EHRHART_RESULTS.json\` (PASS). The finite enumeration proves the four required Ehrhart input values exactly; **the integral Ehrhart theorem, not finite extrapolation**, establishes the formula for all \(n\). Exact all-source minimax optimality relies on the R749SPR eight-facet classification, which is author-checked and awaiting independent mathematical review. No native X6/V29/V39 operation bridge is asserted.

**Next:** determine the first combinatorial source/event wall of the continuously deformed optimal-center polytope near \((1/10,1/2)\), and the corresponding lattice or quasipolynomial census under a declared grid normalization. Preserve signed Walsh source and provenance information when investigating native X6 operations.
