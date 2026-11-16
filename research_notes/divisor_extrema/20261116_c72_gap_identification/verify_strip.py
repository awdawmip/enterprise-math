"""Exact boundary certificates for the two-block first-landing theorem."""
from fractions import Fraction
from math import prod


def rising(value, count):
    return prod(range(value, value + count))


def ratio_without_center(c, v):
    return Fraction(
        448 * (v + 1) * (4 * v + 5) * rising(v + 5, 15),
        15 * (v + 4) * rising(c + 6, 15),
    )


def verify(c=2501):
    rho_next = Fraction(4 * c + 5, c + 5)
    improved = set()
    original = set()
    samples = {}
    for v in range(c - 1, 1, -1):
        ratio = ratio_without_center(c, v)
        exact_test = ratio * (1 - rho_next)
        if rho_next < Fraction(4, 5) and exact_test < 1:
            improved.add(v)
        if rho_next < 1 and ratio < 1:
            original.add(v)
        if v in (1149, 1150):
            samples[v] = (rho_next, ratio, exact_test)
        rho_next *= Fraction(4 * v + 5, 4 * (v + 5))
    if c == 2501:
        assert original == set(range(2, 1132))
        assert improved == set(range(2, 1150))
        lower = samples[1149]
        upper = samples[1150]
        assert Fraction(9935, 10000) < lower[-1] < Fraction(9936, 10000)
        assert Fraction(10064, 10000) < upper[-1] < Fraction(10065, 10000)
    return max(original), max(improved)


if __name__ == "__main__":
    for stock in (2249, 2500, 2501, 3000, 10000):
        print(stock, *verify(stock))
