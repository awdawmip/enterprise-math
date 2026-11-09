#!/usr/bin/env python3
"""Exact p^2 first-jet valuation bands for the original CM Gauss overflow."""
from math import comb
import json

def certificate(p):
    assert p>3 and p%24==13
    mod=p*p
    a,b,q=(5*p-1)//8,(7*p-3)//8,(p-1)//4
    inv=lambda x,n:pow(x%n,-1,n)
    d=[1]
    for k in range(1,p):
        d.append(d[-1]*(8*k-7)*(8*k-5)*inv(16*k*k,mod)%mod)
    fact=[1]*p
    for k in range(1,p): fact[k]=fact[k-1]*k%p
    d0,d1=[0]*p,[0]*p
    for k in range(p):
        if k<=a:
            base=pow(4,k,mod)*comb(a,k)*comb(b,k)%mod
            ha=sum(inv(i,p) for i in range(a-k+1,a+1))%p
            hb=sum(inv(i,p) for i in range(b-k+1,b+1))%p
            d0[k]=base
            d1[k]=(-p*base*inv(8,p)*(5*ha+7*hb))%mod
        elif k<=b:
            unit=(5*inv(8,p)*pow(4,k,p)*(-1)**(a+k)*fact[a]*fact[k-a-1]
                  *fact[b]*inv(fact[b-k],p)*inv(fact[k]**2,p))%p
            d1[k]=p*unit
        assert (d0[k]+d1[k])%mod==d[k],(p,k)
    def edge(c):
        e=[0]*(p-1)
        for k in range((p+1)//2,p):
            if c[k]==0: continue
            for j in range(p-k,k+1):
                r=k+j-p
                e[r]=(e[r]+c[k]*(-1 if j%2 else 1)*comb(k,j))%mod
        return e
    e,base,jet=edge(d),edge(d0),edge(d1)
    assert all((base[r]+jet[r])%mod==e[r] for r in range(p-1))
    assert all(e[r]%p==0 for r in range(q+1,p-1))
    assert all(e[r]==0 for r in range(3*q+1,p-1))
    assert all(base[r]==0 for r in range(q+1,p-1))
    T=[2,1]; inv36=inv(36,mod)
    for r in range(2,3*q+1):
        T.append((T[-1]-inv36*T[-2])%mod)
    low=sum(e[r]*T[r] for r in range(q+1))%mod
    middle=sum(e[r]*T[r] for r in range(q+1,3*q+1))%mod
    assert low%p==middle%p==0
    assert (low+middle)%mod==sum(e[r]*T[r] for r in range(3*q+1))%mod
    return dict(p=p,a=a,b=b,q=q,degree_p2=3*q,
                low_over_p=low//p,middle_over_p=middle//p,
                scalar=(low+middle)%mod,scalar_over_p=((low+middle)%mod)//p,
                coefficients_exactly_matched=p,overflow_coefficients_matched=p-1)

if __name__=="__main__":
    print(json.dumps([certificate(p) for p in (13,37,61,109,373)],indent=2))
