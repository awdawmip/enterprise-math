#!/usr/bin/env python3
"""Original factorial, signed finite Green flux and all-prime p^3 window."""
from math import isqrt
def primes(n):
    return [p for p in range(5,n+1) if all(p%d for d in range(2,isqrt(p)+1))]
def table(n,p,mod):
    v=[0]*(n+1);u=[1]*(n+1)
    for i in range(1,n+1):
        t=i;c=0
        while t%p==0:t//=p;c+=1
        v[i]=v[i-1]+c;u[i]=u[i-1]*t%mod
    return v,u
def original_units(k,p,mod,v,u,power=0):
    vp=v[2*k]+v[3*k]-5*v[k]
    assert vp>=power
    den=pow(u[k],5,mod)*pow(216,k,mod)%mod
    return pow(p,vp-power,mod)*u[2*k]*u[3*k]*pow(den,-1,mod)%mod
def green(p,N):
    r=(p-1)//6;mod=p**N
    ks=[3*r+1+s for s in range(r+1)]
    v,u=table(3*ks[-1],p,mod)
    Y=[original_units(k,p,mod,v,u,2) for k in ks]
    assert all(y%p for y in Y[:-1]) and not Y[-1]%p
    K=[pow(k,3,mod) for k in ks]
    C=[(2*k+1)*(3*k+1)*(3*k+2)*pow(36,-1,mod)%mod for k in ks[:-1]]
    assert all((C[s]*Y[s]-K[s+1]*Y[s+1])%mod==0 for s in range(r))
    W=[6*k+1 for k in ks[:-1]]
    F=sum(a*b for a,b in zip(W,Y[:-1]))%mod
    def back(w):
        P=[0]*(r+1)
        for s in range(r-1,-1,-1):
            P[s]=(C[s]*P[s+1]-w[s])*pow(K[s],-1,mod)%mod
        assert all((C[s]*P[s+1]-K[s]*P[s]-w[s])%mod==0 for s in range(r))
        return P
    P=back(W)
    assert (F+K[0]*Y[0]*P[0])%mod==0
    W0=W[:];W0[0]=(W0[0]-F*pow(Y[0],-1,mod))%mod
    assert back(W0)[0]==0
    q=[0]+[3*s*s+5*s+7 for s in range(1,r)]+[0]
    D=[(C[s]*q[s+1]-K[s]*q[s])%mod for s in range(r)]
    assert sum(D[s]*Y[s] for s in range(r))%mod==0
    return F,P[0]
def full(p):
    mod=p**3;v,u=table(3*(p-1),p,mod)
    return sum((6*k+1)*original_units(k,p,mod,v,u) for k in range(p))%mod
if __name__=="__main__":
    ps=primes(2000)
    high=[p for p in ps if p%6==1]
    for p in high:
        for N in (1,2,3):green(p,N)
    for p in ps:
        target=p if p%6==1 else (p**3-p)
        assert full(p)==target, (p,full(p),target)
    print("PASS 148 high-strip primes * 3 precisions, 22952 sites per precision; 301 full original sums mod p^3")
    for p in (13,19,373):print("sample",p,"flux,P0 mod p^2",green(p,2))
