from enterprise_math.legendre import direct_square_interval_prime_count, is_prime
from enterprise_math.p017_p018_square_anchor_sieve_diagonal import (
    half_cutoff_rough_decomposition,
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


def test_half_cutoff_rough_set_is_exactly_primes_plus_short_semiprimes():
    for k in range(10, 61):
        data = half_cutoff_rough_decomposition(k)
        assert (
            data["prime_count_from_decomposition"]
            == direct_square_interval_prime_count(k)
        )
        assert data["half_rough_count"] == (
            data["prime_count_from_decomposition"] + data["semiprime_count"]
        )
        for left_prime, right_prime, value, offset in data["semiprime_edges"]:
            assert 2 * left_prime > k
            assert left_prime <= k < right_prime < 2 * k + 4
            assert is_prime(left_prime)
            assert is_prime(right_prime)
            assert value == left_prime * right_prime == k * k + offset


def test_half_cutoff_semiprime_graph_has_degree_one_two_and_twin_excess():
    for k in range(10, 81):
        data = half_cutoff_rough_decomposition(k)
        for _left_prime, neighbours in data["left_degrees"]:
            assert len(neighbours) <= 2
            if len(neighbours) == 2:
                assert neighbours[1] - neighbours[0] == 2
        for _right_prime, neighbours in data["right_degrees"]:
            assert len(neighbours) <= 1
        assert data["semiprime_count"] <= data["semiprime_capacity_bound"]


def test_half_buchstab_margin_is_a_finite_sufficient_certificate():
    for k in range(10, 81):
        data = half_cutoff_rough_decomposition(k)
        if data["half_buchstab_certificate_positive"]:
            assert data["half_buchstab_certificate_margin"] > 0
            assert direct_square_interval_prime_count(k) > 0
