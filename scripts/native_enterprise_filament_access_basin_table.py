#!/usr/bin/env python3
"""Generate/check the exact D2--D19 native filament access basin table."""

from __future__ import annotations

import csv
import math
from itertools import combinations
from pathlib import Path


PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67)


def step_gcd(S: tuple[int, ...]) -> int:
    base = S[0]
    g = 0
    for j in S[1:]:
        g = math.gcd(g, abs(j - base))
    return g


def information_set(S: tuple[int, ...], U: int) -> bool:
    mixed = any(j % 2 == 0 for j in S) and any(j % 2 == 1 for j in S)
    return mixed and math.gcd(step_gcd(S), U) == 1


def rows():
    P = 1
    for d, q in enumerate(PRIMES, start=1):
        P *= q
        if d < 2:
            continue
        U = P // 6
        for k in range(3, 10):
            counts = {
                s: sum(
                    information_set(S, U)
                    for S in combinations(range(k), s)
                )
                for s in range(2, k + 1)
            }
            yield {
                "collapse_dimension": d,
                "new_prime_channel": q,
                "primorial_modulus": P,
                "island_size_k": k,
                **{f"info_sets_size{s}": counts.get(s, 0) for s in range(2, 10)},
                "total_info_sets": sum(counts.values()),
            }


def main() -> None:
    table = list(rows())

    total_expected = {
        2: {3:3,4:9,5:21,6:49,7:105,8:225,9:465},
        3: {3:3,4:9,5:21,6:48,7:103,8:222,9:461},
        4: {3:3,4:9,5:21,6:48,7:103,8:221,9:459},
    }
    for row in table:
        d = row["collapse_dimension"]
        k = row["island_size_k"]
        stage = 2 if d == 2 else 3 if d == 3 else 4
        assert row["total_info_sets"] == total_expected[stage][k]

        E = (k + 1) // 2
        O = k // 2
        for s in range(3, k + 1):
            closed = math.comb(k, s) - math.comb(E, s) - math.comb(O, s)
            assert row[f"info_sets_size{s}"] == closed

    # Explicit stabilization after d=4.
    by_k = {}
    for row in table:
        if row["collapse_dimension"] >= 4:
            sig = tuple(row[f"info_sets_size{s}"] for s in range(2, 10))
            by_k.setdefault(row["island_size_k"], set()).add(sig)
    assert all(len(v) == 1 for v in by_k.values())

    fields = [
        "collapse_dimension", "new_prime_channel", "primorial_modulus",
        "island_size_k", *[f"info_sets_size{s}" for s in range(2,10)],
        "total_info_sets",
    ]

    out = Path("native_enterprise_filament_access_basin_d2_d19.csv")
    with out.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(table)

    print("ROWS=126")
    print("D2_D19_ACCESS_BASIN=PASS")
    print("THREE_PLUS_PROBE_COUNTS=DIMENSION_STABLE")
    print("TWO_PROBE_STAGES=D2,D3,D4_STABLE")
    print(f"CSV={out}")


if __name__ == "__main__":
    main()
