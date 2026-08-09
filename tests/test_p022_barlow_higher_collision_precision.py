from itertools import combinations, product
from math import comb

from enterprise_math.p022_barlow_higher_collision_precision import (
    balanced_checkpoint_layers,
    central_binomial_exchange_products,
    generalized_binomial_power_sum,
    minimal_spectrum_tradeoff,
    one_three_exchange_phase,
    one_three_to_two_two_moment_difference,
    ordered_equal_observation_tuple_count,
    selected_collision_count,
)
from enterprise_math.p022_barlow_precision_fibers import (
    selected_layer_observation,
    selected_observation_image_size,
)


def _words(length: int):
    return tuple(tuple(word) for word in product((-1, 1), repeat=length))


def _fiber_sizes(length: int, selected_layers: tuple[int, ...]) -> tuple[int, ...]:
    fibers: dict[tuple[int, ...], int] = {}
    for word in _words(length):
        observed = selected_layer_observation(word, selected_layers)
        fibers[observed] = fibers.get(observed, 0) + 1
    return tuple(fibers.values())


def _compositions(length: int, parts: int):
    for cuts in combinations(range(1, length), parts - 1):
        previous = 0
        segments = []
        for cut in cuts + (length,):
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


def test_generalized_binomial_power_sums_match_direct_definition() -> None:
    for length in range(0, 10):
        for order in range(1, 8):
            assert generalized_binomial_power_sum(length, order) == sum(
                comb(length, index) ** order for index in range(length + 1)
            )


def test_ordered_tuple_factorization_matches_direct_fiber_moments() -> None:
    for length in range(0, 8):
        schedules = [()]
        if length:
            schedules.extend(
                [
                    (length,),
                    tuple(range(1, length + 1)),
                    tuple(range(2, length + 1, 2)),
                ]
            )
        for selected_layers in schedules:
            fibers = _fiber_sizes(length, selected_layers)
            for order in range(1, 7):
                direct = sum(size ** order for size in fibers)
                assert ordered_equal_observation_tuple_count(
                    length, selected_layers, order
                ) == direct


def test_stirling_transform_matches_direct_p011_collision_counts() -> None:
    for length in range(0, 8):
        schedules = [()]
        if length:
            schedules.extend(
                [
                    (length,),
                    tuple(range(1, length + 1)),
                    tuple(range(2, length + 1, 2)),
                ]
            )
        for selected_layers in schedules:
            fibers = _fiber_sizes(length, selected_layers)
            for order in range(1, 8):
                direct = sum(
                    comb(size, order) for size in fibers if size >= order
                )
                assert selected_collision_count(
                    length, selected_layers, order
                ) == direct


def test_balanced_schedule_maximizes_image_and_minimizes_pair_collisions() -> None:
    for length in range(2, 11):
        for checkpoint_count in range(2, min(5, length) + 1):
            balanced = balanced_checkpoint_layers(length, checkpoint_count)
            balanced_image = selected_observation_image_size(length, balanced)
            balanced_j2 = selected_collision_count(length, balanced, 2)
            for segments in _compositions(length, checkpoint_count):
                layers = _layers(segments)
                assert selected_observation_image_size(
                    length, layers
                ) <= balanced_image
                assert selected_collision_count(length, layers, 2) >= balanced_j2


def test_pair_exchange_is_strict_when_segment_gap_is_at_least_two() -> None:
    for longer in range(3, 12):
        for shorter in range(1, longer - 1):
            before, after = central_binomial_exchange_products(longer, shorter)
            assert after < before


def test_full_collision_spectrum_has_no_single_balanced_optimum() -> None:
    tradeoff = minimal_spectrum_tradeoff()
    assert tradeoff["balanced_layers"] == (2, 4)
    assert tradeoff["unbalanced_layers"] == (1, 4)
    assert tradeoff["balanced_J1_J4"] == (16, 10, 4, 1)
    assert tradeoff["unbalanced_J1_J4"] == (16, 12, 4, 0)

    assert tradeoff["balanced_J1_J4"][1] < tradeoff["unbalanced_J1_J4"][1]
    assert tradeoff["balanced_J1_J4"][3] > tradeoff["unbalanced_J1_J4"][3]


def test_shortest_balancing_exchange_has_exact_moment_phase_transition() -> None:
    assert one_three_exchange_phase(1) == 0
    for order in (2, 3, 4):
        assert one_three_exchange_phase(order) == -1
        assert one_three_to_two_two_moment_difference(order) < 0
    for order in range(5, 20):
        assert one_three_exchange_phase(order) == 1
        assert one_three_to_two_two_moment_difference(order) > 0

    assert one_three_to_two_two_moment_difference(4) == -16
    assert one_three_to_two_two_moment_difference(5) == 180


def test_order_five_values_match_the_phase_formula() -> None:
    assert generalized_binomial_power_sum(1, 5) == 2
    assert generalized_binomial_power_sum(2, 5) == 34
    assert generalized_binomial_power_sum(3, 5) == 488
    assert 34**2 - 2 * 488 == 180
