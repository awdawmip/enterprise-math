#!/usr/bin/env python3
"""Exact enumeration regression for the closed-form X6 N-BRC endpoint kernel."""
from collections import Counter
from fractions import Fraction

from brc_kernel import (
    c2_weight_channels,
    equal_axis_endpoint_multiplicity,
    origin_companion_return_multiplicity,
)

AXES = (
    (1, 0, 0),
    (0, 1, 0),
    (-1, -1, 0),
    (-1, -1, 1),
    (0, 1, 1),
    (1, 0, 1),
)


def add(x, y):
    return (x[0] + y[0], x[1] + y[1], (x[2] + y[2]) & 1)


def main():
    dist = Counter({(0, 0, 0): 1})
    checks = 0
    for length in range(0, 8):
        if length > 0:
            nxt = Counter()
            for state, count in dist.items():
                for axis in AXES:
                    nxt[add(state, axis)] += count
            dist = nxt
        assert sum(dist.values()) == 6 ** length
        checks += 1
        for p in range(-length, length + 1):
            for q in range(-length, length + 1):
                for sheet in (0, 1):
                    assert dist.get((p, q, sheet), 0) == equal_axis_endpoint_multiplicity(length, p, q, sheet)
                    checks += 1

    assert origin_companion_return_multiplicity(3) == (24, 24)
    assert origin_companion_return_multiplicity(6) == (2880, 2880)
    checks += 2

    plus, minus = c2_weight_channels(((1, 1), (2, 2), (3, 3)))
    assert plus == (Fraction(2), Fraction(4), Fraction(6))
    assert minus == (Fraction(0), Fraction(0), Fraction(0))
    checks += 2

    plus, minus = c2_weight_channels(((1, 2), (3, 5), (7, 11)))
    assert plus == (Fraction(3), Fraction(8), Fraction(18))
    assert minus == (Fraction(-1), Fraction(-2), Fraction(-4))
    checks += 2

    print("PASS_X6_BRC_KERNEL")
    print("enumeration_lengths=0..7")
    print("checks=", checks)
    print("return_m3=(24,24)")
    print("return_m6=(2880,2880)")
    print("pair_symmetric_weights=>minus_character_channel_zero")


if __name__ == "__main__":
    main()
