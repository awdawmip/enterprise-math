#!/usr/bin/env python3
"""Exact nonzero runner classification, unsigned auxiliary M3 Port--Euler model."""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import comb

ports = [p for p in combinations(range(6), 2) if p not in {(0, 1), (2, 3), (4, 5)}]
bit = {p: 1 << i for i, p in enumerate(ports)}
E = []
for i, j, k in product(range(2), repeat=3):
    a, b, c = (i, 2+j), (i, 4+k), (2+j, 4+k)
    E.append((bit[a]^bit[b], bit[a]^bit[c], bit[b]^bit[c]))
F = {0}
for tri in combinations(range(6), 3):
    available = [p for p in combinations(tri, 2) if p in bit]
    if len(available) == 2:
        edge = bit[available[0]] ^ bit[available[1]]
        F |= {x ^ edge for x in tuple(F)}
assert len(ports) == 12 and len(E) == 8 and len(F) == 512

# Polynomial P[b][i] = coefficient of t^i in [X^b] prod_support(t+X^e1+X^e2+X^e3).
P = {0: (1,)}
for edges in E:
    nxt = defaultdict(lambda: [0]*9)
    for mask, coeffs in P.items():
        for i, value in enumerate(coeffs):
            if value:
                if i < 8:
                    nxt[mask][i+1] += value
                for edge in edges:
                    nxt[mask^edge][i] += value
    P = {mask: tuple(coeffs) for mask, coeffs in nxt.items()}
assert len(P) == 2048
classes = defaultdict(list)
for boundary in sorted(F):
    classes[P.get(boundary, (0,)*9)].append(boundary)
assert len(classes) == 19
assert P[0] == (9, 0, 16, 0, 6, 0, 0, 0, 1)

# The exact nonzero runner candidate: the 12 pairwise-adjacent two-point boundaries.
runner12 = {3, 12, 17, 34, 48, 68, 136, 192, 768, 1280, 2560, 3072}
runner3 = {51, 204, 3840}  # one complete four-point grid
assert set(classes[P[3]]) == runner12
assert set(classes[P[51]]) == runner3
assert P[3] == (6, 8, 6, 8, 2, 0, 2, 0, 0)
assert P[51] == (8, 0, 16, 0, 8, 0, 0, 0, 0)

# Exact Bernstein positivity on [1/2,1] and [1,3].
# For b != 0,3, (p_3(t)-p_b(t))/(t-1)^2 is polynomial, nonnegative.
def quotient_twice(d):
    q = []
    for i in range(7):
        q.append(d[i]+(2*q[-1] if q else 0)-(q[-2] if len(q)>1 else 0))
    reconstruct = [0]*9
    for i, value in enumerate(q):
        reconstruct[i] += value
        reconstruct[i+1] -= 2*value
        reconstruct[i+2] += value
    assert tuple(reconstruct) == tuple(d)
    return q

def bernstein(coeff, lo, hi):
    n = len(coeff)-1
    power = [Fraction(0) for _ in range(n+1)]
    for i, v in enumerate(coeff):
        for k in range(i+1):
            power[k] += Fraction(v)*comb(i,k)*lo**(i-k)*(hi-lo)**k
    return [sum((power[i]*Fraction(comb(j,i),comb(n,i)) for i in range(j+1)), Fraction(0)) for j in range(n+1)]

certificate = []
for coeffs, boundaries in sorted(classes.items(), key=lambda item: min(item[1])):
    rep = min(boundaries)
    if rep in {0, 3}:
        continue
    d = [P[3][i]-coeffs[i] for i in range(9)]
    q = quotient_twice(d)
    left, right = bernstein(q, Fraction(1,2), Fraction(1)), bernstein(q, Fraction(1), Fraction(3))
    assert min(left) >= 0 and min(right) >= 0, (rep, left, right)
    if rep == 18:  # sole class with extra zero at t=1; strict elsewhere
        assert q == [2, 0, -4, 0, 2, 0, 0]
    else:
        assert min(left) > 0 and min(right) > 0
    certificate.append((rep, len(boundaries), str(min(left)), str(min(right))))
assert len(certificate) == 17

# Isolated admissible ratio t=1/3 (uniform m=3); exact integer scoring.
def local_weights(m):
    r = m//2
    return ((r+1)*(r+2)//2, r*(r+1)//2) if m%2 == 0 else (r*(r+1)//2, (r+1)*(r+2)//2)

def exact_fiber(m, boundary):
    A, B = local_weights(m)
    return sum(value*A**i*B**(8-i) for i, value in enumerate(P.get(boundary, (0,)*9))) - (3 if boundary == 0 else 0)

runner3_value = max(exact_fiber(3, boundary) for boundary in F if boundary)
assert runner3_value == 64800
assert {b for b in F if b and exact_fiber(3, b) == runner3_value} == runner3
assert max(exact_fiber(1, b) for b in F if b) == 8

for m in range(2, 13):
    best = max(exact_fiber(m, b) for b in F if b)
    winners = {b for b in F if b and exact_fiber(m, b) == best}
    expected = runner3 if m == 3 else runner12
    assert winners == expected
    A, B = local_weights(m)
    assert exact_fiber(m, 0) == A**8 + 6*A**4*B**4 + 16*A**2*B**6 + 9*B**8 - 3
    if m != 3:
        assert best == (6*B**8 + 8*A*B**7 + 6*A**2*B**6 + 8*A**3*B**5 + 2*A**4*B**4 + 2*A**6*B**2)
    else:
        assert best == 8*B**4*(A*A+B*B)**2
print('PASS', 'forced_boundaries=', len(F), 'polynomial_classes=',len(classes), 'Bernstein_certificates=',len(certificate))
print('NONZERO_RUNNER_FOR_M_2_AND_M_GEQ4=', sorted(runner12))
print('NONZERO_RUNNER_FOR_M_3=', sorted(runner3))
print('CERTIFICATE [representative, multiplicity, min Bernstein left, right]:')
for row in certificate:
    print(*row)
print('ALL_REGRESSIONS_PASSED m=1..12')
