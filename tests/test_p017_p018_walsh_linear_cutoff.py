from enterprise_math.p017_p018_walsh_linear_cutoff import (
    cutoff_local_harmonic,
    cutoff_walsh_orientation_point,
    cutoff_walsh_profile,
)
from enterprise_math.p017_p018_walsh_minimal_boundary_amplifier import reusable_floor_product_cutoff


def test_linear_cutoff_weight_is_positive_exactly_on_prime_target_and_nonpositive_on_composites():
    # k=17, r=1: upper 307 is prime.
    prime = cutoff_walsh_orientation_point(17, 1, 4, "upper")
    assert prime["target_state"] == 307
    assert prime["target_prime"] is True
    assert prime["linear_cutoff_weight"] > 0

    # k=17, r=7: lower 299=13*23 has no factor <=4, hence one visible high support prime <=k.
    composite = cutoff_walsh_orientation_point(17, 7, 4, "lower")
    assert composite["target_state"] == 299
    assert composite["target_prime"] is False
    assert composite["target_low_support"] == ()
    assert composite["high_band_support_count"] >= 1
    assert composite["linear_cutoff_weight"] <= 0


def test_fourth_root_scale_has_positive_complete_coordinate_margin_on_bounded_examples():
    # Integer fourth-root cutoffs for these scales are 6 and 9 respectively.
    for k, cutoff in ((46, 6), (82, 9)):
        local = cutoff_local_harmonic(k, cutoff)
        assert local["positive_local_model_margin"] is True
        profile = cutoff_walsh_profile(k, cutoff)
        assert profile["symmetric_linear_cutoff_weight"] > 0
        assert profile["prime_exists"] is True


def test_half_cutoff_makes_every_composite_weight_zero_and_prime_signal_nonnegative():
    for k in (17, 46, 82):
        cutoff = reusable_floor_product_cutoff(k)
        profile = cutoff_walsh_profile(k, cutoff)
        assert profile["half_cutoff_terminal_exact"] is True
        assert profile["symmetric_linear_cutoff_weight"] > 0
        assert profile["prime_exists"] is True
        assert all(row["pair_weight"] >= 0 for row in profile["rows"])
