# OAI7 r351 — Global prime-29 loss-observer fibers and test-functional rank

2026-11-19. Author-side exact finite theorem; shares the prior OAI7/r347–r350 Driver mathematical context, not an independent Native review.

## Theorem A: full observer-equivalence classification

Let G=F_29. For a 5-element shift set C and a 4-element test set K, define
\[
b_K(C)=\mathbf 1\{29-|K-C|>29^{3/4}\}=\mathbf1\{|K-C|\le16\}.
\]
Translation of either C or K leaves this indicator unchanged. There are exactly 4095 translation classes of 5-sets and 819 translation classes of 4-sets. For each 5-set class, form its full 819-bit signature \(\sigma(C)=(b_K(C))_K\).

The map from all **4095** shift classes to signatures has exactly **4067 distinct values**, comprising **4039 singleton fibers and 28 two-element fibers**. Every pair is a set C and its reflected class [-C], and all 56 paired inputs occur in the two 28-member affine orbits of shapes {0,1,2,3,5} and {0,1,2,4,5}, respectively (orbits 1 and 2 in r347's enumeration). There are **no other signature collisions** in the entire 4095-class universe, and no external class shares a signature with a positive-support r350 class.

## Theorem B: all test-loss functions are independent

The 819-by-4095 binary matrix B with entries \(B_{K,C}=b_K(C)\) has **full row rank 819 over F_2**. Thus its 819 test-class loss functions are linearly independent over Q on the full class domain: a nonzero minor modulo 2 is also a nonzero integer minor.

## Entropy consequence

For any distribution on the 4095 shift classes, replace each class by a fixed representative of its complete signature fiber. This leaves every individual 4-set failure probability and the worst-case maximum unchanged. Its entropy becomes \(H(\sigma(C))=H(C)-H(C\mid\sigma(C))\), the minimum entropy for that **fixed full signature law**. Such a quotient needs at most 4067 atoms. Each fiber has size at most 2; the reduction is at most one bit and is concentrated on the 28 exceptional fibers. For uniform input over the 4095 classes the exact entropy reduction is \(56/4095\) bits.

For the r347 exact minimax optimizer, r350 had already merged precisely those 28 pairs in its selected 378-class support, reducing entropy by \(34177518/474893659\) bits. The new global classification shows that no other classes can be merged by *equality of full loss signatures*. Optimization over **different** signature mixtures with the same minimax value remains a separate problem.

## Finite proof: complete integer-bitmask enumeration

Python 3 standard library only. The verifier enumerates all raw 5- and 4-subsets, quotients by translation, checks every 819-by-4095 event, classifies every signature fiber, and independently computes the 819 row pivots over F_2.

~~~python
from itertools import combinations
from collections import defaultdict, Counter
from math import comb

p=29
FULL=(1<<p)-1
def rot(m,t):
    t%=p
    return (((m<<t)|(m>>(p-t)))&FULL) if t else m
def norm(m):
    return min(rot(m,t) for t in range(p))
def mul(m,a):
    return sum(1<<((a*x)%p) for x in range(p) if (m>>x)&1)
def reps(k):
    return sorted({norm(sum(1<<x for x in a))
                   for a in combinations(range(p),k)})
def affine_orbits(base):
    ix={c:i for i,c in enumerate(base)}
    seen=set()
    out=[]
    for c in base:
        if c in seen: continue
        ids=sorted({ix[norm(mul(c,a))] for a in range(1,p)})
        orb=[base[i] for i in ids]
        assert not (set(orb)&seen)
        seen.update(orb)
        out.append(orb)
    assert len(seen)==len(base)
    return out
def bad(k,c):
    covered=0
    for x in range(p):
        if (c>>x)&1:
            covered|=rot(k,-x)
    return covered.bit_count()<=16
C=affine_orbits(reps(5))
K=affine_orbits(reps(4))
assert (len(C),len(K))==(150,33)
cc=[c for orb in C for c in orb]
kk=[k for orb in K for k in orb]
assert len(cc)==comb(p,5)//p==4095
assert len(kk)==comb(p,4)//p==819
sig=[sum(int(bad(k,c))<<i for i,k in enumerate(kk)) for c in cc]
fibers=defaultdict(list)
for c,s in zip(cc,sig):
    fibers[s].append(c)
assert len(fibers)==4067
assert Counter(map(len,fibers.values()))=={1:4039,2:28}
pairs=[v for v in fibers.values() if len(v)==2]
assert all(norm(mul(a,p-1))==b for a,b in pairs)
special=set(C[1])|set(C[2])
paired={a for v in pairs for a in v}
assert len(C[1])==len(C[2])==28 and paired==special
assert norm(sum(1<<x for x in (0,1,2,3,5))) in C[1]
assert norm(sum(1<<x for x in (0,1,2,4,5))) in C[2]

# Independent F2 row rank of the full test-by-input incidence matrix.
basis={}
for i in range(len(kk)):
    bits=sum(((sig[j]>>i)&1)<<j for j in range(len(cc)))
    while bits:
        pivot=bits.bit_length()-1
        if pivot in basis:
            bits^=basis[pivot]
        else:
            basis[pivot]=bits
            break
assert len(basis)==819
print("r351 PASS: 4095 x 819; 4067 signatures; 28 reflected pairs; rank 819")
~~~

All exact assertions passed in a local execution using integer bit operations. rot implements cyclic translation exactly; bit_count computes the union cardinality exactly. The quotient by all translations gives complete finite coverage, not sampling. F2 independence implies rational independence.

## Source and attribution

r347 exact primal/dual certificate: commit 12bd331ea2aef70cc844682db432a623b235e726.
r349 translation quotient: commit eac1b9044c3b76648b6d352c50ec243650b1bec9.
r350 selected support and 350-column rank: commit 2737a8ea300816066714ef0ff8d72b62c6df2e46.
Original OAI7 scientist EM-EMF6D046-5A2844; Task RS-OAI7-028-C-20261007-6F2A81; publication TP2-96FAC49786245691AE19.

This finite external-model result is not an independent Native mathematical review, Source/Activity publication, formal Task acceptance, X6 carrier transfer or parent-goal completion.
