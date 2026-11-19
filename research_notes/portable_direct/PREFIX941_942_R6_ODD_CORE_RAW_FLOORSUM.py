#!/usr/bin/env python3
"""Exact O(log(2^j)) per (k,i,j,t,sign) raw-witness counter.
Public mathematical auxiliary observer; no private data or credentials.
"""
from math import gcd
import json, sys
L,U=262145,524287

def ceildiv(a,b):
    assert b>0
    return -(-a//b)

def floor_sum_unsigned(n,m,a,b):
    # Sum_{0<=i<n} floor((a*i+b)/m). a,b >=0, m>=1.
    ans=0
    while True:
        if a>=m:
            ans+=(n-1)*n*(a//m)//2
            a%=m
        if b>=m:
            ans+=n*(b//m)
            b%=m
        y=a*n+b
        if y<m:break
        n=y//m
        b=y%m
        m,a=a,m
    return ans

def count_bit_ones(start,step,n,j):
    assert start>=0 and step>=0
    if n<=0:return 0
    return floor_sum_unsigned(n,1<<j,step,start)-2*floor_sum_unsigned(n,1<<(j+1),step,start)

def count_cell(k,i,j,t,e):
    # e=+1 for bit 0, -1 for bit 1
    c=(1<<i)-e*(1<<j)
    g=gcd(k,t)
    if c%g:return 0
    t1=t//g; k1=k//g; c1=c//g
    a0=(pow(k1,-1,t1)*c1)%t1 if t1>1 else 0
    b0=(k*a0-c)//t
    p=(1-b0)%2
    if (a0+t1*p)%2!=1:return 0
    A=a0+t1*p
    B=b0+k1*p
    sa=2*t1; sb=2*k1
    low=max(ceildiv(L-A,sa),ceildiv(L-B,sb))
    high=min((U-A)//sa,(U-B)//sb)
    if high<low:return 0
    n=high-low+1
    base=k*(A+sa*low)
    bitones=count_bit_ones(base,k*sa,n,j)
    return n-bitones if e==1 else bitones

def compute(k, tmax=None):
    assert k%2==1 and k>0
    if tmax is None:tmax=(k*U+(1<<18))//L
    raw_by_t=[0]*tmax
    by_j=[[0]*19 for _ in range(19)]
    for i in range(19):
        for j in range(19):
            for t in range(1,tmax+1):
                v=count_cell(k,i,j,t,+1)+count_cell(k,i,j,t,-1)
                raw_by_t[t-1]+=v;by_j[i][j]+=v
    return {"k":k,"tmax":tmax,"total_raw_witnesses":sum(raw_by_t),"raw_by_t":raw_by_t,"by_ij":by_j}

def naive_cell(k,i,j,t,e):
    n=0
    for a in range(L,U+1,2):
        x=k*a
        bit=(x>>j)&1
        if bit!=(e<0):continue
        d=(x^(1<<j))-(1<<i)
        if d==t*((d//t)) and d%t==0 and L<=d//t<=U and d//t%2==1:n+=1
    return n

if __name__=='__main__':
    for k in (3,11,13,15):
        r=compute(k)
        print(k, r['total_raw_witnesses'],r['raw_by_t'], flush=True)
        with open(f'/mnt/data/PREFIX941_RAW_SIEVE_K{k}.json','w') as f:json.dump(r,f,sort_keys=True)
    # independent small samples using exhaustive odd a: ensure floor-sum count exact
    cases=[(3,0,2,1,+1),(3,17,7,5,-1),(11,18,18,16,+1),(11,0,17,6,-1),(13,8,6,5,+1),(13,1,17,16,-1),(15,0,0,1,+1)]
    print('spot checks:',[(c,count_cell(*c),naive_cell(*c)) for c in cases])
