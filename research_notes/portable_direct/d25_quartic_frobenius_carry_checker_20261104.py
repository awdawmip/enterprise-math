#!/usr/bin/env python3
"""Exact finite-field Frobenius carry check, author-side only."""
from math import isqrt, comb

def primes(n):
    ss=bytearray([1])*(n+1); ss[:2]=b'\x00\x00'
    for d in range(2,isqrt(n)+1):
        if ss[d]:ss[d*d:n+1:d]=bytearray((n-d*d)//d+1)
    return [p for p in range(5,n+1) if ss[p] and p%8==5]

def check(p, full=True):
    q=(p-5)//8; L=5*q+3; t=2*q+1
    v=[1]
    for k in range(L):
        v.append(v[-1]*(8*k+1)*(8*k+3)*pow(576*(k+1)**2,-1,p)%p)
    b=[1]
    for k in range(t):
        b.append(b[-1]*(4*k+1)*(4*k+2)*(4*k+3)*pow(576*(k+1)**3,-1,p)%p)
    lam=v[L]*v[L]*pow(b[t],-1,p)%p
    assert lam!=0
    pred=b+[0]*(p-t-1)+[lam*x%p for x in b]
    assert len(pred)==2*L+1
    if full:
        c=[0]*(2*L+1)
        for i,x in enumerate(v):
            for j,y in enumerate(v):
                c[i+j]=(c[i+j]+x*y)%p
        assert c==pred, (p,'polynomial')
    else:
        for n in (0,t,t+1,p-1,p,p+1,p+t,2*L):
            act=sum(v[i]*v[n-i] for i in range(max(0,n-L),min(L,n)+1))%p
            assert act==pred[n], (p,n)
    if p<=101:
        for k in range(t+1):
            assert b[k]==comb(2*k,k)**2*comb(4*k,2*k)*pow(2304,-k,p)%p
    port=sum((8*k+1)*x for k,x in enumerate(b))%p
    upper=sum((8*(p+k)+1)*lam*x for k,x in enumerate(b))%p
    assert upper==lam*port%p
    m=p*p; v2=[1]*p; b2=[1]*p
    for k in range(p-1):
        v2[k+1]=v2[k]*(8*k+1)*(8*k+3)*pow(576*(k+1)**2,-1,m)%m
        b2[k+1]=b2[k]*(4*k+1)*(4*k+2)*(4*k+3)*pow(576*(k+1)**3,-1,m)%m
    S=sum(v2)%m; D=sum(k*v2[k] for k in range(p))%m
    V=sum((8*k+1)*b2[k] for k in range(p))%m
    T=(S*S+16*S*D-V)%m
    assert T%p==upper
    assert port==0
    assert (S*S+16*S*D)%m==0 # finite observation, not theorem
    return lam,T//p

if __name__=="__main__":
    ps=primes(2000)
    for p in ps:check(p,full=p<=1200)
    print("PASS",len(ps),"primes",sum(p<=1200 for p in ps),"full",sum(p>1200 for p in ps),"sampled")
    for p in (5,13,29,37,61,373):
        print(p,check(p,full=True))
