"""Exact 2D material-to-kinematic direction/budget tradeoff on Z^2.

This module extends the scalar E001 rebound-budget coupling without introducing
angles or real-valued normalization.  For a nonzero incoming integer vector

    v = g*u,

``g=gcd(|v_x|,|v_y|)`` and ``u`` is the primitive signed lattice direction.
For a material response sample ``r`` on amplitude ``A``, write

    g*r = A*t + rho,     0 <= rho < A.

Two explicit finite policies are compared:

* COMPONENTWISE: scale each coordinate independently with toward-zero integer
  projection.  This preserves the exact L-infinity return budget
  ``floor(||v||_inf*r/A)`` but can change the primitive direction.
* PRIMITIVE_RAY_LOCKED: return ``t*u``.  This preserves the primitive lattice
  direction exactly but can under-return the L-infinity budget.

Let ``M=max(|u_x|,|u_y|)``.  Then the exact ray-locked budget defect is

    floor(M*rho/A),

and COMPONENTWISE preserves the primitive ray iff

    M*rho < A.

Thus axis directions and square diagonals (M=1) are always locked.  General
primitive slopes can expose a finite precision tradeoff controlled entirely by
the quotient remainder ``rho``.  These are kinematic bookkeeping statements,
not physical momentum or energy laws.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd

Vector2D = tuple[int, int]


def _require_integer(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def _require_response(response_sample: int, amplitude: int) -> None:
    _require_integer("response_sample", response_sample)
    _require_integer("amplitude", amplitude)
    if amplitude <= 0:
        raise ValueError("amplitude must be positive")
    if not 0 <= response_sample <= amplitude:
        raise ValueError("response_sample must lie in 0..amplitude")


def _validate_vector(vector: Vector2D) -> Vector2D:
    if not isinstance(vector, tuple) or len(vector) != 2:
        raise ValueError("incoming_vector must be a 2-tuple")
    x, y = vector
    _require_integer("incoming_vector[0]", x)
    _require_integer("incoming_vector[1]", y)
    if x == 0 and y == 0:
        raise ValueError("incoming_vector must be nonzero")
    return x, y


def _signed_scaled_component(value: int, response_sample: int, amplitude: int) -> int:
    magnitude = abs(value) * response_sample // amplitude
    if value < 0:
        return -magnitude
    return magnitude


def linf_budget(vector: Vector2D) -> int:
    """Return the non-negative L-infinity magnitude of one integer vector."""
    x, y = vector
    return max(abs(x), abs(y))


@dataclass(frozen=True)
class PrimitiveRay2D:
    incoming_vector: Vector2D
    ray_scale: int
    primitive_direction: Vector2D
    primitive_linf: int


def primitive_ray_2d(incoming_vector: Vector2D) -> PrimitiveRay2D:
    """Factor a nonzero integer vector into gcd scale times a primitive ray."""
    x, y = _validate_vector(incoming_vector)
    scale = gcd(abs(x), abs(y))
    if scale <= 0:
        raise AssertionError("nonzero integer vector produced zero gcd scale")
    primitive = (x // scale, y // scale)
    if gcd(abs(primitive[0]), abs(primitive[1])) != 1:
        raise AssertionError("primitive direction retained a common factor")
    primitive_linf = linf_budget(primitive)
    if linf_budget((scale * primitive[0], scale * primitive[1])) != linf_budget((x, y)):
        raise AssertionError("primitive-ray factorization changed L-infinity budget")
    return PrimitiveRay2D(
        incoming_vector=(x, y),
        ray_scale=scale,
        primitive_direction=primitive,
        primitive_linf=primitive_linf,
    )


def componentwise_return_vector(
    incoming_vector: Vector2D,
    response_sample: int,
    amplitude: int,
) -> Vector2D:
    """Scale each signed coordinate independently by the finite material ratio."""
    x, y = _validate_vector(incoming_vector)
    _require_response(response_sample, amplitude)
    return (
        _signed_scaled_component(x, response_sample, amplitude),
        _signed_scaled_component(y, response_sample, amplitude),
    )


def primitive_ray_locked_return_vector(
    incoming_vector: Vector2D,
    response_sample: int,
    amplitude: int,
) -> Vector2D:
    """Return the largest response on the original primitive lattice ray."""
    ray = primitive_ray_2d(incoming_vector)
    _require_response(response_sample, amplitude)
    returned_scale = ray.ray_scale * response_sample // amplitude
    ux, uy = ray.primitive_direction
    return returned_scale * ux, returned_scale * uy


@dataclass(frozen=True)
class DirectionBudgetReport2D:
    incoming_vector: Vector2D
    ray_scale: int
    primitive_direction: Vector2D
    primitive_linf: int
    response_sample: int
    amplitude: int
    ray_return_scale: int
    ray_remainder: int
    exact_linf_return_budget: int
    componentwise_vector: Vector2D
    primitive_ray_locked_vector: Vector2D
    componentwise_linf_budget: int
    primitive_ray_locked_linf_budget: int
    ray_locked_budget_defect: int
    expected_defect_from_remainder: int
    componentwise_preserves_primitive_ray: bool
    remainder_lock_condition: bool


def direction_budget_report_2d(
    incoming_vector: Vector2D,
    response_sample: int,
    amplitude: int,
) -> DirectionBudgetReport2D:
    """Return the exact direction-vs-budget comparison for one finite state."""
    ray = primitive_ray_2d(incoming_vector)
    _require_response(response_sample, amplitude)
    returned_scale, remainder = divmod(ray.ray_scale * response_sample, amplitude)
    componentwise = componentwise_return_vector(
        incoming_vector, response_sample, amplitude
    )
    locked = primitive_ray_locked_return_vector(
        incoming_vector, response_sample, amplitude
    )
    exact_budget = linf_budget(incoming_vector) * response_sample // amplitude
    componentwise_budget = linf_budget(componentwise)
    locked_budget = linf_budget(locked)
    if componentwise_budget != exact_budget:
        raise AssertionError("componentwise projection failed exact L-infinity budget")

    defect = exact_budget - locked_budget
    expected_defect = ray.primitive_linf * remainder // amplitude
    if defect != expected_defect:
        raise AssertionError("ray-locked budget defect disagrees with remainder formula")
    if not 0 <= defect < ray.primitive_linf:
        raise AssertionError("ray-locked budget defect escaped primitive-direction bound")

    preserves_ray = componentwise == locked
    lock_condition = ray.primitive_linf * remainder < amplitude
    if preserves_ray != lock_condition:
        raise AssertionError("primitive-ray lock condition disagrees with exact vectors")

    return DirectionBudgetReport2D(
        incoming_vector=ray.incoming_vector,
        ray_scale=ray.ray_scale,
        primitive_direction=ray.primitive_direction,
        primitive_linf=ray.primitive_linf,
        response_sample=response_sample,
        amplitude=amplitude,
        ray_return_scale=returned_scale,
        ray_remainder=remainder,
        exact_linf_return_budget=exact_budget,
        componentwise_vector=componentwise,
        primitive_ray_locked_vector=locked,
        componentwise_linf_budget=componentwise_budget,
        primitive_ray_locked_linf_budget=locked_budget,
        ray_locked_budget_defect=defect,
        expected_defect_from_remainder=expected_defect,
        componentwise_preserves_primitive_ray=preserves_ray,
        remainder_lock_condition=lock_condition,
    )


@dataclass(frozen=True)
class DirectionLockResidueCounts2D:
    incoming_vector: Vector2D
    amplitude: int
    ray_scale: int
    primitive_linf: int
    ray_amplitude_gcd: int
    response_residue_count: int
    locked_response_residues: int
    divergent_response_residues: int
    maximum_locked_remainder: int


def direction_lock_residue_counts_2d(
    incoming_vector: Vector2D,
    amplitude: int,
) -> DirectionLockResidueCounts2D:
    """Count exact response residues whose componentwise result stays on the ray.

    The count is over ``response_sample mod A``, represented by ``0..A-1``.
    Multiplication by the ray scale ``g`` reaches exactly the remainder subgroup
    generated by ``h=gcd(g,A)``; every reachable remainder has ``h`` preimages.
    """
    ray = primitive_ray_2d(incoming_vector)
    _require_integer("amplitude", amplitude)
    if amplitude <= 0:
        raise ValueError("amplitude must be positive")
    threshold = (amplitude - 1) // ray.primitive_linf
    h = gcd(ray.ray_scale, amplitude)
    locked_reachable_remainders = threshold // h + 1
    locked_residues = h * locked_reachable_remainders
    if not 1 <= locked_residues <= amplitude:
        raise AssertionError("locked residue count escaped denominator cycle")
    return DirectionLockResidueCounts2D(
        incoming_vector=ray.incoming_vector,
        amplitude=amplitude,
        ray_scale=ray.ray_scale,
        primitive_linf=ray.primitive_linf,
        ray_amplitude_gcd=h,
        response_residue_count=amplitude,
        locked_response_residues=locked_residues,
        divergent_response_residues=amplitude - locked_residues,
        maximum_locked_remainder=threshold,
    )
