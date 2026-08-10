"""Liveness/fairness boundary for asynchronous helper progress.

For a finite helper-dependency poset, legal progress states are order ideals.
From every ideal a completion schedule exists.  If the scheduler may stutter
forever, nonterminal states do not guarantee completion.  Under weak fairness
(every continuously enabled helper is eventually fired), every ideal does
complete because a minimal helper in the complement stays enabled until firing.

The liveness statements are classical finite-transition/concurrency facts.  The
module packages them as a P025 future-contract pressure test.
"""

from __future__ import annotations

from dataclasses import dataclass

from .balanced_binary_synergy import balanced_binary_synergy
from .closure_async_progress_poset import helper_ideals
from .closure_async_query_ladder import enabled_helpers


@dataclass(frozen=True)
class FairnessLivenessProfile:
    arity: int
    completed: frozenset[str]
    helper_count: int
    remaining_helpers: int
    terminal: bool
    enabled_nonempty_if_nonterminal: bool
    may_complete: bool
    must_complete_unrestricted_with_stutter: bool
    must_complete_under_weak_fairness: bool
    unrestricted_counterexample_kind: str | None


def fairness_liveness_profile(arity: int, completed: frozenset[str]) -> FairnessLivenessProfile:
    if isinstance(arity, bool) or not isinstance(arity, int) or arity < 4:
        raise ValueError("arity must be an integer >= 4")
    compiler = balanced_binary_synergy(arity)
    ideals = set(helper_ideals(arity))
    if completed not in ideals:
        raise ValueError("completed helper set must be a legal ideal")
    m = len(compiler.helpers)
    terminal = len(completed) == m
    enabled = enabled_helpers(arity, completed)
    enabled_condition = terminal or bool(enabled)
    if not enabled_condition:
        raise AssertionError("every nonterminal finite-poset ideal has an enabled minimal complement element")

    # Existential completion is witnessed by repeatedly choosing enabled helpers.
    may_complete = True

    # If stutter/no-op is a legal scheduler move with no fairness requirement,
    # any nonterminal state admits the infinite all-stutter execution.
    must_unrestricted = terminal

    # Structural theorem: in a finite monotone poset process, choose a minimal
    # helper outside the ideal. It is enabled and remains continuously enabled
    # until fired. Weak fairness eventually fires it. Induct on remaining count.
    must_weak_fair = True

    return FairnessLivenessProfile(
        arity=arity,
        completed=completed,
        helper_count=m,
        remaining_helpers=m - len(completed),
        terminal=terminal,
        enabled_nonempty_if_nonterminal=enabled_condition,
        may_complete=may_complete,
        must_complete_unrestricted_with_stutter=must_unrestricted,
        must_complete_under_weak_fairness=must_weak_fair,
        unrestricted_counterexample_kind=None if terminal else "infinite_stutter",
    )


def fairness_quotient_counts(arity: int) -> dict[str, int]:
    """Class counts for three coarse completion futures over all legal ideals."""
    ideals = tuple(helper_ideals(arity))
    may_values = {fairness_liveness_profile(arity, ideal).may_complete for ideal in ideals}
    unrestricted_values = {
        fairness_liveness_profile(arity, ideal).must_complete_unrestricted_with_stutter
        for ideal in ideals
    }
    weak_fair_values = {
        fairness_liveness_profile(arity, ideal).must_complete_under_weak_fairness
        for ideal in ideals
    }
    return {
        "may_complete_classes": len(may_values),
        "must_unrestricted_classes": len(unrestricted_values),
        "must_weak_fair_classes": len(weak_fair_values),
    }
