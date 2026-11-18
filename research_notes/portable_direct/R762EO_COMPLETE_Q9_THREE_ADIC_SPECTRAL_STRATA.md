# R762EO — Complete q=9 three-adic spectrum including the previously unresolved high stratum

**Date:** 2026-11-18. **Task line:** RS-X6-TRIADIC-CLOSURE-DYNAMICS. **Identity provenance:** EM-X6-3050F6. **Status:** EXACT_CERTIFICATE_DERIVED_FROM_R762EM / AUTHOR_PROVED / NOT_REVIEWED.

## Exact result

In the full three-coordinate **positive terminal BRC** group ring
\[
R=\mathbb Z[(\mathbb Z/9\mathbb Z)^3],\qquad
P=1+X+Z+XY+YZ+XYZ,
\]
let \(\lambda_{ijk}=P(\zeta_9^i,\zeta_9^j,\zeta_9^k)\), \(0\le i,j,k<9\), with \(v_3(3)=1\). The 729 characters have the **complete exact 3-adic valuation distribution**
\[
\boxed{
\begin{array}{c|r|r}
v_3(\lambda)&\text{distinct eigenvalues}&\text{characters counting multiplicity}\\\hline
1/3&90&486\\
2/3&24&144\\
1&12&39\\
+\infty\;(\lambda=0)&1&60\\\hline
\text{total}&127&729
\end{array}}
\]
The high stratum left as \(v_\pi\ge6\) or zero in R762EA, at q=9, consists **exactly** of 39 nonzero values of valuation 1 and 60 zero characters. In particular there is no nonzero q=9 eigenvalue with \(v_3>1\).

## Integer Newton-polygon certificate

Reuse the **exact immutable** R762EM factor list at GitHub commit
\`b21958c0178439717e77947be3cfee43570533a6\`,
path \`research_notes/portable_direct/R762EM_Q9_SPECTRAL_EVIDENCE.json\`.
That certificate enumerates 27 rational irreducible factors \(F_O(T)\), their degrees, and their occurrence multiplicities \(m_O\), with
\[
\mu_9(T)=\prod_OF_O(T),\quad \deg\mu_9=127,\quad
\chi_9(T)=\prod_OF_O(T)^{m_O}.
\]

**Proof.** The standard Newton polygon theorem for a polynomial over the complete valued field \(\mathbb Q_3\) says that each lower-hull segment of horizontal length \(h\) and slope \(-s\) contributes precisely \(h\) roots, counted with algebraic multiplicity, of valuation \(s\). This theorem applies to exact integer coefficients of each \(F_O\), and therefore also to their product. Extract the 3-adic valuation of every nonzero integer coefficient exactly; zero coefficients have ordinate \(+\infty\). For the full \(\mu_9\), the lower-hull vertices (coefficient exponent, 3-adic valuation) are
\[
\boxed{(1,58),\ (13,46),\ (37,30),\ (127,0).}
\]
The zero constant coefficient and unit coefficient of \(T^{127}\) are exact. The three hull edges have slopes \(-1,-2/3,-1/3\) and horizontal lengths \(12,24,90\), respectively. Thus the **126 distinct nonzero roots** of \(\mu_9\) have valuations \(1,2/3,1/3\) with counts \(12,24,90\).

For the *character multiplicities* one must not multiply these aggregate counts by a uniform factor: the R762EM factors have different \(m_O\). Apply the same exact lower-hull algorithm to **each** \(F_O\) and sum (edge horizontal length) multiplied by its recorded \(m_O\). This yields 39 characters at valuation 1, 144 at 2/3 and 486 at 1/3. The separate \(F_O(T)=T\) contributes 60 zero characters. The count is \(39+144+486+60=729\), establishing the table. QED.

The Newton polygon also supplies an exact norm check:
\[
v_3\!\left(\left|\prod_{\lambda\ne0,\;\lambda\text{ distinct}}\lambda\right|\right)
=12(1)+24(2/3)+90(1/3)=58;
\]
this matches the coefficient of \(T^1\) in \(\mu_9(T)\), whose valuation is precisely 58.

## Verification and scope

All calculations used exact 3-divisibility of integer coefficients and rational slopes; no floating-point evaluation of complex roots was used. Direct author-side code read R762EM's source JSON at its immutable commit through the authorized repository connector, reconstructed \(\mu_9\), obtained all four vertices, and independently aggregated the 27 factor polygons with their recorded multiplicities. Accompanying \`R762EO_VERIFY.py\` reproduces the calculation from the exact predecessor JSON; \`R762EO_EVIDENCE.json\` records the computed numbers, provenance, and scope.

This is a **derived spectral classification**, relying on the author-proof/exhaustive character factorization in R762EM; that antecedent and the present result remain independently \`NOT_REVIEWED\`. The P000 signed native Cell/Link/Port event alphabet, triadic closure semantics, future-permission path carriers and V17/V29/V39 transport do not follow from valuations of this positive terminal BRC projection.

## Next research question

Use the complete q=9 valuation strata and the order-127 single-return reconstruction from R762EN to bound or witness the integer content of every coefficient vector \(P_9^n\) at arbitrary \(n\). In parallel study a source-typed native signed Cell/Link/Port event licence and the observer-safe differences from this terminal spectrum. The original P000 and taskbook science remain frozen; no new CLAIM, Source progress, Result, Review, or Foundation admission is represented here.
