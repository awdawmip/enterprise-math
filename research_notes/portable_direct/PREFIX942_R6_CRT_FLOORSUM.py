#!/usr/bin/env python3
"""PREFIX-942: exact CRT/floor-sum witness census with independent small brute check."""
from math import gcd
import random, json

def floor_sum(n,m,a,b):
    assert n>=0 and m>=1 and a>=0 and b>=0
    ans=0
    while True:
        if a>=m:
            ans+=n*(n-1)//2*(a//m); a%=m
        if b>=m:
            ans+=n*(b//m); b%=m
        z=a*n+b
        if z<m: return ans
        n=z//m
        b=z%m
        a,m=m,a

def count_branch(k,t,i,j,s,lo,hi):
    H=1<<j; C=(1<<i)+s*H
    d=gcd(k,t)
    if C%d: return 0
    km=k//d
    residue=(-C//d*pow(t//d,-1,km))%km if km>1 else 0
    residue += km*(residue%2==0)
    step=2*km
    bmin=max(lo,-((C-k*lo)//t)) # ceil((k*lo-C)/t)
    bmax=min(hi,(k*hi-C)//t)
    if bmin>bmax: return 0
    first=residue + ((bmin-residue+step-1)//step)*step
    if first>bmax: return 0
    n=(bmax-first)//step+1
    y=t*first+(1<<i)
    A=t*step
    bits=floor_sum(n,H,A,y)-2*floor_sum(n,2*H,A,y)
    assert 0<=bits<=n, (k,t,i,j,s,bits,n)
    return n-bits if s==1 else bits

def count_core(k,lo,hi,maxbit):
    tmax=(k*hi+(1<<maxbit)-1)//lo
    total=0; by_t={}
    for t in range(1,tmax+1):
        n=0
        for i in range(maxbit+1):
            for j in range(maxbit+1):
                if (t%2==1)!=((i==0)==(j==0)): continue
                n += count_branch(k,t,i,j,1,lo,hi)
                n += count_branch(k,t,i,j,-1,lo,hi)
        if n: by_t[t]=n
        total+=n
    return total,by_t

def brute_core(k,lo,hi,maxbit):
    total=0
    Q=range(lo,hi+1,2)
    for a in Q:
        for i in range(maxbit+1):
            for j in range(maxbit+1):
                D=(k*a^(1<<j))-(1<<i)
                if D<=0:continue
                for b in Q:
                    total+=D%b==0
    return total

def main():
    rng=random.Random(942)
    for _ in range(300):
        n=rng.randrange(1,20);m=rng.randrange(1,200)
        a=rng.randrange(0,500);b=rng.randrange(0,500)
        assert floor_sum(n,m,a,b)==sum((a*q+b)//m for q in range(n))
    print("floor_sum randomized pass")
    for k in (1,3,5,7,9,11,13):
        count,_=count_core(k,5,63,5)
        brute=brute_core(k,5,63,5)
        assert count==brute,(k,count,brute)
        print("small",k,count,brute)
    for k in (11,13,15,17):
        count,by_t=count_core(k,262145,524287,18)
        print("full",k,count,"by_t",json.dumps(by_t,sort_keys=True))
    print("ALL_EXACT_CHECKS_PASSED")

if __name__=="__main__":
    main()
