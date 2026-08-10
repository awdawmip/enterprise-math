from fractions import Fraction

from enterprise_math.abc_local_observable_jet import (
    forward_difference,
    local_future_jet_profile,
    stage112_arithmetic_cancellation_fixture,
)


def test_forward_differences_detect_quadratic_cancellation() -> None:
    polynomial = (Fraction(0), Fraction(-1), Fraction(1))  # r(r-1)
    assert forward_difference(polynomial, 0, 0) == 0
    assert forward_difference(polynomial, 0, 1) == 0
    assert forward_difference(polynomial, 0, 2) == 2


def test_realized_order_depends_on_crossed_candidate_count() -> None:
    polynomial = (Fraction(0), Fraction(-1), Fraction(1))
    one = local_future_jet_profile(polynomial, 0, 1)
    two = local_future_jet_profile(polynomial, 0, 2)
    assert one.realized_action_order == 0
    assert two.realized_action_order == 3
    assert two.degree_geometry_cap == 3


def test_base_rank_changes_realized_order() -> None:
    polynomial = (Fraction(0), Fraction(-1), Fraction(1))
    profile = local_future_jet_profile(polynomial, 1, 1)
    assert profile.forward_differences == (Fraction(0), Fraction(2))
    assert profile.realized_action_order == 2


def test_degree_geometry_cap_limits_local_order() -> None:
    cubic = (Fraction(1), Fraction(2), Fraction(-1), Fraction(3))
    profile = local_future_jet_profile(cubic, 0, 1)
    assert profile.degree_geometry_cap == 2
    assert profile.realized_action_order <= 2


def test_exact_arithmetic_fixture_switches_from_zero_to_cubic_order() -> None:
    data = stage112_arithmetic_cancellation_fixture()
    assert len(data["one_candidate"]) == 1
    assert len(data["two_candidates"]) == 2
    assert data["one_profile"].realized_action_order == 0
    assert data["two_profile"].realized_action_order == 3
