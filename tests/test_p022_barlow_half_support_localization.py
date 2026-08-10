from enterprise_math.p022_barlow_half_support_localization import (
    automatically_safe_companion_offset,
    dangerous_companion_offset_floor,
    integer_basis_index_bound,
    integer_basis_respects_index_bound,
    largest_prime_factor,
    target_half_support_localization,
    target_half_support_small_index_bound,
    target_support_offsets,
)
from enterprise_math.p022_barlow_low_order_defect_reduction import primes_through


def test_integer_basis_prime_halving_bound_on_initial_range() -> None:
    for value in range(2, 500):
        assert integer_basis_respects_index_bound(value)
        assert integer_basis_index_bound(value) == (largest_prime_factor(value) + 1) // 2


def test_target_residue_support_localization_exact_examples() -> None:
    # p=29 = 5 mod24, m=14: aside from m-1=13, all support is <=5.
    bound, support = target_half_support_localization(29)
    assert bound == 5
    assert support == (1, 2, 3, 4, 13)
    assert all(index == 13 or index <= 5 for index in support)

    # p=47 = 23 mod24, m=23: aside from 22, all support is <=12.
    bound, support = target_half_support_localization(47)
    assert bound == 12
    assert all(index == 22 or index <= 12 for index in support)


def test_localization_holds_for_target_primes_below_five_hundred() -> None:
    for prime in primes_through(499):
        if prime > 5 and prime % 24 in (5, 23):
            bound, support = target_half_support_localization(prime)
            midpoint = (prime - 1) // 2
            assert all(index == midpoint - 1 or index <= bound for index in support)


def test_near_midpoint_offsets_are_automatically_safe() -> None:
    # p=29: m=14, small-support bound=5, dangerous nontrivial offsets start at 9.
    assert dangerous_companion_offset_floor(29) == 9
    for offset in range(2, 9):
        assert automatically_safe_companion_offset(29, offset)
    assert not automatically_safe_companion_offset(29, 1)
    assert not automatically_safe_companion_offset(29, 9)

    # The actual support offsets are exactly the locations not excluded by the theorem.
    assert target_support_offsets(29) == (1, 10, 11, 12, 13)


def test_p_five_and_twenty_three_mod_twenty_four_have_expected_bounds() -> None:
    for prime in (29, 53, 101, 149, 173, 197):  # 5 mod24
        midpoint = (prime - 1) // 2
        assert target_half_support_small_index_bound(prime) == (midpoint + 1) // 3

    for prime in (23, 47, 71, 167, 191, 239):  # 23 mod24
        midpoint = (prime - 1) // 2
        assert target_half_support_small_index_bound(prime) == (midpoint + 1) // 2
