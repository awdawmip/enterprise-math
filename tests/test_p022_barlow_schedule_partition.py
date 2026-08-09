from itertools import combinations

from enterprise_math.p022_barlow_collision_geometry import (
    collision_coefficients_from_selected_layers,
)
from enterprise_math.p022_barlow_schedule_partition import (
    all_final_observing_collision_state_count,
    all_final_observing_ordered_schedule_count,
    all_selected_layer_collision_state_count,
    all_selected_layer_schedule_count,
    average_geometry_fiber_all_selected_layers,
    average_order_fiber_over_collision_states,
    collision_state_count_final,
    ordered_final_schedule_count,
    partition_count_exact_parts,
    partition_number,
)


def _compositions(total: int, parts: int):
    if parts == 0:
        if total == 0:
            yield ()
        return
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


def test_partition_count_exact_parts_matches_sorted_composition_multisets() -> None:
    for total in range(1, 16):
        for parts in range(1, total + 1):
            multisets = {
                tuple(sorted(segments))
                for segments in _compositions(total, parts)
            }
            assert partition_count_exact_parts(total, parts) == len(multisets)


def test_partition_number_is_sum_over_exact_part_counts() -> None:
    known = (1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42, 56)
    assert tuple(partition_number(n) for n in range(len(known))) == known
    for total in range(0, 30):
        assert partition_number(total) == sum(
            partition_count_exact_parts(total, parts)
            for parts in range(total + 1)
        )


def test_fixed_nm_collision_states_are_integer_partitions() -> None:
    for total in range(1, 11):
        for parts in range(1, total + 1):
            collision_states = set()
            for segments in _compositions(total, parts):
                collision_states.add(
                    collision_coefficients_from_selected_layers(
                        total, _layers(segments)
                    )
                )
            assert len(collision_states) == collision_state_count_final(
                total, parts
            )
            assert ordered_final_schedule_count(total, parts) == sum(
                1 for _ in _compositions(total, parts)
            )


def test_all_final_observing_schedule_space_is_compositions_to_partitions() -> None:
    for total in range(1, 12):
        assert all_final_observing_ordered_schedule_count(total) == 2 ** (
            total - 1
        )
        assert all_final_observing_collision_state_count(total) == partition_number(
            total
        )


def test_arbitrary_checkpoint_subsets_map_to_tail_plus_partition_states() -> None:
    for total in range(0, 8):
        collision_states = set()
        layers = tuple(range(1, total + 1))
        for size in range(total + 1):
            for selected in combinations(layers, size):
                collision_states.add(
                    collision_coefficients_from_selected_layers(total, selected)
                )
        assert len(collision_states) == all_selected_layer_collision_state_count(
            total
        )
        assert all_selected_layer_schedule_count(total) == 2**total


def test_average_fiber_ratios_reconstruct_total_schedule_counts() -> None:
    for total in range(1, 20):
        numerator, denominator = average_geometry_fiber_all_selected_layers(total)
        assert numerator * all_selected_layer_collision_state_count(total) == (
            denominator * all_selected_layer_schedule_count(total)
        )

        for parts in range(1, total + 1):
            num, den = average_order_fiber_over_collision_states(total, parts)
            assert num * collision_state_count_final(total, parts) == (
                den * ordered_final_schedule_count(total, parts)
            )
