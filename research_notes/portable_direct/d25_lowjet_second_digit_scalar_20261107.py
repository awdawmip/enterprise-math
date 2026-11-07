#!/usr/bin/env python3
"""Scalar A/B p-adic Gauss zero/derivative source identity; p^3 exact check."""
from d25_compact_fricke_defect_20261107 import primes,series,run

def scalar_gamma(p):
    mod=p**3
    m=(p-1)//6
    k=(p-3)//8 if p%8==3 else (p-5)//8
    xa=pow(2,-1,mod);xb=pow(9,-1,mod)
    f=series(p,mod,[(6,1),(3,1)],2*m)
    g=series(p,mod,([(8,1),(8,3)] if p%8==3 else [(8,5),(8,7)]),3*k+1)
    def jet(c,x):
        f=d=0;xp=1
        for n,a in enumerate(c):
            f=(f+a*xp)%mod
            d=(d+n*a*xp)%mod
            xp=xp*x%mod
        return f,d
    FA,TA=jet(f,xa);FB,TB=jet(g,xb)
    assert FA%p==FB%p==0,(p,FA,FB)
    ua,ub=FA//p,FB//p
    C=1 if p%8==3 else (1-xb)%mod
    delta=1 if p%8==3 else 0
    numerator=12*ua*TA-16*C*ub*TB
    assert numerator%p==0
    gamma=(numerator//p+ua*ua-delta*ub*ub)%p
    ga=(FA*FA+12*FA*TA)%mod
    gb=((FB*FB+16*FB*TB) if delta else 16*C*FB*TB)%mod
    assert (ga-gb)%(p*p)==0
    assert ((ga-gb)%mod)//(p*p)==gamma
    return gamma,ua%p,ub%p,TA%p,TB%p

def main():
    P=list(primes(2500))
    samples={}
    for p in P:
        z=scalar_gamma(p)
        assert z[0]==run(p)[5],p
        if p in (13,19,43,67,373,997):samples[p]=z
    assert len(P)==94 and samples[373][0]==219
    print("PASS scalar p-adic second digit",len(P),"target primes p<2500")
    print(samples)
if __name__=="__main__":main()
