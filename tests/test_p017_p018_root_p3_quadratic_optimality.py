from fractions import Fraction

from enterprise_math.p017_p018_root_p3_quadratic_optimality import (
    feasible_quadratic_weight,
    fourth_root_log2_margin,
    local_main_coefficient,
    optimal_quadratic_weight,
    quadratic_weight_values,
)


def test_generation4_weight_is_pointwise_feasible_and_has_expected_values():
    A, B = optimal_quadratic_weight()
    assert (A, B) == (Fraction(1), Fraction(2, 3))
    assert feasible_quadratic_weight(A, B) is True
    assert quadratic_weight_values(A, B) == (
        Fraction(1), Fraction(0), Fraction(-1, 3), Fraction(0)
    )


def test_nearby_feasible_vertices_do_not_beat_optimum_for_lambda_below_two():
    A, B = optimal_quadratic_weight()
    for lam in (0.2, 0.5, 0.6931471805599453, 1.0, 1.5, 1.9):
        optimum = local_main_coefficient(lam, A, B)
        candidates = (
            (Fraction(1), Fraction(0)),
            (Fraction(1), Fraction(1, 2)),
            (Fraction(4, 3), Fraction(1)),
            (Fraction(3, 2), Fraction(7, 6)),
            (Fraction(2), Fraction(5, 3)),
        )
        for a, b in candidates:
            if feasible_quadratic_weight(a, b):
                assert local_main_coefficient(lam, a, b) <= optimum + 1e-15


def test_log2_pair_overlap_gain_is_strictly_positive():
    data = fourth_root_log2_margin()
    assert data["optimal_quadratic_margin"] > data["first_order_margin"] > 0
    assert 0.466 < data["optimal_quadratic_margin"] < 0.468
