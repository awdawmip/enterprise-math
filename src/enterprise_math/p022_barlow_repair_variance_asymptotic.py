"""Exact finite support identities for the Barlow repair variance asymptotic.

The theorem note ``P022_BARLOW_REPAIR_VARIANCE_ASYMPTOTIC`` proves that the
exact repair variable R_N differs in L2-o(sqrt(N)) from the four-wall surrogate

    W_N = A_S + A_T + (A_U + A_V)/2.

This module keeps the finite pieces of that comparison integer/rational:

- exact cardinal-walk origin return probabilities and origin local-time second
  moments;
- exact second moment of the Bernoulli-thinning martingale correction;
- an exact finite L2 upper bound for R_N-W_N;
- a symbolic descriptor of the analytic variance constant
  7-(6+8*sqrt(2))/pi.

The Brownian/local-time invariance step itself is analytic prior art and is not
encoded as a floating numerical primitive here.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb

from .p022_barlow_repair_covariance import microscopic_total_repair_variance

Rational = tuple[int, int]


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _as_tuple(value: Fraction) -> Rational:
    return value.numerator, value.denominator


def cardinal_origin_return_probability_fraction(time: int) -> Rational:
    """Exact probability that the rotated cardinal walk is at the origin.

    The origin condition is equivalent to both original simple walks being at
    zero.  Odd times are impossible.  At time ``2j`` the probability is

        C(2j,j)^2 / 16^j.
    """
    _require_natural("time", time)
    if time % 2:
        return 0, 1
    half = time // 2
    return _as_tuple(Fraction(comb(2 * half, half) ** 2, 16**half))


def cardinal_origin_local_time_mean_fraction(length: int) -> Rational:
    """Exact mean number of origin visits at pre-step times ``0,...,N-1``."""
    _require_natural("length", length)
    total = Fraction(0, 1)
    for time in range(length):
        numerator, denominator = cardinal_origin_return_probability_fraction(time)
        total += Fraction(numerator, denominator)
    return _as_tuple(total)


def cardinal_origin_local_time_second_moment_fraction(length: int) -> Rational:
    """Exact second moment of cardinal-walk origin local time.

    If q_t=P(X_t=0), the Markov property gives

        E[C_N^2] = sum_t q_t + 2 sum_(s<t) q_s q_(t-s).
    """
    _require_natural("length", length)
    probabilities = [
        Fraction(*cardinal_origin_return_probability_fraction(time))
        for time in range(length)
    ]
    second = sum(probabilities, Fraction(0, 1))
    for left in range(length):
        for right in range(left + 1, length):
            second += 2 * probabilities[left] * probabilities[right - left]
    return _as_tuple(second)


def lazy_axis_zero_probability_fraction(time: int) -> Rational:
    """Exact return probability for one rotated lazy coordinate."""
    _require_natural("time", time)
    return _as_tuple(Fraction(comb(2 * time, time), 4**time))


def thinning_martingale_second_moment_fraction(length: int) -> Rational:
    """Exact E[M_N^2] for the split-departure thinning martingale.

    The one-step martingale increment is zero off both axes and at the origin,
    and is +/-1/2 on exactly one coordinate axis.  Hence

        E[M_N^2]
          = 1/4 sum_t P(exactly one axis)
          = 1/2 sum_t (P(U_t=0)-P(U_t=V_t=0)).
    """
    _require_natural("length", length)
    total = Fraction(0, 1)
    for time in range(length):
        axis = Fraction(*lazy_axis_zero_probability_fraction(time))
        origin = Fraction(*cardinal_origin_return_probability_fraction(time))
        total += Fraction(1, 2) * (axis - origin)
    return _as_tuple(total)


def wall_surrogate_error_l2_bound_fraction(length: int) -> Rational:
    """Exact finite upper bound on E[(R_N-W_N)^2].

    The exact difference is ``M_N-C_N``.  Therefore

        (M-C)^2 <= 2 M^2 + 2 C^2.
    """
    _require_natural("length", length)
    martingale = Fraction(*thinning_martingale_second_moment_fraction(length))
    origin_second = Fraction(*cardinal_origin_local_time_second_moment_fraction(length))
    return _as_tuple(2 * martingale + 2 * origin_second)


def repair_variance_limit_descriptor() -> tuple[int, int, int]:
    """Descriptor of ``7-(6+8*sqrt(2))/pi``.

    Returns ``(7,6,8)`` rather than storing a floating approximation.  The
    theorem note derives this constant from four wall-local-time covariance
    limits.
    """
    return 7, 6, 8


def finite_total_variance_ratio_fraction(length: int) -> Rational:
    """Exact finite ``Var(R_N)/N`` for comparison with the analytic limit."""
    _require_natural("length", length)
    if length == 0:
        return 0, 1
    numerator, denominator = microscopic_total_repair_variance(length)
    return _as_tuple(Fraction(numerator, denominator * length))
