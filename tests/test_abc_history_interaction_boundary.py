from fractions import Fraction

from enterprise_math.abc_history_interaction_boundary import (
    crossings_from_future_ranks,
    full_corner_matrix,
    interaction_boundary,
    reconstruct_unresolved_matrix,
)
from enterprise_math.abc_signed_exponent_transport import dyadic_difference_pressure_tower


def test_resolved_candidate_rows_are_forced_all_one() -> None:
    boundary = interaction_boundary(
        Fraction(1, 1),
        (Fraction(1, 2), Fraction(3, 4), Fraction(2, 1), Fraction(4, 1)),
        (Fraction(3, 2), Fraction(3, 1), Fraction(5, 1)),
    )
    assert boundary.resolved_candidate_count == 2
    assert boundary.unresolved_candidate_count == 2
    assert full_corner_matrix(boundary)[:2] == ((1, 1, 1), (1, 1, 1))


def test_unresolved_corner_block_is_ferrers_and_reconstructs() -> None:
    boundary = interaction_boundary(
        Fraction(1, 1),
        (Fraction(2, 1), Fraction(4, 1), Fraction(6, 1)),
        (Fraction(3, 2), Fraction(3, 1), Fraction(5, 1), Fraction(7, 1)),
    )
    assert boundary.unresolved_crossing_depths == (1, 2, 3)
    assert boundary.future_unresolved_ranks == (0, 1, 2, 3)
    assert reconstruct_unresolved_matrix(4, boundary.unresolved_crossing_depths) == boundary.unresolved_corner_matrix
    assert crossings_from_future_ranks(3, boundary.future_unresolved_ranks) == boundary.unresolved_crossing_depths


def test_interaction_state_count_collapses_raw_bits() -> None:
    boundary = interaction_boundary(
        Fraction(1, 1),
        (Fraction(2, 1), Fraction(4, 1), Fraction(6, 1), Fraction(8, 1)),
        (Fraction(3, 2), Fraction(3, 1), Fraction(5, 1), Fraction(7, 1)),
    )
    assert boundary.compatible_interaction_state_count == 70
    assert boundary.unconstrained_interaction_state_count == 65536


def test_zero_unresolved_candidates_need_no_second_order_precision() -> None:
    boundary = interaction_boundary(
        Fraction(2, 1),
        (Fraction(1, 2), Fraction(1, 1), Fraction(3, 2)),
        (Fraction(2, 1), Fraction(3, 1)),
    )
    assert boundary.unresolved_candidate_count == 0
    assert boundary.compatible_interaction_state_count == 1
    assert full_corner_matrix(boundary) == ((1, 1), (1, 1), (1, 1))


def test_arithmetic_fixture_has_only_unresolved_suffix_information() -> None:
    pressures = dyadic_difference_pressure_tower(3, 41, 2, 3).pressures
    old_max = pressures[1]
    boundary = interaction_boundary(
        old_max,
        (Fraction(1, 20), Fraction(1, 2), Fraction(1, 1), Fraction(5, 1), Fraction(11, 1)),
        pressures[2:],
    )
    assert boundary.resolved_candidate_count == 2
    assert boundary.unresolved_candidate_count == 3
    assert boundary.unresolved_crossing_depths == (0, 0, None)
    assert boundary.future_unresolved_ranks == (2, 2)
