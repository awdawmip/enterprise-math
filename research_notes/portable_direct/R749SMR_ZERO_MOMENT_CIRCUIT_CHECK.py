"""Exact finite certificate for R749SMR's d=4 zero-Walsh-moment fibers.
No numerical optimization or external packages are used.
"""
from fractions import Fraction as F
from itertools import combinations
import json

N = 16
C = (1, 2, 4, 8, 15)
BAR_C = tuple(x for x in range(1, N) if x not in C)

def chi(a, x):
    return 1 if ((a & x).bit_count() & 1) == 0 else -1

def solve(a, b):
    """Exact 5x5 elimination; None for singular matrices."""
    z = [[F(v) for v in row] + [F(rhs)] for row, rhs in zip(a, b)]
    for j in range(5):
        k = next((k for k in range(j,5) if z[k][j]), None)
        if k is None:
            return None
        z[j], z[k] = z[k], z[j]
        piv = z[j][j]
        z[j] = [x / piv for x in z[j]]
        for k in range(5):
            if k == j:
                continue
            mult = z[k][j]
            if mult:
                z[k] = [u - mult*v for u, v in zip(z[k], z[j])]
    return tuple(z[j][5] for j in range(5))

def tv_uniform(p):
    return sum(abs(y-F(1,N)) for y in p)/2

signs = {x: tuple(chi(a,x) for a in C) for x in range(N)}
assert len(set(signs.values())) == N
assert all(__import__('math').prod(v) == 1 for v in signs.values())
assert all(sum(s==-1 for s in v) in (0,2,4) for v in signs.values())

for pair in combinations(range(N),2):
    assert any(signs[pair[0]][i]==signs[pair[1]][i] for i in range(5))
for triple in combinations(range(N),3):
    cols = [tuple(signs[x][i] for x in triple) for i in range(5)]
    if any(len(set(col)) == 1 for col in cols):
        continue
    minority = set()
    for col in cols:
        assert len(set(col)) == 2
        minority.add(0 if col[1]==col[2] else 1 if col[0]==col[2] else 2)
    assert minority == {0,1,2}

H = (0,7,8,15)
assert all(sum(chi(a,x) for x in H)==0 for a in C)
p_h = tuple(F(1,4) if x in H else F(0) for x in range(N))
assert tv_uniform(p_h)==F(3,4)

A = [signs[x] for x in range(N)]
vertices = set()
singular = 0
feasible_bases = 0
for z in combinations(range(N),5):
    c = solve([A[x] for x in z], [-1]*5)
    if c is None:
        singular += 1
        continue
    p = tuple((1+sum(c[j]*A[x][j] for j in range(5)))/16 for x in range(N))
    if all(x>=0 for x in p):
        assert sum(p)==1
        assert all(sum(p[x]*chi(a,x) for x in range(N))==0 for a in BAR_C)
        feasible_bases += 1
        vertices.add(c)

unit_vectors = {
    tuple(F(s) if j==i else F(0) for j in range(5))
    for i in range(5) for s in (-1,1)
}
third_sign_vectors = {
    tuple(F(s,3) for s in signs[x]) for x in range(N)
}
assert len(unit_vectors)==10 and len(third_sign_vectors)==16
assert vertices == unit_vectors | third_sign_vectors
assert len(vertices)==26

by_type = {}
for c in vertices:
    p = tuple((1+sum(c[j]*A[x][j] for j in range(5)))/16 for x in range(N))
    risk = tv_uniform(p)
    tag='unit' if c in unit_vectors else 'one-third sign'
    by_type[tag]=by_type.get(tag,0)+1
    assert risk == (F(1,2) if tag=='unit' else F(5,16))

report = {
    'result': 'PASS',
    'date': '2026-11-13',
    'statement': 'zero retained moments only, d=4',
    'five_circuit': list(C),
    'complement': list(BAR_C),
    'n_pairs_checked': 120,
    'n_triples_checked': 560,
    'n_facets': 16,
    'n_facet_5_subsets': 4368,
    'n_singular_bases': singular,
    'n_feasible_bases': feasible_bases,
    'n_distinct_vertices': len(vertices),
    'vertex_types': by_type,
    'zero_moment_radius_C': '3/4',
    'zero_moment_radius_complement': '1/2',
    'nonzero_moment_global_radius': 'NOT_TESTED',
    'algorithm': 'exact rational 5x5 elimination and finite sign-pattern coverage',
}
print(json.dumps(report, sort_keys=True, indent=2))
