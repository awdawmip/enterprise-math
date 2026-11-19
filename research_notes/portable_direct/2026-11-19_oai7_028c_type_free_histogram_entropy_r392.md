# OAI7 r392 — Exact *unconditional* histogram entropy for a shared conditional sampler

Date: 2026-11-19. Task context: `RS-OAI7-028-C-20261007-6F2A81` / `TP2-96FAC49786245691AE19`. Status: **author-side mathematical theorem and exact finite example**, not an independent Native review or a frozen Result. This note refines the r388–r391 finite conditional sampler; it does not change the pinned Gaussian walk, the statement of r386, or the original Researcher attribution.

## 1. The law-type entropy can be replaced by the actual histogram information

Fix a finite exact-checkpoint variable `A`, a finite **common** lattice alphabet \(\mathcal D=\{v_1,\ldots,v_M\}\), and arbitrary conditional laws \(\nu_a\) on \(\mathcal D\), including irrational probabilities and zero weights. Choose **one global ordering of \(\mathcal D\)**, independent of \(a\). Let \(T=T(A)\) denote the exact conditional law type, and \(Q\ge1\) a fixed base length.

For each supported \(a\), put \(F_i(a)=\sum_{j\le i}\nu_a(v_j)\), draw \(U\sim{\rm Unif}[0,1)\) conditionally independently of \(A\), and set
\[
 N_i=\lfloor QF_i(A)+U\rfloor-\lfloor QF_{i-1}(A)+U\rfloor.
\]
Then \(N=(N_1,\ldots,N_M)\) is a nonnegative integer histogram with \(\sum_i N_i=Q\). Write
\[
 g(N)=\gcd\{N_i:N_i>0\},\qquad d(N)=Q/g(N).
\]
For each histogram \(N\), use one **fixed deterministic canonical** primitive word with \(N_i/g(N)\) copies of symbol \(v_i\), repeat it \(g(N)\) times to length \(Q\), and choose uniformly among its \(d(N)\) distinct cyclic rotations, obtaining \(W=(W_1,\ldots,W_Q)\). Extend periodically to \(h_\ell=W_{1+((\ell-1)\bmod Q)}\).

**Theorem (exact scalar entropy, all horizons \(n\ge Q\)).** Each sample position has exactly its original one-trial conditional law:
\[
 \Pr(h_\ell=v_i\mid A=a)=\nu_a(v_i)
 \qquad(\forall\,a,\ell,i).
\]
Moreover, with Shannon entropies consistently in natural logarithms,
\[
 \boxed{H(h_1,\ldots,h_n)=H(N)+\mathbb E\log d(N),\qquad n\ge Q.}\tag{1}
\]
Consequently,
\[
 \boxed{H(h_1,\ldots,h_n)
 \le\min\left\{\log {Q+M-1\choose M-1},\,
 H(T)+\log M\right\}+\log Q.}\tag{2}
\]
The bound and the equality are independent of \(n\) for \(n\ge Q\). A stronger, information-specific identity is
\[
 \boxed{H(h_1,\ldots,h_n)
 =H(N\mid T)+I(N;T)+\mathbb E\log d(N).}\tag{3}
\]
Thus \(\,I(N;T)\), not the potentially much larger \(\,H(T)\), is the exact additional histogram cost of mixing checkpoint-law types. If the histogram distribution is known, (1) is a directly checkable **necessary and sufficient entropy-budget test for this particular sampler**:
\[
 H(N)+\mathbb E\log d(N)\le\kappa s\bar L.
\tag{4}
\]
It is not asserted as a lower bound for every possible coupling.

**Proof.** By telescoping and averaging the uniform \(U\), \(\mathbb E[N_i\mid A=a]=Q\nu_a(v_i)\). Conditional on \(N\), uniform cyclic rotation puts symbol \(v_i\) at each fixed location with probability \(N_i/Q\), giving the exact marginal assertion. The primitive-period argument of r390 makes the orbit size precisely \(d(N)\). Because the canonical word is a function of the **global histogram \(N\) alone**, and not of its generating type \(T\), there are precisely \(d(N)\) equiprobable outputs conditional on \(N\). The output \(W\) determines \(N\) by counting its letters. Hence
\[
 H(W)=H(N)+H(W\mid N)=H(N)+\mathbb E\log d(N).
\]
The \(n\)-prefix for \(n\ge Q\) contains the entire \(W\) and is itself determined by \(W\), proving (1). There are \({Q+M-1\choose M-1}\) possible nonnegative compositions of \(Q\) across \(M\) symbols. For each fixed \(T=t\), at most \(m_t\le M\) systematic-rounding histogram patterns occur because the map \(U\mapsto N\) changes at no more than \(m_t-1\) distinct interior breakpoints; thus \(H(N\mid T)\le\log M\). Use \(H(N)=H(N\mid T)+I(N;T)\le H(T)+\log M\), and \(\log d(N)\le\log Q\), proving (2)–(3). QED.

For direct computation, the unconditional histogram law is exactly
\[
 \Pr(N=\mathbf n)=\sum_a\Pr(A=a)\,
 {\rm Leb}\{u\in[0,1):N(a,u)=\mathbf n\}.
\tag{5}
\]
This is a **push-forward of the true checkpoint experiment**. Different conditional laws can induce the same count pattern; (5) automatically merges them, unlike a bound that charges the entire type label.

## 2. The zero-failure event certificate remains valid

For each supported \(a\), every good signed coordinate \(c\), eligible \(K,x\) and event \(D_{a,c,K,x}\subseteq\mathcal D\) from r386/r389, regard its support indices as a subset \(B\subseteq\{1,\ldots,M\}\) in the fixed global order. Let \(b(B)\) be the minimum of the numbers of maximal consecutive runs of \(B\) and its complement, with \(b=0\) for empty/full sets. The exact systematic discrepancy identity telescopes in that global order:
\[
 |\sum_{v_i\in D}N_i-Q\nu_a(D)|<b(B)
\]
when \(b(B)>0\), and is zero otherwise. Thus if
\[
 \boxed{Q\,\delta(3-\tau-4\delta)\frac{u_c}{p_c}>
 b(B_{a,c,K,x})\quad\text{for every eligible }(a,c,K,x),}\tag{6}
\]
then every \(n=LQ\), \(L\ge1\), satisfies r386's conditional lower-tail sampler property (CS) with **zero failure probability**. This is the same proof and exact coverage threshold as r389/r391, now paired with (1) instead of the law-type bound. A universally sufficient fallback is \(Q\delta(3-\tau-4\delta)\min_c(u_c/p_c)>M\). All of r386's separate conditional-coverage, joint-entropy and geometric hypotheses remain in force.

**Gaussian schedule read-through.** At the exact next checkpoint \(A=A_{i+1}\) of the pinned `schedule.tex`, its conditional terminal displacements do lie in one finite \(\mathcal D_{i+1}\), uniformly over supported \(A\) in each fixed-start experiment. The coupling is an *auxiliary list-test experiment*; it need not be substituted for the physically defined forward walk. Therefore (5)–(6) yield a concrete alternative data-cost verification for that exact walk, namely (4), provided the actual checkpoint-law histogram distribution and the other original transfer assumptions are established. The prior \(\le n_i\log|\mathcal D_{i+1}|\) proof remains a valid independent route. This note does not claim the new budget is smaller for that schedule before its histogram probabilities are computed.

## 3. Exact 64-type counterexample to charging the full law-type entropy

Take \(Q=7\), \(J=64\), \(A\) uniform on \(\{1,\ldots,J\}\), and the shared alphabet \(\mathcal D=\{0,1\}\). Define
\[
 \theta_j=\frac1Q\left(\frac13+\frac{j}{3(J+1)}\right),
 \quad \nu_j(1)=\theta_j,\quad \nu_j(0)=1-\theta_j.
\]
The \(J\) conditional laws are all distinct: \(H(T)=\log64\). But \(Q\theta_j\in(1/3,2/3)\), so the rare-symbol count \(N_1\) is only \(0\) or \(1\), and
\[
 \Pr(N_1=1)=Q\mathbb E\theta_A=\frac12.
\]
There is one all-zero period of probability \(1/2\) and exactly seven distinct one-rare-symbol periods, each with probability \(1/14\). Hence
\[
 \boxed{H(h_1,\ldots,h_n)=\log2+\tfrac12\log7
 \quad(\forall n\ge7),}
\]
which is approximately \(1.6661022551\) nats, compared with \(H(T)=\log64\approx4.1588830834\) nats. Every position has the **exact unconditional rare-symbol marginal** \(1/14\), and at checkpoint \(j\) it has the exact conditional marginal \(\theta_j\). A finite exact-rational enumeration of all 64 types and eight output words reproduces the distribution and the entropy identity.

~~~python
from fractions import Fraction as F
from collections import defaultdict
from math import log
Q,J=7,64
P=defaultdict(F)
for j in range(1,J+1):
    theta=(F(1,3)+F(j,3*(J+1)))/Q
    a=Q*theta # probability of one rare symbol in systematic count
    P[(0,)*Q]+=(1-a)/J
    for phase in range(Q):
        w=tuple(int(i==phase) for i in range(Q))
        P[w]+=a/(J*Q)
assert len(P)==8
assert P[(0,)*Q]==F(1,2)
assert all(P[tuple(int(i==phase) for i in range(Q))]==F(1,14)
           for phase in range(Q))
assert all(sum(prob for w,prob in P.items() if w[i])==F(1,14)
           for i in range(Q))
H=-sum(float(v)*log(float(v)) for v in P.values())
assert abs(H-(log(2)+log(7)/2))<1e-12
print(len(P),H)
~~~

## 4. Attribution and remaining real review

Original frozen source: [openai/math@adc7f124 coverage-transfer.tex](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex); exact Gaussian sampling schedule at that same commit: [schedule.tex](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/schedule.tex). Inputs: r386 (changed-model CS transfer), r389 (ordered event discrepancy), r390 (primitive period), and r391 (fixed-\(Q\) iteration). The original Researcher `EM-EMF6D046-5A2844` retains their own saved Task work. The mathematical authorship and evidence exposure in this note are the **same Driver scientific context** as r386–r391 and **not an independent adjudication**.

Open point: evaluate actual \(\Pr(N=\mathbf n)\) from the Gaussian exact-checkpoint law, compare (4) with \(\kappa_i s_iL_*\) in `schedule.tex`, and decide if the type-free construction yields a quantitative schedule improvement. Formal Source/Activity linking, Native Result and independent acceptance still require the correct original role/DA and frozen target. Task, Result and mother objective completion are unchanged.
