from fractions import Fraction
from itertools import product

from enterprise_math.abc_finite_history_closure import (
    exact_history_area,
    finite_history_signature,
    history_area_from_signature,
    multilinear_area,
    recover_coordinate_from_history_areas,
    verify_all_histories,
)
from enterprise_math.abc_signed_exponent_transport import dyadic_difference_pressure_tower


def test_all_finite_histories_close_at_second_order() -> None:
    thresholds = (Fraction(1, 4), Fraction(1, 1))
    values = (Fraction(1, 2), Fraction(3, 2))
    candidates = (Fraction(3, 4), Fraction(2, 1))
    futures = (Fraction(2, 1), Fraction(3, 1))
    assert verify_all_histories(thresholds, values, candidates, futures)


def test_exact_formula_matches_direct_area() -> None:
    thresholds = (Fraction(1, 4), Fraction(1, 1))
    values = (Fraction(1, 2), Fraction(3, 2))
    candidates = (Fraction(3, 4), Fraction(2, 1), Fraction(5, 2))
    futures = (Fraction(2, 1), Fraction(3, 1))
    exact = exact_history_area(
        thresholds,
        values,
        candidates,
        futures,
        selected_threshold_indices=(0, 2),
        future_prefix_length=2,
    )
    signature = finite_history_signature(thresholds, values, candidates, futures)
    assert exact == history_area_from_signature(signature, (0, 2), 2)


def test_response_coordinates_are_recoverable_from_history_areas() -> None:
    signature = finite_history_signature(
        (Fraction(1, 4), Fraction(1, 1)),
        (Fraction(1, 2), Fraction(3, 2)),
        (Fraction(3, 4), Fraction(2, 1)),
        (Fraction(2, 1), Fraction(3, 1)),
    )
    recovered = recover_coordinate_from_history_areas(signature, 0, 0)
    assert recovered["threshold_span"] == signature.threshold_spans[0]
    assert recovered["future_node_rank"] == signature.future_node_ranks[0]
    assert recovered["mixed_corner"] == signature.mixed_corners[0][0]


def test_arithmetic_dyadic_envelope_closes() -> None:
    pressures = dyadic_difference_pressure_tower(3, 41, 2, 3).pressures
    current = pressures[:2]
    futures = pressures[2:]
    thresholds = (Fraction(1, 25), Fraction(1, 2))
    candidates = (Fraction(11, 20), Fraction(1, 1), Fraction(11, 1))
    assert verify_all_histories(thresholds, current, candidates, futures)


def test_no_irreducible_third_order_threshold_threshold_node_term() -> None:
    signature = finite_history_signature(
        (Fraction(1, 4),),
        (Fraction(1, 2), Fraction(3, 2)),
        (Fraction(3, 4), Fraction(5, 4)),
        (Fraction(2, 1),),
    )

    # Third Boolean finite difference in x0, x1, y0.
    total = 0
    for x0, x1, y0 in product((0, 1), repeat=3):
        sign = -1 if (3 - (x0 + x1 + y0)) % 2 else 1
        total += sign * multilinear_area(signature, (x0, x1), (y0,))
    assert total == 0


def test_no_irreducible_third_order_threshold_node_node_term() -> None:
    signature = finite_history_signature(
        (Fraction(1, 4),),
        (Fraction(1, 2),),
        (Fraction(3, 4),),
        (Fraction(1, 1), Fraction(2, 1)),
    )

    total = 0
    for x0, y0, y1 in product((0, 1), repeat=3):
        sign = -1 if (3 - (x0 + y0 + y1)) % 2 else 1
        total += sign * multilinear_area(signature, (x0,), (y0, y1))
    assert total == 0
