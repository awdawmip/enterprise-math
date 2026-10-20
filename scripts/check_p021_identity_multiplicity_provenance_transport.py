#!/usr/bin/env python3
"""Deterministic checker for the P021 identity/multiplicity/provenance continuation.

This checker assumes the previously frozen common-order normalization: after
transporting labels along the forced one-step matchings, every one-step support
is upper triangular with the diagonal present.  It verifies the new
multiplicity/provenance claims only; it does not re-prove the older common-order
identity theorem.
"""

from __future__ import annotations

from itertools import product
from math import comb


def eye(n: int) -> list[list[int]]:
    return [[int(i == j) for j in range(n)] for i in range(n)]


def matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    n = len(a)
    return [
        [sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)]
        for i in range(n)
    ]


def support(a: list[list[int]]) -> list[list[int]]:
    return [[int(x > 0) for x in row] for row in a]


def add(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[x + y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def sub(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[x - y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def upper_supports(n: int):
    """All 0/1 upper-triangular supports with every diagonal entry equal to 1."""
    positions = [(i, j) for i in range(n) for j in range(i + 1, n)]
    for bits in product((0, 1), repeat=len(positions)):
        a = eye(n)
        for (i, j), bit in zip(positions, bits):
            a[i][j] = bit
        yield a


def zeta_upper(n: int) -> list[list[int]]:
    return [[int(i <= j) for j in range(n)] for i in range(n)]


def verify_sequence(seq: tuple[list[list[int]], ...]) -> int:
    """Verify support, defect recurrence, and the sharp common-order upper bound."""
    n = len(seq[0])
    h = len(seq)
    count = eye(n)
    bool_support = eye(n)
    defect = [[0] * n for _ in range(n)]

    for step in seq:
        next_count = matmul(count, step)

        support_join_count = matmul(bool_support, step)
        next_bool = support(support_join_count)
        new_collision = sub(support_join_count, next_bool)

        next_defect = add(matmul(defect, step), new_collision)

        assert next_bool == support(next_count)
        assert next_defect == sub(next_count, next_bool)
        assert all(x >= 0 for row in next_defect for x in row)

        count = next_count
        bool_support = next_bool
        defect = next_defect

    for i in range(n):
        for j in range(n):
            if i > j:
                assert count[i][j] == 0
                continue
            d = j - i
            assert count[i][j] <= comb(h + d - 1, d)

    zero_defect = all(x == 0 for row in defect for x in row)
    all_endpoint_path_counts_at_most_one = all(
        x <= 1 for row in count for x in row
    )
    assert zero_defect == all_endpoint_path_counts_at_most_one

    return max(x for row in count for x in row)


def main() -> None:
    exhaustive = []
    for n in range(1, 4):
        supports = tuple(upper_supports(n))
        for h in range(1, 4):
            checked = 0
            max_multiplicity = 0
            for seq in product(supports, repeat=h):
                max_multiplicity = max(max_multiplicity, verify_sequence(seq))
                checked += 1
            exhaustive.append(
                {
                    "n": n,
                    "h": h,
                    "sequences": checked,
                    "max_endpoint_multiplicity": max_multiplicity,
                }
            )

    sharp_checks = []
    for n in range(1, 7):
        z = zeta_upper(n)
        count = eye(n)
        for h in range(1, 9):
            count = matmul(count, z)
            for i in range(n):
                for j in range(i, n):
                    d = j - i
                    assert count[i][j] == comb(h + d - 1, d)
            sharp_checks.append({"n": n, "h": h})

    u = [[1, 1], [0, 1]]
    count = eye(2)
    minimal_family = []
    for h in range(1, 9):
        count = matmul(count, u)
        assert count == [[1, h], [0, 1]]
        assert support(count) == u
        minimal_family.append(
            {
                "h": h,
                "count_1_to_2": h,
                "boolean_support_1_to_2": 1,
                "erased_extra_provenance": h - 1,
            }
        )

    print(
        {
            "status": "PASS",
            "exhaustive_common_order_sequences": exhaustive,
            "sharp_zeta_checks": len(sharp_checks),
            "minimal_two_label_family": minimal_family,
        }
    )


if __name__ == "__main__":
    main()
