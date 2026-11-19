# OAI7 r388 — Exact finite-alphabet sampling for arbitrary real checkpoint laws with logarithmic common-data entropy

Date: 2026-11-19. Status: **author-side mathematical proof and exact finite-arithmetic example**, distinct from Native Result intake or independent Driver acceptance. Scope: the exact finite-checkpoint, finite-lattice-displacement setup of OAI7-028-C.

## 1. General theorem (the rationality restriction in r387 is unnecessary)

Let \(A\) be finite, and for each supported checkpoint \(a\) let \(\nu_a\) be **any** finitely supported probability measure on the lattice \(\Lambda\); its weights may be irrational. Let \(T(A)\) record the exact distinct law type and a fixed canonical ordering of its support (the same type uses the same ordering). Put
\[
 m_a=|\operatorname{supp}\nu_a|,\qquad M=\max_a m_a.
\]
For any fixed integer \(n\ge1\), the following explicit construction produces **exactly the original one-trial conditional marginal** \(\nu_a\) at every sample index, while sharply bounding the empirical error and the entropy of the *entire* sequence.

For law type \(t\), enumerate its positive-probability support \(v_1,\ldots,v_m\) and let
\[
 F_0=0,\quad F_i=\sum_{j\le i}\nu_t(v_j),\quad F_m=1.
\]
Sample an auxiliary \(U\sim\operatorname{Unif}[0,1)\), independent of \(A\), and form integer counts
\[
 \boxed{N_i(U)=\lfloor nF_i+U\rfloor-\lfloor nF_{i-1}+U\rfloor.}\tag{1}
\]
The \(N_i\) are nonnegative and sum to \(n\). Form a canonical word of length \(n\) containing exactly \(N_i\) copies of displacement \(v_i\). Independently sample one uniform cyclic rotation \(R\in\{0,\ldots,n-1\}\), and let \(h_1,\ldots,h_n\) be that rotated word.

**Theorem (systematic balanced sampler).** For every supported \(a\) and \(1\le\ell\le n\):
\[
 \boxed{\Pr\{h_\ell=v_i\mid A=a\}=\nu_a(v_i).}\tag{2}
\]
For every subset \(D\) of the lattice support, the empirical number of visits obeys, **surely**,
\[
 \boxed{\left|\sum_{\ell=1}^n{\bf1}_{\{h_\ell\in D\}}-n\nu_a(D)\right|<m_a.}\tag{3}
\]
Moreover the shared vector \(\mathcal H=(h_1,\ldots,h_n)\) is a finite random variable and satisfies
\[
 \boxed{H(\mathcal H\mid A)\le\log M+\log n,\qquad
 H(\mathcal H)\le H(T(A))+\log M+\log n.}\tag{4}
\]

**Proof.** Write \(\{z\}=z-\lfloor z\rfloor\). From (1),
\[
 N_i-n\nu_t(v_i)=\{nF_{i-1}+U\}-\{nF_i+U\}\in(-1,1).
\]
The sum telescopes to \(\lfloor n+U\rfloor-\lfloor U\rfloor=n\). For every real \(z\), \(\mathbb E_U\lfloor z+U\rfloor=z\), so \(\mathbb E N_i=n\nu_t(v_i)\). After a uniform cyclic rotation, any given position in the word is \(v_i\) with conditional probability \(N_i/n\); averaging over the count vector yields (2). For any event \(D\), the empirical count is exactly \(\sum_{v_i\in D}N_i\); summing the strict per-symbol errors gives (3).

The count vector changes only when \(U\) crosses one of the at most \(m-1\) interior breakpoints determined by the fractional parts of \(nF_i\), \(i=1,\ldots,m-1\). Therefore it has at most \(m\) possible values, and \(H(N\mid T=t)\le\log m\). The full sample vector is a deterministic function of \((T,N,R)\) where \(R\) has \(n\) equally likely values. Thus \(H(\mathcal H\mid A)\le\log M+\log n\), and \(H(\mathcal H)\le H(T)+\log M+\log n\). Although \(U\) was written as continuous for clarity, only its at most \(m\) discrete breakpoint classes affect the output. The entire output \(\mathcal H\) remains finite-alphabet as required in the source Shannon argument. QED.

## 2. Zero-failure conditional sampler criterion for all real finite laws

Adopt the exact common checkpoint \(Y=y(A)\), signed homomorphisms \(\phi_c\), and notation of [r386](https://github.com/awdawmip/enterprise-math/blob/9c5b8c0da18f6a85b640da07664fdd9b8cb4c92b/research_notes/portable_direct/2026-11-19_oai7_028c_dependent_conditional_sampler_coverage_transfer_r386.md). At a good coordinate \(c\) and supported \(a\), let \(p_c=|G_c|\), \(u_c=\lceil p_c^{1-\beta}\rceil\), \(\rho=\tau+4\delta\), \(E_{a,c}=\{v:\Pr(\phi_c(h_1)=v\mid A=a)<\rho/p_c\}\).

For every \(K\subseteq G_c\) of size \(u_c\) and every \(x\in G_c\) satisfying \(|(K-x)\cap E_{a,c}|\le\delta u_c\), the *original* one-trial law gives
\[
\nu_a\{h:x+\phi_c(h)\in K\}
\ge \rho(1-\delta)\,u_c/p_c.
\]
Applying (3) to this lattice event gives
\[
 \sum_{\ell=1}^n{\bf1}_{\{x+\phi_c(h_\ell)\in K\}}
 > n\rho(1-\delta)u_c/p_c-M.
\]
Thus the **strict, deterministic** lower-tail sampler property (CS) of r386 holds with zero failure probability for all checkpoints, coordinates, sets and candidates as soon as
\[
 \boxed{n\,\delta(3-\tau-4\delta)\,
           \min_c\frac{u_c}{p_c}>M.}\tag{5}
\]
In fact any integer \(n\) above this explicit threshold works, irrespective of whether the conditional law is rational or irrational.

**Corollary.** The entropy-to-coverage conclusion of r386 holds for arbitrary finitely supported real conditional displacement laws if all its other hypotheses and
\[
 \boxed{H(T(A))+\log M+\log n\le \kappa s\bar L}
\]
hold, with \(n\) satisfying (5). The old conditionally-iid Shannon cost was \(n\,\mathbb E_aH(\nu_a)\); this *alternative sampler* pays at most the entropy of the law type plus two **logarithmic** terms. For fixed \(M,p,\tau,\delta,\beta\), this is a precise finite construction rather than a heuristic independence replacement.

The construction changes the *joint law of the repeated auxiliary displacements* while preserving each marginal \(\nu_a\) **exactly**. It does not, by itself, prove that the actual Gaussian-walk geometry authorizes that joint sampling schedule or that its information budget is small.

## 3. Exact nonuniform finite certificate (not relying on rationality for the theorem)

Take \(\Lambda=\mathbb Z\), \(p=11\), \(\phi(h)=h\bmod11\), and
\[
\nu(0)=1/3,\qquad
\nu(i)=2/27\ \ (i=1,\ldots,9),\qquad\nu(10)=0.
\]
With \(\rho=7/16\), \(\tau=3/8,\delta=1/64,\beta'=\beta=1/2\), the conditional exception set is exactly \(\{10\}\), and \(u=\lceil\sqrt{11}\rceil=4\). Choose \(n=700\), \(M=10\). Then
\[
 n\delta(3-\tau-4\delta)\frac up
 =\frac{700}{64}\frac{41}{16}\frac4{11}
 =\frac{7175}{704}>10=M,
\]
so (5) is satisfied.

Exact rational enumeration of all breakpoint intervals produces **10 possible count vectors**. For every such vector, every size-4 test subset \(K\) and every \(x\) whose translated \(K\) avoids the exception residue 10, the observed hit count is at least **206**, while the list threshold is \(n(25/64)(4/11)=4375/44\approx99.43\). The exhaustive test checks **23,100** triples \((N,K,x)\) and verifies, by exact arithmetic, \(\mathbb EN_i=n\nu(i)\) for every \(i\).

~~~python
from fractions import Fraction as F
from itertools import combinations
p, n, u = 11, 700, 4
prob = [F(1,3)] + [F(2,27)]*9 + [F(0)]
cum = [F(0)]
for x in prob: cum.append(cum[-1]+x)
breaks = sorted({F(0),F(1)} |
                {F(1)-(n*z % 1) for z in cum[1:-1] if n*z % 1})
patterns = []
for lo, hi in zip(breaks,breaks[1:]):
    U = (lo+hi)/2
    N = [int((n*cum[i+1]+U).__floor__())-
         int((n*cum[i]+U).__floor__()) for i in range(p)]
    assert sum(N)==n
    assert all(abs(F(N[i])-n*prob[i])<1 for i in range(p))
    patterns.append((hi-lo,N))
assert len(patterns)==10
assert all(sum(w*N[i] for w,N in patterns)==n*prob[i] for i in range(p))
checks, minhit = 0, n
for weight,N in patterns:
    for Ktuple in combinations(range(p),u):
        K = set(Ktuple)
        for x in range(p):
            if (x+10)%p in K: continue
            hits = sum(N[v] for v in range(p) if (x+v)%p in K)
            minhit = min(minhit, hits)
            assert 64*p*hits > 25*n*u
            checks += 1
assert (checks,minhit)==(23100,206)
print(len(patterns),checks,minhit)
~~~

The real-law construction is proved for all finite supports; these computations only certify this concrete test case.

## 4. Exact provenance and remaining scientific applicability

- External pinned theorem: [openai/math@adc7f124 \`coverage-transfer.tex\`](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex). Its independent conditional trials remain one valid sufficient mechanism; the exact result of this note concerns a separately proved correlated sampler.
- [r385](https://github.com/awdawmip/enterprise-math/blob/7541049857493e92fd9489705cc05ed77528ea68/research_notes/portable_direct/2026-11-19_oai7_028c_strict_coverage_min_entropy_iid_cost_r385.md) is the conditional-iid lower-bound theorem. [r386](https://github.com/awdawmip/enterprise-math/blob/9c5b8c0da18f6a85b640da07664fdd9b8cb4c92b/research_notes/portable_direct/2026-11-19_oai7_028c_dependent_conditional_sampler_coverage_transfer_r386.md) establishes the general conditional-sampler replacement, and [r387](https://github.com/awdawmip/enterprise-math/blob/a6e57470351805f0aae5ee708c9906b61d901556/research_notes/portable_direct/2026-11-19_oai7_028c_rational_law_balanced_cyclic_sampler_r387.md) handles rational laws with zero discrepancy. The present theorem discharges the rationality restriction.
- Original task \`RS-OAI7-028-C-20261007-6F2A81\` / immutable publication \`TP2-96FAC49786245691AE19\`; retain its original author \`EM-EMF6D046-5A2844\`.
- Remaining mathematics: estimate the actual conditional displacement-law type entropy \(H(T(A))\), true support size \(M\), and the schedule's permitted joint coupling for the Gaussian moat application. For X6/BRC, a typed carrier and provenance-safe event correspondence require a separate argument. No such applicability, independent Native Result, review or task closure is asserted by this note.
