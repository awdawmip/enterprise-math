"""Current ledger precision induced by a family of possible future transfer graphs.

A transfer graph partitions material ledger compartments into connected
components.  As long as the future only uses transfers inside that graph and
observes graph-invariant linear histories, one component total per connected
component is sufficient.

That current quotient can become unsafe if the declared future operation
language may later change the transfer graph.  Removing policy edges can split a
current component and make previously hidden compartment detail observable.

Given a finite family of possible future transfer graphs ``G_1,...,G_k``, define
an equivalence relation on compartments by

    u ~_future v
      iff u and v lie in the same connected component of every G_i.

This is the common refinement (meet) of the future component partitions.  The
minimal current additive ledger state capable of reconstructing every future
graph's component totals is one total per ``~_future`` block.

Why it is sufficient: every component of every future graph is a union of meet
blocks, so its total is the sum of their retained totals.

Why it is necessary: if two compartments are merged despite being separated by
some future graph, place one whole quantum in either compartment.  The merged
candidate state is identical, while that future graph assigns the quantum to
different component totals.

Hence a precision choice based only on the **current** transfer graph is safe
only if every declared future transfer graph preserves its component
identifications.  Future policy/topology changes can require finer state now.

This is finite partition refinement / graph connectivity, not a new generic
future-quotient theorem.  It is the material-ledger specialization of the P023
principle that current compression is relative to the whole declared future
operation language.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Hashable, Iterable, Mapping, Sequence

from .material_ledger_transfer_graph import (
    TransferEdge,
    transfer_graph_components,
)


Compartment = Hashable


def _vertices(values: Iterable[Compartment]) -> tuple[Compartment, ...]:
    result = tuple(values)
    if not result:
        raise ValueError("at least one compartment is required")
    if len(set(result)) != len(result):
        raise ValueError("compartment names must be unique")
    return result


def _future_graphs(
    values: Sequence[Iterable[TransferEdge]],
) -> tuple[tuple[TransferEdge, ...], ...]:
    result = tuple(tuple(edges) for edges in values)
    if not result:
        raise ValueError("at least one future transfer graph is required")
    return result


def future_transfer_precision_partition(
    compartments: Iterable[Compartment],
    future_transfer_graphs: Sequence[Iterable[TransferEdge]],
) -> tuple[frozenset[Compartment], ...]:
    """Meet of all future transfer-component partitions."""
    vertices = _vertices(compartments)
    graphs = _future_graphs(future_transfer_graphs)
    component_maps = []
    for edges in graphs:
        components = transfer_graph_components(vertices, edges)
        component_maps.append(
            {
                vertex: component
                for component in components
                for vertex in component
            }
        )

    groups: dict[tuple[frozenset[Compartment], ...], set[Compartment]] = {}
    for vertex in vertices:
        signature = tuple(mapping[vertex] for mapping in component_maps)
        groups.setdefault(signature, set()).add(vertex)
    return tuple(
        sorted(
            (frozenset(group) for group in groups.values()),
            key=lambda block: tuple(sorted(map(repr, block))),
        )
    )


def future_transfer_precision_signature(
    compartments: Iterable[Compartment],
    future_transfer_graphs: Sequence[Iterable[TransferEdge]],
    ledger: Mapping[Compartment, int],
) -> tuple[int, ...]:
    """Minimal additive current state: total content in each future-meet block."""
    vertices = _vertices(compartments)
    if set(ledger) != set(vertices):
        raise ValueError("ledger must define exactly one value per compartment")
    for value in ledger.values():
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError("ledger entries must be nonnegative integers")
    partition = future_transfer_precision_partition(
        vertices,
        future_transfer_graphs,
    )
    return tuple(sum(ledger[vertex] for vertex in block) for block in partition)


def reconstruct_future_component_totals(
    compartments: Iterable[Compartment],
    future_transfer_graphs: Sequence[Iterable[TransferEdge]],
    ledger: Mapping[Compartment, int],
    future_graph_index: int,
) -> tuple[int, ...]:
    """Reconstruct one future graph's component totals from the meet-block state."""
    vertices = _vertices(compartments)
    graphs = _future_graphs(future_transfer_graphs)
    if isinstance(future_graph_index, bool) or not isinstance(future_graph_index, int):
        raise TypeError("future_graph_index must be an integer")
    if not 0 <= future_graph_index < len(graphs):
        raise ValueError("future_graph_index is outside the declared family")
    if set(ledger) != set(vertices):
        raise ValueError("ledger must define exactly one value per compartment")

    meet = future_transfer_precision_partition(vertices, graphs)
    meet_totals = {
        block: sum(ledger[vertex] for vertex in block)
        for block in meet
    }
    future_components = transfer_graph_components(
        vertices,
        graphs[future_graph_index],
    )
    reconstructed = tuple(
        sum(
            total
            for block, total in meet_totals.items()
            if block.issubset(component)
        )
        for component in future_components
    )
    direct = tuple(
        sum(ledger[vertex] for vertex in component)
        for component in future_components
    )
    if reconstructed != direct:
        raise AssertionError("future meet-block totals failed to reconstruct component totals")
    return reconstructed


def compartments_future_indistinguishable(
    compartments: Iterable[Compartment],
    future_transfer_graphs: Sequence[Iterable[TransferEdge]],
    left: Compartment,
    right: Compartment,
) -> bool:
    """Whether two unit ledger placements stay in one component in every future graph."""
    vertices = _vertices(compartments)
    if left not in vertices or right not in vertices:
        raise ValueError("compartment is outside the declared ledger")
    partition = future_transfer_precision_partition(
        vertices,
        future_transfer_graphs,
    )
    return any(left in block and right in block for block in partition)


@dataclass(frozen=True)
class FutureTransferPrecisionReport:
    current_components: tuple[frozenset[Compartment], ...]
    future_meet_components: tuple[frozenset[Compartment], ...]
    current_invariant_rank: int
    required_future_safe_rank: int
    current_component_totals_are_future_safe: bool


def future_transfer_precision_report(
    compartments: Iterable[Compartment],
    current_transfer_graph: Iterable[TransferEdge],
    future_transfer_graphs: Sequence[Iterable[TransferEdge]],
) -> FutureTransferPrecisionReport:
    vertices = _vertices(compartments)
    current_components = transfer_graph_components(
        vertices,
        tuple(current_transfer_graph),
    )
    future_meet = future_transfer_precision_partition(
        vertices,
        future_transfer_graphs,
    )

    current_map = {
        vertex: component
        for component in current_components
        for vertex in component
    }
    safe = all(
        all(current_map[vertex] == current_map[next(iter(block))] for vertex in block)
        for block in future_meet
    ) and all(
        any(current_component.issubset(block) for block in future_meet)
        for current_component in current_components
    )
    # The compact criterion above is intentionally checked against the direct
    # partition relation below: current component totals are sufficient exactly
    # when every current component is already a union-free block of the future meet,
    # i.e. the future meet does not split any current component.
    direct_safe = all(
        any(current_component.issubset(block) for block in future_meet)
        for current_component in current_components
    )
    if safe != direct_safe:
        raise AssertionError("future transfer precision safety criteria disagreed")

    return FutureTransferPrecisionReport(
        current_components=current_components,
        future_meet_components=future_meet,
        current_invariant_rank=len(current_components),
        required_future_safe_rank=len(future_meet),
        current_component_totals_are_future_safe=direct_safe,
    )
