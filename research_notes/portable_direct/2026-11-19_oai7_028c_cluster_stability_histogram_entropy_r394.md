# OAI7 r394 — Cluster-stable systematic histograms: a measurable entropy budget

Date: 2026-11-19. Scientific scope: OAI7-028-C, formal task `RS-OAI7-028-C-20261007-6F2A81`, publication `TP2-96FAC49786245691AE19`. Status: **author-side proved conditional lemma and exact finite test; not independent Native review, accepted Result, Task completion or Gaussian-schedule improvement**. This is a new consequence of [r392](2026-11-19_oai7_028c_type_free_histogram_entropy_r392.md), with the r393 high-entropy obstruction left intact.

## Theorem: bound unconditional sampler entropy using *approximate* law clusters

Let \(A\) be an arbitrary finite checkpoint variable and \(\nu_a=(\nu_a(1),\dots,\nu_a(M))\) a family of conditional laws on one common, globally ordered finite alphabet \(\{v_1,\dots,v_M\}\), with zero probabilities allowed. Fix an integer \(Q\ge1\). Let \(\mathsf C=\mathsf C(A)\) be any deterministic finite cluster label, and for each cluster \(c\) choose an arbitrary *reference probability law* \(\mu_c\) on the same ordered alphabet. Define their cumulative probabilities \(F_i(a)=\sum_{j\le i}\nu_a(j)\) and \(G_i(c)=\sum_{j\le i}\mu_c(j)\), for \(1\le i<M\).

Use a **single** \(U\sim\mathrm{Unif}[0,1)\) independent of \(A\), and define coupled systematic histograms
\[
N_i=\lfloor QF_i(A)+U\rfloor-\lfloor QF_{i-1}(A)+U\rfloor,\quad
N_i^0=\lfloor QG_i(\mathsf C)+U\rfloor-\lfloor QG_{i-1}(\mathsf C)+U\rfloor,
\]
where \(F_0=G_0=0\) and \(F_M=G_M=1\). Let
\[
 R=\binom{Q+M-1}{M-1},\qquad
 \varepsilon=\min\left\{1,\ Q\,\mathbb E\left[\sum_{i=1}^{M-1}|F_i(A)-G_i(\mathsf C)|\right]\right\}.
\]
For \(M\ge2\), if \(\varepsilon\le1-1/R\), the r392 histogram-canonical-word sampler, repeated periodically, obeys for **every** \(n\ge Q\):
\[
\boxed{\quad H(h_1,\dots,h_n)
 \le H(N^0)+h_2(\varepsilon)+\varepsilon\log(R-1)+\log Q
 \le H(\mathsf C)+\log M+h_2(\varepsilon)+\varepsilon\log(R-1)+\log Q.\quad}\tag{1}
\]
Entropy units are **nats**. Here \(h_2(t)=-t\log t-(1-t)\log(1-t)\), \(h_2(0)=0\). For every \(\varepsilon\), including larger ones, the unconditional bound \(H(h_1,\dots,h_n)\le\log R+\log Q\) holds. At \(M=1\), the sole histogram and output are deterministic and the entropy is zero.

The stronger **exact** r392 formula still holds:
\[
H(h_1,\dots,h_n)=H(N)+\mathbb E\log\bigl(Q/\gcd(N_i:N_i>0)\bigr).
\tag{2}
\]
The new bound (1) is useful when there are very many different \(\nu_a\), but their \(Q\)-scaled CDFs are close to a small set of reference laws. It does **not** assert that small support or strict residue coverage alone guarantees small entropy.

### Proof

For any real \(x,y\) and a uniform \(U\in[0,1)\),
\[
\Pr(\lfloor x+U\rfloor\ne\lfloor y+U\rfloor)\le\min(1,|x-y|).
\]
Indeed for \(|x-y|<1\) only an interval of \(U\) of length \(|x-y|\) crosses the extra integer boundary; for larger distance the upper bound 1 is trivial. If all \(M-1\) internal rounded cumulative sums agree, the full histogram vectors agree (the endpoints are identically 0 and \(Q\)). Conditional union bound and averaging thus give
\[
 \alpha:=\Pr(N\ne N^0)\le\varepsilon.\tag{3}
\]

Let \(E=1_{\{N\ne N^0\}}\). Since \(N\) has at most \(R\) values and, when \(E=1\), cannot equal \(N^0\),
\[
H(N)\le H(N^0)+H(E)+H(N\mid N^0,E)
       \le H(N^0)+h_2(\alpha)+\alpha\log(R-1).\tag{4}
\]
The function on the right beyond \(H(N^0)\) is increasing on \(0\le\alpha\le1-1/R\), proving the first bound via (3). Conditional on \(\mathsf C=c\), systematic rounding of the fixed reference law \(\mu_c\) has at most \(M\) possible integer histograms: the \(M-1\) internal cumulative floors can change only once each as \(U\) traverses \([0,1)\). Thus
\[
 H(N^0)\le H(\mathsf C)+H(N^0\mid\mathsf C)\le H(\mathsf C)+\log M.
\]
Finally insert (4) into the exact r392 identity (2), using \(\log d(N)\le\log Q\). The crude \(\log R+\log Q\) bound follows from counting histograms and phases, and the case \(M=1\) is immediate. QED.

### Exact rational diagnostic example (not a Gaussian-law claim)

Take \(Q=10,M=3\), \(A\) uniform on \(J=128\) values \(j=0,\dots,127\), and two clusters \(c=j\bmod2\). Set
\[
 \mu_0=(3/10,2/10,5/10),\quad
 \mu_1=(2/10,5/10,3/10),\quad
 t_j=(j-63)/200000,\quad
 \nu_j=(\mu_c(1)+t_j,\mu_c(2)-t_j,\mu_c(3)).
\]
The \(128\) conditional laws are distinct. All positive probabilities and \(Q\)-scaled CDF deviations are exact rationals. The reference histogram \(N^0\) is deterministic in each cluster (two equally weighted patterns), so \(H(N^0)=\log2\). The exact disagreement rate is
\[
 \alpha=\varepsilon=Q\mathbb E|t_j|=1/625=0.0016,\quad R=\binom{12}{2}=66.
\]
The actual histogram law has six outputs with exact probabilities:
\[
\begin{array}{c|c}
N & \Pr(N)\\ \hline
(3,2,5),(2,5,3)&312/625\ \text{each}\\
(2,3,5),(4,1,5)&1/2500\ \text{each}\\
(1,6,3)&31/80000\\
(3,4,3)&33/80000
\end{array}
\]
Therefore exact rational summation, followed only by evaluation of logarithms, yields
\[
\begin{aligned}
H(N)&\approx0.706154947317,\\
H(N^0)+h_2(\varepsilon)+\varepsilon\log65&\approx0.711725322148,\\
H(h_1,\dots,h_n)&\approx3.008740040311\quad(n\ge10),\\
\text{bound (1), using exact }H(N^0)&\approx3.014310415142.
\end{aligned}
\]
Every histogram in this example has gcd 1, so the final entropy adds exactly \(\log10\), not merely at most \(\log10\). This is a case with \(H(T(A))=\log128\approx4.85203\), yet a two-cluster CDF approximation sharply controls the actual shared data cost.

The following finite verification uses only exact rational arithmetic for the histogram distributions and the disagreement event; floating-point logarithms are for displaying the entropy.

~~~python
from fractions import Fraction as F
from collections import defaultdict
from math import comb, log
Q,M,J=10,3,128
references=[(F(3,10),F(2,10),F(5,10)),
            (F(2,10),F(5,10),F(3,10))]
def cum(p):
    z=[F(0)]
    for v in p: z.append(z[-1]+v)
    return z
def histogram(p,u):
    f=cum(p)
    return tuple((Q*f[i+1]+u).__floor__()-(Q*f[i]+u).__floor__()
                 for i in range(M))
def cuts(p):
    b={F(0),F(1)}
    for v in cum(p)[1:-1]:
        z=Q*v
        frac=z-z.__floor__()
        if frac: b.add(1-frac)
    return b
actual,reference=defaultdict(F),defaultdict(F)
disagree=F(0); cdf_union=F(0)
for j in range(J):
    c=j%2
    t=F(j-63,200000)
    p=(references[c][0]+t,references[c][1]-t,references[c][2])
    cdf_union+=Q*abs(t)/J
    borders=sorted(cuts(p)|cuts(references[c]))
    for x,y in zip(borders,borders[1:]):
        prob=(y-x)/J
        a=histogram(p,(x+y)/2)
        b=histogram(references[c],(x+y)/2)
        actual[a]+=prob
        reference[b]+=prob
        if a!=b: disagree+=prob
assert sum(actual.values())==sum(reference.values())==1
assert len(actual)==6 and len(reference)==2
assert disagree==cdf_union==F(1,625)
assert all(__import__('math').gcd(*a)==1 for a in actual)
def H(p):
    return -sum(float(v)*log(float(v)) for v in p.values() if v)
e=float(disagree); R=comb(Q+M-1,M-1)
h2=lambda z: -z*log(z)-(1-z)*log(1-z)
assert H(actual)<=H(reference)+h2(e)+e*log(R-1)+1e-12
print(len(actual), e, H(actual), H(reference),
      H(actual)+log(Q),
      H(reference)+h2(e)+e*log(R-1)+log(Q))
~~~

## Scientific use and boundaries

For the pinned Gaussian walk [schedule.tex](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/schedule.tex), determine the *actual* exact-checkpoint CDF family, cluster references and conditional event-run discrepancy certificate. If (1) meets the actual \(\kappa_i s_i L_*\) budget and the r386 conditional sampler tail hypothesis is verified for those same events, this supplies a quantified **alternative auxiliary-list experiment**. Its success is not implied by the present abstract example; the original independent-sampling Gaussian theorem is untouched. Keep original researcher `EM-EMF6D046-5A2844`'s contribution intact. This note originates in the same author/Driver research context as r386–r393, and is **not** an independent acceptance review. Formal Source/Activity linkage awaits genuine original-role authorization.
