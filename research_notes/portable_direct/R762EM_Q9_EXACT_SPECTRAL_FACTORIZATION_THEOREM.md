# R762EM — Exact q=9 full-three-coordinate BRC spectral factorization and optimal recurrence order

**Date:** 2026-11-18. **Task:** RS-X6-TRIADIC-CLOSURE-DYNAMICS. **Author line:** EM-X6-3050F6. **Status:** EXACT_FINITE_CERTIFICATE / AUTHOR_PROVED / NOT_REVIEWED. Follows R762EK–EL, Draft PR #2720. P000 scientific input frozen at \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json\`; taskbook frozen at \`@e3f42efac29a2da2d95be391f3231a664e2fade0\`.

## Exact theorem

Let G=(Z/9Z)^3, R=Z[G], with commuting generators X,Y,Z, and let

\[
P=1+X+Z+XY+YZ+XYZ,\qquad T_P:f\mapsto Pf.
\]

The six terms are six separately named positive BRC branches, retained as such before applying the terminal endpoint observer. T_P acts on the 729-dimensional rational group algebra Q[G]. Its eigenvalue multiset admits exactly **127 distinct** eigenvalues partitioned into **27 rational Galois orbits**. The orbit degree histogram is:

| degree over Q | number of distinct minimal factors | contribution to minimal-polynomial degree |
|---:|---:|---:|
| 1 | 3 | 3 |
| 2 | 2 | 4 |
| 3 | 4 | 12 |
| 6 | 18 | 108 |
| **Total** | **27** | **127** |

For each certificate entry O, write a_O=(a0,...,a5) for the specified representative of the eigenvalue \(\lambda_O=\sum_{h=0}^5 a_h\zeta_9^h\), d_O for its orbit size, m_O for its per-eigenvalue occurrence count, and
\(F_O(T)=\sum_{k=0}^{d_O} f_{O,k}T^k\) using the ascending coefficients in the accompanying JSON file.

The **exact rational minimal and characteristic polynomials** are thereby specified in fully factored, reproducible form:

\[
\boxed{\mu_9(T)=\prod_{O=1}^{27}F_O(T),\quad \deg\mu_9=127;}
\]
\[
\boxed{\chi_9(T)=\prod_{O=1}^{27}F_O(T)^{m_O},\quad \deg\chi_9=729.}
\]

Each F_O is irreducible over Q. In particular, T, T-3, T-6 and T²±3T+9 are among the 27 factors. The zero eigenvalue occurs exactly 60 times; this agrees with the R762ED eight-line zero-locus (8·9−12=60).

**Corollary (sharp exact linear recurrence).** The simultaneous 729 endpoint-count sequences of P^n satisfy a single integer-coefficient linear recurrence of exact least order **127**, obtained by substituting the 127-degree monic \(\mu_9(T)\) into P. No scalar-coefficient recurrence of order ≤126 holds for the entire terminal count vector for every n≥0. Equivalently, the rational span of \(1,P,P^2,\ldots\) has dimension 127. By diagonalizability, \(\operatorname{rank}_{\mathbb Q}T_P^n=669\) for all n≥1.

This strengthens the all-q lower bound \(\deg \mu_q\ge q+1\) in R762EL to an exact value at q=9. It supplies the minimal multi-spectral recurrence state in this terminal vector sense, not a native signed Cell/Link/Port compression guarantee.

## Proof and complete finite certificate

Fix \(\zeta=\zeta_9\) and work in \(A=\mathbb Z[z]/(z^6+z^3+1)\), a free Z-module with basis \(1,z,\ldots,z^5\). The q=9 Fourier characters of G are indexed by all 729 triples \((i,j,k)\in\{0,\ldots,8\}^3\). Their eigenvalues are precisely

\[
\lambda_{ijk}=1+\zeta^i+\zeta^k+\zeta^{i+j}+\zeta^{j+k}+\zeta^{i+j+k}.
\]

The six units \(U=(\mathbb Z/9\mathbb Z)^\times=\{1,2,4,5,7,8\}\) act by exact automorphisms \(z\mapsto z^u\). For an eigenvalue \(\lambda\), its U-orbit O is exactly its complete set of conjugates over Q. Consequently its monic minimal polynomial is \(F_O(T)=\prod_{\alpha\in O}(T-\alpha)\in\mathbb Z[T]\), and has degree |O|; the orbit calculation thus proves irreducibility by Galois theory.

The attached program performs a **complete exhaustive finite certificate** using only integer-vector arithmetic in A:

1. Enumerate every one of the 729 character triples and convert each eigenvalue to the unique six-integer normal form. Record all multiplicities.
2. Partition the distinct vectors by the six exact U-actions, checking orbit closure and equality of multiplicity for every conjugate.
3. Construct each orbit factor by integer polynomial multiplication modulo \(z^6+z^3+1\); assert all nonconstant z-coordinates vanish, the leading coefficient is 1 and the factor evaluates to zero at each orbit member.
4. Check the computed orbit histogram (3,2,4,18), exactly 127 distinct roots, 27 factors, \(\sum_O d_Om_O=729\), zero multiplicity 60, and the independent trace identity \(\sum_{ijk}\lambda_{ijk}=729\).

Because the group algebra is split by its characters over C, T_P is diagonalizable, and its characteristic polynomial is the product of (T−λ) with the character multiplicities. The minimal polynomial contains one factor for every distinct λ. Grouping those roots into verified rational conjugacy orbits gives the displayed formulas. The cyclic-vector assertion follows because \(F(P)=F(T_P)(1)\) and \(F(T_P)=0\) exactly when \(F(P)=0\) in the unital group algebra. Thus the minimal possible simultaneous recurrence order is also 127.

The coefficient arithmetic is integral, with no floating-point estimates. The program is executable with an ordinary Node runtime; a separate Python standard-library implementation has also reproduced the 27-orbit and 127-eigenvalue counts locally. The attached JSON contains every orbit representative, all 27 explicit monic factors and their exact multiplicities.

## Research boundary and next question

This is a complete q=9 finite-character theorem for the positive six-branch terminal observer of the current X6 task. P000 remains the full six-native-axis signed Cell system; this calculation does not determine a native \`TRIADIC_CLOSURE_E\` event permission, V17/V29/V39 transport, or future-operation-safe quotient.

**Next mathematical question:** use the explicit 27 factors to derive integral 3-adic nondivisibility witnesses for the full three-coordinate content \(v_3(\gcd\operatorname{coeff}(P_9^n))\) at every horizon; compare the q=9 spectral model with R762DN's all-horizon conjecture. Independently inspect original native signed event predicates rather than inferring those from terminal positivity. No independent mathematical review was performed.
