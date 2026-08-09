"""Linear second-moment bound for total Barlow event repair.

After rotating two signed drifts into the cardinal Z^2 walk, each coordinate is
a lazy one-dimensional walk with increments -1,0,+1 of probabilities 1/4,1/2,1/4.
Its zero-return probability is p_t=C(2t,t)/4^t. The generating function
P(z)=(1-z)^(-1/2) gives the exact convolution sum p*p=1 and hence an exact
second moment for coordinate-axis local time.
"""

from __future__ import annotations

from math import comb, gcd

from .p022_barlow_orientation_variance import (
    one_sided_orientation_mean,
    one_sided_orientation_second_moment,
)

Rational = tuple[int, int]


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _reduce(numerator: int, denominator: int) -> Rational:
    divisor = gcd(abs(numerator), denominator)
    return numerator // divisor, denominator // divisor


def lazy_zero_probability_fraction(time: int) -> Rational:
    _require_natural("time", time)
    return comb(2 * time, time), 4**time


def lazy_axis_local_time_mean_fraction(length: int) -> Rational:
    """Exact E[L_N] for visits at times 0,...,N-1."""
    _require_natural("length", length)
    if length == 0:
        return 0, 1
    n = length - 1
    return _reduce((2 * n + 1) * comb(2 * n, n), 4**n)


def lazy_axis_local_time_second_moment_fraction(length: int) -> Rational:
    """Exact E[L_N^2] = 2N-E[L_N]."""
    _require_natural("length", length)
    mean_num, mean_den = lazy_axis_local_time_mean_fraction(length)
    return _reduce(2 * length * mean_den - mean_num, mean_den)


def two_sided_orientation_second_moment_fraction(length: int) -> Rational:
    """Exact E[(E_1+E_2)^2] from independence of the two signed walks."""
    _require_natural("length", length)
    mean_num, mean_den = one_sided_orientation_mean(length)
    second_num, second_den = one_sided_orientation_second_moment(length)
    numerator = (
        2 * second_num * mean_den * mean_den
        + 2 * mean_num * mean_num * second_den
    )
    denominator = second_den * mean_den * mean_den
    return _reduce(numerator, denominator)


def split_second_moment_linear_bound(length: int) -> int:
    """Integer upper bound E[B^2] < 8N (and 0 when N=0).

    B is at most L_U+L_V, the total visits to the two coordinate axes before
    the next step. By (a+b)^2<=2a^2+2b^2 and symmetry,

        E[B^2] <= 4 E[L_U^2] < 8N.
    """
    _require_natural("length", length)
    return 8 * length


def total_repair_second_moment_linear_bound(length: int) -> int:
    """Certified O(N) bound for E[(E+B)^2].

    Uses (E+B)^2<=2E^2+2B^2, exact orientation E^2, and B^2<8N.
    The returned integer is deliberately simple rather than sharp.
    """
    _require_natural("length", length)
    if length == 0:
        return 0
    e2_num, e2_den = two_sided_orientation_second_moment_fraction(length)
    twice_e2_ceiling = (2 * e2_num + e2_den - 1) // e2_den
    return twice_e2_ceiling + 16 * length


def total_repair_variance_linear_bound(length: int) -> int:
    """Variance is at most the raw second moment."""
    return total_repair_second_moment_linear_bound(length)
