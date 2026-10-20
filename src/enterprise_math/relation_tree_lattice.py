"""Sparse spanning-tree coordinates for canonical A3 weighted relation state.

Canonical A3 uses positive integer capacities ``m_i`` and integer state totals
``p_i`` with pair relations

    Z_ij = m_j*p_i - m_i*p_j.

The full skew relation matrix has rational dimension ``N-1``.  This module shows
that any spanning tree supplies exactly those ``N-1`` relation coordinates, and
adding the grand total

    P = sum_i p_i

makes a full-rank integer coordinate map.

For a tree ``T`` with vertex degrees ``deg_T(i)``, the exact image-lattice index
of

    p |-> (P, (Z_e)_{e in T})

inside ambient ``Z^N`` is

    I_T = (sum_i m_i) * product_i m_i^(deg_T(i)-1).

Proof sketch.  Put ``M=diag(m_i)``, write ``p=M q``, and orient the tree with
incidence matrix ``B``.  For edge ``e=(u,v)``, ``Z_e=m_u*m_v*(q_u-q_v)`` up to
orientation sign.  Hence after multiplying the coordinate matrix by ``M``, one
can factor ``m_u*m_v`` from each tree-relation row.  The remaining matrix is
``[m^T; B^T]``.  Every maximal tree-incidence cofactor is ``±1`` with the common
orientation sign, so expansion along ``m^T`` has absolute determinant
``sum_i m_i``.  Dividing by ``det M=product_i m_i`` gives the formula above.

Let

    g = gcd_i(m_i),
    a_i = m_i/g,
    tau = sum_i a_i = (sum_i m_i)/g.

Every A3 relation is divisible by ``g``.  After replacing each tree coordinate
by the primitive relation ``z_e=Z_e/g``, the exact index becomes

    I_T^prim = tau * product_i a_i^(deg_T(i)-1).

Thus the canonical A3 translation period ``tau`` is the unavoidable global
integer-lattice factor left after all local relation quanta have been removed.
Tree topology contributes only the primitive-capacity degree factor.

Since every tree has ``deg_i>=1`` and ``sum_i(deg_i-1)=N-2``, the smallest tree
index is attained by a star centered at a minimum-capacity vertex, while the
largest is attained by a star centered at a maximum-capacity vertex.

If a primitive capacity ``a_c=1`` is available and a primitive star is centered
at ``c``, its relations are

    z_ci = a_i*p_c - p_i.

Then

    p_c = (P + sum_i z_ci) / tau.

Consequently arbitrary integer star relation coordinates are legal exactly when
that numerator is divisible by ``tau``.  In this precision-friendly case the
entire sparse-coordinate legality burden collapses to one global congruence
modulo the canonical translation period.

These are integer-lattice properties of A3 relation state.  No E001 contact or
physical semantics is imported here, and no novelty claim is made relative to
standard incidence/SNF lattice theory.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd

from .relation_lattice import capacity_gcd, primitive_capacity_vector, relation_translation_period

TreeEdge = tuple[int, int]


def _require_capacities(capacities: tuple[int, ...]) -> None:
    if not isinstance(capacities, tuple) or not capacities:
        raise ValueError("capacities must be a nonempty tuple")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value <= 0
        for value in capacities
    ):
        raise ValueError("capacities must be positive integers")


def _require_tree(capacities: tuple[int, ...], edges: tuple[TreeEdge, ...]) -> None:
    _require_capacities(capacities)
    if not isinstance(edges, tuple):
        raise ValueError("edges must be a tuple")
    vertex_count = len(capacities)
    if len(edges) != max(0, vertex_count - 1):
        raise ValueError("a spanning tree must have exactly N-1 edges")
    if vertex_count == 1:
        return

    parent = list(range(vertex_count))

    def find(vertex: int) -> int:
        while parent[vertex] != vertex:
            parent[vertex] = parent[parent[vertex]]
            vertex = parent[vertex]
        return vertex

    def union(left: int, right: int) -> bool:
        left_root = find(left)
        right_root = find(right)
        if left_root == right_root:
            return False
        parent[right_root] = left_root
        return True

    seen: set[tuple[int, int]] = set()
    for edge in edges:
        if not isinstance(edge, tuple) or len(edge) != 2:
            raise ValueError("each tree edge must be an ordered pair")
        left, right = edge
        if any(isinstance(value, bool) or not isinstance(value, int) for value in edge):
            raise ValueError("tree vertices must be integers")
        if not (0 <= left < vertex_count and 0 <= right < vertex_count):
            raise ValueError("tree vertex is outside the capacity domain")
        if left == right:
            raise ValueError("tree edge cannot be a loop")
        key = tuple(sorted((left, right)))
        if key in seen:
            raise ValueError("tree may contain each undirected edge only once")
        seen.add(key)
        if not union(left, right):
            raise ValueError("tree edges contain a cycle")

    root = find(0)
    if any(find(vertex) != root for vertex in range(vertex_count)):
        raise ValueError("tree edges must connect every vertex")


def tree_degrees(
    capacities: tuple[int, ...],
    edges: tuple[TreeEdge, ...],
) -> tuple[int, ...]:
    """Return spanning-tree degrees in vertex order."""
    _require_tree(capacities, edges)
    if len(capacities) == 1:
        return (0,)
    degrees = [0] * len(capacities)
    for left, right in edges:
        degrees[left] += 1
        degrees[right] += 1
    return tuple(degrees)


def tree_relation_coordinates(
    capacities: tuple[int, ...],
    totals: tuple[int, ...],
    edges: tuple[TreeEdge, ...],
    *,
    primitive: bool = False,
) -> tuple[int, ...]:
    """Return ``(grand_total, oriented tree relations)`` as exact integers."""
    _require_tree(capacities, edges)
    if not isinstance(totals, tuple) or len(totals) != len(capacities):
        raise ValueError("totals must match capacities")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in totals):
        raise ValueError("totals must be integers")
    divisor = capacity_gcd(capacities) if primitive else 1
    relations: list[int] = []
    for left, right in edges:
        value = capacities[right] * totals[left] - capacities[left] * totals[right]
        if value % divisor:
            raise AssertionError("A3 relation lost its common capacity quantum")
        relations.append(value // divisor)
    return (sum(totals), *relations)


def tree_relation_lattice_index(
    capacities: tuple[int, ...],
    edges: tuple[TreeEdge, ...],
) -> int:
    """Return exact full-coordinate image index ``I_T``."""
    degrees = tree_degrees(capacities, edges)
    if len(capacities) == 1:
        return 1
    result = sum(capacities)
    for capacity, degree in zip(capacities, degrees):
        result *= capacity ** (degree - 1)
    return result


def primitive_tree_relation_lattice_index(
    capacities: tuple[int, ...],
    edges: tuple[TreeEdge, ...],
) -> int:
    """Return exact image index after dividing every relation by ``gcd(m)``."""
    degrees = tree_degrees(capacities, edges)
    if len(capacities) == 1:
        return 1
    primitive = primitive_capacity_vector(capacities)
    result = relation_translation_period(capacities)
    for capacity, degree in zip(primitive, degrees):
        result *= capacity ** (degree - 1)
    divisor = capacity_gcd(capacities) ** (len(capacities) - 1)
    if tree_relation_lattice_index(capacities, edges) // divisor != result:
        raise AssertionError("primitive tree index disagrees with relation-quantum removal")
    return result


@dataclass(frozen=True)
class TreeRelationIndexExtrema:
    minimum_capacity: int
    maximum_capacity: int
    minimum_centers: tuple[int, ...]
    maximum_centers: tuple[int, ...]
    minimum_index: int
    maximum_index: int
    primitive_minimum_capacity: int
    primitive_maximum_capacity: int
    primitive_minimum_index: int
    primitive_maximum_index: int
    translation_period: int


def tree_relation_index_extrema(capacities: tuple[int, ...]) -> TreeRelationIndexExtrema:
    """Closed min/max index over all spanning trees on the complete vertex set."""
    _require_capacities(capacities)
    if len(capacities) == 1:
        return TreeRelationIndexExtrema(
            minimum_capacity=capacities[0],
            maximum_capacity=capacities[0],
            minimum_centers=(0,),
            maximum_centers=(0,),
            minimum_index=1,
            maximum_index=1,
            primitive_minimum_capacity=1,
            primitive_maximum_capacity=1,
            primitive_minimum_index=1,
            primitive_maximum_index=1,
            translation_period=1,
        )

    minimum = min(capacities)
    maximum = max(capacities)
    total = sum(capacities)
    exponent = len(capacities) - 2
    primitive = primitive_capacity_vector(capacities)
    primitive_min = min(primitive)
    primitive_max = max(primitive)
    tau = relation_translation_period(capacities)
    return TreeRelationIndexExtrema(
        minimum_capacity=minimum,
        maximum_capacity=maximum,
        minimum_centers=tuple(
            index for index, value in enumerate(capacities) if value == minimum
        ),
        maximum_centers=tuple(
            index for index, value in enumerate(capacities) if value == maximum
        ),
        minimum_index=total * minimum**exponent,
        maximum_index=total * maximum**exponent,
        primitive_minimum_capacity=primitive_min,
        primitive_maximum_capacity=primitive_max,
        primitive_minimum_index=tau * primitive_min**exponent,
        primitive_maximum_index=tau * primitive_max**exponent,
        translation_period=tau,
    )


@dataclass(frozen=True)
class PrimitiveStarReconstruction:
    center: int
    primitive_capacities: tuple[int, ...]
    translation_period: int
    grand_total: int
    leaf_relations: tuple[tuple[int, int], ...]
    congruence_numerator: int
    legal: bool
    reconstructed_totals: tuple[int, ...] | None


def reconstruct_primitive_unit_star(
    capacities: tuple[int, ...],
    center: int,
    grand_total: int,
    leaf_relations: tuple[tuple[int, int], ...],
) -> PrimitiveStarReconstruction:
    """Reconstruct a primitive star centered at ``a_center=1`` from one congruence.

    ``leaf_relations`` must contain ``(leaf, z_center_leaf)`` for every noncenter
    vertex exactly once, with the relation oriented from center to leaf:

        z_center_leaf = a_leaf*p_center - p_leaf.
    """
    _require_capacities(capacities)
    if isinstance(center, bool) or not isinstance(center, int) or not 0 <= center < len(capacities):
        raise ValueError("center must be a valid vertex index")
    if isinstance(grand_total, bool) or not isinstance(grand_total, int):
        raise ValueError("grand_total must be an integer")
    primitive = primitive_capacity_vector(capacities)
    if primitive[center] != 1:
        raise ValueError("primitive star reconstruction requires center capacity m/g=1")
    if not isinstance(leaf_relations, tuple):
        raise ValueError("leaf_relations must be a tuple")
    expected_leaves = set(range(len(capacities))) - {center}
    observed: dict[int, int] = {}
    for entry in leaf_relations:
        if not isinstance(entry, tuple) or len(entry) != 2:
            raise ValueError("each leaf relation must be (leaf, primitive_relation)")
        leaf, relation = entry
        if (
            isinstance(leaf, bool)
            or not isinstance(leaf, int)
            or leaf not in expected_leaves
            or leaf in observed
        ):
            raise ValueError("leaf relations must name every noncenter vertex exactly once")
        if isinstance(relation, bool) or not isinstance(relation, int):
            raise ValueError("primitive relation values must be integers")
        observed[leaf] = relation
    if set(observed) != expected_leaves:
        raise ValueError("leaf relations must cover every noncenter vertex")

    tau = relation_translation_period(capacities)
    numerator = grand_total + sum(observed.values())
    legal = numerator % tau == 0
    reconstructed: tuple[int, ...] | None = None
    if legal:
        center_total = numerator // tau
        values = [0] * len(capacities)
        values[center] = center_total
        for leaf, relation in observed.items():
            values[leaf] = primitive[leaf] * center_total - relation
        reconstructed = tuple(values)
        if sum(reconstructed) != grand_total:
            raise AssertionError("primitive star reconstruction lost grand total")
        edges = tuple((center, leaf) for leaf in sorted(expected_leaves))
        coordinates = tree_relation_coordinates(
            capacities,
            reconstructed,
            edges,
            primitive=True,
        )
        expected = (grand_total, *(observed[leaf] for leaf in sorted(expected_leaves)))
        if coordinates != expected:
            raise AssertionError("primitive star reconstruction lost relation coordinates")

    return PrimitiveStarReconstruction(
        center=center,
        primitive_capacities=primitive,
        translation_period=tau,
        grand_total=grand_total,
        leaf_relations=tuple(sorted(observed.items())),
        congruence_numerator=numerator,
        legal=legal,
        reconstructed_totals=reconstructed,
    )
