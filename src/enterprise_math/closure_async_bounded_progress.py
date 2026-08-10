"""Exact completion deadline under a bounded-progress scheduler contract.

Define a B-progress contract: while the helper process is nonterminal, every
block of B scheduler steps contains at least one actual helper firing.  Steps
may otherwise stutter, and each firing completes exactly one helper.

If r helpers remain, the exact worst-case completion time is B*r.  The upper
bound follows by one firing per B-step block; sharpness is attained by B-1
stutters followed by one firing, repeated until completion.
"""

from __future__ import annotations

from dataclasses import dataclass

from .closure_async_fairness import fairness_liveness_profile


@dataclass(frozen=True)
class BoundedProgressDeadline:
    arity: int
    completed: frozenset[str]
    progress_window: int
    remaining_helpers: int
    worst_case_steps: int
    sharp: bool


def bounded_progress_deadline(
    arity: int,
    completed: frozenset[str],
    progress_window: int,
) -> BoundedProgressDeadline:
    if isinstance(progress_window, bool) or not isinstance(progress_window, int) or progress_window <= 0:
        raise ValueError("progress_window must be a positive integer")
    profile = fairness_liveness_profile(arity, completed)
    remaining = profile.remaining_helpers
    return BoundedProgressDeadline(
        arity=arity,
        completed=completed,
        progress_window=progress_window,
        remaining_helpers=remaining,
        worst_case_steps=progress_window * remaining,
        sharp=True,
    )


def bounded_progress_deadline_class_count(arity: int, progress_window: int) -> int:
    """Deadline future is equivalent to remaining-helper rank: m+1 classes."""
    if isinstance(progress_window, bool) or not isinstance(progress_window, int) or progress_window <= 0:
        raise ValueError("progress_window must be a positive integer")
    from .closure_async_progress_poset import helper_ideals

    values = {
        bounded_progress_deadline(arity, ideal, progress_window).worst_case_steps
        for ideal in helper_ideals(arity)
    }
    return len(values)
