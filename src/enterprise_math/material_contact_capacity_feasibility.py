"""Exact material-capacity versus single-contact demand precision phase.

``material_contact_capacity_physical`` supplies one exact one-tick material
impulse capacity

    C = N/D

in momentum-count units before contact-lattice projection.  A single closing
contact with closing score magnitude ``q`` and self-coupling ``K`` has exact
zero-score impulse demand

    R = q/K.

At contact impulse denominator ``s``:

    u_s = floor(N*s/D)        (available material capacity numerator),
    a_s = ceil(q*s/K)         (minimum nonclosing response numerator).

Feasibility is ``u_s>=a_s``.  The exact physical strength comparison is the
integer cross-difference

    delta = N*K - q*D.

Three regimes follow.

1. ``delta<0``: ``C<R``.  No denominator can make the material strong enough;
   infeasibility is physical, not a precision artifact.

2. ``delta=0``: ``C=R``.  Feasibility occurs exactly when the common rational
   demand is representable, i.e. on the divisibility sublattice

       s in (K/gcd(K,q))*N_{>0}.

3. ``delta>0``: ``C>R``.  Coarse denominators can still under-represent material
   capacity.  Writing ``N*s=D*u_s+rho_s`` gives

       K*u_s-q*s = (s*delta-K*rho_s)/D.

   Since ``0<=rho_s<D``, every integer denominator satisfying

       s*delta >= K(D-1)

   is feasible.  This gives a finite universal threshold; exact search below it
   yields the smallest integer denominator after which *all* larger integer
   denominators are feasible.

Along a true divisibility refinement ``s' = m*s``, feasibility is monotone:
``u_{ms}>=m*u_s`` while ``a_{ms}<=m*a_s``.  Thus a represented feasible material
response never becomes infeasible on a true refinement multiple, even though
numerically adjacent non-multiple denominators may show different phase behavior.

This is rational/floor/ceil arithmetic specialized to E001 material/contact
precision.  Contact-network ownership remains elsewhere.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd

from .material_contact_capacity_physical import ExactMaterialImpulseCapacity

UNDERPOWERED = "UNDERPOWERED"
BALANCED = "BALANCED"
OVERPOWERED = "OVERPOWERED"


def _positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _ceil_div(numerator: int, denominator: int) -> int:
    if numerator <= 0:
        return 0
    return (numerator + denominator - 1) // denominator


@dataclass(frozen=True)
class MaterialContactCapacityFeasibility:
    contact_denominator: int
    capacity_numerator: int
    minimum_required_numerator: int
    feasible: bool
    strength_cross_difference: int
    strength_regime: str
    balanced_exact_base_denominator: int | None
    sufficient_eventual_feasibility_denominator: int | None
    exact_permanent_feasibility_denominator: int | None

    @property
    def precision_caused_capacity_deficit(self) -> bool:
        return self.strength_regime == OVERPOWERED and not self.feasible

    @property
    def physically_underpowered(self) -> bool:
        return self.strength_regime == UNDERPOWERED


def _capacity_numerator(
    exact: ExactMaterialImpulseCapacity,
    denominator: int,
) -> int:
    return exact.raw_numerator * denominator // exact.raw_denominator


def _required_numerator(q: int, coupling: int, denominator: int) -> int:
    return _ceil_div(q * denominator, coupling)


def _is_feasible(
    exact: ExactMaterialImpulseCapacity,
    q: int,
    coupling: int,
    denominator: int,
) -> bool:
    return _capacity_numerator(exact, denominator) >= _required_numerator(
        q, coupling, denominator
    )


def material_contact_capacity_feasibility(
    exact: ExactMaterialImpulseCapacity,
    closing_score: int,
    self_coupling: int,
    contact_denominator: int,
) -> MaterialContactCapacityFeasibility:
    """Classify physical strength and precision-limited feasibility at denominator s."""
    _positive("closing_score", closing_score)
    _positive("self_coupling", self_coupling)
    _positive("contact_denominator", contact_denominator)
    q = closing_score
    k = self_coupling
    s = contact_denominator
    n = exact.raw_numerator
    d = exact.raw_denominator
    delta = n * k - q * d
    capacity = _capacity_numerator(exact, s)
    required = _required_numerator(q, k, s)
    feasible = capacity >= required

    if delta < 0:
        regime = UNDERPOWERED
        balanced_base = None
        sufficient = None
        permanent = None
        if feasible:
            raise AssertionError("physically underpowered material became discretely feasible")
    elif delta == 0:
        regime = BALANCED
        balanced_base = k // gcd(k, q)
        sufficient = None
        permanent = None
        if feasible != (s % balanced_base == 0):
            raise AssertionError("balanced material/contact feasibility lost exact sublattice")
    else:
        regime = OVERPOWERED
        balanced_base = None
        sufficient_raw = _ceil_div(k * (d - 1), delta)
        sufficient = max(1, sufficient_raw)
        if not _is_feasible(exact, q, k, sufficient):
            raise AssertionError("eventual feasibility sufficient threshold failed")
        last_infeasible = 0
        for candidate in range(1, sufficient + 1):
            if not _is_feasible(exact, q, k, candidate):
                last_infeasible = candidate
        permanent = last_infeasible + 1
        if permanent > sufficient:
            raise AssertionError("exact permanent feasibility exceeded sufficient bound")
        # Verify the finite gap up to the proven-all-feasible threshold.
        if any(
            not _is_feasible(exact, q, k, candidate)
            for candidate in range(permanent, sufficient + 1)
        ):
            raise AssertionError("exact permanent feasibility search left a finite hole")

    return MaterialContactCapacityFeasibility(
        contact_denominator=s,
        capacity_numerator=capacity,
        minimum_required_numerator=required,
        feasible=feasible,
        strength_cross_difference=delta,
        strength_regime=regime,
        balanced_exact_base_denominator=balanced_base,
        sufficient_eventual_feasibility_denominator=sufficient,
        exact_permanent_feasibility_denominator=permanent,
    )


def verify_capacity_feasibility_under_divisibility_refinement(
    exact: ExactMaterialImpulseCapacity,
    closing_score: int,
    self_coupling: int,
    coarse_denominator: int,
    refinement_multiplier: int,
) -> bool:
    """Verify that feasible coarse response remains feasible at a true refinement multiple."""
    _positive("coarse_denominator", coarse_denominator)
    _positive("refinement_multiplier", refinement_multiplier)
    coarse = material_contact_capacity_feasibility(
        exact,
        closing_score,
        self_coupling,
        coarse_denominator,
    )
    fine = material_contact_capacity_feasibility(
        exact,
        closing_score,
        self_coupling,
        coarse_denominator * refinement_multiplier,
    )
    if coarse.feasible and not fine.feasible:
        raise AssertionError("material contact feasibility regressed under true refinement")
    if coarse.feasible:
        if fine.capacity_numerator < refinement_multiplier * coarse.capacity_numerator:
            raise AssertionError("fine material capacity lost scaled coarse capacity")
        if fine.minimum_required_numerator > refinement_multiplier * coarse.minimum_required_numerator:
            raise AssertionError("fine minimum contact demand exceeded scaled coarse witness")
    return True
