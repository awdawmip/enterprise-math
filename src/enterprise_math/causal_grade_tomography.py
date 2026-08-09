"""Graded causal-event tomography: primitive geometry is only the first shell.

Given a finite event universe, an admissibility law and a nonnegative integer
grade, define E_<=R as all nonzero allowed events of grade at most R.  The first
nonempty grade is the primitive shell, while higher budgets reveal additional
causal event channels.  Two grammars may share the same primitive shell yet split
at a higher grade.

The first grade at which their accepted event sets differ is a direct causal
tomography depth.  Support-order tomography is the specialization grade=event
support size.
"""

from __future__ import annotations

from typing import Callable, Hashable, TypeVar

Event = TypeVar("Event", bound=Hashable)
Law = Callable[[Event], bool]
Grade = Callable[[Event], int]


def visible_events(
    universe: tuple[Event, ...],
    law: Law,
    grade: Grade,
    budget: int,
) -> frozenset[Event]:
    if isinstance(budget, bool) or not isinstance(budget, int) or budget < 0:
        raise ValueError("budget must be a non-negative integer")
    result = set()
    for event in universe:
        value = grade(event)
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError("event grade must be a non-negative integer")
        if law(event) and value <= budget:
            result.add(event)
    return frozenset(result)


def primitive_grade(
    universe: tuple[Event, ...],
    law: Law,
    grade: Grade,
) -> int | None:
    grades = [grade(event) for event in universe if law(event)]
    return min(grades) if grades else None


def primitive_shell(
    universe: tuple[Event, ...],
    law: Law,
    grade: Grade,
) -> frozenset[Event]:
    minimum = primitive_grade(universe, law, grade)
    if minimum is None:
        return frozenset()
    return frozenset(event for event in universe if law(event) and grade(event) == minimum)


def first_grade_difference(
    universe: tuple[Event, ...],
    left_law: Law,
    left_grade: Grade,
    right_law: Law,
    right_grade: Grade,
    maximum_budget: int,
) -> int | None:
    for budget in range(maximum_budget + 1):
        if visible_events(universe, left_law, left_grade, budget) != visible_events(
            universe, right_law, right_grade, budget
        ):
            return budget
    return None


def graded_shell_histogram(
    universe: tuple[Event, ...],
    law: Law,
    grade: Grade,
) -> dict[int, int]:
    histogram: dict[int, int] = {}
    for event in universe:
        if not law(event):
            continue
        value = grade(event)
        histogram[value] = histogram.get(value, 0) + 1
    return dict(sorted(histogram.items()))
