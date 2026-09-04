#!/usr/bin/env python3
"""Exact checks for the parity-scattering profile spectral exponent.

The theorem-level algebra uses ``Fraction`` only. Decimal output is merely a
readable display of an exactly bracketed algebraic root.
"""

from __future__ import annotations

from fractions import Fraction


def moment(beta: Fraction) -> Fraction:
    """M(beta)=integral_0^1 q(t)t^{-beta} dt in closed rational form."""
    return (
        Fraction(1, 1) / (1 - beta)
        - Fraction(32, 9) / (2 - beta)
        + Fraction(32, 9) / (3 - beta)
    )


def cubic(beta: Fraction) -> Fraction:
    return 9 * beta**3 - 45 * beta**2 + 86 * beta - 32


def bisect_root(
    left: Fraction, right: Fraction, iterations: int = 96
) -> tuple[Fraction, Fraction]:
    assert cubic(left) < 0 < cubic(right)
    for _ in range(iterations):
        middle = (left + right) / 2
        if cubic(middle) < 0:
            left = middle
        else:
            right = middle
    return left, right


def check_moment_formula() -> None:
    # Exact integral of 1 - (32/9)t + (32/9)t^2 against t^{-beta}.
    for beta in (
        Fraction(0),
        Fraction(1, 10),
        Fraction(1, 3),
        Fraction(47, 100),
        Fraction(12, 25),
    ):
        direct = (
            Fraction(1, 1 - beta)
            - Fraction(32, 9) * Fraction(1, 2 - beta)
            + Fraction(32, 9) * Fraction(1, 3 - beta)
        )
        assert moment(beta) == direct
        denominator = 9 * (1 - beta) * (2 - beta) * (3 - beta)
        assert (moment(beta) - 1) * denominator == -cubic(beta)

    assert moment(Fraction(0)) == Fraction(11, 27)


def check_monotonicity_grid() -> None:
    # The analytic derivative is positive term-by-term in the integral form.
    # This exact grid is only an independent arithmetic regression check.
    previous = moment(Fraction(0))
    for numerator in range(1, 100):
        beta = Fraction(numerator, 100)
        current = moment(beta)
        assert current > previous
        previous = current


def check_safe_exponent() -> None:
    beta = Fraction(47, 100)
    value = moment(beta)
    assert value == Fraction(17878100, 18464193)
    assert Fraction(1) - value == Fraction(586093, 18464193)
    assert value < 1
    assert cubic(beta) < 0

    # 0.482 lies above the critical root, giving an exact narrow bracket.
    upper = Fraction(241, 500)
    assert cubic(upper) > 0
    left, right = bisect_root(beta, upper)
    assert right - left < Fraction(1, 10**28)
    assert cubic(left) < 0 < cubic(right)
    print(
        "critical beta bracket:",
        f"[{float(left):.12f}, {float(right):.12f}]",
    )


def check_affine_barrier() -> None:
    # Abstract one-step barrier algebra. If T(W)<=rho W and forcing <=
    # (1-rho)K W, then T(KW)+forcing<=KW.
    rho = moment(Fraction(47, 100))
    K = Fraction(13, 7)
    W = Fraction(17, 19)
    forcing = (1 - rho) * K * W
    assert rho * K * W + forcing == K * W

    # Square-root transfer of the safe energy exponent 47/100.
    assert Fraction(47, 100) / 2 == Fraction(47, 200)


def main() -> None:
    check_moment_formula()
    check_monotonicity_grid()
    check_safe_exponent()
    check_affine_barrier()
    print("parity-profile spectral exponent: exact checks passed")


if __name__ == "__main__":
    main()
