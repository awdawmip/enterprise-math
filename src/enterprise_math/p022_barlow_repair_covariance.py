"""Exact microscopic mixed moments for two-sided Barlow event repair.

The bivariate quotient-state mechanism polynomial is

    M_N(x,y) = sum_h a_h x^E(h) y^B(h),

where E counts orientation/zero-wall repair and B counts side-label/split-wall
repair.  Microscopic weighting evaluates at (x,y)=(2,2), because history h has
exact microscopic fiber size 2^(E+B).

Euler operators x*d/dx and y*d/dy therefore recover ordinary raw moments of
E and B under the uniform microscopic measure without enumerating 4^N word
pairs.
"""

from __future__ import annotations

from math import gcd

from .p022_barlow_repair_mechanism import mechanism_polynomial_terms

Rational = tuple[int, int]
RawMoments = tuple[int, int, int, int, int, int]
# (domain, sum_E, sum_B, sum_E2, sum_B2, sum_EB)


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _reduce(numerator: int, denominator: int) -> Rational:
    if denominator <= 0:
        raise ValueError("denominator must be positive")
    divisor = gcd(abs(numerator), denominator)
    return numerator // divisor, denominator // divisor


def microscopic_joint_raw_moments(length: int) -> RawMoments:
    """Return exact unnormalized microscopic moments of (E,B).

    Every quotient history of mechanism type (E,B) and quotient multiplicity a
    represents exactly a*2^(E+B) microscopic word pairs.
    """
    _require_natural("length", length)
    domain = 4**length
    sum_e = 0
    sum_b = 0
    sum_e2 = 0
    sum_b2 = 0
    sum_eb = 0
    mass = 0
    for orientation, split, history_count in mechanism_polynomial_terms(length):
        microscopic_count = history_count * (2 ** (orientation + split))
        mass += microscopic_count
        sum_e += orientation * microscopic_count
        sum_b += split * microscopic_count
        sum_e2 += orientation * orientation * microscopic_count
        sum_b2 += split * split * microscopic_count
        sum_eb += orientation * split * microscopic_count
    if mass != domain:
        raise AssertionError("mechanism polynomial must reconstruct the microscopic domain")
    return domain, sum_e, sum_b, sum_e2, sum_b2, sum_eb


def microscopic_orientation_mean(length: int) -> Rational:
    domain, sum_e, *_ = microscopic_joint_raw_moments(length)
    return _reduce(sum_e, domain)


def microscopic_split_mean(length: int) -> Rational:
    domain, _, sum_b, *_ = microscopic_joint_raw_moments(length)
    return _reduce(sum_b, domain)


def microscopic_orientation_variance(length: int) -> Rational:
    domain, sum_e, _, sum_e2, _, _ = microscopic_joint_raw_moments(length)
    return _reduce(sum_e2 * domain - sum_e * sum_e, domain * domain)


def microscopic_split_variance(length: int) -> Rational:
    domain, _, sum_b, _, sum_b2, _ = microscopic_joint_raw_moments(length)
    return _reduce(sum_b2 * domain - sum_b * sum_b, domain * domain)


def microscopic_repair_covariance(length: int) -> Rational:
    """Exact Cov(E,B) under uniform microscopic weighting."""
    domain, sum_e, sum_b, _, _, sum_eb = microscopic_joint_raw_moments(length)
    return _reduce(sum_eb * domain - sum_e * sum_b, domain * domain)


def microscopic_total_repair_variance(length: int) -> Rational:
    """Exact Var(E+B) under uniform microscopic weighting."""
    domain, sum_e, sum_b, sum_e2, sum_b2, sum_eb = microscopic_joint_raw_moments(length)
    sum_r = sum_e + sum_b
    sum_r2 = sum_e2 + 2 * sum_eb + sum_b2
    return _reduce(sum_r2 * domain - sum_r * sum_r, domain * domain)


def covariance_numerator(length: int) -> int:
    """Signed numerator of the reduced microscopic covariance."""
    return microscopic_repair_covariance(length)[0]


def covariance_sign(length: int) -> int:
    numerator = covariance_numerator(length)
    return (numerator > 0) - (numerator < 0)


def finite_covariance_sign_changes(limit: int) -> tuple[tuple[int, int, int], ...]:
    """Return adjacent horizons where the exact covariance sign changes.

    Each entry is (N, sign_at_N, sign_at_N_plus_1). Zeros are retained as a
    boundary rather than silently skipped.
    """
    _require_natural("limit", limit)
    if limit < 1:
        return ()
    output: list[tuple[int, int, int]] = []
    previous = covariance_sign(1)
    for length in range(2, limit + 1):
        current = covariance_sign(length)
        if current != previous:
            output.append((length - 1, previous, current))
        previous = current
    return tuple(output)
