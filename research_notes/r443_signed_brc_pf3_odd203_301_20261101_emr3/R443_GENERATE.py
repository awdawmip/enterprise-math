#!/usr/bin/env python3
"""Reproducible exact signed BRC coefficient construction from independent convolution identities."""
from math import comb, gcd
from functools import reduce, lru_cache
from pathlib import Path
import sys, hashlib

@lru_cache(maxsize=None)
def B(n,k): return comb(n,k) if 0<=k<=n else 0

def raw(r,s):
    return B(r+s,2*s)*sum(B(r-s,q)*(B(2*s,r-2*q)-B(2*s,r-2*q-1)) for q in range(r-s+1))

def catalan(r,s):
    k=(r-1)//2
    return B(r+s,2*s)*sum(B(s-1,2*q)*4**q*(B(2*(k-q),k-q)//(k-q+1)) for q in range(min(k,(s-1)//2)+1))

lo=int(sys.argv[1]) if len(sys.argv)>1 else 203
hi=int(sys.argv[2]) if len(sys.argv)>2 else 301
rows=[];eq_count=0
for r in range(lo,hi+1,2):
    assert r%2==1 and r>=5
    nums=[]
    for s in range(r,1,-1):
        a,b=raw(r,s),catalan(r,s)
        assert a==b and a>0,(r,s,a,b)
        nums.append(a);eq_count+=1
    g=reduce(gcd,nums)
    nums=[x//g for x in nums]
    assert len(nums)==r-1
    rows.append(str(r)+' '+str(len(nums))+' '+' '.join(map(str,nums)))
output='\n'.join(rows)+'\n'
out_path=Path(__file__).with_name('R443_INPUTS.txt')
out_path.write_text(output)
print('R443_INPUT_PASS',len(rows),eq_count,len(output.encode()),hashlib.sha256(output.encode()).hexdigest())
