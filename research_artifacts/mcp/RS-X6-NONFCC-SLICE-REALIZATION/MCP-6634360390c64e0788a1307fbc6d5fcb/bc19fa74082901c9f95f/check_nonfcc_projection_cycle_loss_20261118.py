#!/usr/bin/env python3
"""Exact bounded native/triangular-quotient simplicity classification."""
from itertools import permutations
D=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
def trace(word):
    z=[0,0,0];out=[tuple(z)]
    for s in word:
        for j in range(3): z[j]+=D[s][j]
        out.append(tuple(z))
    return out
def simple(vertices):
    return vertices[-1]==vertices[0] and len(set(vertices[:-1]))==len(vertices)-1
def proj(v): return (v[0]-v[2],v[1]-v[2])
counts={(True,True):0,(True,False):0,(False,True):0,(False,False):0}
for w in permutations(range(6)):
    native=trace(w)
    quotient=[proj(v) for v in native]
    counts[(simple(native),simple(quotient))]+=1
assert counts=={(True,True):84,(True,False):108,(False,True):0,(False,False):528}
w=(0,2,4,1,3,5)
assert simple(trace(w)) and not simple([proj(v) for v in trace(w)])
print("PASS: 720 words; 84 carrier-simple native loops, 108 native-simple projected losses, 528 non-simple")
