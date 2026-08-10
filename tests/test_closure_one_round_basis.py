from enterprise_math.closure_implication_bases import (
    Implication,
    basis_report,
    chain_closure_states,
)
from enterprise_math.closure_one_round_basis import (
    full_circuit_one_round_report,
    missing_rooted_circuits,
    rooted_circuit_basis,
)


def test_full_circuit_table_is_one_round_complete():
    labels = ("a", "b", "c")
    omega = (frozenset({"a"}), frozenset({"b"}), frozenset({"a", "b", "c"}))
    report = full_circuit_one_round_report(labels, omega)
    assert report.rule_count == 3
    assert report.worst_case_rounds == 1


def test_deleting_any_chain_circuit_loses_one_round_closure_for_its_premise():
    labels = ("a", "c", "b")
    omega = chain_closure_states(labels)
    full = rooted_circuit_basis(labels, omega)
    assert len(full) == 3

    for deleted in full:
        reduced = tuple(rule for rule in full if rule != deleted)
        assert missing_rooted_circuits(labels, omega, reduced)
        report = basis_report(labels, omega, reduced)
        # Deleting the transitive a->b circuit preserves eventual closure, but
        # cannot preserve the one-round bound. Deleting an adjacent circuit may
        # even destroy completeness.
        assert (not report.complete) or report.worst_case_rounds != 1


def test_transitive_circuit_is_optional_only_when_more_than_one_round_is_allowed():
    labels = ("a", "c", "b")
    omega = chain_closure_states(labels)
    iterative = (
        Implication(frozenset({"a"}), "c"),
        Implication(frozenset({"c"}), "b"),
    )
    report = basis_report(labels, omega, iterative)
    assert report.complete
    assert report.worst_case_rounds == 2
    assert len(missing_rooted_circuits(labels, omega, iterative)) == 1
