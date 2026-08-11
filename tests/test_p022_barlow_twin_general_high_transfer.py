from fractions import Fraction

from enterprise_math.p022_barlow_twin_general_high_transfer import (
    fixed_general_high_numerator_gcd,
    fixed_general_high_parameters,
    fixed_transfer_residue_class_is_compatible,
    forced_midpoint_c_candidates,
    general_high_affine_data,
    general_high_c_interval,
    quadratic_remainder_gap,
)


def test_general_high_c_window_is_strictly_short_and_forced_unique() -> None:
    expected = {
        (96, 3): ((23, 27), (24,)),
        (90, 6): ((20, 24), (24,)),
        (285, 15): ((17, 21), (18,)),
        (576, 63): ((-28, -24), (-24,)),
    }
    for (rank, gap), (window, candidates) in expected.items():
        assert general_high_c_interval(rank, gap) == window
        assert forced_midpoint_c_candidates(rank, gap) == candidates
        assert window[1] - window[0] <= 5


def test_affine_digit_data_eliminates_the_moving_rank_parameter() -> None:
    high, prime, low, delta = general_high_affine_data(90, 6, 24)
    assert (high, prime, low, delta) == (96, 647, 546, 72)
    assert prime % 24 == 23

    rho, fixed_delta, x = fixed_general_high_parameters(6, 24)
    assert rho == Fraction(73, 8)
    assert fixed_delta == delta == 72
    assert x == Fraction(4225, 32)
    assert (8 * 90 - (8 * 6 + 24 + 1)) == prime


def test_quadratic_remainders_have_the_unwrapped_fixed_gap() -> None:
    # This arithmetic candidate is far enough into the seven-rank horizon and
    # both universal quadratic remainders lie in the primitive symmetric band.
    left, right, delta = quadratic_remainder_gap(90, 6, 24)
    assert (left, right, delta) == (314, 386, 72)
    assert right - left == delta


def test_small_general_branches_have_coprime_fixed_transfers() -> None:
    assert fixed_general_high_numerator_gcd(3, 24) == 1
    assert fixed_general_high_numerator_gcd(6, 24) == 1
    assert fixed_general_high_numerator_gcd(15, 18) == 1


def test_plain_coprimality_is_too_strong_but_the_first_exception_is_incompatible() -> None:
    # Pressure boundary: the universal conjecture gcd=1 is false.  This exact
    # pair has gcd 701, but c=-120 requires q=23 mod24 whereas 701=5 mod24.
    assert fixed_general_high_numerator_gcd(51, -120) == 701
    assert not fixed_transfer_residue_class_is_compatible(51, -120, 701)
