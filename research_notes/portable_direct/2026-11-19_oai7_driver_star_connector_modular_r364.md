# OAI7 r364 — Modular signed-cut conservation and the mixed-gap star obstruction

Date: 2026-11-19. **Exact author-side combinatorial theorem** extending r360–r363. The original OAI7 research task, researcher and all prior contribution sources are preserved. This note is neither a Native Result nor an independent review.

## Setting and general modular incidence theorem

Let $p\ge3$ be an integer and $G=\mathbb Z/p\mathbb Z$. There are $m\ge p-1$ labeled profiles $x$, with integer numerators $n_x>0$, $N=\sum_x n_x$, and (\gcd(N,p)=1). Profile $x$ has an ordered $d$-coordinate shape (W_x=$w_{x,1},\dots,w_{x,d}$\in G^d). A positive-mass atom $(x,t)$ outputs $t+w_{x,i}$ at coordinate $i$, with the same weight $z_{x,t}>0$ at every coordinate; the profile total is $n_x/N$.

Assume the first coordinate is **exactly uniform**, the support has the sharp cardinality $S=m+p-1$, precisely $p-1$ profiles each support **two** atoms, and all other profiles support exactly one atom. Denote the $p-1$ connector profiles by $X_2$. By the coprime connectivity argument in r360, the first-coordinate bipartite incidence graph is a tree; deleting singleton-profile leaves and suppressing degree-two profiles gives a labeled tree $T$ on the $p$ residue vertices.

For each connector $x\in X_2$, orient its two first-coordinate residue endpoints as $a_x,b_x$ and denote its corresponding atoms by $e_{x,a},e_{x,b}$. Let $k_x\in\{1,\ldots,p-1\}$ be the number of residue vertices in the profile-side component after removing $e_{x,a}$ from the first-coordinate bipartite tree (equivalently, the $b_x$-side size of $T\setminus\{x\}$). Put (\delta_i$x$=w_{x,i}-w_{x,1}\in G).

**Theorem A $signed-cut modular conservation$.** If another coordinate $i$ is exactly uniform, then for every $v\in G$,
\[
\boxed{
\sum_{x\in X_2:\,b_x+\delta_i$x$=v} k_x
-
\sum_{x\in X_2:\,a_x+\delta_i$x$=v} k_x
\equiv1\pmod p .
}\tag{A}
\]
These are only $p$ integer congruences. They depend on the first-coordinate connector tree and the candidate shape offsets, but **not** on the actual numerator values except for the coprimality hypothesis. They can reject a proposed second-coordinate structure before tree connectivity, cut-signature sums or rational positivity are recomputed. Passing $A$ is necessary, not by itself sufficient.

**Proof.** For each edge $e$ of the first-coordinate bipartite tree, let (c$e$) be the number of residue vertices on the profile-side component of its edge deletion, and (s$e$) the sum of profile numerators there. The tree-flow identity of r360 is
\[
pN z_e=p\,s$e$-N\,c$e$.
\]
For a singleton profile $y$, (c$e$=0) and $pNz_e=pn_y\equiv0\pmod p$. For a degree-two connector $x$, the endpoint atoms have (c$e_{x,a}$=k_x) and (c$e_{x,b}$=p-k_x), hence
\[
pNz_{x,a}\equiv-Nk_x,\qquad
pNz_{x,b}\equiv+Nk_x\pmod p.
\]
If coordinate $i$ is uniform, the sum of $pNz_e$ over atoms landing at $v$ equals $N$ exactly. Taking this identity modulo $p$ and dividing by the invertible residue (N\in$\mathbb Z/p\mathbb Z$^\times) proves $A$. No independence, auxiliary ordering randomness, or second-coordinate tree premise was used. QED.

## Stronger mixed-gap exclusion: star connector skeleton

**Theorem B (star obstruction).** Under Theorem A, assume the first-coordinate connector tree $T$ is a **star** with common center residue $r\in G$. Equivalently, every degree-two connector $x$ links the center $a_x=r$ to a different leaf residue $b_x\ne r$, and the $p-1$ leaves exhaust $G\setminus\{r\}$.

If coordinate $i$ is exactly uniform, then
\[
\boxed{\delta_i$x$=\beta_i\quad\text{for every connector }x\in X_2}\tag{B}
\]
for some single $\beta_i\in G$. The actual center in the $i$-th coordinate is $r+\beta_i$.

**Proof.** For each star edge, $k_x=1$. Define (H_i$v$=\#\{x:r+\delta_i$x$=v\}) and (L_i$v$=\#\{x:b_x+\delta_i$x$=v\}). Equation $A$ gives
\[
D_i$v$:=L_i$v$-H_i$v$\equiv1\pmod p.
\]
There are exactly $p-1$ connectors, so (-$p-1$\le D_i$v$\le p-1). Therefore (D_i$v$\in\{1,1-p\}). Also (\sum_vD_i$v$=0), so **exactly one** residue $v_i$ has (D_i$v_i$=1-p), and all other residues have value (1). At $v_i$, the only possible nonnegative counts with (L_i$v_i$-H_i$v_i$=1-p) are (L_i$v_i$=0) and (H_i$v_i$=p-1). Thus every hub atom lands at the same $v_i$: (r+\delta_i$x$=v_i) for all connectors, establishing $B$. QED.

**Corollary $all-coordinate no-go without a common edge gap$.** If $d\ge2$, all $d$ coordinate marginals are exactly uniform, and the ordered shapes $W_x$ are pairwise inequivalent under common translation, then no such sharp-support, $p-1$-connector **star** law exists. Indeed $B$ in every coordinate makes every connector shape a common translate of any other, and $p-1\ge2$. The connector gaps $b_x-r$ in a star are generally **all different**, so this excludes a mixed-gap topology not covered by the fixed-step-cycle theorem r363. This theorem does not rule out non-star mixed-gap trees or degree-three-and-above profiles.

The proof works for composite $p$ as long as (\gcd(N,p)=1), unlike the prime-specific fixed-step-cycle argument.

## Exact finite illustration: p=5, N=17

Take nine profiles. Four connectors $x=0,1,2,3$ each have $n_x=1$, first-coordinate hub residue (0) with mass $3/85$, and leaf residue $x+1$ with mass $2/85$. Four singleton profiles $x=4,5,6,7$ each have $n_x=3$, their first-coordinate atom at residue $x-3$ with mass $15/85$. A final singleton $x=8$ has $n_x=1$, first-coordinate residue (0), mass $5/85$. Thus $N=4+12+1=17$, support is $4\cdot2+5=13=m+p-1$, and each residue has exactly mass $17/85=1/5$.

For second-coordinate relative connector shifts ((0,1,2,3)), keeping singleton shifts zero, the exact marginal becomes
\[
(10,20,20,20,15)/85,
\]
rather than ((17,17,17,17,17)/85). The theorem rules out **every** choice of singleton shifts repairing this mixed connector-shift assignment. For constant connector shifts, the modular obstruction vanishes; taking every profile shift equal gives a valid all-uniform second marginal.

The following Python 3 standard-library check tests all $5^4=625$ connector-shift choices against Theorem A's necessary congruences; exactly the five constant tuples survive. It also recomputes the rational example:

```python
from itertools import product
from fractions import Fraction as F

p, N = 5, 17
atoms = []
for x in range(4):
    atoms += [(x, 0, F(3, 85)), (x, x + 1, F(2, 85))]
for j in range(4):
    atoms.append((j + 4, j + 1, F(15, 85)))
atoms.append((8, 0, F(5, 85)))
assert len(atoms) == 13 and sum((z for x, a, z in atoms), F()) == 1

def marginal(shifts):
    offsets = tuple(shifts) + (0,) * 5
    return [sum((z for x, a, z in atoms
                 if (a + offsets[x]) % p == v), F())
            for v in range(p)]

assert marginal((0, 0, 0, 0)) == [F(1, 5)] * p
assert marginal((0, 1, 2, 3)) == [F(10, 85), F(20, 85),
                                  F(20, 85), F(20, 85), F(15, 85)]

survivors = []
for ds in product(range(p), repeat=p-1):
    signed = [0] * p
    for x, shift in enumerate(ds):
        signed[shift % p] -= 1
        signed[(x + 1 + shift) % p] += 1
    if all((d - 1) % p == 0 for d in signed):
        survivors.append(ds)
assert survivors == [(j,)*4 for j in range(5)]
print("r364 PASS: 625 modular cases, 5 constant-shift survivors")
```

## Research frontier and source provenance

For OAI7's exact (p=29,m=350,d=5,N=13,297,022,452), (N\bmod29=17), the already established sharp-support target is (S=378). Any candidate with 28 degree-two connector profiles must avoid **both** r363's fixed-gap cycle trees and r364's all-gaps star trees. For an arbitrary non-star connector tree, use (A) as a cheap modular sieve, followed by r360's full labeled cut-signature/strict-positivity test. Any profile of degree \(\ge3\) requires an appropriately generalized weighted-edge modular test.

Original researcher: EM-EMF6D046-5A2844. Task: RS-OAI7-028-C-20261007-6F2A81, immutable publication TP2-96FAC49786245691AE19. Reused author/Driver sources: r357@22bd6c41175866bc05595faf26ec7745f84b3b54, r360@0443ab938e4fac0af40d6b6c6f04fe8c3813bf6a, r362@56be4c9f0b13b12ab781fced72b2a8ca019d0756, and r363@d7cd8098c71e30220d6480a41f3d7b8322aa3ef6. The separate original external Gaussian-prime coverage-transfer source and its hypotheses are unchanged; this is a finite combinatorial model result only. No Source-authenticated Result, Native review, Researcher CLAIM, Task completion or parent objective closure is inferred.
