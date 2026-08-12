from fractions import Fraction

from enterprise_math.p017_p018_walsh_amplifier_pareto import (
    canonical_pareto_comparison,
    incidence_norm_lower_bound,
    reusable_downset_size,
)


def test_reusable_downset_counts_exact_floor_relevant_subsets():
    # C_46=22.  For {3,5,11}: 1,3,5,11,15 are reusable.
    assert reusable_downset_size(46, (3, 5, 11)) == 5


def test_l1_uncertainty_interpolates_between_pointwise_and_incidence_extrema():
    support = (3, 5, 11)
    point = incidence_norm_lower_bound(46, support, pointwise_weight=1, power=1)
    balanced = incidence_norm_lower_bound(46, support, pointwise_weight=5, power=1)
    assert point["reusable_downset_size"] == 5
    assert point["free_high_product_subset_count"] == 3
    assert point["incidence_power_sum_lower_bound"] == 9
    assert 1 + point["incidence_power_sum_lower_bound"] == 10
    assert balanced["incidence_power_sum_lower_bound"] == 5


def test_l2_holder_tradeoff_is_exact_rational_lower_bound():
    data = incidence_norm_lower_bound(46, (3, 5, 11), pointwise_weight=1, power=2)
    assert data["incidence_power_sum_lower_bound"] == Fraction(31, 3)


def test_canonical_compilers_are_distinct_pareto_endpoints_on_high_product_support():
    data = canonical_pareto_comparison(46, (3, 5, 11))
    assert data["pointwise_minimal_weight"] == 1
    assert data["pointwise_minimal_l1_lower_bound"] == 9
    assert data["incidence_optimal_weight"] == 5
    assert data["incidence_optimal_l1_cost"] == 5
    assert data["pareto_tradeoff"] is True


def test_low_product_support_has_no_tradeoff_because_all_incidence_is_forced():
    data = canonical_pareto_comparison(46, (3, 5))
    assert data["reusable_downset_size"] == 4
    assert data["pointwise_minimal_weight"] == 4
    assert data["incidence_optimal_weight"] == 4
    assert data["pareto_tradeoff"] is False
