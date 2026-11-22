from enterprise_math.p017_p018_walsh_incidence_optimal import (
    incidence_optimal_alpha,
    incidence_optimal_profile,
    incidence_optimal_weight,
    root_pattern_l1_cost,
    verify_forced_low_product_incidence,
)


def test_low_product_incidence_coefficients_are_forced_to_one_and_cancel_floor():
    for support in ((3,), (5,), (3, 5)):
        assert incidence_optimal_alpha(46, support) == 1
        data = verify_forced_low_product_incidence(46, support)
        assert data["reusable_floor_set"] is True
        assert data["orientation_floor_coefficient_beta"] == 0
        assert data["boundary_only"] is True


def test_high_product_incidence_is_zero_and_selected_column_is_floor_free_geometrically():
    assert incidence_optimal_alpha(46, (5, 11)) == 0
    data = verify_forced_low_product_incidence(46, (5, 11))
    assert data["selected_radical"] == 55
    assert data["reusable_floor_product_cutoff"] == 22
    assert data["reusable_floor_set"] is False
    assert data["boundary_only"] is True


def test_incidence_optimal_weight_counts_only_reusable_floor_subsets():
    # C_46=22.  For {3,5,11}, reusable subsets are 1,3,5,11,15.
    assert incidence_optimal_weight(46, (3, 5, 11)) == 5
    data = root_pattern_l1_cost(46, (3, 5, 11))
    assert data["minimal_root_pattern_l1_cost"] == 5
    assert data["incidence_optimal_weight"] == 5
    assert data["hard_walsh_root_pattern_l1_cost"] == 8


def test_incidence_optimal_detector_preserves_prime_positivity_and_reduces_hard_weight():
    expected = {
        37: (16, 15),
        46: (44, 27),
        82: (86, 53),
        862: (636, 417),
    }
    for k, (hard, optimal) in expected.items():
        data = incidence_optimal_profile(k)
        assert data["hard_walsh_weighted_prime_observable"] == hard
        assert data["incidence_optimal_weighted_prime_observable"] == optimal
        assert optimal <= hard
        assert data["positive_iff_prime_exists"] is True
        assert data["prime_exists"] is True


def test_large_pressure_point_keeps_only_floor_relevant_divisor_incidence():
    data = incidence_optimal_profile(8191)
    assert data["reusable_floor_product_cutoff"] == 4095
    assert data["hard_walsh_weighted_prime_observable"] == 7118
    assert data["incidence_optimal_weighted_prime_observable"] == 4688
    assert data["positive_iff_prime_exists"] is True
