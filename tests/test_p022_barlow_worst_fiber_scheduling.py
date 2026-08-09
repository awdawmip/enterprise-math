from itertools import combinations

from enterprise_math.p022_barlow_higher_collision_precision import (
    checkpoint_layers_from_segments,
)
from enterprise_math.p022_barlow_worst_fiber_scheduling import (
    central_fiber_factor,
    collision_free_above_maximum_fiber,
    maximum_fiber_from_checkpoint_layers,
    maximum_fiber_from_segments,
    minimax_segment_multisets,
    minimum_possible_maximum_fiber,
    odd_pair_increment_factor,
    odd_to_even_increment_factor,
)


def _compositions(length: int, parts: int):
    for cuts in combinations(range(1, length), parts - 1):
        previous = 0
        result = []
        for cut in cuts + (length,):
            result.append(cut - previous)
            previous = cut
        yield tuple(result)


def test_increment_factors_match_central_binomial_ratios() -> None:
    assert odd_to_even_increment_factor() == 2
    previous_num = None
    previous_den = None
    for pair_index in range(1, 15):
        numerator, denominator = odd_pair_increment_factor(pair_index)
        before = central_fiber_factor(2 * pair_index - 1)
        after = central_fiber_factor(2 * pair_index + 1)
        assert after * denominator == before * numerator
        assert numerator < 4 * denominator
        if previous_num is not None:
            assert numerator * previous_den > previous_num * denominator
        previous_num, previous_den = numerator, denominator

        odd = 2 * pair_index + 1
        assert central_fiber_factor(odd + 1) == 2 * central_fiber_factor(odd)


def test_closed_minimax_value_matches_all_small_positive_compositions() -> None:
    for length in range(1, 15):
        for checkpoint_count in range(1, min(length, 6) + 1):
            values = [
                (maximum_fiber_from_segments(segments), tuple(sorted(segments)))
                for segments in _compositions(length, checkpoint_count)
            ]
            minimum = min(value for value, _ in values)
            minimizing_multisets = tuple(
                sorted({segments for value, segments in values if value == minimum})
            )
            assert minimum_possible_maximum_fiber(
                length, checkpoint_count
            ) == minimum
            assert minimax_segment_multisets(
                length, checkpoint_count
            ) == minimizing_multisets


def test_checkpoint_layer_form_matches_segment_product() -> None:
    for length in range(2, 12):
        for checkpoint_count in range(1, min(length, 5) + 1):
            for segments in minimax_segment_multisets(length, checkpoint_count):
                layers = checkpoint_layers_from_segments(segments)
                assert maximum_fiber_from_checkpoint_layers(
                    length, layers
                ) == maximum_fiber_from_segments(segments)
                assert maximum_fiber_from_segments(
                    segments
                ) == minimum_possible_maximum_fiber(length, checkpoint_count)


def test_near_dense_case_explains_three_vs_two_two_tradeoff() -> None:
    # N=m+2: pair-balanced minimax uses one length-three segment and all other
    # segments length one, whereas ordinary length balancing uses two length-two
    # segments when m>=2.
    for checkpoint_count in range(2, 10):
        length = checkpoint_count + 2
        minimizers = minimax_segment_multisets(length, checkpoint_count)
        expected = tuple(sorted((1,) * (checkpoint_count - 1) + (3,)))
        assert minimizers == (expected,)
        assert minimum_possible_maximum_fiber(length, checkpoint_count) == 3
        assert collision_free_above_maximum_fiber(3) == 4


def test_minimax_schedule_pushes_zero_tail_of_collision_spectrum_as_low_as_possible() -> None:
    for length in range(2, 12):
        for checkpoint_count in range(1, min(length, 5) + 1):
            minimum = minimum_possible_maximum_fiber(length, checkpoint_count)
            first_zero = collision_free_above_maximum_fiber(minimum)
            for segments in _compositions(length, checkpoint_count):
                assert maximum_fiber_from_segments(segments) >= minimum
                assert maximum_fiber_from_segments(segments) + 1 >= first_zero
