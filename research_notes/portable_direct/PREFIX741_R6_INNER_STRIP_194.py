#!/usr/bin/env python3
"""PREFIX-741-R6. Exact BRC-Gamma inner-strip 194 reflected cells.
Frozen scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Usage: python PREFIX741_R6_INNER_STRIP_194.py [start_j end_j]
Without row arguments, checks the complete 97-cell upper set.
Standard library only; exact integer and fractions arithmetic.
"""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction as F
from math import comb
from hashlib import sha256
import json, sys

N, WD = 189, 1 << 18
# Exact candidate ranges (half-open i bounds), no corner touching diagonal.
RANGES = {40:(20,26),41:(20,29),42:(20,30),43:(20,30),
          44:(20,30),45:(20,30),46:(20,30),47:(21,30),
          48:(22,30),49:(24,30),50:(25,30),51:(26,30)}
EXPECTED_MIN_MICRO = {40:76822785,41:64435515,42:52351966,
    43:40623320,44:29297111,45:18416958,46:8022371,
    47:4306928,48:1234142,49:5198650,50:3439333,51:2260654}

@lru_cache(None)
def inside(n,k,x):
    return 40*(n+1)*comb(n,k)*x**k*(WD-x)**(n-k) > WD**n

@lru_cache(None)
def wide(n,k):
    if k > n//2: return wide(n,n-k)
    mid = k*WD//n
    assert inside(n,k,mid)
    if k == 0:
        lo=hi=0
    else:
        a,b=0,mid
        while b-a>1:
            x=(a+b)//2
            if inside(n,k,x): b=x
            else: a=x
        lo,hi=a,b
    a,b=mid,WD
    while b-a>1:
        x=(a+b)//2
        if inside(n,k,x): a=x
        else: b=x
    if 4*(a-hi)>WD: return True
    if 4*(b-lo)<WD: return False
    raise ArithmeticError("Frozen width undecided")

rows=[{0:1}]
for n in range(1,N+1):
    count=defaultdict(int)
    for k,v in rows[-1].items():
        count[k]+=v
        count[k+1]+=v
    rows.append({k:v for k,v in count.items() if wide(n,k)})
assert not rows[N] and sum(map(len,rows[:N]))==9529
for n,row in enumerate(rows[:N]):
    assert all(0<=v<=comb(n,k) for k,v in row.items())
    assert all(row.get(k,0)==row.get(n-k,0) for k in range(n+1))
    assert all(row.get(k+1,0)*comb(n,k)>=row.get(k,0)*comb(n,k+1)
               for k in range(n//2))

@lru_cache(maxsize=512)
def tails(q):
    a,b=q.numerator,q.denominator-q.numerator
    pa=[1];pb=[1]
    for _ in range(N):
        pa.append(pa[-1]*a)
        pb.append(pb[-1]*b)
    return (tuple(sum(v*pa[k]*pb[n-k] for k,v in row.items())*
                  q.denominator**(N-1-n) for n,row in enumerate(rows[:N])),
            q.denominator**(N-1))

C=[[comb(n+m,n)*2**(2*N-2-n-m) for m in range(N)] for n in range(N)]
Z=2**(2*N-1)

@lru_cache(maxsize=512)
def pair(p,z):
    t1,d1=tails(p);t2,d2=tails(z)
    a1,a2=sum(t1),sum(t2)
    b1=sum((n+1)*v for n,v in enumerate(t1))
    b2=sum((n+1)*v for n,v in enumerate(t2))
    cross0=cross1=0
    for n,x in enumerate(t1):
        if not x: continue
        for m,y in enumerate(t2):
            if not y: continue
            xy=x*y*C[n][m]
            cross0+=xy
            cross1+=(n+m+1)*xy
    D=d1*d2*Z
    mu=F((a1*d2+a2*d1)*Z-cross0,D)
    M2=F(2*(b1*d2+b2*d1)*Z-cross1,D)
    assert mu>=0 and M2>=mu*mu
    return mu,M2

emu, em2=pair(F(0),F(73,500))
eW=em2-emu*emu
oldmu, oldm2=pair(F(0),F(3,20))
oldW=oldm2-oldmu*oldmu
def dig(x): return sha256(str(x).encode("utf-8")).hexdigest()
# Existing frozen-prefix moment regressions, no scientific input rebasing.
assert dig(emu.numerator)=="797121e567e6422d342b2647cd17ff01187d5000b08bde8a954730d071bed46e"
assert dig(eW.numerator)=="814be93bb068b6a6e688e8ea5a466939a06e617b67ab585c177176f57afd57ae"

def endpoint_lower(i,j,split,di,dj,mu,W):
    a=F(split*i+di,384*split)
    b=F(split*j+dj,384*split)
    c=F(split*i+di+1,384*split)
    d=F(split*j+dj+1,384*split)
    L,_=pair(a,b)
    _,H=pair(c,d)
    t0=W-H+L*L
    return min(t0,t0-(mu-L)/2)

def lower_cell(i,j,split,mu,W):
    return min(endpoint_lower(i,j,split,di,dj,mu,W)
               for di in range(split) for dj in range(split))

def check_row(j):
    lo,hi=RANGES[j]
    rec=[]
    for i in range(lo,hi):
        g=lower_cell(i,j,2,emu,eW)
        assert g>1,(i,j,"frozen Gamma gap must exceed one")
        floor=(g*1000000).numerator//(g*1000000).denominator
        # Exact PREFIX-712 original 384-cell endpoint test.
        old=lower_cell(i,j,1,oldmu,oldW)
        assert old<=0,(i,j,"historical PREFIX-712 collision")
        rec.append([i,j,floor])
    assert min(v[2] for v in rec)==EXPECTED_MIN_MICRO[j],j
    return rec

def main():
    if len(sys.argv)==3:
        start,end=map(int,sys.argv[1:3])
    elif len(sys.argv)==1:
        start,end=40,52
    else: raise SystemExit("usage: checker.py [first_j last_j_exclusive]")
    assert 40<=start<end<=52
    got=[]
    for j in range(start,end):
        row=check_row(j)
        got.extend(row)
        print("PASS",j,"count",len(row),"min_micro",min(x[2] for x in row),flush=True)
        pair.cache_clear(); tails.cache_clear()
    if (start,end)==(40,52):
        assert len(got)==97
        assert min(x[2] for x in got)==1234142
        new={(i,j) for i,j,_ in got}
        mirror=new | {(j,i) for i,j in new}
        assert len(mirror)==194
        assert all(max(i,j)<=51 and min(i,j)>=20 for i,j in mirror)
        assert 141526+len(mirror)==141720
    print("ALL_CHECKS_PASS PREFIX741-R6",len(got), "upper cells")

if __name__=="__main__":main()
