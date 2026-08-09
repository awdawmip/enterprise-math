from itertools import product

from enterprise_math.p022_barlow_repair_tail import (
    counting_tail_bound_fraction,
    counting_tail_upper_bound,
    exact_tail_inequality,
    linear_repair_tail_bound_fraction,
    microscopic_high_repair_count,
    microscopic_high_repair_fraction,
    rational_linear_threshold,
)
from enterprise_math.p022_barlow_two_sided_repair import (
    two_sided_repair_bit_count,
    unordered_absolute_pair_history,
)


def _words(length: int):
    return tuple(tuple(word) for word in product((-1, 1), repeat=length))


def _direct_tail_count(length: int, threshold: int) -> int:
    words = _words(length)
    return sum(
        1
        for left in words
        for right in words
        if two_sided_repair_bit_count(
            unordered_absolute_pair_history(left, right)
        )
        >= threshold
    )


def test_exact_tail_counts_match_direct_microscopic_grouping() -> None:
    for length in range(0, 7):
        for threshold in range(0, length + 3):
            assert microscopic_high_repair_count(
                length, threshold
            ) == _direct_tail_count(length, threshold)


def test_tail_counting_inequality_holds_at_every_supported_threshold() -> None:
    for length in range(0, 30):
        for threshold in range(0, length + 3):
            left, right = exact_tail_inequality(length, threshold)
            assert left <= right
            assert microscopic_high_repair_count(
                length, threshold
            ) <= counting_tail_upper_bound(length, threshold)


def test_tail_fraction_is_exact_normalization() -> None:
    for length in range(0, 15):
        for threshold in range(0, length + 3):
            numerator, denominator = microscopic_high_repair_fraction(
                length, threshold
            )
            assert numerator * (4**length) == (
                microscopic_high_repair_count(length, threshold) * denominator
            )


def test_tail_bound_fraction_is_never_below_exact_tail() -> None:
    for length in range(1, 30):
        for threshold in range(1, length + 2):
            exact_num, exact_den = microscopic_high_repair_fraction(
                length, threshold
            )
            bound_num, bound_den = counting_tail_bound_fraction(
                length, threshold
            )
            assert exact_num * bound_den <= bound_num * exact_den


def test_rational_linear_threshold_is_exact_ceiling() -> None:
    for length in range(0, 30):
        for numerator, denominator in ((1, 2), (1, 3), (2, 3), (3, 5)):
            threshold = rational_linear_threshold(length, numerator, denominator)
            assert threshold * denominator >= numerator * length
            if threshold:
                assert (threshold - 1) * denominator < numerator * length


def test_linear_tail_bound_is_a_valid_finite_counting_bound() -> None:
    for length in range(1, 25):
        for numerator, denominator in ((1, 2), (1, 3), (2, 3)):
            threshold = rational_linear_threshold(length, numerator, denominator)
            exact_num, exact_den = microscopic_high_repair_fraction(
                length, threshold
            )
            bound_num, bound_den = linear_repair_tail_bound_fraction(
                length, numerator, denominator
            )
            assert exact_num * bound_den <= bound_num * exact_den


def test_highest_impossible_threshold_has_zero_exact_tail() -> None:
    for length in range(1, 30):
        assert microscopic_high_repair_count(length, length + 2) == 0
