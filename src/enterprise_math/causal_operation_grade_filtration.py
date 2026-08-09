"""Future precision induces a nonnegative integer filtration on compatible dynamics.

Given a distinguishing-depth matrix D, every ultimate-compatible raw endomap f
has semantic loss grade ell(f).  Define F_C={f:ell(f)<=C}.  Then F_0 is exactly
the set of operations preserving every finite-budget equivalence layer, and
composition satisfies F_A∘F_B subset F_(A+B).

For small finite systems this module exhaustively counts the operation-grade
histogram.  It is a semantic dynamics spectrum derived from future precision,
not a physical energy distribution.
"""

from __future__ import annotations

from itertools import product
from typing import Hashable, Mapping

from .causal_semantic_grade import (
    Depth,
    operation_preserves_ultimate_equivalence,
    semantic_loss_grade,
)

State = Hashable


def operation_has_layer_degree_at_most(
    states: tuple[State, ...],
    depth: Mapping[tuple[State, State], Depth],
    operation: Mapping[State, State],
    degree: int,
) -> bool:
    """Exact all-budget condition D(fx,fy)>=D(x,y)-degree."""
    if isinstance(degree, bool) or not isinstance(degree, int) or degree < 0:
        raise ValueError("degree must be a non-negative integer")
    if not operation_preserves_ultimate_equivalence(states, depth, operation):
        return False
    for left in states:
        for right in states:
            before = depth[(left, right)]
            after = depth[(operation[left], operation[right])]
            if before is None:
                if after is not None:
                    return False
                continue
            if after is None:
                continue
            if after < before - degree:
                return False
    return True


def semantic_grade_matches_minimum_layer_degree(
    states: tuple[State, ...],
    depth: Mapping[tuple[State, State], Depth],
    operation: Mapping[State, State],
) -> bool:
    grade = semantic_loss_grade(states, depth, operation)
    if not operation_has_layer_degree_at_most(states, depth, operation, grade):
        return False
    return grade == 0 or not operation_has_layer_degree_at_most(
        states, depth, operation, grade - 1
    )


def grade_zero_preserves_every_depth_threshold(
    states: tuple[State, ...],
    depth: Mapping[tuple[State, State], Depth],
    operation: Mapping[State, State],
) -> bool:
    """ell(f)=0 iff every pair-equivalence threshold is preserved."""
    grade_zero = semantic_loss_grade(states, depth, operation) == 0
    finite_depths = sorted(
        {
            value
            for value in depth.values()
            if value is not None
        }
    )
    preserves = True
    for threshold in finite_depths:
        for left in states:
            for right in states:
                before = depth[(left, right)]
                after = depth[(operation[left], operation[right])]
                equivalent_before = before is None or before > threshold
                equivalent_after = after is None or after > threshold
                if equivalent_before and not equivalent_after:
                    preserves = False
                    break
            if not preserves:
                break
        if not preserves:
            break
    return grade_zero == preserves


def grade_histogram_on_small_system(
    states: tuple[State, ...],
    depth: Mapping[tuple[State, State], Depth],
) -> dict[int, int]:
    """Exhaust all ultimate-compatible raw endomaps and count by semantic grade."""
    histogram: dict[int, int] = {}
    for outputs in product(states, repeat=len(states)):
        operation = dict(zip(states, outputs))
        if not operation_preserves_ultimate_equivalence(states, depth, operation):
            continue
        grade = semantic_loss_grade(states, depth, operation)
        histogram[grade] = histogram.get(grade, 0) + 1
    return dict(sorted(histogram.items()))


def filtration_count_from_histogram(
    histogram: Mapping[int, int],
    degree: int,
) -> int:
    if isinstance(degree, bool) or not isinstance(degree, int) or degree < 0:
        raise ValueError("degree must be a non-negative integer")
    return sum(count for grade, count in histogram.items() if grade <= degree)


def composition_respects_grade_filtration(
    states: tuple[State, ...],
    depth: Mapping[tuple[State, State], Depth],
    first: Mapping[State, State],
    second: Mapping[State, State],
) -> bool:
    first_grade = semantic_loss_grade(states, depth, first)
    second_grade = semantic_loss_grade(states, depth, second)
    composed = {state: second[first[state]] for state in states}
    return semantic_loss_grade(states, depth, composed) <= first_grade + second_grade
