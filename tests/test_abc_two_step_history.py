from fractions import Fraction

from enterprise_math.abc_two_step_history import (
    mixed_two_step_response,
    one_step_area_signature,
    stage101_mixed_collision,
    stage101_two_node_collision,
    two_node_response,
    two_threshold_final_area,
)


def test_mixed_two_step_requires_corner_bit() -> None:
    data = stage101_mixed_collision()
    signature = data["shared_one_step_signature"]
    assert signature.area == 1
    assert signature.candidate_first_depth is None
    assert signature.next_node_rank == 1
    assert data["flat_response"].corner_bit == 0
    assert data["jump_response"].corner_bit == 1
    assert data["flat_response"].final_area == 2
    assert data["jump_response"].final_area == 3


def test_two_node_history_requires_second_rank() -> None:
    data = stage101_two_node_collision()
    assert data["shared_one_step_signature"] == (0, 0)
    assert data["flat_response"].second_node_rank == 0
    assert data["jump_response"].second_node_rank == 1
    assert data["flat_response"].final_area == 0
    assert data["jump_response"].final_area == 1


def test_threshold_threshold_history_is_additive() -> None:
    thresholds = (Fraction(1, 5),)
    values = (Fraction(1, 4), Fraction(3, 4), Fraction(2, 1))
    final_area = two_threshold_final_area(
        thresholds,
        values,
        Fraction(1, 2),
        Fraction(3, 2),
    )
    assert final_area == 6


def test_mixed_formula_is_order_independent() -> None:
    thresholds = (Fraction(1, 4), Fraction(1, 1))
    values = (Fraction(1, 2), Fraction(3, 2))
    response = mixed_two_step_response(
        thresholds,
        values,
        Fraction(3, 4),
        Fraction(2, 1),
    )
    assert response.area == 3
    assert response.threshold_span == 1
    assert response.next_node_rank == 2
    assert response.corner_bit == 1
    assert response.final_area == 7


def test_finite_candidate_already_crossed_forces_mixed_corner() -> None:
    thresholds = (Fraction(1, 10),)
    values = (Fraction(1, 2),)
    candidate = Fraction(2, 5)
    next_value = Fraction(3, 5)
    signature = one_step_area_signature(thresholds, values, candidate, next_value)
    response = mixed_two_step_response(thresholds, values, candidate, next_value)
    assert signature.candidate_first_depth == 0
    assert response.corner_bit == 1


def test_two_node_response_adds_ranks() -> None:
    response = two_node_response(
        (Fraction(1, 2), Fraction(1, 1), Fraction(2, 1)),
        (Fraction(1, 4),),
        Fraction(3, 4),
        Fraction(3, 1),
    )
    assert response.area == 0
    assert response.first_node_rank == 1
    assert response.second_node_rank == 3
    assert response.final_area == 4
