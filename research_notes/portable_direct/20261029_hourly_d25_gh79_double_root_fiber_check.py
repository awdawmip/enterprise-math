#!/usr/bin/env python3
"""GH79 exact Fp jets: double-root fiber and normalization witness (auxiliary research)."""
from collections import Counter

def primes_lt(bound):
    alive = bytearray(b'\x01') * bound
    alive[:2] = b'\x00\x00'
    for k in range(2, int((bound - 1)**0.5)+1):
        if alive[k]:
            alive[k*k::k] = b'\x00' * len(alive[k*k::k])
    return [n for n in range(7, bound) if alive[n]]

def coeffs(p):
    d = (p - 3)//4
    h=[1]
    for r in range(d):
        num=pow(4*r+3, 3, p)
        den=(4*r+4)*(4*r+5)*(4*r+6)
        h.append(h[-1]*num*pow(den, -1, p)%p)
    return h

def jet(h, k, z, p):
    acc=0
    for r in range(k,len(h)):
        falling=1
        for j in range(k): falling=falling*(r-j)%p
        acc=(acc+h[r]*falling*pow(z,r-k,p))%p
    return acc

n=0; categories=Counter()
for p in primes_lt(2000):
    if p%8!=7: continue
    h=coeffs(p)
    j=[jet(h,k,9,p) for k in range(3)]
    H=[(8*r+5)*v%p for r,v in enumerate(h)]
    Hj=[jet(H,k,9,p) for k in range(2)]
    assert Hj[0]==(72*j[1]+5*j[0])%p
    assert Hj[1]==(72*j[2]+13*j[1])%p
    categories[(p%24, j[0]==0, j[1]==0, j[2]!=0, Hj[0]==0, Hj[1]!=0)]+=1
    if p==23:
        assert h==[1,10,7,21,19,11]
        assert j==[0,0,21]
        assert H==[5,15,9,11,13,12]
        assert Hj==[0,17]
        alpha=pow(16,-1,p)
        for i in range(2*((p-3)//4)+2):
            alpha=alpha*pow(4*i+1,3,p)%p
            for b in (2,3,4):
                factor=(4*i+b)%p
                if factor: alpha=alpha*pow(factor,-1,p)%p
        d=(p-3)//4
        Q=alpha*pow(9,2*d+2,p)*pow(8,-1,p)%p
        C=[1]
        for r in range(d):
            C.append(C[-1]*9*pow(4*r+1,3,p)*pow((4*r+2)*(4*r+3)*(4*r+4),-1,p)%p)
        slopes=[Q*Hj[1]*pow(value,-1,p)%p for value in C]
        assert alpha==12 and Q==2 and C==[1,9,2,9,3,19] and slopes==[11,14,17,14,19,3]
        print('EXACT_GH79_WITNESS p=23 Ucoeff=',h,'U_jets=',j,'Hcoeff=',H,'H_jets=',Hj)
        print('EXACT_GH79_RANK_SLOPES p=23 alpha=',alpha,'C=',C,'A_r_prime=',slopes)
    n+=1
assert n==78
assert categories[(23, True, True, True, True, True)]==37
assert categories == Counter({
    (7,False,False,False,True,True):1,
    (7,False,False,True,True,True):40,
    (23,True,True,True,True,True):37,
})
print('GH79_VERIFIED_ODD_CLASS_PRIMES',n)
for key,value in sorted(categories.items()): print('OBSERVED_ONLY_CATEGORY',key,'count=',value)
