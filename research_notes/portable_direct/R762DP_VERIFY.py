#!/usr/bin/env python3
"""Exact integer BRC tests for R762DP; no floats or external dependencies."""
from math import gcd
from functools import reduce
import json

BRANCHES = ((0, 0, 1), (1, 0, 2), (0, 1, 2), (1, 1, 1))

def advance(hist, q):
    nxt = [[0] * q for _ in range(q)]
    for x in range(q):
        for z in range(q):
            v = hist[x][z]
            if v == 0: continue
            for dx, dz, w in BRANCHES:
                nxt[(x+dx)%q][(z+dz)%q] += w * v
    return nxt

def content(hist):
    return reduce(gcd, (v for row in hist for v in row), 0)

def expected(q, n):
    d = q // 3
    if n < q: return 1
    if n < q + 2*d: return 9
    if 2*q <= n < 2*q + d: return 81
    return None

def check(q, end):
    hist = [[0] * q for _ in range(q)]
    hist[0][0] = 1
    points, checked = {}, 0
    picks = {1,q-1,q,q+1,q+2*(q//3)-1,q+2*(q//3),2*q-1,2*q,2*q+q//3-1,2*q+q//3}
    for n in range(1,end+1):
        hist = advance(hist,q)
        c = content(hist)
        want = expected(q,n)
        if want is not None:
            assert c == want,(q,n,c,want)
            checked += 1
        assert sum(map(sum,hist)) == 6**n, (q,n,'mass')
        if n in picks: points[str(n)]=str(c)
        if n==q:
            d=q//3
            assert all((hist[x][z]//9) % 3 == (1 if x==d and z==d or x==2*d and z==2*d else 2 if (x==d and z==2*d or x==2*d and z==d) else 0) for x in range(q) for z in range(q)), (q,'D')
    return {'q':q,'n_range':[1,end],'theorem_checks':checked,'sample_contents':points,'full_mass_checks':end,'frobenius_D_check':True}

if __name__=='__main__':
    rs=[check(9,21),check(27,63),check(81,189)]
    print(json.dumps({'status':'PASS','method':'exact Python integer positive BRC 2-coordinate cyclic convolution','results':rs},indent=2,ensure_ascii=False))
