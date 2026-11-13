#!/usr/bin/env python3
"""Exact centered-fiber radius for the 4-bit five-circuit and complement."""
import json
from fractions import Fraction as Q
from itertools import combinations

D = 4
N = 1 << D
C = (1, 2, 4, 8, 15)
BAR = tuple(a for a in range(1, N) if a not in C)

def chi(a, x):
    return 1 if ((a & x).bit_count() & 1) == 0 else -1

def solve(A, b):
    n = len(b)
    T = [[Q(v) for v in row] + [Q(bi)] for row, bi in zip(A, b)]
    for j in range(n):
        k = next((i for i in range(j, n) if T[i][j]), None)
        if k is None:
            return None
        T[j], T[k] = T[k], T[j]
        v = T[j][j]
        T[j] = [x / v for x in T[j]]
        for i in range(n):
            if i != j and T[i][j]:
                f = T[i][j]
                T[i] = [x - f * y for x, y in zip(T[i], T[j])]
    return tuple(row[-1] for row in T)

def spans(basis):
    return tuple(sorted({a ^ b ^ c for a in (0, basis[0])
                         for b in (0, basis[1])
                         for c in (0, basis[2])})) if len(basis) == 3 else tuple(
            sorted({a ^ b for a in (0, basis[0]) for b in (0, basis[1])}))

def find_zero_moment_coset(U, rank):
    for basis in combinations(range(1, N), rank):
        H = spans(basis)
        if len(H) != (1 << rank):
            continue
        if all(sum(chi(a, x) for x in H) == 0 for a in U):
            return list(H)
    raise AssertionError("no witness")

def tv_uniform(p):
    return sum(max(v - Q(1, N), Q(0)) for v in p)

def main():
    shared_sign_pairs = sum(any(chi(a,x)==chi(a,y) for a in C)
                            for x,y in combinations(range(N),2))
    assert shared_sign_pairs == 120
    Hc = find_zero_moment_coset(C, 2)
    Hb = find_zero_moment_coset(BAR, 3)
    assert len(Hc) == 4 and len(Hb) == 8
    pc = tuple(Q(1,4) if x in Hc else Q(0) for x in range(N))
    pb = tuple(Q(1,8) if x in Hb else Q(0) for x in range(N))
    assert tv_uniform(pc)==Q(3,4) and tv_uniform(pb)==Q(1,2)
    signs = [[chi(a,x) for a in C] for x in range(N)]
    vertices = set()
    nonsingular = 0
    for active in combinations(range(N), 5):
        t = solve([signs[x] for x in active], [-1]*5)
        if t is None:
            continue
        nonsingular += 1
        if all(1+sum(t[j]*signs[x][j] for j in range(5))>=0
               for x in range(N)):
            vertices.add(t)
    unit = {tuple(Q(s if j==i else 0) for j in range(5))
            for i in range(5) for s in (-1, 1)}
    parity_signs = {tuple(Q(chi(a,x),3) for a in C) for x in range(N)}
    assert len(vertices)==26 and vertices == unit | parity_signs
    risk = {}
    for t in vertices:
        p = tuple((1+sum(t[j]*signs[x][j] for j in range(5)))/16
                  for x in range(N))
        assert min(p)>=0 and sum(p)==1
        assert all(sum(p[x]*chi(a,x) for x in range(N))==0 for a in BAR)
        risk[t] = tv_uniform(p)
    assert max(risk.values())==Q(1,2)
    assert {risk[t] for t in unit}=={Q(1,2)}
    assert {risk[t] for t in parity_signs}=={Q(5,16)}
    return {
        "status":"PASS", "schema":"R749SMR_CENTERED_FIBER_EXACT_V1",
        "arithmetic":"fractions.Fraction exact rational",
        "C":list(C), "BAR":list(BAR),
        "zero_fiber_chebyshev_radius_C":"3/4",
        "zero_fiber_chebyshev_radius_BAR":"1/2",
        "pairwise_shared_sign_checks":shared_sign_pairs,
        "C_zero_moment_support_H":Hc,
        "BAR_zero_moment_support_H":Hb,
        "active_subsets_checked":4368,
        "nonsingular_active_subsets":nonsingular,
        "BAR_zero_fiber_vertices":len(vertices),
        "vertex_kinds":{"unit":len(unit),"parity_signs_thirds":len(parity_signs)},
        "vertex_TV_kinds":{"unit":"1/2","parity_signs_thirds":"5/16"},
        "scope":"centered moment fiber only; global nonlinear minimax remains open",
    }

if __name__ == "__main__":
    print(json.dumps(main(),sort_keys=True,indent=2))
