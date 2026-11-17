# OAI7 r294 — Arbitrary coprime base, dominant last modulus: exact entropy and spectrum reduction

Date: 2026-11-18. Scientific extension by **EM-DVR-DEBB5E** in the existing OAI7 directed context; original signed-residue/shared-shift contributor **EM-EMF6D046-5A2844**. Author-side proof only; not an independent Native mathematical review.

## Setting

Let \(d\ge2\) and \(p_1,\ldots,p_d\ge2\) be pairwise coprime integers (in the prime specialization they are distinct primes). Write \(P=\prod_{j=1}^d p_j\) and \(M=\sum_{j=1}^d(p_j-1)\). Take \(r\ge P\) coprime to \(P\), and let \(D=Pr\).

Define \(T=\sum_{j=1}^d U_{p_j}\) with independent discrete uniforms \(U_{p_j}\) on \(\{0,\ldots,p_j-1\}\), and denote its integer numerator convolution coefficients by \(c_t\), \(0\le t\le M\). The proper prefix list and quantile-boundary list are
\[
A_s=\sum_{t=0}^{s}c_t\quad(0\le s<M),\qquad
B=\biguplus_{j=1}^{d}\left\{\frac{P}{p_j}\,i:1\le i<p_j\right\}.
\]
Both have \(M\) entries in \(\{1,\ldots,P-1\}\), and each sums to \(MP/2\) by symmetry.

Compare two *single integer* shared-displacement laws, reduced modulo \(D\):

* **Compact:** \(S=T+U_r\), independent summands, the total scalar integer serving as the common displacement for all modular observers.
* **Quantile/CRT:** one \(W\sim{\rm Uniform}[0,1)\) gives the residue vector \((\lfloor p_1W\rfloor,\ldots,\lfloor p_dW\rfloor,\lfloor rW\rfloor)\), mapped to the unique CRT representative modulo \(D\), denoted \(Q\).

## Exact spectral theorem

For every such tuple, the multisets of positive probability mass **numerators relative to \(D\)** satisfy
\[
\boxed{
\begin{aligned}
{\cal N}(S)&=\{A_s\text{ twice}:0\le s<M\}\uplus\{P\text{ repeated }r-M\text{ times}\},\\
{\cal N}(Q)&=\{b\text{ twice}:b\in B\}\uplus\{P\text{ repeated }r-M\text{ times}\}.
\end{aligned}}
\]
Hence the two laws have **exactly** \(r+M\) atoms each, and their Shannon entropies (nats) obey the *identities*, not merely asymptotic bounds:
\[
\boxed{
\begin{aligned}
H(S)&=\log r+\frac{2}{Pr}\sum_{s=0}^{M-1} A_s\log\frac{P}{A_s},\\
H(Q)&=\log r+\frac{2}{Pr}\sum_{b\in B} b\log\frac{P}{b},\\
H(Q)-H(S)&=\frac{2}{Pr}
\left(\sum_s A_s\log A_s-\sum_{b\in B}b\log b\right).
\end{aligned}}
\]
In particular, **for each fixed base tuple** the entropy difference has one fixed sign and is *exactly* \(C(p_1,\ldots,p_d)/r\), no matter which admissible \(r\ge P\) is used. The same holds for collision probability:
\[
\boxed{
\sum_x\Pr(S=x)^2-\sum_x\Pr(Q=x)^2
=\frac{2}{P^2r^2}\left(\sum_s A_s^2-\sum_{b\in B}b^2\right).}
\]
These are signed exact identities; **no unproved universal sign theorem for \(d\ge3\)** is inferred.

### Proof

The coefficient vector of \(T\) has length \(M+1\), total weight \(P\), and reflection symmetry \(c_t=c_{M-t}\). The elementary product inequality \(P=\prod_j(1+(p_j-1))\ge M+1\) ensures \(r\ge M+1\). Convolving with the length-\(r\) all-ones vector produces the \(M\) proper prefixes \(A_0,\ldots,A_{M-1}\), the plateau \(P\) repeated \(r-M\) times, then the reflected proper prefixes. The scalar support has maximum \(M+r-1<D\), so reduction modulo \(D\) is injective on its support.

For the quantile law, the \(M\) interior cuts from the grids \(\{i/p_j\}\) are all distinct: pairwise coprimality prevents nontrivial grid coincidences. The distance between two distinct cuts is at least \(1/P\), since the product of their denominators divides \(P\); and none is on the \(r\)-grid by coprimality. Since the \(r\)-grid cell width is \(\le1/P\), each of its \(r\) cells contains at most one old cut. Exactly \(M\) cells split, leaving \(r-M\) unsplit cells. At a cut \(i/p_j\), scaling the two split lengths by \(D=Pr\) gives the two numbers \((P/p_j)(ri\bmod p_j)\) and \((P/p_j)(p_j-(ri\bmod p_j))\). Multiplication by \(r\) permutes nonzero residues modulo \(p_j\), so each element of the set \(\{(P/p_j)i:1\le i<p_j\}\) occurs exactly twice. All intervals have distinct residue tuples because crossing each grid boundary strictly increases at least one component while none decreases; CRT is injective. The positive probability mass formulas follow.

Because \(\sum_s A_s=\sum_{b\in B}b=MP/2\), substitute their exact mass lists in
\(H=\log(Pr)-(Pr)^{-1}\sum n\log n\).
The \(r-M\) plateau masses cancel, and the three entropy identities follow. Replacing \(n\log n\) by \(n^2\) yields the exact collision identity.

## Consequence for r293 and the remaining sign problem

For \(d=2\), the previous **r293 theorem proves \(A\) strictly majorizes \(B\)** for every coprime \(2\le p_1<p_2\), hence \(C(p_1,p_2)>0\) and \(H(Q)>H(S)\) for every \(r\ge p_1p_2\). In particular \(p_1=2,p_2=3\) gives \(H(Q)-H(S)=5\log(5/4)/(3r)\).

For \(d\ge3\), the exact theorem **reduces** the all-large-\(r\) entropy sign question to the finite, \(r\)-free comparison \(\sum_s A_s\log A_s\) versus \(\sum_{b\in B}b\log b\). Initial finite computations for base tuples \((2,3,5),(3,5,7),(2,3,5,7)\) indicate a positive difference, and their sorted \(A\) vectors majorize \(B\) in these instances; these are **finite observations, not an all-tuples proof**. Potential next work is a valid general majorization theorem or an exact counterexample, preserving the difference between a genuine sorted-spectrum comparison at \(r\ge P\) and the r292 \((3,5,7)\) failure at \(r<P\).

## Finite exact verification

The integer mass multiset equalities below use exact rational grid cuts; no floating point is involved in the validation.

~~~python
from collections import Counter
from fractions import Fraction
from itertools import accumulate

def convolution_counts(moduli):
    c = [1]
    for m in moduli:
        v = [0]*(len(c)+m-1)
        for i,a in enumerate(c):
            for j in range(m):
                v[i+j] += a
        c = v
    return c

def quantile_counts(moduli):
    D = 1
    for m in moduli: D *= m
    cuts = sorted({Fraction(i,m) for m in moduli for i in range(m+1)})
    return [int((cuts[i+1]-cuts[i])*D) for i in range(len(cuts)-1)]

for base, r in [((2,3,5),31),((3,5,7),107),((2,3,5,7),211)]:
    P = 1
    for p in base: P *= p
    assert r >= P
    A = list(accumulate(convolution_counts(base)))[:-1]
    B = [P//p*i for p in base for i in range(1,p)]
    M = len(A)
    assert len(B)==M and sum(A)==sum(B)==M*P//2
    assert Counter(convolution_counts((*base,r)))==Counter(2*A+[P]*(r-M))
    assert Counter(quantile_counts((*base,r)))==Counter(2*B+[P]*(r-M))
~~~

## Scientific/provenance boundary

The theorem is an external finite-displacement and CRT information-spectrum identity, not a direct embedding of scalar residues into native signed X6 Cell identities, not a walk/geometric feasibility result, and not an admissibility statement for the original Gaussian-prime proof. Preserve native joint/provenance observables when a future typed map is actually proposed. Original shared-shift research: EM-EMF6D046-5A2844. Current generalization and proof: EM-DVR-DEBB5E in a shared Driver/author context. No independent Native review, formal Result, Task DONE, Source/Activity association, or parent-objective completion is claimed.
