"""Task-relative quotients of asynchronous helper-progress ideals.

With all raw antecedents present, every pre-output helper ideal eventually has
the same saturated raw endpoint.  Different runtime futures require different
quotients:

* endpoint-only: one class;
* remaining helper firings: ideal cardinality / rank;
* enabled-action identity or exact progress: cardinality can fail and labelled
  ideal geometry is needed.
"""

from __future__ import annotations

from dataclasses import dataclass

from .balanced_binary_synergy import balanced_binary_synergy
from .closure_async_progress_poset import helper_ideals, helper_predecessors


@dataclass(frozen=True)
class AsyncQueryLadderReport:
    arity: int
    helper_count: int
    endpoint_class_count: int
    remaining_work_class_count: int
    exact_progress_class_count: int
    same_rank_action_collision_left: frozenset[str] | None
    same_rank_action_collision_right: frozenset[str] | None
    left_enabled: frozenset[str] | None
    right_enabled: frozenset[str] | None


def enabled_helpers(arity: int, completed: frozenset[str]) -> frozenset[str]:
    compiler = balanced_binary_synergy(arity)
    predecessors = helper_predecessors(arity)
    return frozenset(
        helper
        for helper in compiler.helpers
        if helper not in completed and predecessors[helper].issubset(completed)
    )


def asynchronous_query_ladder_report(arity: int) -> AsyncQueryLadderReport:
    if isinstance(arity, bool) or not isinstance(arity, int) or arity < 4:
        raise ValueError("arity must be an integer >= 4")
    compiler = balanced_binary_synergy(arity)
    ideals = tuple(helper_ideals(arity))
    helper_count = len(compiler.helpers)

    sizes = {len(ideal) for ideal in ideals}
    if sizes != set(range(helper_count + 1)):
        raise AssertionError("finite poset ideals must realize every cardinality along a linear extension")

    left = right = None
    left_enabled = right_enabled = None
    by_size: dict[int, list[frozenset[str]]] = {}
    for ideal in ideals:
        by_size.setdefault(len(ideal), []).append(ideal)
    for bucket in by_size.values():
        for i in range(len(bucket)):
            e_i = enabled_helpers(arity, bucket[i])
            for j in range(i + 1, len(bucket)):
                e_j = enabled_helpers(arity, bucket[j])
                if e_i != e_j:
                    left, right = bucket[i], bucket[j]
                    left_enabled, right_enabled = e_i, e_j
                    break
            if left is not None:
                break
        if left is not None:
            break

    return AsyncQueryLadderReport(
        arity=arity,
        helper_count=helper_count,
        endpoint_class_count=1,
        remaining_work_class_count=helper_count + 1,
        exact_progress_class_count=len(ideals),
        same_rank_action_collision_left=left,
        same_rank_action_collision_right=right,
        left_enabled=left_enabled,
        right_enabled=right_enabled,
    )
