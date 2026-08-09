"""Exact collision inflation created by candidate-set enlargement.

Given realized labeled images ``A_i`` and candidate supersets ``C_i``, project
tagged incidences ``(i, y)`` to ``y``. Enlarging ``A_i`` to ``C_i`` thickens
those projection fibers. This module computes the exact coefficient inflation
of the P011 collision polynomial under that domain thickening.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Hashable, Iterable, Mapping
from math import comb
from typing import TypeVar

Label = TypeVar("Label", bound=Hashable)
Point = TypeVar("Point", bound=Hashable)


def incidence_multiplicity(images: Mapping[Label, Iterable[Point]]) -> Counter[Point]:
    """Return ``m(y)=#{i:y in image_i}`` for finite labeled image families."""

    counts: Counter[Point] = Counter()
    for values in images.values():
        for point in set(values):
            counts[point] += 1
    return counts


def candidate_excess(
    actual: Mapping[Label, Iterable[Point]],
    candidate: Mapping[Label, Iterable[Point]],
) -> Counter[Point]:
    """Return ``delta(y)=m_C(y)-m_A(y)`` after verifying ``A_i subset C_i``."""

    if set(actual) != set(candidate):
        raise ValueError("actual and candidate must have the same label set")

    for label in actual:
        a = set(actual[label])
        c = set(candidate[label])
        if not a <= c:
            raise ValueError("every actual image must be a subset of its candidate image")

    ma = incidence_multiplicity(actual)
    mc = incidence_multiplicity(candidate)
    return Counter({point: mc[point] - ma[point] for point in mc if mc[point] > ma[point]})


def collision_coefficient(images: Mapping[Label, Iterable[Point]], order: int) -> int:
    """Return the P011 coefficient ``sum_y binom(m(y), order)``."""

    if order < 1:
        raise ValueError("order must be positive")
    return sum(comb(m, order) for m in incidence_multiplicity(images).values() if m >= order)


def collision_inflation(
    actual: Mapping[Label, Iterable[Point]],
    candidate: Mapping[Label, Iterable[Point]],
    order: int,
) -> int:
    """Exact increase in the order-``k`` collision coefficient."""

    if order < 1:
        raise ValueError("order must be positive")
    candidate_excess(actual, candidate)  # validates inclusion
    return collision_coefficient(candidate, order) - collision_coefficient(actual, order)


def pair_collision_inflation_formula(
    actual: Mapping[Label, Iterable[Point]],
    candidate: Mapping[Label, Iterable[Point]],
) -> int:
    """Compute ``sum_y [m_A(y) delta(y) + binom(delta(y),2)]``."""

    ma = incidence_multiplicity(actual)
    delta = candidate_excess(actual, candidate)
    return sum(ma[point] * d + comb(d, 2) for point, d in delta.items())


def all_candidate_pair_collisions_are_spurious(
    actual: Mapping[Label, Iterable[Point]],
    candidate: Mapping[Label, Iterable[Point]],
) -> bool:
    """Whether actual images are disjoint but candidate images collide."""

    return collision_coefficient(actual, 2) == 0 and collision_coefficient(candidate, 2) > 0
