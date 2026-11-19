# OAI7 r357 — Sharp 378-row exact minimax sampler with one uniform ordered coordinate

Date: 2026-11-19. New finite, exact, constructive research increment in the same OAI7 / RESEARCH_DRIVER scientific line; preserves all original author contributions and independent-Review status.

## Result and scope

Let \(G=\mathbb F_{29}\); \(H=(H_1,\ldots,H_5)\) has five distinct coordinates, \(C=\{H_i\}\), and for each deterministic four-set \(K\subset G\) define \(b_K(C)=\mathbf1\{|K-C|\le16\}\). The established exact minimax value is

\[
v=\frac{2024467747}{3324255613}.
\]

Using the exact 350 positive complete-loss-profile masses \(p_x\) fixed by r351–r352, there exists an **explicit rational ordered sampler** such that

\[
\boxed{q(H)=v,\quad H_1\sim\mathrm{Unif}(\mathbb F_{29}),\quad
 |\operatorname{supp}(H)|=378.}
\]

By the modular connectivity theorem r356, **378 is the exact minimum possible support** among all exact-minimax ordered laws with **the first coordinate uniformly distributed**. In particular,

\[
\boxed{\min_{\substack{q(H)=v\\H_1\mathrm{\ uniform}}}
|\operatorname{supp}(H)|=378.}
\]

For the concrete 350-fiber assignment and allocation order certified below, the joint entropy is the following exact finite expression:

\[
H(H)=-\sum_{(x,a,z)\in\mathcal A}z\log_2 z
=7.87234801890010571075605169525823734\ldots\ \mathrm{bits},
\]
where every weight \(z\) in the displayed algorithm is an **exact rational number**. The 378-row construction's entropy is only \(0.00260239459045282317\ldots\) bits above the universal complete-profile entropy lower bound \(H_{350}=7.86974562430965288758638198708\ldots\).

**Constraint distinction:** r357 proves exact optimal support and a low-entropy explicit construction when **one specified position** is uniform. The existing r353 490-row existence theorem covers **all five** uniform positions simultaneously and remains the current constructive-existence bound for that stricter model. Do not substitute this one-coordinate construction for an all-five-coordinate sampler.

## General exact transport theorem

Let \(X\) have \(m\) positive rational masses \(p_x\in N^{-1}\mathbb Z\), summing to 1, and let \(a\) range over \(p\) target labels. For each fiber \(x\), assume there is at least one allowed distinct output \(h_{x,a}\) with first coordinate \(a\), and outputs from different pairs \((x,a)\) are pairwise distinct and allow recovery of \(X\). Assign the masses \(p_x\) to source rows of a two-way transportation table and the target masses \(1/p\) to its columns. The standard *north-west corner* construction fills each positive cell with the minimum of the remaining row and column capacities.

Because all supplies and demands are rational, every occupied weight is exactly rational. Its positive-cell support is at most \(m+p-1\), and the output's first coordinate is uniformly distributed while \(X\)'s distribution is preserved. If \(\gcd(N,p)=1\), **every proper nonempty cumulative row sum** lies in \(N^{-1}\mathbb Z\) and cannot equal a proper nonempty cumulative column sum \(j/p\). Thus the procedure has no interior simultaneous row/column exhaustion and exactly \(m+p-1\) positive cells. Combined with r356's universal lower bound, this proves optimal support in this group-transport model.

For OAI7, let \(W_x\) be one r350 representative set for each of the 350 complete loss profiles, all chosen from pairwise translation-inequivalent classes. Fix a deterministic ordered tuple \(w_{x,1},\ldots,w_{x,5}\) for each representative. From an occupied transportation cell \((x,a)\) output

\[
H_i=w_{x,i}+a-w_{x,1}\pmod {29},\qquad i=1,\ldots,5.
\]

The first coordinate is exactly \(a\), the five coordinates remain distinct, and the result's complete loss profile is \(x\); the label and translation can be recovered from the output. The event \(b_K(C)\) is invariant under translating the whole codeword, so preserving each \(p_x\) preserves **every** individual fixed-test failure probability from r351, not merely its maximum. The support equals the number of positive transportation cells.

The masses are \(p_x=a_j/(Dt_j)\) for singleton translation classes, and \(2a_j/(28D)\) for each of the 14 twin fibers in affine orbits \(j=1,2\). Here \(D=474893659\), \(t_j=14\) for \(j=6\) and \(t_j=28\) otherwise, and \(a_j\) are the exact r347 orbit numerators. With \(N=28D=13297022452\), \(\gcd(N,29)=1\). The supplied 350-family order below specifies a particular exact NW allocation; within each family use the canonical r350 representative enumeration.

## Complete reproducible rational certificate (Python 3 standard library)

The following program verifies the prescribed family multiplicities, all 350 exact profile row masses, 29 exact target column masses, coprimality, exactly 378 positive cells and that exactly 28 fibers split into two cells (322 fibers remain unsplit). It computes the exact entropy expression from rational weights and uses high-precision decimal logarithms only for its displayed decimal approximation. The independent r351/r352 finite rank/dual certificates establish that these profile masses attain \(q=v\).

~~~python
from fractions import Fraction as F
from collections import Counter
from math import gcd, log2
D=474893659
a={
1:16479487,2:17698031,5:90390274,6:10843621,
7:139525152,11:6049484,23:10138260,25:26578050,
30:14514456,37:22809640,47:3118488,50:39221480,
114:53586612,115:23940624
}
N=28*D
assert N==13297022452 and N%29==17 and gcd(N,29)==1

ORDER = """
7,1,7,37,30,47,6,47,11,50,37,23,47,30,5,1,50,2,25,30,7,2,115,11,6,114,50,2,23,37,11,11,25,5,1,6,1,6,30,37,25,1,114,47,5,25,7,37,115,50,25,6,30,50,47,114,50,47,23,7,25,2,2,23,47,25,23,11,115,37,7,1,47,25,114,30,11,25,11,1,115,47,30,30,6,47,114,7,25,47,7,50,11,25,23,23,25,47,11,23,5,50,115,25,2,5,11,115,115,47,50,5,47,1,115,23,5,37,37,30,5,30,23,114,23,11,114,115,115,23,50,5,11,2,5,11,7,5,30,7,23,30,50,23,11,11,115,25,1,114,47,7,30,23,7,47,37,5,7,5,37,5,47,25,2,47,5,7,7,37,114,1,23,11,5,115,7,25,114,6,2,1,23,11,25,30,114,114,47,37,6,23,5,114,115,37,7,50,30,7,6,6,1,25,115,5,23,30,114,47,30,115,23,7,37,25,115,11,1,37,11,37,5,25,5,37,5,50,23,50,115,30,7,30,47,2,115,115,7,6,7,2,114,1,23,7,47,37,2,5,25,50,11,114,5,25,5,37,30,23,114,37,11,50,114,23,114,50,2,114,6,6,11,11,114,114,50,50,47,50,37,114,115,2,37,37,37,30,115,115,7,23,7,50,11,114,37,115,30,5,5,114,50,115,11,50,115,25,25,23,114,11,30,5,30,50,5,7,47,115,23,30,47,25,37,47,115,11,30,25,23,50,47,114,6,25,11,50,115,50,30,47,30,25,7,37,114,50,37,7
"""
order=[int(v) for v in ORDER.split(',')]
assert len(order)==350 and sum(a.values())==D
assert Counter(order)==Counter({j:(14 if j in (1,2,6) else 28) for j in a})
numerators=[a[j]*(2 if j in (1,2,6) else 1) for j in order]
assert sum(numerators)==N
supplies=[F(k,N) for k in numerators]
target=[F(1,29) for _ in range(29)]
assert all(v>0 for v in supplies)
allocation=[]
column=0
capacity=target[0]
for x,mass in enumerate(supplies):
    left=mass
    while left:
        z=min(left,capacity)
        assert z>0
        allocation.append((x,column,z))
        left-=z
        capacity-=z
        if not capacity:
            column+=1
            if column<29:
                capacity=target[column]
assert column==29 and len(allocation)==378
assert all(sum((z for xx,aa,z in allocation if xx==x),F())==supplies[x]
           for x in range(350))
assert all(sum((z for xx,aa,z in allocation if aa==col),F())==F(1,29)
           for col in range(29))
row_counts=Counter(x for x,aa,z in allocation)
assert Counter(row_counts.values())=={1:322,2:28}
H=-sum(float(z)*log2(float(z)) for x,aa,z in allocation)
assert abs(H-7.87234801890010571)<1e-12
print("r357 PASS: 350 fibers, 29 uniform first-coordinate values,"
      " 378 exact rational rows, entropy =", H, "bits")
~~~

The exact arithmetic determines the distribution; evaluating real logarithms does not affect support, uniformity or minimax validity. Independent decimal evaluation at 65-digit precision gave \(7.87234801890010571075605169525823734112980226776995921652\) bits, from the same rational allocation.

## Scientific interpretation, provenance, next experiment

This separates two notions of marginal constraints:
1. **One exact uniform position:** sharp support 378, now constructively attained, with entropy about 7.87235 bits.
2. **All five exact uniform positions:** r353 gives a rational vertex with at most 490 rows, and r356 gives the universal support lower bound 378. Exact minimum support and exact entropy minimum remain unresolved.

An especially useful next computational objective is to extract and authenticate a sparse, exact rational *five-coordinate*-uniform vertex from r353's 495-equation polytope, reusing its full profile-mass theorem and keeping all constraint checks exact.

Original OAI7 task: RS-OAI7-028-C-20261007-6F2A81, immutable TP2-96FAC49786245691AE19, researcher EM-EMF6D046-5A2844. Shared author-side Driver construction is not an independent Native Result Review or Activity association.

Pinned sources: [r351](https://github.com/awdawmip/enterprise-math/blob/10ac54cc216860ddfd0ce62fe82b229318482573/research_notes/portable_direct/2026-11-19_oai7_driver_global_entropy_minimizer_r351.md); [r352](https://github.com/awdawmip/enterprise-math/blob/c660dc487bbb5f96789a3b2876ed82c32245eecf/research_notes/portable_direct/2026-11-19_oai7_driver_all_minimax_laws_entropy_interval_r352.md); [r353](https://github.com/awdawmip/enterprise-math/blob/b9890c5cccd0a2e0176a19759b850bf997ecd8b3/research_notes/portable_direct/2026-11-19_oai7_driver_sparse_uniform_marginal_exact_existence_r353.md); [r356](https://github.com/awdawmip/enterprise-math/blob/b8d5997425d3a86110f9e2463b3e87b3e24b601a/research_notes/portable_direct/2026-11-19_oai7_driver_modular_uniform_support_gap_r356.md).
