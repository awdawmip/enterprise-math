# R284BC — Uniform Port-output diameter and exact minimal 2×2 actuator heights

Date: 2026-11-20. Scientific status: **AUTHOR_PROVED / EXACT_FINITE_EXHAUSTION_PASSED / NOT_REVIEWED**.

**Lineage:** R284AT → R284AX → R284AY → R284AZ → R284BA → R284BB. The inherited frozen scientific pin for R284AT is Git blob SHA-1 `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. This manuscript develops the *auxiliary named directed-Port determinant observer*. It does not amend P000, identify an auxiliary two-coordinate matrix with an Enterprise-native two-dimensional plane, or claim a BRC/Heartbeat physical residual calculation. The algebraic calculations use exact integers.

## Observer and theorem

Fix integers \(n\ge2\), \(H\ge2\), \(K\ge0\). An unknown \(C\in\{1,\dots,H\}^{n\times n}\) is measured using common programmable integer controls

\[
D=\operatorname{diag}(d_0,\dots,d_{n-1}),\qquad Z=\sum_{j=1}^{n-1}z_j E_{0j},\qquad |d_i|,|z_j|\le K,
\]
\[
Y_C(D,Z)=\det(D-Z-C).
\]

The proof also applies to more general, fixed off-diagonal edit matrices \(Z\) bounded *per entry* by \(K\), provided the entry bound on \(D-Z-C\) remains \(H+K\).

**BC1 (output diameter theorem).** For every two matrices \(C,C'\) and every common admissible setting,

\[
\boxed{|Y_C(D,Z)-Y_{C'}(D,Z)|\le W_n(H,K):=
n\,n!\,(H-1)(H+K)^{n-1}.}
\tag{BC1}
\]

**Proof.** Put \(A=D-Z-C\) and \(A'=D-Z-C'\). Every entry in either has absolute value at most \(H+K\), while \(|A_{ij}-A'_{ij}|\le H-1\). For each permutation \(\sigma\in S_n\), telescope the difference between the products \(\prod_i A_{i,\sigma(i)}\) and \(\prod_i A'_{i,\sigma(i)}\), changing one factor at a time. Its absolute value is at most \(n(H-1)(H+K)^{n-1}\). The Leibniz determinant expansion contains \(n!\) signed permutation products. The triangle inequality proves BC1. This holds for all signs, ranks and candidate matrices. QED.

There are \(N=H^{n^2}\) candidate matrices. Their **integer** outputs under any one control setting fit in an interval of diameter at most \(W_n\). Therefore any one-read injective instrument necessarily satisfies

\[
\boxed{H^{n^2}-1\le n\,n!\,(H-1)(H+K)^{n-1}.}
\tag{BC2}
\]

For a readout \(Y_C+\epsilon\) with independent, adversarial absolute error \(|\epsilon|\le\delta\), \(\delta\ge0\), the closed error intervals associated with different candidates must be disjoint. Because their centers are integers, adjacent ordered centers must differ by at least \(\Delta=\lfloor2\delta\rfloor+1\). Thus one-read exact recovery requires

\[
\boxed{(H^{n^2}-1)\Delta\le n\,n!\,(H-1)(H+K)^{n-1}.}
\tag{BC3}
\]

In particular, define \(\lceil\sqrt[p]{A/B}\rceil_{\rm int}\) to be the smallest nonnegative integer \(t\) satisfying \(B t^p\ge A\). Then

\[
K\ge\max\left\{0,\left\lceil\sqrt[n-1]{\frac{(H^{n^2}-1)\Delta}{n\,n!\,(H-1)}}\right\rceil_{\rm int}-H\right\}.
\tag{BC4}
\]

For fixed integer \(H\ge2\) and \(\delta=0\), Stirling's formula gives the necessary asymptotic bound

\[
K\ge (e+o(1))H^{n+1}/n-H,\qquad n\to\infty.
\tag{BC5}
\]

This improves the leading \(H^n\) dependence in the earlier R284AY unconditioned cardinality estimate by one power of \(H\). Both are necessary bounds; for all parameter ranges the stronger one is obtained by taking their maximum.

For \(q\) **exact** adaptive integer readouts with the same amplitude cap, each node of the decision tree has at most \(W_n+1\) different integer outputs, regardless of its prior path. Therefore

\[
\boxed{q\log_2(W_n+1)\ge n^2\log_2 H.}
\tag{BC6}
\]

The noise statement BC3 is one-read; BC6 does not silently treat arbitrary continuous noisy transcripts as a finite-alphabet exact-read tree.

## BC2 — exact finite optimum at n=2, H=2

Write \(C=\begin{pmatrix}a&b\\c&d\end{pmatrix}\), where \(a,b,c,d\in\{1,2\}\). All \(2^4=16\) matrices are included. With \(x=d_0\), \(y=d_1\), \(z=z_1\), the determinant response is

\[
Y_C(x,y,z)=(x-a)(y-d)-(b+z)c.
\tag{BC7}
\]

**Signed-control optimum:** For all integers \(-K\le x,y,z\le K\), the least height permitting exact recovery from one scalar is **\(K=9\)**. Complete examination at \(K=8\) covers all \(17^3=4913\) possible settings, none injective. At \(K=9\), \((x,y,z)=(-9,-4,-4)\) produces sixteen distinct sorted values

\[
[52,53,54,56,57,58,59,61,62,63,64,66,68,69,70,72].
\]

Exactly 8 of the \(19^3=6859\) signed settings at height 9 are injective. Nested control domains establish failure at every lower signed height.

**Nonnegative-control optimum:** If instead \(0\le x,y,z\le K\), the least height is **\(K=10\)**. All \(10^3=1000\) settings at \(K=9\) fail injection. The setting \((7,10,10)\) at \(K=10\) gives sixteen distinct sorted values

\[
[16,18,21,23,24,26,28,29,30,32,33,34,36,37,42,43].
\]

Exactly 2 of the \(11^3=1331\) nonnegative settings at height 10 are injective.

These are *complete finite enumeration theorems with reproducible exact algorithms*, not claims of a general closed-form optimum for arbitrary \(n\) or \(H\). Both witnesses have minimum output spacing 1. The R284BA constant-one-difference matrix pair shows this is also the maximum attainable minimum spacing of all candidates for this model. Consequently for unrestricted finite actuator height, \(0\le\delta<1/2\) is the sharp adversarial-noise regime at \(n=2,H=2\).

## Quantitative comparison

Exact integer lower bounds for a single noiseless read:

| n | H | R284AY necessary K | R284BC necessary K |
|---:|---:|---:|---:|
| 2 | 2 | 0 | 2 |
| 3 | 2 | 2 | 4 |
| 4 | 2 | 5 | 7 |
| 8 | 2 | 61 | 91 |
| 16 | 2 | 9,227 | 14,764 |
| 32 | 2 | 328,603,591 | 565,667,321 |
| 8 | 3 | 1,596 | 3,404 |
| 16 | 3 | 6,061,593 | 14,271,995 |

For \(n=2,H=2\), the new universal diameter estimate only implies \(K\ge2\), while the full structural collision certificate gives \(K=9\) (signed) and \(10\) (nonnegative). The distinction identifies genuine algebraic restrictions beyond scalar output capacity.

## Exact reproduction and provenance

The companion standard-library script **R284BC_port_diameter_and_small_height_checker.py** deterministically enumerates 19,900 signed settings over heights 0–9, 4,356 nonnegative settings over heights 0–10, and all 16 unknown matrices per setting. It additionally performs 12,502 direct diameter comparisons and evaluates integer nth-root bounds via integer-only binary search. The result is preserved in **R284BC_exact_verification.json**, status PASS, independent review NOT_REVIEWED. The general bound is the proof above; exhaustive counts prove only the specified finite optimal heights.

The original research source family R284AT/R284AY/R284BB and its exact observer/finite-alphabet assumptions are preserved; the current norm context and protected P000 are read separately. The scientific artifact publication is independent of any native Task CLAIM, Activity source association, PROGRESS, formal Result or independent Review.

## Next discriminating units

1. Condition the diameter bound on named diagonal and star-column coefficients to derive finer fiberwise capacity constraints.
2. Determine minimal exact \(n=3,H=2\) instrument height by certificate-producing bounded search, and compare signed and nonnegative control domains.
3. Compare this necessary bound with R284AZ/R284BB sufficient setting costs under full input, precision, decoding and verification accounting; investigate polynomial-time decoding.
