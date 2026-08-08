"""Exact collision-polynomial increments induced by deterministic fiber merging.

This module connects the Pair/kernel event layer to P011 higher-order collision
spectra.  Given an old finite partition and a deterministic map on its block
labels, every new block is a union of old blocks.  Its exact polynomial
increment counts subsets that become contained in one new block at this step
but were not already contained in one old block.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Hashable, Iterable, Mapping
from math import comb
from typing import TypeVar

Label = TypeVar("Label", bound=Hashable)
NewLabel = TypeVar("NewLabel", bound=Hashable)


def _require_positive_sizes(sizes: Iterable[int]) -> tuple[int, ...]:
    values = tuple(sizes)
    if not values:
        raise ValueError("at least one old fiber is required")
    for value in values:
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
            raise ValueError("fiber sizes must be positive integers")
    return values


def fiber_collision_coefficients(size: int) -> tuple[int, ...]:
    """Return coefficients of ``(1+t)^size - 1`` from degree 1 through size."""
    if isinstance(size, bool) or not isinstance(size, int) or size <= 0:
        raise ValueError("size must be a positive integer")
    return tuple(comb(size, degree) for degree in range(1, size + 1))


def merged_fiber_increment_coefficients(sizes: Iterable[int]) -> tuple[int, ...]:
    """Exact collision-spectrum increment when old fibers merge into one.

    For old fiber sizes ``m_i``, the returned degree-k coefficient is

    ``C(sum m_i,k) - sum_i C(m_i,k)``.

    It counts k-subsets that lie in the merged fiber but were not already
    contained in one old fiber.
    """
    values = _require_positive_sizes(sizes)
    total = sum(values)
    return tuple(
        comb(total, degree) - sum(comb(value, degree) for value in values)
        for degree in range(1, total + 1)
    )


def newly_colliding_pairs_count(sizes: Iterable[int]) -> int:
    """Return the number of unordered pairs newly merged at this step."""
    values = _require_positive_sizes(sizes)
    return sum(
        values[left] * values[right]
        for left in range(len(values))
        for right in range(left + 1, len(values))
    )


def polynomial_add(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    """Add degree-1-indexed coefficient vectors."""
    length = max(len(left), len(right))
    return tuple(
        (left[index] if index < len(left) else 0)
        + (right[index] if index < len(right) else 0)
        for index in range(length)
    )


def collision_polynomial_from_fiber_sizes(sizes: Iterable[int]) -> tuple[int, ...]:
    """Return P011 collision-polynomial coefficients for a finite partition."""
    result: tuple[int, ...] = ()
    for size in sizes:
        result = polynomial_add(result, fiber_collision_coefficients(size))
    return result


def partition_step_increment(
    old_sizes: Mapping[Label, int],
    old_to_new: Mapping[Label, NewLabel],
) -> tuple[int, ...]:
    """Return the full polynomial increment for one deterministic block merge.

    Every old block label must have exactly one target label.  Target blocks are
    unions of old blocks.  A target receiving only one old block contributes
    zero increment.
    """
    if set(old_sizes) != set(old_to_new):
        raise ValueError("old_sizes and old_to_new must have identical labels")
    grouped: dict[NewLabel, list[int]] = defaultdict(list)
    for label, size in old_sizes.items():
        if isinstance(size, bool) or not isinstance(size, int) or size <= 0:
            raise ValueError("fiber sizes must be positive integers")
        grouped[old_to_new[label]].append(size)

    result: tuple[int, ...] = ()
    for sizes in grouped.values():
        result = polynomial_add(result, merged_fiber_increment_coefficients(sizes))
    return result


def new_fiber_sizes(
    old_sizes: Mapping[Label, int],
    old_to_new: Mapping[Label, NewLabel],
) -> dict[NewLabel, int]:
    """Aggregate old fiber cardinalities into their deterministic target fibers."""
    if set(old_sizes) != set(old_to_new):
        raise ValueError("old_sizes and old_to_new must have identical labels")
    result: dict[NewLabel, int] = defaultdict(int)
    for label, size in old_sizes.items():
        if isinstance(size, bool) or not isinstance(size, int) or size <= 0:
            raise ValueError("fiber sizes must be positive integers")
        result[old_to_new[label]] += size
    return dict(result)
