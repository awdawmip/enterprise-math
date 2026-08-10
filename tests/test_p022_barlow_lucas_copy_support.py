from enterprise_math.p022_barlow_lucas_copy_support import (
    forced_copy_denominator_high_remainders_are_preprimitive,
    forced_copy_numerator_support_bound,
    forced_copy_pollution_is_single_digit,
    forced_copy_positive_pollution,
)


def test_forced_copy_numerator_tree_stays_below_q() -> None:
    for rank, prime in ((6, 73), (15, 179), (30, 1361), (30, 2593)):
        exact_max, bound = forced_copy_numerator_support_bound(rank, prime)
        assert exact_max <= bound < prime


def test_any_high_denominator_support_has_preprimitive_remainder() -> None:
    for rank, prime in ((6, 73), (15, 179), (30, 2593)):
        assert forced_copy_denominator_high_remainders_are_preprimitive(rank, prime)


def test_all_pollution_is_on_the_original_zero_alphabet() -> None:
    assert forced_copy_pollution_is_single_digit(6, 73) == ()
    assert forced_copy_pollution_is_single_digit(15, 179) == ()
    assert forced_copy_pollution_is_single_digit(30, 2593) == ((30, -1),)


def test_known_large_primitive_samples_have_no_positive_pollution() -> None:
    for rank, prime in ((6, 73), (15, 179), (9, 937), (30, 1361), (30, 2593), (21, 3019)):
        assert forced_copy_positive_pollution(rank, prime) == ()
