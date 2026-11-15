# R749SPX — Conditional tail-flux order and an exact non-single-crossing source-fiber counterexample

**2026-11-15 · AUTHOR_EXACT_NOT_REVIEWED.** Independent portable continuation of R749SPR–SPW. Frozen scientific input: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. The claim concerns the auxiliary 16-atom Walsh minimax-center model at \((t,s)=(1/10,1/2)\), with no change of P000 or native X6 source-event semantics. The full optimum center polytope \(K\) and the two 26-letter minimal source alphabets are taken from R749SPR/SPU. The current Source Researcher-ID and Activity association are independently tracked.

## 1. Exact model and source-fiber counts

Write \(P=K\cap\mathbb Z^3\) for the 33 first-level integer center coordinates \((H,U,V)\). Define \(F\subset P\) as the 25 lattice letters present in any uniquely representable unordered pair sum from \(P\). This is the R749SPU forced alphabet, reconstructible from the eight facets in the accompanying executable. The two minimal 26-letter alphabets are \(A_0=F\cup\{(0,0,0)\}\) and \(A_1=F\cup\{(-1,0,0)\}\).

For \(n\ge0\), let \(F_n(H,U,V)\) be the number of *unordered weak-composition* multisets of size \(n\) over the 25 labeled letters of \(F\), with coordinate sum \((H,U,V)\). Define \(M_j(n,H,U,V)\) in the same way for alphabet \(A_j\), with \(F_0(0,0,0)=1\) and all nonexistent counts zero. These are integer counts; source multiplicity is retained.

The optional-type convolution of R749SPW gives the identities
\[
M_0(n,H,U,V)=\sum_{k=0}^{n}F_{n-k}(H,U,V),\qquad
M_1(n,H,U,V)=\sum_{k=0}^{n}F_{n-k}(H+k,U,V).
\]

## 2. Theorem: exact conditional upper-tail flux

For **every** integer \(n\ge1\) and \(H,U,V\in\mathbb Z\), define
\[
C_n(H,U,V)=\sum_{h\ge H}\left[M_0(n,h,U,V)-M_1(n,h,U,V)\right].
\]
All sums are finite. Then
\[
\boxed{C_n(H,U,V)=
\sum_{k=1}^{n}\sum_{r=0}^{k-1}F_{n-k}(H+r,U,V)\ge0.}
\]

**Proof.** In the exact optional-count convolution, fix \(k\), and sum each difference over \(h\ge H\). Shifting the index \(h\mapsto h+k\) in its second term cancels all terms except \(h=H,\ldots,H+k-1\). The \(k=0\) contribution cancels identically. Summation over all \(k\) yields the displayed nonnegative integer formula. No regularity, unimodality, or asymptotic hypothesis is used. \(\square\)

Consequently, at each fixed \((U,V)\) with positive total count, the conditional \(H\)-readout for \(A_0\) **first-order stochastically dominates** that for \(A_1\). In particular, the two alphabets have the same \((U,V)\)-slice mass
\[
N_n(U,V)=\sum_{k=0}^n\sum_h F_{n-k}(h,U,V).
\]

The paired source-count coupling identifies the last optional slot and shifts the summed \(H\) coordinate by its nonnegative count \(k\). Its conditional mean displacement is
\[
\mathbb E[k\mid U,V]
=\frac{\sum_{k=0}^n k\sum_h F_{n-k}(h,U,V)}{N_n(U,V)}.
\]
Every pair in that coupling shares \((U,V)\). For normalized Walsh centers \(q_{(H,U,V)/n}\), their atom-TV metric along a fixed \((U,V)\) line is \(|\Delta H|/(20n)\). The coupling gives the upper bound in the Kantorovich problem, while the 1-Lipschitz signed Walsh \(h/2\) moment gives the matching lower bound. Therefore
\[
\boxed{
W_1^{TV}\left(\mu_{0,n}\mid U,V,\ \mu_{1,n}\mid U,V\right)
=\frac{\sum_{k=0}^n k\sum_h F_{n-k}(h,U,V)}
 {20n\,N_n(U,V)}.}
\]
This exact conditional identity strengthens the unconditional transport value \(1/520\) obtained in R749SPW.

## 3. Sharp distinction: the pointwise fiber difference is not single-crossing

Let \(D_n(H,U,V)=M_0(n,H,U,V)-M_1(n,H,U,V)\). Tail dominance says that *partial sums* of \(D_n\) are nonnegative; it does not force the signs of \(D_n\) to change just once.

Already at \(n=3,\ U=V=0\), exact multiset enumeration gives:

| H | M0 | M1 | D=M0-M1 |
|---:|---:|---:|---:|
| -2 | 29 | 26 | +3 |
| -1 | 28 | 34 | -6 |
| 0 | 29 | 27 | +2 |

Thus the sign pattern contains \(+\to-\to+\), disproving any proposed *universal one-crossing rule for pointwise source-fiber multiplicity* under these model assumptions. Along the same slice, the number of possible 26-type source multisets is \(N_3(0,0)=158\), with total optional-count sum 32. Hence
\[
\mathbb E[k\mid U=V=0]=16/79,\qquad
W_1^{TV}(\mu_{0,3}\mid0,0,\mu_{1,3}\mid0,0)=4/1185.
\]
This gives a concrete observer-sensitive residual: the monotone upper-tail order is exact while individual readout frequencies can reverse repeatedly.

## 4. Fully reproducible integer evidence

The dependency-free JavaScript verifier constructs all 33 lattice points from the eight R749SPR inequalities, derives exactly 25 forced types from all 561 unordered pair sums, and calculates all multiset coefficients using in-place unbounded-letter dynamic programming. No floating-point arithmetic or sampling is used. For \(n=1,\ldots,7\) it checks **every** \((U,V)\) slice, every integer threshold \(H=-2n-1,\ldots,2n+1\), and the closed nonnegative flux formula, including all zero and boundary coefficients in that finite support.

| n | Multisets per alphabet | Distinct readouts | (U,V) slices | Slices with more than one sign change | Max sign changes |
|---:|---:|---:|---:|---:|---:|
| 1 | 26 | 26 | 17 | 0 | 1 |
| 2 | 351 | 179 | 55 | 0 | 1 |
| 3 | 3,276 | 531 | 115 | 3 | 3 |
| 4 | 23,751 | 1,181 | 197 | 0 | 1 |
| 5 | 142,506 | 2,221 | 301 | 0 | 1 |
| 6 | 736,281 | 3,743 | 427 | 0 | 1 |
| 7 | 3,365,856 | 5,839 | 575 | 4 | 3 |

The finite verification is an exact check of the declared \(n\le7\) domain. The all-\(n\) statements follow from the displayed combinatorial proof. The reproducible certificate uses \`node R749SPX_WALSH_CONDITIONAL_TAIL_FLUX_CERT.js\` and produces \`R749SPX_WALSH_CONDITIONAL_TAIL_FLUX_RESULTS.json\`; its actual execution returned PASS.

**Scientific status and next question.** The all-\(n\) flux formula and conditional transport equality are proved for the two specified labeled alphabets, contingent on the R749SPR/SPU frozen Walsh identification; they are AUTHOR_EXACT_NOT_REVIEWED. Next characterize the precise occurrence and number of multi-crossing pointwise fiber sign chambers as \(n\) grows, possibly by exploiting the nonnegative flux finite-difference structure \(D_n(H,U,V)=C_n(H,U,V)-C_n(H+1,U,V)\), and determine eventual extremal-fiber ordering. Mapping these statements into native signed-Port/Cell transitions remains an independent source-preserving bridge problem.
