"""Exact small coefficient extraction for the proved T6 completion cuts.

This does not enumerate T6 affine classes, integer completions or certificates.
The analytic theorem supplies the global cutoff; this program evaluates only
the resulting at-most-49 integer denominator candidates using Fraction.
"""
from fractions import Fraction
from math import ceil
import json


def smooth13(a):
    for p in (2, 3, 5, 7, 11, 13):
        while a % p == 0:
            a //= p
    return a == 1


def coefficients(h, k):
    out = [1]
    for b in range(2, h + 2):
        nxt = [0] * (len(out) + 1)
        for i, v in enumerate(out):
            nxt[i] += v
            nxt[i + 1] -= b * v
        out = nxt
    return [0] * k + out


def value(a, h, k):
    v = Fraction(1, a**k * (a - 1))
    for b in range(2, h + 2):
        v *= 1 - Fraction(b, a)
    return v


def extract():
    rows = []
    for h in range(1, 7):
        for k in range(7 - h):
            cutoff = ceil(Fraction((k + h + 1) * (h + 1), k + 1))
            candidates = list(range(2, cutoff + 1))
            vals = [(a, value(a, h, k)) for a in candidates]
            if not smooth13(cutoff):
                raise ValueError("This family's claimed admissible endpoint was not verified")
            maximum = max(v for a, v in vals if smooth13(a))
            all_integer_maximum = max(v for a, v in vals)
            rows.append({
                "h": h, "k": k,
                "moment_coefficients": coefficients(h, k),
                "analytic_integer_cutoff": cutoff,
                "cutoff_is_13_smooth": smooth13(cutoff),
                "sharp_unit_cost_cap": str(maximum),
                "maximizers": [a for a, v in vals if smooth13(a) and v == maximum],
                "unrestricted_integer_cap": str(all_integer_maximum),
                "unrestricted_maximizers": [a for a, v in vals if v == all_integer_maximum],
                "candidate_values": [{"a": a, "admissible": smooth13(a), "ratio": str(v)} for a, v in vals],
            })
    return {
        "schema": "T6_DISCRETE_ANNIHILATOR_MOMENT_CUT_EXACT_CONSTANTS_V1",
        "arithmetic": "fractions.Fraction exact rational arithmetic",
        "scientific_scope": "21 scalar maxima under the separately proved analytic cutoff",
        "not_executed": ["affine T6 census", "integer completion search", "old certificates"],
        "rows": rows,
    }


if __name__ == "__main__":
    print(json.dumps(extract(), indent=2) + "\n", end="")
