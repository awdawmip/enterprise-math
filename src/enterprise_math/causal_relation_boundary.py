"""Relation-boundary versus state-boundary observations on A_p graph balls.

For the A_p zero-sum integer graph with primitive directed roots e_i-e_j, let
B_p(r) be the radius-r graph ball.  Counting newly added states gives the usual
shell `|B_p(r)|-|B_p(r-1)|`, which has growth degree p-1 but is not generally an
A_(p-1) ball.

A different causal observation counts directed primitive relations cut by
removing/isolating B_p(r): edges from an inside state to an outside state.  For
each fixed directed root alpha=e_i-e_j, the crossing edges are in bijection with
B_(p-1)(r) by merging the i,j coordinates.  Hence

    E_p,alpha(r)=|B_(p-1)(r)|
    E_p(r)=p(p+1)|B_(p-1)(r)|.

For p=1, define |B_0(r)|=1, so E_1(r)=2.  This is an exact family-lowering
boundary theorem.  It demonstrates that "surface" is observation-dependent:
state shell and cut-relation boundary are both valid finite observations but
only the latter literally reproduces the lower-dimensional ball family here.
"""

from __future__ import annotations

from itertools import product

from .lattice_geometry import a_ball_count, a_graph_distance


def lower_a_ball_count(p_minus_one: int, radius: int) -> int:
    if isinstance(p_minus_one, bool) or not isinstance(p_minus_one, int) or p_minus_one < 0:
        raise ValueError("p_minus_one must be a non-negative integer")
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be a non-negative integer")
    return 1 if p_minus_one == 0 else a_ball_count(p_minus_one, radius)


def per_direction_cut_formula(p: int, radius: int) -> int:
    if isinstance(p, bool) or not isinstance(p, int) or p <= 0:
        raise ValueError("p must be a positive integer")
    return lower_a_ball_count(p - 1, radius)


def total_directed_cut_formula(p: int, radius: int) -> int:
    if isinstance(p, bool) or not isinstance(p, int) or p <= 0:
        raise ValueError("p must be a positive integer")
    return p * (p + 1) * per_direction_cut_formula(p, radius)


def _enumerated_a_ball(p: int, radius: int) -> frozenset[tuple[int, ...]]:
    """Small exact oracle for tests; not intended for large production counts."""
    if isinstance(p, bool) or not isinstance(p, int) or p <= 0:
        raise ValueError("p must be a positive integer")
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be a non-negative integer")
    coordinate_count = p + 1
    result = set()
    for point in product(range(-radius, radius + 1), repeat=coordinate_count):
        if sum(point) != 0:
            continue
        if a_graph_distance(tuple(0 for _ in point), point) <= radius:
            result.add(point)
    return frozenset(result)


def enumerated_directed_cut_counts(
    p: int,
    radius: int,
) -> dict[tuple[int, int], int]:
    """Exact small-box oracle of outgoing cut edges per directed primitive root."""
    ball = _enumerated_a_ball(p, radius)
    coordinate_count = p + 1
    result = {}
    for receiver in range(coordinate_count):
        for donor in range(coordinate_count):
            if receiver == donor:
                continue
            count = 0
            for point in ball:
                target = list(point)
                target[receiver] += 1
                target[donor] -= 1
                if tuple(target) not in ball:
                    count += 1
            result[(receiver, donor)] = count
    return result


def relation_boundary_matches_lower_dimension(p: int, radius: int) -> bool:
    counts = enumerated_directed_cut_counts(p, radius)
    expected = per_direction_cut_formula(p, radius)
    return (
        all(value == expected for value in counts.values())
        and sum(counts.values()) == total_directed_cut_formula(p, radius)
    )
