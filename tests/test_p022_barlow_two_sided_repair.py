from collections import Counter
from itertools import product

from enterprise_math.p022_barlow_two_sided_repair import (
    diagonal_split_count,
    microscopic_word_pair_realizations,
    ordered_absolute_history_realizations,
    total_zero_departure_events,
    two_sided_microscopic_fiber_size,
    two_sided_repair_bit_count,
    unordered_absolute_pair_history,
)


def _words(length: int):
    return tuple(tuple(word) for word in product((-1, 1), repeat=length))


def _pair_fibers(length: int):
    fibers = {}
    words = _words(length)
    for left in words:
        for right in words:
            history = unordered_absolute_pair_history(left, right)
            fibers.setdefault(history, []).append((left, right))
    return fibers


def test_exact_fiber_size_is_two_to_excursions_plus_diagonal_splits() -> None:
    for length in range(0, 7):
        fibers = _pair_fibers(length)
        for history, words in fibers.items():
            predicted = two_sided_microscopic_fiber_size(history)
            assert predicted == 2 ** two_sided_repair_bit_count(history)
            assert len(words) == predicted


def test_full_repair_enumerates_all_and_only_microscopic_word_pairs() -> None:
    for length in range(0, 6):
        fibers = _pair_fibers(length)
        for history, words in fibers.items():
            assert set(microscopic_word_pair_realizations(history)) == set(words)


def test_ordered_absolute_realizations_use_exactly_one_bit_per_diagonal_split() -> None:
    for length in range(0, 8):
        for history in _pair_fibers(length):
            realizations = ordered_absolute_history_realizations(history)
            assert len(realizations) == 2 ** diagonal_split_count(history)


def test_zero_departure_count_is_invariant_across_label_realizations() -> None:
    from enterprise_math.p022_barlow_excursion_repair import excursion_count

    for length in range(0, 7):
        for history in _pair_fibers(length):
            expected = total_zero_departure_events(history)
            for left_history, right_history in ordered_absolute_history_realizations(history):
                assert excursion_count(left_history) + excursion_count(right_history) == expected


def test_split_bits_occur_only_when_equal_channels_break_symmetry() -> None:
    # length three example:
    # (1,1) -> (0,2) is a split and needs one side-label bit.
    left = (1, -1, 1)
    right = (1, 1, -1)
    history = unordered_absolute_pair_history(left, right)
    assert history[:2] == ((1, 1), (0, 2))
    assert diagonal_split_count(history) >= 1


def test_two_sided_fiber_profile_reconstructs_all_microscopic_pairs() -> None:
    for length in range(0, 7):
        direct = Counter(
            len(words) for words in _pair_fibers(length).values()
        )
        assert sum(fiber_size * history_count for fiber_size, history_count in direct.items()) == 4 ** length
        assert all(fiber_size & (fiber_size - 1) == 0 for fiber_size in direct)
