#!/usr/bin/env python3
"""Exact complete W_s (signed C6, 720 words) kernel-vector coverage and counts.
No external dependencies; integer tuples, all assertions exact.
"""
from itertools import permutations, product

D = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))

def trace(word):
    out=[(0,0,0)]
    for direction in word:
        out.append(tuple(out[-1][i]+D[direction][i] for i in range(3)))
    assert out[-1] == out[0]
    return out

def simple_native(vertices):
    return len(vertices) == 7 and len(set(vertices[:-1])) == 6

def differences(vertices):
    p=vertices[:-1]
    return {tuple(p[i][axis]-p[j][axis] for axis in range(3))
            for i in range(6) for j in range(i+1,6)}

native_simple=[trace(w) for w in permutations(range(6)) if simple_native(trace(w))]
assert len(native_simple) == 192
all_differences=set().union(*(differences(v) for v in native_simple))
ternary_nonzero=set(product((-1,0,1),repeat=3))-{(0,0,0)}
assert all_differences == ternary_nonzero
assert len(all_differences) == 26

expected={(1,0,0):0, (1,1,0):48, (1,1,1):84, (2,1,0):192}
for k, exact_kept in expected.items():
    minus_k=tuple(-x for x in k)
    kept=sum(k not in differences(v) and minus_k not in differences(v)
             for v in native_simple)
    assert kept == exact_kept, (k,kept,exact_kept)
    print("primitive kernel", k, "preserved", kept, "lost", 192-kept)
print("PASS 720 signed words, 192 native-simple, complete 26-vector ternary coverage")
