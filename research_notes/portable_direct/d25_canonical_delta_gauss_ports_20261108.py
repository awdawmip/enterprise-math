#!/usr/bin/env python3
"""Prove/check a Gauss source-port formula for the canonical D24 Delta_p=(g/p*h-1)/p.
This is NOT a proof of Delta_p=R_p; R_p is the frozen target.
"""
from math import comb
from d25_gauss_second_lift_three_strata_20261108 import primes, verify

def check(p):
    assert p%24 in (13,19)
    u=(p-1)//6; v=2*u
    mod=p**3; mod2=p*p
    x=pow(2,-1,mod)
    lam=pow(6,-1,mod2); mu=pow(3,-1,mod2)
    H=[0]*(p); fac=[1]*p
    for n in range(1,p):
        H[n]=(H[n-1]+pow(n,-1,mod2))%mod2
        fac[n]=fac[n-1]*n%mod2
    ifac=[1]*p; ifac[-1]=pow(fac[-1],-1,mod2)
    for n in range(p-1,0,-1): ifac[n-1]=ifac[n]*n%mod2
    Q=0; P=0; H0=0; H1=0
    xn=1
    for n in range(v+1):
        if n<=u:
            q=comb(u,n)*comb(v,n)
            first=(lam*(H[u-n]-H[u])+mu*(H[v-n]-H[v]))%mod2
            pf=q*first%mod2
            Q=(Q+q*xn)%mod
            H0=(H0+(1+12*n)*q*xn)%mod2
        else:
            sign=-1 if (u+n)%2 else 1
            pf=(sign*lam*fac[u]*fac[n-u-1]*fac[v]*ifac[v-n]*ifac[n]*ifac[n])%mod2
        P=(P+pf*xn)%mod2
        H1=(H1+(1+12*n)*pf*xn)%p
        xn=xn*x%mod
    Z=(Q+p*P)%mod
    assert Z%p==0
    z=Z//p
    gauss_over_p,_,ports=verify(p,'A')
    S=sum(ports[2:])%p
    base=((z*H0-1)%mod2)
    assert base%p==0,(p,'UR failed',base)
    D_base=base//p%p
    D_S=S*H0%p
    D_H=z*H1%p
    D_calc=(D_base+D_S+D_H)%p
    # Independent direct g and h recurrences from the exact original 216 coefficients.
    gauss=1; raw_g=0; raw_h=0
    for n in range(p):
        raw_g=(raw_g+gauss)%mod
        raw_h=(raw_h+(12*n+1)*gauss)%mod2
        if n+1<p:
            gauss=gauss*(6*n+1)*(3*n+1)*pow(36*(n+1)*(n+1),-1,mod)%mod
    assert raw_g%p==0
    assert gauss_over_p==raw_g//p%mod2
    raw_prod=((raw_g//p)*raw_h-1)%mod2
    assert raw_prod%p==0
    D_raw=raw_prod//p
    assert D_calc==D_raw,(p,D_calc,D_raw,D_base,D_S,D_H)
    return D_raw,(D_base,D_S,D_H),S,z%p,H0%p,H1

def main():
    ps=[p for p in primes(2500) if p%24 in (13,19)]
    samples={}
    for p in ps:
        res=check(p)
        if p in (13,19,43,67,373):samples[p]=res
    print('PASS canonical Delta source split for',len(ps),'target primes p<2500; no R_p assumption')
    for p,res in sorted(samples.items()):print('p',p,'Delta, (D_base,D_S,D_H), S, Z0,H0,H1 =',res)

if __name__=='__main__':main()
