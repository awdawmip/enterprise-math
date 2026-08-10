from itertools import chain, combinations

from enterprise_math.closure_implication_circuits import (
    RootedCircuit,
    circuit_arity_spectrum,
    closure_is_unary_generated,
    closure_of,
    maximum_circuit_arity,
    one_round_circuit_closure,
    rooted_circuits,
)


def powerset(items):
    items = tuple(items)
    return tuple(
        frozenset(subset)
        for size in range(len(items) + 1)
        for subset in combinations(items, size)
    )


def test_higher_order_fixture_has_exact_binary_circuit():
    labels = ("a", "b", "c")
    omega = (frozenset({"a"}), frozenset({"b"}), frozenset({"a", "b", "c"}))
    circuits = set(rooted_circuits(labels, omega))

    assert RootedCircuit(frozenset({"a", "b"}), "c") in circuits
    assert RootedCircuit(frozenset({"c"}), "a") in circuits
    assert RootedCircuit(frozenset({"c"}), "b") in circuits
    assert maximum_circuit_arity(labels, omega) == 2
    assert circuit_arity_spectrum(labels, omega) == {1: 2, 2: 1}
    assert not closure_is_unary_generated(labels, omega)


def test_full_rooted_circuit_table_recovers_closure_in_one_round():
    labels = ("a", "b", "c")
    omega = (frozenset({"a"}), frozenset({"b"}), frozenset({"a", "b", "c"}))
    for seed in powerset(labels):
        assert one_round_circuit_closure(labels, omega, seed) == closure_of(labels, omega, seed)


def test_unary_chain_fixture_is_unary_generated_but_has_transitive_rooted_circuit():
    labels = ("a", "c", "b")
    omega = (
        frozenset(),
        frozenset({"b"}),
        frozenset({"b", "c"}),
        frozenset({"a", "b", "c"}),
    )
    circuits = set(rooted_circuits(labels, omega))
    assert circuits == {
        RootedCircuit(frozenset({"a"}), "c"),
        RootedCircuit(frozenset({"a"}), "b"),
        RootedCircuit(frozenset({"c"}), "b"),
    }
    assert closure_is_unary_generated(labels, omega)
    assert maximum_circuit_arity(labels, omega) == 1
