"""Exact second moment and variance of Barlow orientation-type repair.

For one labelled signed prefix, orientation repair equals the number of visits
to zero before the next microscopic step, i.e. the number of departures from
the coordinate-wall stabilizer.  At horizon N these visits occur at even times
2j with ``0<=j<=floor((N-1)/2)``.

The one-sided local-time second moment collapses exactly because the normalized
central-binomial return probabilities convolve to one:

    sum_{i=0}^s p_i p_(s-i) = 1,
    p_j=C(2j,j)/4^j.

This gives a closed rational variance without floating arithmetic.
"""

from __future__ import annotations

from math import comb, gcd

Rational = tuple[int, int]


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _reduce(numerator: int, denominator: int) -> Rational:
    if denominator <= 0:
        raise ValueError("denominator must be positive")
    divisor = gcd(abs(numerator), denominator)
    return numerator // divisor, denominator // divisor


def one_sided_orientation_mean(length: int) -> Rational:
    """Exact mean A_N of one-sided orientation repair."""
    _require_natural("length", length)
    if length == 0:
        return 0, 1
    m = (length - 1) // 2
    return _reduce((2 * m + 1) * comb(2 * m, m), 4**m)


def one_sided_orientation_second_moment(length: int) -> Rational:
    """Exact second moment ``2(m+1)-A_N``.

    Let ``L=sum_{j=0}^m I_j`` with ``I_j`` the event that the signed walk is
    at zero at time ``2j``.  For ``i<j``, the Markov property gives

        P(I_i I_j)=p_i p_(j-i).

    Therefore

        E[L^2]=sum_i p_i + 2 sum_{i<j} p_i p_(j-i).

    Writing ``A_k=sum_{r=0}^k p_r`` and summing by the total index uses
    ``(sum p_j z^j)^2=(1-z)^(-1)``, hence every convolution coefficient is 1
    and the triangular sum is ``m+1``.  The result is ``2(m+1)-A_m``.
    """
    _require_natural("length", length)
    if length == 0:
        return 0, 1
    m = (length - 1) // 2
    mean_num, mean_den = one_sided_orientation_mean(length)
    return _reduce(2 * (m + 1) * mean_den - mean_num, mean_den)


def one_sided_orientation_variance(length: int) -> Rational:
    """Exact variance ``2(m+1)-A_N-A_N^2``."""
    mean_num, mean_den = one_sided_orientation_mean(length)
    second_num, second_den = one_sided_orientation_second_moment(length)
    numerator = second_num * mean_den * mean_den - (
        mean_num * mean_num * second_den
    )
    denominator = second_den * mean_den * mean_den
    return _reduce(numerator, denominator)


def two_sided_orientation_mean(length: int) -> Rational:
    """Two labelled sides are independent, so the mean doubles."""
    mean_num, mean_den = one_sided_orientation_mean(length)
    return _reduce(2 * mean_num, mean_den)


def two_sided_orientation_variance(length: int) -> Rational:
    """Two labelled sides are independent, so the variance doubles."""
    var_num, var_den = one_sided_orientation_variance(length)
    return _reduce(2 * var_num, var_den)


def return_probability_convolution_identity(index: int) -> Rational:
    """Exact check of ``sum_i p_i p_(n-i)=1`` with a common denominator."""
    _require_natural("index", index)
    denominator = 4**index
    numerator = sum(
        comb(2 * i, i)
        * comb(2 * (index - i), index - i)
        for i in range(index + 1)
    )
    return _reduce(numerator, denominator)


def leading_two_sided_variance_constant_descriptor() -> tuple[int, int]:
    """Descriptor for ``2*(1-2/pi)``; analytic comparison only.

    The exact finite variance remains rational.  The tuple records coefficients
    `(2,4)` in ``2 - 4/pi``.
    """
    return 2, 4
