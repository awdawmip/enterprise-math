#!/usr/bin/env python3
"""Portable, exact signed-BRC input generation; checks both independent formulas."""
from math import comb,gcd
from functools import reduce
from pathlib import Path
import hashlib

ROOT=Path(__file__).resolve().parent

def B(n,k): return comb(n,k) if 0<=k<=n else 0

def Hraw(r,s):
    return B(r+s,2*s)*sum(B(r-s,q)*(B(2*s,r-2*q)-B(2*s,r-2*q-1)) for q in range(r-s+1))

def Hcat(r,s):
    k=(r-1)//2
    return B(r+s,2*s)*sum(B(s-1,2*q)*4**q*B(2*(k-q),k-q)//(k-q+1) for q in range(min(k,(s-1)//2)+1))

rows=[];count=0
for r in range(99,202,2):
    values=[]
    for s in range(r,1,-1):
        c=Hcat(r,s)
        assert c==Hraw(r,s),(r,s)
        assert c>0,(r,s)
        values.append(c)
        count+=1
    g=reduce(gcd,values)
    a=[v//g for v in values]
    rows.append(f'{r} {len(a)} '+' '.join(map(str,a)))
raw=('\n'.join(rows)+'\n').encode()
(ROOT/'R442_INPUTS.txt').write_bytes(raw)
print('R442_INPUT_PASS rows=',len(rows),'coeffs=',count,'bytes=',len(raw),'sha256=',hashlib.sha256(raw).hexdigest())
