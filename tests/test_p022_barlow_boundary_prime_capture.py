import pytest

from enterprise_math.p022_barlow_boundary_prime_capture import (
    boundary_escape_zero_support_from_kernel,
    boundary_prime,
    boundary_q_relation_high_support,
    boundary_reflected_interior_pair_cannot_both_be_twin,
)


def test_boundary_q_relation_has_exact_four_term_high_support() -> None:
    assert boundary_prime(6) == 17
    assert boundary_q_relation_high_support(6) == (
        (6, 1),
        (8, 1),
        (9, -1),
        (16, 1),
    )
    assert boundary_prime(36) == 107
    assert boundary_q_relation_high_support(36) == (
        (36, 1),
        (53, 1),
        (54, -1),
        (106, 1),
    )
    assert boundary_q_relation_high_support(156) == (
        (156, 1),
        (233, 1),
        (234, -1),
        (466, 1),
    )


def test_complete_boundary_kernel_has_only_the_reflected_endpoint_pair() -> None:
    assert boundary_escape_zero_support_from_kernel(6, (6, 10)) == (6, 10)
    assert boundary_escape_zero_support_from_kernel(36, (36, 70)) == (36, 70)
    assert boundary_escape_zero_support_from_kernel(156, (156, 310)) == (156, 310)


def test_reflected_strict_interior_cannot_be_a_twin_pair() -> None:
    # q=107, q-1=106.  Every strict interior index is paired to 106-d.
    # The mod-3 theorem forbids both members from being twin centers.
    for digit in range(38, 69):
        assert boundary_reflected_interior_pair_cannot_both_be_twin(36, digit)


def test_synthetic_reflection_pair_fails_the_deleted_edge_kernel() -> None:
    # At r=36, 51 is a twin center but its reflection 55 is not.  Therefore a
    # reflection-symmetric alphabet with that extra pair cannot be completely
    # hidden by the first-reentry defect kernel.
    with pytest.raises(ValueError):
        boundary_escape_zero_support_from_kernel(36, (36, 51, 55, 70))
