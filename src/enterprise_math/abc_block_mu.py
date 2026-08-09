"""Exact compressed solver for the first nondegenerate witness radius ``mu``.

At radius ``r``, each integer block has a finite set of reachable arithmetic
derivative values.  Additivity couples only those scalar values.  Wronskian
degeneracy on the compressed relation is exactly the integer scaling line

    (t_a,t_b,t_c) = k*(a,b,c).

Therefore ``mu`` is the first radius whose compressed additive reachable set
contains a point outside that line.  The solver enumerates reachable derivative
*values* per block, not prime-coordinate witness cubes.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd

from .abc_block_floor_line import exact_absorption_floor_access
from .abc_block_value_quotient import block_value_witness_state
from .abc_support import abc_support_state
from .abc_unit_relation import (
    raw_block_derivative_coefficients,
    raw_block_derivative_image_generator,
)


@dataclass(frozen=True)
class MuSolution:
    abc: tuple[int, int, int]
    mu: int
    derivative_values: tuple[int, int, int]
    wronskian: int
    absorption_redundancy: int
    block_radii: tuple[int, int, int]
    floor_access_upper_bound: int


def _primitive_raw_row(n: int) -> tuple[int, tuple[int, ...]]:
    if n == 1:
        return 0, ()
    coefficients = raw_block_derivative_coefficients(n)
    generator = raw_block_derivative_image_generator(n)
    row = tuple(value // generator for _prime, value in coefficients)
    if gcd(*row) != 1:
        raise AssertionError("raw derivative row failed primitive normalization")
    return generator, row


def reachable_block_derivative_values(n: int, radius: int) -> frozenset[int]:
    """Return every raw derivative value reachable with block radius ``<=radius``.

    Dynamic set addition tracks scalar derivative values only.  It does not
    enumerate the Cartesian product of prime-coordinate witness vectors.
    """
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be a non-negative integer")
    if n == 1:
        return frozenset({0})
    generator, row = _primitive_raw_row(n)
    reachable = {0}
    values = range(-radius, radius + 1)
    for coefficient in row:
        reachable = {
            subtotal + coefficient * coordinate
            for subtotal in reachable
            for coordinate in values
        }
    return frozenset(generator * reduced for reduced in reachable)


def degenerate_scaling_parameter(
    a: int, b: int, c: int, derivative_a: int, derivative_b: int
) -> int | None:
    """Return integer ``t`` when the additive compressed state lies on W=0.

    For a primitive relation ``gcd(a,b)=1``, ``a*v=b*u`` forces
    ``u=a*t`` and ``v=b*t``.  Additivity then gives ``t_c=c*t``.
    """
    abc_support_state(a, b, c)
    if a * derivative_b - b * derivative_a != 0:
        return None
    if derivative_a % a or derivative_b % b:
        raise AssertionError("primitive W=0 state failed integer scaling divisibility")
    t_a = derivative_a // a
    t_b = derivative_b // b
    if t_a != t_b:
        raise AssertionError("Wronskian-zero ratios failed to agree")
    return t_a


def compressed_additive_states_at_radius(
    a: int, b: int, c: int, radius: int
) -> tuple[tuple[int, int, int], ...]:
    """Return all additive block-value states reachable within a common radius."""
    abc_support_state(a, b, c)
    values_a = reachable_block_derivative_values(a, radius)
    values_b = reachable_block_derivative_values(b, radius)
    values_c = reachable_block_derivative_values(c, radius)
    states = []
    for u in values_a:
        for v in values_b:
            w = u + v
            if w in values_c:
                states.append((u, v, w))
    return tuple(sorted(states))


def exact_minimum_nondegenerate_witness_radius(a: int, b: int, c: int) -> MuSolution:
    """Return exact arbitrary-support ``mu`` from compressed reachable values.

    The exact floor-access radius ``nu`` supplies a finite nondegenerate upper
    bound.  Radii are scanned from one upward; at each radius only scalar block
    derivative values are combined.  The first additive state outside the
    scaling line is therefore the exact first nondegenerate fine-witness radius.
    """
    abc_support_state(a, b, c)
    upper = exact_absorption_floor_access(a, b, c).nu
    for radius in range(1, upper + 1):
        states = compressed_additive_states_at_radius(a, b, c, radius)
        for u, v, _w in states:
            if degenerate_scaling_parameter(a, b, c, u, v) is not None:
                continue
            state = block_value_witness_state(a, b, c, u, v)
            if state.global_radius != radius:
                # If a state appeared with a strictly smaller exact block cost it
                # would have been present in an earlier reachable-value layer.
                raise AssertionError("first compressed escape did not occur at its exact radius")
            return MuSolution(
                abc=(a, b, c),
                mu=radius,
                derivative_values=state.derivative_values,
                wronskian=state.wronskian,
                absorption_redundancy=state.absorption_redundancy,
                block_radii=state.block_radii,
                floor_access_upper_bound=upper,
            )
    raise AssertionError("floor witness upper bound must eventually escape scaling line")
