# R284T — Joint bordered-determinant certificates for collapsing Port comparison grids

2026-11-18. Status: **AUTHOR_PROVED / EXACT_FRACTION_EXAMPLES_PASSED / NOT_REVIEWED**.

Frozen scientific input: 43ec6098b1330ae86d0a7863be336c5d97f6ef34. Exact predecessor: R284S at d158b4942c8602c21ee21b0967d5a8fcc858ee2f, research_notes/portable_direct/R284S_RANK_ONE_QUADRATIC_OBSTRUCTION_GRID_REDUCTION_20261118.md. Dependencies: R281 (future-operation observer relevance), R282 (multiaffine determinant presentations), R284/R284R (1/2/3-point tensor grids), R284S (single-edit rank-one quadratic coefficient). This result concerns **auxiliary, named, nonnegative-rational BRC Port systems** with additive edits and explicitly matched scalar outputs. No transfer to native X6 dynamics, branch identity or provenance-sensitive operations is inferred.

## 1. A full observer comparison is one bordered determinant

For each model h=1,2 and matched observer q, let

\[
M_h(x)=I-W_h-\sum_i x_i e_{u_{hi}}e_{v_{hi}}^\top,\quad
F_{h,q}(x)=a_h^\top M_h(x)^{-1}b_h.
\]

Each named edit contributes one rank-one update per model; endpoints may differ across models. On the common stable domain, let \(D_h=\det M_h\), \(N_h=a_h^\top\operatorname{adj}(M_h)b_h\), \(P_q=N_1D_2-N_2D_1\). These are **unnormalized** determinant presentations; multiplying both numerator and denominator of either model by the same nonzero constant preserves every degree/zero certificate.

Form the bordered matrix

\[
K_q(x)=\begin{pmatrix}
M_1(x)&0&b_1\\
0&M_2(x)&-b_2\\
a_1^\top&a_2^\top&0
\end{pmatrix}.
\]

**Theorem R284T-A.** For every pair of rational Port systems,

\[
\boxed{P_q(x)=-\det K_q(x).}\tag{1}
\]

If an edit \(x_i\) is present in both models, it occurs in exactly two distinct columns of \(K_q\). With zero \(x_i\), replace column \(v_{1i}\) by the embedded \(e_{u_{1i}}\) and column \(n_1+v_{2i}\) by the embedded \(e_{n_1+u_{2i}}\); denote this modified matrix by \(K^{[i,i]}_q(z)\), where \(z=(x_j)_{j\ne i}\). Then

\[
\boxed{[x_i^2]P_q(x_i,z)=-\det K^{[i,i]}_q(z).}\tag{2}
\]

For an edit occurring in just one reduced model, the quadratic coefficient is automatically zero. No inverse of the bordered matrix and no expansion of the multivariate rational response is needed.

**Proof.** When \(M_1,M_2\) are invertible, take the Schur complement of \(\operatorname{diag}(M_1,M_2)\) to obtain \(\det K_q=-D_1D_2(F_{1,q}-F_{2,q})\). This proves (1) on a nonempty open set; both sides are polynomials and hence the identity holds identically. Each of the two edited columns equals its zero-edit column minus \(x_i\) times the corresponding unit vector. By determinant multilinearity, the quadratic coefficient selects both edited components. The two negative signs cancel; combine with (1) to get (2). The identity also holds when \(K_q\) is singular. QED.

**Observer reduction is essential.** For output q and model h, set to zero every edit outside R281's exact future-observer relevance set \(R_{h,q}\) *in that model's matrix*, before building \(K_q\). R281 says this leaves the rational readout unchanged for the full declared additive operation language. Write the resulting comparison polynomial \(P_q^*\), which now has R284R's degree bounds: 0 outside \(U\), 1 in \(U\setminus B\), 2 in \(B\). An unreduced determinant may retain invisible denominator factors; applying reduced-grid bounds to such a raw determinant would be invalid.

At stable \(z\), the R284S rank-one quantities \(A_h,B_h,C_h\) satisfy

\[
[x_i^2]P_q^*(x_i,z)
=D_1^*(0,z)D_2^*(0,z)
\big[(A_1-A_2)C_1C_2+B_2C_1-B_1C_2\big].\tag{3}
\]

Thus (2) is a direct, inverse-free determinant certificate for R284S's exact quadratic obstruction.

## 2. Theorem R284T-B: a simultaneous finite zero-minor certificate

Take R284R's shared-output grid with \(l=|U\setminus B|\) originally linear coordinates, \(b=|B|\) potentially quadratic coordinates and a fixed zero node in each irrelevant coordinate. Every selected rational product-grid point must be jointly stable; small nonnegative distinct nodes suffice. Choose any ordering \(i_1,\ldots,i_b\) of B.

At stage k evaluate the exact quadratic coefficient \(S_{q,i_k}(z)=-\det K_q^{[i_k,i_k]}(z)\) for **every declared output q**, at all product-grid points of the other coordinates, taking 2 nodes for each of the l originally linear coordinates and each previously certified candidate \(i_1,\ldots,i_{k-1}\), 3 nodes for each uncertified candidate \(i_{k+1},\ldots,i_b\), and 1 node for irrelevant coordinates.

If all those exact determinants vanish, then \(S_{q,i_k}\equiv0\) for every output and all remaining edit values, so \(\deg_{x_{i_k}}P_q^*\le1\) globally. Continue in order. If all b stages pass, equality of the two Port models at just \(2^{l+b}\) product-grid nodes is equivalent to equality of their complete rational response functions on the common admissible additive-edit domain.

**Proof.** Prior stages bound the polynomial degree of \(P_q^*\), and hence of its coefficient \(S_{q,i_k}\), by at most 1 in all previously certified coordinates, 2 in all remaining candidates, 1 in originally linear coordinates and 0 in irrelevant coordinates. Exact vanishing on the stated tensor grid forces the coefficient polynomial to be identically zero by multivariate interpolation. Induct over k. After the b stages every \(P_q^*\) is multiaffine. The final two-node tensor grid therefore proves \(P_q^*\equiv0\), which is equivalent to rational response equality wherever the two denominators are nonzero. QED.

For b passing stages, the exact maximum number of *quadratic-minor sites* is

\[
\sum_{k=1}^{b}2^l2^{k-1}3^{b-k}=2^l(3^b-2^b).\tag{4}
\]

Together with \(2^{l+b}\) final equality sites this totals \(2^l3^b\): the staged certificate **does not itself claim a generic one-shot grid-count speedup**. Its scientific gain is a reusable degree-drop certificate involving a single \((n_1+n_2+1)\)-determinant per candidate site, without multivariate rational expansion. Structural zero-minor identities can bypass sites entirely. For a family of subsequent comparisons subject to the same certified degree identities, only the reduced equality grids are needed. Operation counts, exact determinant size, coefficient heights, preprocessing and reuse need accounting before a wall-clock advantage can be claimed.

For binary p-adic interpolation, when all quadratic identities are globally certified, using nodes \(0,1/Q\) (Q sufficiently large and odd) in every retained coordinate makes the interpolation loss \(\kappa=0\), compared with the possible R284R three-node loss \(b\). R284R's target denominator-valuation stratum and sample precision still govern any mod-\(2^k\) consequence.

A nonzero exact value of a substituted determinant is a **witness that this polynomial's quadratic degree does not collapse**. It does not prove that every conceivable two-node test fails.

## 3. Exact two-edit witness: 9 nodes reduce to one after polynomial certification

In each model use Ports \(0,1,2\), observer \((0,0)\), baseline edges \(0\to1=a=1/4\), \(2\to0=c=3/8\), and \(0\to0=t_h\), with \(t_1=1/4,t_2=0\). Both systems admit the same two *named* edits \(x:1\to2\), \(y:0\to0\). For \(0\le x,y\le1/10\) all rows are strictly substochastic; both edits are on observer-relevant cycles in both graphs.

Exact inversion gives

\[
F_1(x,y)=\frac1{3/4-y-3x/32},\qquad
F_2(x,y)=\frac1{1-y-3x/32}.
\]

Here \(N_1=N_2=1\), \(D_1=3/4-y-3x/32\), \(D_2=1-y-3x/32\), hence

\[
\boxed{P(x,y)=D_2-D_1\equiv1/4.}\tag{5}
\]

R284R's graph-only rule would use \(3\times3=9\) comparison nodes; the *verified constant cross-product* permits **one node** for this fixed pair. At \(x=y=0\), outputs \(4/3\) and \(1\) correctly distinguish the models. This is a pair-specific polynomial certificate, not a universal one-point Port sampling theorem.

For a discriminating negative control, reuse R284S's single-edit three-Port pair: model 1 uses \((a,b,\gamma)=(1/4,1/4,0)\); model 2 uses \((1/4,15/64,1/4)\). Exact calculation yields

\[
P(x)=x/256-x^2/64,\qquad [x^2]P=-1/64,
\]

and the substituted-column determinant gives the same nonzero coefficient. The negative control prevents a false universal cycle-bearing degree-collapse inference.

## 4. Executed verification and next scientific unit

Reproduction script: research_notes/portable_direct/R284T_joint_quadratic_coefficient_certificate.py (Python standard library Fraction and exact Gauss–Jordan / determinant elimination). Evidence: research_notes/portable_direct/R284T_joint_quadratic_certificate_verification.json. The actually executed assertions passed: all nine two-variable inverse/formula/constant-polynomial checks; nine 7×7 bordered-determinant identities; six two-column coefficient determinants matched against independent exact second differences; one nonzero quadratic coefficient plus four control samples. The tests establish these finite examples; Theorems A/B have the separate complete algebraic proofs above.

**Next question.** Find a graph-cut or sparse symbolic certificate for the identically vanishing substituted-column determinant as a polynomial in the other named edits, without a full tensor grid. Quantify complete exact bit complexity including graph reduction and repeated pair comparisons. For stronger native claims, define a provenance- and future-operation-preserving X6 observer bridge first.
