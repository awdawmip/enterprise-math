"""Exact positive-rational BRC gauge and prime-valuation holonomy calculus.

The module implements the main-backed PR #1132-#1133 results.  Rational gauge
classes are represented primewise before any logarithmic readout; mod-m shadows
and complementary m-th-power thickness remain exact integer/rational objects.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from typing import Sequence

from .exact_arithmetic import BRCRootTrace, brc_root_integer_value, root

RationalInput = int | Fraction
RationalEdge = tuple[int, int, RationalInput]


def _fraction(value: RationalInput) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError("value must be int or Fraction")
    result = Fraction(value)
    if result <= 0:
        raise ValueError("rational holonomy values must be positive")
    return result


def _factor_positive_integer(value: int) -> dict[int, int]:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError("positive integer required")
    result: dict[int, int] = {}
    x = value
    p = 2
    while p * p <= x:
        while x % p == 0:
            result[p] = result.get(p, 0) + 1
            x //= p
        p = 3 if p == 2 else p + 2
    if x > 1:
        result[x] = result.get(x, 0) + 1
    return result


def prime_valuations(value: RationalInput) -> tuple[tuple[int, int], ...]:
    """Return finite-support prime valuations of a positive rational."""
    q = _fraction(value)
    result = _factor_positive_integer(q.numerator)
    for prime, exponent in _factor_positive_integer(q.denominator).items():
        result[prime] = result.get(prime, 0) - exponent
        if result[prime] == 0:
            del result[prime]
    return tuple(sorted(result.items()))


def _reconstruct_valuations(data: dict[int, int]) -> Fraction:
    result = Fraction(1, 1)
    for prime, exponent in sorted(data.items()):
        if exponent >= 0:
            result *= prime**exponent
        else:
            result /= prime ** (-exponent)
    return result


@dataclass(frozen=True)
class PowerThickness:
    """Unique ``q = skeleton * thickness**degree`` decomposition."""

    source: Fraction
    degree: int
    skeleton: int
    thickness: Fraction

    def reconstruct(self) -> Fraction:
        return Fraction(self.skeleton, 1) * self.thickness**self.degree

    def brc_root_materialization(self) -> tuple[Fraction, BRCRootTrace, BRCRootTrace]:
        """Verify/materialize the residual degree-th root through BRC ROOT traces."""
        residual = self.source / self.skeleton
        numerator, numerator_trace = brc_root_integer_value(
            root(residual.numerator, self.degree)
        )
        denominator, denominator_trace = brc_root_integer_value(
            root(residual.denominator, self.degree)
        )
        result = Fraction(numerator, denominator)
        if result != self.thickness:
            raise AssertionError("BRC ROOT materialization disagrees with valuation thickness")
        return result, numerator_trace, denominator_trace


def m_power_free_thickness(value: RationalInput, degree: int) -> PowerThickness:
    """Return the unique positive m-power-free skeleton plus rational thickness."""
    if isinstance(degree, bool) or not isinstance(degree, int) or degree < 2:
        raise ValueError("degree must be an integer >= 2")
    q = _fraction(value)
    skeleton = 1
    quotient_valuations: dict[int, int] = {}
    for prime, exponent in prime_valuations(q):
        quotient, residue = divmod(exponent, degree)
        if residue:
            skeleton *= prime**residue
        if quotient:
            quotient_valuations[prime] = quotient
    thickness = _reconstruct_valuations(quotient_valuations)
    result = PowerThickness(q, degree, skeleton, thickness)
    if result.reconstruct() != q:
        raise AssertionError("m-power thickness failed exact reconstruction")
    return result


def squarefree_thickness(value: RationalInput) -> PowerThickness:
    """Convenience alias for the C2/square-class decomposition."""
    return m_power_free_thickness(value, 2)


def _normalized_edges(
    vertex_count: int, edges: Sequence[RationalEdge]
) -> tuple[tuple[int, int, Fraction], ...]:
    if isinstance(vertex_count, bool) or not isinstance(vertex_count, int) or vertex_count <= 0:
        raise ValueError("vertex_count must be a positive integer")
    result: list[tuple[int, int, Fraction]] = []
    for source, target, weight in edges:
        if (
            isinstance(source, bool)
            or isinstance(target, bool)
            or not isinstance(source, int)
            or not isinstance(target, int)
            or not 0 <= source < vertex_count
            or not 0 <= target < vertex_count
        ):
            raise ValueError("edge endpoints must be valid vertex indices")
        result.append((source, target, _fraction(weight)))
    return tuple(result)


def _validate_tree(
    vertex_count: int,
    edges: tuple[tuple[int, int, Fraction], ...],
    tree_indices: tuple[int, ...],
) -> None:
    if len(tree_indices) != vertex_count - 1 or len(set(tree_indices)) != len(tree_indices):
        raise ValueError("spanning tree must contain exactly vertex_count-1 distinct edges")
    if any(index < 0 or index >= len(edges) for index in tree_indices):
        raise ValueError("tree edge index out of range")
    graph: list[list[int]] = [[] for _ in range(vertex_count)]
    for index in tree_indices:
        source, target, _ = edges[index]
        if source == target:
            raise ValueError("a spanning tree cannot contain a self-loop")
        graph[source].append(target)
        graph[target].append(source)
    seen = {0}
    queue = deque([0])
    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    if len(seen) != vertex_count:
        raise ValueError("selected edges do not form a connected spanning tree")


def _tree_path(
    vertex_count: int,
    edges: tuple[tuple[int, int, Fraction], ...],
    tree_indices: tuple[int, ...],
    start: int,
    target: int,
) -> tuple[tuple[int, int], ...]:
    graph: list[list[tuple[int, int, int]]] = [[] for _ in range(vertex_count)]
    for index in tree_indices:
        source, end, _ = edges[index]
        graph[source].append((end, index, +1))
        graph[end].append((source, index, -1))
    parent: dict[int, tuple[int, int, int] | None] = {start: None}
    queue = deque([start])
    while queue and target not in parent:
        vertex = queue.popleft()
        for neighbor, index, sign in graph[vertex]:
            if neighbor not in parent:
                parent[neighbor] = (vertex, index, sign)
                queue.append(neighbor)
    if target not in parent:
        raise ValueError("tree path does not exist")
    reversed_path: list[tuple[int, int]] = []
    vertex = target
    while vertex != start:
        item = parent[vertex]
        if item is None:
            raise AssertionError("tree parent chain ended early")
        previous, index, sign = item
        reversed_path.append((index, sign))
        vertex = previous
    reversed_path.reverse()
    return tuple(reversed_path)


def fundamental_cycle_holonomy(
    vertex_count: int,
    edges: Sequence[RationalEdge],
    tree_indices: Sequence[int],
    edge_index: int,
) -> Fraction:
    """Return the algebraic fundamental-cycle product of one non-tree edge."""
    normalized = _normalized_edges(vertex_count, edges)
    tree = tuple(tree_indices)
    _validate_tree(vertex_count, normalized, tree)
    if edge_index in set(tree):
        raise ValueError("fundamental coordinate requires a non-tree edge")
    if edge_index < 0 or edge_index >= len(normalized):
        raise ValueError("edge index out of range")
    source, target, result = normalized[edge_index]
    for tree_index, sign in _tree_path(vertex_count, normalized, tree, target, source):
        weight = normalized[tree_index][2]
        result *= weight if sign > 0 else Fraction(1, 1) / weight
    return result


@dataclass(frozen=True)
class TreeGaugeNormalForm:
    """Root/tree-relative complete rational gauge normal form."""

    root: int
    tree_indices: tuple[int, ...]
    vertex_scales: tuple[Fraction, ...]
    normalized_edge_weights: tuple[Fraction, ...]
    non_tree_indices: tuple[int, ...]
    fundamental_holonomies: tuple[Fraction, ...]


def rational_tree_gauge_normal_form(
    vertex_count: int,
    edges: Sequence[RationalEdge],
    tree_indices: Sequence[int],
    root: int = 0,
) -> TreeGaugeNormalForm:
    """Normalize a rational weighted connected graph so every tree edge has weight 1."""
    normalized = _normalized_edges(vertex_count, edges)
    tree = tuple(tree_indices)
    _validate_tree(vertex_count, normalized, tree)
    if isinstance(root, bool) or not isinstance(root, int) or not 0 <= root < vertex_count:
        raise ValueError("root must be a valid vertex index")

    scales: list[Fraction | None] = [None] * vertex_count
    scales[root] = Fraction(1, 1)
    remaining = set(tree)
    while remaining:
        progress = False
        for index in tuple(remaining):
            source, target, weight = normalized[index]
            if scales[source] is not None and scales[target] is None:
                scales[target] = scales[source] / weight
                remaining.remove(index)
                progress = True
            elif scales[target] is not None and scales[source] is None:
                scales[source] = weight * scales[target]
                remaining.remove(index)
                progress = True
            elif scales[source] is not None and scales[target] is not None:
                if weight * scales[target] / scales[source] != 1:
                    raise AssertionError("tree normalization consistency failed")
                remaining.remove(index)
                progress = True
        if not progress:
            raise AssertionError("tree gauge propagation stalled")

    if any(value is None or value <= 0 for value in scales):
        raise AssertionError("tree normalization failed to assign positive scales")
    h = tuple(value for value in scales if value is not None)
    edge_weights = tuple(
        weight * h[target] / h[source]
        for source, target, weight in normalized
    )
    if any(edge_weights[index] != 1 for index in tree):
        raise AssertionError("tree edge failed to normalize to one")
    tree_set = set(tree)
    non_tree = tuple(index for index in range(len(normalized)) if index not in tree_set)
    holonomies = tuple(edge_weights[index] for index in non_tree)
    for index, coordinate in zip(non_tree, holonomies):
        if coordinate != fundamental_cycle_holonomy(vertex_count, normalized, tree, index):
            raise AssertionError("normalized non-tree weight disagrees with fundamental holonomy")
    return TreeGaugeNormalForm(root, tree, h, edge_weights, non_tree, holonomies)


def prime_holonomy_coordinates(
    coordinates: Sequence[RationalInput],
) -> tuple[tuple[int, tuple[int, ...]], ...]:
    """Return prime-indexed integer coordinate vectors for rational holonomies."""
    values = tuple(_fraction(value) for value in coordinates)
    prime_set = sorted({prime for value in values for prime, _ in prime_valuations(value)})
    tables = [dict(prime_valuations(value)) for value in values]
    return tuple(
        (prime, tuple(table.get(prime, 0) for table in tables))
        for prime in prime_set
    )


def mod_m_holonomy_shadow(
    coordinates: Sequence[RationalInput], degree: int
) -> tuple[tuple[int, tuple[int, ...]], ...]:
    """Return the all-prime valuation shadow modulo ``degree``."""
    if isinstance(degree, bool) or not isinstance(degree, int) or degree < 2:
        raise ValueError("degree must be an integer >= 2")
    return tuple(
        (prime, tuple(exponent % degree for exponent in vector))
        for prime, vector in prime_holonomy_coordinates(coordinates)
    )
