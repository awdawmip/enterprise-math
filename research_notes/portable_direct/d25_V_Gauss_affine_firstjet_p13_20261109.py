#!/usr/bin/env python3
"""D25: exact first affine jet for the original V Gauss factor, p=13 mod24."""
from math import comb

def certificate(p):
    assert p>5 and p%24==13
    a=(5*p-1)//8; b=(7*p-3)//8
    pp=p*p; z=pow(9,-1,pp); zz=z%p
    P=sum(comb(a,k)*comb(b,k)*pow(z,k,pp) for k in range(a+1))%pp
    inv=[0]+[pow(i,-1,p) for i in range(1,p)]
    H=[0]
    for i in range(1,p): H.append((H[-1]+inv[i])%p)
    r=5*pow(8,-1,p)%p; s=7*pow(8,-1,p)%p
    L=0
    for k in range(a+1):
        c=comb(a,k)*comb(b,k)*pow(zz,k,p)%p
        L=(L-c*(r*(H[a]-H[a-k])+s*(H[b]-H[b-k])))%p
    fact=[1]
    for i in range(1,p): fact.append(fact[-1]*i%p)
    fi=[pow(v,-1,p) for v in fact]
    T=0
    for k in range(a+1,b+1):
        t=r*(-1)**(a+k)*fact[a]*fact[b]*fact[k-a-1]*fi[b-k]*fi[k]**2*pow(zz,k,p)
        T=(T+t)%p
    M=d=1
    for k in range(p-1):
        d=d*(8*k+1)*(8*k+3)*pow(576*(k+1)**2,-1,pp)%pp
        M=(M+d)%pp
    assert (P+p*(L+T))%pp==M,(p,P,L,T,M)
    return p,a,b,P//p%p if P%p==0 else None,L,T,M

def primes(n):
    a=[True]*(n+1); a[:2]=[False,False]
    for d in range(2,int(n**0.5)+1):
        if a[d]:
            for k in range(d*d,n+1,d): a[k]=False
    return [p for p in range(n+1) if a[p]]

if __name__=="__main__":
    rows=[certificate(p) for p in primes(1000) if p%24==13]
    assert len(rows)==22
    assert all(x[3] is not None and (x[3]+x[4]+x[5])%x[0]==0 and x[6]==0 for x in rows)
    print("PASS",len(rows),"exact firstjet certificates")
    for p in (13,37,61,109,157,181,373):
        print(next(x for x in rows if x[0]==p))
