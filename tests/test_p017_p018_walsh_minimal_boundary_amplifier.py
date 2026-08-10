from enterprise_math.p017_p018_walsh_minimal_boundary_amplifier import (
    minimal_boundary_amplifier_weight,
    minimal_boundary_walsh_profile,
    orientation_floor_coefficient,
    verify_pointwise_minimality,
)


def test_low_product_columns_cancel_and_high_product_columns_need_no_floor_cancellation():
    low = orientation_floor_coefficient(46, (3, 5))
    high = orientation_floor_coefficient(46, (5, 11))
    assert low["selected_radical"] == 15
    assert low["orientation_floor_coefficient"] == 0
    assert low["low_product_requires_cancellation"] is True
    assert high["selected_radical"] == 55
    assert high["coarse_floor_zero_by_product"] is True
    assert high["orientation_floor_coefficient"] != 0


def test_minimality_forces_hard_value_only_below_reusable_product_cutoff():
    low = verify_pointwise_minimality(46, (3, 5))
    high = verify_pointwise_minimality(46, (5, 11))
    assert low["minimal_weight"] == 4
    assert low["minimality_reason"] == "ZERO_FLOOR_CONSTRAINT_FORCES_HARD_WALSH"
    assert high["minimal_weight"] == 1
    assert high["minimality_reason"] == "FLOOR_ALREADY_ZERO_MINIMAL_POSITIVE_WEIGHT_ONE"
    assert minimal_boundary_amplifier_weight(46, ()) == 1


def test_minimal_boundary_detector_preserves_prime_positivity_and_strictly_reduces_hard_weight():
    expected = {
        46: (44, 22),
        82: (86, 36),
        862: (636, 265),
    }
    for k, (hard, minimal) in expected.items():
        data = minimal_boundary_walsh_profile(k)
        assert data["hard_walsh_weighted_prime_observable"] == hard
        assert data["minimal_boundary_weighted_prime_observable"] == minimal
        assert minimal <= hard
        assert data["minimal_detector_positive_iff_prime_exists"] is True
        assert data["prime_mirror_side_exists"] is True


def test_one_side_minimal_weight_is_bounded_by_transverse_precision_depth():
    data = minimal_boundary_walsh_profile(8191)
    assert data["transverse_primorial_depth"] == 4
    assert data["one_side_weight_ceiling"] == 16
    assert data["minimal_boundary_weighted_prime_observable"] == 2781
    assert data["hard_walsh_weighted_prime_observable"] == 7118
