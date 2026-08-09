from itertools import combinations

from enterprise_math.p022_barlow_collision_geometry import (
    collision_coefficients_from_profile,
    collision_coefficients_from_selected_layers,
    fiber_profile_from_collision_coefficients,
    recover_checkpoint_geometry_from_collision_coefficients,
)
from enterprise_math.p022_barlow_fiber_convolution import (
    profile_from_selected_layers,
)
from enterprise_math.p022_barlow_precision_fibers import selected_segment_lengths


def _selected_layer_sets(length: int):
    yield ()
    for count in range(1, min(length, 5) + 1):
        for layers in combinations(range(1, length + 1), count):
            yield tuple(layers)


def test_p011_binomial_inversion_roundtrips_barlow_profiles() -> None:
    for length in range(0, 11):
        for selected_layers in _selected_layer_sets(length):
            profile = profile_from_selected_layers(length, selected_layers)
            coefficients = collision_coefficients_from_profile(profile)
            assert fiber_profile_from_collision_coefficients(coefficients) == profile


def test_complete_collision_polynomial_recovers_unordered_checkpoint_geometry() -> None:
    for length in range(0, 11):
        for selected_layers in _selected_layer_sets(length):
            coefficients = collision_coefficients_from_selected_layers(
                length, selected_layers
            )
            segments, tail = selected_segment_lengths(length, selected_layers)
            assert recover_checkpoint_geometry_from_collision_coefficients(
                coefficients
            ) == (tuple(sorted(segments)), tail)


def test_segment_order_remains_invisible_to_collision_polynomial() -> None:
    # Same segment multiset, different checkpoint locations.
    first_segments = (1, 2, 3)
    second_segments = (3, 2, 1)
    first_layers = (1, 3, 6)
    second_layers = (3, 5, 6)
    assert first_segments != second_segments
    assert first_layers != second_layers

    first = collision_coefficients_from_selected_layers(6, first_layers)
    second = collision_coefficients_from_selected_layers(6, second_layers)
    assert first == second
    assert recover_checkpoint_geometry_from_collision_coefficients(first) == (
        (1, 2, 3),
        0,
    )


def test_hidden_tail_is_visible_in_collision_polynomial_through_fiber_scale() -> None:
    # Same observed segment multiset but different invisible tail gives a
    # different polynomial and the inverse recovers the tail exactly.
    first = collision_coefficients_from_selected_layers(6, (2, 4))
    second = collision_coefficients_from_selected_layers(8, (2, 4))
    assert first != second
    assert recover_checkpoint_geometry_from_collision_coefficients(first) == (
        (2, 2),
        2,
    )
    assert recover_checkpoint_geometry_from_collision_coefficients(second) == (
        (2, 2),
        4,
    )
