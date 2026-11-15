#!/usr/bin/env python3
"""Portable exact Gaussian residual-fiber discovery for one signed X6 Z^3 slice.

Independent C4-style construction; NOT the original R063 Stage0 checker or its
512-case regression. A brute verifier is called only AFTER discovery is hashed.
"""
from __future__ import annotations
from collections import Counter
from functools import lru_cache
from hashlib import sha256
from math import comb, factorial, isqrt
import json


def factors(n: int):
    assert n >= 1
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            out.append((p, e))
        p = 3 if p == 2 else p + 2
    if n > 1:
        out.append((n, 1))
    return out


def gmul(x, y):
    a, b = x
    c, d = y
    return (a*c-b*d, a*d+b*c)


def gpow(z, k):
    out = (1, 0)
    for _ in range(k):
        out = gmul(out, z)
    return out


@lru_cache(None)
def two_squares_factorization(n: int):
    """Every signed ordered Gaussian integer pair of norm n, by prime allocation."""
    assert n >= 0
    if n == 0:
        return ((0, 0),)
    options = {(1, 0)}
    scalar = 1
    for p, e in factors(n):
        if p % 4 == 3:
            if e & 1:
                return ()
            scalar *= p ** (e // 2)
        elif p == 2:
            scalar_g = gpow((1, 1), e)
            options = {gmul(z, scalar_g) for z in options}
        else:
            assert p % 4 == 1
            # Prime split only. Never search a^2+b^2=n at the target norm.
            ab = next(((a, isqrt(p-a*a)) for a in range(1, isqrt(p)+1)
                       if a*a <= p and isqrt(p-a*a)**2 == p-a*a
                       and isqrt(p-a*a)>0), None)
            assert ab is not None, (p, e)
            pi, bar = ab, (ab[0], -ab[1])
            options = {gmul(z, gmul(gpow(pi, j), gpow(bar, e-j)))
                       for z in options for j in range(e+1)}
    units = ((1,0),(-1,0),(0,1),(0,-1))
    answer = sorted({gmul(u, (scalar*z[0],scalar*z[1]))
                     for u in units for z in options})
    assert all(a*a+b*b==n for a,b in answer)
    return tuple(answer)


def words(a,b,c):
    x,y,z=abs(a),abs(b),abs(c)
    # BRC decomposition: first shuffle two components, then insert the third.
    return comb(x+y,x)*comb(x+y+z,z)


def discovery(N):
    assert N>=0
    R=isqrt(N)
    cs=[]
    points=[]
    for c in range(-R,R+1):
        M=N-c*c
        pairs=two_squares_factorization(M)
        if pairs:
            cs.append((c,M,len(pairs)))
            points.extend((a,b,c) for a,b in pairs)
    assert len(points)==len(set(points))
    assert all(a*a+b*b+c*c==N for a,b,c in points)
    return tuple(sorted(points)),tuple(cs)


def brute_verify(N):
    R=isqrt(N)
    return {(a,b,c) for a in range(-R,R+1) for b in range(-R,R+1)
            for c in range(-R,R+1) if a*a+b*b+c*c==N}


def run(N):
    pts, layers=discovery(N)
    digest=sha256(json.dumps(pts,separators=(',',':')).encode()).hexdigest()
    # Independent verification is downstream of frozen discovered bytes/digest.
    assert set(pts)==brute_verify(N)
    mass=sum(words(*p) for p in pts)
    support=Counter(sum(x!=0 for x in p) for p in pts)
    per_layer=[]
    for c,M,n in layers:
        group=[p for p in pts if p[2]==c]
        assert len(group)==n
        per_layer.append({'c':c,'residual':M,'pairs':n,'BRC_mass':str(sum(words(*p) for p in group))})
    return {'N':N,'count':len(pts),'mass':str(mass),
            'support':dict(sorted(support.items())),
            'snapshot_SHA256':digest,'layers':per_layer}


def main():
    # Validation sources do not feed discovery.
    a=run(25)
    b=run(2500)
    assert (a['count'],a['mass'])==(30,'846')
    assert b['count']==150
    assert b['mass']=='26860799510260072787603759892561716013678'
    assert b['support']=={1:6,2:48,3:96}
    abs_c={abs(row['c']) for row in b['layers']}
    assert abs_c=={0,14,18,24,30,32,40,48,50},abs_c
    assert len(b['layers'])==17
    assert b['layers']==list(sorted(b['layers'],key=lambda r:r['c']))
    print('PASS_X6_GAUSSIAN_RESIDUAL_FIBER_NATIVE_SIGNED_Z3_NOT_ORIGINAL_R063')
    print(json.dumps({'N25':{'count':a['count'],'mass':a['mass'],'sha':a['snapshot_SHA256']},
                      'N2500':b},ensure_ascii=False,separators=(',',':')))


if __name__=='__main__':
    main()
