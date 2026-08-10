from enterprise_math.poset_witness_count_zeta import (
    count_required_labels,
    counts_by_ideal,
    invert_upper_counts,
    witness_count_transform,
)


def antichain_poset(n: int):
    elements = tuple(range(n))
    leq = frozenset((x, x) for x in elements)
    return elements, leq


def test_zeta_transform_inverts_exact_witness_multiplicities():
    elements, leq = antichain_poset(3)
    multiplicities = {
        frozenset(): 2,
        frozenset({0}): 3,
        frozenset({1, 2}): 4,
        frozenset({0, 1, 2}): 5,
    }
    transform = witness_count_transform(elements, leq, multiplicities)
    recovered = invert_upper_counts(elements, leq, counts_by_ideal(transform))
    expected = {ideal: 0 for ideal in transform.ideals}
    expected.update(multiplicities)
    assert recovered == expected


def test_raw_count_query_depends_only_on_maximal_antichain_normal_form():
    elements = (0, 1, 2, 3)
    leq = frozenset((i, j) for i in elements for j in elements if i <= j)
    multiplicities = {
        frozenset(): 1,
        frozenset({0, 1}): 2,
        frozenset({0, 1, 2, 3}): 7,
    }
    assert count_required_labels(
        elements, leq, multiplicities, frozenset({0, 1, 3})
    ) == count_required_labels(elements, leq, multiplicities, frozenset({3})) == 7


def test_boolean_family_is_recovered_as_zero_one_multiplicity_vector():
    elements, leq = antichain_poset(2)
    family = {
        frozenset({0}): 1,
        frozenset({1}): 1,
    }
    transform = witness_count_transform(elements, leq, family)
    recovered = invert_upper_counts(elements, leq, counts_by_ideal(transform))
    assert {ideal for ideal, multiplicity in recovered.items() if multiplicity} == set(family)
    assert all(value in (0, 1) for value in recovered.values())


def test_empty_query_is_total_witness_count():
    elements, leq = antichain_poset(2)
    multiplicities = {
        frozenset(): 2,
        frozenset({0}): 3,
        frozenset({0, 1}): 5,
    }
    transform = witness_count_transform(elements, leq, multiplicities)
    assert count_required_labels(elements, leq, multiplicities, frozenset()) == 10
    assert transform.total_witness_multiplicity == 10
