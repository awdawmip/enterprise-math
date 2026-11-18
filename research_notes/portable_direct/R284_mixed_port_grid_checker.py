#!/usr/bin/env python3
"""Exact Fraction certificate for scoped R284 labeled BRC Port mixed grids.

Finite tests support, but do not replace, the determinant/interpolation proof.
"""
from fractions import Fraction as Q
from itertools import permutations, product
from random import Random
import json


def add(a, b):
    o = dict(a)
    for k, v in b.items():
        o[k] = o.get(k, Q(0)) + v
        if not o[k]:
            del o[k]
    return o


def mul(a, b):
    o = {}
    for p, v in a.items():
        for q, w in b.items():
            k = tuple(x + y for x, y in zip(p, q))
            o[k] = o.get(k, Q(0)) + v*w
    return {k: v for k, v in o.items() if v}


def det(a, m):
    n = len(a)
    zero = (0,)*m
    if not n:
        return {zero: Q(1)}
    o = {}
    for p in permutations(range(n)):
        inversions = sum(p[i] > p[j] for i in range(n) for j in range(i+1, n))
        prod = {zero: Q(-1 if inversions % 2 else 1)}
        for i in range(n):
            prod = mul(prod, a[i][p[i]])
        o = add(o, prod)
    return o


def matrix_poly(n, w, edits):
    m = len(edits)
    z = (0,)*m
    a = [[{z: Q(i == j) - w[i][j]} for j in range(n)] for i in range(n)]
    for k, (u, v) in enumerate(edits):
        e = tuple(int(i == k) for i in range(m))
        a[u][v] = add(a[u][v], {e: Q(-1)})
    return a


def numerator_denominator(n, w, edits, output):
    a = matrix_poly(n, w, edits)
    m = len(edits)
    d = det(a, m)
    row, col = output[1], output[0]
    minor = [[a[i][j] for j in range(n) if j != col] for i in range(n) if i != row]
    num = det(minor, m)
    if (row + col) % 2:
        num = {k:-v for k,v in num.items()}
    return num, d


def inverse(w):
    n = len(w)
    a = [[Q(i == j)-w[i][j] for j in range(n)] + [Q(i == j) for j in range(n)] for i in range(n)]
    for i in range(n):
        r = next(j for j in range(i, n) if a[j][i] != 0)
        a[i], a[r] = a[r], a[i]
        div = a[i][i]
        a[i] = [v/div for v in a[i]]
        for j in range(n):
            if i != j:
                fac = a[j][i]
                a[j] = [x-fac*y for x,y in zip(a[j], a[i])]
    return [row[n:] for row in a]


def cycle_vertices(w, edits):
    s = inverse(w)
    m = len(edits)
    reach = [[s[edits[i][1]][edits[j][0]] != 0 for j in range(m)] for i in range(m)]
    for k in range(m):
        for i in range(m):
            for j in range(m):
                reach[i][j] |= reach[i][k] and reach[k][j]
    return {i for i in range(m) if reach[i][i]}


def eval_observer(n, w, edits, output, weights):
    v = [list(row) for row in w]
    for (u, t), x in zip(edits, weights):
        v[u][t] += x
    assert max(map(sum, v)) < 1
    return inverse(v)[output[0]][output[1]]


def val_p(x, p):
    if x == 0:
        return None
    a, b = abs(x.numerator), x.denominator
    out = 0
    while a % p == 0:
        out += 1
        a //= p
    while b % p == 0:
        out -= 1
        b //= p
    return out


def kappa(nodes, p):
    return max(sum(val_p(nodes[i]-nodes[j],p) for j in range(len(nodes)) if j != i) for i in range(len(nodes)))


def from_edges(n, edges):
    w = [[Q(0) for _ in range(n)] for _ in range(n)]
    for a,b,x in edges:
        w[a][b] += Q(x)
    return w


def check_models(w1, w2, edits, output):
    n, m = len(w1), len(edits)
    n1,d1 = numerator_denominator(n,w1,edits,output)
    n2,d2 = numerator_denominator(n,w2,edits,output)
    cross = add(mul(n1,d2),{k:-v for k,v in mul(n2,d1).items()})
    cyc = cycle_vertices(w1,edits) | cycle_vertices(w2,edits)
    for i in range(m):
        assert max([k[i] for k in cross] or [0]) <= (2 if i in cyc else 1)
        if i not in cyc:
            assert all(k[i] == 0 for k in d1) and all(k[i] == 0 for k in d2)
    return cyc,cross


def run():
    q = Q(1,7)
    checks=0
    ed=[(1,2),(3,4)]
    w1=from_edges(5,[(0,1,Q(1,4)),(2,3,Q(1,4))])
    w2=from_edges(5,[(0,1,Q(1,5)),(2,3,Q(1,4))])
    cyc,p = check_models(w1,w2,ed,(0,4))
    assert cyc == set()
    for x,y in product((Q(0),q),(Q(0),q)):
        assert eval_observer(5,w1,ed,(0,4),(x,y))==x*y/16
        assert eval_observer(5,w2,ed,(0,4),(x,y))==x*y/20
        checks+=2
    assert kappa((Q(0),q),2)==0
    w1=from_edges(5,[(0,1,Q(1,4)),(2,0,Q(1,4)),(0,3,Q(1,4))])
    w2=from_edges(5,[(0,1,Q(1,4)),(2,0,Q(1,4)),(0,3,Q(1,5))])
    cyc,p = check_models(w1,w2,ed,(0,4))
    assert cyc == {0}
    for x,y in product((Q(0),q,2*q),(Q(0),q)):
        assert eval_observer(5,w1,ed,(0,4),(x,y))==y/4/(1-x/16)
        assert eval_observer(5,w2,ed,(0,4),(x,y))==y/5/(1-x/16)
        checks+=2
    assert kappa((Q(0),q,2*q),2)==1
    assert kappa((Q(0),q,2*q),13)==0
    rng=Random(28420261118)
    random_pairs=0
    for n in (3,4):
        for m in (1,2,3):
            for _ in range(12):
                ws=[]
                for _ in range(2):
                    w=[[Q(rng.randrange(0,3),32*n) for _ in range(n)] for _ in range(n)]
                    ws.append(w)
                edits=[(rng.randrange(n),rng.randrange(n)) for _ in range(m)]
                check_models(ws[0],ws[1],edits,(rng.randrange(n),rng.randrange(n)))
                random_pairs+=1
    return {"status":"PASS","method":"exact rational polynomial determinant and matrix inverse","deterministic_random_seed":28420261118,"random_model_pairs":random_pairs,"explicit_observer_checks":checks,"pure_acyclic_grid_size":4,"mixed_grid_size":6,"p2_kappa_acyclic":0,"p2_kappa_one_cyclic":1,"p13_kappa_one_cyclic":0}


if __name__ == "__main__":
    print(json.dumps(run(),sort_keys=True,indent=2))
