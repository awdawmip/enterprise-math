#!/usr/bin/env python3
"""Supersession checker for the former c515 high-pair absorption claim.

Retains the local kernel/count facts and explicitly verifies the least-shell
budget obstruction.  The full high-pair absorption conclusion is withdrawn;
see p017_p2_c515_t12_least_shell_budget_correction_20260827.py.
"""

from fractions import Fraction as Q


def main() -> None:
    u0 = Q(1, 6)
    umax = Q(73, 240)
    U = Q(113, 240)
    beta = Q(31, 40)
    basin = Q(9, 5)

    # Retained local facts.
    assert U - beta == -umax
    assert 4 * beta - 3 * umax == Q(35, 16) > basin
    assert (3 * beta - basin) / 2 == Q(21, 80)

    # Correct budget includes the least-prime shell.
    base = 12 * u0 - 1
    least = Q(1, 2)
    pair_budget = base - least
    assert base == 1
    assert pair_budget == Q(1, 2)

    # Two high-pair penalties can total one, so the old uniform absorption
    # does not follow at the lower endpoint.
    assert pair_budget < 2 * Q(1, 2)

    print("P017 former high-pair absorption checker: SUPERSEDED AS EXPECTED")
    print("local kernel/count facts PASS; least-shell budget blocks old conclusion")


if __name__ == "__main__":
    main()
