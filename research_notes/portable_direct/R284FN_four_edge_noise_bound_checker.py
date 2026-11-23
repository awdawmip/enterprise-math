#!/usr/bin/env python3
"""Finite integer crosschecks for R284FN, not a replacement for the all-q,u proof."""
from itertools import combinations
from math import comb

A, B = (2,3,6,7), (1,3,4,6)
AA = ((2,3),(2,6),(3,7),(6,7))
BB = ((1,3),(1,6),(3,4),(4,6))
D = ((1,3,5,7),(2,3,6,7),(4,5,6,7),
     (1,2,5,6),(1,3,4,6),(2,3,4,5))

def parts(n,k):
    if k==1:
        yield (n,)
    else:
        for i in range(n+1):
            for tail in parts(n-i,k-1):
                yield (i,)+tail

def sep(x, modes, adj, q, u):
    return (any(x[p]>2*q+2*u for p in modes)
       or any(x[p]+x[t]>3*q+2*u for p,t in adj)
       or sum(x[p] for p in modes)>4*q+2*u)

count=0
for q in range(4):
    for u in range(2):
        n=4*q+3*u+1
        total=0
        for xs in parts(n,7):
            x=(0,)+xs
            if (all(sum(x[p] for p in d)>=2*(q+u)+1 for d in D)
                and sep(x,A,AA,q,u) and sep(x,B,BB,q,u)):
                raise AssertionError((q,u,n,x))
            total+=1
        assert total==comb(n+6,6)
        count+=total
        print(f'q={q} u={u} n={n} checked={total} passed')
print('TOTAL',count)
assert count==128996
