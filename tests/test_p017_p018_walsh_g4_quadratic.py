from enterprise_math.p017_p018_walsh_g4_quadratic import (
    g4_quadratic_value,
    walsh_g4_orientation_point,
    walsh_g4_profile,
)


def test_g4_quadratic_values_match_prime_semiprime_repeated_squarefree_spectrum():
    assert [g4_quadratic_value(c) for c in range(4)] == [3, 0, -1, 0]


def test_repeated_triple_is_the_only_negative_raw_class_and_is_repaired_single_use():
    # Search a bounded nontrivial scale for one repeated-triple row; the module
    # itself certifies c=2 iff a unique repeated medium prime occurs.
    found = None
    for k in (46, 82, 100, 202, 862):
        data = walsh_g4_profile(k)
        rows = [row for row in data["rows"] if row["repeated_triple"]]
        if rows:
            found = rows[0]
            break
    assert found is not None
    assert found["target_medium_support_size"] == 2
    assert found["raw_walsh_g4_weight"] < 0
    assert found["repeated_single_use_correction"] > 0
    assert found["corrected_walsh_g4_weight"] == 0
    assert found["repeated_prime"] ** 2 > found["k"]


def test_corrected_walsh_g4_is_exact_nonnegative_prime_detector():
    for k in (46, 82, 202, 862):
        data = walsh_g4_profile(k)
        assert data["raw_plus_repeated_equals_corrected"] is True
        assert data["repeated_prime_global_single_use"] is True
        assert data["corrected_weighted_prime_signal_times_three"] > 0
        assert data["positive_corrected_iff_prime_exists"] is True
        assert data["one_orientation_quadratic_floor_main"] == 3 * data["smooth_shadow"][
            "smooth_shadow_count_Psi"
        ]
        assert data["symmetric_quadratic_floor_main"] == 6 * data["smooth_shadow"][
            "smooth_shadow_count_Psi"
        ]


def test_every_nonprime_corrected_row_is_zero():
    data = walsh_g4_profile(202)
    for row in data["rows"]:
        if row["target_prime"]:
            assert row["corrected_walsh_g4_weight"] > 0
        else:
            assert row["corrected_walsh_g4_weight"] == 0
