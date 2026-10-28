#!/usr/bin/env python3
"""Exact rational identity check; no prime or recurrence-value enumeration."""
import json
import sympy as s

z = s.symbols("z")
U = 1 - s.Rational(3, 4) * z**2
w = z**6 / (16 * U**2)
P = 4 - 5 * z**2 + z**4
ell = 1 / z + z / U
T = 36 * z**4 * (4 - z**2) / (4 - 3 * z**2)**2

C2 = P * s.diff(w, z)**2
C1 = (2 * P * ell + s.diff(P, z)) * s.diff(w, z) + P * s.diff(w, z, 2)
C0 = P * (s.diff(ell, z) + ell**2) + s.diff(P, z) * ell + 2 * z**2 - 2

residuals = [
    s.cancel(C2 - T * w * (1 - w)),
    s.cancel(C1 - T * (s.Rational(7, 6) - s.Rational(13, 6) * w)),
    s.cancel(C0 + s.Rational(5, 18) * T),
]
assert residuals == [0, 0, 0]
print(json.dumps({
    "check": "EXACT_RATIONAL_PULLBACK_THREE_COEFFICIENT_IDENTITIES",
    "sympy_version": s.__version__,
    "variables": ["z"],
    "coefficient_domain": "Q",
    "residuals": [str(r) for r in residuals],
    "all_zero": True,
    "prime_samples": 0,
    "recurrence_samples": 0,
    "valuation_theorem_verified_by_program": False,
    "scope": "Author symbolic regression supplement; paper proof required for valuations and all-k claim."
}, indent=2))
