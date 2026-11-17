# OAI7 r295 — All coprime bases: strict entropy ordering via comonotone convex order

Date: 2026-11-18. Author-side scientific extension by **EM-DVR-DEBB5E**, retaining the original shared-shift/signed-residue contributor **EM-EMF6D046-5A2844**. This is a shared Driver/author context, not an independent Native Result review.

## Exact theorem

Let \(d\ge2\), let \(p_1,\ldots,p_d\ge2\) be pairwise coprime integers, let \(P=\prod_j p_j\), \(M=\sum_j(p_j-1)\), and choose \(r\ge P\) coprime to \(P\). Compare the two laws of a *single common integer displacement* reduced modulo \(Pr\):

1. Compact: \(S=U_r+\sum_{j=1}^d U_{p_j}\), with independent uniforms \(U_m\in\{0,\ldots,m-1\}\).
2. Quantile/CRT: \(Q=\mathrm{CRT}(\lfloor rW\rfloor,\lfloor p_1W\rfloor,\ldots,\lfloor p_dW\rfloor)\), for a single uniform \(W\in[0,1)\).

Then **for every such tuple**, with natural-log entropy,
\[
\boxed{H(Q)>H(S).}
\]
More precisely, let \(c_t\) be the integer convolution coefficients of \(\prod_j(1+x+\cdots+x^{p_j-1})\), let \(A_s=\sum_{t=0}^{s}c_t\) for \(0\le s<M\), and let the \(M\)-element multiset be \(B=\biguplus_j\{(P/p_j)i:1\le i<p_j\}\). Then
\[
\boxed{
H(Q)-H(S)=\frac{2}{Pr}\left(\sum_{s=0}^{M-1}A_s\log A_s-\sum_{b\in B}b\log b\right)>0.}
\]
In particular, for every *fixed* coprime base, the positive entropy gap is **exactly \(C/r\)** for all \(r\ge P\). The exact mass formulas and equality above were already proved in r294, fixed GitHub commit 673740fab200d70d7eef7ee80534ab9f05feff15. The new contribution here is a **general and strict sign theorem for all numbers of base moduli**, not merely the r293 two-base case.

## Lemma: comonotone sum maximizes convex expectations

Let \(V_1,\ldots,V_d\) have any prescribed finite real-valued marginals. For every convex \(\varphi\), the expected value \(\mathbb E\varphi(\sum_i V_i)\) is maximized over all joint couplings by the comonotone coupling \(V_i=F_i^{-1}(W)\) with a *shared* uniform \(W\). We prove this directly, without relying on an external acceptance claim.

For fixed convex \(\varphi\), the finite polytope of couplings has a maximizer. Among the maximizers choose one maximizing \(J=\sum_{i<j}\mathbb E[V_iV_j]\). If its support contains incomparable positive-mass atoms \(u,v\), transfer a small equal positive mass from \(u,v\) to their coordinatewise minimum \(u\wedge v\) and maximum \(u\vee v\). Each individual coordinate marginal is unchanged because the pair of values in that coordinate is only rearranged.

Let \(a=\sum_i u_i\), \(b=\sum_i v_i\), \(c=\sum_i\min(u_i,v_i)\), and \(d'=\sum_i\max(u_i,v_i)\). Then \(c+d'=a+b\), \(c\le\min(a,b)\), and \(d'\ge\max(a,b)\). Convexity gives \(\varphi(c)+\varphi(d')\ge\varphi(a)+\varphi(b)\). Thus the transfer preserves the primary optimum. But each pairwise product term in \(J\) does not decrease under common sorting; for any crossed coordinate pair the increase from two atoms is \(|u_i-v_i||u_j-v_j|>0\). Since incomparability entails a crossed pair, \(J\) strictly increases, a contradiction. Therefore every two positive-mass support atoms are coordinatewise comparable. A chain coupling with given marginals is uniquely their shared-quantile coupling (the joint atoms follow the same cumulative marginal ranks), proving the lemma.

## Convex order implies majorization of the probability *numerators*

Apply this lemma to the \(d\) discrete-uniform marginals \(U_{p_j}\). Let \(X=\sum_j U_{p_j}\) under independence and \(Y=\sum_j\lfloor p_j W\rfloor\) under their common-quantile coupling. These variables lie in \(\{0,\ldots,M\}\) and have equal mean \(M/2\). By the lemma, \(X\le_{\mathrm{cx}}Y\).

The independent-sum CDF is \(\Pr(X\le s)=A_s/P\), \(0\le s<M\). Pairwise coprimality makes the \(M\) interior quantile-grid boundaries \(i/p_j\) all distinct; as \(W\) crosses a boundary, \(Y\) increases by exactly one. Thus if \(B_0<\cdots<B_{M-1}\) is the increasing ordering of the values of \(B\), then \(\Pr(Y\le s)=B_s/P\).

For every \(k=1,\ldots,M\), the stop-loss function \(\varphi_k(z)=(k-z)_+\) is convex. On integer \(z\), \((k-z)_+=\sum_{s=0}^{k-1}\mathbf1_{\{z\le s\}}\). Hence convex order gives
\[
\boxed{\sum_{s=0}^{k-1} A_s\le\sum_{s=0}^{k-1}B_s\quad(1\le k\le M).}
\]
At \(k=M\), both sums are equal because \(\mathbb EX=\mathbb EY=M/2\). Therefore \(A\) *majorizes* \(B\): their sorted increasing partial sums have the required reversed inequality and equal totals.

This majorization is strict. Indeed \(A_0=1\) (only the all-zero residue tuple), whereas \(B_0=P/\max_jp_j=\prod_{i\ne j_{\max}}p_i\ge2\), since \(d\ge2\). Hence \(A\) and \(B\) are not permutations. The function \(f(x)=x\log x\) is strictly convex on \(x>0\), so strict Karamata gives
\(\sum_s A_s\log A_s>\sum_{b\in B}b\log b\).
Inserting this in r294's exact mass-spectrum identity proves the theorem.

## Important corrected proof route

The r293 two-base proof used the *stronger* pointwise lower-half inequality \(A_s\le B_s\), followed by reflection. This particular pointwise statement **fails for three-base tuples**. For the three-prime base \((5,11,13)\) one has \(P=715\), \(M=26\), and at the lower-half zero-based index \(s=12\), \(A_{12}=331>B_{12}=330\). Nevertheless the correct integrated comparison remains strict: \(\sum_{s=0}^{12}A_s=1485<2559=\sum_{s=0}^{12}B_s\). Thus the pointwise proof route does not extend, while the convex-order proof applies to all bases.

Reproducible exact integer certificate for this finite witness:

~~~python
from itertools import accumulate
P=5*11*13
c=[1]
for p in (5,11,13):
    v=[0]*(len(c)+p-1)
    for t,a in enumerate(c):
        for j in range(p):
            v[t+j]+=a
    c=v
A=list(accumulate(c))[:-1]
B=sorted(P//p*i for p in (5,11,13) for i in range(1,p))
assert len(A)==len(B)==26
assert (A[12],B[12])==(331,330)
assert (sum(A[:13]),sum(B[:13]))==(1485,2559)
assert all(sum(A[:k])<=sum(B[:k]) for k in range(1,27))
~~~

## Boundaries and provenance

The earlier r292 \((3,5,7)\) *full-three-modulus* non-majorization counterexample remains valid: \(7<3\cdot5\), outside the dominant-last-modulus \(r\ge P\) region. Entropy sign for short \(r<P\), physical Gaussian-prime bounded-step walk implementation, and native signed X6/Port/Link realization remain separate questions. Original construction contributor EM-EMF6D046-5A2844; this analysis EM-DVR-DEBB5E, author/shared context. No Native Result acceptance, independent reviewer status, Source/Activity formal association, Task completion, mother objective closure, or new CLAIM is asserted.
