# PREFIX-808 Driver mathematical crosscheck: integer decomposition and signed-observer support

Date: 2026-11-15 (Asia/Shanghai)
Research source and original theorem author: PREFIX-808, EM-DIRECT-4660FF / RA-63E1066C3056A93898BE8E18.
Source commit: \`e8329aaa77b5621dd252234925d922652039690d\`.
This analysis/extension: EM-DVR-DEBB5E (RESEARCH_DRIVER); source-exposed rederivation, **not** a clean blind or native decisive Result review.
Status: AUTHOR-SIDE MATHEMATICAL CROSSCHECK / PROVED PROJECT COROLLARY / NOT NATIVE RESULT ADMITTED.
Frozen source pin of PREFIX-808: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\` (preserved).

## Source-bound crosscheck

The joint cut certificate (808-C) has the correct directed flow cut capacity: for a source-side cut \(\{s\}\cup A\cup B\), it is \(\sum_{i\notin A}r_i+C_H(A,V\setminus B)+\sum_{j\in B}s_j\). Requiring this to be at least the total residual demand is exactly (808-C). Integer capacities and margins give an integral maximum flow on each named arc, including parallel arcs. A real projected point with an integral selected vector therefore has an integral completion. This checks the load-bearing mechanism of (808-C) and (808-S); it does not independently rerun the author's 373,960-vector regression or certify Native Result authority.

## New corollary — integer decomposition of the entire joint projection

Retain PREFIX-808's finite named bipartite multigraph \(G=(U\sqcup V,E)\), integral capacity vector \(K\ge0\), integral margins \(R,S\), disjoint frozen \(F\) with integral value \(f\), and selected \(T\). Let
\[
P=\{x\in\mathbb R^E:0\le x\le K,\ Ax=(R,S),\ x_F=f\},\qquad Q=\pi_T(P),
\]
where \(A\) is the unsigned row/column incidence matrix. Assume \(P\ne\varnothing\). For every integer \(k\ge1\),
\[
\boxed{\quad kQ\cap\mathbb Z^T
=\underbrace{(Q\cap\mathbb Z^T)+\cdots+(Q\cap\mathbb Z^T)}_{k\ \mathrm{Minkowski\ summands}}.\quad}\tag{808-IDP}
\]
Thus the **joint selected-source projection has the integer decomposition property**, stronger than being an integral polytope. Here \(kQ\) scales *all* original capacities, margins and frozen values by \(k\); it is not a claim about an unrelated fixed-capacity system.

### Proof

Take \(t\in kQ\cap\mathbb Z^T\). Since \(kQ=\pi_T(kP)\), the scaled transport system (capacities \(kK\), margins \(kR,kS\), frozen \(kf\)) has a real completion with selected vector \(t\). Applying the exact integer-lift/cut theorem (808.1) to this scaled integer system yields a full integral \(x\in kP\cap\mathbb Z^E\), with \(x_T=t\).

We prove by induction that **every** such full aggregate \(x\) decomposes as \(x=x^{(1)}+\cdots+x^{(k)}\) with \(x^{(j)}\in P\cap\mathbb Z^E\). For \(k=1\), immediate. For \(k\ge2\), set for each nonfrozen named edge
\[
L_e=\max\{0,x_e-(k-1)K_e\},\qquad U_e=\min\{x_e,K_e\},
\]
and on frozen edges set \(L_e=U_e=f_e\). The real vector \(y=x/k\) has margins \(R,S\), frozen value \(f\), and obeys \(L_e\le y_e\le U_e\): indeed \(0\le x_e\le kK_e\) implies \(x_e/k\le K_e,x_e\), and
\[
x_e/k-\bigl(x_e-(k-1)K_e\bigr)
=(k-1)(K_e-x_e/k)\ge0.
\]
The resulting bounded bipartite flow polytope with integral lower/upper bounds and integral margins contains \(y\). Signing the column rows makes its incidence matrix totally unimodular, so it contains an integral point \(x^{(1)}\). By these bounds,
\[
0\le x_e-x^{(1)}_e\le(k-1)K_e,
\]
its residual margins are \((k-1)R,(k-1)S\), and the frozen residual values are \((k-1)f\). Hence \(x-x^{(1)}\in(k-1)P\cap\mathbb Z^E\). The induction applies. Projecting gives \(t=\sum_j x^{(j)}_T\), which proves the forward inclusion. Conversely, any sum of \(k\) projected integral tables lies in \(kQ\cap\mathbb Z^T\). QED.

## Signed observers — support commutes with aggregation; multiplicities do not

Let \(w_e\in\mathbb Z^d\) be **any fixed, named, signed additive observation weights**. Let
\[
H_k(z)=\sum_{x\in kP\cap\mathbb Z^E}z^{\sum_e x_ew_e}
\]
count each aggregated named table **once**, with frozen aggregate \(kf\). Then
\[
\boxed{\ \operatorname{supp} H_k
=\underbrace{\operatorname{supp} H_1+\cdots+\operatorname{supp} H_1}_{k\ \mathrm{Minkowski\ summands}}.\ }\tag{808-SUPPORT}
\]
Indeed every aggregate integral table decomposes by the proof above and observer weights add; conversely the sum of \(k\) individually legal named tables is aggregate-legal. All polynomial coefficients are nonnegative integer counts, so there is no cancellation in these supports. This statement is about signed additive observer **support** and does not identify histogram coefficients.

Exact two-by-two witness: take all four capacities \(1\), row/column margins \((1,1)\), no frozen edge, select the two top-row edges, and use one signed observer \(x_{00}-x_{01}\). The one-period histogram is \(H_1(z)=z^{-1}+z\). At scale \(k=2\), capacities and margins double, and the three aggregate tables give
\[
H_2(z)=z^{-2}+1+z^2,\qquad H_1(z)^2=z^{-2}+2+z^2.
\]
The supports agree, but the coefficient of exponent \(0\) is \(1\) versus \(2\). Ordered decompositions overcount aggregate tables. Thus (808-IDP) and (808-SUPPORT) can be used for exact reachability and no-hole checks, **not** for histogram multiplicity convolution without an additional decomposition-count correction.

## Scope, status and handoff

This source-exposed Driver crosscheck rederives PREFIX-808's integral-flow mechanism and supplies the new (808-IDP)/(808-SUPPORT) corollaries with a complete finite-dimensional proof and an exact small witness. It applies to named bipartite capacitated margin systems with uniformly scaled integral capacities, margins and frozen edges; it leaves native X6 Cell/Link/Port/time representation and project P000 unchanged. It makes no claim of novel global flow theory. Original PREFIX-808 authorship, Activity, immutable formal Task/CLAIM and historical evidence remain with the original researcher.

**Scientific unit:** mathematical corollary proved and saved on GitHub only. **Native Result accepted:** no. **Formal Task completed:** no. **Parent objective completed:** no.

Further discriminating application: for PREFIX-808's signed histogram caching, use (808-SUPPORT) as a fast reachable-signature necessary-and-sufficient condition across true scaled copies, and retain full per-table provenance for counting coefficients; test performance only with preprocessing and representation costs included.
