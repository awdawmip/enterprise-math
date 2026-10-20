from enterprise_math.p017_p018_mirror_cross_cutoff import (
    cross_local_model,
    mirror_cross_cutoff_point,
    mirror_cross_cutoff_profile,
)


def test_double_rough_quadratic_separator_has_exact_prime_side_sign():
    # k=23,r=13 is double rough at cutoff 4: lower 539=7^2*11 is composite,
    # upper 565=5*113 is also composite, so the separator must be nonpositive.
    composite = mirror_cross_cutoff_point(23, 13, 4)
    assert composite["double_rough"] is True
    assert composite["prime_side"] is False
    assert composite["quadratic_separator"] <= 0

    # A prime-containing double-rough example at the same scale.
    rows = mirror_cross_cutoff_profile(23, 4)["rows"]
    prime_rows = [row for row in rows if row.get("double_rough") and row.get("prime_side")]
    assert prime_rows
    assert all(row["quadratic_separator"] > 0 for row in prime_rows)


def test_aggregate_positive_separator_is_a_valid_prime_certificate():
    for k, cutoff in ((23, 4), (46, 6), (82, 9)):
        data = mirror_cross_cutoff_profile(k, cutoff)
        assert data["positive_is_prime_certificate"] is True


def test_cross_local_model_uses_ordered_distinct_medium_prime_pairs():
    data = cross_local_model(46, 6)
    L = data["harmonic_mass_L"]
    Q2 = data["diagonal_square_mass_Q2"]
    assert data["ordered_cross_overlap_local_ratio"] == L * L - Q2
    assert data["quadratic_separator_local_coefficient"] == 1 - (L * L - Q2)
