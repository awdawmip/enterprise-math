from fractions import Fraction

import pytest

from enterprise_math.p022_barlow_franel_boundary_dual_hasse_jet import (
    boundary_kernel_from_conjugate_hasse_jet,
    boundary_to_conjugate_term_ratio,
    boundary_zero_avoids_conjugate_scalar_hasse,
    boundary_zero_is_conjugate_fixed_log_derivative,
    conjugate_contiguous_gosper_reduction,
    conjugate_hasse_zero_is_simple,
    conjugate_period_jets_residue,
    conjugate_period_term_ratio,
    dual_hasse_lagrange_relation_at_one,
    dual_hasse_log_derivative_sum,
    franel_zero_dual_hasse_first_jet_pair,
    original_and_conjugate_operators_are_formal_adjoints,
)


def test_exact_conjugate_contiguous_reduction() -> None:
    assert boundary_to_conjugate_term_ratio(0) == 1
    assert conjugate_period_term_ratio(0) == Fraction(2, 27)
    for index in range(15):
        left, right = conjugate_contiguous_gosper_reduction(index)
        assert left == right


def test_formal_adjoint_and_lagrange_relation() -> None:
    assert original_and_conjugate_operators_are_formal_adjoints()
    for prime in (5, 11, 17, 23, 29, 41, 53, 71, 89, 107, 149):
        assert dual_hasse_lagrange_relation_at_one(prime)


def test_conjugate_picard_fuchs_scalar_zero_is_simple() -> None:
    # p=107 is the smallest known scalar-Hasse zero in this period-two pair.
    _, period, theta_period, _ = conjugate_period_jets_residue(107)
    assert period == 0
    assert theta_period != 0
    assert conjugate_hasse_zero_is_simple(107)


def test_boundary_kernel_is_conjugate_first_jet() -> None:
    for prime in (5, 11, 17, 23, 29, 41, 53, 71, 89, 107, 149):
        _, actual, _, _ = boundary_kernel_from_conjugate_hasse_jet(prime)
        assert isinstance(actual, int)
        assert boundary_zero_avoids_conjugate_scalar_hasse(prime)


def test_dual_log_derivative_sum_on_ordinary_samples() -> None:
    for prime in (11, 17, 23, 29, 41, 53, 71, 89, 149):
        left, right, target = dual_hasse_log_derivative_sum(prime)
        assert (left + right) % prime == target


def test_control_franel_zero_hits_both_first_jet_targets() -> None:
    # 149 | F_50 is the frozen non-target control showing that one-third
    # Franel zeros exist outside the admissible P022 n=0 mod 3 boundary.
    assert boundary_zero_is_conjugate_fixed_log_derivative(149)
    assert franel_zero_dual_hasse_first_jet_pair(149)


def test_nonzero_boundary_sample_does_not_claim_log_derivative_target() -> None:
    assert not boundary_zero_is_conjugate_fixed_log_derivative(17)
    assert not franel_zero_dual_hasse_first_jet_pair(17)


def test_invalid_prime_rejected() -> None:
    with pytest.raises(ValueError):
        boundary_kernel_from_conjugate_hasse_jet(13)
