#!/usr/bin/env python3
"""Exact finite regression for RS-GEO6-FIRSTWAVE-ACCEPTED-PRIOR-ART-SYNTHESIS."""
from collections import deque
from itertools import combinations, permutations, product
from math import comb

checks = 0
def ck(x, msg):
    global checks
    if not x:
        raise AssertionError(msg)
    checks += 1

# S4 on the six 2-subsets of a four-set = Johnson scheme J(4,2).
pts = range(4)
s4 = list(permutations(pts))
axes = list(combinations(pts, 2))
idx = {e:i for i,e in enumerate(axes)}
seen, orbitals = set(), []
for pair in combinations(range(6), 2):
    if pair in seen:
        continue
    orb = set()
    for p in s4:
        a = idx[tuple(sorted((p[axes[pair[0]][0]], p[axes[pair[0]][1]])))]
        b = idx[tuple(sorted((p[axes[pair[1]][0]], p[axes[pair[1]][1]])))]
        orb.add(tuple(sorted((a,b))))
    seen |= orb
    orbitals.append(orb)
ck(sorted(map(len, orbitals)) == [3,12], "J(4,2) orbital sizes")
degrees = []
for orb in orbitals:
    d = [0]*6
    for a,b in orb:
        d[a] += 1; d[b] += 1
    ck(len(set(d)) == 1, "orbital regularity")
    degrees.append(d[0])
ck(sorted(degrees) == [1,4], "J(4,2) valencies")
ck(sorted({0,degrees[0],degrees[1],sum(degrees)}) == [0,1,4,5], "invariant degrees")

# Lee ball in Z^6.
def V6(r):
    return sum(2**j * comb(6,j) * comb(r,j) for j in range(7))
for r in range(5):
    direct = sum(1 for x in product(range(-r,r+1), repeat=6)
                 if sum(abs(a) for a in x) <= r)
    ck(direct == V6(r), f"Lee ball r={r}")
ck([V6(r) for r in range(5)] == [1,13,85,377,1289], "Lee regression")

# Hamming H(6,q): diameter six while q^6 grows.
for q in range(2,6):
    ds = {sum(a != 0 for a in v) for v in product(range(q), repeat=6)}
    ck(ds == set(range(7)), f"H(6,{q}) distances")
    ck(q**6 > 6, f"H(6,{q}) growth")

# Signed-shell separation.
def sep(patterns):
    ps = list(patterns)
    for k in range(1,5):
        for inds in combinations(range(len(ps)), k):
            chosen = [ps[i] for i in inds]
            if all({p[j] for p in chosen} == {-1,1} for j in range(6)):
                return k
    return None
allp = list(product((-1,1), repeat=6))
elementary = [p for p in allp if sum(x == -1 for x in p) in (0,2)]
even = [p for p in allp if sum(x == -1 for x in p) % 2 == 0]
ck(sep(elementary) == 3, "elementary separation")
ck(sep(even) == 2, "even separation")
ck(sep(allp) == 2, "full-sign separation")
ck(sep([(1,)*6]) is None, "sign-preserving no cover")

# K6 edge cover has size three.
rho = None
for k in range(1,4):
    for es in combinations(combinations(range(6),2), k):
        if len({v for e in es for v in e}) == 6:
            rho = k; break
    if rho is not None: break
ck(rho == 3, "K6 edge cover")

minus = (-1,)*6
ck(minus in even, "all-minus is even weight")
def flip(i,j):
    p = [1]*6; p[i] = p[j] = -1; return tuple(p)
def mul(a,b): return tuple(x*y for x,y in zip(a,b))
ck(mul(mul(flip(0,1),flip(2,3)),flip(4,5)) == minus, "global inversion")

# E6 from the frozen integral Gram matrix.
G = [
 [2,0,-1,0,0,0],
 [0,2,0,-1,0,0],
 [-1,0,2,-1,0,0],
 [0,-1,-1,2,-1,0],
 [0,0,0,-1,2,-1],
 [0,0,0,0,-1,2],
]
def gv(v):
    return [sum(G[i][j]*v[j] for j in range(6)) for i in range(6)]
def refl(v,i):
    w = list(v); w[i] -= gv(v)[i]; return tuple(w)
def inner(v,w):
    return sum(v[i]*G[i][j]*w[j] for i in range(6) for j in range(6))
roots = {(1,0,0,0,0,0)}
q = deque(roots)
while q:
    v = q.popleft()
    for i in range(6):
        w = refl(v,i)
        if w not in roots:
            roots.add(w); q.append(w)
ck(len(roots) == 72, "E6 root count")
ck(all(inner(v,v) == 2 for v in roots), "E6 norm")
deg = [sum(1 for w in roots if w != v and inner(v,w) == 1) for v in roots]
ck(set(deg) == {20}, "E6 contact degree")
ck(sum(deg)//2 == 720, "E6 contact edges")

print(f"PASS GEO6_FIRSTWAVE_ACCEPTED_PRIOR_ART_SYNTHESIS checks={checks}")
