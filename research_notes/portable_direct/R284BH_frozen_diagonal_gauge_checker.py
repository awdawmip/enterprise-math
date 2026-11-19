#!/usr/bin/env python3
"""Exact finite checks for R284BH universal frozen-diagonal Port gauge."""
from fractions import Fraction as F
from itertools import product
import json, random

def det(mat):
    a = [[F(x) for x in row] for row in mat]
    n = len(a)
    ans = F(1)
    for k in range(n):
        pivot = next((j for j in range(k, n) if a[j][k]), None)
        if pivot is None:
            return F(0)
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            ans = -ans
        q = a[k][k]
        ans *= q
        for i in range(k + 1, n):
            t = a[i][k] / q
            for j in range(k + 1, n):
                a[i][j] -= t * a[k][j]
            a[i][k] = F(0)
    return ans

def obs(c, d, z):
    n = len(c)
    a = [[F(d[i] if i == j else 0) - F(c[i][j]) for j in range(n)] for i in range(n)]
    for i in range(1, n):
        a[0][i] -= F(z[i])
    return det(a)

def gauge(c, j, t, dj, k=1):
    """j is frozen; j>=1: left row-0 shear; j=0: right column-k shear."""
    cp = [[F(x) for x in row] for row in c]
    n = len(c)
    if j:
        for col in range(n):
            cp[0][col] += F(t) * F(c[j][col])
        cp[0][j] -= F(t) * F(dj)
    else:
        for row in range(n):
            cp[row][k] += F(t) * F(c[row][0])
        cp[0][k] -= F(t) * F(dj)
    return cp

rng = random.Random(28420261120)
checks = 0
families = []
for n in range(2, 8):
    for j in range(n):
        for trial in range(20):
            c = [[rng.randint(1, 8) for _ in range(n)] for _ in range(n)]
            dj = F(rng.randrange(-12, 13), rng.randrange(1, 6))
            t = F(1, 1000 * (1 + abs(dj)))
            cp = gauge(c, j, t, dj)
            assert all(x > 0 for row in cp for x in row)
            assert cp != [[F(x) for x in r] for r in c]
            for _ in range(8):
                d = [F(rng.randrange(-9, 10), rng.randrange(1, 5)) for _ in range(n)]
                d[j] = dj
                z = [F(0)] + [F(rng.randrange(-9, 10), rng.randrange(1, 4)) for _ in range(n-1)]
                assert obs(c, d, z) == obs(cp, d, z), (n, j, trial, d, z)
                checks += 1
    families.append({'n': n, 'frozen_coordinates_covered': n, 'exact_observation_checks': n * 20 * 8})

binary_checks = 0
binary_pairs = 0
for bits in product((1, 2), repeat=9):
    c = [list(bits[i*3:i*3+3]) for i in range(3)]
    for j in range(3):
        cp = gauge(c, j, 1, 0)
        if all(1 <= x <= 2 and x.denominator == 1 for row in cp for x in row):
            binary_pairs += 1
            for d0, d1, d2, z1, z2 in product((0, 1, 3), repeat=5):
                d = [d0, d1, d2]
                d[j] = 0
                assert obs(c, d, [0, z1, z2]) == obs(cp, d, [0, z1, z2])
                binary_checks += 1

w = [[1] * 3 for _ in range(3)]
w0 = gauge(w, 0, 1, 0)
w1 = gauge(w, 1, 1, 0)
assert w0 == [[1,2,1],[1,2,1],[1,2,1]]
assert w1 == [[2,2,2],[1,1,1],[1,1,1]]

obj = {
  'schema':'R284BH_UNIVERSAL_FROZEN_DIAGONAL_PORT_GAUGE_V1',
  'seed':28420261120,
  'exact_rational_observation_checks':checks,
  'families':families,
  'binary_3x3_admissible_pairs':binary_pairs,
  'binary_3x3_exact_observation_checks':binary_checks,
  'binary_witness_C':w,
  'binary_witness_frozen_d0':[[int(x) for x in row] for row in w0],
  'binary_witness_frozen_d1':[[int(x) for x in row] for row in w1],
  'binary_witness_setting':'fixed d_j=0, all other d and z arbitrary',
  'status':'PASS',
  'scope':'Finite exact checks; general result follows from determinant-preserving row or column shears.'
}
with open('R284BH_frozen_diagonal_gauge_verification.json','w') as f:
    json.dump(obj, f, ensure_ascii=False, indent=2)
print(json.dumps(obj, ensure_ascii=False, indent=2))
