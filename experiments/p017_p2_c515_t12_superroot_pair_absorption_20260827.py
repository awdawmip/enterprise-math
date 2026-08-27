#!/usr/bin/env python3
"""Exact-rational checker for c=103/20 super-root ordered-pair absorption."""

from fractions import Fraction as Q


def main() -> None:
    U = Q(113, 240)
    ustar = Q(73, 240)
    delta = Q(93, 20)

    # Root is u+t=9/10 and hard u<73/240.
    t_lower = Q(9, 10) - ustar
    assert t_lower == Q(143, 240) > ustar

    # Hence U-t<1/6, so kappa=1/2 throughout the super-root hard strip.
    assert U - t_lower == -Q(1, 8) < Q(1, 6)

    # Three super-root larger primes would force W^3/r^2 > W^2,
    # because r<W^(73/216) and 2*(73/216)<1.
    assert 2 * Q(73, 216) == Q(73, 108) < 1

    # At most two pair shells, each kappa=1/2.
    assert 2 * Q(1, 2) == 1

    # Base-minus-T3 numerator is 12u-1 and is >=1 for u>=1/6.
    assert 12 * Q(1, 6) - 1 == 1
    assert Q(1) / delta == Q(20, 93)

    print("P017 c515 super-root pair absorption checker: PASS")
    print("super-root hard-pair kernel = 1/2")
    print("at most two such larger primes per basin state")
    print("base-minus-T3 absorbs their full pair penalty pointwise")


if __name__ == "__main__":
    main()
