"""Exact finite X6 raw-marginal recovery experiment, not Foundation admission.

Uses the observer adapter (and its BRC histograms) plus SymPy's rational
simplex. A <=7-support feasible answer certifies uniqueness among ALL finite
nonnegative spatial measures by OWNER-FREE-20260907-3MARGINAL-7V8.
It does not recover branch labels, path histories, or min-zero-only data.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import combinations, product
import json
from pathlib import Path
from typing import Mapping

from sympy import Matrix, Rational
from sympy.solvers.simplex import InfeasibleLPError, linprog

from observer_certificate import Branch, all_three_axis_tables, parity_branches

AXES = tuple(combinations(range(6), 3))
Table = dict[tuple[int, ...], Fraction]
Marginals = dict[tuple[int, ...], Table]


def validate_tables(tables: Mapping) -> Marginals:
    """Require all labeled raw-coordinate tables; absent entries mean zero."""
    if any(not isinstance(axes, tuple) or len(axes) != 3
           or any(type(axis) is not int for axis in axes) or axes not in AXES
           for axes in tables):
        raise ValueError("axis labels must be sorted triples of distinct integer axes")
    if set(tables) != set(AXES):
        raise ValueError("exactly the 20 sorted raw three-axis tables are required")
    result = {}
    for axes in AXES:
        table = {}
        for address, mass in tables[axes].items():
            if not isinstance(address, tuple) or len(address) != 3 or any(type(v) is not int for v in address):
                raise ValueError("raw addresses must be three signed integers")
            if isinstance(mass, bool) or not isinstance(mass, (int, Fraction)):
                raise TypeError("masses must be exact int or Fraction")
            if mass < 0:
                raise ValueError("negative marginal mass is forbidden")
            if mass:
                table[address] = Fraction(mass)
        result[axes] = table
    totals = {sum(t.values(), Fraction()) for t in result.values()}
    if len(totals) != 1:
        raise ValueError("marginal totals disagree")
    return result


def candidate_join(tables: Marginals) -> tuple[tuple[int, ...], ...]:
    """Every nonnegative feasible support lies in this complementary join.

    If the generating measure has s support points, each complementary table
    has <=s addresses, so at most s**2 candidates are tested before filtering.
    """
    candidates = []
    for left, right in product(tables[(0, 1, 2)], tables[(3, 4, 5)]):
        coordinate = left + right
        if all(tuple(coordinate[a] for a in axes) in tables[axes] for axes in AXES):
            candidates.append(coordinate)
    return tuple(sorted(candidates))


def recover(tables: Mapping, *, max_candidates: int = 256) -> dict:
    """Return a verified measure and a conservative mathematical status.

    More than seven recovered support points is NOT an ambiguity certificate.
    The prototype reports uniqueness as unclassified in that case.
    """
    tables = validate_tables(tables)
    if type(max_candidates) is not int or max_candidates < 1:
        raise ValueError("max_candidates must be a positive integer")
    total = sum(tables[AXES[0]].values(), Fraction())
    if not total:
        return {"status": "UNIQUE_ZERO", "candidate_count": 0, "support_count": 0, "distribution": ()}
    join_size = len(tables[(0, 1, 2)]) * len(tables[(3, 4, 5)])
    if join_size > max_candidates:
        raise ValueError("declared candidate budget exceeded; no mathematical conclusion")
    candidates = candidate_join(tables)
    if not candidates:
        raise ValueError("no nonnegative spatial distribution fits the support tables")
    rows, rhs = [], []
    for axes in AXES:
        for address, mass in sorted(tables[axes].items()):
            rows.append([int(tuple(z[a] for a in axes) == address) for z in candidates])
            rhs.append(Rational(mass.numerator, mass.denominator))
    width = len(candidates)
    reduced, pivots = Matrix([row + [value] for row, value in zip(rows, rhs)]).rref()
    if width in pivots:
        raise ValueError("exact row reduction proves inconsistent marginal equations")
    free = [column for column in range(width) if column not in pivots]
    # x_p = b_p - sum_j R[p,j] t_j; each free variable t_j is itself
    # a spatial mass, so its default nonnegative bound is legitimate.
    values = [Rational(0)] * width
    for row, column in enumerate(pivots):
        values[column] = reduced[row, width]
    if any(value < 0 for value in values):
        if not free:
            raise ValueError("unique linear solution has negative mass")
        inequalities = [[reduced[row, column] for column in free] for row in range(len(pivots))]
        bounds = [reduced[row, width] for row in range(len(pivots))]
        try:
            _, parameters = linprog([0] * len(free), inequalities, bounds)
        except InfeasibleLPError as exc:
            raise ArithmeticError("solver did not return a feasible point; no verified infeasibility certificate") from exc
        for column, value in zip(free, parameters):
            values[column] = value
        for row, column in enumerate(pivots):
            values[column] = reduced[row, width] - sum(
                reduced[row, j] * values[j] for j in free
            )
    distribution = tuple(
        (z, Fraction(value)) for z, value in zip(candidates, values) if value
    )
    if any(mass < 0 for _, mass in distribution):
        raise ArithmeticError("solver returned negative mass")
    recovered = tuple(Branch(f"recovered:{i}", z, mass) for i, (z, mass) in enumerate(distribution))
    if all_three_axis_tables(recovered) != tables:
        raise ArithmeticError("solver answer failed exact BRC marginal verification")
    count = len(distribution)
    return {
        "status": "UNIQUE_BY_SUPPORT_BOUND" if count < 8 else "FEASIBLE_UNIQUENESS_UNCLASSIFIED",
        "candidate_count": len(candidates), "prefilter_join_count": join_size,
        "equation_rank": len(pivots), "free_mass_variables": len(free),
        "support_count": count, "distribution": distribution,
    }


def _serializable(result: dict) -> dict:
    return {**result, "distribution": [
        {"coordinate": list(z), "mass": str(mass)} for z, mass in result["distribution"]
    ]}


def demonstration() -> dict:
    # A deleted point from the sharp eight-point parity witness is a difficult
    # sparse case: the join retains spurious points which exact equations remove.
    seven = parity_branches(0)[:-1]
    weighted = tuple(Branch(b.label, b.coordinate, Fraction(i + 1, i + 2)) for i, b in enumerate(seven))
    cases = {"seven_equal": seven, "seven_rational": weighted,
             "eight_ambiguous": parity_branches(0), "empty": ()}
    output = {}
    for name, source in cases.items():
        result = recover(all_three_axis_tables(source))
        if len(source) < 8:
            assert dict(result["distribution"]) == {b.coordinate: b.weight for b in source}
        else:
            assert result["status"] == "FEASIBLE_UNIQUENESS_UNCLASSIFIED"
            assert all_three_axis_tables(source) == all_three_axis_tables(parity_branches(1))
        output[name] = _serializable(result)
    return {"status": "PASS", "arithmetic": "exact rational", "cases": output,
            "scope": "raw signed spatial marginals only; no label/provenance recovery"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = json.dumps(demonstration(), ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(payload + "\n", encoding="utf-8", newline="\n")
    else:
        print(payload)
