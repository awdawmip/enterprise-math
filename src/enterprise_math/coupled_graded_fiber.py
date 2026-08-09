"""Coupled graded LEGO composition with support/multiplicity and grade shift.

Each fine state carries integer `(total, grade)`.  A pair `(u,v)` composes with
nonnegative multiplicity kappa(u,v) and optional integer cross-grade shift
gamma(u,v).  The joint state contributes

    total = total_u + total_v,
    grade = grade_u + grade_v + gamma(u,v).

Thus support/multiplicity (`kappa`) and interaction grade (`gamma`) remain typed
and separate.  Free independent composition is kappa=1, gamma=0.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Hashable

State = Hashable
Label = tuple[int, int]


def coupled_graded_counts(
    left_labels: dict[State, Label],
    right_labels: dict[State, Label],
    coupling: dict[tuple[State, State], int],
    cross_grade: dict[tuple[State, State], int] | None = None,
    maximum_grade: int | None = None,
) -> dict[Label, int]:
    if not isinstance(left_labels, dict) or not isinstance(right_labels, dict):
        raise ValueError("state labels must be dicts")
    if cross_grade is None:
        cross_grade = {}
    result: dict[Label, int] = defaultdict(int)
    for left, (left_total, left_grade) in left_labels.items():
        for right, (right_total, right_grade) in right_labels.items():
            pair = (left, right)
            multiplicity = coupling.get(pair, 0)
            shift = cross_grade.get(pair, 0)
            for value, name in (
                (left_total, "total"),
                (right_total, "total"),
                (left_grade, "grade"),
                (right_grade, "grade"),
                (shift, "cross grade"),
            ):
                if isinstance(value, bool) or not isinstance(value, int):
                    raise ValueError(f"{name} values must be integers")
            if left_grade < 0 or right_grade < 0:
                raise ValueError("input grades must be non-negative")
            if isinstance(multiplicity, bool) or not isinstance(multiplicity, int) or multiplicity < 0:
                raise ValueError("coupling multiplicities must be non-negative integers")
            if not multiplicity:
                continue
            grade = left_grade + right_grade + shift
            if grade < 0:
                raise ValueError("joint grade must remain non-negative")
            if maximum_grade is not None and grade > maximum_grade:
                continue
            result[(left_total + right_total, grade)] += multiplicity
    return dict(result)


def free_graded_coupling(
    left_states: tuple[State, ...],
    right_states: tuple[State, ...],
) -> dict[tuple[State, State], int]:
    return {
        (left, right): 1
        for left in left_states
        for right in right_states
    }


def grade_shift_support(
    cross_grade: dict[tuple[State, State], int],
) -> frozenset[tuple[State, State]]:
    """Pairs carrying a nonzero interaction grade shift."""
    if any(isinstance(value, bool) or not isinstance(value, int) for value in cross_grade.values()):
        raise ValueError("cross-grade shifts must be integers")
    return frozenset(pair for pair, value in cross_grade.items() if value != 0)
