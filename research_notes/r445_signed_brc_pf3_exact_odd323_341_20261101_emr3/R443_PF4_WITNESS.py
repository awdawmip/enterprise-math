#!/usr/bin/env python3
"""Exact, independent 24-term Leibniz witnesses for order-four failure."""
from pathlib import Path
from math import comb, gcd
from functools import reduce, lru_cache
from itertools import permutations
import hashlib, sys

@lru_cache(maxsize=None)
def B(n,k): return comb(n,k) if 0<=k<=n else 0

def h_raw(r,s): return B(r+s,2*s)*sum(B(r-s,q)*(B(2*s,r-2*q)-B(2*s,r-2*q-1)) for q in range(r-s+1))
def det_perm(a,base):
    m=[[a[h] if 0<=h<len(a) else 0 for h in (base+j-i for j in range(4))] for i in range(4)]
    answer=0
    for p in permutations(range(4)):
        term=1
        for i,j in enumerate(p):term*=m[i][j]
        inversions=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        answer+=(-1 if inversions%2 else 1)*term
    return answer
base=Path(__file__).resolve().parent
rows=base.joinpath('R443_INPUTS.txt').read_text().splitlines()
out=[]
for line in rows:
    vs=list(map(int,line.split()));r,n=vs[:2];a=vs[2:]
    assert n==len(a)==r-1
    # Independent original signed BRC convolution.
    raw=[h_raw(r,r-j) for j in range(n)]
    common=reduce(gcd,raw)
    assert a==[v//common for v in raw]
    d=det_perm(a,r-3)
    assert d<0
    out.append(f'{r} rows=0,1,2,3 cols={r-3},{r-2},{r-1},{r} normalized_det={d} raw_det={d*(common**4)}')
joined='\n'.join(out)+'\n'
base.joinpath('R443_PF4_NEGATIVE_WITNESSES.txt').write_text(joined)
print('R443_PF4_WITNESS_PASS',len(rows),'sha256',hashlib.sha256(joined.encode()).hexdigest())
print('first',out[0][:130]);print('last',out[-1][:130])
