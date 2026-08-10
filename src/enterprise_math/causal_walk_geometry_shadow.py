"""When does a traditional pair observation become a causal-walk shadow?

Let A be the primitive-direction relation graph.  For an unordered pair u,v,
record equality/antipode flags and the exact numbers of primitive relation walks
of lengths 1..h between them.  A declared traditional pair observation g(u,v)
(e.g. an exact Gram inner product) is an h-step causal shadow when it is constant
on every such walk-signature class.

The minimum such h is an *observation absorption horizon*.  This does not claim
that walk counts are physical primitives; they are one explicit causal future
language generated solely by repeated primitive relations.
"""

from __future__ import annotations

from typing import Callable, Hashable

from .causal_primitive_link_profile import Adjacency, Vector

PairObservation = Callable[[Vector, Vector], Hashable]


def negate(vector: Vector) -> Vector:
    return tuple(-value for value in vector)


def pair_walk_signatures_from_source(
    adjacency: Adjacency,
    source: Vector,
    maximum_horizon: int,
) -> dict[Vector, tuple[int, ...]]:
    if source not in adjacency:
        raise ValueError("source must belong to adjacency")
    if (
        isinstance(maximum_horizon, bool)
        or not isinstance(maximum_horizon, int)
        or maximum_horizon < 0
    ):
        raise ValueError("maximum_horizon must be a non-negative integer")

    signatures = {target: [] for target in adjacency}
    counts = {source: 1}
    for _ in range(maximum_horizon):
        next_counts: dict[Vector, int] = {}
        for current, multiplicity in counts.items():
            for nxt in adjacency[current]:
                next_counts[nxt] = next_counts.get(nxt, 0) + multiplicity
        counts = next_counts
        for target in adjacency:
            signatures[target].append(counts.get(target, 0))
    return {target: tuple(values) for target, values in signatures.items()}


def minimum_pair_observation_horizon(
    adjacency: Adjacency,
    observation: PairObservation,
    maximum_horizon: int,
) -> int | None:
    """Smallest h such that pair observation is determined by causal walk data."""
    if not adjacency:
        raise ValueError("adjacency must be non-empty")
    vertices = tuple(adjacency)
    tables = {
        source: pair_walk_signatures_from_source(adjacency, source, maximum_horizon)
        for source in vertices
    }

    for horizon in range(maximum_horizon + 1):
        value_by_signature: dict[tuple, Hashable] = {}
        valid = True
        for index, left in enumerate(vertices):
            for right in vertices[index:]:
                signature = (
                    left == right,
                    left == negate(right),
                    tables[left][right][:horizon],
                )
                value = observation(left, right)
                previous = value_by_signature.get(signature)
                if previous is None:
                    value_by_signature[signature] = value
                elif previous != value:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            return horizon
    return None


def pair_observation_type_count_at_horizon(
    adjacency: Adjacency,
    horizon: int,
) -> int:
    vertices = tuple(adjacency)
    tables = {
        source: pair_walk_signatures_from_source(adjacency, source, horizon)
        for source in vertices
    }
    return len({
        (
            left == right,
            left == negate(right),
            tables[left][right],
        )
        for index, left in enumerate(vertices)
        for right in vertices[index:]
    })
