#!/usr/bin/env python3
"""R284BK circular real-noise test; calls R284BJ finite-field checker."""
from fractions import Fraction
import json

from R284BJ_finite_field_port_checker import exact_fixture

cases = [
    (2, 2, 0, Fraction(49, 100)),
    (3, 2, 3, Fraction(9, 2)),
    (4, 2, 3, Fraction(39, 1)),
]
results = []
for n, H, original_integer_delta, rho in cases:
    fixture = exact_fixture(n=n, H=H, delta=original_integer_delta, seed=20261120)
    gap = fixture["minimum_cyclic_residue_gap"]
    assert 2 * rho < gap
    results.append({
        "n": n,
        "H": H,
        "matrices_exhausted": fixture["matrices_exhausted"],
        "p": fixture["p"],
        "minimum_cyclic_gap": gap,
        "tested_real_radius": f"{rho.numerator}/{rho.denominator}",
        "strict_gap_proof": "2*rho < min_gap",
        "sha256_sorted_residues": fixture["sorted_residues_sha256"],
    })

print(json.dumps({
    "schema": "R284BK_CIRCULAR_REAL_NOISE_CHECK_V1",
    "status": "PASS",
    "cases": results,
    "verification": "finite exhaustive exact-gap check, rational radius",
    "independent_review": "NOT_REVIEWED",
}, indent=2))
