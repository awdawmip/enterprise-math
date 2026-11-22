from enterprise_math.p017_p018_walsh_degree_adaptive_cutoff import (
    adaptive_cutoff_zone,
    degree_adaptive_cutoff_profile,
    degree_adaptive_orientation_weight,
    degree_collapse_at_p2,
)


def test_degree_two_collapses_to_degree_one_at_p2_boundary():
    for k in (82, 862, 8191):
        data = degree_collapse_at_p2(k)
        assert data["normalized_semantics_match_at_p2"] is True
        assert data["degree_two_below_p2"] is True
        assert data["degree_one_at_and_above_p2"] is True


def test_cutoff_zone_uses_quadratic_then_linear_exact_prime_semantics():
    for k in (82, 862):
        z3, z2, C = adaptive_cutoff_zone(k)
        cutoffs = sorted({z3, max(z3, z2 - 1), z2, C})
        for cutoff in cutoffs:
            data = degree_adaptive_cutoff_profile(k, cutoff)
            assert data["positive_iff_prime_exists"] is True
            assert data["common_floor_main_is_3Psi"] is True
            assert data["proof_degree"] == (2 if cutoff < z2 else 1)


def test_prime_orientation_weight_is_always_three_times_visible_amplifier():
    # k=82 has many bounded examples; locate one prime-side radius through the profile.
    z3, z2, C = adaptive_cutoff_zone(82)
    for cutoff in (z3, z2, C):
        profile = degree_adaptive_cutoff_profile(82, cutoff)
        prime_rows = [row for row in profile["rows"] if row["target_prime"]]
        assert prime_rows
        for row in prime_rows[:5]:
            data = degree_adaptive_orientation_weight(
                82, int(row["radius"]), cutoff, str(row["orientation"])
            )
            assert data["corrected_weight"] == 3 * data["low_walsh_amplifier"]
            assert data["exact_prime_semantics"] is True
