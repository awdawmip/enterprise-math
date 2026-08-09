from itertools import product

from enterprise_math.p022_barlow_repair_complexity import (
    central_binomial_partial_average,
    diagonal_split_average,
    diagonal_total_identity,
    even_zero_overlap_correction,
    exact_average_identity,
    one_sided_orientation_average,
    orientation_total_identity,
    two_sided_repair_average_closed,
)
from enterprise_math.p022_barlow_two_sided_repair import (
    two_sided_repair_bit_count,
    unordered_absolute_pair_history,
)


def _words(length: int):
    return tuple(tuple(word) for word in product((-1, 1), repeat=length))


def _direct_average(length: int) -> tuple[int, int]:
    words = _words(length)
    total = 0
    for left in words:
        for right in words:
            total += two_sided_repair_bit_count(
                unordered_absolute_pair_history(left, right)
            )
    denominator = 4**length
    divisor = 1
    # Denominators are powers of two; reducing by repeated factors keeps the
    # oracle visibly integer-only.
    while total and total % 2 == 0 and denominator % 2 == 0:
        total //= 2
        denominator //= 2
        divisor *= 2
    return total, denominator


def test_one_sided_orientation_average_matches_existing_exact_total() -> None:
    for length in range(0, 40):
        left, right = orientation_total_identity(length)
        assert left == right


def test_diagonal_split_average_matches_existing_exact_total() -> None:
    for length in range(0, 30):
        left, right = diagonal_total_identity(length)
        assert left == right


def test_closed_average_decomposition_matches_independent_total_load() -> None:
    for length in range(0, 50):
        closed, direct = exact_average_identity(length)
        assert closed == direct


def test_closed_average_matches_direct_microscopic_grouping() -> None:
    for length in range(0, 7):
        assert two_sided_repair_average_closed(length) == _direct_average(length)


def test_known_initial_average_values_are_exact_rationals() -> None:
    expected = (
        (0, 1),
        (2, 1),
        (5, 2),
        (29, 8),
        (63, 16),
        (617, 128),
        (1297, 256),
        (5959, 1024),
        (12347, 2048),
        (219457, 32768),
        (451069, 65536),
    )
    assert tuple(two_sided_repair_average_closed(n) for n in range(11)) == expected


def test_central_binomial_partial_identity_by_common_denominator() -> None:
    # Directly sum C(2t,t)/4^t after lifting every term to 4^M.
    from math import comb

    for maximum in range(0, 30):
        denominator = 4**maximum
        numerator = sum(
            comb(2 * time, time) * (4 ** (maximum - time))
            for time in range(maximum + 1)
        )
        closed_num, closed_den = central_binomial_partial_average(maximum)
        assert numerator * closed_den == closed_num * denominator


def test_even_overlap_correction_is_exact_finite_sum() -> None:
    from math import comb

    for length in range(0, 30):
        m = (length - 1) // 2 if length else 0
        denominator = 16**m
        numerator = sum(
            (comb(2 * j, j) ** 2) * (16 ** (m - j))
            for j in range(1, m + 1)
        )
        closed_num, closed_den = even_zero_overlap_correction(length)
        assert numerator * closed_den == closed_num * denominator


def test_diagonal_average_is_nonnegative_and_zero_only_before_a_split_can_occur() -> None:
    assert diagonal_split_average(0) == (0, 1)
    assert diagonal_split_average(1) == (0, 1)
    for length in range(2, 30):
        assert diagonal_split_average(length)[0] > 0


def test_average_additional_repair_is_always_below_worst_case() -> None:
    for length in range(1, 80):
        numerator, denominator = two_sided_repair_average_closed(length)
        assert numerator < (length + 1) * denominator
