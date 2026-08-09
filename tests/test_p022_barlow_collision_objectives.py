from itertools import combinations

from enterprise_math.p022_barlow_collision_geometry import (
    collision_coefficients_from_selected_layers,
    fiber_profile_from_collision_coefficients,
)
from enterprise_math.p022_barlow_collision_objectives import (
    checkpoint_objective_summary,
    collision_image_size,
    collision_max_fiber_count,
    collision_max_fiber_size,
    collision_objective_summary,
    collision_pair_ambiguity,
)


def _compositions(total: int, parts: int):
    for cuts in combinations(range(1, total), parts - 1):
        previous = 0
        segments = []
        for cut in cuts + (total,):
            segments.append(cut - previous)
            previous = cut
        yield tuple(segments)


def _layers(segments: tuple[int, ...]) -> tuple[int, ...]:
    running = 0
    result = []
    for segment in segments:
        running += segment
        result.append(running)
    return tuple(result)


def test_generic_collision_functionals_match_inverted_fiber_profile() -> None:
    for total in range(1, 11):
        for parts in range(1, total + 1):
            for segments in _compositions(total, parts):
                coefficients = collision_coefficients_from_selected_layers(
                    total, _layers(segments)
                )
                profile = fiber_profile_from_collision_coefficients(coefficients)
                assert collision_image_size(coefficients) == sum(
                    count for _, count in profile
                )
                assert collision_pair_ambiguity(coefficients) == sum(
                    count * size * (size - 1) // 2
                    for size, count in profile
                )
                maximum = max(size for size, _ in profile)
                assert collision_max_fiber_size(coefficients) == maximum
                assert collision_max_fiber_count(coefficients) == dict(profile)[
                    maximum
                ]


def test_minimal_pair_vs_degree_tradeoff_is_visible_in_one_polynomial() -> None:
    balanced = collision_coefficients_from_selected_layers(4, (2, 4))
    unbalanced = collision_coefficients_from_selected_layers(4, (1, 4))

    assert balanced == (16, 10, 4, 1)
    assert unbalanced == (16, 12, 4)

    assert collision_image_size(balanced) == 9
    assert collision_image_size(unbalanced) == 8
    assert collision_pair_ambiguity(balanced) == 10
    assert collision_pair_ambiguity(unbalanced) == 12
    assert collision_max_fiber_size(balanced) == 4
    assert collision_max_fiber_size(unbalanced) == 3

    # Balanced improves image and J2 but worsens collision-polynomial degree.
    assert collision_image_size(balanced) > collision_image_size(unbalanced)
    assert collision_pair_ambiguity(balanced) < collision_pair_ambiguity(
        unbalanced
    )
    assert collision_max_fiber_size(balanced) > collision_max_fiber_size(
        unbalanced
    )


def test_collision_summary_includes_post_aggregation_order_repair() -> None:
    # N=10,m=4 comparison from the order-repair theorem.
    balanced = checkpoint_objective_summary(10, (2, 4, 7, 10))
    concentrated = checkpoint_objective_summary(10, (1, 4, 7, 10))

    # (image, J2, max fiber, number of max fibers, order fiber)
    assert balanced[0] == 144
    assert concentrated[0] == 128
    assert balanced[1] == 6688
    assert concentrated[1] == 7488
    assert balanced[4] == 6
    assert concentrated[4] == 4

    assert balanced[0] > concentrated[0]
    assert balanced[1] < concentrated[1]
    assert balanced[4] > concentrated[4]


def test_summary_matches_individual_functionals() -> None:
    for total in range(1, 12):
        for parts in range(1, min(total, 5) + 1):
            for segments in _compositions(total, parts):
                layers = _layers(segments)
                coefficients = collision_coefficients_from_selected_layers(
                    total, layers
                )
                summary = collision_objective_summary(coefficients)
                assert summary[:4] == (
                    collision_image_size(coefficients),
                    collision_pair_ambiguity(coefficients),
                    collision_max_fiber_size(coefficients),
                    collision_max_fiber_count(coefficients),
                )
                assert checkpoint_objective_summary(total, layers) == summary
