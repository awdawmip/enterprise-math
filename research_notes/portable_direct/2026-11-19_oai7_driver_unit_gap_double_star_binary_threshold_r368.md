# OAI7 r368 — Exact coordinate threshold for unit-gap double-star samplers

Date: 2026-11-19. Driver-side **author research / internal proof audit**, building on r360, r365–r367. This proves a classification of an explicitly scoped combinatorial family. It does not assert an independent Native Result review or resolve the prime-29 OAI7 minimum-support problem.

## Exact statement

Let (p\ge4) and (G=\mathbb Z/p\mathbb Z). Consider positive rational samplers with (m\ge p-1) labeled ordered (d)-coordinate profiles, masses (n_x/N>0) where (n_x,N\in\mathbb Z_{>0}), (\sum n_x=N) and (\gcd(N,p)=1). Their supported atoms ((x,t)) have positive weights shared by all coordinates and output (t+w_{x,i}\in G) in coordinate (i). Assume:

1. The support size is exactly (S=m+p-1); exactly (p-1) profiles support two translations and all others support one.
2. Every coordinate marginal is exactly uniform on (G).
3. The (p-1) two-translation profiles have pairwise inequivalent ordered shapes under simultaneous translation.
4. The first-coordinate contracted residue tree is a genuine double star with central hubs (u,v=u+g), both with at least one attached leaf, and **the hub gap generates (G): (\gcd(g,p)=1)**.

**Theorem (existence classification).** A sampler satisfying these four conditions for some positive integer masses and some profiles exists **if and only if**
\[
\boxed{p\text{ is even and } d\ge 1+\lceil\log_2(p/2)\rceil.}
\]
For the existence direction it suffices to take exactly (m=p-1) profiles, with exactly two atoms per profile. Thus (S=2(p-1)=m+p-1). For odd (p), the obstruction extends r366 beyond primes to any cyclic modulus whose central hub gap is a generator. This statement concerns freely selected profiles/masses in the declared family; it does **not** assert compatibility with OAI7's *fixed* 350 prime-29 profiles or their fixed numerator vector.

## Necessity: one fixed leaf matching and a binary code

By the coprime first-coordinate incidence argument and the labeled-cut invariant of r360, the proof of r365 applies: after translating coordinate (i) by the central profile offset (\beta_i), the two hubs remain (u,v). A leaf connector originally based at (u) can either stay put or shift (+g); one based at (v) can either stay put or shift (-g). The leaf destinations in each coordinate form a permutation of (L=G\setminus\{u,v\}).

Since (g) generates (G), the step-(g) cycle on (G) becomes a **path with (p-2) vertices** after removing its adjacent hubs (u,v). Every permutation of (L) that sends a vertex to itself or a neighboring path vertex is a product of disjoint adjacent transpositions. A moving edge must exchange a leaf of hub type A (moving (+g)) with a leaf of type B (moving (-g)). Since types are fixed from the first coordinate, the union of possible moving edges over *all* coordinates is a fixed matching (\mathcal M) in this path (each A can be its left endpoint only, each B its right endpoint only).

Pairwise translation-inequivalence to the central connector means every leaf connector must move in **at least one** coordinate. Thus every leaf vertex belongs to (\mathcal M), making it a **perfect matching**. Consequently (p-2) must be even, hence (p) even. A path of even length has a unique perfect matching, comprising (r=(p-2)/2) edges. On each edge, both endpoint connectors move or both stay in coordinate (i), so the edge defines a common nonzero binary code of length (d-1). Codes on distinct edges must differ: otherwise the two A connectors, one on each edge, have exactly the same vector of relative offsets and therefore translation-equivalent shapes. Hence
\[
r\le 2^{d-1}-1\quad\Longleftrightarrow\quad d\ge1+\lceil\log_2(r+1)\rceil=1+\lceil\log_2(p/2)\rceil.
\]
This proves necessity, including for even composite (p).

## Sufficiency: compressed binary-code construction

Let (p=2r+2\ge4), (d=1+\lceil\log_2(r+1)\rceil), and select any (r) **distinct nonzero** binary codewords (b_j\in\{0,1\}^{d-1}), (j=1,\ldots,r). Set
\[
N=p(p-1)+1,\qquad q=\frac{p-1}{pN},\qquad Q=\frac{p+1}{2N}.
\]
Take (m=2r+1=p-1) profiles with ordered shapes
\[
W_C=(0,\ldots,0),\quad W_{A_j}=(0,b_j),\quad W_{B_j}=(0,-b_j)\pmod p.
\]
For (C) take translations (0,1), each of mass (Q). For (A_j), take translations (0,2j) with masses (q,1/p). For (B_j), take translations (1,2j+1) with masses (q,1/p).

The total profile masses are ((p+1)/N) for (C) and (p/N) for each (A_j,B_j), with integer numerators summing to (N), and (N\equiv1\pmod p). At coordinate 1 the leaf residues (2,3,\ldots,p-1) each have mass (1/p), while each hub receives (rq+Q=1/p). In coordinate (i\ge2), a pair with ((b_j)_{i-1}=1) exchanges its equal hub masses (q) between (0,1), and its equal leaf masses (1/p) between (2j,2j+1); a pair with bit 0 remains unchanged. Therefore all (d) marginals remain uniform. Every atom is positive, every profile has degree two, and (S=2(p-1)). The shapes are pairwise translation-inequivalent: the first entry is zero, codewords are nonzero and distinct, and (+1\not\equiv-1\pmod p) for (p\ge4). For larger (d) append zero coordinates.

The earlier r367 construction used **one-hot codewords** and (d=p/2); binary coding compresses the coordinate count to **(\Theta(\log p))**, and the matching argument proves that this compressed count is *sharp throughout the unit-gap double-star family*. For example (p=30) permits (d=5) rather than (15).

## Exact rational reproducibility

This checker verifies all declared conditions for **every even (p\in[4,150])**; the symbolic construction and matching proof, rather than the finite test, establish the unbounded theorem.

```python
from fractions import Fraction as F
from math import gcd

def verify(p):
    assert p>=4 and p%2==0
    r=(p-2)//2
    d=1+r.bit_length()   # 1 + ceil(log2(r+1))
    N=p*(p-1)+1
    assert gcd(N,p)==1
    q,Q=F(p-1,p*N),F(p+1,2*N)
    shapes=[(0,)*d]
    atoms=[(0,0,Q),(0,1,Q)]
    for j in range(1,r+1):
        b=tuple((j>>k)&1 for k in range(d-1))
        shapes.extend([(0,)+b,(0,)+tuple(-z for z in b)])
        atoms.extend([(2*j-1,0,q),(2*j-1,2*j,F(1,p)),
                      (2*j,1,q),(2*j,2*j+1,F(1,p))])
    assert len(shapes)==p-1 and len(atoms)==2*(p-1)
    assert len({tuple(z%p for z in w) for w in shapes})==p-1
    assert sum((z for x,t,z in atoms), F())==1
    for i in range(d):
        hist=[sum((z for x,t,z in atoms
                  if (t+shapes[x][i])%p==v),F()) for v in range(p)]
        assert hist==[F(1,p)]*p
    return p,d

assert [verify(p) for p in range(4,152,2)][-1]==(150,8)
print("r368 PASS: 74 even moduli, exact rational marginals")
```

## Provenance and status boundary

Original Task: RS-OAI7-028-C-20261007-6F2A81; immutable publication TP2-96FAC49786245691AE19; researcher EM-EMF6D046-5A2844. Driver-side predecessors: r360@0443ab938e4fac0af40d6b6c6f04fe8c3813bf6a, r365@1631f4f41483227841a7bd1bde95478073adbf0c, r366@7b10202fc6cf4e55a420c7791b961d7a8611b3e2, r367@43f66e0843e0ef369f8ae38c867e05ab36c8fc76. The source theorem is author-side, with neither frozen Native Result nor independent Native review; no Task/parent objective completion or original-owner reassignment is claimed. Prime-29 OAI7 remains outside the constructive even-modulus regime.
