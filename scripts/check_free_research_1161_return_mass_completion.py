"""Finite integer return-mass completion checker for free research #1161.

For 2n time slots, each slot carries two independent binary labels.  There are
16^n total paired histories.  Requiring each binary coordinate to be balanced
selects binom(2n,n)^2 histories, so

    c_n = binom(2n,n)^2 / 16^n

is the exact positive-rational return mass.

The #1159 Wallis tail certificate plus the exact finite relation
(2n+1)c_n W_n=1 yields

    2/((2n+1)c_n) < tau <= 4/((4n+1)c_n).

After the #1161 power-series/Wronskian closure tau=Pi_*, these are pure integer
finite certificates for the endogenous AGM completion constant.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb


def return_count(n: int) -> int:
    if n < 0:
        raise ValueError("n must be nonnegative")
    return comb(2 * n, n) ** 2


def total_count(n: int) -> int:
    if n < 0:
        raise ValueError("n must be nonnegative")
    return 16**n


def return_mass(n: int) -> Fraction:
    return Fraction(return_count(n), total_count(n))


def completion_bounds(n: int) -> tuple[Fraction, Fraction]:
    if n < 1:
        raise ValueError("n must be positive")
    count = return_count(n)
    total = total_count(n)
    lower = Fraction(2 * total, (2 * n + 1) * count)
    upper = Fraction(4 * total, (4 * n + 1) * count)
    return lower, upper


def decimal_cell(x: Fraction, digits: int) -> int:
    scale = 10**digits
    return (x.numerator * scale) // x.denominator


def format_cell(cell: int, digits: int) -> str:
    text = str(cell)
    if len(text) <= digits:
        text = "0" * (digits + 1 - len(text)) + text
    return text[:-digits] + "." + text[-digits:]


def run() -> dict[str, object]:
    # Exact coefficient recurrence regression.
    for n in range(0, 1000):
        c0 = return_mass(n)
        c1 = return_mass(n + 1)
        expected_ratio = Fraction((2 * n + 1) ** 2, (2 * n + 2) ** 2)
        if c1 != c0 * expected_ratio:
            raise AssertionError(f"return-mass recurrence failed at n={n}")

    n = 10_000
    lo, hi = completion_bounds(n)
    lo_cell = decimal_cell(lo, 4)
    hi_cell = decimal_cell(hi, 4)
    if lo_cell != hi_cell:
        raise AssertionError("completion interval does not share four decimals")

    # The width is itself an exact rational finite certificate.
    width = hi - lo
    if width <= 0:
        raise AssertionError("completion bracket width must be positive")

    return {
        "recurrence_cases": 1000,
        "certificate_n": n,
        "shared_decimal_cell_4": format_cell(lo_cell, 4),
        "lower_lt_upper": lo < hi,
        "integer_only_count_formula": True,
    }


if __name__ == "__main__":
    result = run()
    expected = {
        "recurrence_cases": 1000,
        "certificate_n": 10_000,
        "shared_decimal_cell_4": "3.1415",
        "lower_lt_upper": True,
        "integer_only_count_formula": True,
    }
    if result != expected:
        raise SystemExit(f"unexpected return-mass result: {result!r}")
    for key, value in result.items():
        print(f"{key}={value}")
