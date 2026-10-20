#!/usr/bin/env python3
"""Exact checker for the native Enterprise arrangement-lift bifurcation."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb
from pathlib import Path
import csv


def eta_mod(j: int, chi: int, modulus: int) -> int:
    return ((3 * j * j + chi * (j & 1)) * pow(2, -1, modulus)) % modulus


def spectrum_ring(k: int, modulus: int, chi: int) -> Counter[int]:
    out: Counter[int] = Counter()
    eta = [eta_mod(j, chi, modulus) for j in range(k)]
    for a in range(modulus):
        for b in range(modulus):
            zeros = sum(
                (a + b * j + eta[j]) % modulus == 0
                for j in range(k)
            )
            out[zeros] += 1
    return out


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def first_nonsquare(p: int) -> int:
    for d in range(2, p):
        if legendre(d, p) == -1:
            return d
    raise AssertionError(p)


def add2(x: tuple[int, int], y: tuple[int, int], p: int) -> tuple[int, int]:
    return ((x[0] + y[0]) % p, (x[1] + y[1]) % p)


def scale2(c: int, x: tuple[int, int], p: int) -> tuple[int, int]:
    return ((c * x[0]) % p, (c * x[1]) % p)


def spectrum_field_q2(k: int, p: int, chi: int) -> Counter[int]:
    # Pair representation a+b*u; only addition and base-field scaling are needed.
    _ = first_nonsquare(p)
    elems = [(x, y) for x in range(p) for y in range(p)]
    eta = [eta_mod(j, chi, p) for j in range(k)]
    out: Counter[int] = Counter()
    for a in elems:
        for b in elems:
            zeros = 0
            for j in range(k):
                v = add2(add2(a, scale2(j, b, p), p), (eta[j], 0), p)
                zeros += v == (0, 0)
            out[zeros] += 1
    return out


def eta_frac(j: int, chi: int = 1) -> Fraction:
    return Fraction(3 * j * j + chi * (j & 1), 2)


def intersection_slope(i: int, j: int, chi: int = 1) -> Fraction:
    return -(eta_frac(j, chi) - eta_frac(i, chi)) / (j - i)


def vandermonde(values: list[Fraction]) -> Fraction:
    ans = Fraction(1, 1)
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            ans *= values[j] - values[i]
    return ans


def defect_from_spectrum(k: int, spec: Counter[int]) -> int:
    b = sum((m - 1) * count for m, count in spec.items() if m >= 2)
    return comb(k, 2) - b


def main() -> None:
    k = 9
    expected = {
        (11, 1): (18, 4, 1, 7, 51),
        (11, -1): (18, 4, 1, 7, 51),
        (13, 1): (24, 4, 0, 4, 84),
        (13, -1): (27, 3, 0, 3, 85),
        (23, 1): (24, 4, 0, 4, 354),
        (23, -1): (24, 2, 1, 5, 353),
        (31, 1): (30, 2, 0, 2, 716),
        (31, -1): (30, 2, 0, 2, 716),
        (53, 1): (30, 2, 0, 2, 2366),
        (53, -1): (30, 2, 0, 2, 2366),
    }

    rows = []
    for (q, chi), exp in expected.items():
        spec = spectrum_ring(k, q, chi)
        got = (spec[2], spec[3], spec[4], defect_from_spectrum(k, spec), spec[0])
        assert got == exp, (q, chi, got, exp)
        b = comb(k, 2) - got[3]
        assert spec[0] == q * q - k * q + b
        rows.append((q, chi, *got, b))

    # Exact second-layer contrast.
    field_counts = {}
    ring_counts = {}
    for q in (13, 23):
        for chi in (1, -1):
            f = spectrum_field_q2(k, q, chi)
            r = spectrum_ring(k, q * q, chi)
            field_counts[(q, chi)] = f[0]
            ring_counts[(q, chi)] = r[0]
            assert defect_from_spectrum(k, r) == 0
            assert r[0] == q**4 - k * q**2 + comb(k, 2)

    assert field_counts[(13, 1)] == 27072
    assert field_counts[(13, -1)] == 27073
    assert ring_counts[(13, 1)] == ring_counts[(13, -1)] == 27076

    assert field_counts[(23, 1)] == 275112
    assert field_counts[(23, -1)] == 275111
    assert ring_counts[(23, 1)] == ring_counts[(23, -1)] == 275116

    # Boundary discriminant quotient.
    left = [intersection_slope(0, j, 1) for j in range(1, k)]
    right = [intersection_slope(k, j, 1) for j in range(1, k)]
    ratio = abs(vandermonde(left) / vandermonde(right))
    assert ratio == Fraction(91, 529)

    csv_path = Path(__file__).with_name(
        "NATIVE_ENTERPRISE_K9_ARRANGEMENT_DEFECT_AND_LIFT_20260824.csv"
    )
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow([
            "q", "chi", "n2", "n3", "n4", "defect_delta",
            "all_unit_Fq", "characteristic_constant_b",
            "all_unit_Fq2", "all_unit_Zmodq2"
        ])
        for q, chi, n2, n3, n4, delta, n0, b in rows:
            writer.writerow([
                q, chi, n2, n3, n4, delta, n0, b,
                field_counts.get((q, chi), ""),
                ring_counts.get((q, chi), "")
            ])

    print("ARRANGEMENT_CHARACTERISTIC_POLYNOMIAL=PASS")
    print("DEFECT_IDENTITY=PASS")
    print("K9_EXCEPTIONAL_DEFECT_TABLE=PASS")
    print("FQ2_UNRAMIFIED_DEFECT_PERSISTENCE=PASS q=13,23")
    print("ZQ2_RAMIFIED_DEFECT_HEALING=PASS q=13,23")
    print("BOUNDARY_DISCRIMINANT_RATIO=91/529=7*13/23^2")
    print("K9_CHIRAL_FIELD_COUNTS_Q13=27072/27073")
    print("K9_CHIRAL_FIELD_COUNTS_Q23=275112/275111")
    print("K9_CHIRAL_RING_COUNTS_Q13=27076/27076")
    print("K9_CHIRAL_RING_COUNTS_Q23=275116/275116")
    print(f"CSV={csv_path}")


if __name__ == "__main__":
    main()
