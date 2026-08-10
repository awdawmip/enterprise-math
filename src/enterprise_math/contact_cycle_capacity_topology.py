"""Discrete contact-topology transitions driven by explicit cycle-memory exhaustion.

This E001 layer consumes the finite witness-capacity policy from the preceding
E001/P024 bridge.  It does *not* claim that capacity exhaustion is a universal
fracture law.  Instead it studies one explicit candidate world policy:

    when the next declared memory increment cannot fit on one or more contacts,
    those contacts become candidates for removal from the future contact graph.

The finite-memory arithmetic determines the first-exhaustion set, but it does
not choose a topology selector when several contacts exhaust simultaneously.
This module therefore reports both the simultaneous-removal outcome and every
single-bottleneck outcome rather than silently choosing one.

For an undirected finite contact graph with V bodies, E active contacts and c
components, cycle rank is

    beta = E - V + c.

Removing a contact set F gives

    beta - beta' = |F| - (c' - c).

Thus removal of one non-bridge cycle contact lowers beta by one without
splitting the component, while removal of a bridge raises component count and
leaves beta unchanged.  The identity extends exactly to arbitrary removal
sets.

The event is sampled/discrete: if ``tau`` complete macro repetitions fit in the
memory capacity, topology exhaustion is encountered at the attempted
``tau+1``-st repetition.  No hidden continuous crack path is inserted.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Iterable, Sequence

from .contact_cycle_memory_policy import (
    witness_capacity_repetition_capacity,
)


Edge = tuple[int, int]
Vector = tuple[int, ...]


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _graph(
    num_vertices: int,
    edges: Iterable[Sequence[int]],
) -> tuple[Edge, ...]:
    _require_int("num_vertices", num_vertices)
    if num_vertices <= 0:
        raise ValueError("num_vertices must be positive")
    result = []
    for raw in tuple(edges):
        if len(raw) != 2:
            raise ValueError("each contact edge must have two endpoints")
        left, right = raw
        _require_int("edge endpoint", left)
        _require_int("edge endpoint", right)
        if not (0 <= left < num_vertices and 0 <= right < num_vertices):
            raise ValueError("edge endpoint is outside the vertex set")
        if left == right:
            raise ValueError("self-loop contacts are not supported")
        result.append((left, right))
    return tuple(result)


def _removed_indices(
    removed: Iterable[int],
    edge_count: int,
) -> tuple[int, ...]:
    values = tuple(removed)
    if len(set(values)) != len(values):
        raise ValueError("removed contact indices must be distinct")
    for value in values:
        _require_int("removed contact index", value)
        if not 0 <= value < edge_count:
            raise ValueError("removed contact index is outside the graph")
    return tuple(sorted(values))


def contact_component_count(
    num_vertices: int,
    edges: Iterable[Sequence[int]],
    removed: Iterable[int] = (),
) -> int:
    graph = _graph(num_vertices, edges)
    removed_set = set(_removed_indices(removed, len(graph)))
    adjacency = [[] for _ in range(num_vertices)]
    for index, (left, right) in enumerate(graph):
        if index in removed_set:
            continue
        adjacency[left].append(right)
        adjacency[right].append(left)

    seen: set[int] = set()
    count = 0
    for start in range(num_vertices):
        if start in seen:
            continue
        count += 1
        seen.add(start)
        queue: deque[int] = deque([start])
        while queue:
            current = queue.popleft()
            for neighbor in adjacency[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
    return count


def contact_cycle_rank(
    num_vertices: int,
    edges: Iterable[Sequence[int]],
    removed: Iterable[int] = (),
) -> int:
    graph = _graph(num_vertices, edges)
    removed_indices = _removed_indices(removed, len(graph))
    active_edges = len(graph) - len(removed_indices)
    components = contact_component_count(
        num_vertices,
        graph,
        removed_indices,
    )
    return active_edges - num_vertices + components


@dataclass(frozen=True)
class WitnessExhaustionEvent:
    safe_completed_repetitions: int | None
    first_exhaustion_attempt: int | None
    bottleneck_contacts: tuple[int, ...]

    @property
    def never_exhausts(self) -> bool:
        return self.safe_completed_repetitions is None


def first_witness_exhaustion(
    witness_state: Sequence[int],
    capacity: Sequence[int],
    increment: Sequence[int],
) -> WitnessExhaustionEvent:
    lifetime = witness_capacity_repetition_capacity(
        witness_state,
        capacity,
        increment,
    )
    if lifetime is None:
        return WitnessExhaustionEvent(None, None, ())

    state = tuple(witness_state)
    limits = tuple(capacity)
    step = tuple(increment)
    bottlenecks = tuple(
        index
        for index, (value, limit, delta) in enumerate(
            zip(state, limits, step, strict=True)
        )
        if delta > 0 and (limit - value) // delta == lifetime
    )
    if not bottlenecks:
        raise AssertionError("finite lifetime must have a bottleneck contact")
    return WitnessExhaustionEvent(
        safe_completed_repetitions=lifetime,
        first_exhaustion_attempt=lifetime + 1,
        bottleneck_contacts=bottlenecks,
    )


@dataclass(frozen=True)
class ContactRemovalTopologyReport:
    removed_contacts: tuple[int, ...]
    before_component_count: int
    after_component_count: int
    before_cycle_rank: int
    after_cycle_rank: int
    component_increase: int
    cycle_rank_drop: int

    @property
    def disconnects_graph_further(self) -> bool:
        return self.component_increase > 0


def contact_removal_topology_report(
    num_vertices: int,
    edges: Iterable[Sequence[int]],
    removed: Iterable[int],
) -> ContactRemovalTopologyReport:
    graph = _graph(num_vertices, edges)
    removed_indices = _removed_indices(removed, len(graph))
    before_components = contact_component_count(num_vertices, graph)
    after_components = contact_component_count(
        num_vertices,
        graph,
        removed_indices,
    )
    before_rank = contact_cycle_rank(num_vertices, graph)
    after_rank = contact_cycle_rank(
        num_vertices,
        graph,
        removed_indices,
    )
    component_increase = after_components - before_components
    cycle_drop = before_rank - after_rank
    if cycle_drop != len(removed_indices) - component_increase:
        raise AssertionError("cycle-rank removal identity failed")
    return ContactRemovalTopologyReport(
        removed_contacts=removed_indices,
        before_component_count=before_components,
        after_component_count=after_components,
        before_cycle_rank=before_rank,
        after_cycle_rank=after_rank,
        component_increase=component_increase,
        cycle_rank_drop=cycle_drop,
    )


@dataclass(frozen=True)
class ExhaustionTopologySpectrum:
    exhaustion: WitnessExhaustionEvent
    simultaneous_bottleneck_removal: ContactRemovalTopologyReport | None
    single_bottleneck_removals: tuple[ContactRemovalTopologyReport, ...]

    @property
    def topology_selector_is_required(self) -> bool:
        return len(self.exhaustion.bottleneck_contacts) > 1


def first_exhaustion_topology_spectrum(
    num_vertices: int,
    edges: Iterable[Sequence[int]],
    witness_state: Sequence[int],
    capacity: Sequence[int],
    increment: Sequence[int],
) -> ExhaustionTopologySpectrum:
    graph = _graph(num_vertices, edges)
    if not (
        len(witness_state) == len(capacity) == len(increment) == len(graph)
    ):
        raise ValueError(
            "witness state, capacity, increment, and contact graph must have one entry per contact"
        )
    exhaustion = first_witness_exhaustion(
        witness_state,
        capacity,
        increment,
    )
    if exhaustion.never_exhausts:
        return ExhaustionTopologySpectrum(exhaustion, None, ())

    simultaneous = contact_removal_topology_report(
        num_vertices,
        graph,
        exhaustion.bottleneck_contacts,
    )
    singles = tuple(
        contact_removal_topology_report(
            num_vertices,
            graph,
            (contact,),
        )
        for contact in exhaustion.bottleneck_contacts
    )
    return ExhaustionTopologySpectrum(
        exhaustion,
        simultaneous,
        singles,
    )


def active_edges_after_removal(
    edges: Iterable[Sequence[int]],
    removed: Iterable[int],
) -> tuple[Edge, ...]:
    graph = tuple(tuple(edge) for edge in edges)
    if not graph:
        return ()
    vertex_bound = 1 + max(max(edge) for edge in graph)
    normalized = _graph(vertex_bound, graph)
    removed_set = set(_removed_indices(removed, len(normalized)))
    return tuple(
        edge
        for index, edge in enumerate(normalized)
        if index not in removed_set
    )
