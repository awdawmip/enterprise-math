#!/usr/bin/env python3
"""Exact combinatorial checks for prime-winding logarithmic cutoff chambers.

The chamber volumes are checked through integer numerators: after multiplying
by ``r!``, the total chamber of image size ``j`` has multiplicity
``r.descFactorial(j) * S(r,j)``.  All calculations are exact integers or
``Fraction``.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, factorial


def stirling_second(n: int, k: int) -> int:
    if n == 0:
        return 1 if k == 0 else 0
    if k == 0:
        return 0
    return stirling_second(n - 1, k - 1) + k * stirling_second(n - 1, k)


def desc_factorial(n: int, k: int) -> int:
    assert 0 <= k <= n
    out = 1
    for j in range(k):
        out *= n - j
    return out


def image_chamber_count(r: int, j: int) -> int:
    assert 0 <= j <= r
    return stirling_second(r, j) * desc_factorial(r, j)


def fixed_overcut_volume(r: int, k: int) -> Fraction:
    """Volume for one prescribed set of k coordinates exceeding cutoff 1."""
    assert 0 <= k <= r
    j = r - k
    numerator = sum(
        (-1) ** h * comb(j, h) * (j - h) ** r
        for h in range(j + 1)
    )
    return Fraction(numerator, factorial(r))


def total_overcut_volume(r: int, k: int) -> Fraction:
    return comb(r, k) * fixed_overcut_volume(r, k)


def check_stirling_inclusion_exclusion(max_degree: int = 10) -> None:
    for r in range(1, max_degree + 1):
        for k in range(r + 1):
            j = r - k
            fixed = fixed_overcut_volume(r, k)
            assert fixed == Fraction(factorial(j) * stirling_second(r, j), factorial(r))
            total = total_overcut_volume(r, k)
            assert total == Fraction(stirling_second(r, j), factorial(k))
            assert factorial(r) * total == image_chamber_count(r, j)


def check_total_simplex_partition(max_degree: int = 10) -> None:
    for r in range(1, max_degree + 1):
        count_sum = sum(image_chamber_count(r, j) for j in range(r + 1))
        assert count_sum == r**r

        volume_sum = sum(
            (total_overcut_volume(r, k) for k in range(r + 1)),
            Fraction(0, 1),
        )
        assert volume_sum == Fraction(r**r, factorial(r))


def check_low_degree_chambers() -> None:
    assert [image_chamber_count(2, j) for j in range(3)] == [0, 2, 2]
    assert [image_chamber_count(3, j) for j in range(4)] == [0, 3, 18, 6]

    degree_three_by_deficiency = [
        image_chamber_count(3, 3 - k) for k in range(3)
    ]
    assert degree_three_by_deficiency == [6, 18, 3]
    assert sum(degree_three_by_deficiency) == 27

    normalized = [Fraction(value, 27) for value in degree_three_by_deficiency]
    assert normalized == [Fraction(2, 9), Fraction(2, 3), Fraction(1, 9)]

    # The core is the 3! permutation sector; the deepest chamber is the
    # constant-map sector and has the same 1/9 coefficient as S3 energy survival.
    assert degree_three_by_deficiency[0] == factorial(3)
    assert normalized[-1] == Fraction(1, 9)


def check_function_image_count(max_degree: int = 7) -> None:
    # Independent direct count for small r: functions [r] -> [r] grouped by image size.
    from itertools import product

    for r in range(1, max_degree + 1):
        direct = [0] * (r + 1)
        for values in product(range(r), repeat=r):
            direct[len(set(values))] += 1
        expected = [image_chamber_count(r, j) for j in range(r + 1)]
        assert direct == expected


def main() -> None:
    check_stirling_inclusion_exclusion()
    check_total_simplex_partition()
    check_low_degree_chambers()
    check_function_image_count()
    print("prime-winding Stirling chamber checks: PASS")


if __name__ == "__main__":
    main()
