"""Exact Mobius inversion of the centered carry geometry lift.

This companion stays inside the T0_BRC count-centered carry research surface.
It records an exact algebraic inverse relation; it is not an operator-norm or RH
estimate.
"""
from __future__ import annotations

from .brc_count_centered_carry import (
    GammaAffine,
    _require_positive_int,
    centered_geometry_ratio,
    mobius,
)


def root_centered_carry_ratio(numerator: int, denominator: int = 1) -> GammaAffine:
    """Exact formal root wavelet kappa_gamma(x)=c_1(x)-gamma_c for x>=1."""
    numerator = _require_positive_int("numerator", numerator)
    denominator = _require_positive_int("denominator", denominator)
    if numerator < denominator:
        raise ValueError("root centered carry inversion is declared for x>=1")
    root_carry = (2 * numerator) // denominator - 2 * (numerator // denominator)
    if root_carry not in (0, 1):
        raise AssertionError("root doubling carry must be Boolean")
    return GammaAffine(root_carry, -1)


def mobius_inverted_geometry_ratio(numerator: int, denominator: int = 1) -> GammaAffine:
    """Return sum_{a<=x} mu(a) K_gamma(x/a) and verify root recovery.

    For ``x=numerator/denominator >= 1`` the exact identity is

        sum_{a<=x} mu(a) K_gamma(x/a) = c_1(x)-gamma_c.

    The Mobius layer is therefore the exact inverse of the all-divisor geometry
    lifting on this signal.  This does not estimate the remaining Lambda-weighted
    observer and does not imply an RH bound.
    """
    numerator = _require_positive_int("numerator", numerator)
    denominator = _require_positive_int("denominator", denominator)
    if numerator < denominator:
        raise ValueError("Mobius geometry inversion is declared for x>=1")
    population = numerator // denominator
    total = GammaAffine()
    for a in range(1, population + 1):
        mu = mobius(a)
        if mu:
            total = total + centered_geometry_ratio(numerator, denominator * a).scale(mu)
    expected = root_centered_carry_ratio(numerator, denominator)
    if total != expected:
        raise AssertionError("Mobius inversion of centered geometry failed")
    return total
