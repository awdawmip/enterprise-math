#!/usr/bin/env python3
"""Exact structural audit for the R5 Q-progression exception-degree bound.

This checks finite support-incidence and cyclotomic pole-count facts.
The all-m rational identity and 91 baseline nonvanishing certificates
remain sourced mathematical dependencies rather than rerun by this audit.
"""
from collections import Counter
from math import lcm

W = (7, 9, 11, 13, 16, 17, 19, 23, 25, 27, 31, 37)
U = tuple(range(214, 222))
V = tuple(range(223, 291))
Z = tuple(range(296, 313))
S = tuple(m for m in range(1, 79809)
          if m % 58 in (0, 54, 55, 56, 57)
          and m % 64 in (0, 60, 61, 62, 63)
          and m % 43 in (0, 37, 38, 39, 40, 41, 42))
L = 229746052653717600
Q = 2 * L
assert len(S) == 91 and S[0] == 2492 and S[-1] == 79808
assert Q == 459492105307435200
assert all(Q % (2 * d) == 0 for d in W)
assert lcm(*(2*d for d in W), 79808) == Q
assert lcm(*W) == 92119507880400

# The exact U max-layer expansion has at most 6 t-denominator
# factors; one q-Euler derivative gives at most 7.
A_DEG, DA_DEG = 5, 6
caps = {}
for d in W:
    b0 = [p for p in V if p % d == 0]
    c0 = [p for p in Z if p % d == 0]
    assert b0 and c0
    if d != 37:
        assert len(b0) >= 2  # B'(zeta_d) identically zero
    else:
        assert b0 == [259]
        assert max(Counter(p % d for p in V)[r] + (r == 0)
                   for r in range(d)) <= 2
    if d in (7, 9, 11, 13):
        assert len(c0) >= 2  # C'(zeta_d) identically zero
    else:
        assert len(c0) == 1
        assert max(Counter(p % d for p in Z)[r] + (r == 0)
                   for r in range(d)) <= 2
    assert sum(p % d == 0 for p in range(214, 315)) >= 3
    if d in (7, 9, 27, 31):
        u0 = [p for p in U if p % d == 0]
        assert len(u0) == 1 and u0[0] in (216, 217, 218)
        assert all(p % d for p in (214, 215, 219, 220, 221))
        caps[d] = A_DEG  # R0=0, degree of R'<=5
    elif d == 37:
        assert sum(p % d == 0 for p in range(214, 315)) == 3
        caps[d] = A_DEG  # use R0!=0 for the exact 3rd order pole
    else:
        caps[d] = DA_DEG  # selected R0 degree<=5 or R'<=6
assert sum(caps.values()) == 67
assert len([d for d in W if caps[d] == 5]) == 5
assert len(S) * sum(caps.values()) == 6097
for d in W:
    print(f'd={d:2d} B0={sum(p % d == 0 for p in V):2d} '
          f'C0={sum(p % d == 0 for p in Z):2d} '
          f'exception_degree_cap={caps[d]}')
print('ALL CHECKS PASS: 91 phases; 12 roots; 67 exceptions/class; 6097 total')
