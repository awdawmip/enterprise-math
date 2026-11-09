#!/usr/bin/env python3
"""Exact finite-log carry reconstruction of p^2 Gauss overflow from G_p."""
from math import comb
import json

def check(p):
    assert p>3 and p%24==13
    mod=p*p
    inv=lambda x,m:pow(x%m,-1,m)
    f,g=[1],[1]
    for k in range(1,p):
        f.append(f[-1]*(8*k-7)*(8*k-5)*inv(64*k*k,mod)%mod)
        g.append(g[-1]*(4*k-3)*(4*k-1)*inv(16*k*k,mod)%mod)
    e=[0]*p
    for k in range((p+1)//2,p):
        c=pow(4,k,mod)*f[k]%mod
        for j in range(p-k,k+1):
            e[k+j-p]=(e[k+j-p]+c*(-1 if j&1 else 1)*comb(k,j))%mod
    assert all((g[k]+sum(g[j]*(-1)**k*comb(j,k) for j in range(k,p)))%mod==0
               for k in range(p))
    A=[0]*p
    for j in range(1,p):
        v=inv(j,p)
        for k in range(p-j):
            A[j+k]=(A[j+k]+v*g[k])%p
    Ar=[sum(A[j]*(-1)**k*comb(j,k) for j in range(k,p))%p for k in range(p)]
    predicted=[(-2*g[k]+2*p*Ar[k])%mod for k in range(p)]
    assert predicted==e
    T=[2,1]; inv36=inv(36,mod)
    for r in range(2,p):
        T.append((T[-1]-inv36*T[-2])%mod)
    S=sum(e[r]*T[r] for r in range(p))%mod
    assert S%p==0
    tr_A=sum(Ar[r]*T[r] for r in range(p))%p
    assert (S//p-2*tr_A)%p==0
    return dict(p=p,coefficients_reconstructed=p,S_mod_p2=S,
                S_over_p=S//p,trace_logcarry=tr_A)

if __name__=="__main__":
    print(json.dumps([check(p) for p in (13,37,61,109,373)],indent=2))
