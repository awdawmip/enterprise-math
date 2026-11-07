#!/usr/bin/env python3
"""Exact support proof checks: unique F0*F2 Frobenius tail overflow."""
from d25_three_stratum_harmonic_four_port_check_20261107 import gauss_ports, primes

def check_one(p,model):
    if model=='A':
        u=(p-1)//6;v=2*u;pars=(u,v,1,2,6);lam=6;x=pow(2,-1,p);eps=0
    else:
        u=(p-3)//8 if p%8==3 else (p-5)//8
        v=3*u+1;pars=(u,v,1,3,8);lam=8;x=pow(9,-1,p);eps=1 if p%8==5 else 0
    F0,F1,F2=gauss_ports(p,*pars)
    F0=[a%p for a in F0];F1=[a%p for a in F1];F2=[a%p for a in F2]
    def product(a,b):
        out=[0]*(2*p+2)
        for i,aa in enumerate(a):
            if aa:
                for j,bb in enumerate(b):
                    if bb:out[i+j]=(out[i+j]+aa*bb)%p
        if eps:out=[(x-(out[i-1] if i else 0))%p for i,x in enumerate(out)]
        return out
    assert not any(product(F0,F0)[p:])
    assert not any(product(F0,F1)[p:])
    assert not any(product(F1,F1)[p:])
    full=product(F0,F2)
    val=0;first=None
    for n in range(p,p+u+eps):
        d=(2*sum(F0[i]*F2[n-i] for i in range(u+1) if 0<=n-i<p)
           -2*eps*sum(F0[i]*F2[n-1-i] for i in range(u+1) if 0<=n-1-i<p))%p
        assert d==2*full[n]%p,(p,model,n,d,full[n])
        if first is None:first=d
        val=(val+(1+lam*(n-p))*pow(x,n-p+1,p)*d)%p
    assert all(full[n]%p==0 for n in range(p+u+eps,len(full)))
    return (u+eps,first,val)

if __name__=='__main__':
    ctA=ctB=0
    for p in primes(401):
        if p%6==1:check_one(p,'A');ctA+=1
        if p%8 in (3,5):check_one(p,'B');ctB+=1
    assert (ctA,ctB)==(37,41)
    witnesses={p:(check_one(p,'A'),check_one(p,'B')) for p in (13,19,43,67,373)}
    assert witnesses=={
        13:((2,1,0),(2,7,10)),
        19:((3,1,12),(2,12,3)),
        43:((7,42,15),(5,17,14)),
        67:((11,22,21),(8,26,46)),
        373:((62,315,196),(47,97,131))
    },witnesses
    print('PASS tail-only Frobenius support for',ctA,'A',ctB,'B primes <=401')
    print(witnesses)
