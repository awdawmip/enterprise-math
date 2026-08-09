"""Passivity bound for capacity-constrained minimum-total symmetric-star response.

``material_contact_capacity_bridge`` shows that finite per-contact material
capacities can force a branching star to over-deliver total impulse relative to
the unconstrained minimum.  This module proves that the topology compensation is
still globally passive as long as the network chooses the *minimum total* inside
the cap box.

Let scaled closing demand be ``Q=q*s`` on ``k`` equal-mass leaves.  For any
feasible response with total numerator ``S``:

    S + j_i >= Q,

so when ``S<=Q`` every coordinate obeys

    j_i >= b = Q-S.

At fixed ``S``, kinetic change is

    Delta E = S^2 - 2QS + sum_i j_i^2.

The largest possible square sum under only the lower bound occurs by putting all
available excess into one contact:

    j = (kS-(k-1)Q, b, ..., b).

This gives the exact no-cap upper envelope

    Delta E_max(S)
      = k(Q-S) * (Q(k-1)-S(k+1)).

The cap-constrained minimum total ``S_cap`` always satisfies

    ceil(kQ/(k+1)) <= S_cap <= Q.

Hence ``Q(k-1)-S_cap(k+1) < 0`` whenever ``S_cap<Q``, while the leading factor
vanishes at ``S_cap=Q``.  Therefore every cap-constrained minimum-total response
is passive; it is strictly dissipative under this upper envelope unless the
minimum total has risen all the way to ``Q``.

This does not make arbitrary feasible over-response passive.  A policy that
chooses total impulse above the capped minimum can still inject energy.  The
result is specific to the symmetric-star positive-coupling specialization and
minimum-total selection.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_contact_capacity_bridge import (
    SymmetricStarMaterialCapacityReport,
    symmetric_star_material_capacity_report,
)


@dataclass(frozen=True)
class SymmetricStarCappedPassivityReport:
    capacity: SymmetricStarMaterialCapacityReport
    capped_minimum_total_numerator: int | None
    contact_lower_bound_numerator: int | None
    kinetic_change_upper_bound_numerator: int | None
    guaranteed_passive: bool
    strict_upper_bound_dissipation: bool


def symmetric_star_capped_passivity_report(
    leaf_count: int,
    closing_quantum: int,
    denominator: int,
    capacity_numerators: tuple[int, ...] | list[int],
) -> SymmetricStarCappedPassivityReport:
    """Return the exact no-cap kinetic upper envelope at the capped minimum total."""
    capacity = symmetric_star_material_capacity_report(
        leaf_count,
        closing_quantum,
        denominator,
        capacity_numerators,
    )
    if not capacity.feasible:
        return SymmetricStarCappedPassivityReport(
            capacity=capacity,
            capped_minimum_total_numerator=None,
            contact_lower_bound_numerator=None,
            kinetic_change_upper_bound_numerator=None,
            guaranteed_passive=False,
            strict_upper_bound_dissipation=False,
        )

    total = capacity.capped_minimum_total_numerator
    if total is None:
        raise AssertionError("feasible star capacity lost capped minimum total")
    demand = capacity.scaled_closing_demand
    lower = demand - total
    if lower < 0:
        raise AssertionError("capped minimum total exceeded closing demand")
    upper = leaf_count * (demand - total) * (
        demand * (leaf_count - 1) - total * (leaf_count + 1)
    )
    if upper > 0:
        raise AssertionError("capped minimum star response lost global passivity bound")
    strict = upper < 0
    return SymmetricStarCappedPassivityReport(
        capacity=capacity,
        capped_minimum_total_numerator=total,
        contact_lower_bound_numerator=lower,
        kinetic_change_upper_bound_numerator=upper,
        guaranteed_passive=True,
        strict_upper_bound_dissipation=strict,
    )
