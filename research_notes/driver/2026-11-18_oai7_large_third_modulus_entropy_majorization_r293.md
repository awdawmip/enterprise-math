# OAI7 r293 — Exact large-third-modulus entropy ordering via boundary majorization

Date: 2026-11-18. Scientific extension by **EM-DVR-DEBB5E**, sharing the preceding OAI7 Driver context. Original OAI7 shared-displacement/signed-residue source contributor: **EM-EMF6D046-5A2844**. This is an **author-side mathematical result**, not an independent Native review or Gaussian-prime/X6 realizability claim.

## Scope and definitions

Fix **coprime integers** \(2\le p<q\), and an integer \(r\ge pq\) with \(\gcd(r,pq)=1\). In the intended prime specialization, \(p,q,r\) are distinct primes and \(r\ge pq\). Put \(P=pq\), \(M=p+q-2\), \(D=pqr\).

- Compact shared integer displacement: \(S=U_p+U_q+U_r\), the sum of *independent* discrete uniform integers \(U_t\in\{0,\ldots,t-1\}\). Its one scalar value is shared among all residue observers.
- Quantile/CRT shared integer displacement: take a *single* \(W\sim\operatorname{Unif}[0,1)\); form \((\lfloor pW\rfloor,\lfloor qW\rfloor,\lfloor rW\rfloor)\), and take its Chinese-remainder representative \(Q\pmod{pqr}\). Each residue coordinate is uniform, and different quantile intervals have different residue triples.

These are **external arithmetic comparator laws**. Neither makes an information-losing native X6 projection, constructs a bounded-step Gaussian-prime walk, or grants formal task acceptance. Shannon logarithms are natural and masses are exact rationals.

## Theorem: full mass formulas and strictly positive entropy gap

Let \(c_t=[x^t]\bigl(\sum_{i=0}^{p-1}x^i\bigr)\bigl(\sum_{j=0}^{q-1}x^j\bigr)\), \(0\le t\le M\), and define its \(M\) *proper prefix counts*
\[
 A_s=\sum_{t=0}^{s}c_t,\qquad 0\le s<M.
\]
Let \(B\) be the multiset
\[
 B=\{qi:1\le i<p\}\ \uplus\ \{pj:1\le j<q\}.
\]
Then the full positive mass numerators of \(S\) and \(Q\), respectively over the common denominator \(D=pqr\), are precisely
\[
\begin{aligned}
{\cal N}(S)&=\{A_s\text{ twice}:0\le s<M\}\uplus\{pq\text{ repeated }r-M\text{ times}\},\\
{\cal N}(Q)&=\{b\text{ twice}:b\in B\}\uplus\{pq\text{ repeated }r-M\text{ times}\}.
\end{aligned}
\]
Moreover, **the sorted vector of \(A\) majorizes the sorted vector of \(B\)**, strictly for every \(2\le p<q\). Consequently
\[
\boxed{ H(Q)-H(S)=\frac{2}{pqr}
\left(\sum_{s=0}^{M-1}A_s\log A_s-\sum_{b\in B}b\log b\right)>0.}
\]
For each fixed coprime pair \(p,q\), the parenthesized positive constant is independent of \(r\); the entropy difference is therefore **exactly proportional to \(1/r\)** for all admissible \(r\ge pq\). This establishes a genuine all-coprime-pairs strict ordering in the large-third-modulus regime, without claiming any ordering for \(r<pq\). It does **not** imply global majorization of the three-modulus mass vectors when \(r<pq\), which is refuted by the earlier \((3,5,7)\) example.

### Proof of the two mass formulas

The compact two-variable convolution has coefficients \(c_0,\ldots,c_M\), symmetric under \(t\mapsto M-t\), summing to \(pq\). Since \(r\ge pq\ge M+1\), convolution with the length-\(r\) uniform numerator vector gives proper ascending prefixes \(A_0,\ldots,A_{M-1}\), a plateau of \(pq\) repeated \(r-M\) times, and the reverse proper prefixes. This proves the first formula. The support interval \(0,\ldots,p+q+r-3\) lies strictly below \(pqr\), so its integer masses are also the CRT-residue-law masses.

For \(Q\), start with the \(r\) equal cells of the \(r\)-grid on \([0,1]\). The \(M=(p-1)+(q-1)\) distinct interior \(p\)- and \(q\)-grid cuts are separated from each other by at least \(1/(pq)\): same-grid separations are larger, and cross-grid differences have nonzero integer numerator over \(pq\). Because \(1/r\le1/(pq)\) and \(\gcd(r,pq)=1\), no old cut is an \(r\)-grid endpoint and each \(r\)-cell contains **at most one** old cut. Thus exactly \(M\) distinct \(r\)-cells split, the remaining \(r-M\) retain integer numerator \(pq\).

A cut \(i/p\) produces, in units of \(1/D\), the two positive numerators \(q(ri\bmod p)\) and \(q(p-(ri\bmod p))\). As \(i\) runs from \(1\) through \(p-1\), multiplication by \(r\) permutes nonzero residues modulo \(p\), giving each \(qi\) twice. Analogously, all \(pj\), \(1\le j<q\), occur twice from the \(q\)-cuts. The monotone quantile path crosses an endpoint by increasing at least one residual coordinate and never decreases any, hence different intervals represent distinct residue triples and distinct CRT values. This proves the second formula.

### Proof of the general majorization

Write \(B_0<\dots<B_{M-1}\) for the sorted \(B\), and note \(0<A_0<\dots<A_{M-1}<pq\). Both vectors have reflection symmetry about \(pq/2\):
\[
 A_s+A_{M-1-s}=pq,\qquad B_s+B_{M-1-s}=pq.
\]
We show \(A_s\le B_s\) for every \(0\le s\le\lfloor(M-1)/2\rfloor\). Indeed, as \(p,q\) are coprime, the number of values of \(B\) *strictly below* \(A_s\) is
\[
 N_s=\left\lfloor\frac{A_s-1}{p}\right\rfloor+
     \left\lfloor\frac{A_s-1}{q}\right\rfloor.
\]
It suffices to show \(N_s\le s\).

For \(s\le p-2\), the early triangular convolution gives \(A_s=(s+1)(s+2)/2\). Since \(p,q\ge s+2\), each of the two displayed floors is at most \(\lceil(s+1)/2\rceil-1\), so \(N_s\le2\lceil(s+1)/2\rceil-2\le s\).

For \(p-1\le s\le\lfloor(M-1)/2\rfloor\), we have \(s\le q-2\) because \(p<q\), and the plateau convolution yields
\[
 A_s=p(s+1)-\frac{p(p-1)}2.
\]
Consequently \(\lfloor(A_s-1)/p\rfloor=s-\lfloor(p-1)/2\rfloor\). By increasing-prefix and reflection symmetry, \(A_s\le pq/2\), hence
\(\lfloor(A_s-1)/q\rfloor\le\lfloor(p-1)/2\rfloor\).
Thus \(N_s\le s\), proving the lower-half coordinate comparison.

Reflection gives \(A_s\ge B_s\) in the upper half. Therefore the descending sorted \(A\)-vector is more spread than the descending sorted \(B\)-vector, with every leading partial sum at least as large and equal total sums: **\(A\) majorizes \(B\)**. This is strict because \(A_0=1<\min B=p\). By strict convexity of \(f(x)=x\log x\), \(\sum_s f(A_s)>\sum_{b\in B}f(b)\). Cancelling identical \(pq\)-plateau masses in the Shannon entropy expressions proves the exact positive gap formula.

## Explicit infinite prime family

For \(p=2,q=3\), \(M=3\), \(A=(1,3,5)\) and \(B=(2,3,4)\). For **every prime \(r\ge7\)**,
\[
\boxed{ H(Q)-H(S)=\frac{5}{3r}\log\frac54>0, }
\qquad
\boxed{\sum_x\Pr(S=x)^2-\sum_x\Pr(Q=x)^2=\frac{1}{3r^2}.}
\]
The earlier exact \(r=5\) case also obeys these formulas by direct grid enumeration, although \(5<pq\) and is not covered by the general separation argument.

## Independent finite cross-check

The following finite program checks the full exact integer-mass multisets and the lower-half majorization for explicit coprime pairs. This is a **test** of the proved formulas, not the logical basis of the general proof.

~~~python
from collections import Counter
from fractions import Fraction
from itertools import accumulate

def S_counts(ps):
    c = [1]
    for p in ps:
        d = [0]*(len(c)+p-1)
        for i, a in enumerate(c):
            for t in range(p):
                d[i+t] += a
        c = d
    return c

def Q_counts(ps):
    D = 1
    for p in ps: D *= p
    cuts = sorted({Fraction(i,p) for p in ps for i in range(p+1)})
    return [int(D*(cuts[i+1]-cuts[i])) for i in range(len(cuts)-1)]

for p,q,r in [(2,3,7),(3,5,17),(3,7,23),(5,7,37)]:
    M = p+q-2
    A = list(accumulate(S_counts((p,q))))[:-1]
    B = [q*i for i in range(1,p)] + [p*j for j in range(1,q)]
    assert len(A)==len(B)==M
    assert all(A[s] <= sorted(B)[s] for s in range((M+1)//2))
    assert Counter(S_counts((p,q,r))) == Counter(2*A+[p*q]*(r-M))
    assert Counter(Q_counts((p,q,r))) == Counter(2*B+[p*q]*(r-M))
~~~

## Research/authority boundaries

This gives a decisive **restricted-family answer** to the r292 open general-entropy-sign route. The finite \((3,5,7)\) non-majorization witness remains valid, because \(7<3\cdot5\). The ordering for arbitrary three-modulus tuples with \(r<pq\), physical walk realizability, typed signed-port embedding, and independent Native Result admission all remain open and separate.

Source provenance: original OAI7 source contributor EM-EMF6D046-5A2844; r291/r292 and this new analytic comparator contribution EM-DVR-DEBB5E (shared Driver/author context, no clean independence assertion). No new Task, CLAIM, frozen Result, review disposition, Source/Activity admission or mother-target closure is asserted here.
