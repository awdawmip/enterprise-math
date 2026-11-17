# OAI7 r296 — Sharp separation scale for the exact entropy-dominance mechanism

Date: 2026-11-18. Author-side follow-up by **EM-DVR-DEBB5E** in existing shared OAI7 directed context. The original shared-displacement/signed-residue scientific contributor remains **EM-EMF6D046-5A2844**. No independent Native review or physical/native X6 realization is claimed.

## Improved theorem (all coprime bases, last modulus above pair-product threshold)

Let \(p_1,\ldots,p_d\ge2\) be **pairwise coprime integers**, \(d\ge2\), \(P=\prod_jp_j\), \(M=\sum_j(p_j-1)\), and set
\[
\boxed{R=\max_{1\le i<j\le d}p_ip_j.}
\]
Choose **any** integer \(r\ge R\) with \(\gcd(r,P)=1\). In particular, \(r\) need **not** be greater than the full product \(P\).

Define the compact integer common-displacement law
\(S=U_r+\sum_j U_{p_j}\), with all summands independent uniforms on \(\{0,\dots,m-1\}\), and the quantile/CRT common-displacement law
\(Q=\operatorname{CRT}(\lfloor rW\rfloor,\lfloor p_1W\rfloor,\dots,\lfloor p_dW\rfloor)\) from a **single** uniform \(W\in[0,1)\).

Let \(c_t\) be the convolution counts of \(\sum_j U_{p_j}\), \(A_s=\sum_{t=0}^{s}c_t\) for \(0\le s<M\), and
\(B=\biguplus_j\{(P/p_j)i:1\le i<p_j\}\).

**Theorem.** The exact positive mass numerators over denominator \(Pr\) are
\[
\boxed{
\begin{aligned}
{\cal N}(S)&=\{A_s \text{ twice}\}_{s=0}^{M-1}\uplus\{P \text{ repeated } r-M\text{ times}\},\\
{\cal N}(Q)&=\{b\text{ twice}\}_{b\in B}\uplus\{P \text{ repeated } r-M\text{ times}\}.
\end{aligned}}
\]
Hence the full Shannon entropy relation is the **strict theorem**
\[
\boxed{H(Q)-H(S)
=\frac{2}{Pr}
\left(\sum_{s=0}^{M-1}A_s\log A_s-\sum_{b\in B}b\log b\right)>0.}
\]
The positive coefficient is independent of \(r\). The exact collision-probability gap is
\[
\boxed{
\sum_x\Pr(S=x)^2-\sum_x\Pr(Q=x)^2
=\frac{2}{P^2r^2}\left(\sum_s A_s^2-\sum_{b\in B}b^2\right).
}
\]
The collision formula is an identity; no positivity statement for arbitrary bases is needed to obtain the Shannon theorem.

This improves the condition \(r\ge P\) of r294/r295 to \(r\ge R\). For \(d\ge3\) pairwise coprime moduli, \(R<P\), so the new theorem covers a genuine previously open region.

## Proof of the improved separation bound

The \(M\) interior quantile cut points belonging to the base grids are
\(\mathcal C=\biguplus_j\{i/p_j:1\le i<p_j\}\). Pairwise coprimality makes these all distinct.

For any two distinct cuts, either both come from the same grid of denominator \(p_i\), in which case their distance is at least \(1/p_i\ge1/R\), or their denominators are distinct \(p_i,p_j\), in which case the distance is
\[
\left|\frac a{p_i}-\frac b{p_j}\right|
=\frac{|a p_j-bp_i|}{p_ip_j}
\ge\frac1{p_ip_j}\ge\frac1R.
\]
Thus **all distinct interior cuts are separated by at least \(1/R\)**.

Every \(r\)-grid cell has length \(1/r\le1/R\), and none of these cuts lies on its boundary because \(\gcd(r,P)=1\). Therefore an open \(r\)-cell contains at most one old cut: two interior points in the same cell would have distance strictly less than its length, contradicting the separation bound.

We also need \(r>M\) for the compact convolution plateau. Sort \(p_1<\cdots<p_d\). Since they are \(d\) distinct integers each at least \(2\), \(p_{d-1}\ge d\). Therefore
\[
R=p_{d-1}p_d\ge d p_d>
\sum_{i=1}^d(p_i-1)=M,
\]
so indeed \(r>M\).

Consequently exactly \(M\) distinct \(r\)-cells split and \(r-M\) remain unsplit. At each old \(p_j\)-cut the two split-mass numerators in units of \(1/(Pr)\) are \((P/p_j)(ri\bmod p_j)\) and \((P/p_j)(p_j-(ri\bmod p_j))\). Coprimality ensures each \(1,\ldots,p_j-1\) occurs once in the first expression and once in the second as \(i\) varies, giving \(2B\) independently of \(r\). This is the full Q mass formula.

Since \(r>M\), the convolution of the base numerator coefficients with the length-\(r\) uniform vector yields the proper prefixes \(A_s\) twice and the plateau \(P\) exactly \(r-M\) times. Also \(M+r-1<Pr\), hence reduction of the compact integer support modulo \(Pr\) is injective. This proves the full S mass formula.

Entropy and collision identities follow by exact mass counting. Finally, the all-base *strict majorization* \(A\succ B\) was established in the r295 comonotone convex-order proof, and is independent of \(r\). Strict convexity of \(x\log x\) yields the strictly positive Shannon entropy gap. QED.

## Separation scale is exactly the minimum grid-spacing reciprocal

The lower bound \(1/R\) on the separation between old cuts is attained: choose the two largest coprime moduli \(p_{d-1},p_d\). Bézout's identity provides interior grid fractions \(a/p_{d-1}\), \(b/p_d\) satisfying \(|a p_d-b p_{d-1}|=1\), hence distance \(1/R\). (The nontrivial inverse residue chooses \(1\le a<p_{d-1}\) and \(1\le b<p_d\).) Thus the **minimum pairwise separation in the union of base grid cuts is exactly \(1/R\)**.

This proves that \(r\ge R\) is the exact *uniform mesh-width threshold* derived from grid separation. It is **not** a proof that entropy ordering fails or split-free geometry is impossible for every \(r<R\); finer alignment with the \(r\)-grid can permit additional cases.

## Exact newly covered prime examples

- Base \(p=(2,3,5)\): \(R=15<P=30\). New allowed prime \(r=17\), with entropy gap \(H(Q)-H(S)>0\) and mass formulas proved above.
- Base \(p=(2,3,5,7)\): \(R=35<P=210\). Prime \(r=37\) is newly covered.
- Base \(p=(3,5,7)\): \(R=35<P=105\). Prime \(r=43\) is newly covered.
- Base \(p=(5,11,13)\): \(R=143<P=715\). Prime \(r=151\) is newly covered.

The \((3,5,7)\) r292 negative **majorization** example has last modulus \(7<3\cdot5=15\) for base \((3,5)\), so it remains outside this theorem and is unchanged.

## Reproducible finite exact certificates

~~~python
from fractions import Fraction
from collections import Counter
from itertools import accumulate

def compact_counts(ms):
    c=[1]
    for m in ms:
        d=[0]*(len(c)+m-1)
        for t,a in enumerate(c):
            for k in range(m):
                d[t+k]+=a
        c=d
    return c

def quantile_counts(ms):
    P=1
    for m in ms: P*=m
    cuts=sorted({Fraction(i,m) for m in ms for i in range(m+1)})
    return [int(P*(cuts[k+1]-cuts[k])) for k in range(len(cuts)-1)]

for base,r in [((2,3,5),17),((2,3,5,7),37),((3,5,7),43),((5,11,13),151)]:
    P=1
    for p in base: P*=p
    R=max(p*q for j,p in enumerate(base) for q in base[j+1:])
    M=sum(p-1 for p in base)
    assert R<=r<P and M<r
    A=list(accumulate(compact_counts(base)))[:-1]
    B=[P//p*i for p in base for i in range(1,p)]
    assert Counter(compact_counts((*base,r)))==Counter(A+A+[P]*(r-M))
    assert Counter(quantile_counts((*base,r)))==Counter(B+B+[P]*(r-M))
    assert sum(A)==sum(B)==M*P//2
~~~

## Scope and contribution boundary

These are exact theorems about **external finite integer/residue comparator distributions**, not proofs of the original physical Gaussian-prime bounded-step displacement model or native typed X6/Port/Link realization. They do not erase joint/provenance directions or promote a scalar projection into full native cell identity. Original OAI7 contributor EM-EMF6D046-5A2844; r293–r296 mathematical extensions EM-DVR-DEBB5E, shared directed Driver/author context. Native Result admission, independent Native review, Source/Activity formal association, Task DONE and mother objective completion all remain separately unperformed.
