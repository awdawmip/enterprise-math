from enterprise_math.p017_p018_root_p3_mobius_descent import (
    mobius_descent_transport_row,
    root_p3_mobius_descent_profile,
)


def test_pointwise_transport_law_covers_prime_and_composite_rows():
    # k=100 has z_3=10.
    prime = mobius_descent_transport_row(100, 10009)
    repeated_a = mobius_descent_transport_row(100, 10043)  # 11^2 * 83
    repeated_b = mobius_descent_transport_row(100, 10051)  # 19 * 23^2
    assert prime["quotient_mobius_sum"] == 0
    assert prime["mobius_descent_curvature"] == 3
    assert repeated_a["quotient_mobius_sum"] == 1
    assert repeated_a["mobius_descent_curvature"] == 0
    assert repeated_b["quotient_mobius_sum"] == 1
    assert repeated_b["mobius_descent_curvature"] == 0


def test_state_and_swapped_quotient_channel_sums_agree():
    for k in (4, 5, 8, 17, 31, 64, 100, 257):
        data = root_p3_mobius_descent_profile(k)
        assert data["exact_mobius_descent_recovery"] is True
        assert data["descent_prime_identity_rhs"] == 3 * data["prime_count"]
        assert data["mobius_descent_curvature_sum"] == (
            3 * data["prime_count"] + data["rough_prime_cube_count"]
        )


def test_k1000_descent_checkpoint():
    data = root_p3_mobius_descent_profile(1000)
    assert data["fourth_root_cutoff"] == 31
    assert data["rough_count"] == 309
    assert data["prime_count"] == 152
    assert data["descent_prime_identity_rhs"] == 456
