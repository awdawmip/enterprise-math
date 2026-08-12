from enterprise_math.p022_barlow_franel_midpoint_harmonic_pairing import (
    harmonic_difference_pair,
    midpoint_central_sum,
    midpoint_harmonic_companions,
    midpoint_term_reflection,
)


def test_midpoint_term_and_harmonic_reflections() -> None:
    for prime in (5, 7, 13, 23, 29, 31):
        midpoint = (prime - 1) // 2
        for index in range(midpoint + 1):
            left, right = midpoint_term_reflection(prime, index)
            assert left == right
            fk, fmirror, hm = harmonic_difference_pair(prime, index)
            assert (fk + fmirror) % prime == hm


def test_forced_midpoint_central_sum_vanishes() -> None:
    for prime in (5, 7, 13, 23, 29, 31, 37, 47):
        assert midpoint_central_sum(prime) == 0


def test_harmonic_companion_pairing_is_exact() -> None:
    expected = {
        5: (2, 1, 0),
        7: (4, 2, 0),
        13: (10, 5, 0),
        23: (14, 7, 0),
        29: (18, 9, 0),
        31: (8, 4, 0),
        37: (35, 36, 0),
        47: (4, 2, 0),
    }
    for prime, values in expected.items():
        assert midpoint_harmonic_companions(prime) == values
