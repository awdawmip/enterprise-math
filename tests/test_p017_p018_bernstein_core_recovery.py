from enterprise_math.p017_p018_bernstein_core_recovery import (
    bernstein_recovery_parameters,
    bernstein_recovery_profile,
    bernstein_tail_coefficients,
    bernstein_tail_value,
)


def test_bernstein_tail_monomial_coefficients_match_direct_tail():
    for degree in (5, 10, 17):
        threshold = (13 * degree + 19) // 20
        coefficients = bernstein_tail_coefficients(degree, threshold)
        for z in (0.1, 0.5, 0.7, 0.9):
            direct = bernstein_tail_value(z, degree, threshold)
            expanded = sum(coefficient * (z**ell) for ell, coefficient in coefficients)
            assert abs(direct - expanded) <= 1e-9 * max(1.0, abs(direct), abs(expanded))


def test_universal_parameters_keep_recovery_gap_below_half_unit():
    for k in (46, 82, 1192, 8191):
        data = bernstein_recovery_parameters(k, 3)
        assert float(data["recovery_gap_ceiling"]) <= 0.5
        if not bool(data["exact_high_core_correction_is_zero"]):
            assert int(data["bernstein_degree"]) == 16 * int(data["epsilon_exponent"])
            assert int(data["bernstein_threshold"]) == (
                13 * int(data["bernstein_degree"]) + 19
            ) // 20


def test_bounded_direct_profiles_recover_integer_high_core_correction():
    for k in (46, 82, 1192):
        data = bernstein_recovery_profile(k, 3)
        assert data["diagnostic_recovery_matches"] is True
        assert int(data["diagnostic_ceil_q"]) == int(data["actual_high_core_correction"])
        assert -1e-8 <= float(data["diagnostic_gap"]) <= float(data["recovery_gap_ceiling"]) + 1e-7
