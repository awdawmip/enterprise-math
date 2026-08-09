"""Exact integer linear material oscillator and its short-period stability restriction.

Consider the simplest local force/drift material element with positive integer
coefficients ``a,b``:

    p' = p - a*x,
    x' = x + b*p'.

On the integer state vector ``(x,p)`` the update matrix is

    M = [[1-a*b, b], [-a, 1]],

with determinant 1 and trace ``2-a*b``.  It preserves the exact integer quadratic
form

    Q(x,p) = a*x^2 - a*b*x*p + b*p^2.

The form is positive definite exactly when ``0<a*b<4``.  For positive integer
``a,b`` this leaves only three products.  Cayley-Hamilton then gives exact matrix
orders:

    a*b = 1  -> M^6 = I,
    a*b = 2  -> M^4 = I,
    a*b = 3  -> M^3 = I.

Thus an exact 2D linear oscillator with integer kick/drift coefficients cannot
supply arbitrarily fine harmonic phase resolution: every positive-definite case
is a short crystallographic orbit.  At ``a*b=4`` the invariant degenerates and
nonzero generic orbits can grow linearly; above 4 the form is indefinite and the
map is hyperbolic.

This is an elementary symplectic-Euler / Cayley-Hamilton restriction, not a
novelty claim.  Its E001 role is negative: realistic fine-phase material
oscillation needs additional finite structure such as rational scale/detail,
nonlinear response, or higher-dimensional internal state rather than pretending
that exact integer 2D linear coefficients can approximate arbitrary sine phases.
"""

from __future__ import annotations

from dataclasses import dataclass

ELLIPTIC_SHORT_PERIOD = "ELLIPTIC_SHORT_PERIOD"
PARABOLIC_BOUNDARY = "PARABOLIC_BOUNDARY"
HYPERBOLIC = "HYPERBOLIC"


def _positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def integer_linear_material_step(
    deformation: int,
    momentum: int,
    kick_coefficient: int,
    drift_coefficient: int,
) -> tuple[int, int]:
    """Apply one exact kick-then-drift integer linear material step."""
    if isinstance(deformation, bool) or not isinstance(deformation, int):
        raise ValueError("deformation must be an integer")
    if isinstance(momentum, bool) or not isinstance(momentum, int):
        raise ValueError("momentum must be an integer")
    _positive("kick_coefficient", kick_coefficient)
    _positive("drift_coefficient", drift_coefficient)
    after_momentum = momentum - kick_coefficient * deformation
    after_deformation = deformation + drift_coefficient * after_momentum
    return after_deformation, after_momentum


def integer_linear_material_invariant(
    deformation: int,
    momentum: int,
    kick_coefficient: int,
    drift_coefficient: int,
) -> int:
    """Return Q=a*x^2-a*b*x*p+b*p^2."""
    if isinstance(deformation, bool) or not isinstance(deformation, int):
        raise ValueError("deformation must be an integer")
    if isinstance(momentum, bool) or not isinstance(momentum, int):
        raise ValueError("momentum must be an integer")
    _positive("kick_coefficient", kick_coefficient)
    _positive("drift_coefficient", drift_coefficient)
    a = kick_coefficient
    b = drift_coefficient
    return a * deformation * deformation - a * b * deformation * momentum + b * momentum * momentum


@dataclass(frozen=True)
class IntegerLinearOscillatorClassification:
    kick_coefficient: int
    drift_coefficient: int
    coefficient_product: int
    matrix_trace: int
    determinant: int
    invariant_discriminant_resource: int
    regime: str
    exact_matrix_period: int | None


def integer_linear_oscillator_classification(
    kick_coefficient: int,
    drift_coefficient: int,
) -> IntegerLinearOscillatorClassification:
    """Classify the exact integer linear kick/drift oscillator."""
    _positive("kick_coefficient", kick_coefficient)
    _positive("drift_coefficient", drift_coefficient)
    product = kick_coefficient * drift_coefficient
    trace = 2 - product
    # Four times the determinant of the symmetric matrix of Q.
    positive_resource = product * (4 - product)
    if product < 4:
        regime = ELLIPTIC_SHORT_PERIOD
        period = {1: 6, 2: 4, 3: 3}[product]
    elif product == 4:
        regime = PARABOLIC_BOUNDARY
        period = None
    else:
        regime = HYPERBOLIC
        period = None
    return IntegerLinearOscillatorClassification(
        kick_coefficient=kick_coefficient,
        drift_coefficient=drift_coefficient,
        coefficient_product=product,
        matrix_trace=trace,
        determinant=1,
        invariant_discriminant_resource=positive_resource,
        regime=regime,
        exact_matrix_period=period,
    )


def iterate_integer_linear_material(
    deformation: int,
    momentum: int,
    kick_coefficient: int,
    drift_coefficient: int,
    steps: int,
) -> tuple[int, int]:
    if isinstance(steps, bool) or not isinstance(steps, int) or steps < 0:
        raise ValueError("steps must be a non-negative integer")
    state = (deformation, momentum)
    for _ in range(steps):
        state = integer_linear_material_step(
            state[0], state[1], kick_coefficient, drift_coefficient
        )
    return state
