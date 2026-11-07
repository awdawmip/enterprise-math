#!/usr/bin/env python3
"""Exact A short-carry and Cartier observer certificate (author-side)."""
from math import isqrt, comb

def primes(limit):
    for p in range(7,limit):
        if p%6==1 and all(p%d for d in range(2,isqrt(p)+1)):yield p

def data(p):
    m=(p-1)//6
    inv=lambda z:pow(z%p,-1,p)
    q=[1]
    for i in range(m):q.append(q[-1]*(m-i)*(2*m-i)*inv((i+1)**2)%p)
    r=[inv(18*(m+1)*(2*m+1))]
    for j in range(4*m-1):
        r.append(r[-1]*(j+1)**2*inv((m+j+2)*(2*m+j+2))%p)
    return m,q,r

def carry(p,q,r):
    m=len(q)-1
    return [sum(q[j+ell+1]*r[j] for j in range(m-ell))%p for ell in range(m)]

def direct(p,q,r,x):
    xp=[1]*len(q);xi=[1]*len(r);inverse=pow(x,-1,p)
    for i in range(1,len(q)):xp[i]=xp[i-1]*x%p
    for j in range(1,len(r)):xi[j]=xi[j-1]*inverse%p
    total=0
    for j,rj in enumerate(r):
        subtotal=sum(q[i]*xp[i]*(6*(i-j)-5) for i in range(min(j+1,len(q))))
        total=(total+2*rj*xi[j]*subtotal)%p
    return total

def compact(p,q,r,h,x):
    Q=sum(v*pow(x,i,p) for i,v in enumerate(q))%p
    assert Q==0
    DQ=sum(i*v*pow(x,i,p) for i,v in enumerate(q))%p
    R=sum(v*pow(x,p-1-j,p) for j,v in enumerate(r))%p
    H=sum(v*pow(x,i,p) for i,v in enumerate(h))%p
    DH=sum(i*v*pow(x,i,p) for i,v in enumerate(h))%p
    return (12*DQ*R-2*x*(H+6*DH))%p,(DQ*R)%p,H,DH

def main():
    n=0;roots=0;samples={}
    for p in primes(2500):
        m,q,r=data(p);h=carry(p,q,r)
        assert h[-1]==comb(2*m,m)*r[0]%p and h[-1]!=0
        # Independent coefficient routing using full original exponents for p<250.
        if p<250:
            for ell,a in enumerate(h):
                b=sum(q[i]*r[j] for i in range(len(q)) for j in range(len(r))
                      if p-1+i-j==p+ell)%p
                assert a==b,(p,ell)
        n+=1
        if p%24 not in (13,19):continue
        roots+=1;x=pow(2,-1,p)
        z=compact(p,q,r,h,x)
        assert direct(p,q,r,x)==z[0],(p,z)
        if p in (13,19,43,67,373):samples[p]=z
    assert roots==94 and n==178,(n,roots)
    assert {p:v[0] for p,v in samples.items()}=={13:9,19:13,43:31,67:30,373:1}
    print("PASS A exact short carry",n,"primes; full A readout",roots,"primes")
    print(samples)
if __name__=="__main__":main()
