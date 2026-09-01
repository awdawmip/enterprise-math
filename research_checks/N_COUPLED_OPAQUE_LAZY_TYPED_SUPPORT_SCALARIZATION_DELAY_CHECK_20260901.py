#!/usr/bin/env python3
from __future__ import annotations

from itertools import combinations
from math import gcd


def det_bareiss(matrix: list[list[int]]) -> int:
    a = [row[:] for row in matrix]
    n = len(a)
    if n == 0:
        return 1
    sign = 1
    prev = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot_row = next((i for i in range(k + 1, n) if a[i][k] != 0), None)
            if pivot_row is None:
                return 0
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * pivot - a[i][k] * a[k][j]) // prev
        for i in range(k + 1, n):
            a[i][k] = 0
        prev = pivot
    return sign * a[-1][-1]


def reflection_rows_cyclic(d: int) -> list[list[int]]:
    rows: list[list[int]] = []
    zero = [0] * d
    zero[0] = 1
    rows.append(zero)
    for x in range(d):
        for y in range(d):
            z = (x + y) % d
            row = [0] * d
            row[x] += 1
            row[y] += 1
            row[z] -= 1
            rows.append(row)
    return rows


def closure_from_generator(d: int) -> list[int]:
    seen = {0, 1 % d}
    while True:
        grown = seen | {(x + y) % d for x in seen for y in seen}
        if grown == seen:
            return sorted(seen)
        seen = grown


def rank_mod(matrix: list[list[int]], p: int) -> int:
    a = [[x % p for x in row] for row in matrix]
    m = len(a)
    n = len(a[0]) if m else 0
    rank = 0
    for col in range(n):
        pivot = next((i for i in range(rank, m) if a[i][col] % p), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, p)
        a[rank] = [(v * inv) % p for v in a[rank]]
        for i in range(m):
            if i != rank and a[i][col] % p:
                factor = a[i][col] % p
                a[i] = [(u - factor * v) % p for u, v in zip(a[i], a[rank])]
        rank += 1
    return rank


def gcd_maximal_minors(rows: list[list[int]]) -> tuple[int, int]:
    ncols = len(rows[0])
    g = 0
    count = 0
    for idxs in combinations(range(len(rows)), ncols):
        minor = [rows[i] for i in idxs]
        g = gcd(g, abs(det_bareiss(minor)))
        count += 1
    return g, count


def main() -> int:
    total_minors = 0
    reflection_cases = 0
    for d in (2, 3, 4, 5):
        assert closure_from_generator(d) == list(range(d))
        rows = reflection_rows_cyclic(d)
        divisor, count = gcd_maximal_minors(rows)
        total_minors += count
        reflection_cases += 1
        assert divisor == d, (d, divisor)

    n = 15
    rows3 = reflection_rows_cyclic(3)
    rows5 = reflection_rows_cyclic(5)
    d3, _ = gcd_maximal_minors(rows3)
    d5, _ = gcd_maximal_minors(rows5)
    assert gcd(n, d3) == 3
    assert gcd(n, d5) == 5
    assert rank_mod(rows3, 3) == 2 and rank_mod(rows3, 5) == 3
    assert rank_mod(rows5, 3) == 5 and rank_mod(rows5, 5) == 4

    print(
        "PASS N_COUPLED_OPAQUE_REFLECTION "
        f"reflection_cases={reflection_cases} maximal_minors={total_minors} "
        "N15_one_sided_cases=2"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
