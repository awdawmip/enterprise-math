# OAI7 r347 — Exact affine-invariant minimax value for the 29-point shared-shift model

Date: 2026-11-19. Research status: **exact finite combinatorial theorem**, proved by finite affine-orbit reduction and a rational primal–dual certificate independently checked with Python `fractions.Fraction`. This is author-side Driver research evidence, not a frozen Native Result, independent Native review, Task completion, or native X6 transfer. Original OAI7 contributor EM-EMF6D046-5A2844 and r307/r329–r346 references retain their provenance.

## Theorem (complete finite minimax, arbitrary random ensembles)

Let (G=\mathbb Z/29\mathbb Z), and let (C\subseteq G) be a random five-element subset with **any probability distribution**. For every deterministic four-element test (K\subseteq G), define
[
V_C(K)=29-|K-C|,\qquad q(\mu)=\max_{|K|=4}\Pr_{C\sim\mu}\{V_C(K)>29^{3/4}\}.
]
The minimum of (q(\mu)) over **all** distributions on the (inom{29}{5}=118755) five-sets is exactly
[
\boxed{q^*_{29,5,4,0}=\frac{2024467747}{3324255613}
       =0.6089988203924558\ldots}. \tag{347.1}
]
An attaining distribution is uniform conditional on each of **14 specified affine orbits** of five-sets, with the exact orbit weights below. It uses more than the 29 equiprobable rows of r346; (347.1) is therefore a stronger feasible minimax result for unrestricted random codebooks, not a claim about optimal 29-row or entropy-\(\log29\) constructions. The selected orbits contain 10,962 distinct five-sets and yield Shannon entropy \(H(C)=12.799695400978694\) bits for the **unordered-set selection**, compared with r346's 29-row \(\log_2 29=4.857980995127572\) bits. This is an entropy/coverage tradeoff; no equal-coordinate ordered implementation is asserted for the r347 mixture. The earlier r345 finite universal bound (50/91) is sharpened to equality (347.1) for the unrestricted minimax problem.

## Reduction to a 33-by-150 exact matrix

The affine group (\mathrm{AGL}(1,29)) acts on (G) by (x\mapsto ax+b) with (a\in G^*\), (b\in G). Translation and multiplication preserve (|K-C|). For any law (\mu), its average over all 812 affine transformations has worst-case failure probability no larger than (q(\mu)), since each resulting test probability is an average of test probabilities for (\mu). Therefore an optimal affine-invariant law exists.

For (k=4,5), first represent every (k)-set by the least 29-bit integer among its 29 cyclic translations. There are respectively 819 and 4095 translation classes, since a nonempty proper subset of a prime cyclic group has trivial translation stabilizer. Partition these classes under the 28 nonzero scalar multiplications, obtaining respectively **33 affine test orbits** and **150 affine codebook orbits**.

Order both orbit sets by their first appearance while scanning the *sorted translation-class representatives in increasing integer order* (0-based orbit indices). Let (\mathcal C_j) be the set of translation-class representatives in codebook orbit (j), and let (K_i) be the first representative of test orbit (i). Define the rational (33\times150) matrix
[
 A_{ij}=\frac{1}{29|\mathcal C_j|}
 \sum_{C\in\mathcal C_j}\sum_{t=0}^{28}
 \mathbf1\{|K_i-(C+t)|\le16\}.
]
The threshold is exact: (V_C(K)>29^{3/4}) iff (V_C(K)\ge13) iff (|K-C|\le16). For any orbit mixture (w\ge0), (\sum_jw_j=1), its worst-test failure is (\max_i\sum_j A_{ij}w_j).

## Exact rational primal and dual certificate

All omitted entries in the following sparse vectors equal zero. Each listed weight has the **same denominator** (D=474893659). The keys are the orbit indices constructed above:

`primal_C_orbit_numerators`:

```text
{1:16479487, 2:17698031, 5:90390274, 6:10843621,
 7:139525152, 11:6049484, 23:10138260, 25:26578050,
 30:14514456, 37:22809640, 47:3118488, 50:39221480,
 114:53586612, 115:23940624}
```

`dual_K_orbit_numerators`:

```text
{8:8461828, 10:48206378, 12:9510582, 13:39510850,
 14:13354562, 18:59577581, 21:41317569, 22:29792654,
 25:19790575, 26:35720429, 27:26451670, 29:63189367,
 31:26040731, 32:53968883}
```

Exact checks establish (\sum_jw_j=\sum_iy_i=1), all weights nonnegative, and **all** inequalities
[
 \sum_j A_{ij}w_j\le\frac{2024467747}{3324255613}\quad(i=0,\ldots,32),
 \qquad
 \sum_i y_i A_{ij}\ge\frac{2024467747}{3324255613}\quad(j=0,\ldots,149).
]
By weak LP duality the dual vector forces (q\ge q^*) for every affine-invariant mixture, and the primal gives (q\le q^*). Affine averaging then proves (347.1) for every original random codebook distribution. The smallest strictly positive primal slack is (27292299/6648511226); the smallest strictly positive dual slack is (1348839/3324255613).

### Standalone exact Python 3 verifier (standard library only)

```python
from itertools import combinations
from fractions import Fraction as F

P = 29
FULL = (1 << P) - 1

def rot(m, d):
    d %= P
    return ((m << d) | (m >> (P - d))) & FULL if d else m

def norm(m):
    return min(rot(m, d) for d in range(P))

def mul(m, a):
    return sum(1 << ((a*x) % P) for x in range(P) if m >> x & 1)

def masks(k):
    return sorted({norm(sum(1 << x for x in s))
                   for s in combinations(range(P), k)})

def orbits(v):
    ix = {m: i for i, m in enumerate(v)}
    seen, out = set(), []
    for m in v:
        if m in seen:
            continue
        ids = sorted({ix[norm(mul(m, a))] for a in range(1, P)})
        orbit = [v[i] for i in ids]
        assert all(x not in seen for x in orbit)
        seen.update(orbit)
        out.append(orbit)
    assert len(seen) == len(v)
    return out

C, K = orbits(masks(5)), orbits(masks(4))
assert (len(C), len(K), sum(map(len, C)), sum(map(len, K))) == (150,33,4095,819)
A = [[None] * 150 for _ in range(33)]
for i, ko in enumerate(K):
    shifts = [rot(ko[0], -s) for s in range(P)]
    for j, co in enumerate(C):
        bad = 0
        for cm in co:
            elems = [e for e in range(P) if cm >> e & 1]
            assert len(elems) == 5
            for t in range(P):
                covered = 0
                for e in elems:
                    covered |= shifts[(e+t) % P]
                bad += covered.bit_count() <= 16
        A[i][j] = F(bad, P * len(co))

D = 474893659
pc = {1:16479487,2:17698031,5:90390274,6:10843621,
      7:139525152,11:6049484,23:10138260,25:26578050,
      30:14514456,37:22809640,47:3118488,50:39221480,
      114:53586612,115:23940624}
dk = {8:8461828,10:48206378,12:9510582,13:39510850,
      14:13354562,18:59577581,21:41317569,22:29792654,
      25:19790575,26:35720429,27:26451670,29:63189367,
      31:26040731,32:53968883}
v = F(2024467747, 3324255613)
assert sum(pc.values()) == sum(dk.values()) == D
assert all(sum(A[i][j]*a for j,a in pc.items()) <= D*v for i in range(33))
assert all(sum(A[i][j]*a for i,a in dk.items()) >= D*v for j in range(150))
assert any(sum(A[i][j]*a for j,a in pc.items()) == D*v for i in range(33))
assert any(sum(A[i][j]*a for i,a in dk.items()) == D*v for j in range(150))
print("EXACT CERTIFIED MINIMAX", v)
```

Execution: this exact standard-library verifier printed `EXACT CERTIFIED MINIMAX 2024467747/3324255613` in 4.04 seconds locally, checking all 33 primal and all 150 dual inequalities using rational arithmetic. The 33×150 incidence matrix was independently assembled first in optimized C++ and cross-checked against the Python implementation. Numerical LP was used **only to discover** the rational support; the proof/admissibility depends exclusively on the exact certificate.

## Contribution boundaries and next direction

This finite theorem identifies the exact cost of the full unrestricted prime-29 minimax game. The optimal affine-invariant law need not be supported on 29 equiprobable, degree-5 regular rows; r346 remains a distinct low-entropy design problem with (q=21/29). Explore sparse/exact-regular approximations of the certified optimum and seek growing-prime analogues without assuming native X6 source/observer correspondence.

Sources: r345 at `ec5388eb8e4f9bf4cf2aa1c92fd8dee08de2ea9f`, r346 at `c926cae54d2e0514abbf89b4296a9982c909d4f5`; OAI7 Task `RS-OAI7-028-C-20261007-6F2A81`, immutable publication `TP2-96FAC49786245691AE19`. Current Driver provenance includes previous author-side OAI7 scientific work; no independent Native mathematical review is claimed.
