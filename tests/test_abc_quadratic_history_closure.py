from fractions import Fraction
from itertools import product

from enterprise_math.abc_quadratic_history_closure import (
    direct_quadratic_energy,
    evaluate_quadratic_energy_jet,
    quadratic_energy_jet,
    stage108_arithmetic_cubic_fixture,
    third_boolean_difference_two_thresholds_one_future,
)


def test_quadratic_energy_jet_matches_direct_recomputation() -> None:
    thresholds = (Fraction(1, 4), Fraction(1, 1))
    values = (Fraction(1, 2), Fraction(3, 2))
    candidates = (Fraction(3, 4), Fraction(2, 1))
    futures = (Fraction(2, 1), Fraction(3, 1))
    jet = quadratic_energy_jet(thresholds, values, candidates, futures)
    for x in product((0, 1), repeat=2):
        for y in product((0, 1), repeat=2):
            assert evaluate_quadratic_energy_jet(jet, x, y) == direct_quadratic_energy(
                thresholds, values, candidates, futures, x, y
            )


def test_arithmetic_fixture_has_genuine_third_order_interaction() -> None:
    data = stage108_arithmetic_cubic_fixture()
    jet = data["jet"]
    assert data["pressures"] == (Fraction(1, 22), Fraction(13, 22))
    assert data["third_difference"] == 2
    assert third_boolean_difference_two_thresholds_one_future(jet, 0, 1, 0) == 2


def test_cubic_coefficient_vanishes_if_future_crosses_only_one_candidate() -> None:
    jet = quadratic_energy_jet(
        (),
        (Fraction(1, 1),),
        (Fraction(2, 1), Fraction(4, 1)),
        (Fraction(3, 1),),
    )
    assert third_boolean_difference_two_thresholds_one_future(jet, 0, 1, 0) == 0


def test_no_fourth_order_term_for_quadratic_energy() -> None:
    jet = quadratic_energy_jet(
        (),
        (Fraction(1, 1),),
        (Fraction(2, 1), Fraction(3, 1), Fraction(4, 1)),
        (Fraction(5, 1),),
    )
    # Fourth difference in x0,x1,x2,y0 must vanish because the polynomial degree is <=3.
    total = 0
    for x0, x1, x2, y0 in product((0, 1), repeat=4):
        sign = -1 if (4 - (x0 + x1 + x2 + y0)) % 2 else 1
        total += sign * evaluate_quadratic_energy_jet(jet, (x0, x1, x2), (y0,))
    assert total == 0
