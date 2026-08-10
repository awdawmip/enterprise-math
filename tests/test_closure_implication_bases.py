from enterprise_math.closure_implication_bases import (
    Implication,
    basis_report,
    chain_adjacent_basis,
    chain_closure_states,
    chain_full_circuit_basis,
    forward_chaining_trace,
)


def test_rooted_circuit_can_be_globally_redundant_under_chaining():
    labels = ("a", "c", "b")
    states = chain_closure_states(labels)
    full = chain_full_circuit_basis(labels)
    reduced = (
        Implication(frozenset({"a"}), "c"),
        Implication(frozenset({"c"}), "b"),
    )
    assert basis_report(labels, states, full).complete
    report = basis_report(labels, states, reduced)
    assert report.sound and report.complete
    assert report.rule_count == 2
    assert report.worst_case_rounds == 2


def test_chain_extremes_rule_count_vs_parallel_depth():
    labels = ("x0", "x1", "x2", "x3")
    states = chain_closure_states(labels)

    adjacent = chain_adjacent_basis(labels)
    full = chain_full_circuit_basis(labels)
    adjacent_report = basis_report(labels, states, adjacent)
    full_report = basis_report(labels, states, full)

    assert adjacent_report.sound and adjacent_report.complete
    assert adjacent_report.rule_count == 3
    assert adjacent_report.worst_case_rounds == 3
    assert full_report.sound and full_report.complete
    assert full_report.rule_count == 6
    assert full_report.worst_case_rounds == 1


def test_four_node_chain_has_exact_intermediate_pareto_fixture():
    labels = ("x0", "x1", "x2", "x3")
    states = chain_closure_states(labels)
    intermediate = chain_adjacent_basis(labels) + (
        Implication(frozenset({"x0"}), "x2"),
    )
    report = basis_report(labels, states, intermediate)
    assert report.sound and report.complete
    assert (report.rule_count, report.worst_case_rounds) == (4, 2)

    # From x0 the shortcut buys one full parallel round.
    trace = forward_chaining_trace(frozenset({"x0"}), intermediate)
    assert trace == (
        frozenset({"x0"}),
        frozenset({"x0", "x1", "x2"}),
        frozenset({"x0", "x1", "x2", "x3"}),
    )
