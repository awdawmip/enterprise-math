from enterprise_math.p022_barlow_franel_zero_geometry import (
    forced_midpoint_is_primitive,
    forced_midpoint_profile,
    forced_midpoint_zero_count_is_odd,
    zero_digits_are_nonadjacent,
    zero_digits_are_reflection_symmetric,
)
from enterprise_math.p022_barlow_low_order_defect_reduction import primes_through


def test_zero_digit_symmetry_and_nonadjacency_on_small_primes() -> None:
    for prime in primes_through(199):
        if prime <= 2:
            continue
        assert zero_digits_are_reflection_symmetric(prime)
        assert zero_digits_are_nonadjacent(prime)


def test_forced_midpoint_zero_alphabet_has_odd_size() -> None:
    for prime in primes_through(199):
        if prime > 2 and prime % 8 in (5, 7):
            assert forced_midpoint_zero_count_is_odd(prime)


def test_midpoint_primitivity_is_minimal_zero_alphabet() -> None:
    # p=23 has the singleton zero alphabet {11}; the forced midpoint is primitive.
    midpoint, rank, zero_count, primitive = forced_midpoint_profile(23)
    assert (midpoint, rank, zero_count, primitive) == (11, 11, 1, True)
    assert forced_midpoint_is_primitive(23)

    # p=29 has zero alphabet {12,14,16}; midpoint 14 is not primitive.
    midpoint, rank, zero_count, primitive = forced_midpoint_profile(29)
    assert (midpoint, rank, zero_count, primitive) == (14, 12, 3, False)
    assert not forced_midpoint_is_primitive(29)


def test_more_forced_profiles_preserve_rank_bound_and_parity() -> None:
    for prime in (5, 7, 13, 31, 47, 53, 71, 101, 149, 173, 191):
        midpoint, rank, zero_count, _ = forced_midpoint_profile(prime)
        assert rank <= midpoint
        assert zero_count >= 1
        assert zero_count % 2 == 1
