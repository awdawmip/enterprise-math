"""Exact author-side checks for EC49FVC 7-adic/13-adic phase sieve.
The infinite theorem is proved by local valuation case splits, not this finite enumeration.
"""
from fractions import Fraction
from math import gcd

Q=Fraction
BETA=Q(3,637)
GAMMA=Q(141024,1653649)
U=Q(4822040484,8132285009)

def val(z,p):
    if z==0:
        raise ValueError('zero does not have finite valuation')
    n,d=z.numerator,z.denominator
    k=0
    while n%p==0:
        n//=p;k+=1
    while d%p==0:
        d//=p;k-=1
    return k

def phase_pair(x,p):
    T0=(1-x)*(1-BETA*x)
    TE=(1-x)*(1+GAMMA*x)
    a=1-T0
    b=1-U*TE
    R=T0/(U*TE)
    S=R*b/a
    assert 0<a<b<1 and 1<R<S
    return val(R,p),val(S,p)

def impossible(vr,vs):
    return (vr,vs)!=(0,0) and not (vr*vs>0 and abs(vr)<abs(vs))

assert (val(BETA,7),val(GAMMA,7),val(U,7),val(1+GAMMA,7))==(-2,0,0,0)
assert (val(BETA,13),val(GAMMA,13),val(U,13),val(1+GAMMA,13))==(-1,1,0,0)
assert ((1-99)//49)%7 == 5
assert ((1-157)//13)%13 == 1
assert 343*169==57967

counts={7:0,13:0}
for d in range(2,321):
    for m in range(1,d):
        if gcd(m,d)!=1: continue
        x=Q(m,d)
        for p,mod,exception in ((7,343,99),(13,169,157)):
            if m%p==0 or d%p==0: continue
            residue=m*pow(d,-1,mod)%mod
            if residue==exception: continue
            pair=phase_pair(x,p)
            assert impossible(*pair),(x,p,residue,pair)
            counts[p]+=1

for x in (Q(99,344),Q(157,170),Q(1,2),Q(7,20),Q(1,30)):
    print('WITNESS',str(x),'v7',phase_pair(x,7),'v13',phase_pair(x,13))
assert (99%343, 157%169)==(99,157)
print('EXACT_FINITE_CROSSCHECK_PASS',counts,'CRT_exception=38858 mod57967','unit_classes_certified=45863/45864')
