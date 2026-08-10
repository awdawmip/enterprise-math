"""Exact finite census and P008 pressure tests for quotient-safe operation algebras.

Generic operation descent itself is already owned by A2/P023 and Lean-checked in
``EnterpriseMath/Quotient/OperationCongruence.lean``. This module adds a finite
census/decomposition layer plus exact witnesses for complete-growth interval
quotients.

For a finite partition q:X->Q with fiber sizes m_a, an r-ary operation is safe
exactly when every product fiber is mapped into one output fiber. Hence the
number of safe r-ary operations is

    product_{a in Q^r} sum_{b in Q} m_b ** product_i m_{a_i}.

For a P008 complete-growth partition with integer basins
[V(k), V(k+1)-1], ordinary binary addition cannot descend through any quotient
having a basin of width greater than one: fixing the second input to 1 gives a
+1 translation, and the first/last states of that basin are separated.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Hashable, Iterable, Mapping, Sequence
from itertools import product
from math import prod
from typing import TypeVar

State = TypeVar("State", bound=Hashable)
Label = TypeVar("Label", bound=Hashable)


def _states(domain: Iterable[State]) -> tuple[State, ...]:
    states = tuple(domain)
    if not states:
        raise ValueError("domain must be nonempty")
    if len(states) != len(set(states)):
        raise ValueError("domain states must be distinct")
    return states


def fiber_sizes(
    domain: Iterable[State], partition: Mapping[State, Label]
) -> tuple[int, ...]:
    """Return positive fiber sizes in deterministic first-seen label order."""
    states = _states(domain)
    if set(partition) != set(states):
        raise ValueError("partition must be total on the domain and have no extra keys")
    ordered_labels: list[Label] = []
    seen: set[Label] = set()
    for state in states:
        label = partition[state]
        if label not in seen:
            seen.add(label)
            ordered_labels.append(label)
    counts = Counter(partition[state] for state in states)
    return tuple(counts[label] for label in ordered_labels)


def safe_operation_count_from_fiber_sizes(
    sizes: Sequence[int], arity: int
) -> int:
    """Count all quotient-safe ``arity``-ary operations on a finite partition.

    ``sizes`` are the nonzero sizes of quotient fibers. The result counts all
    fine operations X^arity -> X whose output quotient class depends only on the
    input quotient classes.
    """
    sizes = tuple(sizes)
    if not sizes or any(
        isinstance(size, bool) or not isinstance(size, int) or size <= 0
        for size in sizes
    ):
        raise ValueError("sizes must be a nonempty sequence of positive integers")
    if isinstance(arity, bool) or not isinstance(arity, int) or arity < 1:
        raise ValueError("arity must be a positive integer")

    total = 1
    for coarse_tuple in product(range(len(sizes)), repeat=arity):
        fine_input_count = prod(sizes[index] for index in coarse_tuple)
        total *= sum(target_size**fine_input_count for target_size in sizes)
    return total


def safe_operation_count(
    domain: Iterable[State],
    partition: Mapping[State, Label],
    arity: int,
) -> int:
    return safe_operation_count_from_fiber_sizes(
        fiber_sizes(domain, partition), arity
    )


def uniform_safe_operation_count(
    class_count: int, fiber_size: int, arity: int
) -> int:
    """Closed form for ``class_count`` equal fibers of size ``fiber_size``."""
    for name, value in (
        ("class_count", class_count),
        ("fiber_size", fiber_size),
        ("arity", arity),
    ):
        if isinstance(value, bool) or not isinstance(value, int) or value < 1:
            raise ValueError(f"{name} must be a positive integer")
    coarse_tuple_count = class_count**arity
    fine_tuple_count = fiber_size**arity
    return class_count**coarse_tuple_count * fiber_size ** (
        coarse_tuple_count * fine_tuple_count
    )


def _validate_growth(growth: Sequence[int]) -> tuple[int, ...]:
    values = tuple(growth)
    if len(values) < 2:
        raise ValueError("growth must contain at least two complete levels")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in values
    ):
        raise ValueError("growth values must be nonnegative integers")
    if any(left >= right for left, right in zip(values, values[1:])):
        raise ValueError("growth must be strictly increasing")
    return values


def addition_unit_obstruction(
    growth: Sequence[int],
) -> tuple[int, int, int, int] | None:
    """Return ``(level, left, right, addend)`` witnessing failure of + congruence.

    If a represented basin has width > 1, then ``left=V(k)`` and
    ``right=V(k+1)-1`` have the same level, while adding one leaves ``left`` in
    the basin and moves ``right`` to the next level.
    """
    values = _validate_growth(growth)
    for level, (left_boundary, right_boundary) in enumerate(
        zip(values, values[1:])
    ):
        if right_boundary - left_boundary > 1:
            return level, left_boundary, right_boundary - 1, 1
    return None


def all_represented_basins_are_singletons(growth: Sequence[int]) -> bool:
    values = _validate_growth(growth)
    return all(right - left == 1 for left, right in zip(values, values[1:]))


def translation_safe_on_periodic_width_sample(
    widths: Sequence[int], increment: int, cycles: int = 6
) -> bool:
    """Exact bounded checker for a periodically repeated width word.

    It is intended as a regression oracle for non-identifiability examples, not
    as a replacement for the stage-3 periodic-basin theorem.
    """
    widths = tuple(widths)
    if not widths or any(
        isinstance(width, bool) or not isinstance(width, int) or width <= 0
        for width in widths
    ):
        raise ValueError("widths must be positive integers")
    if (
        isinstance(increment, bool)
        or not isinstance(increment, int)
        or increment < 0
    ):
        raise ValueError("increment must be a nonnegative integer")
    if isinstance(cycles, bool) or not isinstance(cycles, int) or cycles < 2:
        raise ValueError("cycles must be an integer at least two")

    boundaries = [0]
    for index in range(cycles * len(widths) + 2 * len(widths)):
        boundaries.append(boundaries[-1] + widths[index % len(widths)])

    def level(amount: int) -> int:
        lo, hi = 0, len(boundaries)
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if boundaries[mid] <= amount:
                lo = mid
            else:
                hi = mid
        return lo

    maximum = boundaries[cycles * len(widths)] - 1 - increment
    if maximum < 0:
        return True
    first_in_class: dict[int, int] = {}
    for amount in range(maximum + 1):
        cls = level(amount)
        if cls not in first_in_class:
            first_in_class[cls] = amount
            continue
        representative = first_in_class[cls]
        if level(representative + increment) != level(amount + increment):
            return False
    return True
