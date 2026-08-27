#!/usr/bin/env python3
"""Supersession checker for the former c515 super-root pair absorption claim."""

from fractions import Fraction as Q


def main() -> None:
    U = Q(113, 240)
    ustar = Q(73, 240)
    u0 = Q(1, 6)

    # Retained local facts: super-root kernel is 1/2 and at most two such pairs.
    t_lower = Q(9, 10) - ustar
    assert t_lower == Q(143, 240) > ustar
    assert U - t_lower < Q(1, 6)
    assert 2 * Q(73, 216) < 1

    # Correct pair budget after least-prime-shell cost at u=1/6.
    base = 12 * u0 - 1
    least = Q(1, 2)
    pair_budget = base - least
    assert pair_budget == Q(1, 2)
    assert pair_budget < 2 * Q(1, 2)

    print("P017 former super-root absorption checker: SUPERSEDED AS EXPECTED")
    print("kernel/count facts PASS; full absorption is not budget-valid")


if __name__ == "__main__":
    main()
