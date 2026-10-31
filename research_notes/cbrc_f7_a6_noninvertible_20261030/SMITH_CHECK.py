#!/usr/bin/env python3
"""Exact regression for fixed-scalar F7 A6 minimum-index Smith type.
Universal proof is in SMITH_COKERNEL.md; this checks all 16*16 matrices.
"""
from itertools import combinations, permutations, product
from math import gcd
import json
D=((1,1,0,0),(1,-1,0,0),(0,0,1,1),(0,0,1,-1))
def mul(X,Y):
    return tuple(tuple(sum(x*z for x,z in zip(row,col)) for col in zip(*Y)) for row in X)
def det(X):
    if len(X)==1: return X[0][0]
    return sum((-1)**j*X[0][j]*det(tuple(tuple(row[k] for k in range(len(X)) if k!=j) for row in X[1:])) for j in range(len(X)))
def divisors(A):
    return tuple(gcd(*[abs(det(tuple(tuple(A[i][j] for j in cs) for i in rs)))
           for rs in combinations(range(4),r) for cs in combinations(range(4),r)])
           for r in range(1,5))
seen=set()
for p in permutations(range(4)):
    if p[0]//2==p[1]//2: continue
    for signs in product((-1,1), repeat=4):
        T=tuple(tuple(signs[j] if i==p[j] else 0 for j in range(4)) for i in range(4))
        A=mul(mul(D,T),D)
        assert all(abs(x)==1 for row in A for x in row)
        assert mul(tuple(zip(*A)),A)==tuple(tuple(4 if i==j else 0 for j in range(4)) for i in range(4))
        assert divisors(A)==(1,2,4,16)
        seen.add(A)
assert len(seen)==256
print(json.dumps({"status":"PASS","coverage":"16 split permutations x 16 signs","matrices":256,"distinct":256,"gcd_minors":[1,2,4,16],"smith_invariants":[1,2,2,4]},indent=2))
