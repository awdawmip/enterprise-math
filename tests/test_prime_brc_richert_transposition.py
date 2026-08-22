from fractions import Fraction

from enterprise_math.prime_brc_richert_transposition import (
    abel_prefix_recoalescence,
    brc_before_absolute_value,
    campbell_hit_count,
    cofactor_sift_count,
    cofactor_window,
    cofactor_windows_are_disjoint,
    prefix_remainder,
    shell_remainder,
    shell_sift_count,
)


def test_l054_cofactor_windows_replay_disjoint():
    ps = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
    assert cofactor_windows_are_disjoint(31, ps)
    assert cofactor_windows_are_disjoint(31, ps, campbell=True)


def test_campbell_window_excludes_exact_upper_endpoint_hit():
    # k=10: full P017 includes 120=5*24; Campbell A(100)=(100,120) excludes it.
    full = cofactor_window(10, 5)
    strict = cofactor_window(10, 5, campbell=True)
    assert full == (21, 24)
    assert strict == (21, 23)
    assert campbell_hit_count(10, 5) == 3


def test_shell_to_cofactor_sift_transposition_both_endpoint_conventions():
    # z=5, so the supplied sifting primes are 2 and 3; shell primes are >=5.
    z_primes = (2, 3)
    for p in (5, 7, 11, 13, 17, 19):
        assert shell_sift_count(31, p, z_primes) == cofactor_sift_count(31, p, z_primes)
        assert shell_sift_count(31, p, z_primes, campbell=True) == cofactor_sift_count(
            31, p, z_primes, campbell=True
        )


def test_abel_prefix_identity_exact():
    data = abel_prefix_recoalescence(
        (Fraction(3), Fraction(5), Fraction(7)),
        (Fraction(5, 6), Fraction(1, 2), Fraction(1, 6)),
    )
    assert data["shell_sum"] == data["prefix_sum"]
    assert data["prefix_values"] == (Fraction(3), Fraction(8), Fraction(15))


def test_prefix_remainder_is_sum_before_absolute_value():
    ps = (5, 7, 11)
    for d in (2, 3, 6, 10, 15):
        assert prefix_remainder(31, ps, d) == sum(
            (shell_remainder(31, p, d) for p in ps), Fraction(0)
        )
        assert prefix_remainder(31, ps, d, campbell=True) == sum(
            (shell_remainder(31, p, d, campbell=True) for p in ps), Fraction(0)
        )


def test_brc_before_absolute_value_never_worse_and_can_be_strict():
    rows = (
        {2: Fraction(1, 2), 3: Fraction(-1, 3)},
        {2: Fraction(-1, 2), 3: Fraction(1, 3)},
        {2: Fraction(1, 2), 3: Fraction(1, 3)},
    )
    weights = (Fraction(1), Fraction(2, 3), Fraction(1, 3))
    result = brc_before_absolute_value(rows, weights, (2, 3))
    assert result["prefix_l1"] <= result["shell_l1"]
    assert result["saving"] > 0
