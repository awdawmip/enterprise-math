"""No-nonzero-cycle theorem for toward-zero projected Pythagorean rotation.

This module closes the logical premise used by the E001 finite extinction bound.
The proof is finite/integer and does not use a real angle or trigonometric
periodicity.

Theorem
=======
For a valid nontrivial ``PythagoreanRotation(a,b,c)`` and componentwise signed
projection toward zero, no nonzero represented state can lie on a periodic
orbit.

Proof chain
-----------
1. The projected squared radius is nonincreasing.  A periodic orbit must return
   to the same radius, so every step on that orbit has zero radius loss.
2. For a toward-zero step write each lifted coordinate as ``c*q+r``.  Quotient
   and nonzero remainder have the same sign, and

       c^2 (N_before-N_after)
         = 2c(q_x r_x + q_y r_y) + r_x^2 + r_y^2.

   Every term on the right is nonnegative.  Zero loss therefore forces
   ``r_x=r_y=0``.  Every step on a hypothetical periodic orbit is thus the exact
   rational rotation by ``z=(a+i b)/c``.
3. A nonzero exact period of length n would imply ``z^n=1``.  Put
   ``t=z+z^-1=2a/c``.  Define integer polynomials

       P_0=2, P_1=X, P_(k+1)=X P_k-P_(k-1).

   Then ``P_n(t)=z^n+z^-n=2``.  For n>=1, ``P_n(X)-2`` is monic with integer
   coefficients.  The rational-root theorem therefore forces the reduced
   denominator of ``t`` to be 1.
4. A valid rotation has ``0<=2a/c<2``.  An integral trace can only be 0 or 1.
   Trace 0 gives ``a=0`` and hence ``b=c``, forbidden by the rotation contract.
   Trace 1 gives ``c=2a`` and then the Pythagorean identity gives
   ``b^2=3a^2``.  This has no positive integer solution because the exponent of
   prime 3 is even on the left and odd on the right.

Therefore the exact rational rotation has no finite order, hence the projected
map has no nonzero periodic orbit.

Combined with finiteness of the integer lattice ball and deterministic forward
iteration, every represented orbit must reach the fixed state (0,0) before a
nonzero state can repeat.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd

from .material_oscillator import PythagoreanRotation, ProjectedRotationStep


@dataclass(frozen=True)
class FiniteOrderObstruction:
    """Arithmetic obstruction to finite order of one rational circle rotation."""

    reduced_trace_numerator: int
    reduced_trace_denominator: int
    trace_is_noninteger: bool
    rational_root_theorem_requires_integer_trace: bool


@dataclass(frozen=True)
class NoNonzeroCycleCertificate:
    """Source-level theorem certificate used by finite extinction bounds."""

    rotation: PythagoreanRotation
    finite_order_obstruction: FiniteOrderObstruction
    no_nonzero_periodic_orbit: bool


def reduced_rotation_trace(rotation: PythagoreanRotation) -> tuple[int, int]:
    """Return reduced numerator/denominator of the exact trace ``2a/c``."""
    numerator = 2 * rotation.a
    denominator = rotation.c
    common = gcd(numerator, denominator)
    return numerator // common, denominator // common


def finite_order_obstruction(rotation: PythagoreanRotation) -> FiniteOrderObstruction:
    """Certify that the exact rational rotation cannot have finite order.

    A finite-order rotation would force the reduced trace denominator to be 1
    by the monic trace-polynomial/rational-root argument in the module proof.
    The valid Pythagorean-rotation contract rules out both possible integral
    traces 0 and 1, so every valid instance has denominator greater than 1.
    """
    numerator, denominator = reduced_rotation_trace(rotation)
    if denominator == 1:
        # This branch is mathematically impossible for a validated rotation.
        # Keep the explicit checks so future changes to the rotation contract
        # cannot silently invalidate the theorem dependency.
        if numerator == 0:
            if rotation.a != 0 or rotation.b != rotation.c:
                raise AssertionError("trace-zero Pythagorean contradiction did not close")
        elif numerator == 1:
            if rotation.c != 2 * rotation.a:
                raise AssertionError("trace-one reduction disagrees with raw coefficients")
            if rotation.b * rotation.b != 3 * rotation.a * rotation.a:
                raise AssertionError("trace-one Pythagorean contradiction did not reduce to b^2=3a^2")
            raise AssertionError("positive integers cannot satisfy b^2=3a^2")
        raise AssertionError("valid rotation produced an impossible integral trace")
    return FiniteOrderObstruction(
        reduced_trace_numerator=numerator,
        reduced_trace_denominator=denominator,
        trace_is_noninteger=True,
        rational_root_theorem_requires_integer_trace=True,
    )


def zero_loss_step_is_exact(step: ProjectedRotationStep) -> bool:
    """Verify the equality case: zero radius loss iff both projection details vanish."""
    exact = step.details == (0, 0)
    if (step.norm_sq_loss == 0) != exact:
        raise AssertionError("toward-zero zero-loss equality case disagrees with projection detail")
    return exact


def certify_no_nonzero_periodic_orbit(
    rotation: PythagoreanRotation,
) -> NoNonzeroCycleCertificate:
    """Return the theorem certificate for one valid Pythagorean rotation."""
    obstruction = finite_order_obstruction(rotation)
    return NoNonzeroCycleCertificate(
        rotation=rotation,
        finite_order_obstruction=obstruction,
        no_nonzero_periodic_orbit=True,
    )
