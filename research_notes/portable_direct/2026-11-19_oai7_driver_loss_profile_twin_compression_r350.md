# OAI7 r350 — Exact loss-profile twins reduce prime-29 minimax support to 350

Date: 2026-11-19. **Author-side exact finite theorem** and standalone exhaustive certificate; shared OAI7/r347–r349 Driver context, not an independent Native Result review.

## Theorem

Work in \(G=\mathbb F_{29}\), 5-element shifts \(C\), 4-element fixed tests \(K\), and
\[
b_K(C)=\mathbf1\{29-|K-C|>29^{3/4}\}=\mathbf1\{|K-C|\le16\}.
\]
Let \(Q\) be the 378 translation-class representatives in r349's positive r347 affine-orbit support
\(S=(1,2,5,6,7,11,23,25,30,37,47,50,114,115)\), using exactly r347's 0-based deterministic enumeration. Their full loss profiles \(\sigma(C)=(b_K(C))_{|K|=4}\) have **350 distinct values**: 28 pairs of identical profiles (14 pairs in each of affine orbits 1 and 2) and 322 singleton fibers. The 350 distinct binary profiles are \(\mathbb Q\)-linearly independent.

Merge the r349 probabilities of each twin pair onto one representative. The new **350-atom** law preserves every individual fixed-test failure probability and therefore retains the **exact minimax**
\[
\boxed{q^*=\frac{2024467747}{3324255613}}.
\]
Write \(D=474893659\). The probability mass of each twin's parent affine orbit is \(w_1=16479487/D\), \(w_2=17698031/D\). Two equal-probability atoms merge in each pair, so
\[
\boxed{H_{r349}-H_{r350}=w_1+w_2
=\frac{34177518}{474893659}\ {\rm bits}},\quad
\boxed{H_{r350}=7.869745624309653\ldots\ {\rm bits}}.
\]
The previous support counts were 10,962 in the affine-invariant r347 law and 378 in the translation-quotiented r349 law.

**Conditional entropy optimality.** Among laws supported on these *same 378 representatives* with the *same entire fixed-test failure-probability vector* as r349 (not merely the same maximum), the 350-atom law minimizes set entropy. To see this, write \(p_x=\Pr(\sigma(C)=x)\). The rank-350 matrix of distinct profile columns uniquely determines all \(p_x\) from their expected profile. The chain rule \(H(C)=H(\sigma(C))+H(C\mid\sigma(C))\ge H((p_x))\) gives the lower bound, attained by using one set per profile fiber.

## Exact coverage of the finite proof

For every \(t\), \(K-(C+t)=(K-C)-t\), so all 23,751 four-element tests reduce to 819 translation-distinct tests without changing any indicator. The following Python 3 standard-library verifier enumerates all 4,095 translation-distinct five-sets, all 819 test classes, the specified 378 support columns, their 28 duplicate pairs, and calculates exact rank 350 **over \(\mathbb F_2\)** by bitwise elimination. Thus a nonzero integer 350-minor exists, proving rank 350 over \(\mathbb Q\). Entropy decimals are used only for display; its exact improvement is the rational number above.

~~~python
from itertools import combinations
from collections import defaultdict
from math import log2
P=29; FULL=(1<<P)-1
def rot(m,s):
    s%=P
    return ((m<<s)|(m>>(P-s)))&FULL if s else m
def norm(m):return min(rot(m,t) for t in range(P))
def mul(m,a):return sum(1<<((a*x)%P) for x in range(P) if (m>>x)&1)
def representatives(k):
    return sorted({norm(sum(1<<x for x in s)) for s in combinations(range(P),k)})
def orbits(reps):
    where={m:i for i,m in enumerate(reps)}
    seen=set(); out=[]
    for m in reps:
        if m in seen:continue
        ids=sorted({where[norm(mul(m,a))] for a in range(1,P)})
        orb=[reps[i] for i in ids]
        assert all(q not in seen for q in orb)
        seen.update(orb);out.append(orb)
    assert len(seen)==len(reps)
    return out
def bad(k,c):
    union=0
    for e in range(P):
        if (c>>e)&1:union |= rot(k,-e)
    return union.bit_count()<=16
C=orbits(representatives(5)); K=orbits(representatives(4))
assert (len(C),len(K))==(150,33)
S=[1,2,5,6,7,11,23,25,30,37,47,50,114,115]
CS=[c for j in S for c in C[j]]
KS=[k for orb in K for k in orb]
assert (len(CS),len(KS))==(378,819)
sig=[sum(int(bad(k,c))<<i for i,k in enumerate(KS)) for c in CS]
g=defaultdict(list)
for idx,p in enumerate(sig):g[p].append(idx)
twins=[ids for ids in g.values() if len(ids)>1]
assert len(g)==350 and len(twins)==28
assert all(len(ids)==2 for ids in twins)
assert all(ids[0]<56 and ids[1]<56 for ids in twins)
assert sum(set(ids)<set(range(28)) for ids in twins)==14
assert sum(set(ids)<set(range(28,56)) for ids in twins)==14
basis={}
for i in range(len(KS)):
    bits=sum(((sig[j]>>i)&1)<<j for j in range(len(CS)))
    while bits:
        pivot=bits.bit_length()-1
        if pivot in basis:bits ^= basis[pivot]
        else:basis[pivot]=bits;break
assert len(basis)==350
pc={1:16479487,2:17698031,5:90390274,6:10843621,
    7:139525152,11:6049484,23:10138260,25:26578050,
    30:14514456,37:22809640,47:3118488,50:39221480,
    114:53586612,115:23940624}
D=474893659
oldH=-sum((a/D)*log2((a/D)/len(C[j])) for j,a in pc.items())
gain=(pc[1]+pc[2])/D
assert abs(oldH-7.941714405851122)<1e-12
assert abs(oldH-gain-7.869745624309653)<1e-12
print("r350 PASS: 28 twin pairs, 350 profiles, GF2 rank 350, H=",oldH-gain)
~~~

**Observed:** all exact finite assertions passed; H = 7.869745624309653 bits. In particular, the verification establishes that the two representatives in each paired fiber are indistinguishable by **all specified failure indicators**. This does not assert equality of their full union cardinality for every test or equality of future signed/provenance-bearing or native X6 trajectories. This is a scope-typed observer quotient, retaining any information needed for different future operations.

## Sources and contribution boundary

Pinned r347 exact primal/dual source: commit 12bd331ea2aef70cc844682db432a623b235e726, file research_notes/portable_direct/2026-11-19_oai7_driver_exact_affine_minimax_prime29_r347.md. r348 rigidity: f41c2690daba467ecbde99615a1337e67be46ffd. r349 translation-quotient proof: eac1b9044c3b76648b6d352c50ec243650b1bec9. Original OAI7 scientist EM-EMF6D046-5A2844, Task RS-OAI7-028-C-20261007-6F2A81 and immutable publication TP2-96FAC49786245691AE19 remain credited. This finite external-model lemma grants no CLAIM, Native review, Source/Activity event, Task completion or parent closure.