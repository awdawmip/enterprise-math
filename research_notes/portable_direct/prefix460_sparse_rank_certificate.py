#!/usr/bin/env python3
"""PREFIX-460 exact, deterministic, sparse modular witness.
Requires Python 3.10+ and numpy. Use --m/--t to bound runtime.
Scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Analytic upper bound: PREFIX-459 (read companion manuscript).
"""
import argparse
from functools import lru_cache
from collections import defaultdict
from hashlib import sha256
from math import comb, isqrt
import numpy as np

PRIMES=(32003,32009)
@lru_cache(None)
def vs(n,d):
    if d==0:return ((),)
    return tuple((i,)+v for i in range(n+1) for v in vs(n-i,d-1))
def rows(m,t):
    return tuple((s,a) for s in range(m+1) for a in vs(m-s,5)
        if (m-s-sum(a))%2==0 and all(a[i]>0 for i in range(t)))
def cols(m,t):
    return tuple((b,c) for b in range(m+2-t)
        for c in vs((m+1-t-b)//2,5)
        if b+2*sum(c)+t<=m+1)
def sample(m,t,R,c):
    k=min(len(R),max(c+25,(101*c+99)//100))
    B=defaultdict(list)
    for s,a in R:B[(s,sum(a))].append((s,a))
    keys=sorted(B)
    for key in keys:
        B[key].sort(key=lambda row:(sha256(
            (f'{m}|{t}|{row[0]}|'+','.join(map(str,row[1]))).encode('ascii')
        ).digest(),row))
    ids={key:0 for key in keys};out=[]
    while len(out)<k:
        progress=False
        for key in keys:
            p=ids[key]
            if p<len(B[key]):
                out.append(B[key][p]);ids[key]+=1;progress=True
                if len(out)>=k:break
        assert progress
    return tuple(out)
def matrix(S,C,m,p):
    A=np.empty((len(S),len(C)),dtype=np.int64)
    for i,(s,a) in enumerate(S):
        sp=[pow(s,j,p) for j in range(m+2)]
        ap=[[pow(x,2*j,p) for j in range((m+1)//2+1)] for x in a]
        for j,(b,c) in enumerate(C):
            z=sp[b]
            for h,v in enumerate(c):z=z*ap[h][v]%p
            A[i,j]=z
    return A
def rank(A,p):
    r=0
    for j in range(A.shape[1]):
        if r==A.shape[0]:break
        nz=np.flatnonzero(A[r:,j])
        if not len(nz):continue
        k=r+int(nz[0])
        if k!=r:A[[r,k],j:]=A[[k,r],j:]
        A[r,j:]=A[r,j:]*pow(int(A[r,j]),-1,p)%p
        inds=np.flatnonzero(A[r+1:,j])+r+1
        if len(inds):
            A[inds,j:]=(A[inds,j:]-A[inds,j:j+1]*A[r,j:])%p
        r+=1
    return r
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--m',type=int,choices=range(10,14))
    ap.add_argument('--t',type=int,choices=range(6))
    a=ap.parse_args()
    if a.t is not None and a.m is None:ap.error('--t requires --m')
    for p in PRIMES:assert all(p%i for i in range(2,isqrt(p)+1)) and p*p<2**63
    for m in ([a.m] if a.m is not None else range(10,14)):
        B=comb(m+7,6); total=0;Ctot=0
        for t in ([a.t] if a.t is not None else range(6)):
            R,C=rows(m,t),cols(m,t);S=sample(m,t,R,len(C))
            result=[rank(matrix(S,C,m,p),p) for p in PRIMES]
            defect=max(0,(m-t+3)//2)
            assert result==[len(C)-defect]*2,(m,t,result)
            total+=comb(5,t)*result[0];Ctot+=comb(5,t)*len(C)
            print(f'm={m} t={t} full={len(R)} selected={len(S)} cols={len(C)} ranks={result} defect={defect} PASS',flush=True)
        if a.t is None:
            assert Ctot==B and total==B-16*m
            print(f'd={m+1} q>={m+1}: R(q)={B}*q-{16*m} PASS',flush=True)
if __name__=='__main__':main()
