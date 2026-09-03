"""Exact dyadic certificate experiment for Enterprise Math free research #1161.

This checker uses only Python's standard-library integer/rational arithmetic.
It never evaluates pi and never calls floating-point sqrt.

Mathematical inputs proved in the accompanying research note:

* a_{n+1}=(a_n+b_n)/2, b_{n+1}=sqrt(a_n b_n),
  A_{n+1}=A_n-P_n(a_n-b_n)^2, P_n=2^n;
* the AGM pair has a common limit M and Pi_* := (2M)^2/A_infinity;
* with H_n=a_n+b_n, V_n=2sqrt(a_n b_n), delta_n=P_n(a_n-b_n)^2,
  one has V_n <= 2M <= H_n;
* delta_{n+1}<delta_n/2, hence
  A_n-2 delta_n <= A_infinity <= A_n.

Therefore any rigorous interval enclosures imply

    V_n^2/A_n <= Pi_* <= H_n^2/(A_n-2 delta_n).

The square-root enclosures below are dyadic and are obtained by integer isqrt
on a scaled rational radicand.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import isqrt


@dataclass(frozen=True)
class Interval:
    lo: Fraction
    hi: Fraction

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise ValueError("invalid interval")


def sqrt_bounds(q: Fraction, bits: int) -> Interval:
    """Return dyadic [lo, hi] containing sqrt(q), with denominator 2**bits."""
    if q < 0:
        raise ValueError("sqrt radicand must be nonnegative")
    if q == 0:
        return Interval(Fraction(0), Fraction(0))
    scale = 1 << bits
    scaled_num = q.numerator * scale * scale
    den = q.denominator
    k = isqrt(scaled_num // den)
    lo = Fraction(k, scale)
    if k * k * den == scaled_num:
        hi = lo
    else:
        hi = Fraction(k + 1, scale)
    if not (lo * lo <= q <= hi * hi):
        raise AssertionError("sqrt enclosure failed")
    return Interval(lo, hi)


def sqrt_interval(x: Interval, bits: int) -> Interval:
    left = sqrt_bounds(x.lo, bits).lo
    right = sqrt_bounds(x.hi, bits).hi
    return Interval(left, right)


def mul_positive(x: Interval, y: Interval) -> Interval:
    if x.lo < 0 or y.lo < 0:
        raise ValueError("positive interval multiplication expected")
    return Interval(x.lo * y.lo, x.hi * y.hi)


def square_positive(x: Interval) -> Interval:
    if x.lo < 0:
        raise ValueError("positive interval square expected")
    return Interval(x.lo * x.lo, x.hi * x.hi)


def common_decimal_cell(lo: Fraction, hi: Fraction, max_digits: int = 100) -> tuple[int, int] | None:
    """Largest d for which lo and hi lie in the same 10^-d half-open cell."""
    best: tuple[int, int] | None = None
    for digits in range(max_digits + 1):
        scale = 10**digits
        left = (lo.numerator * scale) // lo.denominator
        right = (hi.numerator * scale) // hi.denominator
        if left != right:
            break
        best = (digits, left)
    return best


def format_decimal_cell(digits: int, cell: int) -> str:
    if digits == 0:
        return str(cell)
    text = str(cell)
    if len(text) <= digits:
        text = "0" * (digits + 1 - len(text)) + text
    return text[:-digits] + "." + text[-digits:]


def run(bits: int = 300, steps: int = 4) -> list[tuple[int, int, str]]:
    if bits < 32:
        raise ValueError("use at least 32 dyadic bits")
    if steps < 1:
        raise ValueError("steps must be positive")

    one = Fraction(1)
    a = Interval(one, one)
    b = sqrt_bounds(Fraction(1, 2), bits)
    A = Interval(one, one)
    P = 1

    results: list[tuple[int, int, str]] = []

    for n in range(steps + 1):
        H = Interval(a.lo + b.lo, a.hi + b.hi)
        U = Interval(a.lo - b.hi, a.hi - b.lo)
        if U.lo <= 0:
            raise AssertionError("AGM gap enclosure lost positivity")

        root_ab = sqrt_interval(mul_positive(a, b), bits)
        V = Interval(2 * root_ab.lo, 2 * root_ab.hi)

        delta = square_positive(U)
        delta = Interval(P * delta.lo, P * delta.hi)

        Ainf_lo = A.lo - 2 * delta.hi
        if Ainf_lo <= 0:
            raise AssertionError("tail certificate did not preserve positive denominator")

        lower = V.lo * V.lo / A.hi
        upper = H.hi * H.hi / Ainf_lo
        if lower > upper:
            raise AssertionError("Pi_* bracket inverted")

        cell = common_decimal_cell(lower, upper)
        if cell is not None:
            digits, cell_id = cell
            if digits > 0:
                results.append((n, digits, format_decimal_cell(digits, cell_id)))

        if n == steps:
            break

        next_a = Interval(H.lo / 2, H.hi / 2)
        next_b = root_ab
        next_A = Interval(A.lo - delta.hi, A.hi - delta.lo)
        a, b, A = next_a, next_b, next_A
        P *= 2

    return results


if __name__ == "__main__":
    result = run()
    expected = [
        (1, 2, "3.14"),
        (2, 7, "3.1415926"),
        (3, 18, "3.141592653589793238"),
        (4, 39, "3.141592653589793238462643383279502884197"),
    ]
    if result != expected:
        raise SystemExit(f"unexpected certificate output: {result!r}")
    for n, digits, prefix in result:
        print(f"n={n}: certified_decimal_places={digits} prefix={prefix}")
