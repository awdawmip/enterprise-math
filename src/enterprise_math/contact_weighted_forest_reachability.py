"""Exact integer reachability for body-weighted forest contact Grams.

For an oriented contact forest with positive integer body weights ``d_v``, let

    D = diag(d_v),
    K = B^T D B.

The forest has no kernel ambiguity, but integer targets can still fail to lie in
``im_Z K``.  This module gives a constructive criterion without floating-point
or rational matrix inversion as world semantics.

For one tree component, integrate an integer target ``c`` to integer vertex
potentials ``s`` satisfying

    s_head - s_tail = c_e.

If ``K j=c`` and ``y=B j``, then

    D y = s + t*1

for one constant ``t``.  The zero-sum condition on ``y`` uniquely forces

    t = - (sum_v s_v/d_v) / (sum_v 1/d_v).

The target is integer-reachable exactly when this forced ``t`` is an integer and
all ``s_v+t`` are divisible by ``d_v``.  The implementation evaluates the same
criterion with integer lcm weights only.  When it passes, ``y_v=(s_v+t)/d_v``
is an integer zero-sum body vector and the unique impulse is recovered by leaf
peeling ``B j=y``.

For a connected n-body tree, the finite cokernel order is

    det(B^T D B) = sum_r prod_{v != r} d_v.

For a forest, component determinants multiply.  The abstract weighted-tree
cokernel depends only on the vertex weights of each component, not on tree
shape: every tree incidence basis is a unimodular basis of the same A-type root
lattice.  In the common-weight case ``d_v=d`` this specializes to invariant
factors

    d,...,d,n*d

and hence ``(Z/d)^(n-2) direct_sum Z/(n*d)``.  Setting ``d=1`` recovers the
preceding ``Z/n`` forest theorem.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from math import gcd, lcm
from typing import Iterable, Sequence

from .contact_forest_reachability import (
    ForestComponent,
    apply_integer_matrix,
    forest_components,
    forest_incidence_matrix,
    integrated_vertex_potential,
)


Edge = tuple[int, int]
Vector = tuple[int, ...]
Matrix = tuple[tuple[int, ...], ...]


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _positive_weights(values: Sequence[int] | Iterable[int], size: int) -> Vector:
    result = tuple(values)
    if len(result) != size:
        raise ValueError(f"body_weights must have length {size}")
    for value in result:
        _require_int("body weight", value)
        if value <= 0:
            raise ValueError("body weights must be positive")
    return result


def _edges_from_incidence(incidence: Matrix) -> tuple[Edge, ...]:
    if not incidence:
        return ()
    edge_count = len(incidence[0])
    result = []
    for edge in range(edge_count):
        tail = next(
            body for body, row in enumerate(incidence) if row[edge] == -1
        )
        head = next(
            body for body, row in enumerate(incidence) if row[edge] == 1
        )
        result.append((tail, head))
    return tuple(result)


def weighted_forest_contact_gram(
    num_vertices: int,
    edges: Iterable[Sequence[int]],
    body_weights: Sequence[int],
) -> Matrix:
    incidence = forest_incidence_matrix(num_vertices, edges)
    weights = _positive_weights(body_weights, num_vertices)
    edge_count = len(incidence[0]) if incidence else 0
    return tuple(
        tuple(
            sum(
                weights[body]
                * incidence[body][left]
                * incidence[body][right]
                for body in range(num_vertices)
            )
            for right in range(edge_count)
        )
        for left in range(edge_count)
    )


def _lcm_all(values: Iterable[int]) -> int:
    result = 1
    for value in values:
        result = lcm(result, value)
    return result


@dataclass(frozen=True)
class WeightedComponentReachability:
    vertices: tuple[int, ...]
    forced_shift: int | None
    weighted_zero_sum_numerator: int
    reciprocal_weight_sum_numerator: int
    divisible_coordinates: bool
    reachable: bool


def _component_reachability(
    component: ForestComponent,
    potential: Vector,
    weights: Vector,
) -> WeightedComponentReachability:
    component_weights = tuple(weights[v] for v in component.vertices)
    common = _lcm_all(component_weights)
    reciprocal_coefficients = tuple(
        common // weight for weight in component_weights
    )
    denominator = sum(reciprocal_coefficients)
    numerator = sum(
        potential[vertex] * coefficient
        for vertex, coefficient in zip(
            component.vertices,
            reciprocal_coefficients,
            strict=True,
        )
    )

    if numerator % denominator:
        return WeightedComponentReachability(
            component.vertices,
            None,
            numerator,
            denominator,
            False,
            False,
        )
    forced_shift = -numerator // denominator
    divisible = all(
        (potential[vertex] + forced_shift) % weights[vertex] == 0
        for vertex in component.vertices
    )
    return WeightedComponentReachability(
        component.vertices,
        forced_shift,
        numerator,
        denominator,
        divisible,
        divisible,
    )


def weighted_forest_component_reachability(
    num_vertices: int,
    edges: Iterable[Sequence[int]],
    body_weights: Sequence[int],
    target: Sequence[int],
) -> tuple[WeightedComponentReachability, ...]:
    incidence = forest_incidence_matrix(num_vertices, edges)
    graph = _edges_from_incidence(incidence)
    weights = _positive_weights(body_weights, num_vertices)
    if len(target) != len(graph):
        raise ValueError("target must have one value per contact")
    for value in target:
        _require_int("target", value)
    potential = integrated_vertex_potential(
        num_vertices,
        graph,
        target,
    )
    return tuple(
        _component_reachability(component, potential, weights)
        for component in forest_components(num_vertices, graph)
    )


def weighted_forest_target_is_reachable(
    num_vertices: int,
    edges: Iterable[Sequence[int]],
    body_weights: Sequence[int],
    target: Sequence[int],
) -> bool:
    return all(
        report.reachable
        for report in weighted_forest_component_reachability(
            num_vertices,
            edges,
            body_weights,
            target,
        )
    )


def _solve_forest_body_vector(
    num_vertices: int,
    graph: tuple[Edge, ...],
    body_vector: Vector,
) -> Vector:
    residual = list(body_vector)
    adjacency: list[list[tuple[int, int]]] = [
        [] for _ in range(num_vertices)
    ]
    for edge, (tail, head) in enumerate(graph):
        adjacency[tail].append((head, edge))
        adjacency[head].append((tail, edge))
    alive = [True] * num_vertices
    degree = [len(row) for row in adjacency]
    counts: list[int | None] = [None] * len(graph)
    queue: deque[int] = deque(
        vertex for vertex, value in enumerate(degree) if value <= 1
    )
    while queue:
        vertex = queue.popleft()
        if not alive[vertex]:
            continue
        neighbors = [
            pair for pair in adjacency[vertex] if alive[pair[0]]
        ]
        if len(neighbors) > 1:
            continue
        if not neighbors:
            if residual[vertex] != 0:
                raise ValueError("body vector does not sum to zero on a component")
            alive[vertex] = False
            continue
        other, edge = neighbors[0]
        tail, _ = graph[edge]
        sign_here = -1 if vertex == tail else 1
        count = sign_here * residual[vertex]
        counts[edge] = count
        sign_other = -1 if other == tail else 1
        residual[vertex] -= sign_here * count
        residual[other] -= sign_other * count
        alive[vertex] = False
        degree[other] -= 1
        if degree[other] <= 1:
            queue.append(other)
    if any(residual) or any(value is None for value in counts):
        raise ValueError("forest body-vector solve did not close")
    return tuple(int(value) for value in counts)


def solve_weighted_forest_contact_target(
    num_vertices: int,
    edges: Iterable[Sequence[int]],
    body_weights: Sequence[int],
    target: Sequence[int],
) -> Vector | None:
    incidence = forest_incidence_matrix(num_vertices, edges)
    graph = _edges_from_incidence(incidence)
    weights = _positive_weights(body_weights, num_vertices)
    if len(target) != len(graph):
        raise ValueError("target must have one value per contact")
    potential = integrated_vertex_potential(
        num_vertices,
        graph,
        target,
    )
    reports = weighted_forest_component_reachability(
        num_vertices,
        graph,
        weights,
        target,
    )
    if not all(report.reachable for report in reports):
        return None

    body = [0] * num_vertices
    report_by_vertex = {
        vertex: report
        for report in reports
        for vertex in report.vertices
    }
    for vertex in range(num_vertices):
        shift = report_by_vertex[vertex].forced_shift
        assert shift is not None
        numerator = potential[vertex] + shift
        if numerator % weights[vertex]:
            raise AssertionError("reachable coordinate lost divisibility")
        body[vertex] = numerator // weights[vertex]

    impulse = _solve_forest_body_vector(
        num_vertices,
        graph,
        tuple(body),
    )
    gram = weighted_forest_contact_gram(
        num_vertices,
        graph,
        weights,
    )
    if apply_integer_matrix(gram, impulse) != tuple(target):
        raise AssertionError("constructed weighted forest impulse missed target")
    return impulse


def weighted_tree_determinant(
    weights: Sequence[int] | Iterable[int],
) -> int:
    """Closed determinant ``sum_r prod_{v!=r} d_v`` for one tree component."""
    values = tuple(weights)
    if not values:
        raise ValueError("weights must be nonempty")
    _positive_weights(values, len(values))
    if len(values) == 1:
        return 1
    result = 0
    for omitted in range(len(values)):
        product_value = 1
        for index, value in enumerate(values):
            if index != omitted:
                product_value *= value
        result += product_value
    return result


def weighted_forest_contact_gram_determinant(
    num_vertices: int,
    edges: Iterable[Sequence[int]],
    body_weights: Sequence[int],
) -> int:
    incidence = forest_incidence_matrix(num_vertices, edges)
    graph = _edges_from_incidence(incidence)
    weights = _positive_weights(body_weights, num_vertices)
    result = 1
    for component in forest_components(num_vertices, graph):
        result *= weighted_tree_determinant(
            tuple(weights[v] for v in component.vertices)
        )
    return result


def common_weight_tree_cokernel_invariant_factors(
    body_count: int,
    common_weight: int,
) -> tuple[int, ...]:
    """SNF factors for any connected tree with one common positive body weight."""
    _require_int("body_count", body_count)
    _require_int("common_weight", common_weight)
    if body_count <= 1:
        raise ValueError("body_count must be at least two")
    if common_weight <= 0:
        raise ValueError("common_weight must be positive")
    return (
        (common_weight,) * (body_count - 2)
        + (body_count * common_weight,)
    )


@dataclass(frozen=True)
class WeightedForestReachabilityReport:
    component_reports: tuple[WeightedComponentReachability, ...]
    determinant: int
    reachable: bool
    unique_integer_impulse: Vector | None


def weighted_forest_reachability_report(
    num_vertices: int,
    edges: Iterable[Sequence[int]],
    body_weights: Sequence[int],
    target: Sequence[int],
) -> WeightedForestReachabilityReport:
    component_reports = weighted_forest_component_reachability(
        num_vertices,
        edges,
        body_weights,
        target,
    )
    impulse = solve_weighted_forest_contact_target(
        num_vertices,
        edges,
        body_weights,
        target,
    )
    return WeightedForestReachabilityReport(
        component_reports=component_reports,
        determinant=weighted_forest_contact_gram_determinant(
            num_vertices,
            edges,
            body_weights,
        ),
        reachable=impulse is not None,
        unique_integer_impulse=impulse,
    )
