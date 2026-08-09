from enterprise_math.p022_barlow_defect_core_obstruction import (
    obstruction_vector_by_defect_150,
)
from enterprise_math.p022_barlow_defect_core_saturation import (
    PAIRING_ONE,
    PAIRING_TWO,
)
from enterprise_math.p022_barlow_franel_marker_primes import (
    HORIZON_150,
    MARKER_12,
    MARKER_66,
    franel_occurrence_indices,
    marker_reads_relation_coefficient,
    private_franel_marker,
    verify_saturation_markers_150,
)
from enterprise_math.p022_barlow_low_order_defect_reduction import (
    composite_A_relation_exponents,
    composite_indices,
)


def test_saturation_primes_are_simple_private_Franel_markers_through_150() -> None:
    assert franel_occurrence_indices(MARKER_12, HORIZON_150) == (12,)
    assert franel_occurrence_indices(MARKER_66, HORIZON_150) == (66,)
    assert private_franel_marker(MARKER_12, HORIZON_150) == (12, 1)
    assert private_franel_marker(MARKER_66, HORIZON_150) == (66, 1)


def test_marker_indices_are_prime_boundary_segments() -> None:
    assert 2 * 12 - 1 == 23
    assert 2 * 66 - 1 == 131


def test_private_marker_rows_read_central_binomial_relation_coefficients() -> None:
    for segment in composite_indices(HORIZON_150):
        actual_12, expected_12 = marker_reads_relation_coefficient(
            MARKER_12, 12, segment, horizon=HORIZON_150
        )
        actual_66, expected_66 = marker_reads_relation_coefficient(
            MARKER_66, 66, segment, horizon=HORIZON_150
        )
        assert actual_12 == expected_12
        assert actual_66 == expected_66


def test_obstruction_pairings_can_be_computed_from_relation_coefficients_only() -> None:
    sparse = dict(obstruction_vector_by_defect_150())

    pairing_12 = 0
    pairing_66 = 0
    for segment, coefficient in sparse.items():
        alpha = dict(composite_A_relation_exponents(segment))
        pairing_12 += coefficient * (-alpha.get(12, 0))
        pairing_66 += coefficient * (-alpha.get(66, 0))

    # Saturation module names q=73589 as pairing one and q=176459 as two.
    assert pairing_66 == PAIRING_ONE == -13_311
    assert pairing_12 == PAIRING_TWO == 2_518


def test_full_marker_verifier_passes() -> None:
    assert verify_saturation_markers_150()
