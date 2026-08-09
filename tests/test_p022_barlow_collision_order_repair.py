from itertools import permutations
from math import comb

from enterprise_math.p022_barlow_collision_geometry import (
    collision_coefficients_from_selected_layers,
)
from enterprise_math.p022_barlow_collision_order_repair import (
    balanced_schedule_order_fiber_size,
    checkpoint_layers_from_ordered_segments,
    collision_coefficients_ignore_segment_order,
    complete_geometry_state_cardinality_from_collision,
    ordered_geometry_fiber_size_from_collision_coefficients,
    ordered_segment_geometry_fiber_size,
)


def _distinct_permutations(segments: tuple[int, ...]):
    return set(permutations(segments))


def test_multinomial_order_fiber_size_matches_direct_distinct_permutations() -> None:
    examples = (
        (1,),
        (1, 1),
        (1, 2),
        (1, 1, 2),
        (1, 2, 3),
        (2, 2, 3, 3),
        (1, 2, 2, 3, 3, 3),
    )
    for segments in examples:
        assert ordered_segment_geometry_fiber_size(segments) == len(
            _distinct_permutations(segments)
        )


def test_complete_collision_polynomial_is_invariant_under_segment_permutation() -> None:
    for segments in ((1, 2, 3), (1, 1, 2, 3), (2, 2, 3, 4)):
        values = {
            collision_coefficients_ignore_segment_order(tuple(order))
            for order in _distinct_permutations(segments)
        }
        assert len(values) == 1


def test_every_segment_permutation_gives_a_distinct_checkpoint_layer_tuple() -> None:
    for segments in ((1, 2, 3), (1, 1, 2, 3), (2, 2, 3, 4)):
        layer_sets = {
            checkpoint_layers_from_ordered_segments(tuple(order))
            for order in _distinct_permutations(segments)
        }
        assert len(layer_sets) == ordered_segment_geometry_fiber_size(segments)


def test_collision_inversion_recovers_exact_remaining_order_fiber() -> None:
    examples = (
        ((1, 2, 3), 0),
        ((1, 1, 2, 3), 2),
        ((2, 2, 3, 4), 3),
    )
    for segments, hidden_tail in examples:
        coefficients = collision_coefficients_ignore_segment_order(
            segments, hidden_tail
        )
        recovered_segments, recovered_tail, order_fiber = (
            complete_geometry_state_cardinality_from_collision(coefficients)
        )
        assert recovered_segments == tuple(sorted(segments))
        assert recovered_tail == hidden_tail
        assert order_fiber == ordered_segment_geometry_fiber_size(segments)
        assert ordered_geometry_fiber_size_from_collision_coefficients(
            coefficients
        ) == order_fiber


def test_balanced_schedule_order_fiber_has_closed_binomial_count() -> None:
    for length in range(1, 30):
        for checkpoints in range(1, length + 1):
            base, remainder = divmod(length, checkpoints)
            segments = (base,) * (checkpoints - remainder) + (
                (base + 1,) * remainder
            )
            assert ordered_segment_geometry_fiber_size(
                segments
            ) == balanced_schedule_order_fiber_size(length, checkpoints)
            assert balanced_schedule_order_fiber_size(
                length, checkpoints
            ) == comb(checkpoints, remainder)


def test_exact_equal_spacing_has_no_order_ambiguity() -> None:
    for checkpoints in range(1, 12):
        for base in range(1, 8):
            length = checkpoints * base
            assert balanced_schedule_order_fiber_size(length, checkpoints) == 1


def test_hidden_tail_does_not_change_order_fiber_cardinality() -> None:
    segments = (1, 2, 2, 4)
    expected = ordered_segment_geometry_fiber_size(segments)
    for hidden_tail in range(0, 8):
        coefficients = collision_coefficients_ignore_segment_order(
            segments, hidden_tail
        )
        assert ordered_geometry_fiber_size_from_collision_coefficients(
            coefficients
        ) == expected


def test_ordered_schedule_collision_coefficients_match_direct_selected_layers() -> None:
    segments = (3, 1, 2)
    hidden_tail = 2
    selected_layers = checkpoint_layers_from_ordered_segments(
        segments, hidden_tail
    )
    total_length = sum(segments) + hidden_tail
    assert collision_coefficients_ignore_segment_order(
        segments, hidden_tail
    ) == collision_coefficients_from_selected_layers(
        total_length, selected_layers
    )
