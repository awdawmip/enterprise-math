#!/usr/bin/env python3
"""Original W216 weighted valuation-two half-tail, finite exact 428-prime check."""
from math import isqrt

def primes(n):
    flag=bytearray(b'\x01')*(n+1)
    flag[0]=flag[1]=0
    for p in range(2,isqrt(n)+1):
        if flag[p]:
            for k in range(p*p,n+1,p):flag[k]=0
    return [p for p in range(5,n+1) if flag[p]]

def b2_w(p):
    F=[1]*(2*p)
    V=[0]*(2*p)
    for n in range(1,2*p):
        z=n;vv=0
        while z%p==0:z//=p;vv+=1
        V[n]=V[n-1]+vv
        F[n]=F[n-1]*z%p
    H=(p-1)//2;E=(2*p-1)//3
    total=0
    for b in range(H+1,E+1):
        assert V[2*b]+V[3*b]-5*V[b]==2
        u=F[2*b]*F[3*b]*pow(F[b],-5,p)*pow(216,-b,p)%p
        total=(total+(6*b+1)*u)%p
    return total

if __name__=="__main__":
    P=primes(3000)
    targets=[p for p in P if p%24 in (13,19)]
    vals={p:b2_w(p) for p in P}
    assert len(P)==428 and len(targets)==107
    assert all(v!=0 for v in vals.values())
    assert vals[373]==266 and vals[1171]==1048
    print({"all_prime_count":len(P),"target_prime_count":len(targets),"zeros":[],"p373":vals[373],"p1171":vals[1171]})
