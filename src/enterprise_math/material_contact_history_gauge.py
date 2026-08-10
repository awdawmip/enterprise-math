"""Gauge invariance of spanning-forest contact history repair coordinates.

The minimal history bridge writes delivered contact history as

    j = s(Bj) + z,       z in ker B,

using one spanning-forest section ``s`` of the body-incidence map, then stores
only ``rho_s=Cz``.  The section is a coordinate choice, not physical structure.

For two spanning-forest sections ``s`` and ``t`` on the same contact graph,

    rho_t = rho_s + C(s(b)-t(b)),       b=Bj.

The gauge correction depends only on already-retained body state ``b``.  Hence
``(b,delta,rho_s)`` and ``(b,delta,rho_t)`` are deterministically equivalent
predictive states.

Contact-event repair generators transform covariantly as well.  For one
integer delivered quantum on edge ``e``:

    g_e^s = C(e-s(Be)),
    g_e^t = g_e^s + C(s(Be)-t(Be)).

Because each tree section is integer-linear in ``b``, this coordinate change
commutes with future contact carries.  Which edges look like ``tree`` versus
``chord`` therefore depends on gauge, but exact reconstructed witness values and
future behavior do not.

Spanning-tree gauges and integer flow sections are standard graph algebra.  The
project value is making the nonphysical coordinate dependence explicit in the
E001/P023 history repair state.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Sequence

from .contact_cycle_witness_repair import (
    apply_integer_matrix,
    fundamental_cycle_lattice,
)


Matrix = tuple[tuple[int, ...], ...]
Vector = tuple[int, ...]


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _incidence(incidence: Sequence[Sequence[int]]) -> Matrix:
    rows = tuple(tuple(row) for row in incidence)
    fundamental_cycle_lattice(rows)
    return rows


def _vector(values: Sequence[int], length: int, *, name: str) -> Vector:
    result = tuple(values)
    if len(result) != length:
        raise ValueError(f"{name} must have length {length}")
    for value in result:
        _require_int(name, value)
    return result


def _witness_matrix(
    witness_matrix: Sequence[Sequence[int]],
    edge_count: int,
) -> Matrix:
    rows = tuple(tuple(row) for row in witness_matrix)
    if not rows:
        raise ValueError("witness_matrix must contain at least one row")
    if any(len(row) != edge_count for row in rows):
        raise ValueError("witness_matrix must match contact count")
    for row in rows:
        for value in row:
            _require_int("witness entry", value)
    return rows


def _edge_endpoints(incidence: Matrix, edge: int) -> tuple[int, int]:
    source = next(
        body
        for body, row in enumerate(incidence)
        if row[edge] == -1
    )
    target = next(
        body
        for body, row in enumerate(incidence)
        if row[edge] == 1
    )
    return source, target


def _chosen_spanning_forest(
    incidence: Matrix,
    tree_edges: Sequence[int],
) -> tuple[int, ...]:
    body_count = len(incidence)
    edge_count = len(incidence[0])
    chosen = tuple(tree_edges)
    if len(set(chosen)) != len(chosen):
        raise ValueError("tree_edges must be distinct")
    for edge in chosen:
        _require_int("tree_edge", edge)
        if not 0 <= edge < edge_count:
            raise ValueError("tree_edge is outside the contact set")

    parent = list(range(body_count))
    rank = [0] * body_count

    def find(body: int) -> int:
        while parent[body] != body:
            parent[body] = parent[parent[body]]
            body = parent[body]
        return body

    def union(left: int, right: int) -> bool:
        left_root = find(left)
        right_root = find(right)
        if left_root == right_root:
            return False
        if rank[left_root] < rank[right_root]:
            left_root, right_root = right_root, left_root
        parent[right_root] = left_root
        if rank[left_root] == rank[right_root]:
            rank[left_root] += 1
        return True

    for edge in chosen:
        source, target = _edge_endpoints(incidence, edge)
        if not union(source, target):
            raise ValueError("tree_edges contain a cycle")

    original_components = fundamental_cycle_lattice(
        incidence
    ).component_count
    chosen_components = len({find(body) for body in range(body_count)})
    if chosen_components != original_components:
        raise ValueError("tree_edges do not span every contact component")
    return chosen


def tree_section_from_chosen_forest(
    incidence: Sequence[Sequence[int]],
    body_delta: Sequence[int],
    tree_edges: Sequence[int],
) -> Vector:
    """Integer body-delta section supported on an explicitly chosen forest."""
    matrix = _incidence(incidence)
    body_count = len(matrix)
    edge_count = len(matrix[0])
    target = _vector(body_delta, body_count, name="body_delta")
    chosen = _chosen_spanning_forest(matrix, tree_edges)

    adjacency: list[list[tuple[int, int]]] = [
        [] for _ in range(body_count)
    ]
    for edge in chosen:
        source, sink = _edge_endpoints(matrix, edge)
        adjacency[source].append((sink, edge))
        adjacency[sink].append((source, edge))

    parent: list[int | None] = [None] * body_count
    parent_edge: list[int | None] = [None] * body_count
    root_of: list[int | None] = [None] * body_count
    order: list[int] = []

    for root in range(body_count):
        if parent[root] is not None:
            continue
        parent[root] = root
        root_of[root] = root
        queue: deque[int] = deque([root])
        while queue:
            current = queue.popleft()
            order.append(current)
            for neighbor, edge in adjacency[current]:
                if parent[neighbor] is not None:
                    continue
                parent[neighbor] = current
                parent_edge[neighbor] = edge
                root_of[neighbor] = root
                queue.append(neighbor)

    subtree = list(target)
    flows = [0] * edge_count
    for vertex in reversed(order):
        root = root_of[vertex]
        if root is None:
            raise AssertionError("forest traversal lost component root")
        if vertex == root:
            if subtree[vertex] != 0:
                raise ValueError(
                    "body_delta is not balanced inside a contact component"
                )
            continue
        ancestor = parent[vertex]
        edge = parent_edge[vertex]
        if ancestor is None or edge is None:
            raise AssertionError("forest traversal lost parent edge")
        source, sink = _edge_endpoints(matrix, edge)
        flows[edge] = (
            subtree[vertex]
            if (source, sink) == (ancestor, vertex)
            else -subtree[vertex]
        )
        subtree[ancestor] += subtree[vertex]

    result = tuple(flows)
    if apply_integer_matrix(matrix, result) != target:
        raise AssertionError("chosen forest section failed to reproduce body delta")
    chosen_set = set(chosen)
    if any(
        result[edge] != 0
        for edge in range(edge_count)
        if edge not in chosen_set
    ):
        raise AssertionError("chosen forest section used an off-forest edge")
    return result


def repair_coordinate_with_forest(
    incidence: Sequence[Sequence[int]],
    witness_matrix: Sequence[Sequence[int]],
    delivered_impulse: Sequence[int],
    tree_edges: Sequence[int],
) -> Vector:
    """Return ``C(j-s_T(Bj))`` in one explicit spanning-forest gauge."""
    matrix = _incidence(incidence)
    edge_count = len(matrix[0])
    witness = _witness_matrix(witness_matrix, edge_count)
    delivered = _vector(
        delivered_impulse,
        edge_count,
        name="delivered_impulse",
    )
    body_delta = apply_integer_matrix(matrix, delivered)
    section = tree_section_from_chosen_forest(
        matrix,
        body_delta,
        tree_edges,
    )
    cycle = tuple(
        value - base
        for value, base in zip(delivered, section, strict=True)
    )
    if any(apply_integer_matrix(matrix, cycle)):
        raise AssertionError("forest repair coordinate left the cycle kernel")
    return apply_integer_matrix(witness, cycle)


def repair_gauge_correction(
    incidence: Sequence[Sequence[int]],
    witness_matrix: Sequence[Sequence[int]],
    body_delta: Sequence[int],
    from_tree_edges: Sequence[int],
    to_tree_edges: Sequence[int],
) -> Vector:
    """Body-state-only translation carrying one repair gauge to another."""
    matrix = _incidence(incidence)
    witness = _witness_matrix(witness_matrix, len(matrix[0]))
    source = tree_section_from_chosen_forest(
        matrix,
        body_delta,
        from_tree_edges,
    )
    target = tree_section_from_chosen_forest(
        matrix,
        body_delta,
        to_tree_edges,
    )
    difference = tuple(
        source_value - target_value
        for source_value, target_value in zip(
            source,
            target,
            strict=True,
        )
    )
    if any(apply_integer_matrix(matrix, difference)):
        raise AssertionError("gauge correction section difference is not a cycle")
    return apply_integer_matrix(witness, difference)


@dataclass(frozen=True)
class RepairGaugeTransform:
    body_delta: Vector
    source_repair: Vector
    correction: Vector
    target_repair: Vector


def transform_repair_between_forests(
    incidence: Sequence[Sequence[int]],
    witness_matrix: Sequence[Sequence[int]],
    body_delta: Sequence[int],
    source_repair: Sequence[int],
    from_tree_edges: Sequence[int],
    to_tree_edges: Sequence[int],
) -> RepairGaugeTransform:
    matrix = _incidence(incidence)
    witness = _witness_matrix(witness_matrix, len(matrix[0]))
    body = _vector(body_delta, len(matrix), name="body_delta")
    repair = _vector(
        source_repair,
        len(witness),
        name="source_repair",
    )
    correction = repair_gauge_correction(
        matrix,
        witness,
        body,
        from_tree_edges,
        to_tree_edges,
    )
    target = tuple(
        value + delta
        for value, delta in zip(repair, correction, strict=True)
    )
    return RepairGaugeTransform(
        body_delta=body,
        source_repair=repair,
        correction=correction,
        target_repair=target,
    )


def repair_generators_with_forest(
    incidence: Sequence[Sequence[int]],
    witness_matrix: Sequence[Sequence[int]],
    tree_edges: Sequence[int],
) -> tuple[Vector, ...]:
    """Repair increment of each contact event in one chosen forest gauge."""
    matrix = _incidence(incidence)
    edge_count = len(matrix[0])
    return tuple(
        repair_coordinate_with_forest(
            matrix,
            witness_matrix,
            tuple(
                1 if index == edge else 0
                for index in range(edge_count)
            ),
            tree_edges,
        )
        for edge in range(edge_count)
    )
