from itertools import combinations

from enterprise_math.p022_barlow_checkpoint_design import (
    balanced_schedule_joint_objectives,
    maximum_image_size_with_checkpoint_count,
    maximum_image_size_with_final_checkpoint,
    minimum_image_size_with_checkpoint_count,
    minimum_image_size_with_final_checkpoint,
)
from enterprise_math.p022_barlow_precision_fibers import (
    equal_observation_ordered_pair_count,
    selected_observation_image_size,
)


def test_balanced_final_visible_schedule_maximizes_image_and_minimizes_collisions() -> None:
    for length in range(1, 12):
        for checkpoint_count in range(1, length + 1):
            records = []
            for prefix in combinations(range(1, length), checkpoint_count - 1):
                layers = tuple(prefix) + (length,)
                records.append(
                    (
                        layers,
                        selected_observation_image_size(length, layers),
                        equal_observation_ordered_pair_count(length, layers),
                    )
                )
            balanced_layers, balanced_image, balanced_collisions = (
                balanced_schedule_joint_objectives(length, checkpoint_count)
            )
            assert balanced_image == max(record[1] for record in records)
            assert balanced_collisions == min(record[2] for record in records)
            assert (
                balanced_layers,
                balanced_image,
                balanced_collisions,
            ) in records


def test_final_visible_image_extrema_match_exhaustive_checkpoint_placement() -> None:
    for length in range(1, 12):
        for checkpoint_count in range(1, length + 1):
            values = []
            for prefix in combinations(range(1, length), checkpoint_count - 1):
                layers = tuple(prefix) + (length,)
                values.append(selected_observation_image_size(length, layers))
            assert maximum_image_size_with_final_checkpoint(
                length, checkpoint_count
            ) == max(values)
            assert minimum_image_size_with_final_checkpoint(
                length, checkpoint_count
            ) == min(values)


def test_optional_final_checkpoint_image_extrema_match_all_schedules() -> None:
    for length in range(0, 11):
        for checkpoint_count in range(0, length + 1):
            values = [
                selected_observation_image_size(length, tuple(layers))
                for layers in combinations(range(1, length + 1), checkpoint_count)
            ]
            assert maximum_image_size_with_checkpoint_count(
                length, checkpoint_count
            ) == max(values)
            assert minimum_image_size_with_checkpoint_count(
                length, checkpoint_count
            ) == min(values)


def test_front_loaded_schedule_attains_optional_minimum_image() -> None:
    for length in range(0, 12):
        for checkpoint_count in range(0, length + 1):
            layers = tuple(range(1, checkpoint_count + 1))
            assert selected_observation_image_size(
                length, layers
            ) == minimum_image_size_with_checkpoint_count(length, checkpoint_count)
