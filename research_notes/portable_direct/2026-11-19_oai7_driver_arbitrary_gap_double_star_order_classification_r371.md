# OAI7 r371 — Arbitrary hub-gap double stars: exact order criterion and entropy-preserving construction

Date: 2026-11-19. Driver-side author research and internal proof check. This extends the **unit-generator hub-gap** double-star classification of r368 to **every nonzero hub gap** in a finite cyclic group, without changing the fixed prime-29 OAI7 target. Mathematical authorship here is shared-context Driver-side derivation, not a new independent Native review. Original task researcher: EM-EMF6D046-5A2844; task RS-OAI7-028-C-20261007-6F2A81, publication TP2-96FAC49786245691AE19.

## Theorem: exact classification for a prescribed gap

Let \(p\ge4\), \(G=\mathbb Z/p\mathbb Z\), and fix \(g\in G\setminus\{0\}\). Write \(\ell=\operatorname{ord}_G(g)=p/\gcd(p,g)\). Consider the precise r365/r368 *sharp-support double-star* class: \(m\ge p-1\) pairwise translated-shape-distinct connector profiles have \(p-1\) degree-two translation supports and all other profiles have degree one, with exactly \(S=m+p-1\) positive atoms; all \(d\) ordered output coordinates have uniform \(G\)-marginals; positive profile masses are integer numerators over a common \(N\) coprime to \(p\); the first-coordinate contracted tree is a double star with hubs \(u\) and \(v=u+g\), both bearing leaves; the \(p-1\) degree-two connector shapes are pairwise translation-inequivalent, including the central connector. No primality or generator assumption is made.

Then this family is nonempty **if and only if**
\[
\boxed{\ell\text{ is even and }\ell\ge4,\qquad
       d\ge1+\lceil\log_2(p/2)\rceil.}
\]
Equivalently, \(p\) is even, the specified gap has additive order divisible by two but not equal to two, and the displayed coordinate threshold holds. For sufficiency one may take \(m=p-1\), exactly \(2(p-1)\) atoms, and rational masses; the minimum \(d\) is attained.

In particular, for **every odd** \(p\), *no* sharp-support double star satisfies these hypotheses, regardless of whether the gap generates \(G\). For \(p=8\), a non-generator gap \(g=2\), of order \(4\), already achieves \(d=3\).

## Necessity

Use the labeled-cut theorem r360 and double-star coordinate theorem r365. Translate all residues in coordinate \(i\) by the central connector's offset. The central hubs stay at \(0,g\), and every original hub-\(0\) leaf connector A either stays or shifts **+\(g\)**, while every original hub-\(g\) leaf connector B either stays or shifts **-\(g\)**. The distinct leaf residues must permute \(L=G\setminus\{0,g\}\). Relative to the central profile, their coordinate shape vectors are therefore \(g b_A\) for A and \(-g b_B\) for B, with \(b\in\{0,1\}^{d-1}\), and **no leaf may have the zero bit-vector**.

The additive-\(g\) orbits in \(G\) are cycles of length \(\ell\). The orbit containing hubs \(0,g\) becomes a path with \(\ell-2\) remaining vertices. A permutation on a path using only allowed directions \(+\!g\) for A and \(-\!g\) for B is a union of disjoint adjacent A/B transpositions and fixed points. A leaf can move only to its **unique directed partner** (A at \(x\) with B at \(x+g\)), so the union over all coordinates of movable path edges is one fixed matching. Every leaf must move at least once to differ from the central shape. This path must therefore admit a perfect matching, requiring \(\ell-2\) even, i.e. **\(\ell\) even**.

If \(\ell=2\), the hub orbit has no leaves and \(p\ge4\) leaves occur in other 2-cycles. In any such 2-cycle the only nonidentity leaf permutation swaps its two vertices; both connector profiles thus have the same movement bit-vector, and since \(g=-g\) modulo \(p\), they have identical relative ordered shapes. If neither moves, both have the central shape. Thus \(\ell=2\) contradicts shape distinctness.

Assume now \(\ell\ge4\) even. On any other \(g\)-orbit, a leaf permutation using A moves \(+\!g\), B moves \(-\!g\), or fixed points consists of disjoint adjacent A/B transpositions, **except** for a complete one-direction rotation of a cycle whose vertices are all A (or all B). In an all-A/all-B cycle, a nonidentity permutation moves every vertex together in that coordinate, so all \(\ell\ge4\) connectors in that cycle acquire identical bit-vectors, violating shape distinctness. Hence only the fixed A/B matching mechanism remains. Every leaf must be covered by this matching; altogether there are
\(r=(p-2)/2\) disjoint A/B pairs.

Within a pair, the two leaves move together in every coordinate (otherwise the residue map is not bijective), yielding one **nonzero** binary word \(b_j\in\{0,1\}^{d-1}\). The A connectors of distinct pairs have the same hub and shifts \(g b_j\), so equal words would give translation-equivalent shapes. All \(r\) words must therefore be distinct and nonzero:
\[
r\le2^{d-1}-1
\quad\Longleftrightarrow\quad
d\ge1+\lceil\log_2(p/2)\rceil.
\]
This proves both necessary conditions without assuming \(g\) is a generator.

## Construction, all admissible gaps

Suppose \(\ell\) is even and at least \(4\). Decompose \(G\) into cycles of addition by \(g\). Remove the hubs \(0,g\) from their common cycle and pair the remaining even-length path in consecutive \(g\)-edges. On each other even-length cycle, take any alternating perfect matching in \(g\)-edges. These give exactly \(r=(p-2)/2\) disjoint oriented pairs \((x_j,y_j=x_j+g)\) covering all leaves.

Let \(d=1+\lceil\log_2(r+1)\rceil\), and select \(r\) distinct nonzero binary words \(b_j\in\{0,1\}^{d-1}\). Take:
- central profile \(C=(0,\ldots,0)\), translations \(0,g\);
- profile \(A_j=(0,g b_j)\), translations \(0,x_j\);
- profile \(B_j=(0,-g b_j)\), translations \(g,y_j\).

For any integer \(M\ge1\) put \(N=pM-1\), \(q=1/(pN)\), \(Q=(2M-1)/(2N)\). Assign weight \(Q\) to both central atoms, and weights \(q,1/p\) to the A and B atoms in translation order. Profile numerators are \(2M-1,M,\ldots,M\) over \(N\); these sum to \(N\) and \(\gcd(N,p)=1\).

The first-coordinate distribution has \(1/p\) at every leaf and at both hubs because \(Q+r q=1/p\). Whenever a code bit is 1, its A/B pair exchanges **equal** hub weights \(q\) and **equal** leaf weights \(1/p\), leaving the next coordinate exactly uniform. All profiles are inequivalent: distinct words separate A–A and B–B, nonzero words separate the center, and \(g\not\equiv-g\pmod p\) (since \(\ell\ge4\)) separates A–B. The full ordered outputs distinguish all \(2(p-1)\) supported atoms.

The same entropy argument as r370 is valid for every admissible gap, with \(r=(p-2)/2\) and \(\delta=r/(pM-1)\):
\[
\boxed{H(Y)=\log_2p+\frac2p[h_2(\delta)+\delta\log_2r].}
\]
For each fixed admissible \(p,g,d\), the infimum is \(\log_2p\) as \(M\to\infty\), not attained by strictly positive weights.

## Exact rational verification

A separate exact-fraction checker constructed all allowed gaps for every integer \(4\le p<70\): **764** admissible \((p,g)\) pairs. It verified all shape-inequivalence conditions, full-output atom injectivity, positive weights, correct support count, and every marginal as exactly \(1/p\). Examples: \((p,g,\ell,d)=(8,2,4,3),(12,3,4,4),(12,2,6,4)\). The constructive proof establishes the unrestricted claim; the finite checks audit its implementation.

Reproduction (Python 3 standard library, using exact rational arithmetic):

~~~python
from fractions import Fraction as F
from math import gcd,ceil,log2
def check(p,g,M=1):
    ell=p//gcd(p,g)
    assert p>=4 and 0<g<p and ell>=4 and ell%2==0
    seen=set();pairs=[]
    for s in range(p):
        if s in seen: continue
        cycle=[];t=s
        while t not in seen:
            seen.add(t);cycle.append(t);t=(t+g)%p
        if 0 in cycle:
            assert g in cycle
            path=[(k*g)%p for k in range(2,ell)]
            pairs += [(path[i],path[i+1]) for i in range(0,len(path),2)]
        else:
            pairs += [(cycle[i],cycle[i+1]) for i in range(0,len(cycle),2)]
    r=(p-2)//2;assert len(pairs)==r
    d=1+ceil(log2(r+1));N=p*M-1;q=F(1,p*N);Q=F(2*M-1,2*N)
    shapes=[(0,)*d];atoms=[(0,0,Q),(0,g,Q)]
    for j,(x,y) in enumerate(pairs,1):
        assert y==(x+g)%p
        b=[(j>>k)&1 for k in range(d-1)]
        shapes += [(0,)+tuple(a*g for a in b),
                   (0,)+tuple(-a*g for a in b)]
        atoms += [(2*j-1,0,q),(2*j-1,x,F(1,p)),
                  (2*j,g,q),(2*j,y,F(1,p))]
    assert len(set(tuple(a%p for a in w) for w in shapes))==p-1
    assert len(atoms)==2*(p-1) and sum((z for _,_,z in atoms),F())==1
    Ys=[tuple((t+a)%p for a in shapes[x]) for x,t,_ in atoms]
    assert len(set(Ys))==len(Ys)
    for i in range(d):
        hist=[sum((z for (_,_,z),Y in zip(atoms,Ys) if Y[i]==v),F())
              for v in range(p)]
        assert hist==[F(1,p)]*p
    return d
hits=0
for p in range(4,70):
    for g in range(1,p):
        ell=p//gcd(p,g)
        if ell>=4 and ell%2==0:
            check(p,g);hits+=1
assert hits==764
print("r371 PASS: 764 admissible (p,g) pairs")
~~~

## Contribution, references, remaining target

This note directly reuses the **labeled-cut and center-shift theorems** of r360 and r365, and r368's binary profile mechanism. Its new content is the orbit-by-orbit necessity argument for arbitrary non-generator hub gaps, the exact additive-order criterion, and the verified construction over all admissible \(g\). Relevant immutable source:
- r365: https://github.com/awdawmip/enterprise-math/blob/1631f4f41483227841a7bd1bde95478073adbf0c/research_notes/portable_direct/2026-11-19_oai7_driver_double_star_bit_balance_r365.md
- r368: https://github.com/awdawmip/enterprise-math/blob/6f8f6b04bcee2c628accc73a2cc3bf297327ff2d/research_notes/portable_direct/2026-11-19_oai7_driver_unit_gap_double_star_binary_threshold_r368.md
- r370: https://github.com/awdawmip/enterprise-math/blob/101ceab74397de50abf5ac0c66de8c201d8aa79c/research_notes/portable_direct/2026-11-19_oai7_driver_even_modulus_fixed_p_entropy_infimum_r370.md

For original OAI7, \(p=29\) has no qualifying gap; the fixed-profile \(378\le S_{\min}\le490\) problem remains open. This is an independently testable **author-side subunit**, not a frozen Result, source Activity link, independent Native review, Task completion or parent completion.
