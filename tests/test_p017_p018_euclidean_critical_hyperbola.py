from enterprise_math.p017_p018_euclidean_critical_hyperbola import (
    critical_hyperbola_classification,
    cross_orientation_reuse_capacity,
    low_hyperbola_poisson_bounds,
)


def test_low_hyperbola_has_deterministic_tent_main_dominance():
    for k, q, d in ((46, 3, 5), (82, 5, 7), (862, 7, 11)):
        data = low_hyperbola_poisson_bounds(k, q, d)
        assert data["deterministic_main_dominated"] is True
        assert data["frequency_scale_H_q"] <= 1
        assert data["relative_oscillation_ceiling"] <= 1 / 3


def test_cross_orientation_crt_capacity_is_exact_and_high_products_are_single_use():
    for k, q, d in ((46, 7, 11), (82, 11, 13), (862, 29, 31)):
        M = k * (k + 1)
        data = cross_orientation_reuse_capacity(k, M, q, d)
        assert len(data["physical_hits"]) <= data["reuse_capacity_ceiling"]
        if q * d > k - 1:
            assert data["globally_single_use"] is True
            assert len(data["physical_hits"]) <= 1


def test_critical_surface_selects_reusable_vs_single_use_compilers():
    k = 82
    M = k * (k + 1)
    low = critical_hyperbola_classification(k, M, 5, 7)
    assert low["region"] == "LOW_REUSABLE_MAIN_DOMINATED"
    high = critical_hyperbola_classification(k, M, 11, 13)
    assert high["region"] == "HIGH_SINGLE_USE_BOUNDARY"
    assert high["high_capacity"]["globally_single_use"] is True
