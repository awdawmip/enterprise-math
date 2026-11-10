#!/usr/bin/env python3
"""D25 frozen scalar LIFT cross-port exact integer certificate.
AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED; no native H0/B0 computation.
Scientific pin: c47e13e4aba0e006366f989d6334d443f6333ae3.
"""
from math import comb, factorial

PRIMES=(13,19,109,139,157,163,373)

def check(p):
    assert p>3 and p%24 in (13,19)
    m=(p-1)//6
    mod=p**3
    b=[1]; a=[1]
    for k in range(p-1):
        b.append(b[-1]*(6*k+1)*(3*k+1)*pow(36*(k+1)**2,-1,mod)%mod)
        a.append(a[-1]*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3,-1,mod)%mod)
    # Independently reconstruct each original coefficient.
    num=1
    for k in range(p):
        if k:
            t=k-1
            num *= (6*t+1)*(3*t+1)
        b_ind=num*pow(36**k*factorial(k)**2,-1,mod)%mod
        a_ind=comb(2*k,k)**2*comb(3*k,k)*pow(216,-k,mod)%mod
        assert (b[k],a[k])==(b_ind,a_ind), (p,k)
    M=sum(b)%mod
    N=sum(k*v for k,v in enumerate(b))%mod
    W=sum((6*k+1)*v for k,v in enumerate(a))%mod
    assert M%p==0 and W%p**2==p
    # Independent original signed ordered Clausen cutoff.
    Q=sum((6*(i+j)+1)*b[i]*b[j]
          for i in range(p) for j in range(p-i,p))%mod
    assert Q==(M*(M+12*N)-W)%mod and Q%(p*p)==0
    C=[0]*(m+1); C[1]=pow(10,-1,p)
    for t in range(1,m):
        C[t+1]=C[t]*36*t*t*pow((6*t+5)*(3*t+2),-1,p)%p
    for j in range(1,m+1):
        den=1
        for t in range(j):
            den *= (6*t+5)*(3*t+2)
        assert C[j]==36**(j-1)*factorial(j-1)**2*pow(den,-1,p)%p
    R=2*sum(b[i]*sum((1+6*(i-j))*C[j] for j in range(1,i+1))
            for i in range(1,m+1))%p
    assert R==Q//p**2
    G=M//p
    gh=G*((M+12*N)%p**2)%p**2
    assert gh%p==1
    Delta=((gh-1)%p**2)//p
    lam=((W-p)%mod)//p**2
    assert (Delta-R)%p==lam
    assert Delta==R and lam==0   # Exact finite witnesses only.
    return dict(p=p,m=m,p3=mod,M=M,N=N,W=W,Q=Q,Gh=gh,
                Delta=Delta,R_frozen=R,R_cutoff=Q//p**2,LIFT=lam)

if __name__=="__main__":
    for p in PRIMES:
        print(check(p))
