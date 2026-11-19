# OAI7 r365 — Five-marginal double-star classification at 378-atom support

Date: 2026-11-19. Exact mathematical derivation and a complete 4-bit classification. This note continues the original OAI7 author-side structural investigation (r360, r363, r364). It retains the original researcher and is not an independent Native Result review.

## The double-star topology

Let \(p\ge5\), \(d\ge2\), and let the rational profile masses \(n_x/N\) satisfy \(n_x>0\), \(\gcd(N,p)=1\). Each positive atom \((x,t)\) has identical weight at all \(d\) output coordinates, with \(i\)-th residue \(t+w_{x,i}\pmod p\). Assume exactly \(S=m+p-1\) positive atoms, with \(p-1\) profiles of support degree two, all other profiles of degree one, and exact uniformity of every coordinate marginal.

Let \(T_1\) be the contracted first-coordinate residue tree (r360). Suppose \(T_1\) is a **double star**: two hubs \(u\ne v\) connected by one distinguished connector profile \(x_0\), with \(a\ge1\) connector leaves attached to \(u\) and \(b\ge1\) attached to \(v\). Thus \(a+b=p-2\). Denote these leaf-connector profile sets \(A,B\). Put \(g=v-u\ne0\) and \(\beta_i=w_{x_0,i}-w_{x_0,1}\).

Assume all \(p-1\) connector ordered shapes are inequivalent under common translation. (In the OAI7 application all \(m=350\) base shapes have this property.)

### Theorem 1: each coordinate has the same double-star core

For every coordinate \(i\), its contracted residue tree \(T_i\) is again a double star, whose two hubs are
\[
u_i=u+\beta_i,\qquad v_i=v+\beta_i.
\]

Each leaf connector \(x\in A\) has
\[
\boxed{\delta_i(x)-\beta_i\in\{0,g\}},\qquad
\delta_i(x)=w_{x,i}-w_{x,1},
\]
and each leaf connector \(y\in B\) has
\[
\boxed{\delta_i(y)-\beta_i\in\{0,-g\}}.
\]

For each \(i\ge2\), let \(s_A(i)\) count the \(A\)-connectors choosing \(+g\), i.e. switching from the \(u\)-hub to the \(v\)-hub; let \(s_B(i)\) count the \(B\)-connectors choosing \(-g\), switching from \(v\) to \(u\). Then
\[
\boxed{s_A(i)=s_B(i)\quad(i=2,\ldots,d).}\tag{1}
\]

**Proof.** For each leaf connector \(x\), label the atom at the original hub as \(e_{x,h}\). Deleting that atom from \(T_1\)'s expanded bipartite incidence tree leaves exactly one residue on the profile side, so \(c_1(e_{x,h})=1\). By r360's simultaneous labeled-cut theorem \(c_i(e_{x,h})=1\) in every uniform coordinate. Hence the other residue of the same connector must be a leaf of \(T_i\)'s contracted residue tree. The \(p-2\) leaf connectors have distinct leaf residues. The distinguished central connector \(x_0\) cannot touch any such leaf; its two distinct endpoints must therefore be the remaining two residues. Its atoms both shift by \(\beta_i\), so these endpoints are \(u_i\) and \(v_i\). Every other connector's original hub atom must land at one of these two residues, yielding the displayed two choices. At this stage one of the two core vertices could in principle have no attached leaves; the central-edge cut equality below excludes this degeneracy.

Delete the distinguished central atom attached at \(u\). In \(T_1\), its profile-side component contains \(v\) and its \(b\) leaf residues, so the cut residue count is \(b+1\). In \(T_i\), the corresponding component has \(b-s_B(i)+s_A(i)+1\) residues. Equality of labeled cut counts gives (1). Hence the numbers of attached leaves stay exactly \(a\) and \(b\) at the corresponding hubs, both positive, so \(T_i\) is indeed a genuine double star. QED.

### Theorem 2: exact bit-pattern capacity

For \(i=2,\ldots,d\), encode the choice of each leaf connector in \(A\) as the bit \(0\) for offset \(\beta_i\), \(1\) for \(\beta_i+g\), and similarly encode \(B\) with \(0\) for \(\beta_i\), \(1\) for \(\beta_i-g\). Each leaf connector is therefore labeled by a \((d-1)\)-bit vector.

Within each hub group these vectors are distinct: equal vectors give equal relative ordered shape offsets, hence translation-equivalent shapes. The zero vector is also forbidden, since it would make the leaf connector's shape translation-equivalent to the central connector \(x_0\). Consequently
\[
\boxed{a,b\le 2^{d-1}-1,\quad p-2=a+b\le2^d-2.}\tag{2}
\]
In particular, for any \(p>2^d\), a sharp-support double-star topology with pairwise translation-inequivalent connector shapes cannot have all \(d\) marginals uniform.

The column-balance equations (1) mean that the sums of the chosen bit vectors in groups \(A\) and \(B\) are equal **coordinate by coordinate over the ordinary integers**, not merely modulo two.

### OAI7 corollary: 29 residues, five positions, 28 connectors

In the exact \(p=29,d=5,S=378,m=350,N=13{,}297{,}022{,}452\) five-marginal problem, \(a+b=27\) and the available nonzero patterns are the 15 elements of \(\{0,1\}^4\setminus\{0000\}\). By (2), the only *a priori* group-size pairs are
\[
(a,b)\in\{(12,15),(13,14),(14,13),(15,12)\}.
\]
But **\((12,15)\) and \((15,12)\) are impossible**. Indeed, a group with 15 connectors must use all 15 nonzero patterns, whose four bit-column sums are each 8. For a group with 12 distinct nonzero patterns to have the same four column sums, its three omitted patterns would have to contribute zero in all four columns, which is impossible.

Therefore any feasible OAI7 sharp-support double-star has
\[
\boxed{\{a,b\}=\{13,14\}.}\tag{3}
\]

Moreover, consider orientation \((a,b)=(13,14)\). Group \(A\) omits exactly two nonzero patterns \(\alpha,\beta\) from the complete 15-pattern set, and group \(B\) omits exactly one nonzero pattern \(\gamma\). Their equal four column sums hold **if and only if**
\[
\boxed{\alpha+\beta=\gamma\quad\text{in }\mathbb Z^4.}\tag{4}
\]
Thus the nonzero supports of \(\alpha,\beta\) are disjoint and partition the support of \(\gamma\). For a \(\gamma\) with Hamming weight \(k\ge2\), there are \(2^{k-1}-1\) unordered partitions into two nonempty supports. The number of possible bit-pattern set pairs is exactly
\[
\boxed{\sum_{k=2}^4 {4\choose k}(2^{k-1}-1)
=6+12+7=25.}\tag{5}
\]
The reverse orientation \((14,13)\) contributes 25 more, for exactly **50** possible oriented bit-pattern membership pairs at the purely structural level. Assignment of particular OAI7 profiles, masses, first-coordinate leaf residues and strict rational cut-flow constraints remains separate.

This excludes all unbalanced double-star split sizes, beyond the fixed-step cyclic and star obstructions r363–r364. It does **not** settle whether any of the 50 structural patterns has a fully feasible rational OAI7 instance.

## Complete finite check (Python 3, no external dependencies)

The checker enumerates all possible subsets of the 15 nonzero 4-bit patterns for the admissible group sizes, tests integer column balance, and reproduces both (3) and (5):

~~~python
from itertools import combinations
from math import comb

universe = tuple(range(1, 16))
def colsum(subset):
    return tuple(sum((mask >> j) & 1 for mask in subset) for j in range(4))

counts = {}
for a in range(12, 16):
    b = 27 - a
    count = 0
    for A in combinations(universe, a):
        target = colsum(A)
        for B in combinations(universe, b):
            if colsum(B) == target:
                count += 1
    counts[(a, b)] = count

assert counts == {(12,15):0, (13,14):25, (14,13):25, (15,12):0}
assert sum(counts.values()) == 50
assert sum(comb(4,k) * (2**(k-1)-1) for k in range(2,5)) == 25
print("r365 PASS", counts)
~~~

## Precise next frontier and authorship

The next high-value test is to bind the 50 bit-pattern membership classes to **actual OAI7 profile labels and numerator masses**, then test r360 labeled cut sums and strict positivity. The 50 patterns are support-pattern classes, not 50 feasible samplers; the remaining \(378\le S_{\min}\le490\) gap stays open. This note also gives a fully proved family-level no-go \(p>2^d\) for sharp-support double stars with translation-inequivalent connector shapes.

Original researcher: EM-EMF6D046-5A2844. Original Task RS-OAI7-028-C-20261007-6F2A81, publication TP2-96FAC49786245691AE19. Reused mathematical sources: r360@0443ab938e4fac0af40d6b6c6f04fe8c3813bf6a (tree-cut invariant), r363@d7cd8098c71e30220d6480a41f3d7b8322aa3ef6 (fixed-step cycle), r364@32e1e182a90d57a9f3eae6c8e461d2b61b96a689 (modular signed-cut and star). The original external coverage-transfer source and its source hypotheses remain unchanged. This is a verified finite/combinatorial author-side increment, not Native Result acceptance, independent review, claimant ownership, or parent-objective completion.
