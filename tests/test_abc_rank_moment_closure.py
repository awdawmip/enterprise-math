from math import factorial

from enterprise_math.abc_rank_moment_closure import (
    boolean_difference,
    rank_moment_from_path,
    stage110_exact_order_fixture,
)


def test_stage110_recovers_area_and_quadratic_cases() -> None:
    linear = stage110_exact_order_fixture(1)
    quadratic = stage110_exact_order_fixture(2)
    assert linear["top_interaction_order"] == 2
    assert linear["top_coefficient"] == 1
    assert quadratic["top_interaction_order"] == 3
    assert quadratic["top_coefficient"] == 2


def test_exact_top_order_for_moments_one_through_five() -> None:
    for degree in range(1, 6):
        data = stage110_exact_order_fixture(degree)
        assert data["top_interaction_order"] == degree + 1
        assert data["top_coefficient"] == factorial(degree)


def test_one_order_above_the_top_vanishes() -> None:
    # For degree d, use d+1 candidate variables plus one future selector: order d+2.
    for degree in range(1, 5):
        data = stage110_exact_order_fixture(degree + 1)
        path = data["path"]
        # Evaluate moment degree d using d+1 candidate variables on the same path.
        assert boolean_difference(
            path,
            degree,
            tuple(range(degree + 1)),
            (0,),
        ) == 0


def test_common_path_evaluates_high_degree_moment() -> None:
    data = stage110_exact_order_fixture(4)
    path = data["path"]
    assert rank_moment_from_path(path, 4, (1, 1, 1, 1), (1,)) == 4**4
