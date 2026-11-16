# R749SSB — Exact recovery under one common denominator-count bias

**Date:** 2026-11-16 (Asia/Shanghai). **Status:** AUTHOR_EXACT_NOT_REVIEWED. **Frozen scientific pin:** a72226e2430ffa4786321ac86e7f0c599d5f0389. Direct predecessors: [R749SRY PR #2543](https://github.com/awdawmip/enterprise-math/pull/2543), [R749SRZ–SSA PR #2546](https://github.com/awdawmip/enterprise-math/pull/2546), immutable scientific material at 38b09d4a6dcc81320226b8b689364cb0252f7a81.

## Question and model

R749SSA allowed a separate denominator-count error at each of three sampling positions. Here one *shared* integer denominator error is used in all three observations, reflecting a calibrated common counting bias. Correlation of those errors is joint information relevant to the decoder.

Keep all five labeled positive source weights \(w=(1,1,2,3,6)\), with the first weight-one source marked. Define, for \(q\ge1\),

\[
\Omega_q=\{k\in\mathbb Z_{\ge0}^5:\sum_iw_ik_i\le q-1\},\qquad
C_q=|\Omega_q|,\quad T_q=\sum_{k\in\Omega_q}k_1.
\]

Use the frozen smooth part

\[
H_4(q)=\frac16+\frac1{2q}-\frac{115}{36q^2}+\frac{115}{6q^3}-\frac{16315}{108q^4}
\]

and six-phase cycle \(P=(455,-295,-25,185,-25,-295)/36\). Three offsets are \(J=(0,1,5)\), with ideal signatures \(S_a=(P_a,P_{a+1},P_{a+5})\), indices modulo six.

For two nonnegative integer budgets \(M,K\), the allowed errors are independent integers \(|e_i|\le M\) in marked numerator counts, but **one single integer** \(d\), \(|d|\le K\), is added to all three denominator counts. At \(q=r+h_i\),

\[
Y_i(r;e_i,d)=\frac{q^3(T_q+e_i)}{C_q+d}-q^4H_4(q),\qquad C_{r+h_i}+d>0.
\]

The decoder chooses the unique ideal signature minimizing the maximum absolute deviation; ties count as failure. Define \(N_{\rm common}(M,K)\) as the least integer \(N\ge1\) for which every \(r\ge N\) and every allowed joint error vector recovers \(r\bmod6\). Because \(C_q\) is nondecreasing, a common denominator perturbation is admissible exactly when

\[
d\in[\max(-K,1-C_r),K]\cap\mathbb Z.
\]

The model is a typed auxiliary positive-source observer; no native X6 spatial coordinate, physical time, or signed-BRC morphism is inferred from its phase labels.

## Theorem 1: exact correlated-error failure test

For arbitrary \(k\) sampled coordinates of the above positive-denominator fractional-affine form, with one common denominator perturbation \(d\), independent bounded integer numerator errors, and a finite set of real ideal signatures, the following test is **necessary and sufficient** for a rival \(b\ne a\) to tie or beat the true signature \(a\).

For each admissible integer \(d\), each rival \(b\), each coordinate \(j\), and each endpoint numerator error \(e_j\in\{-M,+M\}\), compute \(u=|Y_j-S_{a,j}|\). Discard a candidate when \(|Y_j-S_{b,j}|>u\). For every \(i\ne j\), put

\[
L_i=\max(S_{a,i}-u,S_{b,i}-u),\quad
U_i=\min(S_{a,i}+u,S_{b,i}+u),\quad q=r+h_i.
\]

The exact allowable numerator-error interval at coordinate \(i\) is

\[
\left[
\max\left(-M,\left\lceil\frac{(L_i+q^4H_4(q))(C_q+d)}{q^3}-T_q\right\rceil\right),
\min\left(M,\left\lfloor\frac{(U_i+q^4H_4(q))(C_q+d)}{q^3}-T_q\right\rfloor\right)
\right]\cap\mathbb Z.
\]

A failing vector exists if and only if at least one anchored candidate has nonempty integer intervals at every remaining coordinate. Per rival this needs at most \(2k(2K+1)\) anchor candidates and \(O(k^2(K+1))\) rational interval tests, independent of \(M\) except for integer bit length.

**Proof.** Fix the shared \(d\); each \(Y_i\) is affine and increasing in its own \(e_i\), since its denominator is positive. In any failing vector choose a coordinate \(j\) attaining its true maximum-norm deviation \(u\), with deviation sign \(\sigma\). Replace \(e_j\) by \(\sigma M\) *without changing \(d\)*. This increases the true deviation to \(u'\ge u\) in the same direction. The original rival condition at \(j\) is \(0\le\sigma(S_{b,j}-S_{a,j})\le2u\), preserved for \(u'\); at all other coordinates both true and rival deviations are still at most the original \(u\). Thus a failure has an endpoint witness. For a fixed endpoint and shared \(d\), both max-norm conditions on the other coordinates are exactly \(L_i\le Y_i\le U_i\). Multiplication by \(C_q+d>0\) and exact ceiling/floor give the integer intervals above. Independent numerator errors allow the intervals to be satisfied separately, constructing an actual failing vector. This proves equivalence. \(\square\)

## Theorem 2: nine sharp global thresholds

For every \(0\le M,K\le2\), the least guaranteed-recovery cutoffs are:

| Shared denominator budget K / numerator budget M | M=0 | M=1 | M=2 |
|---|---:|---:|---:|
| K=0 | **35** | **53** | **65** |
| K=1 | **41** | **55** | **67** |
| K=2 | **41** | **59** | **71** |

For comparison, independent denominator errors at three positions (R749SSA) give the rows \((35,53,65)\), \((261,267,273)\), \((507,513,513)\). At \(M=K=2\), preserving the common-bias relation changes the sharp cutoff from 513 to **71**.

Every entry is minimal, with a failure at \(r=N_{\rm common}(M,K)-1\):

| M | K | Last failure r | True phase | Rival | Shared d | Numerator errors (e0,e1,e2) |
|---:|---:|---:|---:|---:|---:|---|
| 0 | 0 | 34 | 4 | 3 | 0 | (0,0,0) |
| 1 | 0 | 52 | 4 | 3 | 0 | (-1,1,-1) |
| 2 | 0 | 64 | 4 | 3 | 0 | (-2,2,-2) |
| 0 | 1 | 40 | 4 | 3 | -1 | (0,0,0) |
| 1 | 1 | 54 | 0 | 3 | +1 | (-1,1,-1) |
| 2 | 1 | 66 | 0 | 3 | +1 | (-2,2,-2) |
| 0 | 2 | 40 | 4 | 3 | -2 | (0,0,0) |
| 1 | 2 | 58 | 4 | 3 | -2 | (-1,1,-1) |
| 2 | 2 | 70 | 4 | 3 | -2 | (-2,2,-2) |

**Proof.** The accompanying standard-library Python exact-arithmetic certificate uses Theorem 1 for every \(1\le r<1350\) and every one of the nine budgets: **12,141** cutoff/budget tests. It records the final failing position and a full exact witness for each. Independent full integer-error-cube enumeration of all 216 small cases \(r=1,\ldots,24\), \(M,K\in\{0,1,2\}\), reproduces the criterion. Independently recursed source populations verify \(C_q,T_q\) for 24 small cutoffs.

For all \(r\ge1350\), the predecessor exact R749SSA tail result proves that **every independently selected** denominator error vector with \(M,K\le2\) recovers the correct phase. It establishes

\[
\|Y-S_{r\bmod6}\|_\infty<
\frac{63374339249936}{28025208984321}<\frac{15}{4},
\]

half of the minimum inter-signature separation \(15/2\). A shared-\(d\) vector is in that independently admissible set; hence correctness extends to all \(r\ge1350\). Finite exhaustive proof and the cited infinite-tail lemma give the globally minimal nine thresholds. \(\square\)

## Evidence, reproducibility, and further work

The source is a reproducible extension of the *frozen* auxiliary model, with its five distinct labels and the common denominator-bias relation retained. Run the attached Python Fraction certificate to obtain the exact full JSON PASS data; it uses unbounded-coin dynamic programming and a separately recursive small-population crosscheck. The author-side proof depends explicitly on the R749SSA published infinite-tail lemma at PR #2546; independent mathematical review is outstanding.

Next: analyze **partially shared bias partitions**, such as \(d_0=d_1\) with \(d_2\) independent; classify the resulting observation-preserving relation poset and sharp thresholds. More broadly, investigate typed BRC source-port interfaces that preserve signed branch, provenance, multiplicity, phase, and future operations.