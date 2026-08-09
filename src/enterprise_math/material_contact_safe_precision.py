"""Canonical safe contact denominator from physical material strength.

The physical-capacity owner and the single-contact precision bridge together give
a simple engineering decision rule that avoids an unnecessary precision search.

Let exact one-tick material impulse capacity be

    C = N/D,

and let one closing contact have exact zero-score demand

    R = q/K,

with ``q,K>0``.  First compare physical strength by cross multiplication.

* If ``N*K < q*D``, the material is physically underpowered.  No contact impulse
  denominator can fabricate enough capacity without violating the declared
  material law.

* If ``N*K >= q*D``, choose the exact-plastic base denominator

      s_plastic = K/gcd(K,q).

  Then ``q*s_plastic/K`` is an integer.  Since

      C*s_plastic >= R*s_plastic

  and the right-hand side is already integral, the conservative represented
  material capacity ``floor(C*s_plastic)`` is automatically at least that exact
  impulse numerator.  Therefore the response is simultaneously:

      capacity-feasible,
      zero final contact score,
      globally passive for the one-contact kinetic metric.

The exact-plastic denominator is a *safe canonical choice*, not necessarily the
cheapest state precision.  A smaller denominator may already be capacity-feasible
and passive while retaining a nonzero outward overshoot.  The separate passivity
and capacity phase modules quantify that lower-cost frontier.

This is elementary rational/divisibility arithmetic specialized as an E001
contact precision policy; it does not claim a new mechanics theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd

from .material_contact_capacity_feasibility import (
    material_contact_capacity_feasibility,
)
from .material_contact_capacity_physical import ExactMaterialImpulseCapacity


@dataclass(frozen=True)
class SafeSingleContactPrecisionReport:
    physically_strong_enough: bool
    strength_cross_difference: int
    closing_score: int
    self_coupling: int
    safe_plastic_denominator: int | None
    safe_impulse_numerator: int | None
    represented_material_capacity_numerator: int | None
    capacity_margin_numerator: int | None
    exact_zero_score: bool
    passive: bool


def safe_single_contact_precision_report(
    exact_capacity: ExactMaterialImpulseCapacity,
    closing_score: int,
    self_coupling: int,
) -> SafeSingleContactPrecisionReport:
    """Return a guaranteed safe exact-plastic denominator when material strength permits."""
    for name, value in (
        ("closing_score", closing_score),
        ("self_coupling", self_coupling),
    ):
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer")
    q = closing_score
    k = self_coupling
    n = exact_capacity.raw_numerator
    d = exact_capacity.raw_denominator
    delta = n * k - q * d
    if delta < 0:
        return SafeSingleContactPrecisionReport(
            physically_strong_enough=False,
            strength_cross_difference=delta,
            closing_score=q,
            self_coupling=k,
            safe_plastic_denominator=None,
            safe_impulse_numerator=None,
            represented_material_capacity_numerator=None,
            capacity_margin_numerator=None,
            exact_zero_score=False,
            passive=False,
        )

    denominator = k // gcd(k, q)
    required = q * denominator // k
    if k * required != q * denominator:
        raise AssertionError("plastic denominator failed exact zero-score integrality")
    feasibility = material_contact_capacity_feasibility(
        exact_capacity,
        q,
        k,
        denominator,
    )
    if not feasibility.feasible:
        raise AssertionError("physically sufficient material failed at exact plastic denominator")
    capacity = feasibility.capacity_numerator
    margin = capacity - required
    if margin < 0:
        raise AssertionError("safe plastic contact capacity margin became negative")
    # Applying exactly the required numerator gives final score -qs+K*a = 0.
    final_score = -q * denominator + k * required
    energy_change = required * (k * required - 2 * q * denominator)
    if final_score != 0:
        raise AssertionError("safe plastic precision failed zero final score")
    if energy_change > 0:
        raise AssertionError("safe plastic precision injected kinetic energy")
    return SafeSingleContactPrecisionReport(
        physically_strong_enough=True,
        strength_cross_difference=delta,
        closing_score=q,
        self_coupling=k,
        safe_plastic_denominator=denominator,
        safe_impulse_numerator=required,
        represented_material_capacity_numerator=capacity,
        capacity_margin_numerator=margin,
        exact_zero_score=True,
        passive=True,
    )
