from enterprise_math.closure_arity_duality import (
    boolean_identity_states,
    closure_arity_report,
    closure_generator_horizon,
)
from enterprise_math.closure_implication_circuits import maximum_circuit_arity


def test_identity_closure_has_large_query_arity_and_zero_law_arity():
    labels = ("a", "b", "c", "d")
    omega = boolean_identity_states(labels)
    report = closure_arity_report(labels, omega)
    assert report.query_generator_horizon == 4
    assert report.direct_circuit_horizon == 0
    assert report.closed_class_count == 16


def test_higher_order_fixture_has_law_arity_larger_than_query_arity():
    labels = ("a", "b", "c")
    omega = (frozenset({"a"}), frozenset({"b"}), frozenset({"a", "b", "c"}))
    report = closure_arity_report(labels, omega)
    assert report.query_generator_horizon == 1
    assert report.direct_circuit_horizon == 2
    assert report.closed_class_count == 4


def test_no_general_ordering_between_the_two_horizons():
    labels_identity = ("u", "v", "w")
    identity = boolean_identity_states(labels_identity)
    assert closure_generator_horizon(labels_identity, identity) == 3
    assert maximum_circuit_arity(labels_identity, identity) == 0

    labels_higher = ("a", "b", "c")
    higher = (frozenset({"a"}), frozenset({"b"}), frozenset({"a", "b", "c"}))
    assert closure_generator_horizon(labels_higher, higher) == 1
    assert maximum_circuit_arity(labels_higher, higher) == 2
