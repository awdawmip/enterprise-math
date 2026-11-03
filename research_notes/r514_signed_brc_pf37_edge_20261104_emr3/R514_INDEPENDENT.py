#!/usr/bin/env python3
"""R514: independent exact signed-BRC 37x37 determinant check."""
import json
from math import comb
from sympy import Matrix
M=37
K_VALUES=[1,5,6,7,9,14,22,23,24,37]
def cb(n,k):
    return comb(n,k) if 0<=k<=n else 0
def cat(k):
    return cb(2*k,k)//(k+1)
def h_ballot(k,t):
    r=2*k+1
    if not (2<=t<=r): return 0
    return cb(r+t,2*t)*sum(cb(t-1,2*q)*(4**q)*cat(k-q) for q in range(min((t-1)//2,k)+1))
def h_signed(k,t):
    r=2*k+1
    if not (2<=t<=r): return 0
    return cb(r+t,2*t)*sum(cb(r-t,q)*(cb(2*t,r-2*q)-cb(2*t,r-2*q-1)) for q in range(r-t+1))
crosscheck=0
for k in range(1,21):
    for t in range(2,M+2):
        assert h_ballot(k,t)==h_signed(k,t),(k,t)
        crosscheck+=1
checks=[]
for k in K_VALUES:
    mat=Matrix(M,M,lambda i,j:h_ballot(k,3+i-j))
    d=mat.det(method='berkowitz')
    s=1 if d>0 else -1 if d<0 else 0
    expected=1 if k<=5 or 7<=k<=22 else -1
    assert s==expected,(k,s,expected)
    checks.append({'k':k,'sign':s,'digits':len(str(abs(d))),'residue_mod_1000000007':int(d%1000000007)})
print(json.dumps({'status':'R514_INDEPENDENT_PASS','method':'SymPy Berkowitz direct 37x37 integer determinant, independently constructed ballot/Catalan H; raw signed H crosscheck','crosscheck_count':crosscheck,'checks':checks},indent=2))
