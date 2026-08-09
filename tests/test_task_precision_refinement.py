from itertools import product

from enterprise_math.task_precision_refinement import (
    class_count,
    combined_partition,
    local_split_multiplicities,
    minimal_repair_alphabet_size,
    minimal_repair_code,
    realized_class_tuples,
    refines,
    repair_chain_bound,
    repaired_partition,
    same_partition,
    task_partition,
)


def test_task_union_is_common_refinement() -> None:
    states = tuple(range(6))
    q1 = {state: state // 3 for state in states}
    q2 = {state: state % 2 for state in states}

    left = task_partition(states, {"q1": q1})
    right = task_partition(states, {"q2": q2})
    union = task_partition(states, {"q1": q1, "q2": q2})
    combined = combined_partition(states, left, right)

    assert same_partition(states, union, combined)
    assert refines(states, union, left)
    assert refines(states, union, right)


def test_realized_tuple_count_can_be_strictly_below_cartesian_product() -> None:
    states = tuple(range(4))
    first = {0: "A", 1: "A", 2: "B", 3: "B"}
    second = {0: "X", 1: "Y", 2: "Y", 3: "Z"}

    tuples = realized_class_tuples(states, first, second)
    combined = combined_partition(states, first, second)

    assert tuples == frozenset(
        {("A", "X"), ("A", "Y"), ("B", "Y"), ("B", "Z")}
    )
    assert class_count(first) == 2
    assert class_count(second) == 3
    assert class_count(combined) == 4
    assert class_count(combined) < class_count(first) * class_count(second)


def test_minimal_repair_alphabet_is_maximum_local_split() -> None:
    states = tuple(range(6))
    coarse = {0: "A", 1: "A", 2: "A", 3: "B", 4: "B", 5: "B"}
    fine = {0: "a0", 1: "a1", 2: "a2", 3: "b0", 4: "b0", 5: "b1"}

    assert local_split_multiplicities(states, fine, coarse) == {"A": 3, "B": 2}
    assert minimal_repair_alphabet_size(states, fine, coarse) == 3

    repair = minimal_repair_code(states, fine, coarse)
    assert set(repair.values()) == {0, 1, 2}
    assert same_partition(states, repaired_partition(states, coarse, repair), fine)


def test_smaller_repair_alphabet_cannot_realize_target_partition() -> None:
    states = (0, 1, 2)
    coarse = {state: 0 for state in states}
    fine = {state: state for state in states}
    assert minimal_repair_alphabet_size(states, fine, coarse) == 3

    for values in product(range(2), repeat=len(states)):
        repair = dict(zip(states, values, strict=True))
        assert not same_partition(
            states, repaired_partition(states, coarse, repair), fine
        )


def test_repair_chain_cost_is_submultiplicative() -> None:
    states = tuple(range(12))
    coarse = {state: state // 6 for state in states}
    middle = {state: (state // 6, (state % 6) // 2) for state in states}
    fine = {state: state for state in states}

    first, second, direct = repair_chain_bound(states, fine, middle, coarse)
    assert first == 3
    assert second == 2
    assert direct == 6
    assert direct == first * second


def test_repair_chain_bound_can_be_strict() -> None:
    states = (0, 1, 2, 3, 4)
    coarse = {state: 0 for state in states}
    middle = {0: "a", 1: "a", 2: "a", 3: "b", 4: "b"}
    fine = {0: 0, 1: 1, 2: 2, 3: 3, 4: 3}

    first, second, direct = repair_chain_bound(states, fine, middle, coarse)
    assert (first, second, direct) == (2, 3, 4)
    assert direct < first * second
