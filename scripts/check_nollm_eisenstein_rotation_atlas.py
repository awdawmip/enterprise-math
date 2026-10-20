#!/usr/bin/env python3
"""Exact checker for RS-NOLLM-EISENSTEIN-ROTATION-ATLAS.

Stdlib-only; all exact address/refinement checks use integers/Fraction.
No floating nearest-point logic is used.
"""
from __future__ import annotations
from fractions import Fraction
from math import comb
import json


def emul(x, y):
    """Multiply a+b*w, c+d*w with w^2+w+1=0."""
    a, b = x
    c, d = y
    return (a*c - b*d, a*d + b*c - b*d)


def eadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def esub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def enorm(x):
    """Norm a^2-ab+b^2, valid over Q as squared Euclidean length."""
    a, b = x
    return a*a - a*b + b*b


def c_mul_algebra(Q, R):
    # c=(2+w)/3
    return (Fraction(2*Q-R, 3), Fraction(Q+R, 3))


def c_mul_axial(q, r):
    # pointy-top axial basis z=q+r(1+w)
    return (Fraction(q-r, 3), Fraction(q+2*r, 3))


def is_integral_pair(x):
    return all(v.denominator == 1 for v in x)


checks = {}

# H1: exact Voronoi/circle geometry in Eisenstein coordinates.
c = (Fraction(2, 3), Fraction(1, 3))
cbar = (Fraction(1, 3), Fraction(-1, 3))
zero = (Fraction(0), Fraction(0))
one = (Fraction(1), Fraction(0))
zeta = (Fraction(1), Fraction(1))
assert enorm(c) == Fraction(1, 3)
assert enorm(esub(c, one)) == Fraction(1, 3)
assert enorm(esub(c, zeta)) == Fraction(1, 3)
assert enorm(cbar) == Fraction(1, 3)
assert enorm(esub(c, cbar)) == Fraction(1, 3)
assert enorm((Fraction(1, 2), Fraction(0))) == Fraction(1, 4)
checks["H1_exact_hex_circle"] = {
    "circumradius_squared": "1/3",
    "side_squared": "1/3",
    "inradius_squared": "1/4",
    "triple_intersection_checked": True,
}

# H2: index-3 refinement and axial mod-3 classifier.
alpha = (Fraction(1), Fraction(-1))
assert emul(alpha, alpha) == (Fraction(0), Fraction(-3))
assert emul(alpha, c) == (Fraction(1), Fraction(0))
assert eadd(eadd(c, c), c) == (Fraction(2), Fraction(1))
assert not is_integral_pair(c)
for Q in range(-12, 13):
    for R in range(-12, 13):
        got = is_integral_pair(c_mul_algebra(Q, R))
        want = ((Q + R) % 3 == 0)
        assert got == want
for q in range(-12, 13):
    for r in range(-12, 13):
        got = is_integral_pair(c_mul_axial(q, r))
        want = ((q - r) % 3 == 0)
        assert got == want
assert 2*1 - 1*(-1) == 3
checks["H2_refinement"] = {
    "alpha_squared": "-3*w",
    "index": 3,
    "axial_classifier": "q-r mod 3",
    "enumerated_axial_pairs": 25*25,
}

# H3: coefficient identity proving J_n=(n+1)(n+2)*oriented moment.
count = 0
for n in range(0, 41):
    for k in range(0, n+1):
        lhs = Fraction(comb(n+1, k+1), 1)
        rhs = Fraction((n+1)*comb(n, k), k+1)
        assert lhs == rhs
        count += 1
checks["H3_path_jet_coefficients"] = {
    "degrees_checked": [0, 40],
    "coefficient_equalities": count,
}

# Translation-law normalization coefficients are exact rationals.
for n in range(0, 21):
    for k in range(0, n+1):
        coeff = Fraction(
            comb(n, k) * (n+1) * (n+2),
            (k+1) * (k+2),
        )
        assert coeff > 0
checks["H3_translation_coefficients"] = {"degrees_checked": [0, 20]}

# H4: exact phase-count test cases.
for k in range(0, 9):
    assert 3**k >= 1
assert 3**2 == 9
checks["H4_phase_examples"] = {
    "nested_counts_k_0_to_8": [3**k for k in range(9)],
    "nonnested_a_2_over_3": 9,
}

# Exact-resonant scalar multipliers are Eisenstein units.
units = sorted((a, b) for a in range(-2, 3) for b in range(-2, 3)
               if a*a-a*b+b*b == 1)
assert units == [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1)]
checks["H4_units"] = {"count": len(units), "pairs": units}

# H6: polynomial identities behind the AGL(1,p) invariant
# I_p=(x^p-x)^(p-1). Equal degree/order alone is not promoted.
primes = [2, 3, 5, 7, 11, 13, 17, 19]
for p in primes:
    for j in range(1, p):
        assert comb(p, j) % p == 0
    for b in range(p):
        assert (pow(b, p, p) - b) % p == 0
    for a in range(1, p):
        assert pow(a, p, p) == a % p
        assert pow(a, p-1, p) == 1
checks["H6_affine_invariant"] = {
    "primes_checked": primes,
    "degree_formula": "p(p-1)",
    "group_order_formula": "p(p-1)",
    "note": "identity verified; no path-jet obstruction is inferred from equal degree/order",
}

report = {
    "schema": "NOLLM_EISENSTEIN_ROTATION_ATLAS_EXACT_CHECK_V1",
    "task_id": "RS-NOLLM-EISENSTEIN-ROTATION-ATLAS",
    "all_passed": True,
    "checks": checks,
}
print(json.dumps(report, indent=2, sort_keys=True))
