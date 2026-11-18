#!/usr/bin/env python3
"""Scoped exact audit: old 3-positive/min-zero NSIA shell vs pinned X6 signed L1 shell.
This never claims that the 2026-08-27 frozen accepted NSIA theorem is invalid.
"""
from __future__ import annotations
import json
from itertools import product
from math import comb, factorial


def stirling2(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    return sum((-1) ** (k - j) * comb(k, j) * j ** n for j in range(k + 1)) // factorial(k)


def native_endpoint_formula(n: int) -> int:
    return sum(2 ** k * comb(6, k) * comb(n - 1, k - 1)
               for k in range(1, min(6, n) + 1))


def native_brc_formula(n: int) -> int:
    return sum(2 ** k * comb(6, k) * factorial(k) * stirling2(n, k)
               for k in range(1, min(6, n) + 1))


def direct_signed_shell(n: int) -> tuple[int, int]:
    # Exact native signed X6 grade: sum |z_i| = n.
    # Direct cartesian enumeration in [-n,n]^6 is too wasteful for high n;
    # signed compositions are still an independent endpoint construction.
    count = mass = 0
    fact = factorial(n)
    def visit(axis: int, remaining: int, denominator: int) -> None:
        nonlocal count, mass
        if axis == 6:
            if remaining == 0:
                count += 1
                mass += fact // denominator
            return
        for absolute in range(remaining + 1):
            sign_choices = 1 if absolute == 0 else 2
            for _ in range(sign_choices):
                visit(axis + 1, remaining - absolute,
                      denominator * factorial(absolute))
    visit(0, n, 1)
    return count, mass


def legacy_shell(n: int) -> int:
    return sum(1 for a in range(n + 1) for b in range(n + 1)
               for c in range(n + 1) if a + b + c == n and min(a, b, c) == 0)


def main() -> None:
    rows = []
    for n in range(1, 9):
        e, brc = direct_signed_shell(n)
        ef, bf = native_endpoint_formula(n), native_brc_formula(n)
        old = legacy_shell(n)
        if not (e == ef and brc == bf and old == 3*n and e > old):
            raise RuntimeError((n, e, ef, brc, bf, old))
        rows.append({"grade": n, "historical_three_ray_shell": old,
                     "native_signed_x6_endpoints": e, "native_signed_x6_brc_mass": brc})
    out = {"schema": "X6_UNIT143_SCOPED_NSIA_TYPE_AUDIT_V1",
           "frozen_native_source": "59538f585d037d09ef687b28715c4bc1a3f9fe03",
           "frozen_old_ontology": "fd2bcff10ca6e147348b6c1236027fc0d2877df3",
           "original_legacy_script_blob": "f5c9a6045571128281554706f3f31d88f1caf9a9",
           "checked_grades": 8, "verification": "exact_integer_direct_signed_compositions_vs_closed_count_and_Stirling_BRC_formula",
           "rows": rows, "verdict": "PASS_TYPED_NONIDENTITY_NO_OLD_RESULT_MUTATION"}
    print(json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
