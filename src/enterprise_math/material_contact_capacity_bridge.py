"""L3 bridge from finite material impulse capacity to contact-network response.

A constitutive/material layer need not prescribe the delivered multi-contact
impulse vector.  A cleaner interface is to provide, for each active contact,
one finite impulse *capacity* on the currently declared denominator.  The
contact-network layer then asks whether those capacities can realize a
nonclosing response.

This file closes that interface for two topology classes whose response geometry
is already owned elsewhere in E001.

1. Z-coupled weighted path.
   The weighted-chain owner proves a unique componentwise-least feasible impulse
   vector ``j*``.  After scaling the initial momentum by denominator ``s``, its
   solver gives the exact required numerator vector at precision ``s``.  Because
   every feasible vector is componentwise >= ``j*``, contact capacities ``u``
   admit a response iff

       j*_i <= u_i   for every contact i.

   There is no compensating over-delivery on another path edge that can rescue a
   capacity below its least-action demand.

2. Symmetric branching star.
   For ``k`` leaves, closing quantum ``q``, denominator ``s`` and

       Q = q*s,

   a numerator vector ``j`` is feasible exactly when

       S + j_i >= Q,  S=sum(j).

   With material capacities ``0<=j_i<=u_i``, put ``U=sum(u)`` and
   ``u_min=min(u)``.  Since every star score is monotone in every impulse
   coordinate, any capped response exists iff the maximum vector itself is
   feasible:

       U + u_min >= Q.

   The unconstrained minimum total is ``S*`` from the star-spectrum owner.  When
   the cap box is feasible, the exact minimum total inside it is

       S_cap = max(S*, Q-u_min).

   Writing ``Q=(k+1)t+r``, the unconstrained minimum relation has baseline ``t``.
   Hence the exact topology-induced over-response forced by one soft leaf is

       S_cap-S* = max(0, t-u_min).

   A minimum-total unconstrained response remains available under the caps iff
   the cap box is feasible and ``u_min>=t``.  Otherwise other contacts must
   over-deliver to separate the under-capacity leaf through the shared center.

These are E001 specializations of already-owned least-action/star results.  The
capacity abstraction is an engineering bridge only; force/time calibration that
produces the capacities remains a separate material-world concern.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_contact_network_impulse_1d import ContactNetworkMomentum1D
from .material_star_response_precision_phase import (
    star_minimum_total_numerator_at_precision,
    star_scaled_closing_phase,
)
from .material_weighted_chain_least_action_1d import solve_weighted_chain_least_action


def _positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _nonnegative_tuple(
    name: str,
    values: tuple[int, ...] | list[int],
    expected_length: int,
) -> tuple[int, ...]:
    result = tuple(values)
    if len(result) != expected_length:
        raise ValueError(f"{name} must match contact count")
    for value in result:
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError(f"{name} entries must be non-negative integers")
    return result


@dataclass(frozen=True)
class WeightedChainMaterialCapacityReport:
    denominator: int
    capacity_numerators: tuple[int, ...]
    least_required_numerators: tuple[int, ...]
    deficit_numerators: tuple[int, ...]
    feasible: bool

    @property
    def total_required_numerator(self) -> int:
        return sum(self.least_required_numerators)

    @property
    def total_capacity_numerator(self) -> int:
        return sum(self.capacity_numerators)


def weighted_chain_material_capacity_report(
    state: ContactNetworkMomentum1D,
    denominator: int,
    capacity_numerators: tuple[int, ...] | list[int],
) -> WeightedChainMaterialCapacityReport:
    """Exact capped-feasibility test for the weighted path least-action response."""
    _positive("denominator", denominator)
    capacities = _nonnegative_tuple(
        "capacity_numerators",
        capacity_numerators,
        len(state.contacts),
    )
    scaled_state = ContactNetworkMomentum1D(
        masses=state.masses,
        momenta=tuple(denominator * value for value in state.momenta),
        contacts=state.contacts,
    )
    solution = solve_weighted_chain_least_action(scaled_state)
    required = solution.impulse_vector
    deficits = tuple(
        max(0, need - capacity)
        for need, capacity in zip(required, capacities)
    )
    feasible = not any(deficits)
    return WeightedChainMaterialCapacityReport(
        denominator=denominator,
        capacity_numerators=capacities,
        least_required_numerators=required,
        deficit_numerators=deficits,
        feasible=feasible,
    )


@dataclass(frozen=True)
class SymmetricStarMaterialCapacityReport:
    leaf_count: int
    closing_quantum: int
    denominator: int
    scaled_closing_demand: int
    capacity_numerators: tuple[int, ...]
    total_capacity_numerator: int
    minimum_capacity_numerator: int
    baseline_numerator: int
    residue_numerator: int
    unconstrained_minimum_total_numerator: int
    feasible: bool
    capped_minimum_total_numerator: int | None
    topology_overresponse_numerator: int | None
    unconstrained_minimum_relation_available: bool


def symmetric_star_material_capacity_report(
    leaf_count: int,
    closing_quantum: int,
    denominator: int,
    capacity_numerators: tuple[int, ...] | list[int],
) -> SymmetricStarMaterialCapacityReport:
    """Exact capped feasibility and minimum-total penalty for a symmetric star."""
    if isinstance(leaf_count, bool) or not isinstance(leaf_count, int) or leaf_count < 2:
        raise ValueError("leaf_count must be an integer at least two")
    _positive("closing_quantum", closing_quantum)
    _positive("denominator", denominator)
    capacities = _nonnegative_tuple(
        "capacity_numerators",
        capacity_numerators,
        leaf_count,
    )
    demand = closing_quantum * denominator
    total_capacity = sum(capacities)
    minimum_capacity = min(capacities)
    baseline, residue = star_scaled_closing_phase(
        leaf_count,
        closing_quantum,
        denominator,
    )
    unconstrained = star_minimum_total_numerator_at_precision(
        leaf_count,
        closing_quantum,
        denominator,
    )
    if unconstrained != leaf_count * baseline + residue:
        raise AssertionError("star minimum total disagrees with denominator phase")

    feasible = total_capacity + minimum_capacity >= demand
    if feasible:
        capped_minimum = max(unconstrained, demand - minimum_capacity)
        if capped_minimum > total_capacity:
            raise AssertionError("feasible star cap box lost its minimum-total witness")
        overresponse = capped_minimum - unconstrained
        expected_overresponse = max(0, baseline - minimum_capacity)
        if overresponse != expected_overresponse:
            raise AssertionError("star capacity over-response disagrees with baseline formula")
        minimum_relation_available = minimum_capacity >= baseline
    else:
        capped_minimum = None
        overresponse = None
        minimum_relation_available = False

    return SymmetricStarMaterialCapacityReport(
        leaf_count=leaf_count,
        closing_quantum=closing_quantum,
        denominator=denominator,
        scaled_closing_demand=demand,
        capacity_numerators=capacities,
        total_capacity_numerator=total_capacity,
        minimum_capacity_numerator=minimum_capacity,
        baseline_numerator=baseline,
        residue_numerator=residue,
        unconstrained_minimum_total_numerator=unconstrained,
        feasible=feasible,
        capped_minimum_total_numerator=capped_minimum,
        topology_overresponse_numerator=overresponse,
        unconstrained_minimum_relation_available=minimum_relation_available,
    )
