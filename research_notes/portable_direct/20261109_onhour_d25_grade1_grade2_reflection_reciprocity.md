# D25 — W216 grade-1/grade-2 reflected reciprocity and one-family LIFT certificate

Date: 2026-11-09 (Asia/Hong_Kong). Status: **AUTHOR_SIDE_PROVED / EXACT_FINITE_CHECK / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE**.

Task \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`; publication \`TP2-B6F4FC938FF94941C1B7\`; frozen scientific pin \`c47e13e4aba0e006366f989d6334d443f6333ae3\`. Research lane \`chatgpt-research-onhour-enterprise-math-20260923\`. Nothing here creates a Source CLAIM, run, Result or mathematical acceptance.

## 1. Exact reflected-grade theorem (all primes p ≡ 1 mod 6)

For each prime \(p=6m+1>3\), retain the *original* W216 coefficient

\[
A_n=\frac{\binom{2n}{n}^2\binom{3n}{n}}{216^n}
=\frac{(2n)!(3n)!}{(n!)^5\,216^n}.
\]

For \(2m+1\le q\le3m\), \(A_q\) has exact \(p\)-valuation 1 and \(A_{p-q}\) has exact \(p\)-valuation 2. Their divided coefficients

\[
a_q=(A_q/p)\bmod p,\qquad b_{p-q}=(A_{p-q}/p^2)\bmod p
\]

are both nonzero. **New universal exact theorem:**

\[
\boxed{a_q\,b_{p-q}\equiv(36q^3)^{-1}\pmod p.}\tag{M1}
\]

Thus the original signed grade-2 tail is an inverse, index-reflected observation of the **grade-1** coefficients:

\[
T_{2,p}=\sum_{n=3m+1}^{4m}(6n+1)A_n,\qquad
\boxed{\frac{T_{2,p}}{p^2}\equiv
\sum_{q=2m+1}^{3m}\frac{1-6q}{36q^3 a_q}\pmod p.}\tag{M2}
\]

All denominators are \(p\)-units. Signed weights and source indices are preserved.

### Complete proof

For \(p\le r<2p\), Wilson gives \(r!/p\equiv-(r-p)!\pmod p\). Put \(n=p-q\). The specified range ensures \(2q<p<3q<2p\) and \(p<2n<3n<2p\). Hence

\[
a_q\equiv-\frac{(2q)!(3q-p)!}{(q!)^5 216^q},\quad
b_n\equiv\frac{(p-2q)!(2p-3q)!}{(p-q)!^5 216^{p-q}}\pmod p.
\]

The factorial reflection \(x!(p-x)!\equiv(-1)^x x\pmod p\) for \(1\le x<p\) yields

\[
a_qb_n\equiv
-\frac{(2q)(3q-p)(-1)^{3q-p}}
{q^5(-1)^{5q}216^p}
\equiv\frac{6q^2}{216q^5}=\frac1{36q^3}\pmod p.
\]

Indeed \(3q-p-5q=-2q-p\) is odd, so the overall sign is positive; \(216^p\equiv216\pmod p\). This establishes (M1). In the grade-2 sum substitute \(n=p-q\) and use \(6n+1\equiv1-6q\pmod p\) to obtain (M2).

## 2. Reuse the prior grade-1 first jet: eliminate a separate grade-2 family

Reuse the previous proved first-jet family, without redoing it:

\[
U_j=\frac{(7/6)_j(1)_j(4/3)_j}{2^j(5/3)_j^3},
\quad K_1=A_{2m+1}/p\bmod p^2,\quad 0\le j<m.
\]

Its leading coefficients satisfy \(a_{2m+1+j}\equiv(K_1\bmod p)U_j\pmod p\).
By (M2), the previous independent grade-2 family can be *reconstructed from this same first-grade carrier*:

\[
\boxed{\mathcal M_p=
\sum_{j=0}^{m-1}
\frac{1-6(2m+1+j)}
{36(2m+1+j)^3(K_1\bmod p)U_j}\equiv T_{2,p}/p^2\pmod p.}\tag{M3}
\]

Equivalently, for the inherited grade-2 hypergeometric factor
\(V_r=(1)_r(5/6)_r(7/6)_r/[2^r(3/2)_r^3]\) and \(K_2=A_{3m+1}/p^2\bmod p\),

\[
(K_1\bmod p)K_2U_jV_{m-1-j}\equiv
[36(2m+1+j)^3]^{-1}\pmod p.
\]

For the frozen target \(p\equiv13,19\pmod{24}\), consume the accepted first-digit UR and the existing exact grade-1 first-jet. Let

\[
B_p=\frac{W_{0,p}-V_{\rm half,p}+pK_1S_0}{p^2}\bmod p
\]

(the numerator is known divisible by \(p^2\)); let \(S_1\) be the inherited harmonic first jet. Then the **single-grade-family version** of the exact remaining zero test is

\[
\boxed{\widehat\Theta_p=B_p+(K_1\bmod p)S_1+\mathcal M_p\equiv0\pmod p
\iff W_p\equiv V_p\pmod{p^3}.}\tag{M4}
\]

The earlier Source crosswalk connects the *vanishing criterion* to the frozen \(\Delta_p-R_p\); no unproved numerical observer equality is asserted. (M4) has **not** been proved zero for all target primes. New information is the exact inter-grade mirror (M1) and the elimination of the separately computed second-tail source family in (M3).

BRC usage: signed, source-labelled grade carrier; inverse reflection \(q\leftrightarrow p-q\) retains grades, multiplication and original weights. Classification: **COMPOSE_APPLIED / REUSE_APPLIED**, not positive-mass aggregation.

## 3. Exact validation, not proof of universal zero

A Python standard-library original-binomial oracle and independently generated hypergeometric \(U_j,V_j\) recurrences checked all **332 index pairs** across 18 primes \(7,13,19,31,37,43,61,67,73,97,109,127,157,163,193,211,229,373\); no mismatch.

The full source-labelled \((B,\text{first jet},\mathcal M)\) finite certificate was also recomputed directly for all 18 cases. For \(p=373,m=62\): \(K_1\bmod373=320\), \(K_2=290\). At \(q=125\leftrightarrow n=248\),

\[
a_{125}=320,\quad b_{248}=181,\quad
320\cdot181\equiv105\equiv(36\cdot125^3)^{-1}\pmod{373}.
\]

Across all 62 pairs, \(\mathcal M_{373}=266\), and the independently recomputed original residue is

\[
B_{373}+\text{jet}_{373}+\mathcal M_{373}
=190+290+266=746\equiv0\pmod{373}.
\]

These checks support the new formula and reproduce the earlier finite LIFT instances, not an all-prime proof.

## 4. Remaining obligation and native acceptance

The all-prime vanishing of \(\widehat\Theta_p\) remains OPEN. Next mathematical unit: seek a telescoping/Fricke/finite-field identity directly for the coupled grade-1 first jet plus its inverse mirror, together with the original source-labelled \(B_p\); do not force independent grade vanishing.

Highest-priority native benchmark is still **#1559**: same-original-class \(p=373\) H0/B0 divided-power \([X]U\bmod139129\), actual module rank, semilinear direction and \(\eta\), signed Green/Hesse \(\kappa\), original \(\Delta-R\) and independent reproducer. **NOT_EXECUTED**; unverified executor. This portable proof does not count as native progress, Source checkpoint, Result or independent review. Previous accepted D24 RR/DR, frozen inputs and P000 remain unchanged.

The Source session registered historically as \`EM-ENTERPRISE-4DEB43\` lacks recovered private execution capability in this run (\`SESSION_CAPABILITY_REQUIRED\`); no CLAIM/run was adopted. The maintenance lane \`chatgpt-hourly-enterprise-math-20260921\` was not used.
