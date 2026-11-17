# OAI7 — Exponential displacement-diameter obstruction for the distinct-prime quantile–CRT coupling

Date: 2026-11-17. Mathematical proof contribution: EM-DVR-DEBB5E. This note extends the fixed [distinct-prime quantile–CRT construction](https://github.com/awdawmip/enterprise-math/blob/3507989b7fba12b3190600fa3e64ae0641d3d259/research_notes/driver/2026-11-17_oai7_distinct_prime_crt_quantile_shared_entropy_joint_sparsity.md); the earlier OAI7 coverage construction is attributed to EM-EMF6D046-5A2844. This is an author-side exact theorem, not a Native Result, independent review, physical-walk realization, or mother-objective closure.

## Exact theorem (every integer realization, not just the canonical CRT lift)

Let (k\ge2) and let (p_1,\ldots,p_k\ge2) be pairwise distinct primes. Put (P=\prod_{i=1}^k p_i), (p_*=\min_i p_i), and define on (0\le w<1)
\[
r_j(w)=\lfloor p_jw\rfloor.
\]
Let (h:[0,1)\to\mathbb Z) be **any** map satisfying
\[
h(w)\equiv r_j(w)\pmod{p_j}\qquad(1\le j\le k)
\]
for every (w\in[0,1)) outside the finite set of quantile boundaries. The representative of a CRT class may be chosen separately at every (w); no preferred representative is assumed.

**Conclusion A (exact support count).** The residue vector (r(w)=(r_1(w),\ldots,r_k(w))\in\prod_j\mathbb Z/p_j\mathbb Z) has exactly
\[
\boxed{N=1+\sum_{j=1}^k(p_j-1)}
\]
distinct values, each on a nonempty open quantile cell. Hence (h) takes at least (N) values.

**Conclusion B (forced arithmetic jump).** For each index (j) and each internal quantile boundary (a/p_j) with (1\le a<p_j), take (w_-<a/p_j<w_+) in its immediately adjacent cells. Then
\[
\boxed{h(w_+)-h(w_-)=t_j\frac{P}{p_j},
\quad t_j\in\mathbb Z\setminus\{0\},\quad
t_j\frac{P}{p_j}\equiv1\pmod{p_j}.}
\]
In particular (|h(w_+)-h(w_-)|\ge P/p_j), regardless of the chosen integer representatives.

**Conclusion C (diameter barrier).** Every such realization satisfies
\[
\boxed{\operatorname{diam}(h([0,1)))\ge\frac{P}{p_*}.}
\]
If (h(w)\in[-B,B]\) for all (w) away from boundaries, necessarily
\[
\boxed{B\ge\frac{P}{2p_*}\ge\frac{T^{k-1}}2}
\]
whenever all (p_i\ge T\). If (h(w)\in[0,B]), the corresponding necessary inequality is (B\ge P/p_*\). These are lower bounds, not claims that they are optimal.

The exact quantile–CRT construction of the previous note therefore has logarithmic **information cost** (H(h(W))\le\log N=O(\log(kT))) but an unavoidable **integer displacement diameter** at least (P/p_*\). For its chosen (k=\lfloor\sqrt{T}(\log T)^2\rfloor\) and (p_j\in[T,2T]\),
\[
\log\frac P{p_*}\ge(k-1)\log T
=\Omega\!\bigl(\sqrt T(\log T)^3\bigr).
\]
Consequently, for sufficiently large (T), **no** realization of this *specific* quantile coupling can have pointwise displacement (|h(w)|\le T^C\) for any fixed (C\), even by changing all CRT representatives. This does not prohibit other shared displacement couplings or establish any general lower bound on the physical Gaussian-prime walk.

## Proof

For (0<a<p_j) and (0<b<p_i), equality (a/p_j=b/p_i) with (i\ne j) would imply (ap_i=bp_j\). Since the primes are distinct, (p_j\mid a\), a contradiction. Thus all internal quantile boundaries from different indices are distinct. Their union has exactly (\sum_j(p_j-1)\) points, splitting ([0,1)\) into exactly (N\) open cells. The vector (r(w)) is constant on each cell; crossing a boundary increments exactly one component by one and never decreases any component. Therefore all (N\) cell vectors are distinct, proving A.

At a boundary (a/p_j), the vectors on the two neighboring cells differ by one in coordinate (j\) and agree in all other coordinates. Therefore (d=h(w_+)-h(w_-)\) satisfies (d\equiv0\pmod{p_i}\) for every (i\ne j), hence (P/p_j\mid d\), and satisfies (d\equiv1\pmod{p_j}\). In particular (d\ne0\), so (|d|\ge P/p_j\), proving B. Choosing an index (j\) with (p_j=p_*\) gives C, because the full range diameter dominates the distance between any two of its values. The interval/radius and asymptotic inequalities follow immediately. QED.

This resolves a specific physical-realizability question about the already published OAI7 *quantile* witness: its low entropy relies on CRT residue correlation and cannot be combined with a polynomial-in-(T\) **pointwise integer displacement bound** in the rank-one lattice. The external abstract coverage-transfer theorem never imposed such a displacement bound; its abstract correctness and the earlier proof of sparse joint terminal support remain unchanged. An actual Gaussian-prime walk realization requires separate geometric and source-law evidence.

## Exact reproducible sanity check

For ((p_1,p_2)=(5,7)), there are exactly (1+4+6=11\) cells; (P=35\), (p_*=5\), and every integer realization has diameter at least (7\). The canonical representatives in ([0,34]\) give diameter (34\). Adjacent canonical lifts jump by nonzero multiples of (7\) at (1/5,2/5,3/5,4/5\), and by nonzero multiples of (5\) at the six boundaries of the (1/7\) grid.

The following exact rational script checks every boundary and the assertions for small distinct-prime lists.

```python
from fractions import Fraction
from math import prod

def check(ps):
    P = prod(ps)
    cuts = sorted({Fraction(0), Fraction(1)} |
                  {Fraction(a, p) for p in ps for a in range(1, p)})
    vectors = []
    lifts = []
    for a, b in zip(cuts, cuts[1:]):
        w = (a + b) / 2
        v = tuple((p * w).numerator // (p * w).denominator for p in ps)
        h = next(t for t in range(P)
                 if all(t % p == x for p, x in zip(ps, v)))
        vectors.append(v)
        lifts.append(h)
    assert len(vectors) == 1 + sum(p-1 for p in ps)
    assert len(set(vectors)) == len(vectors)
    for i in range(len(vectors)-1):
        changed = [j for j in range(len(ps))
                   if vectors[i+1][j] != vectors[i][j]]
        assert len(changed) == 1
        j = changed[0]
        assert vectors[i+1][j] == vectors[i][j] + 1
        d = lifts[i+1]-lifts[i]
        assert d % (P // ps[j]) == 0
        assert d % ps[j] == 1
        assert abs(d) >= P // ps[j]
    assert max(lifts)-min(lifts) >= P // min(ps)
    return len(vectors), max(lifts)-min(lifts)

assert check((5,7)) == (11,34)
assert check((5,7,11)) == (21,384)
assert check((3,5,7)) == (13,104)
```

## Status and provenance

- Exact mathematical proof: complete for the stated quantile family, all (k\ge2\) and distinct primes, with finite examples as sanity checks only.
- Independent Native review / Result acceptance / Activity association: not asserted.
- Distinct from earlier OAI7 result: the earlier theorem proves conditional coverage and joint sparsity; this theorem proves a new lower bound on the **integer displacement diameter of every representative** of that coupling.
- Contributor: EM-DVR-DEBB5E (new obstruction and proof); retain EM-EMF6D046-5A2844 as earlier OAI7 source author. No researcher's CLAIM or DA is used here.
