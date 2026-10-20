from enterprise_math.p017_p018_walsh_euclidean_modulus_shell import (
    euclidean_modulus_shell,
    euclidean_orientation_channels,
    verify_direct_modulus_roots,
)


def test_low_modulus_shell_has_multiple_unit_step_quotient_lifts():
    data = euclidean_orientation_channels(46, 5)
    assert data["shell_quotient_a"] == 9
    assert data["scale_remainder_s"] == 1
    assert data["remainder_quotient_h"] == 0
    assert data["center_remainder_u"] == 2
    assert data["quotient_center_Q0"] == 432
    assert tuple(row["radius"] for row in data["lower_divisible_channel"]) == (7, 17, 27, 37)
    assert tuple(row["quotient"] for row in data["lower_divisible_channel"]) == (431, 429, 427, 425)
    assert tuple(row["radius"] for row in data["upper_divisible_channel"]) == (3, 13, 23, 33, 43)
    assert tuple(row["quotient"] for row in data["upper_divisible_channel"]) == (433, 435, 437, 439, 441)


def test_high_modulus_shell_is_single_use_in_each_orientation():
    data = euclidean_orientation_channels(46, 29)
    assert data["shell_quotient_a"] == 1
    assert data["scale_remainder_s"] == 17
    assert data["remainder_quotient_h"] == 10
    assert data["center_remainder_u"] == 16
    assert data["quotient_center_Q0"] == 74
    assert data["high_modulus_single_use_shell"] is True
    assert data["lower_divisible_channel"] == ({"j": 1, "radius": 45, "quotient": 73},)
    assert data["upper_divisible_channel"] == ({"j": 0, "radius": 13, "quotient": 75},)


def test_shell_formula_reconstructs_center_exactly():
    data = euclidean_modulus_shell(82, 13)
    assert data["center"] == data["modulus"] * data["quotient_center_Q0"] + data["center_remainder_u"]


def test_direct_root_enumeration_matches_euclidean_shells():
    for k, divisors in ((46, (5, 7, 11, 13, 17, 29, 31, 37, 41, 43)), (82, (7, 11, 13, 17, 19, 23, 29, 31))):
        M = k * (k + 1)
        for d in divisors:
            if M % d == 0:
                continue
            data = verify_direct_modulus_roots(k, d)
            assert data["direct_root_crosscheck"] is True
