from enterprise_math.p022_barlow_zero_boundary_flux import (
    half_defect_boundary_coefficient,
    half_defect_sparse_marker_matches_exact,
    half_defect_sparse_support_zeros,
    prime_edge_weight,
    zero_boundary_crossing_weight,
    zero_boundary_flux_matches_edge_flux,
)


def test_zero_boundary_localization_matches_full_flux_on_small_states() -> None:
    for prime in (29, 149, 173, 269):
        for value in (3, 5, 7, 10, 14, 22):
            if value < prime:
                assert zero_boundary_flux_matches_edge_flux(value, prime)


def test_crossing_weight_has_expected_sign() -> None:
    # For p=173, F_4 is zero.  q=7=2*4-1 is the entering edge, so its
    # contribution has positive sign when the q=7 ancestor is present.
    assert prime_edge_weight(7, 7) == 1
    assert zero_boundary_crossing_weight(7, 4) == 1


def test_explicit_negative_marker_is_one_sparse_boundary_crossing() -> None:
    # p=369581, j=8: q=17=2j+1 occurs two more times on the midpoint DAG
    # than on the p-2 DAG, hence the signed crossing coefficient is -2.
    assert half_defect_boundary_coefficient(369_581, 8) == -2
    assert half_defect_sparse_support_zeros(369_581) == (8,)


def test_collision_can_cancel_between_the_two_dags() -> None:
    # p=26013917 divides F_19.  The q=37 entering edge occurs with equal
    # multiplicity on both DAGs, so the exact defect coefficient is zero.
    assert half_defect_boundary_coefficient(26_013_917, 19) == 0


def test_sparse_marker_matches_exact_on_small_target_primes() -> None:
    for prime in (23, 29, 47, 53, 71, 101, 149, 167, 173, 191, 197, 239, 269, 293):
        assert half_defect_sparse_marker_matches_exact(prime)
