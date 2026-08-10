"""State shell versus relation boundary as an exact incidence distinction.

In any unit-word geometry, every directed relation edge leaving B(r) lands in the
outer shell S(r+1).  Therefore the total relation boundary equals the sum, over
outer-shell states, of their number of inward primitive neighbors.

For complete A_(N-1) transfer geometry, a zero-sum shell state y has a positive
support of size a and negative support of size b.  An inward move must reduce one
positive coordinate and increase one negative coordinate, so its inward degree is
exactly a*b.  Combining with the transfer-graph edge-contraction theorem gives

    sum_{y in S_A(r+1)} a(y)b(y)
      = N(N-1) * |B_(A_(N-2))(r)|.

Thus state-shell counting and relation-boundary counting differ by an intrinsic
integer incidence multiplicity, not by a continuous surface element.
"""

from __future__ import annotations

from .causal_transfer_boundary_contraction import (
    total_relation_boundary_count,
    word_ball,
)
from .causal_transfer_graph_geometry import Edge, Vector, complete_transfer_edges, primitive_transfer_moves


def _add(left: Vector, right: Vector) -> Vector:
    return tuple(a + b for a, b in zip(left, right))


def word_shell(slot_count: int, edges: tuple[Edge, ...], radius: int) -> frozenset[Vector]:
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be a non-negative integer")
    if radius == 0:
        return frozenset({(0,) * slot_count})
    outer = word_ball(slot_count, edges, radius)
    inner = word_ball(slot_count, edges, radius - 1)
    return frozenset(outer - inner)


def inward_primitive_degree(
    state: Vector,
    slot_count: int,
    edges: tuple[Edge, ...],
    radius: int,
) -> int:
    if state not in word_shell(slot_count, edges, radius):
        raise ValueError("state must lie in the declared word shell")
    if radius == 0:
        return 0
    inner = word_ball(slot_count, edges, radius - 1)
    moves = primitive_transfer_moves(slot_count, edges)
    return sum(_add(state, move) in inner for move in moves)


def relation_boundary_is_outer_shell_inward_incidence(
    slot_count: int,
    edges: tuple[Edge, ...],
    radius: int,
) -> bool:
    boundary = total_relation_boundary_count(slot_count, edges, radius)
    shell = word_shell(slot_count, edges, radius + 1)
    incidence = sum(
        inward_primitive_degree(state, slot_count, edges, radius + 1)
        for state in shell
    )
    return boundary == incidence


def a_support_signature(state: Vector) -> tuple[int, int, int]:
    if not state or sum(state) != 0:
        raise ValueError("A state must be nonempty and zero-sum")
    positive = sum(value > 0 for value in state)
    negative = sum(value < 0 for value in state)
    zero = len(state) - positive - negative
    return positive, negative, zero


def a_inward_degree_closed_form(state: Vector) -> int:
    positive, negative, _ = a_support_signature(state)
    return positive * negative


def a_inward_degree_identity(state: Vector) -> bool:
    radius = sum(value for value in state if value > 0)
    if radius == 0:
        return a_inward_degree_closed_form(state) == 0
    edges = complete_transfer_edges(len(state))
    return inward_primitive_degree(state, len(state), edges, radius) == a_inward_degree_closed_form(state)


def a_weighted_shell_incidence(slot_count: int, radius: int) -> int:
    edges = complete_transfer_edges(slot_count)
    shell = word_shell(slot_count, edges, radius + 1)
    return sum(a_inward_degree_closed_form(state) for state in shell)


def a_lower_ball_boundary_identity(slot_count: int, radius: int) -> bool:
    if slot_count < 2:
        raise ValueError("slot_count must be at least two")
    left = a_weighted_shell_incidence(slot_count, radius)
    lower_edges = complete_transfer_edges(slot_count - 1)
    lower_ball = len(word_ball(slot_count - 1, lower_edges, radius)) if slot_count > 2 else 2 * radius + 1
    # A0 / one-slot zero-sum ball has one state, not 2r+1.  Handle N=2 separately.
    if slot_count == 2:
        lower_ball = 1
    right = slot_count * (slot_count - 1) * lower_ball
    return left == right
