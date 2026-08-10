from math import comb

from enterprise_math.chain_implication_extremes import chain_basis_extremes
from enterprise_math.closure_implication_bases import (
    Implication,
    basis_report,
    chain_adjacent_basis,
    chain_closure_states,
)


def test_chain_resource_endpoints_scale_exactly():
    for label_count in range(1, 8):
        labels = tuple(f"x{i}" for i in range(label_count))
        report = chain_basis_extremes(labels)
        n = label_count - 1
        assert report.minimum_rule_count == n
        assert report.minimum_rule_depth == n
        assert report.one_round_rule_count == comb(n + 1, 2)
        assert report.one_round_depth == (0 if n == 0 else 1)
        assert report.adjacent_complete and report.full_complete


def test_adjacent_basis_is_the_minimum_rule_fixture():
    labels = ("x0", "x1", "x2", "x3", "x4")
    states = chain_closure_states(labels)
    adjacent = chain_adjacent_basis(labels)
    report = basis_report(labels, states, adjacent)
    assert report.rule_count == 4
    assert report.worst_case_rounds == 4


def test_wrong_four_rule_chain_basis_is_not_complete():
    labels = ("x0", "x1", "x2", "x3", "x4")
    states = chain_closure_states(labels)
    # Give every non-initial root one rule, but replace the mandatory adjacent
    # x2->x3 edge by a shortcut that cannot fire from seed {x2}.
    wrong = (
        Implication(frozenset({"x0"}), "x1"),
        Implication(frozenset({"x1"}), "x2"),
        Implication(frozenset({"x1"}), "x3"),
        Implication(frozenset({"x3"}), "x4"),
    )
    report = basis_report(labels, states, wrong)
    assert report.sound
    assert not report.complete
