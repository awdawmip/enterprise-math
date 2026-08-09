"""Exact high-dimensional graded LEGO fibers generated from one-slot rules.

A one-slot state x carries an integer value x and a nonnegative integer grade
g(x). Joint LEGO composition only adds these labels:

    total = sum_i x_i,
    grade = sum_i g(x_i).

Let K_N(c,E) count N-slot fine states with total c and exact grade E. Then

    K_(N+1)(c,E) = sum_x K_N(c-x, E-g(x)),

where the sum is finite under a grade budget. Thus arbitrary-dimensional ball,
shell, minimum-grade, and minimizer-multiplicity data are all readings of one
graded LEGO fiber rather than separate geometric primitives.

For g(x)=|x| this produces the L1/graph-cost shadow; for g(x)=x^2 it produces a
square/radial-cost shadow. Geometry-specific scale factors are applied only
after this integer graded fiber is formed.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Callable

Grade = Callable[[int], int]
GradedCounts = dict[tuple[int, int], int]


def power_grade(power: int) -> Grade:
    if isinstance(power, bool) or not isinstance(power, int) or power <= 0:
        raise ValueError("power must be a positive integer")
    return lambda value: abs(value) ** power


def admissible_one_slot_values(maximum_grade: int, grade: Grade) -> tuple[int, ...]:
    if isinstance(maximum_grade, bool) or not isinstance(maximum_grade, int) or maximum_grade < 0:
        raise ValueError("maximum_grade must be a non-negative integer")
    values = []
    for value in range(-maximum_grade, maximum_grade + 1):
        cost = grade(value)
        if isinstance(cost, bool) or not isinstance(cost, int) or cost < 0:
            raise ValueError("grade must return non-negative integers")
        if cost <= maximum_grade:
            values.append(value)
    return tuple(values)


def one_slot_graded_counts(maximum_grade: int, grade: Grade) -> GradedCounts:
    result: GradedCounts = defaultdict(int)
    for value in admissible_one_slot_values(maximum_grade, grade):
        result[(value, grade(value))] += 1
    return dict(result)


def add_one_slot(
    current: GradedCounts,
    maximum_grade: int,
    grade: Grade,
) -> GradedCounts:
    """Exact dimension-raising recurrence by one graded LEGO slot."""
    if not isinstance(current, dict) or not current:
        raise ValueError("current graded counts must be a non-empty dict")
    values = admissible_one_slot_values(maximum_grade, grade)
    result: GradedCounts = defaultdict(int)
    for (total, energy), multiplicity in current.items():
        if isinstance(total, bool) or not isinstance(total, int):
            raise ValueError("totals must be integers")
        if isinstance(energy, bool) or not isinstance(energy, int) or energy < 0:
            raise ValueError("grades must be non-negative integers")
        if isinstance(multiplicity, bool) or not isinstance(multiplicity, int) or multiplicity < 0:
            raise ValueError("multiplicities must be non-negative integers")
        for value in values:
            next_energy = energy + grade(value)
            if next_energy <= maximum_grade:
                result[(total + value, next_energy)] += multiplicity
    return dict(result)


def graded_fiber_counts(
    slots: int,
    maximum_grade: int,
    grade: Grade,
) -> GradedCounts:
    if isinstance(slots, bool) or not isinstance(slots, int) or slots <= 0:
        raise ValueError("slots must be a positive integer")
    current = one_slot_graded_counts(maximum_grade, grade)
    for _ in range(1, slots):
        current = add_one_slot(current, maximum_grade, grade)
    return current


def exact_grade_count(
    slots: int,
    total: int,
    exact_grade: int,
    grade: Grade,
) -> int:
    if isinstance(exact_grade, bool) or not isinstance(exact_grade, int) or exact_grade < 0:
        raise ValueError("exact_grade must be a non-negative integer")
    counts = graded_fiber_counts(slots, exact_grade, grade)
    return counts.get((total, exact_grade), 0)


def graded_ball_count(
    slots: int,
    total: int,
    maximum_grade: int,
    grade: Grade,
) -> int:
    counts = graded_fiber_counts(slots, maximum_grade, grade)
    return sum(
        multiplicity
        for (state_total, energy), multiplicity in counts.items()
        if state_total == total and energy <= maximum_grade
    )


def graded_shell_counts(
    slots: int,
    total: int,
    maximum_grade: int,
    grade: Grade,
) -> tuple[int, ...]:
    counts = graded_fiber_counts(slots, maximum_grade, grade)
    return tuple(
        counts.get((total, energy), 0)
        for energy in range(maximum_grade + 1)
    )


def minimum_reachable_grade(
    slots: int,
    total: int,
    maximum_grade: int,
    grade: Grade,
) -> int:
    """Lowest occupied grade in the `(slots,total)` fiber."""
    shells = graded_shell_counts(slots, total, maximum_grade, grade)
    for energy, multiplicity in enumerate(shells):
        if multiplicity:
            return energy
    raise ValueError("no state with the requested total exists inside maximum_grade")


def minimum_grade_multiplicity(
    slots: int,
    total: int,
    maximum_grade: int,
    grade: Grade,
) -> tuple[int, int]:
    """Return `(minimum_grade, number_of_minimizers)` from the same graded fiber."""
    shells = graded_shell_counts(slots, total, maximum_grade, grade)
    for energy, multiplicity in enumerate(shells):
        if multiplicity:
            return energy, multiplicity
    raise ValueError("no state with the requested total exists inside maximum_grade")
