# OAI7 r393 — Exact positive-coverage obstruction to universally cheap histogram sampling

Date: 2026-11-19. Author-side mathematical theorem and finite exact check; not an independent Native review, Result, or Task completion. Task `RS-OAI7-028-C-20261007-6F2A81` / `TP2-96FAC49786245691AE19`. Direct input: [r392](2026-11-19_oai7_028c_type_free_histogram_entropy_r392.md).

## 1. A full-coverage family with intrinsically large *histogram sampler* information

For any integer \(k\ge2\), put \(Q=2k\), take lattice \(\Lambda=\mathbb Z\), residue group \(G=\mathbb Z/k\mathbb Z\) and the reduction \(\phi:\Lambda\to G\). Let
\[
 \mathcal C_k=\{(N_1,\ldots,N_k)\in\mathbb Z_{\ge1}^{k}:
   \sum_{i=1}^k N_i=2k\},\qquad
 B_k=|\mathcal C_k|={2k-1\choose k-1}.
\]
Choose the exact checkpoint \(A\) uniformly in \(\mathcal C_k\). Conditional on \(A=N\), take a finite displacement law on the common lattice support \(\{0,\ldots,k-1\}\) with
\[
 \nu_N(i-1)=\frac{N_i}{2k}.
\]

**Theorem.** Each conditional law has **no exceptional residue** for the strict coverage floor \(\rho/k\) whenever \(0<\rho<1/2\). Its unconditional one-trial residue law is perfectly uniform on \(G\). However, applying the exact systematic-histogram / shortest-period / uniform-cyclic-rotation sampler from r392 with base length \(Q=2k\), and repeating the resulting block indefinitely, gives for every \(n\ge Q\)
\[
\boxed{H(h_1,\ldots,h_n)
=\log B_k+\log(2k)-\frac{\log2}{B_k}.}\tag{1}
\]
All logarithms use the natural base. Moreover
\[
\boxed{2k\log 2-\log(4k+2)\le H(h_1,\ldots,h_n)
\le2k\log2+\log(2k).}\tag{2}
\]
Thus the unconditional shared-data entropy of **this exact sampler** can grow linearly in the finite conditional support size \(k\), even though the conditional residue coverage is everywhere strict and the unconditional one-trial law is uniform. In this family \(H(T(A))=\log B_k\) and \(I(N;T(A))=\log B_k\); r392's type-free reformulation gives an exact formula but no uniform low-cost bound.

**Proof.** Every component \(N_i\ge1\), so \(\nu_N(i-1)\ge1/(2k)>\rho/k\). Symmetry of the uniform positive compositions gives \(\mathbb E N_i=2\), hence the unconditional one-trial residue mass is \(1/k\). Since every \(Q\)-scaled cumulative probability is an integer, systematic rounding yields exactly the chosen histogram \(N\) for every shift \(U\), without any count-pattern uncertainty.

The common divisor \(g(N)=\gcd_iN_i\) can exceed 1 only when \(N=(2,\ldots,2)\): if \(g\ge2\), each of the \(k\) positive coordinates is at least 2, so the sum \(2k\) forces equality throughout. This single histogram has primitive period \(d=k\); each of the other \(B_k-1\) histograms has primitive period \(d=2k\). The word completely determines \(N\). Using the exact r392 entropy identity,
\[
H(\mathcal H_n)=H(N)+\mathbb E\log d(N)
=\log B_k+\frac{B_k-1}{B_k}\log(2k)
 +\frac1{B_k}\log k,
\]
which simplifies to (1). The central binomial coefficient is the maximum term of \(\sum_{j=0}^{2k}{2k\choose j}=4^k\), so \({2k\choose k}\ge4^k/(2k+1)\). With \(B_k=\frac12{2k\choose k}\), this gives \(\log B_k\ge2k\log2-\log(4k+2)\). The upper bound follows from \(B_k\le4^k\), \(\mathbb E\log d(N)\le\log(2k)\). QED.

## 2. Exact finite example and check

At \(k=5,Q=10\), there are \(B_5={9\choose4}=126\) positive histograms: 125 with primitive period 10 and precisely one with period 5. Therefore
\[
 H(\mathcal H_n)=\log126+\frac{125}{126}\log10
  +\frac1{126}\log5
 \approx7.133365831846\ \text{nats} \quad(n\ge10).
\]
Every conditional residue probability is at least \(1/10\), above the original transfer floor \((7/16)/5=7/80\), and the unconditional marginal is \(1/5\).

~~~python
from itertools import combinations
from collections import Counter
from math import gcd, comb, log
k,Q=5,10
vectors=[]
for cut in combinations(range(1,Q),k-1):
    t=(0,)+cut+(Q,)
    vectors.append(tuple(t[i+1]-t[i] for i in range(k)))
assert len(vectors)==comb(Q-1,k-1)==126
assert all(sum(N)==Q and min(N)>=1 for N in vectors)
assert all(sum(N[i] for N in vectors)==2*len(vectors) for i in range(k))
periods=Counter()
for N in vectors:
    g=0
    for x in N: g=gcd(g,x)
    periods[Q//g]+=1
assert periods=={10:125,5:1}
entropy=log(len(vectors))+sum(m*log(d) for d,m in periods.items())/len(vectors)
assert abs(entropy-(log(126)+log(10)-log(2)/126))<1e-12
print(len(vectors),periods,entropy)
# 126 Counter({10: 125, 5: 1}) 7.1333658318458415
~~~

## 3. Consequence for the pinned Gaussian schedule

The original [`schedule.tex`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/schedule.tex) bounds its actual independent continuation data using \(n_i\log|\mathcal D_{i+1}|\) and establishes the entropy budget from precise scale separation. r392 supplies an alternative **exact** budget quantity \(H(N)+\mathbb E\log d(N)\), but the present family shows that finite shared support and even complete conditional coverage **alone** do not control that quantity logarithmically in support size. Therefore a quantitative Gaussian improvement would need the genuine checkpoint law's histogram distribution or another proved structural restriction. This is an obstruction **for the particular histogram-preserving sampler**, not a lower bound for every possible correlated sampler and not a counterexample to the original transfer theorem.

Provenance: author-side r392 and the pinned external Gaussian preprint; original task researcher `EM-EMF6D046-5A2844` retains their independently saved research. Native Result, independent review, formal Activity linkage and parent closure remain separate.
