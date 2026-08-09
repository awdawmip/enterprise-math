"""Exact affine-line reduction of the P025 absorption-floor access problem.

After the block derivative-value quotient, every non-unit primitive abc triple
has a rank-two lattice

    Lambda = {(u,v): u in A Z, v in B Z, u+v in C Z}.

This module constructs a canonical HNF-like basis of that lattice, restricts the
Wronskian to the basis, and uses Bezout to obtain the full affine line on which
``W=D`` where ``D`` is the positive Wronskian image generator.  Therefore the
arbitrary-support floor-access problem ``nu`` is a one-parameter integer
optimization over exact block access functions.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd, lcm

from .abc_block_value_lattice import block_value_lattice_invariants
from .abc_block_value_quotient import block_value_witness_state
from .abc_support import abc_support_state
from .abc_unit_relation import (
    raw_block_derivative_coefficients,
    raw_block_derivative_image_generator,
)


@dataclass(frozen=True)
class BlockValueFloorLine:
    abc: tuple[int, int, int]
    block_image_generators: tuple[int, int, int]
    basis: tuple[tuple[int, int], ...]
    basis_wronskians: tuple[int, ...]
    wronskian_generator: int
    particular_floor_point: tuple[int, int]
    kernel_direction: tuple[int, int] | None


@dataclass(frozen=True)
class FloorAccessSolution:
    line: BlockValueFloorLine
    derivative_values: tuple[int, int, int]
    block_radii: tuple[int, int, int]
    nu: int
    absorption_floor: int
    searched_parameter_interval: tuple[int, int] | None
    parameter: int | None


def _extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Return positive gcd and Bezout coefficients for arbitrary integers."""
    if b == 0:
        if a >= 0:
            return a, 1, 0
        return -a, -1, 0
    g, x1, y1 = _extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def _block_generator(n: int) -> int:
    if n == 1:
        return 0
    return raw_block_derivative_image_generator(n)


def _wronskian(a: int, b: int, point: tuple[int, int]) -> int:
    u, v = point
    return a * v - b * u


def block_value_lattice_basis(a: int, b: int, c: int) -> tuple[tuple[int, int], ...]:
    """Return an HNF-like basis for the compressed block-value lattice.

    For three non-unit blocks the basis has rank two.  If ``a=1`` or ``b=1``
    the lattice has rank one and the single non-unit derivative value lies in
    the intersection of the remaining two image ideals.
    """
    abc_support_state(a, b, c)
    A, B, C = (_block_generator(n) for n in (a, b, c))

    if A == 0:
        if a != 1 or B <= 0 or C <= 0:
            raise ValueError("floor line requires at least two non-unit blocks")
        return ((0, lcm(B, C)),)
    if B == 0:
        if b != 1 or A <= 0 or C <= 0:
            raise ValueError("floor line requires at least two non-unit blocks")
        return ((lcm(A, C), 0),)
    if C == 0:
        raise AssertionError("c=a+b cannot be a unit block")

    G = gcd(A, B, C)
    d = gcd(A, C)
    modulus = C // d
    y_step = d // G
    if modulus == 1:
        x0 = 0
    else:
        inverse = pow(A // d, -1, modulus)
        x0 = (-(B // G) * inverse) % modulus

    first = (A * modulus, 0)
    second = (A * x0, B * y_step)
    for u, v in (first, second):
        if u % A or v % B or (u + v) % C:
            raise AssertionError("constructed basis escaped compressed lattice")
    determinant = abs(first[0] * second[1] - first[1] * second[0])
    expected_index = A * B * C // G
    if determinant != expected_index:
        raise AssertionError("compressed basis determinant disagrees with lattice index")
    return (first, second)


def block_value_floor_line(a: int, b: int, c: int) -> BlockValueFloorLine:
    """Return the exact ``W=D`` affine floor line (or point in rank one)."""
    invariants = block_value_lattice_invariants(a, b, c)
    basis = block_value_lattice_basis(a, b, c)
    D = invariants.wronskian_image_generator
    values = tuple(_wronskian(a, b, point) for point in basis)

    if len(basis) == 1:
        w = values[0]
        if abs(w) != D:
            raise AssertionError("rank-one floor generator mismatch")
        sign = 1 if w > 0 else -1
        point = (basis[0][0] * sign, basis[0][1] * sign)
        if _wronskian(a, b, point) != D:
            raise AssertionError("rank-one positive floor point failed")
        return BlockValueFloorLine(
            abc=(a, b, c),
            block_image_generators=invariants.block_image_generators,
            basis=basis,
            basis_wronskians=values,
            wronskian_generator=D,
            particular_floor_point=point,
            kernel_direction=None,
        )

    w1, w2 = values
    g, r, s = _extended_gcd(w1, w2)
    if g != D:
        raise AssertionError("basis Wronskian gcd disagrees with determinantal generator")
    g1, g2 = basis
    point = (
        r * g1[0] + s * g2[0],
        r * g1[1] + s * g2[1],
    )
    if _wronskian(a, b, point) != D:
        raise AssertionError("Bezout floor point failed W=D")
    direction = (
        (w2 // D) * g1[0] - (w1 // D) * g2[0],
        (w2 // D) * g1[1] - (w1 // D) * g2[1],
    )
    if direction == (0, 0) or _wronskian(a, b, direction) != 0:
        raise AssertionError("floor-line direction failed Wronskian kernel")
    if gcd(abs(w1 // D), abs(w2 // D)) != 1:
        raise AssertionError("floor direction coefficients must be primitive in lattice basis")

    return BlockValueFloorLine(
        abc=(a, b, c),
        block_image_generators=invariants.block_image_generators,
        basis=basis,
        basis_wronskians=values,
        wronskian_generator=D,
        particular_floor_point=point,
        kernel_direction=direction,
    )


def _coordinate_target_bound(n: int, radius: int) -> int:
    if n == 1:
        return 0
    coefficients = raw_block_derivative_coefficients(n)
    return radius * sum(abs(value) for _prime, value in coefficients)


def _ceil_div(numerator: int, positive_denominator: int) -> int:
    if positive_denominator <= 0:
        raise ValueError("denominator must be positive")
    return -((-numerator) // positive_denominator)


def _interval_for_abs_affine(origin: int, step: int, bound: int) -> tuple[int, int] | None:
    """Return all integer ``k`` satisfying ``|origin+step*k|<=bound``."""
    if bound < 0:
        raise ValueError("bound must be non-negative")
    if step == 0:
        if abs(origin) > bound:
            return None
        return (-10**100, 10**100)
    if step < 0:
        origin = -origin
        step = -step
    lo = _ceil_div(-bound - origin, step)
    hi = (bound - origin) // step
    if lo > hi:
        return None
    return lo, hi


def exact_absorption_floor_access(a: int, b: int, c: int) -> FloorAccessSolution:
    """Compute exact arbitrary-support ``nu`` via the compressed floor line.

    A Bezout floor point gives an initial finite upper bound ``R``.  Any floor
    point with smaller/equal cost must have each derivative target inside the
    radius-``R`` image box of its block.  Along the one-dimensional floor line
    these three target bounds become integer intervals for the line parameter;
    their intersection is finite.  Exhausting only that parameter interval is
    therefore exact and does not enumerate prime-coordinate witness cubes.
    """
    line = block_value_floor_line(a, b, c)
    invariants = block_value_lattice_invariants(a, b, c)
    u0, v0 = line.particular_floor_point

    if line.kernel_direction is None:
        state = block_value_witness_state(a, b, c, u0, v0)
        if abs(state.wronskian) != line.wronskian_generator:
            raise AssertionError("rank-one floor state lost floor Wronskian")
        return FloorAccessSolution(
            line=line,
            derivative_values=state.derivative_values,
            block_radii=state.block_radii,
            nu=state.global_radius,
            absorption_floor=invariants.absorption_floor,
            searched_parameter_interval=None,
            parameter=None,
        )

    initial = block_value_witness_state(a, b, c, u0, v0)
    radius_bound = initial.global_radius
    hu, hv = line.kernel_direction
    origins = (u0, v0, u0 + v0)
    steps = (hu, hv, hu + hv)
    blocks = (a, b, c)

    lower = -10**100
    upper = 10**100
    for n, origin, step in zip(blocks, origins, steps, strict=True):
        bound = _coordinate_target_bound(n, radius_bound)
        interval = _interval_for_abs_affine(origin, step, bound)
        if interval is None:
            raise AssertionError("initial floor point must lie inside its own radius target bounds")
        lower = max(lower, interval[0])
        upper = min(upper, interval[1])
    if lower > upper or lower <= -10**90 or upper >= 10**90:
        raise AssertionError("floor-line target bounds failed to produce finite parameter interval")

    best_state = initial
    best_k = 0
    for k in range(lower, upper + 1):
        u = u0 + k * hu
        v = v0 + k * hv
        state = block_value_witness_state(a, b, c, u, v)
        if state.wronskian != line.wronskian_generator:
            raise AssertionError("floor-line enumeration escaped W=D")
        if state.global_radius < best_state.global_radius:
            best_state = state
            best_k = k

    return FloorAccessSolution(
        line=line,
        derivative_values=best_state.derivative_values,
        block_radii=best_state.block_radii,
        nu=best_state.global_radius,
        absorption_floor=invariants.absorption_floor,
        searched_parameter_interval=(lower, upper),
        parameter=best_k,
    )
