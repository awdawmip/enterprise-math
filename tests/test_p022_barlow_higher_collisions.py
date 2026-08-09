from collections import Counter
from itertools import combinations, product
from math import comb

from enterprise_math.p022_barlow_higher_collisions import (
    collision_count_from_power_moments,
    final_imbalance_power_moment,
    generalized_binomial_power_sum,
    ordered_equal_observation_tuple_count,
    selected_layer_collision_count,
    signed_stirling_first_kind,
)
from enterprise_math.p022_barlow_precision_fibers import selected_layer_observation


def _fiber_sizes(length: int, selected_layers: tuple[int, ...]) -> tuple[int, ...]:
    fibers: Counter[tuple[int, ...]] = Counter()
    for word in product((-1, 1), repeat=length):
        fibers[selected_layer_observation(tuple(word), selected_layers)] += 1
    return tuple(fibers.values())


def test_generalized_binomial_power_sum_matches_one_segment_fibers() -> None:
    for length in range(0, 10):
        fibers = tuple(comb(length, count) for count in range(length + 1))
        for order in range(1, 6):
            assert generalized_binomial_power_sum(length, order) == sum(
                fiber ** order for fiber in fibers
            )


def test_selected_observation_power_moments_factor_exactly() -> None:
    for length in range(0, 8):
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
            fibers = _fiber_sizes(length, selected_layers)
            for order in range(1, 6):
                direct = sum(fiber ** order for fiber in fibers)
                assert ordered_equal_observation_tuple_count(
                    length, selected_layers, order
                ) == direct


def test_signed_stirling_first_kind_coefficients() -> None:
    assert signed_stirling_first_kind(0) == (1,)
    assert signed_stirling_first_kind(1) == (0, 1)
    assert signed_stirling_first_kind(2) == (0, -1, 1)
    assert signed_stirling_first_kind(3) == (0, 2, -3, 1)
    assert signed_stirling_first_kind(4) == (0, -6, 11, -6, 1)


def test_power_moments_recover_p011_collision_counts() -> None:
    for length in range(0, 8):
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
            fibers = _fiber_sizes(length, selected_layers)
            for order in range(1, 6):
                moments = [0] + [
                    sum(fiber ** power for fiber in fibers)
                    for power in range(1, order + 1)
                ]
                direct = sum(comb(fiber, order) for fiber in fibers if fiber >= order)
                assert collision_count_from_power_moments(
                    tuple(moments), order
                ) == direct
                assert selected_layer_collision_count(
                    length, selected_layers, order
                ) == direct


def test_final_imbalance_power_moment_is_generalized_franel_sum() -> None:
    for length in range(0, 12):
        for order in range(1, 7):
            assert final_imbalance_power_moment(
                length, order
            ) == generalized_binomial_power_sum(length, order)


def test_dense_checkpoint_language_has_no_higher_collisions() -> None:
    for length in range(0, 10):
        selected_layers = tuple(range(1, length + 1))
        assert selected_layer_collision_count(length, selected_layers, 1) == 2 ** length
        for order in range(2, 6):
            assert selected_layer_collision_count(length, selected_layers, order) == 0


def test_no_observation_has_one_full_fiber() -> None:
    for length in range(0, 10):
        domain = 2 ** length
        for order in range(1, min(6, domain + 1)):
            assert selected_layer_collision_count(length, (), order) == comb(
                domain, order
            )
