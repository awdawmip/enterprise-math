from enterprise_math.closure_async_fairness import (
    fairness_liveness_profile,
    fairness_quotient_counts,
)
from enterprise_math.closure_async_progress_poset import helper_ideals


def test_every_legal_ideal_may_complete_and_weak_fair_must_complete():
    for arity in range(4, 9):
        for ideal in helper_ideals(arity):
            profile = fairness_liveness_profile(arity, ideal)
            assert profile.may_complete
            assert profile.must_complete_under_weak_fairness
            assert profile.enabled_nonempty_if_nonterminal


def test_unrestricted_stutter_breaks_must_completion_exactly_off_terminal():
    for arity in range(4, 8):
        ideals = tuple(helper_ideals(arity))
        helper_count = fairness_liveness_profile(arity, ideals[-1]).helper_count
        for ideal in ideals:
            profile = fairness_liveness_profile(arity, ideal)
            assert profile.must_complete_unrestricted_with_stutter == (len(ideal) == helper_count)
            assert (profile.unrestricted_counterexample_kind is None) == profile.terminal


def test_completion_future_quotient_counts_change_with_scheduler_contract():
    for arity in range(4, 8):
        counts = fairness_quotient_counts(arity)
        assert counts == {
            "may_complete_classes": 1,
            "must_unrestricted_classes": 2,
            "must_weak_fair_classes": 1,
        }


def test_four_way_empty_ideal_is_may_yes_must_no_without_fairness():
    profile = fairness_liveness_profile(4, frozenset())
    assert profile.may_complete
    assert not profile.must_complete_unrestricted_with_stutter
    assert profile.must_complete_under_weak_fairness
    assert profile.unrestricted_counterexample_kind == "infinite_stutter"
