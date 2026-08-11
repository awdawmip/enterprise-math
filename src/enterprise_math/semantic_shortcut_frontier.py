"""Closed-form Pareto locations for bounded-support semantic shortcuts.

Shortcut storage G(k,d)=sum_{i<=d} C(k,i) grows strictly with d, while worst-case
semantic geodesic is ceil(k/d).  Therefore the nondominated depths are exactly
the smallest d values achieving each distinct geodesic count:

    { ceil(k/r) : r=1,...,k }.

This is the same depth-location arithmetic as the literal block-cache Pareto with
horizon H=k.  Semantic quotienting does not move the nondominated depth choices;
it changes the storage coordinate attached to each choice.
"""

from __future__ import annotations

from .semantic_shortcut_generator_pareto import semantic_shortcut_pareto_frontier


def semantic_shortcut_frontier_depths_closed_form(generator_count: int) -> tuple[int, ...]:
    if isinstance(generator_count, bool) or not isinstance(generator_count, int) or generator_count < 1:
        raise ValueError("generator_count must be a positive integer")
    values = {
        (generator_count + rounds - 1) // rounds
        for rounds in range(1, generator_count + 1)
    }
    return tuple(sorted(values))


def semantic_shortcut_frontier_matches_enumeration(generator_count: int) -> bool:
    predicted = semantic_shortcut_frontier_depths_closed_form(generator_count)
    actual = tuple(
        point.shortcut_depth
        for point in semantic_shortcut_pareto_frontier(generator_count)
    )
    if predicted != actual:
        raise AssertionError("semantic shortcut closed-form frontier disagreed with enumeration")
    return True
