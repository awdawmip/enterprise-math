"""Finite exact reference layer for R004 precision-genesis research.

No floating-point state semantics are used. The executable constructions are
for discovery, falsification, and regression; theorem proofs live in the R004
research note.
"""
from __future__ import annotations

from collections import deque
from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from math import comb, lcm
from typing import Hashable

State = Hashable
Relation = frozenset[tuple[State, State]]


def _nat(n: int, name: str = "value") -> None:
    if isinstance(n, bool) or not isinstance(n, int) or n < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _pos(n: int, name: str = "value") -> None:
    if isinstance(n, bool) or not isinstance(n, int) or n <= 0:
        raise ValueError(f"{name} must be a positive integer")


def scale_chain(max_scale: int) -> tuple[int, ...]:
    _pos(max_scale, "max_scale")
    out = [1]
    while out[-1] < max_scale:
        out.append(out[-1] * 2)
    if out[-1] != max_scale:
        raise ValueError("max_scale must be a power of two")
    return tuple(out)


def projection(fine_state: int, coarse_scale: int, fine_scale: int) -> int:
    _nat(fine_state, "fine_state")
    _pos(coarse_scale, "coarse_scale")
    _pos(fine_scale, "fine_scale")
    if fine_scale % coarse_scale:
        raise ValueError("coarse_scale must divide fine_scale")
    if fine_state >= fine_scale:
        raise ValueError("fine_state outside toy layer")
    return fine_state // (fine_scale // coarse_scale)


def projection_relation(coarse_scale: int, fine_scale: int) -> Relation:
    _pos(coarse_scale)
    _pos(fine_scale)
    if fine_scale % coarse_scale:
        raise ValueError("coarse_scale must divide fine_scale")
    return frozenset(
        (projection(y, coarse_scale, fine_scale), y) for y in range(fine_scale)
    )


def compatible_paths(scales: Sequence[int]) -> tuple[tuple[int, ...], ...]:
    if not scales:
        raise ValueError("scales must be nonempty")
    for scale in scales:
        _pos(scale, "scale")
    for left, right in zip(scales, scales[1:]):
        if right % left:
            raise ValueError("scales must form a divisibility chain")
    finest = scales[-1]
    return tuple(
        tuple(projection(y, scale, finest) for scale in scales)
        for y in range(finest)
    )


def local_pair_collapse(state: int) -> int:
    _nat(state, "state")
    return state - state % 2


def collapse_fibers(states: Iterable[int]) -> dict[int, tuple[int, ...]]:
    temporary: dict[int, list[int]] = {}
    for state in states:
        _nat(state, "state")
        temporary.setdefault(local_pair_collapse(state), []).append(state)
    return {target: tuple(sources) for target, sources in sorted(temporary.items())}


def successors(relation: Relation, source: State) -> frozenset[State]:
    return frozenset(target for current, target in relation if current == source)


def serial_on_support(n: Mapping[State, int], relation: Relation) -> bool:
    for state, count in n.items():
        _nat(count, "multiplicity")
        if count and not successors(relation, state):
            return False
    return True


def propagate_history_multiplicities(
    n: Mapping[State, int], relation: Relation
) -> dict[State, int]:
    """Push path multiplicities through one state-extensional serial relation."""
    if not serial_on_support(n, relation):
        raise ValueError("relation must be serial on occupied support")
    output: dict[State, int] = {}
    for state, count in n.items():
        if not count:
            continue
        for target in successors(relation, state):
            output[target] = output.get(target, 0) + count
    return output


def collision_spectrum(
    n: Mapping[State, int], max_order: int | None = None
) -> tuple[tuple[int, int], ...]:
    counts = tuple(n.values())
    for count in counts:
        _nat(count, "multiplicity")
    if max_order is None:
        max_order = max(counts, default=0)
    _nat(max_order, "max_order")
    return tuple(
        (
            order,
            sum(comb(count, order) for count in counts if count >= order),
        )
        for order in range(1, max_order + 1)
    )


def history_count(n: Mapping[State, int]) -> int:
    for count in n.values():
        _nat(count, "multiplicity")
    return sum(n.values())


def occupied_count(n: Mapping[State, int]) -> int:
    for count in n.values():
        _nat(count, "multiplicity")
    return sum(count > 0 for count in n.values())


def merge_excess(n: Mapping[State, int]) -> int:
    return history_count(n) - occupied_count(n)


def branching_increment(n: Mapping[State, int], relation: Relation) -> int:
    if not serial_on_support(n, relation):
        raise ValueError("relation must be serial on occupied support")
    return sum(
        count * (len(successors(relation, state)) - 1)
        for state, count in n.items()
        if count
    )


def history_balance(n: Mapping[State, int], relation: Relation) -> tuple[int, int, int]:
    after = propagate_history_multiplicities(n, relation)
    branch = branching_increment(n, relation)
    occupied_delta = occupied_count(after) - occupied_count(n)
    merge_delta = merge_excess(after) - merge_excess(n)
    return branch, occupied_delta, merge_delta


def history_relation_factors_through_state(
    history_to_state: Mapping[State, State],
    history_support: Mapping[State, frozenset[State]],
) -> bool:
    grouped: dict[State, frozenset[State]] = {}
    if set(history_to_state) != set(history_support):
        raise ValueError("history domains must match")
    for history, state in history_to_state.items():
        support = history_support[history]
        if not support:
            raise ValueError("supports must be nonempty")
        if state in grouped and grouped[state] != support:
            return False
        grouped[state] = support
    return True


def exhaustive_history_resurrection_counts(
    num_future_states: int = 3,
) -> dict[str, int]:
    _pos(num_future_states, "num_future_states")
    future = tuple(range(num_future_states))
    supports = tuple(
        frozenset(
            future[index]
            for index in range(num_future_states)
            if mask & (1 << index)
        )
        for mask in range(1, 1 << num_future_states)
    )
    return {
        "state_extensional_relations": len(supports),
        "state_extensional_resurrections": 0,
        "history_indexed_relations": len(supports) ** 2,
        "history_indexed_resurrections": sum(
            left != right for left in supports for right in supports
        ),
    }


def _edge(left: State, right: State) -> frozenset[State]:
    if left == right:
        raise ValueError("simple edge needs distinct endpoints")
    return frozenset((left, right))


def connected(
    vertices: Sequence[State], edges: frozenset[frozenset[State]]
) -> bool:
    if not vertices:
        return False
    seen = {vertices[0]}
    queue: deque[State] = deque([vertices[0]])
    while queue:
        current = queue.popleft()
        for edge in edges:
            if current not in edge:
                continue
            other = next(value for value in edge if value != current)
            if other not in seen:
                seen.add(other)
                queue.append(other)
    return seen == set(vertices)


def exhaustive_hidden_geometry_counts(num_vertices: int = 3) -> dict[str, int]:
    _pos(num_vertices, "num_vertices")
    vertices = tuple(range(num_vertices))
    candidates = tuple(combinations(vertices, 2))
    total = nonempty = connected_count = 0
    for mask in range(1 << len(candidates)):
        edges = frozenset(
            _edge(*candidates[index])
            for index in range(len(candidates))
            if mask & (1 << index)
        )
        total += 1
        nonempty += bool(edges)
        connected_count += connected(vertices, edges)
    return {
        "observable_classes": 1,
        "simple_graphs": total,
        "nonempty_simple_graphs": nonempty,
        "connected_simple_graphs": connected_count,
    }


def cycle_edges(size: int) -> frozenset[frozenset[int]]:
    _pos(size, "size")
    if size < 3:
        return frozenset()
    return frozenset(_edge(index, (index + 1) % size) for index in range(size))


def shortest_distance(
    vertices: Sequence[State],
    edges: frozenset[frozenset[State]],
    source: State,
    target: State,
) -> int | None:
    if source not in vertices or target not in vertices:
        raise ValueError("unknown vertex")
    if source == target:
        return 0
    distance = {source: 0}
    queue: deque[State] = deque([source])
    while queue:
        current = queue.popleft()
        for edge in edges:
            if current not in edge:
                continue
            other = next(value for value in edge if value != current)
            if other in distance:
                continue
            distance[other] = distance[current] + 1
            if other == target:
                return distance[other]
            queue.append(other)
    return None


def shell(
    vertices: Sequence[State],
    edges: frozenset[frozenset[State]],
    center: State,
    radius: int,
) -> frozenset[State]:
    _nat(radius, "radius")
    return frozenset(
        vertex
        for vertex in vertices
        if shortest_distance(vertices, edges, center, vertex) == radius
    )


def ball(
    vertices: Sequence[State],
    edges: frozenset[frozenset[State]],
    center: State,
    radius: int,
) -> frozenset[State]:
    _nat(radius, "radius")
    result = set()
    for vertex in vertices:
        distance = shortest_distance(vertices, edges, center, vertex)
        if distance is not None and distance <= radius:
            result.add(vertex)
    return frozenset(result)


def geodesic_count(
    vertices: Sequence[State],
    edges: frozenset[frozenset[State]],
    source: State,
    target: State,
) -> int:
    if source not in vertices or target not in vertices:
        raise ValueError("unknown vertex")
    distance = {source: 0}
    count = {source: 1}
    queue: deque[State] = deque([source])
    while queue:
        current = queue.popleft()
        for edge in edges:
            if current not in edge:
                continue
            other = next(value for value in edge if value != current)
            candidate = distance[current] + 1
            if other not in distance:
                distance[other] = candidate
                count[other] = count[current]
                queue.append(other)
            elif distance[other] == candidate:
                count[other] += count[current]
    return count.get(target, 0)


@dataclass(frozen=True)
class ToyLayer:
    scale: int
    states: tuple[int, ...]
    adjacency: frozenset[frozenset[int]]


def toy_universe(max_scale: int = 8, geometry_scale: int = 4) -> tuple[ToyLayer, ...]:
    scales = scale_chain(max_scale)
    if geometry_scale not in scales:
        raise ValueError("geometry_scale must be a toy scale")
    return tuple(
        ToyLayer(
            scale,
            tuple(range(scale)),
            cycle_edges(scale) if scale >= geometry_scale else frozenset(),
        )
        for scale in scales
    )


def first_geometry_scale(layers: Sequence[ToyLayer]) -> int | None:
    return next((layer.scale for layer in layers if layer.adjacency), None)


def environment_overlap(left: Sequence[State], right: Sequence[State]) -> Fraction:
    if not left or len(left) != len(right):
        raise ValueError("records need equal positive length")
    return Fraction(sum(a == b for a, b in zip(left, right)), len(left))


def square_riemann_sum(n: int) -> Fraction:
    _pos(n, "n")
    return Fraction((n - 1) * (2 * n - 1), 6 * n * n)


def square_riemann_error(n: int) -> Fraction:
    _pos(n, "n")
    return Fraction(1, 3) - square_riemann_sum(n)


def square_forward_difference(n: int, k: int) -> Fraction:
    _pos(n, "n")
    _nat(k, "k")
    if k >= n:
        raise ValueError("k must be below n")
    return Fraction(2 * k + 1, n)


@dataclass(frozen=True)
class DualMonotoneSystem:
    capacities: tuple[int, ...]
    history_classes: tuple[int, ...]
    history_maps: tuple[tuple[int, ...], ...]


def construct_dual_monotone_system(
    capacities: Sequence[int], history_classes: Sequence[int]
) -> DualMonotoneSystem:
    if not capacities or len(capacities) != len(history_classes):
        raise ValueError("same positive length required")
    capacity = tuple(capacities)
    classes = tuple(history_classes)
    for value in capacity:
        _pos(value, "capacity")
    for value in classes:
        _pos(value, "history_classes")
    if any(left > right for left, right in zip(capacity, capacity[1:])):
        raise ValueError("capacity must not decrease")
    if any(left < right for left, right in zip(classes, classes[1:])):
        raise ValueError("history classes must not increase")
    if any(left > right for left, right in zip(classes, capacity)):
        raise ValueError("classes exceed capacity")
    cohort = classes[0]
    maps = tuple(
        tuple(min(history, count - 1) for history in range(cohort))
        for count in classes
    )
    return DualMonotoneSystem(capacity, classes, maps)


def dual_monotone_transition_compatible(system: DualMonotoneSystem) -> bool:
    for before, after in zip(system.history_maps, system.history_maps[1:]):
        induced: dict[int, int] = {}
        for current, target in zip(before, after):
            if current in induced and induced[current] != target:
                return False
            induced[current] = target
    return True


def rational_seed(probabilities: Sequence[Fraction]) -> tuple[int, tuple[int, ...]]:
    """One finite integer seed reproducing an exact rational distribution."""
    row = tuple(probabilities)
    if not row or any(p < 0 for p in row) or sum(row, Fraction(0, 1)) != 1:
        raise ValueError("probabilities must form a rational distribution")
    denominator = 1
    for probability in row:
        denominator = lcm(denominator, probability.denominator)
    return denominator, tuple(
        probability.numerator * (denominator // probability.denominator)
        for probability in row
    )
