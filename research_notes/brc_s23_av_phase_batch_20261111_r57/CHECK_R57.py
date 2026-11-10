#!/usr/bin/env python3
"""Independent, exact-integer R57 batch-cut verifier. Science pin 43ec6098b1330ae86d0a7863be336c5d97f6ef34."""
from bisect import bisect_right
from math import gcd
from random import Random

def bracket(p,q,K):
    a,i,c,j=0,1,1,1
    while i+j<=K:
        if (a+c)*q<(i+j)*p: a,i=a+c,i+j
        else: c,j=c+a,j+i
    return i,j

def run(p,q,m,H,k):
    K=m+H-1
    assert q//gcd(p,q)>K
    i,j=bracket(p,q,K)
    s=j; cuts=[]
    for _ in range(K):
        cuts.append(s)
        s=s-i if s>i else (s+j if s+j<=K else s+j-i)
    assert s==j and set(cuts)==set(range(1,K+1))
    assert all((cuts[t]*p)%q>(cuts[t+1]*p)%q for t in range(K-1))
    w=[(z*p)%q for z in cuts]
    x0=q+w[0]; x1=w[k-1]+(w[k] if k<K else 0)
    history=sorted((2*(z*p%q),z) for z in range(m))
    bv=[v for v,z in history]; order=[z for v,z in history]
    rank={z:t for t,z in enumerate(order)}
    pred={z:order[(t-1)%m] for t,z in enumerate(order)}
    def owners(x):
        return [order[bisect_right(bv,(x-2*r*p)%(2*q))-1] for r in range(1,H+1)]
    old=owners(x0); expect=owners(x1)
    diff=[0]*(H+2); E=0
    live=old[:]
    for s in cuts[:k]:
        lo=max(1,s-m+1); hi=min(H,s)
        diff[lo]+=1;diff[hi+1]-=1;E+=hi-lo+1
        for r in range(lo,hi+1):
            z=s-r
            assert live[r-1]==z
            live[r-1]=pred[z]
    assert live==expect
    count=0; grouped=[]
    for r in range(1,H+1):
        count+=diff[r]
        grouped.append(order[(rank[old[r-1]]-count)%m])
    assert grouped==expect
    def ages(a):
        ret=[None]*m
        for r,z in enumerate(a,1):
            if ret[z] is None:ret[z]=r
        return ret
    assert ages(grouped)==ages(expect)
    return E,old==expect,ages(old)==ages(expect)

def main():
    rng=Random(570011); total=0;N=0
    for m in range(1,13):
        for H in range(1,16):
            K=m+H-1
            for rep in range(8):
                p=rng.randrange(1,1009)
                k=(rep*59+m*13+H*7)%K+1
                E,_,_=run(p,1009,m,H,k)
                total+=E;N+=1
    assert N==1440 and total==39295
    D=10**24;lo=262204504569236716045286
    for p in (lo,lo+1):
        for k in (1,4,32,88,176,264,352):
            E,_,_=run(p,D,128,225,k)
            if k==176:assert E==14418
            if k==352:assert E==28800 and run(p,D,128,225,k)[1:]==(True,True)
    print('PASS_R57',N,total,'frozen_cases',14,'half_events',14418,'full_events',28800)
if __name__=='__main__':main()
