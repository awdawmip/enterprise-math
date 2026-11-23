#!/usr/bin/env python3
"""Four T6 two-v5-profile pairs obstructed by p^2 cancellation and six p-adic inverse moments."""
from functools import lru_cache
CAP=2331
# Original index; odd v2=5 profiles A,B; local prime; individual remaining mass; signature count.
CASES=[(3,(1,65),(33,33),11,221,2811),
       (9,(1,57),(25,33),19,477,9363),
       (13,(3,51),(19,35),19,605,43626),
       (23,(7,39),(23,23),23,861,129174)]

@lru_cache(maxsize=None)
def signature_set(p,R):
    # d=p^2 cancels by S1 in these cases; no additional v2=5 by
    # exact-two hypothesis; v2>=6 signed differences cancel by prior theorem.
    mod=tuple(p**k for k in range(1,7))
    steps=[(p*u-1,tuple(pow(u,-k,p**k) for k in range(1,7)))
           for u in range(1,(R+1)//p+1) if u%p and u%32]
    out=set()
    def rec(i,mass,sig):
        if i==len(steps):
            out.add(sig)
            return
        cost,vec=steps[i]
        for _ in range((R-mass)//cost+1):
            rec(i+1,mass,sig)
            mass+=cost
            sig=tuple((a+b)%m for a,b,m in zip(sig,vec,mod))
    rec(0,0,(0,)*6)
    return out

def high(p,profile):
    return tuple(sum(pow(32*(j//p),-k,p**k)
                     for j in profile if j%p==0)%(p**k)
                 for k in range(1,7))

def plus(p,a,b):
    return tuple((x+y)%(p**k) for k,(x,y) in enumerate(zip(a,b),1))

for idx,A,B,p,R,expected in CASES:
    assert 32*sum(A)-2==CAP-R==32*sum(B)-2
    assert p**2<=R+1<2*p**2
    assert all(j%(p*p)!=0 for j in A+B)
    # S1 first forces equal multiplicities of the only possible p^2 denominator d=p^2.
    sigs=signature_set(p,R)
    assert len(sigs)==expected,(idx,len(sigs),expected)
    left={plus(p,high(p,A),s) for s in sigs}
    right={plus(p,high(p,B),s) for s in sigs}
    assert left.isdisjoint(right),idx
    print('EXCLUDED',idx,'p',p,'states',len(sigs))
print('PASS: 4 more exact-two-v5 pairs excluded; original 26 -> 3 remain')
