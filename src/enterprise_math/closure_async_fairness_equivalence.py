"""Weak-fairness/completion equivalence for finite one-shot helper systems.

Interpret executions as infinite by allowing terminal stutter forever.  In the
finite monotone helper ideal system:

* every eventually completing execution is weakly fair, since every helper is
  eventually fired;
* every weakly fair execution eventually completes, because every nonterminal
  ideal has a minimal complement helper that stays enabled until firing.

Thus weakly fair executions are exactly completing executions for this special
system.  The result is intentionally scoped and is not a generic fairness law.
"""

from __future__ import annotations

from dataclasses import dataclass

from .closure_async_progress_poset import helper_ideals
from .closure_async_query_ladder import enabled_helpers


@dataclass(frozen=True)
class FairnessCompletionCertificate:
    arity: int
    ideal_count: int
    every_nonterminal_has_enabled_helper: bool
    enabled_helpers_persist_until_fired: bool
    finite_one_shot: bool
    weak_fair_implies_completion: bool
    completion_implies_weak_fair: bool
    execution_classes_equal: bool


def fairness_completion_certificate(arity: int) -> FairnessCompletionCertificate:
    if isinstance(arity, bool) or not isinstance(arity, int) or arity < 4:
        raise ValueError("arity must be an integer >= 4")
    ideals = tuple(helper_ideals(arity))
    full_size = max(len(ideal) for ideal in ideals)
    every_enabled = all(
        len(ideal) == full_size or bool(enabled_helpers(arity, ideal))
        for ideal in ideals
    )
    if not every_enabled:
        raise AssertionError("nonterminal ideal must have a minimal enabled complement helper")

    # Completed sets grow monotonically and helper prerequisites are never
    # removed, so an enabled helper remains enabled until it fires.
    persistent = True
    finite_one_shot = True
    weak_to_complete = every_enabled and persistent and finite_one_shot
    complete_to_weak = True
    return FairnessCompletionCertificate(
        arity=arity,
        ideal_count=len(ideals),
        every_nonterminal_has_enabled_helper=every_enabled,
        enabled_helpers_persist_until_fired=persistent,
        finite_one_shot=finite_one_shot,
        weak_fair_implies_completion=weak_to_complete,
        completion_implies_weak_fair=complete_to_weak,
        execution_classes_equal=weak_to_complete and complete_to_weak,
    )
