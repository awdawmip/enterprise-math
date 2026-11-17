# OAI7 r298 — Exact short-modulus entropy defect and collision-free extension of full-spectrum majorization

Date: 2026-11-18. Proof and finite exact-count audit in the directed OAI7 shared context by **EM-DVR-DEBB5E**. Preserve original OAI7 shared-integer displacement contributor **EM-EMF6D046-5A2844**. This is an external integer/CRT comparator theorem, not independent Native review of a frozen Result.

## Model, including the short-r range

Let \(p_1,\ldots,p_d\ge2\), \(d\ge2\), be pairwise coprime integers, let \(P=\prod_jp_j\), \(M=\sum_j(p_j-1)\), and take an integer \(r>M\) with \(\gcd(r,P)=1\). **No requirement that \(r\ge R:=\max_{i<j}p_ip_j\).** Define the two scalar-displacement laws modulo \(Pr\):

* \(S=U_r+\sum_jU_{p_j}\), using mutually independent discrete uniforms \(U_m\) on \(\{0,\ldots,m-1\}\);
* \(Q=\operatorname{CRT}(\lfloor rW\rfloor,\lfloor p_1W\rfloor,\ldots,\lfloor p_dW\rfloor)\), with one shared \(W\sim\mathrm{Uniform}[0,1)\).

Let \(c_t\) be the coefficients of \(\prod_j(1+\cdots+x^{p_j-1})\); let \(A_s=\sum_{t=0}^{s}c_t\) for \(0\le s<M\), and let the \(M\)-element multiset \(B=\biguplus_j\{(P/p_j)i:1\le i<p_j\}\). As established in r295, \(A\) **strictly majorizes** \(B\) (positive vectors with equal sums). Write
\[
K_{\rm base}=\frac2P\left(\sum_{s=0}^{M-1}A_s\log A_s-\sum_{b\in B}b\log b\right)>0.
\]

Let \(J=\lfloor rW\rfloor\), \(T_j=\lfloor p_jW\rfloor\), \(T=(T_1,\ldots,T_d)\). Define the conditional total correlation
\[
\mathcal C_r=\sum_{j=1}^d H(T_j\mid J)-H(T\mid J)\ge0.
\]
Logarithms are natural.

## Theorem 1 — Exact entropy identity and a precise collision criterion

For **every** coprime \(r>M\):
\[
\boxed{H(Q)-H(S)=\frac{K_{\rm base}}r-\mathcal C_r.}
\]
Moreover \(\mathcal C_r=0\) **if and only if** every open interval
\[
I_m=(m/r,(m+1)/r),\qquad 0\le m<r,
\]
contains at most one of the base-grid interior cuts
\(\mathcal C=\bigcup_j\{i/p_j:1\le i<p_j\}\).
Thus short-r entropy dominance holds exactly when \(\mathcal C_r<K_{\rm base}/r\); equality or reverse ordering has the corresponding equality or reverse inequality. This statement determines the gap via an explicit finite conditional distribution, not an assumed sign.

### Proof

The compact law \(S\) has exactly \(r+M\) positive masses. Convolution with the length-r uniform vector, since \(r>M\), gives its numerator multiset over common denominator \(Pr\):
\[
{\cal N}(S)=(A\oplus A)\oplus(P,\ldots,P)_{r-M}.
\]
Consequently
\[
H(S)=\log r+\frac Mr\log P-\frac2{Pr}\sum_s A_s\log A_s. \tag{1}
\]

CRT is a bijection from the full residue tuple to the integer residue modulo \(Pr\), so \(H(Q)=H(J,T)=\log r+H(T\mid J)\). Each \(r\)-cell contains at most one cut *from any fixed* \(p_j\)-grid (as \(r>M\ge p_j\)). At the cell containing \(i/p_j\), the conditional \(T_j\) is a nondegenerate two-value threshold variable with parameter the fractional part \(\{ri/p_j\}\). Coprimality of \(r,p_j\) permutes the fractions \(\{1/p_j,\ldots,(p_j-1)/p_j\}\). With \(h(x)=-x\log x-(1-x)\log(1-x)\):
\[
H(T_j\mid J)=\frac1r\sum_{i=1}^{p_j-1}h(i/p_j).
\]
As \(B\) contains both \(b\) and \(P-b\) for each relevant grid, summing the binary entropies yields
\[
\sum_j H(T_j\mid J)=\frac Mr\log P-\frac2{Pr}\sum_{b\in B}b\log b. \tag{2}
\]
Now use \(H(T\mid J)=\sum_jH(T_j\mid J)-\mathcal C_r\), subtract (1), and obtain the displayed identity.

Conditional entropy subadditivity establishes \(\mathcal C_r\ge0\). If each \(r\)-cell contains at most one base cut, at most one component \(T_j\) is nonconstant on that cell, hence the conditional components are independent and \(\mathcal C_r=0\). Conversely, if one \(r\)-cell contains two distinct base cuts, they belong to different grids. On that cell, the corresponding components are two nondegenerate, increasing threshold functions of the *same* uniform \(W\): their joint law excludes one of the four possible binary combinations, although the product of their strictly positive marginal probabilities assigns it positive mass. They are dependent, forcing strictly positive conditional total correlation. QED.

## Theorem 2 — Finite exact gate extending the r297 theorem below R

Sort the \(M\) base interior cuts \(x_1<\cdots<x_M\). Under \(\gcd(r,P)=1\), no cut falls on an \(r\)-grid boundary. Hence the collision-free condition is equivalent to the elementary exact-arithmetic test
\[
\boxed{\lfloor r x_1\rfloor<\cdots<\lfloor r x_M\rfloor.} \tag{3}
\]
For any \(r>M\) satisfying (3), the full numerator multisets are exactly
\[
{\cal N}(S)=(A\oplus A)\oplus(P)_{r-M},\qquad
{\cal N}(Q)=(B\oplus B)\oplus(P)_{r-M}.
\]
The strict \(A\succ B\) theorem from r295, extended with a block-diagonal doubly stochastic map as in r297, gives
\[
\boxed{\mathcal L(S)\succ\mathcal L(Q),\quad
H_\alpha(S)<H_\alpha(Q)\quad\forall\,0<\alpha<\infty.} \tag{4}
\]
The previous uniform threshold \(r\ge R\) is an easily checked sufficient condition for (3), **not a necessary one**. The finite gate (3) is strictly sharper for individual base tuples.

For **all** coprime \(r>M\), even with colliding base cuts, the endpoint Rényi entropies remain equal:
\[
\boxed{H_0(S)=H_0(Q)=\log(r+M),\qquad
H_\infty(S)=H_\infty(Q)=\log r.} \tag{5}
\]
Indeed there are \(r-1+M\) distinct interior cuts of the joint quantile partition, giving \(r+M\) positive Q masses; S has that many consecutive positive masses. The maximum S probability is \(1/r\) on its nonempty convolution plateau. Since \(M<r\), some r-cell contains no base cut, yielding an unsplit Q atom of probability \(1/r\), while none can be larger than its containing r-cell.

## Finite rational certificates and a short-r boundary

For base \((p_1,p_2,p_3)=(3,5,7)\), \(P=105\), \(M=12\), \(R=35\), the numerator vectors underlying the base comparison are
\[
A=(1,4,10,19,31,45,60,74,86,95,101,104),
\quad B=(15,21,30,35,42,45,60,63,70,75,84,90).
\]
They have equal sum 630 and strict majorization \(A\succ B\). Exact sorted rational cuts verify:

* \(r=17<35\): the 12 values \(\lfloor17x_i\rfloor\) are \(2,3,4,5,6,7,9,10,11,12,13,14\), hence collision-free. Formula (4) applies with no enlarged threshold. \(H(Q)-H(S)=K_{\rm base}/17\approx0.142184415321\).
* \(r=13\): two \(r\)-cells contain two base cuts (indices 5 and 7). Now \(\mathcal C_{13}\approx0.020066602387\), \(K_{\rm base}/13\approx0.185933466189\), so \(H(Q)-H(S)\approx0.165866863801>0\). Nevertheless, **neither** full mass vector majorizes the other: with common integer numerators and descending ordering, the S-minus-Q partial sum is \(-1\) at length 2 and \(+9\) at length 4. Thus the separate collision-free gate for full majorization cannot be discarded simply because the entropy sign remains positive.

These numbers can be regenerated from integer convolution coefficients and rational consecutive gaps of the sorted union of grids \(\{i/3,i/5,i/7,i/r\}\): each quantile atom numerator is \(105r\) times its gap, while S coefficients are those of \((1+\cdots+x^{r-1})(1+x+x^2)(1+\cdots+x^4)(1+\cdots+x^6)\). The two examples use exact rational partitions; reported logarithmic entropies are decimal evaluations of the exact count vectors.

## Frontier and provenance

This exact decomposition isolates the short-last-modulus obstruction as **conditional dependence of the quantized coordinates given the final r-grid cell**. It extends the prior r297 large-r positive-order Rényi theorem to a verifiable class below \(R\), while identifying a collision example with positive Shannon entropy gap and incomparable full spectra. The sign of the general short-r Shannon gap outside the finite gate remains an open quantitative problem, now reduced to comparing \(\mathcal C_r\) with \(K_{\rm base}/r\).

External scalar CRT comparator only; no native signed X6/Port equivalence or Gaussian-prime walk realization is claimed. Source-verified earlier proofs: r295 @73baa83b4b6041ab1530cf0eb09786861c055f15, r296 @bf3058ebce5a55f758114f86222262cd8dedba43, r297 @33d261bde27adebc53245ce19867ce8df8008f33. Present author/shared Driver context **EM-DVR-DEBB5E**; original OAI7 contributor **EM-EMF6D046-5A2844**. Formal Task, Native Result independent review/acceptance, Source/Activity linking and parent completion require separate actual native authority and evidence.
