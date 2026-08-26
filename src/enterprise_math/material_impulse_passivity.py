"""Exact squared-momentum passivity boundary for one wall-opposing integer impulse.

Orient incoming wall motion as positive ``P>0`` and apply a non-negative opposing
impulse ``J``:

    P' = P-J.

The squared-momentum defect is the exact integer identity

    (P-J)^2 - P^2 = J(J-2P).

Therefore a stationary-wall impulse is non-amplifying in this minimal kinetic
proxy exactly when ``0<=J<=2P``.  This separates five integer regimes:

* ``J<P``: decelerated toward motion;
* ``J=P``: stall;
* ``P<J<2P``: dissipative rebound;
* ``J=2P``: equal-magnitude reflection;
* ``J>2P``: active amplification, which needs an explicit energy/source context
  rather than being assumed for a passive material.

For a fixed impulse magnitude ``J``, passivity for every admitted momentum
``P>=P_min`` is equivalent to ``J<=2P_min``.  Equivalently the smallest positive
momentum at which a fixed J becomes non-amplifying is ``ceil(J/2)``.

This is an algebraic engineering constraint, not a claim that squared momentum
alone is a complete physical energy for arbitrary masses/materials.
"""

from __future__ import annotations

from dataclasses import dataclass

DECELERATED_TOWARD = "DECELERATED_TOWARD"
STALL = "STALL"
DISSIPATIVE_REBOUND = "DISSIPATIVE_REBOUND"
ELASTIC_REFLECTION = "ELASTIC_REFLECTION"
ACTIVE_AMPLIFICATION = "ACTIVE_AMPLIFICATION"


@dataclass(frozen=True)
class ImpulsePassivityReport:
    incoming_oriented_momentum: int
    impulse: int
    outgoing_oriented_momentum: int
    squared_before: int
    squared_after: int
    squared_defect: int
    passive_nonamplifying: bool
    regime: str


def impulse_passivity_report(
    incoming_oriented_momentum: int,
    impulse: int,
) -> ImpulsePassivityReport:
    """Classify one non-negative opposing impulse against exact P^2 change."""
    if (
        isinstance(incoming_oriented_momentum, bool)
        or not isinstance(incoming_oriented_momentum, int)
        or incoming_oriented_momentum <= 0
    ):
        raise ValueError("incoming_oriented_momentum must be a positive integer")
    if isinstance(impulse, bool) or not isinstance(impulse, int) or impulse < 0:
        raise ValueError("impulse must be a non-negative integer")
    p = incoming_oriented_momentum
    j = impulse
    after = p - j
    before_sq = p * p
    after_sq = after * after
    defect = after_sq - before_sq
    if defect != j * (j - 2 * p):
        raise AssertionError("squared-momentum defect identity failed")
    passive = defect <= 0
    if j < p:
        regime = DECELERATED_TOWARD
    elif j == p:
        regime = STALL
    elif j < 2 * p:
        regime = DISSIPATIVE_REBOUND
    elif j == 2 * p:
        regime = ELASTIC_REFLECTION
    else:
        regime = ACTIVE_AMPLIFICATION
    if passive != (j <= 2 * p):
        raise AssertionError("passivity classification escaped exact 2P boundary")
    return ImpulsePassivityReport(
        incoming_oriented_momentum=p,
        impulse=j,
        outgoing_oriented_momentum=after,
        squared_before=before_sq,
        squared_after=after_sq,
        squared_defect=defect,
        passive_nonamplifying=passive,
        regime=regime,
    )


def minimum_momentum_for_fixed_impulse_passivity(impulse: int) -> int:
    """Return max(1,ceil(J/2)) for positive admitted momentum quanta."""
    if isinstance(impulse, bool) or not isinstance(impulse, int) or impulse < 0:
        raise ValueError("impulse must be a non-negative integer")
    return max(1, (impulse + 1) // 2)


def fixed_impulse_passive_on_tail(impulse: int, minimum_momentum: int) -> bool:
    """Whether fixed J is non-amplifying for every integer P>=minimum_momentum."""
    if (
        isinstance(minimum_momentum, bool)
        or not isinstance(minimum_momentum, int)
        or minimum_momentum <= 0
    ):
        raise ValueError("minimum_momentum must be a positive integer")
    if isinstance(impulse, bool) or not isinstance(impulse, int) or impulse < 0:
        raise ValueError("impulse must be a non-negative integer")
    return impulse <= 2 * minimum_momentum
