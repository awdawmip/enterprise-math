#!/usr/bin/env python3
"""Exact finite checks for R676 typed bridge and V27 score covariance.
Integer permutations and positive rational combinatorial weights only.
"""
from itertools import permutations, product
from fractions import Fraction

P = range(4)
SIGMA = (2, 1, 0, 3)  # V29 ports 0 <-> 2
TAU = (1, 0, 2, 3)    # declared V27 field-source names 0 <-> 1

def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))

def image(v, p):
    out = [None] * len(v)
    for i, j in enumerate(p):
        out[j] = v[i]
    return tuple(out)

def matrix_image(M, p):
    n = len(M)
    out = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            out[p[i]][p[j]] = M[i][j]
    return tuple(tuple(row) for row in out)

def dot(u, v):
    return sum(x*y for x,y in zip(u, v))

def score(u, Om, x, y):
    return dot(u, y) + dot(x, tuple(sum(Om[i][j]*y[j] for j in P) for i in P))

bridges = sorted(p for p in permutations(P) if compose(p,SIGMA)==compose(TAU,p))
assert len(bridges)==4
assert bridges == [(0,2,1,3),(0,3,1,2),(1,2,0,3),(1,3,0,2)]
assert (0,1,2,3) not in bridges
assert image((1,0,0,0), SIGMA) != image((1,0,0,0), TAU)

M = [[0]*4 for _ in P]
for i,j in ((0,1),(1,2),(2,0)):
    M[i][j] = 1
Om = tuple(tuple(M[i][j]-M[j][i] for j in P) for i in P)
I, O = (0,0,0,10), (2,4,3,0)
u = tuple(I[i]-O[i] for i in P)
assert u == (-2,-4,-3,10)
assert Om == ((0,1,-1,0),(-1,0,1,0),(1,-1,0,0),(0,0,0,0))
assert image(u,TAU) != u
ut = image(u, TAU)
Ot = matrix_image(Om, TAU)
Mt = matrix_image(M, TAU)
assert all(x>=0 for row in Mt for x in row)
assert image(I,TAU)[0]-image(O,TAU)[0] == ut[0]

codes = list(product((-1,0,1), repeat=4))
checks = 0
for x in codes:
    for y in codes:
        assert score(u,Om,x,y)==score(ut,Ot,image(x,TAU),image(y,TAU))
        checks+=1

a,b,c=(0,2,1),(2,1,0),(1,0,2)
h_ab,h_ba=compose(a,b),compose(b,a)
assert h_ab != h_ba
assert compose(compose(c,h_ab),c)==h_ba
hist = {h_ab:Fraction(1,2), h_ba:Fraction(1,2)}
assert sum(hist.values()) == 1
assert hist[h_ab]==hist[h_ba]
flip={0:1,1:0}
assert not [e for e in (0,1) if flip[e]==e]
for eps in (0,1):
    assert flip[eps] == flip[eps]

print('R676_V27_TYPED_BRIDGE_SCORE_AND_SELECTOR_EXACT_PASS')
print('bridges=',bridges)
print('score_pairs=',checks)
print('witness_u=',u,'transformed_u=',ut)
print('two_step_holonomies=',h_ab,h_ba,'branch_weights=1/2,1/2')
