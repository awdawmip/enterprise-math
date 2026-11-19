# OAI7 r380 — Equal-arm cut saturation forces connector-shape coincidence

Date: 2026-11-19. RESEARCH_DRIVER shared-context author-side proof; follows r360 simultaneous labeled cut signatures, r379 odd-centroid obstruction and r378 star rigidity. Preserves original OAI7 researcher EM-EMF6D046-5A2844, Task RS-OAI7-028-C-20261007-6F2A81, immutable publication TP2-96FAC49786245691AE19, and Driver historical EM-DVR-DEBB5E. No independent Native Review has been performed on this theorem.

## Theorem

Let p>=3 be any integer (prime or composite), G=Z/pZ, m>=p-1. Let m positive rational-mass profiles have prescribed ordered coordinate shapes W_x in G^d; every atom (x,t) contributes positive mass to output t+w_(x,i) in coordinate i. Write profile masses n_x/N with positive integer n_x, sum n_x=N and gcd(N,p)=1. Assume all d coordinate marginals are exactly uniform, total number of positive atoms is S=m+p-1, and precisely p-1 profiles have two translations while the other profiles have one.

For each coordinate i, suppressing degree-two profile vertices in its atom/residue bipartite tree gives a labeled residue tree T_i on p vertices, by r360.

Suppose p=kr+1 for integers k>=2 and r>=1, and some T_i has **k distinct connector edges each splitting the residue set into parts of sizes r and p-r**.

Then there exist k distinct connector profiles x_1,...,x_k whose *specifically labeled atoms* at the larger-side ends of those edges all meet at one vertex in **every** coordinate tree. Accordingly their full ordered shape vectors are equivalent under common translation:
\[
\boxed{
  w_{x_a,j}-w_{x_a,i}=w_{x_b,j}-w_{x_b,i}
  \quad\text{for all }a,b\le k,\ \text{coordinates }j.
}
\]
In particular, if the connector profiles are pairwise inequivalent under common translation, such a sharp-support sampler is impossible.

The theorem excludes every **equal-arm centroid**: a residue tree with a center and k branches each containing exactly r=(p-1)/k vertices. It covers the odd-p degree-two centroid case k=2 (r379), the star k=p-1 (r378), and new k>=3 equal-arm topologies with nontrivial internal branching. It uses no primality assumption.

## Elementary cut-saturation lemma

Let T be any tree on p=kr+1 vertices with k>=2. Suppose it has k different edges whose smaller components contain r vertices.

Choose any centroid c of T (each component after deleting c has at most floor(p/2) vertices). Root T at c. Because r<p/2, the *r-vertex side* of every designated edge is necessarily its rooted descendant subtree: if it were the side containing c, the rooted descendant side would have size p-r>p/2, contradicting the centroid property already at the first edge leaving c in that direction.

Two distinct rooted subtrees having the same size r are either disjoint or identical; identical vertex sets have the same parent edge, so distinct designated edges give **disjoint** subtrees. Since their union has kr=p-1 vertices, the sole vertex outside their union is c. Each designated subtree attaches directly to c, and these k edges are all the edges at c; there are no other vertices or branches. Therefore T has a unique degree-k centroid c, with exactly k equally sized branches, and the *larger-side atom* of every designated connector is located at c.

Conversely, a degree-k centroid with k branches each of size r produces exactly k designated r:(p-r) edges. The graph characterization is an equivalence.

## Proof for simultaneous exact uniformity

For each designated connector profile x_a, choose its original labeled atom e_a adjacent to the centroid, i.e., to the larger-side endpoint of its r:(p-r) edge. Removing e_a from the expanded profile/residue tree leaves r residues in the profile-end component, so c_i(e_a)=r.

By r360, each labeled atom preserves its profile-side cut residue count c_j(e) in every exactly uniform coordinate j. Therefore each x_a remains an r:(p-r) connector, with e_a still attached to its larger-side endpoint. In each T_j the same k labeled edges have r-vertex smaller sides. The cut-saturation lemma makes all their larger endpoints coincide at the unique center c_j. In the original coordinate i they coincide at c_i. Hence
\[
w_{x_a,j}+t_a=c_j,\qquad w_{x_a,i}+t_a=c_i,
\]
and so each x_a satisfies w_(x_a,j)-w_(x_a,i)=c_j-c_i. The right side is independent of a. Thus the shapes x_1,...,x_k are all common translates of one another, contradicting pairwise inequivalence when applicable. QED.

The original profile-supply masses, shapes and positivity remain essential to r360; the new cut-saturation argument itself is purely finite-tree combinatorics.

## Prime-29 structural consequence

For OAI7 p=29 and sharp support S=378 with 350 pairwise translation-inequivalent ordered profiles and exactly 28 two-translation connector profiles, p-1=28 has the following divisors k>=2:

| Number of arms k | Vertices per arm r | Excluded centered tree |
|---:|---:|---|
| 2 | 14 | 14+14 balanced two-arm center (r379) |
| 4 | 7 | 7+7+7+7 equal arms |
| 7 | 4 | seven equal four-vertex arms |
| 14 | 2 | fourteen two-vertex arms |
| 28 | 1 | star (r378) |

Every one of these five graph families is excluded for degree-two-only sharp support. Surviving trees need not have unequal arm sizes at every possible vertex; only the exact saturated equal-arm configurations above are ruled out here. As before, other necessary conditions include centroid degree>=3 and diameter>=4; actual prescribed W_x offsets, all 350 n_x values, and r360 integer cut-sum/positivity are still required to test surviving candidates.

## Closed-form number of excluded labeled tree skeletons

The number of labeled trees on p=kr+1 vertices whose unique centroid has k unordered equal-size r-vertex arms is
\[
\boxed{E_{p,k}=p\,\frac{(p-1)!}{k!\,(r!)^k}\,r^{\,k(r-1)}.}
\]
Proof: choose center (p choices), partition remaining p-1 labeled vertices into k unordered blocks of size r ((p-1)!/[k!(r!)^k] choices), and choose a rooted labeled tree on each block (r^(r-2) times r attachment choices = r^(r-1), also 1 when r=1). Each resulting tree has the specified unique centroid, and its decomposition is unique.

For p=29, these five classes are disjoint because their centroid degrees k differ. Relative to all 29^27 labeled trees, the combined fraction is
\[
\frac{\sum_{k\in\{2,4,7,14,28\}} E_{29,k}}{29^{27}}
=0.12006176464221874\ldots .
\]
The 4-arm family by itself adds approximately 0.0000358271654897 of all labeled trees beyond r379. The fractions quantify **skeleton count pruning only**; they make no probability claim about feasible OAI7 distributions.

Exact integer computation (Python 3 standard library, no numerical solver):

~~~python
from math import factorial

def equal_arms_count(p,k):
    assert (p-1)%k == 0 and k>=2
    r=(p-1)//k
    return (p*factorial(p-1)//(factorial(k)*factorial(r)**k)
            * r**(k*(r-1)))

assert equal_arms_count(3,2)==3
assert equal_arms_count(5,2)==60
assert equal_arms_count(7,2)==5670
assert equal_arms_count(7,3)==7*factorial(6)//(factorial(3)*factorial(2)**3)*2**3
p=29
ks=(2,4,7,14,28)
counts={k:equal_arms_count(p,k) for k in ks}
assert counts[2]==366455334440454059511809592698024755200
assert counts[4]==109385156640804715005091176146126400
print("p29 excluded labeled skeletons", sum(counts.values()))
print("p29 excluded fraction", sum(counts.values())/p**(p-2))
~~~

## Preservation / next research branch

r360 pinned exact theorem:
https://github.com/awdawmip/enterprise-math/blob/0443ab938e4fac0af40d6b6c6f04fe8c3813bf6a/research_notes/portable_direct/2026-11-19_oai7_driver_simultaneous_cut_signature_rigidity_r360.md

r379 centroid theorem (checked/corrected final version):
https://github.com/awdawmip/enterprise-math/blob/8454f39e20db2e413dce5f6f6a20c8924f0c5020/research_notes/portable_direct/2026-11-19_oai7_driver_odd_centroid_two_branch_obstruction_r379.md

The next discriminating routes are centered *unequal-branch* trees under the full profile-numerator and coordinate-offset constraints, and support allocations with at least one three-or-more-translation profile. The support interval remains 378<=S_min<=490. This is a shared author-side theorem, not an independently reviewed/accepted Result, Source Activity linkage, new CLAIM, Task DONE or mother-objective completion.
