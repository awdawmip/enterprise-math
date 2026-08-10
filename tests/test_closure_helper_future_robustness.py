from itertools import combinations

from enterprise_math.closure_helper_future_robustness import (
    helper_robustness_report,
    prefix_validity_holds,
)
from enterprise_math.closure_synergy_depth import synergy_chain


def powerset(items):
    items = tuple(items)
    return tuple(
        frozenset(subset)
        for size in range(len(items) + 1)
        for subset in combinations(items, size)
    )


def test_stale_helper_can_be_currently_harmless_but_future_unsafe():
    state = frozenset({"e2"})
    report = helper_robustness_report(4, state)
    assert report.current_projection_correct
    assert not report.prefix_validity
    assert not report.future_robust_under_raw_additions
    assert report.violating_addition is not None
    assert {"a3", "a4"}.issubset(report.violating_addition)


def test_prefix_valid_helpers_are_robust_under_all_raw_additions():
    state = frozenset({"a1", "a2", "e2"})
    report = helper_robustness_report(4, state)
    assert report.prefix_validity
    assert report.future_robust_under_raw_additions


def test_raw_true_output_makes_stale_helpers_raw_endpoint_invisible():
    state = frozenset({"z", "e2"})
    report = helper_robustness_report(4, state)
    assert not report.prefix_validity
    assert report.future_robust_under_raw_additions


def test_robustness_iff_output_true_or_prefix_validity_exhaustively_small():
    for arity in (3, 4):
        compiled = synergy_chain(arity)
        for state in powerset(compiled.labels):
            report = helper_robustness_report(arity, state)
            assert report.future_robust_under_raw_additions == (
                "z" in report.raw_projection or prefix_validity_holds(arity, state)
            )
