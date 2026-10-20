from enterprise_math.p018_pronic_euclidean_lift import (
    pronic_divisor_future_state,
    pronic_euclidean_lift,
)


def test_pronic_remainder_collapses_through_remainder_of_k():
    for k in range(2, 80):
        for n in range(1, 25):
            data = pronic_euclidean_lift(k, n)
            assert data["center_remainder_R"] == data["small_pronic_remainder_t"]
            assert data["remainder_collapses_to_small_pronic"] is True
            assert data["quotient_lift_exact"] is True
            assert data["small_pronic_quotient_c"] <= data["k_remainder_b"]


def test_finite_divisor_future_recovers_pronic_quotient_mod_d():
    for k, n in ((46, 11), (82, 17), (862, 37), (8191, 127)):
        for d in (3, 5, 7, 11, 35):
            data = pronic_divisor_future_state(k, n, d)
            assert data["Q_mod_d"] == data["reconstructed_Q_mod_d"]
            assert data["finite_divisor_future_state_exact"] is True


def test_explicit_two_level_identity():
    data = pronic_euclidean_lift(46, 11)
    a = data["k_quotient_a"]
    b = data["k_remainder_b"]
    c = data["small_pronic_quotient_c"]
    t = data["small_pronic_remainder_t"]
    assert 46 == a * 11 + b
    assert b * (b + 1) == c * 11 + t
    assert 46 * 47 == 11 * data["center_quotient_Q"] + t
