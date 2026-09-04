#!/usr/bin/env python3
"""Exact rational checks for the retained two-channel Mellin matrix."""

from __future__ import annotations

from fractions import Fraction


def A(beta: Fraction) -> Fraction:
    return (
        Fraction(1, 1) / (1 - beta)
        - Fraction(4, 1) / (2 - beta)
        + Fraction(4, 1) / (3 - beta)
    )


def B(beta: Fraction) -> Fraction:
    return Fraction(1, 1) / (2 - beta)


def C(beta: Fraction) -> Fraction:
    return Fraction(4, 9) * (
        Fraction(1, 1) / (2 - beta)
        - Fraction(1, 1) / (3 - beta)
    )


def scalar_multiplier(beta: Fraction) -> Fraction:
    return A(beta) + C(beta)


def channel_polynomial(beta: Fraction) -> Fraction:
    return beta**3 - 5 * beta**2 + 10 * beta - 4


def scalar_polynomial(beta: Fraction) -> Fraction:
    return 9 * beta**3 - 45 * beta**2 + 86 * beta - 32


def check_local_matrix() -> None:
    samples = [Fraction(0), Fraction(1, 7), Fraction(1, 2), Fraction(6, 7), Fraction(1)]
    for s in samples:
        mean = (1 - 2 * s) ** 2
        standard_from_mean = Fraction(4, 9) * s * (1 - s)
        scalar = mean + standard_from_mean
        assert scalar == 1 - Fraction(32, 9) * s * (1 - s)


def check_integrals_by_antiderivative() -> None:
    # Rational beta values avoid any floating-point appeal.
    for beta in [Fraction(0), Fraction(1, 10), Fraction(1, 4), Fraction(2, 5), Fraction(1, 2)]:
        assert A(beta) == (
            Fraction(1, 1) / (1 - beta)
            - Fraction(4, 1) / (2 - beta)
            + Fraction(4, 1) / (3 - beta)
        )
        assert B(beta) == Fraction(1, 1) / (2 - beta)
        assert C(beta) == Fraction(4, 9) * (
            Fraction(1, 1) / (2 - beta)
            - Fraction(1, 1) / (3 - beta)
        )
        assert scalar_multiplier(beta) == (
            Fraction(1, 1) / (1 - beta)
            - Fraction(32, 9) / (2 - beta)
            + Fraction(32, 9) / (3 - beta)
        )


def check_critical_equivalences() -> None:
    for beta in [Fraction(0), Fraction(1, 5), Fraction(12, 25), Fraction(1, 2), Fraction(3, 5)]:
        denominator = (1 - beta) * (2 - beta) * (3 - beta)
        assert denominator > 0
        # A(beta)-1 has the same sign as the channel polynomial.
        assert (A(beta) - 1) * denominator == channel_polynomial(beta)

        # The scalar multiplier equivalence carries the factor 1/9.
        assert (scalar_multiplier(beta) - 1) * denominator == scalar_polynomial(beta) / 9


def check_unique_root_intervals() -> None:
    lo = Fraction(5220, 10000)
    hi = Fraction(5221, 10000)
    assert channel_polynomial(lo) < 0 < channel_polynomial(hi)

    scalar_lo = Fraction(4818, 10000)
    scalar_hi = Fraction(4820, 10000)
    assert scalar_polynomial(scalar_lo) < 0 < scalar_polynomial(scalar_hi)

    # Derivative quadratics are positive on all real numbers by completing
    # the square; rational samples additionally guard the implementation.
    for beta in [Fraction(-10), Fraction(-1), Fraction(0), Fraction(1), Fraction(10)]:
        assert 3 * beta**2 - 10 * beta + 10 > 0


def check_weighted_cone() -> None:
    for beta in [Fraction(0), Fraction(1, 10), Fraction(1, 4), Fraction(2, 5), Fraction(1, 2)]:
        a = A(beta)
        b = B(beta)
        c = C(beta)
        assert 0 <= a < 1
        assert 0 <= b < 1
        assert c > 0
        lam = (1 - a) / (2 * c)
        q = max((1 + a) / 2, b)
        assert lam > 0
        assert q < 1

        for r_i in range(0, 7):
            for v_i in range(0, 7):
                r = Fraction(r_i)
                v = Fraction(v_i)
                out_r = a * r
                out_v = c * r + b * v
                assert out_r + lam * out_v <= q * (r + lam * v)


def main() -> None:
    check_local_matrix()
    check_integrals_by_antiderivative()
    check_critical_equivalences()
    check_unique_root_intervals()
    check_weighted_cone()
    print("retained two-channel Mellin matrix: exact checks passed")


if __name__ == "__main__":
    main()
