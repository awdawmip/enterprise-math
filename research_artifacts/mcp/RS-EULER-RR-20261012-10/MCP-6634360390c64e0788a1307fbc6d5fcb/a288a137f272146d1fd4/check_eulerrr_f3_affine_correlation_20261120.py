#!/usr/bin/env python3
"""Exact finite-domain check for Euler RR F3 algebra and positive-weight correlation."""
from fractions import Fraction
from itertools import product

F = range(3)
S = list(product(F, repeat=3))
AFF = [(u, t) for u in (1, 2) for t in F]

def E(s):
    j, a, r = s
    return j, a, (r + j - a) % 3

def T(s, u, t):
    return tuple((u * x + t) % 3 for x in s)

assert len(S) == 27 and len(AFF) == 6
assert all(E(T(s, *g)) == T(E(s), *g) for s in S for g in AFF)
assert all((E(s)[2] == s[0]) == (s[2] == s[1]) for s in S)
assert all((E(s)[2] - s[0]) % 3 == (s[2] - s[1]) % 3 for s in S)
assert all(E(E(E(s))) == s for s in S)
assert E((1, 0, 0)) != (1, 0, 0)

U = {s: Fraction(1, 27) for s in S}
P = {s: (Fraction(1, 9) if s[2] == s[1] else Fraction(0)) for s in S}
M = {s: (P[s] + U[s]) / 2 for s in S}
assert sum(U.values()) == sum(M.values()) == 1
assert min(M.values()) == Fraction(1, 54)
for i in range(3):
    for label in F:
        assert sum((M[s] for s in S if s[i] == label), Fraction()) == Fraction(1, 3)
        assert sum((U[s] for s in S if s[i] == label), Fraction()) == Fraction(1, 3)
success = lambda D: sum((D[s] for s in S if E(s)[2] == s[0]), Fraction())
assert success(M) == Fraction(2, 3)
assert success(U) == Fraction(1, 3)
print("PASS 162 affine equivariance; 27 preparation, residual and E^3 checks")
print("PASS strict-positive 27-state counterexample: 2/3 vs 1/3")
