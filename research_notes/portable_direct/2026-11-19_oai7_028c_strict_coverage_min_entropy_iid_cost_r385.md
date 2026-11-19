# OAI7 r385 — Sharp strict-coverage entropy floor and the conditional-iid cost in the pinned transfer theorem

Date: 2026-11-19. Direct mathematical audit of the exact external pinned \`coverage-transfer.tex\` theorem, preserving its full checkpoint and Chernoff assumptions. This is an author-side derived lemma, not an independent Native Review or official Result.

## 1. Exact one-coordinate minimum

Fix a finite alphabet of size \(p\ge2\), parameters \(0<\rho<1\), \(0<\beta'<1\), and the external source's strict coverage requirement
\[
 \#\{u:P(u)<\rho/p\}<p^{1-\beta'}.
\]
Set \(L=p^{1-\beta'}\), \(e=\lceil L\rceil-1\), \(t=p-e-1=p-\lceil L\rceil\), and \(b=\rho/p\). Define
\[
 \Phi(p,\rho,\beta')=
  -[1-tb]\log[1-tb]-t b\log b
  =h_2(tb)+tb\log t,
\]
where the second expression uses \(0\log0=0\) and \(\Phi=0\) at \(t=0\).

**Sharp theorem.** Among **all** probability distributions on the \(p\) symbols satisfying strict \((\rho,\beta')\)-coverage,
\[
 \boxed{\min H(P)=\Phi(p,\rho,\beta').}
\]
Every minimizer, up to alphabet permutation, has precisely one mass \(1-tb\), precisely \(t\) masses \(b\), and \(e\) zeros:
\[
 \boxed{P_*=(1-tb,\underbrace{b,\ldots,b}_{t},
                    \underbrace{0,\ldots,0}_{e}).}
\]
The equality masses \(b=\rho/p\) count as *covered* because the source's exceptional event uses \(<\), not \(\le\).

**Proof.** Any admissible \(P\) has at least \(t+1\) entries of mass \(\ge b\). Sort its coordinates in descending order. For each \(1\le j\le t+1\), the complement of the top \(j\) contains at least \(t+1-j\) entries with mass \(\ge b\). Thus the sum of the largest \(j\) entries is at most \(1-(t+1-j)b\). These are exactly the leading partial sums of \(P_*\); all later leading partial sums of \(P_*\) equal 1. Hence \(P_*\) majorizes every admissible \(P\). Strict Schur concavity of Shannon entropy gives \(H(P)\ge H(P_*)\), with equality only at permutations of \(P_*\). The candidate \(P_*\) has exactly \(e=\lceil L\rceil-1<L\) exceptional zeros, so is feasible. QED.

## 2. Consequence for the actual shared-checkpoint theorem

Use the **actual** pinned \`coverage-transfer.tex\` experiment: \(A\) is an exact checkpoint, \(Y=y(A)\) is deterministic given \(A\), \(h_1,\ldots,h_n\) are conditionally iid with law \(\nu_A\), and \(\mathcal H=(h_1,\ldots,h_n)\). The \(2k\) signed maps \(\phi_c\) have coordinate groups \(G_c\) of size \(p_c\in[T,2T]\). The theorem's good-coordinate hypothesis asserts that **at every supported checkpoint \(a\)** all but a fraction \(\eta'<1\) of the signed coordinates of \(\phi_c(y(a)+h_1)\) satisfy strict \((\rho,\beta')\)-coverage, where \(\rho=\tau+4\delta\).

A translation of an alphabet does not change entropy or the number of low-probability residues. Therefore at each \(a\) there exists at least one covered signed coordinate \(c(a)\), and
\[
 H(h_1\mid A=a)\ \ge\
 H(\phi_{c(a)}(h_1)\mid A=a)\
 \ge \Phi(p_{c(a)},\rho,\beta').
\]
Let
\[
 \Phi_*=\min_{c=(j,\sigma)} \Phi(p_c,\rho,\beta').
\]
By the conditional-iid assumption — **after fixing the same exact checkpoint** —
\[
 H(\mathcal H\mid A)=n\,\mathbb E_a H(h_1\mid A=a)
 \ge n\Phi_*.
\]
Conditioning reduces entropy, so the **unconditional** common-data budget of the pinned theorem necessarily obeys
\[
 \boxed{H(\mathcal H)\ge n\Phi_*,
 \qquad n\Phi_*\le \kappa s\overline L.}
\]
This is a necessary numerical feasibility test for the theorem's simultaneous hypotheses \(H(\mathcal H)\le\kappa s\overline L\) and exact-checkpoint conditional coverage. It does **not** challenge the theorem's implication.

The source separately requires, for every coordinate size \(p_c\),
\[
 p_c\exp(-\delta^2n p_c^{-\beta}/2)\le\delta/100.
\]
Consequently the two hypotheses together force
\[
 \boxed{
 \kappa s\overline L \ \ge\
 \Phi_*\,
 \max_c\left[
 \frac{2p_c^\beta}{\delta^2}
 \log\left(\frac{100p_c}{\delta}\right)
 \right].
 }
\]
For small alphabets \(\Phi_*=0\) is possible, yielding a vacuous necessary bound. In substantive parameter ranges with \(\Phi_*>0\), the conditional-iid replication cost grows proportionally to \(n\); sharing \(\mathcal H\) across coordinates charges the vector once in the *coordinate* entropy comparison, but does **not** erase the entropy cost of its \(n\) independent samples. This quantitative boundary can inform schedule design and admissible parameter selection.

**Quantifier discipline:** Coverage is checked at every \(a\), whereas the entropy budget is unconditional. The pointwise lower bound is averaged over \(a\) only after using the conditional-iid entropy identity. The result assumes the original homomorphisms and checkpoint conditioning; it makes no inference about native X6/BRC reachability or a replaced independent-shift model.

## 3. Complete small finite sanity check

For \(p=5,\beta'=1/2,\rho=2/5\), one has \(L=\sqrt5\), \(e=2\), \(t=2\), \(b=2/25\), and
\[
 P_*=(21/25,2/25,2/25,0,0),\qquad
 \Phi=0.5505734282909343\ldots\text{ nats}.
\]
Exhausting the complete probability grid with denominator 25 gives 22,031 admissible ordered vectors, and the displayed entropy minimum. This is only a finite sanity check of the majorization proof.

~~~python
from itertools import combinations
from math import sqrt,log,comb

p=5
L=sqrt(p)
rho_num,rho_den=2,5
D=25
b_num=2 # rho/p=(2/5)/5
def H(counts):
    return -sum((x/D)*log(x/D) for x in counts if x)
best=float('inf')
minima=[]
admissible=0
# Stars and bars: all ordered integer probabilities on five letters, denominator 25.
for cuts in combinations(range(1,D+p),p-1):
    counts=tuple(v-u-1 for u,v in zip((0,)+cuts,cuts+(D+p,)))
    assert sum(counts)==D
    if sum(x<b_num for x in counts)<L:
        admissible+=1
        h=H(counts)
        if h<best-1e-12:
            best=h; minima=[counts]
        elif abs(h-best)<1e-12:
            minima.append(counts)
assert admissible==22031
assert abs(best-H((21,2,2,0,0)))<1e-12
assert all(sorted(x)==[0,0,2,2,21] for x in minima)
print(admissible,best,len(minima))
~~~

## Provenance, precise dependency, and open work

- Exact external statement and proof: [openai/math pinned coverage-transfer.tex](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex), \`thm:transfer\`.
- Original Task: \`RS-OAI7-028-C-20261007-6F2A81\`, publication \`TP2-96FAC49786245691AE19\`. Initial finite Gaussian-moat counterexample and joint shift author: \`EM-EMF6D046-5A2844\`; preserve their exact original source identity.
- [r383](https://github.com/awdawmip/enterprise-math/blob/8421e1f27818aa736b0249119f467ea3418d0280/research_notes/portable_direct/2026-11-19_oai7_028c_independent_common_shift_global_entropy_optimum_r383.md) and [r384](https://github.com/awdawmip/enterprise-math/blob/3bf32a06460d2384417988bf2e4bbb033a2799d4/research_notes/portable_direct/2026-11-19_oai7_028c_checkpoint_arbitrary_holes_one_coin_entropy_optimum_r384.md) study separate explicit finite shift families. Their conditional \(Y\mid C\) may remain random, whereas the **pinned external exact checkpoint has \(Y=y(A)\)**. Do not transfer the optimal h2(a) cost of those families into the external theorem's sample-size hypothesis without a fresh matching construction.

The original research target remains the exact applicability and possible strengthening of the transfer lemma, and any typed native bridge requires its own carrier/provenance argument. This note is an author-side mathematical proof and a necessary condition; formal Result freeze, independent Review, Activity association, formal Task completion, and parent objective closure have not been claimed.
