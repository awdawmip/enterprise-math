from enterprise_math.p017_p018_walsh_minimal_boundary_amplifier import (
    minimal_boundary_amplifier_weight,
    minimal_boundary_walsh_profile,
    orientation_floor_coefficient,
    reusable_floor_product_cutoff,
    verify_pointwise_minimality,
)


def test_reusable_floor_cutoff_includes_odd_parity_factor_two():
    assert reusable_floor_product_cutoff(46) == 22
    assert reusable_floor_product_cutoff(82) == 40


def test_reusable_floor_columns_cancel_and_larger_products_need_no_floor_cancellation():
    low = orientation_floor_coefficient(46, (3, 5))
    high = orientation_floor_coefficient(46, (5, 11))
    assert low["selected_radical"] == 15
    assert low["orientation_floor_coefficient"] == 0
    assert low["reusable_floor_requires_cancellation"] is True
    assert high["selected_radical"] == 55
    assert high["coarse_floor_zero_by_parity_product"] is True
    assert high["orientation_floor_coefficient"] != 0


def test_minimality_forces_hard_value_only_below_exact_reusable_floor_cutoff():
    low = verify_pointwise_minimality(46, (3, 5))
    high = verify_pointwise_minimality(46, (5, 11))
    assert low["minimal_weight"] == 4
    assert low["minimality_reason"] == "ZERO_FLOOR_CONSTRAINT_FORCES_HARD_WALSH"
    assert high["minimal_weight"] == 1
    assert high["minimality_reason"] == (
        "PARITY_ANCHOR_FLOOR_ALREADY_ZERO_MINIMAL_POSITIVE_WEIGHT_ONE"
    )
    assert minimal_boundary_amplifier_weight(46, ()) == 1


def test_minimal_boundary_detector_preserves_prime_positivity_and_strictly_reduces_hard_weight():
    expected = {
        46: (44, 20),
        82: (86, 33),
        862: (636, 230),
    }
    for k, (hard, minimal) in expected.items():
        data = minimal_boundary_walsh_profile(k)
        assert data["hard_walsh_weighted_prime_observable"] == hard
        assert data["minimal_boundary_weighted_prime_observable"] == minimal
        assert minimal <= hard
        assert data["minimal_detector_positive_iff_prime_exists"] is True
        assert data["prime_mirror_side_exists"] is True


def test_one_side_minimal_weight_is_bounded_by_reusable_floor_support_depth():
    data = minimal_boundary_walsh_profile(8191)
    assert data["reusable_floor_product_cutoff"] == 4095
    assert data["reusable_floor_support_depth"] == 4
    assert data["one_side_weight_ceiling"] == 16
    assert data["minimal_boundary_weighted_prime_observable"] == 2519
    assert data["hard_walsh_weighted_prime_observable"] == 7118
