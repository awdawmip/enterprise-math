#!/usr/bin/env python3
"""Exact finite prefix of the positive atomic geometric-sampling countermodel.

This is an abstract exponent spectrum, not a zeta zero computation.  All
calculated quantities are rational.  A row (n, r, sign, weight) denotes
weight/2 times each of the two uniform n-gons at radii r and 2/r, with
z**n = sign * radius**n.  The initial row has n=2, radius=10/7, sign=+1,
and weight=1.  The infinite construction and its summable tail are proved
in POSITIVE_ATOMIC_ALIAS_COUNTERMODEL.md.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path


BASE = Fraction(2)
OUTER_SUPREMUM = Fraction(7, 4)
INITIAL_RADIUS = Fraction(10, 7)


def outer_radius(n: int) -> Fraction:
    level = n.bit_length() + 1  # floor(log_2 n) + 2, exactly.
    return OUTER_SUPREMUM * (
        1 - Fraction(1, 2 * level) - Fraction(1, 100 * n)
    )


def paired_radial_moment(k: int, radius: Fraction) -> Fraction:
    return (radius**k + (BASE / radius) ** k) / 2


def row_moment(k: int, row: dict) -> Fraction:
    n = row["order"]
    if k % n:
        return Fraction(0)
    return (
        row["weight"]
        * row["sign"] ** (k // n)
        * paired_radial_moment(k, row["radius"])
    )


def rat(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


def encode_row(row: dict) -> dict:
    return {
        "order": row["order"],
        "outer_radius": rat(row["radius"]),
        "inner_radius": rat(BASE / row["radius"]),
        "root_sign": row["sign"],
        "total_mass": rat(row["weight"]),
    }


def decode_row(row: dict) -> dict:
    def read_rat(item: dict) -> Fraction:
        return Fraction(int(item["numerator"]), int(item["denominator"]))

    return {
        "order": row["order"],
        "radius": read_rat(row["outer_radius"]),
        "sign": row["root_sign"],
        "weight": read_rat(row["total_mass"]),
    }


def construct(last_order: int) -> tuple[list[dict], list[dict]]:
    rows = [{"order": 2, "radius": INITIAL_RADIUS, "sign": 1, "weight": Fraction(1)}]
    stages = []
    for n in range(2, last_order + 1):
        residual = sum((row_moment(n, row) for row in rows), Fraction(0))
        radius = outer_radius(n)
        weight = abs(residual) / paired_radial_moment(n, radius)
        sign = -1 if residual > 0 else 1
        row = {"order": n, "radius": radius, "sign": sign, "weight": weight}
        rows.append(row)
        stages.append({"order": n, "uncorrected_moment": rat(residual), "added_mass": rat(weight)})
    return rows, stages


def main() -> None:
    # The deliberate exact rational certificate has large denominators.
    # Inputs are a locally bounded construction order, not untrusted integers.
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser()
    parser.add_argument("--last-order", type=int, default=64)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("atomic_moment_prefix.json"))
    args = parser.parse_args()
    if not 2 <= args.last_order <= 256:
        raise SystemExit("Choose an exact finite prefix between 2 and 256.")

    rows, stages = construct(args.last_order)
    encoded_rows = [encode_row(row) for row in rows]
    # Re-read the saved representation; the certificate checks the final
    # measure, rather than only the update made at a construction stage.
    decoded = [decode_row(row) for row in json.loads(json.dumps(encoded_rows))]
    moments = [sum((row_moment(k, row) for row in decoded), Fraction(0)) for k in range(1, args.last_order + 1)]
    if any(moments):
        raise AssertionError("An exact saved-prefix moment failed.")
    if any(row["weight"] < 0 for row in decoded):
        raise AssertionError("Negative atomic mass.")
    if any(not (row["radius"] ** 2 > BASE and row["radius"] < OUTER_SUPREMUM) for row in decoded):
        raise AssertionError("A radius escaped the required annulus.")
    radii = [row["radius"] for row in decoded]
    if any(left >= right for left, right in zip(radii, radii[1:])):
        raise AssertionError("Outer radii must increase strictly.")
    power_two_rows = [row for row in decoded[1:] if row["order"] & (row["order"] - 1) == 0]
    if any(row["weight"] <= 0 or row["sign"] != -1 for row in power_two_rows):
        raise AssertionError("The nonattainment witness at a power of two failed.")

    mass = sum((row["weight"] for row in decoded), Fraction(0))
    payload = {
        "status": "AUTHOR_RECOMPUTATION_ABSTRACT_COUNTERMODEL_NOT_ZETA",
        "author": "EM-DIRECT-E7559A",
        "activity": "RA-D2F111EA1C0D4B1DBEFBC1B4",
        "last_order": args.last_order,
        "base": rat(BASE),
        "outer_radius_supremum": rat(OUTER_SUPREMUM),
        "initial_radius": rat(INITIAL_RADIUS),
        "rows": encoded_rows,
        "construction_stages": stages,
        "final_positive_integer_moment_residuals": [rat(value) for value in moments],
        "finite_total_mass": rat(mass),
        "finite_total_mass_decimal_for_orientation_only": format(float(mass), ".17g"),
        "positive_correction_count": sum(row["weight"] > 0 for row in decoded[1:]),
        "power_two_positive_rows": [row["order"] for row in power_two_rows],
        "claims_not_certified_by_finite_prefix": [
            "Infinite summability is proved analytically in the accompanying note.",
            "These are not zeta zeros and do not have exactly canonical coefficients.",
            "A decimal orientation value is not a directed interval certificate.",
        ],
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "last_order": args.last_order,
        "all_exact_moments_zero": True,
        "positive_corrections": payload["positive_correction_count"],
        "power_two_positive_rows": payload["power_two_positive_rows"],
        "finite_mass_orientation_only": payload["finite_total_mass_decimal_for_orientation_only"],
        "output": str(args.output),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
