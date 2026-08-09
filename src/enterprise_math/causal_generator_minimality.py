"""Bounded exhaustive evidence for causal-minimal primitive direction systems.

This module does NOT prove a global classification.  It searches symmetric
integer generator sets S=-S inside a finite coordinate box and tests purely
combinatorial causal conditions:

* S spans the requested integer rank over Q;
* the first-direction graph s~t iff s-t is again in S is connected;
* all direction vertices have the same link degree;
* optionally, all primitive center-edge common-neighbor contexts are isomorphic
  under the coarse graph signature used elsewhere in A3.

In the {-1,0,1} coordinate box the first connected regular rank-2 system has six
directions (the A2 triangular root pattern), and the first connected regular
rank-3 system has twelve directions; no 6/8/10-direction rank-3 candidate passes.
The first 12-direction examples also have the FCC/A3 primitive edge context
(4 common neighbors, two disjoint internal bonds).

These are finite-search results only.  A global minimality theorem remains open.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product

Vector = tuple[int, ...]


def negate(vector: Vector) -> Vector:
    return tuple(-value for value in vector)


def canonical_sign(vector: Vector) -> Vector:
    for value in vector:
        if value > 0:
            return vector
        if value < 0:
            return negate(vector)
    return vector


def primitive_representatives(rank: int, coordinate_bound: int = 1) -> tuple[Vector, ...]:
    if isinstance(rank, bool) or not isinstance(rank, int) or rank < 1:
        raise ValueError("rank must be positive")
    if isinstance(coordinate_bound, bool) or not isinstance(coordinate_bound, int) or coordinate_bound < 1:
        raise ValueError("coordinate_bound must be positive")
    representatives = {
        canonical_sign(tuple(vector))
        for vector in product(range(-coordinate_bound, coordinate_bound + 1), repeat=rank)
        if any(vector)
    }
    return tuple(sorted(representatives))


def rational_rank(vectors: tuple[Vector, ...]) -> int:
    if not vectors:
        return 0
    width = len(vectors[0])
    matrix = [[Fraction(value) for value in row] for row in vectors]
    row = 0
    for column in range(width):
        pivot = next((candidate for candidate in range(row, len(matrix)) if matrix[candidate][column] != 0), None)
        if pivot is None:
            continue
        matrix[row], matrix[pivot] = matrix[pivot], matrix[row]
        pivot_value = matrix[row][column]
        matrix[row] = [value / pivot_value for value in matrix[row]]
        for other in range(len(matrix)):
            if other == row:
                continue
            factor = matrix[other][column]
            if factor != 0:
                matrix[other] = [
                    value - factor * pivot_entry
                    for value, pivot_entry in zip(matrix[other], matrix[row])
                ]
        row += 1
        if row == len(matrix):
            break
    return row


def symmetric_direction_set(representatives: tuple[Vector, ...]) -> tuple[Vector, ...]:
    return tuple(representatives) + tuple(negate(vector) for vector in representatives)


def direction_adjacency(direction_set: tuple[Vector, ...]) -> dict[Vector, set[Vector]]:
    directions = set(direction_set)
    adjacency = {direction: set() for direction in directions}
    ordered = tuple(directions)
    for index, left in enumerate(ordered):
        for right in ordered[index + 1 :]:
            difference = tuple(a - b for a, b in zip(left, right))
            if difference in directions:
                adjacency[left].add(right)
                adjacency[right].add(left)
    return adjacency


def direction_link_connected(direction_set: tuple[Vector, ...]) -> bool:
    adjacency = direction_adjacency(direction_set)
    if not adjacency:
        return False
    seed = next(iter(adjacency))
    seen = {seed}
    stack = [seed]
    while stack:
        current = stack.pop()
        for nxt in adjacency[current]:
            if nxt not in seen:
                seen.add(nxt)
                stack.append(nxt)
    return len(seen) == len(adjacency)


def direction_link_degree_set(direction_set: tuple[Vector, ...]) -> tuple[int, ...]:
    adjacency = direction_adjacency(direction_set)
    return tuple(sorted({len(neighbors) for neighbors in adjacency.values()}))


def primitive_edge_context_signature(
    direction_set: tuple[Vector, ...],
    direction: Vector,
) -> tuple[int, int, tuple[int, ...], tuple[int, ...]]:
    adjacency = direction_adjacency(direction_set)
    if direction not in adjacency:
        raise ValueError("direction must belong to supplied set")
    common = tuple(adjacency[direction])
    common_adjacency = {vertex: adjacency[vertex] & set(common) for vertex in common}
    edge_count = sum(len(neighbors) for neighbors in common_adjacency.values()) // 2
    unseen = set(common)
    components = []
    while unseen:
        seed = unseen.pop()
        stack = [seed]
        size = 1
        while stack:
            current = stack.pop()
            for nxt in common_adjacency[current]:
                if nxt in unseen:
                    unseen.remove(nxt)
                    stack.append(nxt)
                    size += 1
        components.append(size)
    degrees = tuple(sorted(len(common_adjacency[vertex]) for vertex in common))
    return len(common), edge_count, tuple(sorted(components, reverse=True)), degrees


def edge_contexts_uniform(direction_set: tuple[Vector, ...]) -> bool:
    return len({
        primitive_edge_context_signature(direction_set, direction)
        for direction in direction_set
    }) == 1


def passes_causal_local_filters(direction_set: tuple[Vector, ...], rank: int) -> bool:
    representatives = tuple(
        direction for direction in direction_set if canonical_sign(direction) == direction
    )
    if rational_rank(representatives) != rank:
        return False
    if not direction_link_connected(direction_set):
        return False
    if len(direction_link_degree_set(direction_set)) != 1:
        return False
    if not edge_contexts_uniform(direction_set):
        return False
    return True


def first_bounded_candidate(
    rank: int,
    direction_count: int,
    coordinate_bound: int = 1,
    require_uniform_edge_context: bool = False,
) -> tuple[Vector, ...] | None:
    if direction_count % 2 != 0 or direction_count < 2:
        raise ValueError("direction_count must be a positive even integer")
    half = direction_count // 2
    representatives = primitive_representatives(rank, coordinate_bound)
    for choice in combinations(representatives, half):
        if rational_rank(choice) != rank:
            continue
        direction_set = symmetric_direction_set(choice)
        if not direction_link_connected(direction_set):
            continue
        if len(direction_link_degree_set(direction_set)) != 1:
            continue
        if require_uniform_edge_context and not edge_contexts_uniform(direction_set):
            continue
        return direction_set
    return None


def bounded_minimum_direction_count(
    rank: int,
    coordinate_bound: int = 1,
    maximum_direction_count: int | None = None,
    require_uniform_edge_context: bool = False,
) -> tuple[int, tuple[Vector, ...]] | None:
    representatives = primitive_representatives(rank, coordinate_bound)
    maximum = maximum_direction_count or 2 * len(representatives)
    start = 2 * rank
    if start % 2:
        start += 1
    for count in range(start, maximum + 1, 2):
        candidate = first_bounded_candidate(
            rank,
            count,
            coordinate_bound,
            require_uniform_edge_context,
        )
        if candidate is not None:
            return count, candidate
    return None
