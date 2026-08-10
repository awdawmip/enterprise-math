"""Ehrhart/root-polytope theory as a counting shadow of conservative transfer balls.

For a slot-transfer graph G with oriented incidence columns b_e, the primitive
word norm on the incidence lattice is

    ||x||_G = min { sum |z_e| : B z = x, z integral }.

The real linear-programming relaxation is the gauge of the symmetric edge
polytope P_G=conv{+/- b_e}.  Incidence matrices are totally unimodular; after
splitting z=z^+-z^-, every integer right-hand side has an integral optimal basic
solution.  Hence for integer relation states

    ||x||_G <= r  iff  x in r P_G,

so the word ball is exactly the lattice points of the polytope dilation.  The
traditional Ehrhart polynomial is therefore a counting shadow of primitive
causal operation budget.  Its degree equals the incidence-lattice rank N-c(G).

Symmetric edge polytopes, total unimodularity, and Ehrhart theory are mature
prior art.  The project contribution is the causal ordering and bridges to P008,
P012, P019, and relation-boundary contraction.
"""

from __future__ import annotations

from .causal_transfer_boundary_contraction import word_ball
from .causal_transfer_graph_geometry import Edge, transfer_relation_rank


def transfer_ball_count(slot_count: int, edges: tuple[Edge, ...], radius: int) -> int:
    return len(word_ball(slot_count, edges, radius))


def ball_growth_sequence(
    slot_count: int,
    edges: tuple[Edge, ...],
    maximum_radius: int,
) -> tuple[int, ...]:
    if isinstance(maximum_radius, bool) or not isinstance(maximum_radius, int) or maximum_radius < 0:
        raise ValueError("maximum_radius must be a non-negative integer")
    return tuple(transfer_ball_count(slot_count, edges, radius) for radius in range(maximum_radius + 1))


def forward_difference(values: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(right - left for left, right in zip(values, values[1:]))


def difference_table(values: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    table = [values]
    current = values
    while len(current) > 1:
        current = forward_difference(current)
        table.append(current)
    return tuple(table)


def exact_polynomial_degree_from_samples(values: tuple[int, ...]) -> int | None:
    """Return first difference order that is constant, if enough samples expose it."""
    if len(values) < 2:
        return 0
    current = values
    for degree in range(len(values)):
        if len(set(current)) == 1:
            return degree
        current = forward_difference(current)
        if not current:
            break
    return None


def transfer_growth_rank_matches_difference_degree(
    slot_count: int,
    edges: tuple[Edge, ...],
) -> bool:
    rank = transfer_relation_rank(slot_count, edges)
    # A degree-r Ehrhart polynomial is determined by r+1 values.  Two extra
    # samples make the constant r-th difference visible without interpolation.
    values = ball_growth_sequence(slot_count, edges, rank + 2)
    degree = exact_polynomial_degree_from_samples(values)
    return degree == rank


def shell_growth_sequence(
    slot_count: int,
    edges: tuple[Edge, ...],
    maximum_radius: int,
) -> tuple[int, ...]:
    balls = ball_growth_sequence(slot_count, edges, maximum_radius)
    return (1,) + tuple(balls[radius] - balls[radius - 1] for radius in range(1, len(balls)))


def ehrhart_shadow_statement(slot_count: int, edges: tuple[Edge, ...]) -> tuple[int, int]:
    """Return `(relation_rank, ball_growth_degree)` from executable finite differences."""
    rank = transfer_relation_rank(slot_count, edges)
    values = ball_growth_sequence(slot_count, edges, rank + 2)
    degree = exact_polynomial_degree_from_samples(values)
    if degree is None:
        raise AssertionError("finite sample did not expose a polynomial growth degree")
    return rank, degree
