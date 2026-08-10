from itertools import product

from enterprise_math.safe_operation_algebra import (
    addition_unit_obstruction,
    all_represented_basins_are_singletons,
    safe_operation_count,
    safe_operation_count_from_fiber_sizes,
    translation_safe_on_periodic_width_sample,
    uniform_safe_operation_count,
)


def _preserves_partition(operation, labels):
    n = len(labels)
    return all(
        labels[i] != labels[j] or labels[operation[i]] == labels[operation[j]]
        for i in range(n)
        for j in range(n)
    )


def test_safe_unary_count_matches_exhaustive_partition_preservers():
    labels = (0, 0, 1)
    operations = tuple(product(range(3), repeat=3))
    exhaustive = sum(_preserves_partition(operation, labels) for operation in operations)
    assert exhaustive == 15
    assert safe_operation_count_from_fiber_sizes((2, 1), 1) == exhaustive
    assert safe_operation_count(range(3), {0: 0, 1: 0, 2: 1}, 1) == exhaustive


def test_uniform_closed_form_matches_general_formula():
    for classes in (1, 2, 3):
        for size in (1, 2, 3):
            for arity in (1, 2, 3):
                assert uniform_safe_operation_count(
                    classes, size, arity
                ) == safe_operation_count_from_fiber_sizes(
                    (size,) * classes, arity
                )


def test_binary_addition_unit_obstruction_is_local_and_exact():
    # V(k)=5k: representative-level addition can be coherent, but full fibers
    # already fail under the fixed second input 1.
    assert addition_unit_obstruction((0, 5, 10)) == (0, 0, 4, 1)
    assert not all_represented_basins_are_singletons((0, 5, 10))
    assert addition_unit_obstruction((0, 1, 2, 3, 4)) is None
    assert all_represented_basins_are_singletons((0, 1, 2, 3, 4))


def test_translation_spectrum_does_not_identify_periodic_basin_geometry():
    # Uniform width 3 and primitive periodic width word (1,2) have the same
    # sampled safe-translation spectrum: multiples of total period capacity 3.
    for increment in range(10):
        uniform = translation_safe_on_periodic_width_sample((3,), increment)
        alternating = translation_safe_on_periodic_width_sample((1, 2), increment)
        assert uniform == alternating
        assert uniform == (increment % 3 == 0)


def _binary_operation_preserves_partition(table, labels):
    n = len(labels)

    def op(a, b):
        return table[a * n + b]

    return all(
        labels[a] != labels[a2]
        or labels[b] != labels[b2]
        or labels[op(a, b)] == labels[op(a2, b2)]
        for a in range(n)
        for a2 in range(n)
        for b in range(n)
        for b2 in range(n)
    )


def test_safe_binary_count_matches_exhaustive_partition_preservers():
    labels = (0, 0, 1)
    exhaustive = sum(
        _binary_operation_preserves_partition(table, labels)
        for table in product(range(3), repeat=9)
    )
    assert exhaustive == 1275
    assert safe_operation_count_from_fiber_sizes((2, 1), 2) == exhaustive


def _restricted_growth_partitions(n):
    result = []

    def visit(index, labels, maximum):
        if index == n:
            result.append(tuple(labels))
            return
        for label in range(maximum + 2):
            labels.append(label)
            visit(index + 1, labels, max(maximum, label))
            labels.pop()

    visit(1, [0], 0)
    return tuple(result)


def _equivalence_preserved_by_map(equivalence, operation):
    n = len(equivalence)
    return all(
        equivalence[i] != equivalence[j]
        or equivalence[operation[i]] == equivalence[operation[j]]
        for i in range(n)
        for j in range(n)
    )


def test_full_safe_unary_monoid_recovers_nontrivial_partition_on_small_examples():
    for labels in ((0, 0, 1), (0, 0, 1, 1), (0, 1, 1, 2)):
        n = len(labels)
        safe_maps = tuple(
            operation
            for operation in product(range(n), repeat=n)
            if _preserves_partition(operation, labels)
        )
        invariant_equivalences = tuple(
            equivalence
            for equivalence in _restricted_growth_partitions(n)
            if all(
                _equivalence_preserved_by_map(equivalence, operation)
                for operation in safe_maps
            )
        )
        equality = tuple(range(n))
        universal = (0,) * n
        assert set(invariant_equivalences) == {equality, labels, universal}
