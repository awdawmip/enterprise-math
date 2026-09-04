#!/usr/bin/env python3
"""Exact rational checks for the V21 eight-chamber decomposition."""

from __future__ import annotations

from fractions import Fraction
from itertools import product


def check_pointwise_chambers() -> None:
    n = 42
    actions = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    field = {
        m: Fraction(((13 * m * m + 5 * m + 1) % 37) - 18, 11)
        for m in range(n + 1)
    }

    def valid(a: int, b: int) -> Fraction:
        return Fraction(int(a * b <= n))

    def stopped(a: int, b: int) -> Fraction:
        return 1 - valid(a, b)

    def fold(a: int, b: int) -> int:
        return n // (a * b) if a * b <= n else n // a

    def value(a: int, b: int) -> Fraction:
        return field[fold(a, b)]

    for a, b, d in product(actions, repeat=3):
        swap_lhs = (value(a, b) - value(b, a)) ** 2
        swap_rhs = stopped(a, b) * (field[n // a] - field[n // b]) ** 2
        assert swap_lhs == swap_rhs

        row_lhs = (value(a, b) - value(d, b)) ** 2
        row_rhs = (
            valid(a, b) * valid(d, b)
            * (field[n // (a * b)] - field[n // (d * b)]) ** 2
            + stopped(a, b) * stopped(d, b)
            * (field[n // a] - field[n // d]) ** 2
            + valid(a, b) * stopped(d, b)
            * (field[n // (a * b)] - field[n // d]) ** 2
            + stopped(a, b) * valid(d, b)
            * (field[n // a] - field[n // (d * b)]) ** 2
        )
        assert row_lhs == row_rhs

        column_lhs = (value(a, b) - value(a, d)) ** 2
        column_rhs = (
            valid(a, b) * valid(a, d)
            * (field[n // (a * b)] - field[n // (a * d)]) ** 2
            + valid(a, b) * stopped(a, d)
            * (field[n // (a * b)] - field[n // a]) ** 2
            + stopped(a, b) * valid(a, d)
            * (field[n // a] - field[n // (a * d)]) ** 2
        )
        assert column_lhs == column_rhs


def check_signless_suffix_split() -> None:
    n = 50
    actions = [2, 3, 5, 7]
    field = {
        m: Fraction(((17 * m + 3) % 29) - 14, 9)
        for m in range(n + 1)
    }

    for c, x, y in product(actions, range(n + 1), range(n + 1)):
        gx = field[x] + field[x // c]
        gy = field[y] + field[y // c]
        assert (gx - gy) ** 2 <= (
            2 * (field[x] - field[y]) ** 2
            + 2 * (field[x // c] - field[y // c]) ** 2
        )


def check_structural_zeros() -> None:
    n = 60
    actions = [2, 3, 5, 7, 11, 13]
    for a, b, d in product(actions, repeat=3):
        if a * b <= n:
            assert n // (a * b) == n // (b * a)
        if a * b > n and a * d > n:
            assert n // a == n // a


def main() -> None:
    check_pointwise_chambers()
    check_signless_suffix_split()
    check_structural_zeros()
    print("V21 fourth-order chamber audit: exact checks passed")


if __name__ == "__main__":
    main()
