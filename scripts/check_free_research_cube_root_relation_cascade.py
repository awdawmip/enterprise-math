#!/usr/bin/env python3
"""Exact checks for the one-ninth cube-root relation-energy cascade.

The recurrence

    E[k+1] <= E[k]/9 + (C/L)/3**k

has the explicit majorant

    E[0]/9**k + 9*C/(2*L) * (1/3**k - 1/9**k).

All checks use ``Fraction`` only.
"""

from __future__ import annotations

from fractions import Fraction


def forcing(C: Fraction, L: Fraction, k: int) -> Fraction:
    assert L != 0
    return C / L * Fraction(1, 3) ** k


def majorant(E0: Fraction, C: Fraction, L: Fraction, k: int) -> Fraction:
    assert L != 0
    return (
        Fraction(1, 9) ** k * E0
        + Fraction(9, 2) * C / L
        * (Fraction(1, 3) ** k - Fraction(1, 9) ** k)
    )


def check_exact_recurrence(max_k: int = 100) -> None:
    test_data = [
        (Fraction(7, 5), Fraction(11, 13), Fraction(17, 19)),
        (Fraction(-3, 7), Fraction(5, 2), Fraction(23, 29)),
        (Fraction(31, 37), Fraction(0), Fraction(41, 43)),
    ]
    for E0, C, L in test_data:
        assert majorant(E0, C, L, 0) == E0
        for k in range(max_k):
            assert majorant(E0, C, L, k + 1) == (
                Fraction(1, 9) * majorant(E0, C, L, k)
                + forcing(C, L, k)
            )


def check_comparison(max_k: int = 80) -> None:
    E0 = Fraction(13, 17)
    C = Fraction(19, 23)
    L = Fraction(29, 31)
    E = [E0]
    for k in range(max_k):
        # Strictly smaller than the allowed forcing, to test inequality propagation.
        perturbation = forcing(C, L, k) * Fraction(k + 1, k + 2)
        E.append(Fraction(1, 9) * E[-1] + perturbation)
    for k, value in enumerate(E):
        assert value <= majorant(E0, C, L, k)


def check_log_scale_rate(max_k: int = 100) -> None:
    E0 = Fraction(7, 11)
    C = Fraction(13, 17)
    L0 = Fraction(19, 23)
    for k in range(max_k + 1):
        bound = majorant(E0, C, L0, k)
        simple = (
            Fraction(1, 9) ** k * E0
            + Fraction(9, 2) * C / L0 * Fraction(1, 3) ** k
        )
        assert bound <= simple

        # If log N_k = 3^k L0, the forcing contribution is O(1/log N_k).
        log_scale = 3**k * L0
        forcing_rate = Fraction(9, 2) * C / log_scale
        assert simple == Fraction(1, 9) ** k * E0 + forcing_rate


def check_zero_forcing() -> None:
    E0 = Fraction(5, 8)
    for k in range(50):
        assert majorant(E0, Fraction(0), Fraction(3, 7), k) == Fraction(1, 9) ** k * E0


def main() -> None:
    check_exact_recurrence()
    check_comparison()
    check_log_scale_rate()
    check_zero_forcing()
    print("cube-root relation cascade checks: PASS")


if __name__ == "__main__":
    main()
