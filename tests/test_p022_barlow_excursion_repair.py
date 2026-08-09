from collections import Counter
from itertools import product
from math import comb

from enterprise_math.p022_barlow_excursion_repair import (
    absolute_history_collision_count,
    absolute_history_collision_polynomial_coefficients,
    absolute_history_count_with_excursions,
    absolute_history_fiber_profile,
    absolute_history_image_size,
    absolute_prefix_history,
    average_orientation_repair_load_fraction,
    excursion_count,
    excursion_count_spectrum,
    maximum_excursion_count,
    maximum_orientation_fiber_size,
    orientation_fiber_size,
    reconstruct_word_from_excursion_orientations,
    total_orientation_repair_bit_load,
)


def _words(length: int):
    return tuple(tuple(word) for word in product((-1, 1), repeat=length))


def _history_fibers(length: int):
    fibers = {}
    for word in _words(length):
        history = absolute_prefix_history(word)
        fibers.setdefault(history, []).append(word)
    return fibers


def test_orientation_fiber_is_exactly_one_bit_per_excursion() -> None:
    for length in range(0, 11):
        fibers = _history_fibers(length)
        for history, words in fibers.items():
            assert len(words) == orientation_fiber_size(history)
            excursions = excursion_count(history)
            assert len(words) == 2 ** excursions

            reconstructed = {
                reconstruct_word_from_excursion_orientations(history, orientation)
                for orientation in product((-1, 1), repeat=excursions)
            }
            assert reconstructed == set(words)


def test_absolute_history_image_size_is_central_binomial_prefix_count() -> None:
    for length in range(0, 15):
        direct = len(_history_fibers(length))
        assert direct == absolute_history_image_size(length)
        assert direct == comb(length, length // 2)


def test_excursion_count_closed_form_matches_direct_absolute_histories() -> None:
    for length in range(0, 13):
        direct = Counter(
            excursion_count(history) for history in _history_fibers(length)
        )
        assert dict(excursion_count_spectrum(length)) == dict(direct)
        for excursions, count in direct.items():
            assert absolute_history_count_with_excursions(
                length, excursions
            ) == count


def test_excursion_spectrum_counts_histories_and_microscopic_words_exactly() -> None:
    for length in range(0, 20):
        spectrum = excursion_count_spectrum(length)
        assert sum(count for _, count in spectrum) == absolute_history_image_size(length)
        assert sum((2 ** excursions) * count for excursions, count in spectrum) == 2 ** length


def test_complete_fiber_profile_matches_direct_grouping() -> None:
    for length in range(0, 11):
        direct = Counter(len(words) for words in _history_fibers(length).values())
        assert absolute_history_fiber_profile(length) == tuple(sorted(direct.items()))


def test_p011_collision_counts_match_direct_fiber_formula() -> None:
    for length in range(0, 11):
        profile = absolute_history_fiber_profile(length)
        coefficients = absolute_history_collision_polynomial_coefficients(length)
        for order, coefficient in enumerate(coefficients, start=1):
            direct = sum(
                history_count * comb(fiber_size, order)
                for fiber_size, history_count in profile
                if fiber_size >= order
            )
            assert absolute_history_collision_count(length, order) == direct
            assert coefficient == direct


def test_maximum_excursion_and_fiber_are_attained() -> None:
    for length in range(0, 15):
        direct_max = max(
            (excursion_count(history) for history in _history_fibers(length)),
            default=0,
        )
        assert direct_max == maximum_excursion_count(length)
        direct_fiber = max(
            (len(words) for words in _history_fibers(length).values()),
            default=1,
        )
        assert direct_fiber == maximum_orientation_fiber_size(length)


def test_total_repair_load_matches_direct_word_excursions() -> None:
    for length in range(0, 13):
        direct = sum(excursion_count(absolute_prefix_history(word)) for word in _words(length))
        assert total_orientation_repair_bit_load(length) == direct
        numerator, denominator = average_orientation_repair_load_fraction(length)
        assert numerator * (2 ** length) == direct * denominator


def test_closed_total_repair_load_matches_central_binomial_sum() -> None:
    for length in range(1, 30):
        direct_formula = sum(
            comb(2 * index, index) * 2 ** (length - 2 * index)
            for index in range((length - 1) // 2 + 1)
        )
        assert total_orientation_repair_bit_load(length) == direct_formula
