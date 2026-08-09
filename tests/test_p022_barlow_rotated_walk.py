from itertools import product

from enterprise_math.p022_barlow_rotated_walk import (
    b2_wall_repair_count,
    coordinate_wall_departure_count,
    diagonal_wall_membership_count_before_steps,
    is_cardinal_walk,
    rotated_walk,
)
from enterprise_math.p022_barlow_two_sided_repair import (
    diagonal_split_count,
    total_zero_departure_events,
    two_sided_repair_bit_count,
    unordered_absolute_pair_history,
)


def _words(length: int):
    return tuple(tuple(word) for word in product((-1, 1), repeat=length))


def test_rotation_maps_every_microscopic_pair_to_cardinal_z2_walk() -> None:
    for length in range(0, 7):
        words = _words(length)
        for left in words:
            for right in words:
                assert is_cardinal_walk(rotated_walk(left, right))


def test_two_repair_types_equal_two_b2_wall_mechanisms() -> None:
    for length in range(0, 7):
        words = _words(length)
        for left in words:
            for right in words:
                history = unordered_absolute_pair_history(left, right)
                path = rotated_walk(left, right)
                assert diagonal_wall_membership_count_before_steps(path) == total_zero_departure_events(history)
                assert coordinate_wall_departure_count(path) == diagonal_split_count(history)
                assert b2_wall_repair_count(path) == two_sided_repair_bit_count(history)


def test_origin_counts_two_diagonal_reflections_but_no_coordinate_departure() -> None:
    path = rotated_walk((1,), (1,))
    assert path == ((1, 0),)
    assert diagonal_wall_membership_count_before_steps(path) == 2
    assert coordinate_wall_departure_count(path) == 0
    assert b2_wall_repair_count(path) == 2


def test_axis_departure_is_exactly_side_label_release() -> None:
    # First step reaches the U-axis; second step leaves it into the chamber.
    path = rotated_walk((1, 1), (1, -1))
    assert path == ((1, 0), (1, 1))
    assert coordinate_wall_departure_count(path) == 1
