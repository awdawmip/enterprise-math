from enterprise_math.p017_p018_carry_roughness_discrepancy import (
    carry_roughness_discrepancy,
    full_small_prime_origin_is_dyadic,
)


def test_centered_mobius_carry_is_exact_roughness_displacement_discrepancy():
    for K, primes in (
        (9, (3, 5, 7)),
        (21, (3, 5, 7)),
        (45, (3, 5, 7, 11)),
        (81, (3, 5, 7, 11, 13)),
    ):
        data = carry_roughness_discrepancy(K, primes)
        assert data["carry_is_roughness_displacement_discrepancy"] is True
        assert data["mobius_exact_fiber_sum"] == data["square_basin_roughness_count"]
        assert data["mobius_floor_sum"] == data["origin_roughness_count"]
        assert data["mobius_carry_field"] == (
            data["square_basin_roughness_count"] - data["origin_roughness_count"]
        )
        assert data["channelized_square_roughness_count"] == data["square_basin_roughness_count"]


def test_full_odd_small_prime_origin_shadow_is_exactly_the_binary_axis():
    data = full_small_prime_origin_is_dyadic(20, (3, 5, 7, 11, 13, 17, 19))
    assert data["origin_rough_values"] == (1, 2, 4, 8, 16)
    assert data["dyadic_axis"] == (1, 2, 4, 8, 16)
    assert data["origin_roughness_is_exactly_dyadic"] is True
