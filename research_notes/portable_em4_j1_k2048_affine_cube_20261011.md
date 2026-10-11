# J1 k=2048: 23-dimensional affine cube of conditional minimum escape

Status: AUTHOR_DRAFT / UNREVIEWED / NOT_ADMITTED (independent auxiliary finite-field arithmetic; no formal CLAIM or P000 native transfer).

Source fixed at analysis start: GLOBAL_KNOWLEDGE_V1 main@a9dfb3ab0c9b25fac11dced6ac076872bf174eec; Enterprise Math main@8d21e1bd33cfe9d64058afee266c4de328c4adf5.

## Inherited setup and bound

D_j=(2j-1)^2+32768, 1<=j<=2048. T is the complement of the union of the specific 69 disjoint odd square-product relations in the previously preserved k2048 39-core AUTHOR_DRAFT; |T|=1549. The observer O_T requires Legendre_p(D_j)=-1 for all j in T. Its rank is 1546. On permitted primes p>4098, E=4P+2Z counts original input multiplicity; under O_T, Z=0. The previous exact 39 weighted parity-core certificate proves P>=123, and an attainable witness reaches P=123, giving E_min=492 conditional on O_T. This is NOT the unconditional bound, still 276<=min E<=364.

## New theorem and proof certificate

There are at least 2^23=8,388,608 distinct *complete* attainable discriminant-sign states with O_T and P=123, forming an affine binary cube. In the ascending list of 1656 odd prime factors of all D_j, represent each exponent-parity row by a_j in F2^1656. Use baseline h0 and 23 explicit generator vectors g_i from the companion CUBE_WITNESSES.json (or local author evidence package). For each original index j, set its 23-bit response mask m_j=(a_j·g_i)_i and baseline symbol bit b_j=a_j·h0 (0=Legendre positive, 1=negative).

A second factorization/audit independently verified exactly 24 nonempty mask buckets: m=0 contains 92 positive and 1894 negative entries; the other 23 masks are precisely the 23 distinct singleton masks 2^i, with each such bucket having equal positive and negative counts. Across nonzero masks the baseline has 31 positives and 31 negatives. For every selection s in F2^23, replacing h0 by h0+sum(s_i*g_i) flips either none or all symbols in each singleton bucket, preserving their positive counts. Hence P(s)=92+31=123 for all 2^23 selections. Every T-row has m_j=0 and b_j=1, so O_T is preserved. Every singleton mask occurs, so the full sign patterns are pairwise distinct (not merely two factorizations of one state). The full row rank is 1655, so each attainable complete sign pattern has natural prime density 2^-1655 by quadratic reciprocity, CRT and Dirichlet's theorem. Thus:

  2^-1632 <= density(O_T AND E=492).

Previous bound 2^-1651 is improved by the exact factor 2^19.

## New rigidity upper bound

Equality in the previous 39 weighted-core bound 39<=sum(m_r e_r)<=sum(w_r e_r)=P-84 forces all 99 strict residual classes with m_r<w_r to remain at their own optimum. Their residual readout vectors have rank 68 in the 109-dimensional conditional character space. Core exact-one propagation, only when forced, supplies four further independent equations. Therefore complete minimizing sign states number at most 2^37 and

  2^-1632 <= density(O_T AND E=492) <= 2^-1618;
  2^-86 <= Pr(E=492 | O_T) <= 2^-72.

These are **bounds**, not an exact density calculation; the upper density proof depends on the specific prior 39-core certificate and is not a new universal statement.

## Verification and scope

Local package em4_j1_k2048_affine_cube_20261011.zip SHA256=63da706ed95dfdc781b17c33f7a9fb7560bd4b63844f66a881db369b05595989. A stdlib checker fully refactors the original D_j, checks all 69 square-product witnesses, all 39 weighted cores, ranks 1655/1546/68 and four extra equations; a separate SymPy checker independently refactors all D_j and verifies the raw 23-vector response mask histogram. Both PASS. The local package also contains PROOF.md, unchanged BASE_CERTIFICATE.json, CUBE_WITNESSES.json, verify.py, audit_direct.py, RESULTS.json and SHA256 manifest. This Source note alone does not imply the full code/bundle was uploaded to Source.

BRC reuse: the existing typed positive-integer branch count maps each original input to a unit branch; the algebraic +/- Legendre symbols are labeled constraints, **not** positive masses to cancel. Response-bucket balancing is sufficient for this particular total-positive-count observer on the affine cube but not for arbitrary downstream label queries. No original P000 six-dimensional Cell transfer claimed.

Next: exact count of all conditional minimizers, e.g. a certified enumerator on the remaining 37 dimensions; then controlled relaxation of O_T for possible new unconditional bounds. Formal H/J/C prior-art completion is separate and is not reopened.