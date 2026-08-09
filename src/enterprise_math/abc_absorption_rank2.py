"""Exact absorption-access solver for three prime coordinates.

When ``omega(abc)=3``, the additive witness lattice has rank two and imposing
that the raw Wronskian attain its positive image generator cuts it to one
integer affine line.  The minimum L-infinity radius on that line is therefore
an exact one-dimensional integer interval-intersection problem.

This is standard rank-two integer linear algebra / one-dimensional lattice
optimization used as a P025 reference specialization.  No abc proof or generic
CVP novelty is claimed.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd

from .abc_absorption_bezout import bezout_absorption_certificate
from .abc_witness_absorption import (
    arithmetic_wronskian_value,
    minimum_absorption_redundancy,
    raw_wronskian_vector,
    witness_absorption_redundancy,
)
from .abc_witness_precision import additive_relation_vector, is_additive_witness, witness_coordinates


@dataclass(frozen=True)
class RankTwoAbsorptionOptimum:
    """Exact minimum-norm witness attaining the absorption floor."""

    particular_witness: tuple[int, int, int]
    homogeneous_direction: tuple[int, int, int]
    parameter: int
    witness: tuple[int, int, int]
    radius: int
    absorption_redundancy: int
    image_generator: int


def _content(entries: tuple[int, ...]) -> int:
    value = 0
    for entry in entries:
        value = gcd(value, abs(entry))
    return value


def _primitive_sign_vector(entries: tuple[int, int, int]) -> tuple[int, int, int]:
    content = _content(entries)
    if content == 0:
        raise ValueError("vector must be nonzero")
    normalized = tuple(entry // content for entry in entries)
    first = next(entry for entry in normalized if entry)
    if first < 0:
        normalized = tuple(-entry for entry in normalized)
    return normalized  # type: ignore[return-value]


def common_kernel_direction(a: int, b: int, c: int) -> tuple[int, int, int]:
    """Return the primitive generator of ``ker_Z(alpha) intersect ker_Z(beta)``.

    For three coordinates this is the primitive cross product ``alpha x beta``.
    """
    if len(witness_coordinates(a, b, c)) != 3:
        raise ValueError("rank-two absorption solver requires exactly three prime coordinates")
    alpha = additive_relation_vector(a, b, c)
    beta = raw_wronskian_vector(a, b, c)
    cross = (
        alpha[1] * beta[2] - alpha[2] * beta[1],
        alpha[2] * beta[0] - alpha[0] * beta[2],
        alpha[0] * beta[1] - alpha[1] * beta[0],
    )
    direction = _primitive_sign_vector(cross)
    if sum(x * y for x, y in zip(alpha, direction, strict=True)) != 0:
        raise AssertionError("cross-product direction escaped additive kernel")
    if sum(x * y for x, y in zip(beta, direction, strict=True)) != 0:
        raise AssertionError("cross-product direction escaped Wronskian kernel")
    return direction


def _ceil_div(numerator: int, positive_denominator: int) -> int:
    if positive_denominator <= 0:
        raise ValueError("denominator must be positive")
    return -((-numerator) // positive_denominator)


def parameter_interval_for_radius(
    particular: tuple[int, int, int],
    direction: tuple[int, int, int],
    radius: int,
) -> tuple[int, int] | None:
    """Return all integer ``k`` with ``||particular+k*direction||_inf<=radius``.

    The result is the exact intersection interval in parameter space, or
    ``None`` when the radius is infeasible.
    """
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be a non-negative integer")
    lower: int | None = None
    upper: int | None = None
    for x0, step in zip(particular, direction, strict=True):
        if step == 0:
            if abs(x0) > radius:
                return None
            continue
        if step > 0:
            lo = _ceil_div(-radius - x0, step)
            hi = (radius - x0) // step
        else:
            magnitude = -step
            lo = _ceil_div(x0 - radius, magnitude)
            hi = (x0 + radius) // magnitude
        lower = lo if lower is None else max(lower, lo)
        upper = hi if upper is None else min(upper, hi)
        if lower > upper:
            return None
    if lower is None or upper is None:
        raise AssertionError("primitive homogeneous direction cannot be zero")
    return lower, upper


def _radius_at_parameter(
    particular: tuple[int, int, int],
    direction: tuple[int, int, int],
    parameter: int,
) -> int:
    return max(
        abs(x0 + parameter * step)
        for x0, step in zip(particular, direction, strict=True)
    )


def rank_two_absorption_optimum(a: int, b: int, c: int) -> RankTwoAbsorptionOptimum:
    """Solve the exact minimum radius attaining ``eta_min`` for ``omega(abc)=3``.

    Start from any constructive Bezout witness ``x0`` with ``beta*x0=d``.
    Every other integer solution of ``alpha*x=0, beta*x=d`` is uniquely
    ``x0+k*n0`` for integer ``k``, where ``n0`` is the primitive common-kernel
    direction.  Binary search the smallest radius whose coordinate constraints
    have a common integer parameter.
    """
    if len(witness_coordinates(a, b, c)) != 3:
        raise ValueError("rank-two absorption solver requires exactly three prime coordinates")
    certificate = bezout_absorption_certificate(a, b, c)
    particular = tuple(int(value) for value in certificate.witness)
    if len(particular) != 3:
        raise AssertionError("three-coordinate certificate lost dimension")
    particular3 = (particular[0], particular[1], particular[2])
    direction = common_kernel_direction(a, b, c)

    lo = 0
    hi = certificate.radius
    while lo < hi:
        mid = (lo + hi) // 2
        if parameter_interval_for_radius(particular3, direction, mid) is None:
            lo = mid + 1
        else:
            hi = mid
    radius = lo
    interval = parameter_interval_for_radius(particular3, direction, radius)
    if interval is None:
        raise AssertionError("binary search ended on infeasible radius")

    candidates = {interval[0], interval[1]}
    best_parameter = min(
        candidates,
        key=lambda parameter: (
            _radius_at_parameter(particular3, direction, parameter),
            abs(parameter),
            parameter,
        ),
    )
    witness = tuple(
        x0 + best_parameter * step
        for x0, step in zip(particular3, direction, strict=True)
    )
    witness3 = (witness[0], witness[1], witness[2])
    actual_radius = max(abs(value) for value in witness3)
    if actual_radius != radius:
        raise AssertionError("parameter interval did not realize the optimal radius")
    if not is_additive_witness(a, b, c, witness3):
        raise AssertionError("rank-two optimum escaped additive lattice")
    if arithmetic_wronskian_value(a, b, c, witness3) != certificate.image_generator:
        raise AssertionError("rank-two optimum changed the target Wronskian generator")
    eta = witness_absorption_redundancy(a, b, c, witness3)
    if eta != minimum_absorption_redundancy(a, b, c):
        raise AssertionError("rank-two optimum failed to attain eta_min")

    return RankTwoAbsorptionOptimum(
        particular_witness=particular3,
        homogeneous_direction=direction,
        parameter=best_parameter,
        witness=witness3,
        radius=radius,
        absorption_redundancy=eta,
        image_generator=certificate.image_generator,
    )
