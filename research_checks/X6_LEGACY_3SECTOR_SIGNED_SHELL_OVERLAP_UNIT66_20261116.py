#!/usr/bin/env python3
"""Exact selected-three-axis signed X6 BRC versus three positive two-generator sectors.
All-radius theorem; independent finite exhaustive verification for G=1..512.
Author-side / unreviewed / not admitted; original R061-R063 experiments not rerun.
"""
import json
from math import factorial, isqrt
from pathlib import Path

LIMIT = 512

def require(cond, message):
    if not cond:
        raise AssertionError(message)

def weight(a, b, c=0):
    t = a + b + c
    return factorial(t) // (factorial(a) * factorial(b) * factorial(c))

def add(array, norm, mass):
    if norm <= LIMIT:
        array[norm][0] += 1
        array[norm][1] += mass

signed = [[0, 0] for _ in range(LIMIT + 1)]
minzero = [[0, 0] for _ in range(LIMIT + 1)]
support3 = [[0, 0] for _ in range(LIMIT + 1)]
sector = [[0, 0] for _ in range(LIMIT + 1)]
radius = isqrt(LIMIT)

# Independently enumerate full signed triples, positive charts, 3-support.
for a in range(-radius, radius + 1):
    for b in range(-radius, radius + 1):
        for c in range(-radius, radius + 1):
            g = a*a + b*b + c*c
            if 0 < g <= LIMIT:
                add(signed, g, weight(abs(a), abs(b), abs(c)))
for a in range(radius + 1):
    for b in range(radius + 1):
        g = a*a + b*b
        if 0 < g <= LIMIT:
            add(sector, g, weight(a, b))
        for c in range(radius + 1):
            g = a*a + b*b + c*c
            if 0 < g <= LIMIT:
                if min(a, b, c) == 0:
                    add(minzero, g, weight(a, b, c))
                else:
                    add(support3, g, weight(a, b, c))

examples = {}
for g in range(1, LIMIT + 1):
    sq = int(isqrt(g)**2 == g)
    predicted_minzero = [3*sector[g][j] - 3*sq for j in range(2)]
    predicted_signed = [4*minzero[g][j] - 6*sq + 8*support3[g][j] for j in range(2)]
    require(minzero[g] == predicted_minzero, f"three-sector overlap mismatch g={g}")
    require(signed[g] == predicted_signed, f"signed native shell mismatch g={g}")
    if g in (1, 2, 3, 25, 50, 65, 100, 512):
        examples[str(g)] = {
            "square": bool(sq),
            "two_generator_sector": {"endpoints": sector[g][0], "brc": sector[g][1]},
            "three_sector_minzero_union": {"endpoints": minzero[g][0], "brc": minzero[g][1]},
            "strict_positive_three_support": {"endpoints": support3[g][0], "brc": support3[g][1]},
            "signed_three_axis_shell": {"endpoints": signed[g][0], "brc": signed[g][1]},
        }
certificate = {
    "schema": "X6_LP015_019_SECTOR_SIGNED_SHELL_OVERLAP_UNIT66_V1",
    "status": "AUTHOR_EXACT_FINITE_EXECUTED_UNREVIEWED_NOT_ADMITTED",
    "date": "2026-11-16",
    "domain": "all integers 1<=G<=512, native signed selected Z3; fixed native Cell start",
    "formula": {
        "minzero_endpoints": "E=3*R2-3*is_square",
        "minzero_positive_BRC": "W=3*W2-3*is_square",
        "signed_endpoints": "S=4*E-6*is_square+8*Q_count",
        "signed_positive_BRC": "B=4*W-6*is_square+8*Q_mass",
    },
    "counts": {
        "shells": LIMIT,
        "signed_native_points_examined": (2*radius+1)**3 - 1,
        "nonnegative_triples_examined": (radius+1)**3 - 1,
        "two_gen_pairs_examined": (radius+1)**2 - 1,
        "failed_equalities": 0,
    },
    "samples": examples,
    "frozen_science": {
        "baseline": "59538f585d037d09ef687b28715c4bc1a3f9fe03",
        "historical": "fd2bcff10ca6e147348b6c1236027fc0d2877df3",
    },
    "not_executed": "No original R061/R062/R063 checker or native benchmark executed",
}
target = Path(__file__).with_name("X6_LEGACY_3SECTOR_SIGNED_SHELL_OVERLAP_UNIT66_RESULTS_20261116.json")
target.write_text(json.dumps(certificate, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"status": "PASS", "cases": LIMIT, "samples": examples}, ensure_ascii=False))
