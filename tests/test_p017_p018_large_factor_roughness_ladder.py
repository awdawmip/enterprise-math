from enterprise_math.p017_p018_large_factor_roughness_ladder import (
    cofactor_factor_capacity,
    square_large_factor_roughness_certificate,
)


def test_product_capacity_counts_remaining_factors_exactly():
    data = cofactor_factor_capacity(10_000, 101, 9)
    assert data["cofactor_max"] == 99
    assert data["cofactor_omega_capacity"] == 1
    assert data["total_omega_capacity"] == 2


def test_joint_large_factor_and_roughness_can_certify_prime():
    # 10009 is prime.  Treating its full value as the known large prime factor
    # leaves cofactor capacity zero, hence P1 exactly.
    data = square_large_factor_roughness_certificate(100, 10009, 25, 1)
    assert data["target_almost_prime_certified"] is True
    assert data["total_omega_capacity"] == 1


def test_joint_witness_p2_threshold_is_strict_product_condition():
    # Synthetic finite scales: if the remaining cofactor is <(y+1)^2, then the
    # full state has at most two prime factors once one large prime is known.
    data = square_large_factor_roughness_certificate(1000, 800_000, 31, 2)
    assert data["target_almost_prime_certified"] == data["finite_product_condition"]
