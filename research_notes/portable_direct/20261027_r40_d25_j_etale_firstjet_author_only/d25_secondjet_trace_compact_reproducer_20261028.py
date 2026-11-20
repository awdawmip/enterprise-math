#!/usr/bin/env python3
"""Auxiliary finite-field odd-square trace witness; Python stdlib only."""
from itertools import product
import json

def mat(x): return [x[:2],x[2:]]
def mm(X,Y,p): return [[sum(X[i][k]*Y[k][j] for k in range(2))%p for j in range(2)] for i in range(2)]
def diff(X,Y,p): return [[(X[i][j]-Y[i][j])%p for j in range(2)] for i in range(2)]
def cm(B,A,p): return diff(mm(B,A,p),mm(A,B,p),p)
def tr(X): return X[0][0]+X[1][1]
def zero(M,p): return all(t%p==0 for row in M for t in row)

checks=0
for p in (3,5):
    As=product(range(p),repeat=4) if p==3 else ([0,0,0,0],[0,0,0,1],[1,1,0,1],[0,1,1,0],[0,1,4,0],[0,1,1,1])
    for a in As:
        A=mat(a)
        images={tuple(z for row in cm(mat(b),A,p) for z in row) for b in product(range(p),repeat=4)}
        scalar=(A[0][1]==A[1][0]==0 and A[0][0]==A[1][1])
        assert len(images)==(1 if scalar else p*p)
        for k in product(range(p),repeat=4):
            K=mat(k)
            feasible=(zero(K,p) if scalar else tr(K)%p==0 and tr(mm(A,K,p))%p==0)
            assert feasible==(k in images)
            checks+=1
p=373
A=[[0,0],[0,1]]; B=[[0,1],[0,0]]
K=cm(B,A,p)
assert K==B and tr(K)%p==0 and tr(mm(A,K,p))%p==0
assert tr([[1,0],[0,1]])%p==2
assert tr(mm(A,[[1,0],[0,p-1]],p))%p==p-1
print(json.dumps({'verification':'PASS','case_checks':checks,'exact_scope':'all 2x2 A and K over F3, 6 A and all K over F5, p373 witness','p373':{'A':A,'B':B,'K':K,'preimages':p*p},'classification':'AUTHOR_ONLY_NOT_NATIVE_NOT_ADMITTED'},sort_keys=True))
