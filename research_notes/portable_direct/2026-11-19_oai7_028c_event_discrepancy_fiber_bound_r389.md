# OAI7 r389 — Event-adaptive discrepancy and fiber-controlled dependent sampling

Date: 2026-11-19. Status: **author-side mathematical proof and exact finite check**, not Native Result acceptance or independent review. Task: `RS-OAI7-028-C-20261007-6F2A81`; publication `TP2-96FAC49786245691AE19`. The predecessor is [r388](https://github.com/awdawmip/enterprise-math/blob/9f6a710645f341320159aa5b3f3730e467a51073/research_notes/portable_direct/2026-11-19_oai7_028c_real_law_systematic_balanced_sampler_r388.md).

## 1. A sharper exact discrepancy theorem

Let (A) be finite, and for every supported (a) let (
u_a) be an arbitrary real-valued finite-support probability law, with positive support atoms (v_1,\ldots,v_{m_a}) in a law-type-dependent but fixed order. Use the r388 systematic counts
\[
N_i(U)=\lfloor nF_i+U\rfloor-\lfloor nF_{i-1}+U\rfloor,
\quad F_i=\sum_{j\le i}\nu_a(v_j),\quad U\sim\mathrm{Unif}[0,1).
\]
The uniformly rotated canonical word has exactly the original (
u_a) one-trial conditional marginal at **every position**, and still satisfies
\[
H(\mathcal H)\le H(T(A))+\log M+\log n,\qquad M=\max_a m_a.
\]
No rationality assumption or independence between trials is needed.

For any subset (D\subseteq\operatorname{supp}\nu_a), let (B=\{i:v_i\in D\}\subseteq\{1,\ldots,m_a\}). Write (r(B)) for the number of **maximal consecutive runs** of indices in (B), defining (r(\varnothing)=0), and put
\[
b(B)=\min\{r(B),r(B^{\mathrm c})\}.
\]
Then for every systematic-shift outcome (U),
\[
\boxed{\big|N(D)-n\nu_a(D)\big|<b(B)\quad\text{if }b(B)>0,}
\]
and the difference is **exactly zero** when (b(B)=0).

**Proof.** Set (f_i=\{nF_i+U\}\in[0,1)). The individual error is
\[
N_i-n\nu_a(v_i)=f_{i-1}-f_i.
\]
Over one maximal consecutive run ([l,r]\subseteq B), errors telescope to (f_{l-1}-f_r\in(-1,1)). Summing the runs gives absolute discrepancy (<r(B)) for (r(B)>0). Since the total discrepancy over all support atoms is (f_0-f_{m_a}=0), the discrepancy for (B) is the negative of that for (B^{\mathrm c}). Apply the same argument to the complement. The empty/full cases have zero error. QED.

In particular (b(B)\le |B|), and for nonempty (B) it also satisfies (b(B)\le\min(|B|,m_a-|B|)). The error depends on the **geometry of the event in support order**, not on the full support cardinality alone.

## 2. Exact zero-failure coverage-transfer criterion

Retain all the hypotheses of r386/r388: a fixed common checkpoint (A=a), good signed coordinate (c) with group size (p_c), the same one-trial conditional displacement law (
u_a), (u_c=\lceil p_c^{1-\beta}\rceil), (\rho=\tau+4\delta), and conditional exception set (E_{a,c}). For every (K\subset G_c) with (|K|=u_c), and every (x\in G_c) such that
\[
|(K-x)\cap E_{a,c}|\le\delta u_c,
\]
form the event on **support atoms**
\[
D_{a,c,K,x}=\{v\in\operatorname{supp}\nu_a:x+\phi_c(v)\in K\},
\]
and let (b_{a,c,K,x}=b(\{i:v_i\in D_{a,c,K,x}\})).

The original conditional mass-floor assumption gives
\[
\nu_a(D_{a,c,K,x})\ge(\tau+4\delta)(1-\delta)u_c/p_c.
\]
With (C=\delta(3-\tau-4\delta)>0), therefore **the conditional lower-tail property (CS) of r386 holds with failure probability zero** whenever, for all these (a,c,K,x),
\[
\boxed{nC\,u_c/p_c>b_{a,c,K,x}.}\tag{E}
\]
Indeed, the deterministic number of hits exceeds
(n(\tau+4\delta)(1-\delta)u_c/p_c-b_{a,c,K,x}),
which is strictly greater than (n(\tau+\delta)u_c/p_c) by (E). A simpler sufficient condition uses
\[
q_{a,c}=\max_{z\in G_c}\#\{i:\phi_c(v_i)=z\},
\]
the maximum multiplicity of a **positive-support atom in one coordinate fiber**. Since (|D_{a,c,K,x}|\le q_{a,c}u_c), condition (E) follows from
\[
\boxed{n\delta(3-\tau-4\delta)>\max_{a,c}\ p_cq_{a,c}.}\tag{F}
\]
Good-coordinate quantifiers and the original r386 geometry/entropy hypotheses are unchanged. In all cases one may retain the stronger of r388's support-size bound (M), the fiber bound (q_{a,c}u_c), and the exact run bound (b_{a,c,K,x}); no claim is made that fiber multiplicity is small for arbitrary Gaussian checkpoints. The law-type ordering may be chosen once in advance to reduce the maximal run count, without changing conditional marginals or the entropy bound.

This is a finite conditional sampler theorem. The original Gaussian-walk schedule must separately supply its actual law types, support/fibers and the entropy assumptions before a Gaussian-moat conclusion is asserted.

## 3. Exact finite example: 275 samples instead of 687

Use precisely the r388 example
\[
p=11,\quad \nu(0)=1/3,\quad\nu(i)=2/27\ (1\le i\le9),
\quad\nu(10)=0,\quad
\tau=3/8,\delta=1/64,\beta=\beta'=1/2,\rho=7/16.
\]
Here (u=4), (m=10), (E=\{10\}), and (phi(h)=h\pmod {11}) is injective on the ten positive-support atoms, so (q=1). Criterion (F) reduces to
\[
n\frac{41}{1024}>11.
\]
Thus the first sufficient integer is **(n=275)**. The support-only criterion of r388 needs (n>10\cdot11\cdot1024/(41\cdot4)), whose first sufficient integer is **687**. Both are proved sufficient conditions, not claims of minimal feasible sample number.

The following exact rational arithmetic check of the new (n=275) example enumerates all 10 positive-probability count patterns, all size-four test sets (K), and all shifts (x) avoiding the exceptional residue. It tests the strict CS count threshold and the marginal count expectations, reporting 23,100 valid combinations and minimum 80 hits.

```python
from fractions import Fraction as F
from itertools import combinations

p, n, u = 11, 275, 4
prob = [F(1, 3)] + [F(2, 27)] * 9 + [F(0)]
cum = [F(0)]
for v in prob:
    cum.append(cum[-1] + v)
breaks = sorted({F(0), F(1)} |
                {F(1) - (n*z % 1) for z in cum[1:-1] if n*z % 1})
patterns = []
for lo, hi in zip(breaks, breaks[1:]):
    U = (lo + hi) / 2
    counts = [(n*cum[i+1]+U).__floor__() -
              (n*cum[i]+U).__floor__() for i in range(p)]
    assert sum(counts) == n
    patterns.append((hi-lo, counts))
assert len(patterns) == 10
assert all(sum(w * counts[i] for w, counts in patterns) ==
           n*prob[i] for i in range(p))
checks, min_hits = 0, n
for weight, counts in patterns:
    for Kt in combinations(range(p), u):
        K = set(Kt)
        for x in range(p):
            if (x + 10) % p in K:
                continue
            hits = sum(counts[v] for v in range(p)
                       if (x + v) % p in K)
            assert 64 * p * hits > 25 * n * u
            min_hits = min(min_hits, hits)
            checks += 1
assert (checks, min_hits) == (23100, 80)
print(len(patterns), checks, min_hits)
```

## 4. Provenance and review boundary

This is a follow-on mathematical argument in the **same Driver-authored scientific context** as r386–r388, hence not an independent review. The external source is [openai/math@adc7f124 coverage-transfer.tex](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex). The original Task's named Researcher (EM-EMF6D046-5A2844) retains the original Source contributions. This file establishes only (E), (F) and the verified example; Native Result freeze, Driver acceptance, Task DONE and mother-objective closure require separate real receipts.
