from itertools import product
from math import gcd

from enterprise_math.p022_barlow_repair_covariance import (
    finite_covariance_sign_changes,
    microscopic_joint_raw_moments,
    microscopic_repair_covariance,
    microscopic_total_repair_variance,
)
from enterprise_math.p022_barlow_two_sided_repair import (
    diagonal_split_count,
    total_zero_departure_events,
    unordered_absolute_pair_history,
)


def _words(length: int):
    return tuple(tuple(word) for word in product((-1, 1), repeat=length))


def _reduce(numerator: int, denominator: int):
    g = gcd(abs(numerator), denominator)
    return numerator // g, denominator // g


def _direct_raw_moments(length: int):
    domain = 4**length
    sum_e = sum_b = sum_e2 = sum_b2 = sum_eb = 0
    words = _words(length)
    for left in words:
        for right in words:
            history = unordered_absolute_pair_history(left, right)
            orientation = total_zero_departure_events(history)
            split = diagonal_split_count(history)
            sum_e += orientation
            sum_b += split
            sum_e2 += orientation * orientation
            sum_b2 += split * split
            sum_eb += orientation * split
    return domain, sum_e, sum_b, sum_e2, sum_b2, sum_eb


def test_bivariate_euler_moments_match_direct_microscopic_enumeration() -> None:
    for length in range(0, 7):
        assert microscopic_joint_raw_moments(length) == _direct_raw_moments(length)


def test_covariance_and_total_variance_match_direct_moments() -> None:
    for length in range(0, 7):
        domain, sum_e, sum_b, sum_e2, sum_b2, sum_eb = _direct_raw_moments(length)
        expected_covariance = _reduce(
            sum_eb * domain - sum_e * sum_b,
            domain * domain,
        )
        sum_r = sum_e + sum_b
        sum_r2 = sum_e2 + 2 * sum_eb + sum_b2
        expected_variance = _reduce(
            sum_r2 * domain - sum_r * sum_r,
            domain * domain,
        )
        assert microscopic_repair_covariance(length) == expected_covariance
        assert microscopic_total_repair_variance(length) == expected_variance


def test_finite_covariance_is_not_sign_definite() -> None:
    assert microscopic_repair_covariance(3) == (-1, 8)
    assert microscopic_repair_covariance(10) == (18609, 4194304)
    assert microscopic_repair_covariance(11) == (-144321, 33554432)
    assert microscopic_repair_covariance(12) == (5712175, 67108864)


def test_sign_change_audit_preserves_small_horizon_oscillation() -> None:
    changes = finite_covariance_sign_changes(12)
    assert (2, 0, -1) in changes
    assert (9, -1, 1) in changes
    assert (10, 1, -1) in changes
    assert (11, -1, 1) in changes


def test_total_repair_variance_is_nonnegative() -> None:
    for length in range(0, 25):
        numerator, denominator = microscopic_total_repair_variance(length)
        assert denominator > 0
        assert numerator >= 0
