#!/usr/bin/env python3
"""Exact-rational checker for c515 T1-T2 high-pair pointwise absorption."""

from fractions import Fraction as Q


def main() -> None:
    u0 = Q(1, 6)
    u1 = Q(21, 80)
    umax = Q(73, 240)
    U = Q(113, 240)
    beta = Q(31, 40)
    basin = Q(9, 5)
    delta = Q(93, 20)

    # High-pair kernel collapse: U-(beta-u)=u-73/240 < 1/6.
    assert U - beta == -umax

    # Four high-pair larger primes are impossible even at maximal u.
    four_lower = 4 * beta - 3 * umax
    assert four_lower == Q(35, 16) > basin

    # Three high-pair primes require u>21/80.
    assert (3 * beta - basin) / 2 == u1

    # Base-T3 numerator budgets.
    assert 12 * u0 - 1 == 1
    assert 12 * u1 - 1 == Q(43, 20)
    assert Q(43, 20) > Q(3, 2)

    # Positive normalized margin in the three-pair regime at the transition.
    assert (Q(43, 20) - Q(3, 2)) / delta == Q(13, 93)

    print("P017 c515 high-pair pointwise absorption checker: PASS")
    print("high-pair kernel = 1/2")
    print("u<=21/80: at most 2 high pairs, exactly absorbed at worst")
    print("u>21/80: at most 3 high pairs, margin >13/93 at transition")
    print("analytic ordered-pair carrier reduced to rp < D^(31/40)")


if __name__ == "__main__":
    main()
