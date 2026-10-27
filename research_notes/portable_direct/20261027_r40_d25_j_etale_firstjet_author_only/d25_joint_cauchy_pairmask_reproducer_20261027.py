#!/usr/bin/env python3
"""Portable author-side p^3 pairwise Cauchy carry-support proof regression."""
from collections import defaultdict
from math import comb

def vf(n,p):
    ans=0
    while n:
        n//=p;ans+=n
    return ans

def vu(n,p): return vf(2*n,p)-2*vf(n,p)
def vc(n,p): return vf(3*n,p)+vf(2*n,p)-5*vf(n,p)

def U(p,e):
    a,b=(p+1)//2,(p-1)//2
    if e==0:return 1
    if e==1:return p
    out=a**e+2*b*a**(e-1)+(2*e-3)*b*b*a**(e-2)
    if e>=3:out+=(e-2)*b**3*a**(e-3)
    if e>=4:out+=(e-2)*(e-3)//2*b**4*a**(e-4)
    return out

def count(N,p):
    if N==0:return 0
    digs=[]
    while N:
        N,d=divmod(N,p);digs.append(d)
    # u carry, c binary carry, c ternary carry, sum valuation,
    # addition carry, comparison of source-index sum with N.
    dp={(0,0,0,0,0,0):1}
    for bound in digs:
        nxt=defaultdict(int)
        for (u,a,b,v,add,cmp),w in dp.items():
            for j in range(p):
                uj=(2*j+u)//p
                for k in range(p):
                    ak,bk=(2*k+a)//p,(3*k+b)//p
                    v1=v+uj+ak+bk
                    if v1>=3:continue
                    q,r=divmod(j+k+add,p)
                    cmp1= -1 if r<bound else (1 if r>bound else cmp)
                    nxt[uj,ak,bk,v1,q,cmp1]+=w
        dp=nxt
    return sum(w for (u,a,b,v,add,cmp),w in dp.items()
               if add==0 and cmp==-1)

def example(p,N):
    m=p**3;total=short=seen=0
    cu=[comb(2*j,j)*pow(8,-j,m)%m for j in range(N)]
    cc=[comb(3*k,k)*comb(2*k,k)**2*pow(216,-k,m)%m for k in range(N)]
    for k in range(N):
        for j in range(N-k):
            v=(3*(j+k)-1)*cu[j]*cc[k]
            total=(total+v)%m
            if vu(j,p)+vc(k,p)<3:
                short=(short+v)%m;seen+=1
            else: assert v%m==0
    assert short==total and seen==count(N,p)
    return p,N,seen,N*(N+1)//2,total

if __name__=='__main__':
    for p in (5,7,11,13,19,43):
        for e in range(5):
            if p**e<=20000:
                assert U(p,e)==sum(vu(n,p)<3 for n in range(p**e))
        for N in (1,p+1,2*p+3):
            assert count(N,p)==sum(vu(j,p)+vc(k,p)<3
                                   for k in range(N) for j in range(N-k))
    examples=[example(p,2*p+3) for p in (5,7,11,13,19)]
    assert examples==[(5,13,72,91,82),(7,17,114,153,115),
                      (11,25,246,325,466),(13,29,321,435,2157),
                      (19,41,636,861,3372)]
    assert count(373**3,373)==168999151344875
    print('PASS author-only; full exact signed sample:',examples)
    print('p=373,e=3, count only:',count(373**3,373))
