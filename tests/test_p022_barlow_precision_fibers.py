from itertools import product
from math import comb

from enterprise_math.p022_barlow_precision_fibers import (
    collapsed_unordered_word_pair_count,
    equal_observation_ordered_pair_count,
    final_imbalance_collapsed_pair_count,
    higher_collision_count,
    imbalance_fiber_size,
    imbalance_fiber_spectrum,
    selected_layer_observation,
    selected_observation_fiber_size,
    selected_observation_image_size,
    selected_segment_lengths,
    stacking_word_imbalance,
)


def _words(length: int):
    return tuple(product((-1, 1), repeat=length))


def test_final_imbalance_fibers_are_binomial() -> None:
    for length in range(0, 9):
        words = _words(length)
        for imbalance, expected in imbalance_fiber_spectrum(length):
            direct = sum(1 for word in words if stacking_word_imbalance(word) == imbalance)
            assert direct == expected == imbalance_fiber_size(length, imbalance)
        assert sum(size for _, size in imbalance_fiber_spectrum(length)) == 2 ** length


def test_selected_observation_fiber_size_matches_direct_word_enumeration() -> None:
    for length in range(1, 8):
        words = _words(length)
        candidate_layer_sets = (
            (),
            (length,),
            tuple(range(1, length + 1)),
            tuple(range(2, length + 1, 2)),
        )
        for selected_layers in candidate_layer_sets:
            fibers = {}
            for word in words:
                observed = selected_layer_observation(tuple(word), selected_layers)
                fibers.setdefault(observed, 0)
                fibers[observed] += 1
            assert len(fibers) == selected_observation_image_size(
                length, selected_layers
            )
            for observed, direct_size in fibers.items():
                assert selected_observation_fiber_size(
                    length, selected_layers, observed
                ) == direct_size


def test_selected_segment_lengths_and_unobserved_tail() -> None:
    assert selected_segment_lengths(10, (2, 5, 9)) == ((2, 3, 4), 1)
    assert selected_segment_lengths(10, ()) == ((), 10)
    assert selected_segment_lengths(10, (10,)) == ((10,), 0)


def test_ordered_equal_observation_pair_formula_matches_direct_enumeration() -> None:
    for length in range(0, 7):
        words = tuple(tuple(word) for word in _words(length))
        layer_sets = [()]
        if length:
            layer_sets.extend(
                [
                    (length,),
                    tuple(range(1, length + 1)),
                    tuple(range(2, length + 1, 2)),
                ]
            )
        for selected_layers in layer_sets:
            direct = sum(
                1
                for left in words
                for right in words
                if selected_layer_observation(left, selected_layers)
                == selected_layer_observation(right, selected_layers)
            )
            assert equal_observation_ordered_pair_count(
                length, selected_layers
            ) == direct


def test_final_layer_collision_pair_closed_form() -> None:
    for length in range(0, 12):
        direct_from_fibers = sum(
            comb(size, 2) for _, size in imbalance_fiber_spectrum(length)
        )
        assert final_imbalance_collapsed_pair_count(length) == direct_from_fibers
        assert collapsed_unordered_word_pair_count(
            length, (length,) if length else ()
        ) == direct_from_fibers
        if length:
            assert direct_from_fibers == (
                comb(2 * length, length) - 2 ** length
            ) // 2


def test_querying_every_prefix_layer_eliminates_all_collisions() -> None:
    for length in range(0, 12):
        selected_layers = tuple(range(1, length + 1))
        assert selected_observation_image_size(length, selected_layers) == 2 ** length
        assert equal_observation_ordered_pair_count(
            length, selected_layers
        ) == 2 ** length
        assert collapsed_unordered_word_pair_count(length, selected_layers) == 0


def test_no_observation_collapses_every_distinct_word_pair() -> None:
    for length in range(0, 10):
        assert selected_observation_image_size(length, ()) == 1
        assert equal_observation_ordered_pair_count(length, ()) == 4 ** length
        assert collapsed_unordered_word_pair_count(length, ()) == comb(2 ** length, 2)


def test_denser_checkpoint_language_strictly_reduces_collision_count_on_example() -> None:
    length = 8
    collisions = (
        collapsed_unordered_word_pair_count(length, (8,)),
        collapsed_unordered_word_pair_count(length, (4, 8)),
        collapsed_unordered_word_pair_count(length, (2, 4, 6, 8)),
        collapsed_unordered_word_pair_count(length, tuple(range(1, 9))),
    )
    assert collisions[0] > collisions[1] > collisions[2] > collisions[3] == 0


def test_higher_collision_count_matches_direct_fiber_formula() -> None:
    for length in range(0, 9):
        spectrum = imbalance_fiber_spectrum(length)
        for order in range(1, 6):
            expected = sum(
                comb(size, order) for _, size in spectrum if size >= order
            )
            assert higher_collision_count(length, order) == expected
