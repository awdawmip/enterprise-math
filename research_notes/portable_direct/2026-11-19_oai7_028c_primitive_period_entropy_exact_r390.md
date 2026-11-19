# OAI7 r390 — Primitive-period optimization and denominator-uniform entropy for exact conditional sampling

Date: 2026-11-19. **Author-side mathematical proof**, not independent Driver acceptance or a frozen Native Result. Task: `RS-OAI7-028-C-20261007-6F2A81` (publication `TP2-96FAC49786245691AE19`). Inputs: [r387](https://github.com/awdawmip/enterprise-math/blob/a6e57470351805f0aae5ee708c9906b61d901556/research_notes/portable_direct/2026-11-19_oai7_028c_rational_law_balanced_cyclic_sampler_r387.md), [r388](https://github.com/awdawmip/enterprise-math/blob/9f6a710645f341320159aa5b3f3730e467a51073/research_notes/portable_direct/2026-11-19_oai7_028c_real_law_systematic_balanced_sampler_r388.md), and [r389](https://github.com/awdawmip/enterprise-math/blob/82a3f1cf681892528a858ac14bcbba5c3dee3ed2/research_notes/portable_direct/2026-11-19_oai7_028c_event_discrepancy_fiber_bound_r389.md).

## 1. Exact conditional entropy of a primitive-period balanced sampler

Fix any finite conditional law \(\nu_t\), including irrational probabilities, and an integer \(n\ge1\). In the systematic rounding construction of r388, every realized count vector \(N=(N_i)_i\) is nonnegative integer with \(\sum_iN_i=n\). Let
\[
g(N)=\gcd\{N_i:N_i>0\},\qquad d(N)=n/g(N).
\]
Divide the count vector by \(g(N)\), make a canonical base word \(b(N)\) of length \(d(N)\) with \(N_i/g(N)\) copies of each symbol, and repeat it \(g(N)\) times to form the length-\(n\) word \(w(N)\). Conditional on \(N\) and the law type, choose a uniform rotation of its **distinct cyclic orbit**, comprising exactly \(d(N)\) different words.

**Theorem.** Every trial index \(\ell\) retains exactly the one-trial conditional law \(\nu_A\), and all empirical count and zero-tail statements of r388/r389 continue to hold. Let \(T(A)\) denote the full actual law type and \(N\) its systematic rounded counts. In the same logarithm base as Shannon entropy,
\[
\boxed{H(\mathcal H\mid T)
 =H(N\mid T)+\mathbb E[\log d(N)],}
\]
where \(H(\cdot\mid T)\) denotes the **averaged scalar conditional entropy**, and hence
\[
\boxed{H(\mathcal H)\le
H(T(A))+H(N\mid T(A))+\mathbb E\log\frac{n}{g(N)}
\le H(T(A))+\log M+\mathbb E\log\frac{n}{g(N)}.}\tag{1}
\]
This improves r388 whenever a rounded-count vector has a nontrivial common divisor.

**Proof.** The integer vector \(N/g\) has gcd one. A word of length \(d\) with these counts cannot have a strictly smaller cyclic period \(e\mid d\), since its repetitions would force every count to be divisible by \(d/e>1\). Every such base word thus has least period \(d\), and the repeated length-\(n\) word has exactly \(d\) distinct rotations. Uniform choice among them gives probability \(N_i/n\) for symbol \(i\) at each position. Averaging systematic rounding over its original shift \(U\) gives \(\mathbb EN_i=n\nu_t(v_i)\), so every one-trial marginal equals \(\nu_t\). Counts are unchanged by rotation, preserving all event discrepancies and (CS) certificates. Conditional on \(T\), the count vector \(N\) is determined by the observed output word (via its symbol counts), so the entropy chain rule gives the asserted equality, with \(H(\mathcal H\mid N,T)=\log d(N)\). Finally \(H(N\mid T)\le\log M\), by r388's at-most-\(m_t\) breakpoint pattern bound. QED.

This optimizes orbit size **among uniform rotations of a deterministic word with fixed counts**: any length-\(n\) word with counts \(N\) must have cyclic period divisible by \(n/g(N)\), and the construction attains that bound. No claim is made that it minimizes entropy among all possible non-rotation couplings.

## 2. Rational laws: fixed denominator instead of sample length

Assume every conditional finite law \(\nu_t\) has rational atom weights, and let \(D_t\) be its **least common denominator**, i.e. the smallest positive integer such that \(D_t\nu_t(v)\) is integral at every support atom. Let \(D\) be a common multiple of all the \(D_t\). For any \(n\) divisible by \(D\), the systematic counts are **deterministic**,
\[
N_i=n\nu_t(v_i).
\]
Because \(\gcd\{D_t\nu_t(v_i)\}_i=1\), one has \(g(N)=n/D_t\), so \(d(N)=D_t\). Thus the primitive-period sampler has
\[
\boxed{
H(\mathcal H\mid T)=\mathbb E[\log D_T],\qquad
H(\mathcal H)\le H(T(A))+\mathbb E[\log D_T]
\le H(T(A))+\log D.}\tag{2}
\]
The bound is **independent of the number \(n\) of repeated trials** once \(n\) is a common denominator multiple. For every event \(E\) on the lattice support, its sampled frequency is exactly its conditional probability:
\[
\#\{\ell:h_\ell\in E\}=n\,\nu_A(E)\quad\text{almost surely}.
\]
Consequently r386's conditional sampler tail property (CS) is zero-failure under the original strict conditional mass-floor hypotheses, with **no additional Chernoff or size requirement on \(n\)**. The rest of r386's geometric, conditional-coverage, source-exposure and entropy assumptions still apply unchanged.

This is a sharpening of the rational-law result r387: that note already allowed shorter cyclic periods but bounded the entropy by \(\log n\); (2) identifies the shortest period and a bound that remains fixed when the chosen trial count grows.

## 3. Two boundary families: fixed-denominator saving and sharpness of the logarithmic term

For a fixed rational distribution \((1/2,1/2)\) and every even \(n\), use the alternating word of period \(2\) repeated \(n/2\) times and one fair cyclic phase. All \(n\) positions have the prescribed marginals, the histogram is exact, and \(H(\mathcal H)=\log2\), rather than \(O(\log n)\).

Conversely, for each integer \(n\ge2\), consider the **\(n\)-dependent** binary law \((1-1/n,1/n)\), and demand exactly one rare symbol in every length-\(n\) output while preserving its probability \(1/n\) at every position. The rare symbol's position \(J\) must be uniformly distributed on \(\{1,\ldots,n\}\). Since \(J\) is a function of the output, **every coupling** with these exact properties has
\[
\boxed{H(\mathcal H)\ge H(J)=\log n.}\tag{3}
\]
The uniform cyclic rotation of the one-rare-symbol word attains equality. Hence the \(\log n\) term in r388 is unavoidable **for some laws varying with \(n\)**; it is not a universal lower bound for fixed rational laws.

## 4. Exact nonuniform p=11 check and budget improvement

Use the r388 law on \(\mathbb Z\), with \(\nu(0)=1/3\), \(\nu(i)=2/27\) for \(1\le i\le9\), and \(\nu(10)=0\), with \(\phi(h)=h\bmod11\), \(\rho=7/16\), \(\tau=3/8\), \(\delta=1/64\), \(u=\lceil\sqrt{11}\rceil=4\). Its least denominator is \(D=27\). A primitive base word has nine copies of \(0\) and two copies of each \(1,\ldots,9\), with gcd \(1\). Choosing a uniform one-of-27 cyclic phase gives exact marginals, deterministic exact empirical frequencies and
\[
\boxed{H(\mathcal H)=\log27}
\]
for \(n=27\) **and** for every \(n=27q\) when the base period is repeated \(q\) times. The earlier sufficient generic sample lengths were \(n\ge687\) (r388's M bound) or \(n\ge275\) (r389's fiber bound); exact rational periodicity allows the much shorter \(n=27\) for the changed-model CS certificate.

In the fixed \(n=27\) example, exhaustive exact-integer tests over the 27 distinct phases, all \(\binom{11}{4}\) test subsets, and all candidate shifts avoiding exceptional residue \(10\), give **62,370 tests** and a minimum of **8 hits**; the strict list threshold is \(n(25/64)(4/11)=675/176\), which is smaller than 8. This checks the sampler condition, not the original Gaussian theorem's high-entropy or geometric size hypotheses for \(p=11\).

~~~python
from itertools import combinations
from math import gcd, log
p, u, D = 11, 4, 27
base = [0]*9 + [z for i in range(1,10) for z in (i,i)]
assert len(base) == D and gcd(9,2) == 1
orbit = {tuple(base[(j+i)%D] for i in range(D)) for j in range(D)}
assert len(orbit) == D
assert all(sum(base[(j+i)%D] == v for j in range(D)) ==
           (9 if v == 0 else (2 if 1 <= v <= 9 else 0))
           for i in range(D) for v in range(p))
checks, min_hits = 0, D
for K0 in combinations(range(p),u):
    K=set(K0)
    for x in range(p):
        if (x+10)%p in K: continue
        for phase in range(D):
            hits=sum((x+base[(phase+j)%D])%p in K for j in range(D))
            assert 64*p*hits > 25*D*u
            min_hits=min(min_hits,hits)
            checks += 1
assert (checks,min_hits)==(62370,8)
print(checks,min_hits,log(D))
~~~

## 5. Provenance and actual review status

Original Gaussian source: [openai/math@adc7f124 coverage-transfer.tex](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex). The new theorem is a mathematical extension in this Driver-authored scientific context and remains **author-side**, not an independent review of any native frozen Result. Preserve original Task contributor `EM-EMF6D046-5A2844`. The genuine Gaussian-walk checkpoint distribution's rational denominators, law-type entropy and admissible auxiliary coupling still require exact inspection. Any actual application must meet all remaining hypotheses of r386 and its entropy budget; no native acceptance or mother-objective completion is asserted.
