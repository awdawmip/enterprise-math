from enterprise_math.candidate_collision_inflation import (
    all_candidate_pair_collisions_are_spurious,
    candidate_excess,
    collision_coefficient,
    collision_inflation,
    pair_collision_inflation_formula,
)


def test_pair_inflation_formula_matches_direct_collision_difference() -> None:
    actual = {"a": {1, 2}, "b": {3}, "c": {4, 5}}
    candidate = {"a": {1, 2, 3}, "b": {2, 3}, "c": {3, 4, 5}}
    assert pair_collision_inflation_formula(actual, candidate) == collision_inflation(
        actual, candidate, 2
    )


def test_every_collision_order_is_monotone_under_candidate_enlargement() -> None:
    actual = {0: {0, 1}, 1: {2}, 2: {3, 4}, 3: {5}}
    candidate = {
        0: {0, 1, 2, 3},
        1: {1, 2, 3},
        2: {2, 3, 4},
        3: {3, 5},
    }
    for order in range(1, 5):
        assert collision_inflation(actual, candidate, order) >= 0


def test_strict_candidate_growth_changes_some_collision_coefficient() -> None:
    actual = {0: {0}, 1: {1}}
    candidate = {0: {0, 1}, 1: {1}}
    assert candidate_excess(actual, candidate) == {1: 1}
    assert collision_inflation(actual, candidate, 1) == 1
    assert collision_inflation(actual, candidate, 2) == 1


def test_p017_k14_root9_is_exactly_one_false_pair_collision() -> None:
    actual = {2: {9, 10}, 3: {8}}
    candidate = {2: {9, 10}, 3: {8, 9}}
    assert collision_coefficient(actual, 2) == 0
    assert collision_coefficient(candidate, 2) == 1
    assert pair_collision_inflation_formula(actual, candidate) == 1
    assert all_candidate_pair_collisions_are_spurious(actual, candidate)


def test_delta_two_creates_internal_fake_pair_even_from_empty_actual_fiber() -> None:
    actual = {0: {0}, 1: {1}}
    candidate = {0: {0, 9}, 1: {1, 9}}
    assert candidate_excess(actual, candidate)[9] == 2
    assert pair_collision_inflation_formula(actual, candidate) == 1
