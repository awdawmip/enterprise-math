from enterprise_math.p017_p018_carry_quadratic_reflection import (
    mobius_carry_quadratic_reflection,
    orientation_dual_prime_count_diagnostic,
    physical_square_reflection,
)


def test_full_mobius_carry_reflection_holds_over_complete_common_periods():
    for primes in ((3,), (3, 5), (3, 5, 7)):
        primorial = 1
        for prime in primes:
            primorial *= prime
        for K in range(2 * primorial):
            data = mobius_carry_quadratic_reflection(K, primes)
            assert data["quadratic_reflection_identity"] is True
            assert (
                data["physical_carry_field"] + data["reflected_carry_field"]
                == data["half_roughness_bit"] - data["adjacent_roughness_bit"]
            )


def test_even_physical_reflection_defect_detects_only_powers_of_two():
    assert physical_square_reflection(8)["physical_reflection_defect"] == 1
    assert physical_square_reflection(16)["physical_reflection_defect"] == 1
    for k in (4, 6, 10, 12, 14, 18):
        data = physical_square_reflection(k)
        expected = int(k > 0 and k & (k - 1) == 0)
        assert data["physical_reflection_defect"] == expected


def test_odd_physical_reflection_defect_is_dyadic_successor_minus_twin_endpoint():
    # dyadic-successor examples
    assert physical_square_reflection(7)["physical_reflection_defect"] == 1
    assert physical_square_reflection(15)["physical_reflection_defect"] == 1
    # twin-prime endpoint examples
    assert physical_square_reflection(5)["physical_reflection_defect"] == -1
    assert physical_square_reflection(11)["physical_reflection_defect"] == -1
    assert physical_square_reflection(17)["physical_reflection_defect"] == -1
    # generic odd examples
    assert physical_square_reflection(9)["physical_reflection_defect"] == 0
    assert physical_square_reflection(13)["physical_reflection_defect"] == 0


def test_orientation_dual_identity_reconstructs_bounded_square_interval_prime_counts():
    for k in range(4, 30):
        data = orientation_dual_prime_count_diagnostic(k)
        assert data["orientation_dual_prime_count_identity"] is True
        assert data["orientation_dual_predicted_prime_count"] == data["actual_prime_count"]
