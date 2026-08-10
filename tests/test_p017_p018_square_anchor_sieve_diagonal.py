from enterprise_math.legendre import direct_square_interval_prime_count, is_prime
from enterprise_math.p017_p018_square_anchor_sieve_diagonal import (
    square_root_diagonal_rough_count,
    verify_negative_square_phase,
)


def test_square_root_diagonal_rough_count_is_exact_prime_gap():
    for k in range(2, 41):
        data = square_root_diagonal_rough_count(k)
        assert data["rough_survivor_count"] == direct_square_interval_prime_count(k)
        assert data["interval_length"] == 2 * k
        assert data["root_equals_sieve_cutoff"] is True


def test_forbidden_offsets_are_exactly_minus_k_squared_mod_each_wheel_prime():
    for k in range(2, 31):
        data = verify_negative_square_phase(k)
        assert data["all_local_phases_square_compatible"] is True
        for prime, residue in data["forbidden_offset_residues"]:
            assert residue == (-k * k) % prime


def test_bounded_diagonal_rough_survivors_are_actual_primes():
    for k in (5, 10, 31, 64, 127):
        data = square_root_diagonal_rough_count(k)
        for offset in data["rough_survivor_offsets"]:
            value = k * k + offset
            assert k * k < value < (k + 1) * (k + 1)
            assert is_prime(value)
