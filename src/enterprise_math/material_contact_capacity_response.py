"""Minimum-total contact response under explicit per-contact material capacities.

The general E001 contact-response relation uses one finite *search* budget and
returns ``IMPULSE_UNDERRESOLVED`` when that computational/representation budget
is too small.  This module adds a different finite object: a physically/model-
declared per-contact impulse capacity for the current tick.

For contact capacities ``c_i>=0`` the admissible response box is

    0 <= j_i <= c_i.

This box is finite, so the exact minimum-total feasible response relation can be
found by total-impulse layers without any additional search horizon.  If the box
contains no feasible response, the status is ``MATERIAL_CAPACITY_INSUFFICIENT``.
That means the declared contact capacities cannot make all contacts nonclosing
in this tick.  It is deliberately not called ``UNDERRESOLVED``: increasing a
search budget cannot fix a true capacity shortage; the material/contact state
must change or the world must permit unresolved closing contacts to persist.

Capacity can also reduce response ambiguity without an arbitrary ID tie-break.
For a symmetric branching star, equal capacities preserve permutation symmetry;
asymmetric material capacities can remove some minimum responses and may leave a
single feasible minimizer.  This is a model-data effect, not a deterministic
selector inserted by the solver.

The operator remains finite and relation-valued.  No claim is made that the
capacity vector is a constitutive law by itself; it is an explicit input from a
separate material/impulse layer.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_contact_network_impulse_1d import ContactNetworkMomentum1D
from .material_contact_response_relation import (
    contact_impulse_candidate_is_feasible,
    weak_compositions,
)

MATERIAL_CAPACITY_RESOLVED = "MATERIAL_CAPACITY_RESOLVED"
MATERIAL_CAPACITY_INSUFFICIENT = "MATERIAL_CAPACITY_INSUFFICIENT"


def _require_capacities(
    state: ContactNetworkMomentum1D,
    capacities: tuple[int, ...] | list[int],
) -> tuple[int, ...]:
    result = tuple(capacities)
    if len(result) != len(state.contacts):
        raise ValueError("capacities must contain one entry per declared contact")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in result
    ):
        raise ValueError("contact capacities must be non-negative integers")
    return result


def impulse_respects_contact_capacities(
    impulse_vector: tuple[int, ...] | list[int],
    capacities: tuple[int, ...] | list[int],
) -> bool:
    impulses = tuple(impulse_vector)
    limits = tuple(capacities)
    if len(impulses) != len(limits):
        raise ValueError("impulse_vector and capacities must have common length")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in impulses + limits
    ):
        raise ValueError("impulses and capacities must be non-negative integers")
    return all(value <= limit for value, limit in zip(impulses, limits))


@dataclass(frozen=True)
class ContactCapacityResponseRelation1D:
    status: str
    before: ContactNetworkMomentum1D
    capacities: tuple[int, ...]
    minimum_total_impulse: int | None
    response_relation: tuple[tuple[int, ...], ...]

    @property
    def resolved(self) -> bool:
        return self.status == MATERIAL_CAPACITY_RESOLVED

    @property
    def single_valued(self) -> bool:
        return self.resolved and len(self.response_relation) == 1

    @property
    def total_available_capacity(self) -> int:
        return sum(self.capacities)


def minimum_total_response_under_capacities(
    state: ContactNetworkMomentum1D,
    capacities: tuple[int, ...] | list[int],
) -> ContactCapacityResponseRelation1D:
    """Return the exact minimum-total relation inside one finite capacity box."""
    limits = _require_capacities(state, capacities)
    if not limits:
        raise ValueError("at least one declared contact is required")

    maximum_total = sum(limits)
    for total in range(maximum_total + 1):
        feasible = tuple(
            candidate
            for candidate in weak_compositions(total, len(limits))
            if impulse_respects_contact_capacities(candidate, limits)
            and contact_impulse_candidate_is_feasible(state, candidate)
        )
        if feasible:
            return ContactCapacityResponseRelation1D(
                status=MATERIAL_CAPACITY_RESOLVED,
                before=state,
                capacities=limits,
                minimum_total_impulse=total,
                response_relation=feasible,
            )

    return ContactCapacityResponseRelation1D(
        status=MATERIAL_CAPACITY_INSUFFICIENT,
        before=state,
        capacities=limits,
        minimum_total_impulse=None,
        response_relation=(),
    )


def capacity_relation_is_permutation_closed(
    relation: tuple[tuple[int, ...], ...] | list[tuple[int, ...]],
    permutations: tuple[tuple[int, ...], ...] | list[tuple[int, ...]],
) -> bool:
    """Check whether one capacity-constrained response relation preserves a symmetry."""
    vectors = tuple(relation)
    if not vectors:
        raise ValueError("relation must be nonempty")
    width = len(vectors[0])
    if any(len(vector) != width for vector in vectors):
        raise ValueError("relation vectors must have common width")
    values = set(vectors)
    for permutation in permutations:
        permutation = tuple(permutation)
        if len(permutation) != width or set(permutation) != set(range(width)):
            raise ValueError("permutation must reorder all response coordinates")
        for vector in vectors:
            if tuple(vector[index] for index in permutation) not in values:
                return False
    return True
