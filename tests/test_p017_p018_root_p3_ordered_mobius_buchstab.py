from enterprise_math.p017_p018_root_p3_ordered_mobius_buchstab import (
    fourth_root_ordered_transport,
    mobius_rough_sum,
    ordered_mobius_transport,
)


def test_terminal_cutoff_mobius_sum_is_minus_prime_count():
    for k in (4, 5, 8, 17, 31, 64, 100):
        data = ordered_mobius_transport(k, k)
        assert data["ordered_transport_sum"] == 0
        assert data["terminal_mobius_sum"] == -data["prime_count"]


def test_ordered_cutoff_jumps_telescope_from_several_starts():
    for k in (8, 17, 31, 64):
        for cutoff in (0, 2, 3, k // 2, k):
            data = ordered_mobius_transport(k, cutoff)
            assert data["exact_ordered_recovery"] is True
            assert data["prime_count"] == -data["start_mobius_sum"] - data["ordered_transport_sum"]


def test_fourth_root_ordered_quotients_stay_below_p2_ceiling():
    for k in (8, 17, 31, 64, 100, 257):
        data = fourth_root_ordered_transport(k)
        ceiling = data["quotient_p2_ceiling"]
        assert all(q <= ceiling for _, q, _ in data["ordered_quotient_rows"])
        assert data["exact_ordered_recovery"] is True


def test_k1000_fourth_root_ordered_transport_recovers_152_primes():
    data = fourth_root_ordered_transport(1000)
    assert data["fourth_root_cutoff"] == 31
    assert data["prime_count"] == 152
    assert data["prime_count"] == -data["start_mobius_sum"] - data["ordered_transport_sum"]
