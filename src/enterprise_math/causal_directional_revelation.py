"""Directional anisotropy as finite causal revelation rather than angle error.

Primitive directions are treated as current states.  For a lookahead h, two
primitive directions are equivalent when their compatible-flag continuation
trees agree through h additions.  The resulting nested partitions define exact
P011-style collision and revelation spectra on the primitive shell.

A connected primitive link is tracked separately to prevent vacuous isotropy:
an edgeless/simple-axis direction set may have identical continuation signatures
merely because no direction-to-direction relation exists.
"""

from __future__ import annotations

from math import comb

from .causal_primitive_link_profile import (
    Adjacency,
    flag_future_signature_histogram,
    component_sizes,
)


def direction_type_sizes(adjacency: Adjacency, lookahead: int) -> tuple[int, ...]:
    if isinstance(lookahead, bool) or not isinstance(lookahead, int) or lookahead < 0:
        raise ValueError("lookahead must be a non-negative integer")
    if lookahead == 0:
        return (len(adjacency),)
    histogram = flag_future_signature_histogram(adjacency, 1, lookahead)
    return tuple(sorted(histogram.values(), reverse=True))


def direction_collision_spectrum(
    adjacency: Adjacency,
    lookahead: int,
    maximum_order: int,
) -> tuple[int, ...]:
    if (
        isinstance(maximum_order, bool)
        or not isinstance(maximum_order, int)
        or maximum_order < 1
    ):
        raise ValueError("maximum_order must be a positive integer")
    sizes = direction_type_sizes(adjacency, lookahead)
    return tuple(
        sum(comb(size, order) for size in sizes if size >= order)
        for order in range(1, maximum_order + 1)
    )


def direction_revelation_spectrum(
    adjacency: Adjacency,
    maximum_lookahead: int,
    maximum_order: int,
) -> tuple[tuple[int, ...], ...]:
    if (
        isinstance(maximum_lookahead, bool)
        or not isinstance(maximum_lookahead, int)
        or maximum_lookahead < 1
    ):
        raise ValueError("maximum_lookahead must be a positive integer")
    collisions = tuple(
        direction_collision_spectrum(adjacency, horizon, maximum_order)
        for horizon in range(maximum_lookahead + 1)
    )
    return tuple(
        tuple(before - after for before, after in zip(collisions[h - 1], collisions[h]))
        for h in range(1, maximum_lookahead + 1)
    )


def first_direction_split_horizon(
    adjacency: Adjacency,
    maximum_lookahead: int,
) -> int | None:
    for horizon in range(1, maximum_lookahead + 1):
        if len(direction_type_sizes(adjacency, horizon)) > 1:
            return horizon
    return None


def primitive_relation_is_nonvacuous(adjacency: Adjacency) -> bool:
    """Minimal guard against edgeless/disconnected vacuous isotropy."""
    return len(component_sizes(adjacency)) == 1 and any(adjacency.values())


def minimum_precision_direction_contract(
    adjacency: Adjacency,
    required_lookahead: int,
) -> bool:
    """Candidate contract, not a physical theorem.

    Requires a connected nontrivial relation link and one primitive-direction
    continuation type through the declared causal lookahead.
    """
    if (
        isinstance(required_lookahead, bool)
        or not isinstance(required_lookahead, int)
        or required_lookahead < 0
    ):
        raise ValueError("required_lookahead must be a non-negative integer")
    return (
        primitive_relation_is_nonvacuous(adjacency)
        and all(len(direction_type_sizes(adjacency, h)) == 1 for h in range(required_lookahead + 1))
    )
