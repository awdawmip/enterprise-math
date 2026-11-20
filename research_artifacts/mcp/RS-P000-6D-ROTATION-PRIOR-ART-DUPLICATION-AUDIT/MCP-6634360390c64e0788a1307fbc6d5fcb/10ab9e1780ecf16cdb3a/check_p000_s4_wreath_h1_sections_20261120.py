#!/usr/bin/env python3
"""Exact finite check: 16 split S4 wreath sections, two C2^4 orbits of size 8.
This verifies a declared finite classical semidirect model; not native Full-Cell.
"""
from itertools import permutations, product

P = list(permutations(range(4)))
E = tuple(range(4))
Z = (0, 0, 0, 0)
A = list(product((0, 1), repeat=4))

def composition(p, q):
    return tuple(p[q[i]] for i in range(4))

def cycle(*seq):
    p = list(E)
    for i, j in zip(seq, seq[1:] + seq[:1]):
        p[i] = j
    return tuple(p)

def permute(p, v):
    return tuple(v[p.index(i)] for i in range(4))

def xor(v, w):
    return tuple(x ^ y for x, y in zip(v, w))

def multiply(x, y):
    v, p = x
    w, q = y
    return xor(v, permute(p, w)), composition(p, q)

identity = (Z, E)

def power(x, n):
    result = identity
    for _ in range(n):
        result = multiply(result, x)
    return result

a = cycle(1, 2, 3)
b = cycle(0, 1)
assert power((Z,a), 3) == identity
assert power((Z,b), 2) == identity
assert power(multiply((Z,a), (Z,b)), 4) == identity

sections = set()
for va in A:
    for vb in A:
        ra, rb = (va, a), (vb, b)
        if (power(ra,3) == identity and power(rb,2) == identity
            and power(multiply(ra,rb),4) == identity):
            sections.add((va,vb))
assert len(sections) == 16, len(sections)

orbits = []
remaining = set(sections)
while remaining:
    va, vb = next(iter(remaining))
    orbit = set()
    for v in A:
        c_a = multiply(multiply((v,E),(va,a)),(v,E))[0]
        c_b = multiply(multiply((v,E),(vb,b)),(v,E))[0]
        orbit.add((c_a,c_b))
    assert orbit <= sections
    remaining -= orbit
    orbits.append(orbit)
assert sorted(map(len,orbits)) == [8,8], sorted(map(len,orbits))
print("PASS |S4|=24, |A|=16, exact generator-lift pairs=256")
print("PASS homomorphic sections=16, A-conjugacy orbits=2, sizes=8+8")
