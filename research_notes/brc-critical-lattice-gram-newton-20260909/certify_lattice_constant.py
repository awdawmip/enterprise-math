#!/usr/bin/env python3
"""Exact finite certificate for C_* = 9.503 in the 3D periodic critical NS bilinear bound.

Analytic far-tail proof and the PDE statement are in
research_notes/brc-critical-lattice-gram-newton-20260909.md.
The finite part uses exact Fraction arithmetic and octahedral symmetry.
"""
from __future__ import annotations
from fractions import Fraction
import itertools, json, math
from pathlib import Path

R2 = 36
NEAR_BOUND = Fraction(2321, 125)  # 18.568
CSTAR = Fraction(9503, 1000)
SQRT3_UPPER = Fraction(1351, 780)
PI_UPPER = Fraction(355, 113)

P = []
for p in itertools.product(range(-5, 6), repeat=3):
    n = sum(x*x for x in p)
    if 0 < n < R2:
        P.append((p, n))
assert len(P) == 894
A6 = sum((Fraction(1, n) for _, n in P), Fraction())
assert A6 == Fraction(67048852231, 1012647636)

classes = []
for a in range(13):
    for b in range(a, 13):
        for c in range(b, 13):
            n = a*a + b*b + c*c
            if 0 < n < 169:
                classes.append((a, b, c, n))
assert len(classes) == 277

max_sq = Fraction(0)
max_arg = None
max_radial_sum = None
for a, b, c, n in classes:
    radial_sum = Fraction()
    for p, pn in P:
        q0, q1, q2 = a-p[0], b-p[1], c-p[2]
        qn = q0*q0 + q1*q1 + q2*q2
        if qn:
            radial_sum += Fraction(1, pn*qn)
    value_sq = n * radial_sum * radial_sum
    assert value_sq < NEAR_BOUND * NEAR_BOUND
    if value_sq > max_sq:
        max_sq = value_sq
        max_arg = (a, b, c)
        max_radial_sum = radial_sum

large_k_upper = Fraction(13, 49) * A6
assert large_k_upper < NEAR_BOUND
assert SQRT3_UPPER * SQRT3_UPPER > 3
far_upper = (1 + SQRT3_UPPER/Fraction(12))**4 * PI_UPPER**3
total_upper = 2*NEAR_BOUND + far_upper
assert total_upper < CSTAR*CSTAR

result = {
    "status": "PASS",
    "scope": "exact finite near-field enumeration plus analytic cube/Riesz far-field bound",
    "near_radius": 6,
    "near_lattice_points": len(P),
    "octahedral_classes_checked": len(classes),
    "near_bound": str(NEAR_BOUND),
    "observed_exact_max_class": max_arg,
    "observed_exact_max_radial_sum": str(max_radial_sum),
    "observed_max_decimal": math.sqrt(sum(x*x for x in max_arg))*float(max_radial_sum),
    "large_k_upper_decimal": float(large_k_upper),
    "far_upper_decimal": float(far_upper),
    "total_C_squared_upper_decimal": float(total_upper),
    "certified_C_star": str(CSTAR),
    "certified_C_star_decimal": float(CSTAR),
    "rational_bounds": {
        "sqrt3_upper": str(SQRT3_UPPER),
        "pi_upper": str(PI_UPPER),
        "total_less_than_Cstar_squared": True,
    },
    "limitations": [
        "The constant is explicit and valid, not claimed sharp.",
        "The analytic PDE proof is in the source note.",
        "This certificate does not prove arbitrary-data Navier-Stokes regularity."
    ],
}
Path(__file__).with_name("lattice_constant_verification.json").write_text(
    json.dumps(result, indent=2, ensure_ascii=False)+"\n", encoding="utf-8"
)
print(json.dumps(result, indent=2, ensure_ascii=False))
