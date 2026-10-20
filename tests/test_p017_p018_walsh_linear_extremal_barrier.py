from math import e, log

from enterprise_math.p017_p018_walsh_linear_extremal_barrier import (
    cutoff_family_negative_boundary,
    power_cutoff_extremal_diagnostic,
)


def test_endpoint_regions_fail_for_different_exact_reasons():
    shallow = power_cutoff_extremal_diagnostic(0.30)
    assert shallow["route_classification"] == "LOCAL_WALSH_MARGIN_NONPOSITIVE"
    assert shallow["local_margin_positive"] is False

    deep = power_cutoff_extremal_diagnostic(0.60)
    assert deep["route_classification"] == "LOWER_SIEVE_NONPOSITIVE_S_LE_2"
    assert deep["ordinary_lower_linear_sieve_positive"] is False


def test_only_apparent_overlap_still_fails_extremal_constant_comparison():
    for alpha in (0.38, 0.40, 0.45, 0.49):
        data = power_cutoff_extremal_diagnostic(alpha)
        assert 1 / e < alpha < 0.5
        assert 2 < data["s"] < e < 3
        assert data["local_margin_positive"] is True
        assert data["ordinary_lower_linear_sieve_positive"] is True
        assert data["f_over_F_when_2_lt_s_lt_3"] == log(data["s"] - 1)
        assert data["f_over_F_when_2_lt_s_lt_3"] < data["local_harmonic_limit_log_s"]
        assert data["independent_extremal_margin"] < 0
        assert data["independent_linear_sieve_route_closes"] is False


def test_whole_power_cutoff_family_is_exhausted_by_the_three_regions():
    data = cutoff_family_negative_boundary()
    assert data["positive_local_margin_requires_alpha_gt"] == 1 / e
    assert data["positive_ordinary_lower_sieve_requires_alpha_lt"] == 0.5
    assert data["all_power_cutoffs_fail_independent_extremal_treatment"] is True
    assert data["required_new_input"] == "SIGNED_CORRELATION_OR_BILINEAR_INFORMATION"
