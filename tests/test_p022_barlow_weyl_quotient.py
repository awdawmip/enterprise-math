from itertools import product

from enterprise_math.p022_barlow_two_sided_repair import (
    unordered_absolute_pair_history,
)
from enterprise_math.p022_barlow_weyl_quotient import (
    b2_orbit,
    b2_orbit_size_from_chamber,
    canonical_b2_orbit_representative,
    chamber_path_from_labelled,
    compare_with_existing_repair_theorem,
    labelled_prefix_path,
    path_wall_event_counts,
    quotient_path_lift_count,
)


def _words(length: int):
    return tuple(tuple(word) for word in product((-1, 1), repeat=length))


def test_orbit_representative_classifies_signed_permutation_orbits() -> None:
    samples = (
        (0, 0),
        (0, 3),
        (2, 2),
        (2, 5),
        (-2, 5),
        (-5, -2),
    )
    for state in samples:
        representative = canonical_b2_orbit_representative(state)
        orbit = b2_orbit(state)
        assert all(
            canonical_b2_orbit_representative(member) == representative
            for member in orbit
        )
        assert len(orbit) == b2_orbit_size_from_chamber(representative)


def test_expected_orbit_sizes_on_origin_walls_and_interior() -> None:
    assert b2_orbit_size_from_chamber((0, 0)) == 1
    assert b2_orbit_size_from_chamber((0, 4)) == 4
    assert b2_orbit_size_from_chamber((3, 3)) == 4
    assert b2_orbit_size_from_chamber((2, 5)) == 8


def test_coordination_history_is_exactly_time_labelled_b2_orbit_quotient() -> None:
    for length in range(0, 7):
        words = _words(length)
        for left in words:
            for right in words:
                labelled = labelled_prefix_path(left, right)
                chamber = chamber_path_from_labelled(labelled)
                assert chamber == unordered_absolute_pair_history(left, right)


def test_weyl_wall_event_counts_match_existing_repair_counts() -> None:
    for length in range(0, 8):
        words = _words(length)
        histories = {
            unordered_absolute_pair_history(left, right)
            for left in words
            for right in words
        }
        for history in histories:
            lift, existing = compare_with_existing_repair_theorem(history)
            assert lift == existing
            assert lift == quotient_path_lift_count(history)


def test_first_step_releases_two_sign_reflections_but_no_swap_bit() -> None:
    history = ((1, 1),)
    orientation, split = path_wall_event_counts(history)
    assert orientation == 2
    assert split == 0
    assert quotient_path_lift_count(history) == 4


def test_coordinate_wall_exit_releases_one_orientation_bit() -> None:
    # (1,1)->(0,2)->(1,3): at the last transition the zero coordinate leaves
    # the coordinate wall while the pair remains off the diagonal.
    history = ((1, 1), (0, 2), (1, 3))
    orientation, split = path_wall_event_counts(history)
    assert orientation == 3
    assert split == 1
    assert quotient_path_lift_count(history) == 16


def test_diagonal_split_releases_one_side_label_bit() -> None:
    history = ((1, 1), (0, 2))
    orientation, split = path_wall_event_counts(history)
    assert orientation == 2
    assert split == 1
    assert quotient_path_lift_count(history) == 8


def test_terminal_orbit_size_does_not_bound_history_lift_multiplicity() -> None:
    # Repeated wall resets can create many labelled history lifts even though a
    # single terminal B2 orbit has size at most eight.
    history = (
        (1, 1),
        (0, 0),
        (1, 1),
        (0, 0),
        (1, 1),
    )
    assert b2_orbit_size_from_chamber(history[-1]) == 4
    assert quotient_path_lift_count(history) == 64
