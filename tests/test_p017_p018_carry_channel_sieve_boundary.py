from itertools import product

from enterprise_math.p017_p018_carry_channel_sieve_boundary import (
    mobius_descendant_sieve_identity,
    ramanujan_channel_rough_count,
    realize_pairwise_coprime_carry_bits,
)


def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 1
    return True


def _odd_prime_wheel(limit: int) -> int:
    wheel = 1
    for value in range(3, limit + 1, 2):
        if _is_prime(value):
            wheel *= value
    return wheel


def _prime_count_between_consecutive_squares(k: int) -> int:
    return sum(_is_prime(value) for value in range(k * k + 1, (k + 1) * (k + 1)))


def test_descendant_mobius_cube_is_exact_channel_rough_count():
    for K in range(0, 31):
        for parent in (1, 3, 5, 7, 9):
            for wheel in (1, 3, 5, 7, 15, 21, 35, 105):
                data = mobius_descendant_sieve_identity(K, parent, wheel)
                assert data["exact_sieve_collapse"] is True
                assert data["mobius_fiber_sum"] == data["channel_rough_count"]
                assert data["mobius_carry_sum"] == data["rough_count_discrepancy"]


def test_e1_full_odd_prime_wheel_recovers_prime_gap_and_dyadic_reference():
    for k in range(2, 31):
        K = k - 1
        wheel = _odd_prime_wheel(K)
        data = mobius_descendant_sieve_identity(K, 1, wheel)
        assert data["channel_rough_count"] == _prime_count_between_consecutive_squares(k)
        assert data["reference_rough_count"] == K.bit_length()
        assert (
            data["reference_rough_count"] + data["mobius_carry_sum"]
            == _prime_count_between_consecutive_squares(k)
        )


def test_channel_fourier_conductor_expansion_is_exact_ramanujan_roughness():
    for wheel in (1, 3, 5, 15, 21, 105, 1155):
        for fiber_size in range(0, 13):
            first_quotients = (None,) if fiber_size == 0 else (-9, -1, 1, 7, 21)
            for first_quotient in first_quotients:
                data = ramanujan_channel_rough_count(fiber_size, first_quotient, wheel)
                assert data["exact_ramanujan_reconstruction"] is True
                assert data["rough_count"] == data["direct_rough_count"]


def test_pairwise_coprime_centered_carries_have_full_boolean_crt_expressivity():
    moduli = (3, 5, 7, 11)
    for parity in (0, 1):
        for bits in product((0, 1), repeat=len(moduli)):
            data = realize_pairwise_coprime_carry_bits(
                moduli,
                bits,
                parity,
                minimum_K=10_000,
            )
            assert data["realized_bits"] == bits
            assert data["K"] >= 10_000
            assert data["K"] % 2 == parity
            shifted = realize_pairwise_coprime_carry_bits(
                moduli,
                bits,
                parity,
                minimum_K=data["K"] + data["period"],
            )
            assert shifted["realized_bits"] == bits
            assert shifted["K"] >= data["K"] + data["period"]


def test_independence_needs_coprime_moduli_not_prime_moduli():
    data = realize_pairwise_coprime_carry_bits(
        (9, 25, 7),
        (1, 0, 1),
        parity=1,
        minimum_K=1000,
    )
    assert data["realized_bits"] == (1, 0, 1)
