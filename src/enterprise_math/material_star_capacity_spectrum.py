"""Closed-form capacity spectrum for the symmetric branching-star response.

This E001 specialization combines the general star minimum-response relation
with explicit per-contact material impulse capacities.  It does not replace the
general finite capacity solver; it exposes the exact symmetric-star formula.

For ``k>=2`` contacts, common closing score ``-q`` and capacities ``c_i>=0``, one
candidate ``j`` with total ``S`` is feasible exactly when

    S + j_i >= q,
    0 <= j_i <= c_i.

Put

    L(S) = max(0, q-S),
    C    = sum_i c_i,
    cmin = min_i c_i,
    S*   = ceil(k*q/(k+1)).

At fixed ``S``, a bounded composition exists iff

    L(S) <= cmin,
    k*L(S) <= S <= C.

The middle inequality is exactly the unconstrained star threshold ``S>=S*``.
The first is ``S>=q-cmin``.  Hence the capacity-constrained minimum total is

    S_cap = max(S*, q-cmin)

provided ``S_cap<=C``.  If it exceeds ``C``, the declared material capacities
cannot resolve the star in the current tick.

At the minimum layer, every exact response is

    L <= j_i <= c_i,
    sum_i j_i = S_cap.

The formula exposes two different monotonicities under capacity refinement:

* the feasible set only expands and ``S_cap`` can only weakly decrease;
* the *minimum relation* need not grow by inclusion, because an old higher-total
  optimum can remain feasible while a newly available lower-total layer becomes
  the new optimum.

Example ``k=3,q=5``:

* capacities ``(5,0,0)`` give unique minimum ``(5,0,0)`` at total five;
* capacities ``(5,1,1)`` give unique minimum ``(2,1,1)`` at total four.

The old vector remains feasible after refinement but is no longer minimum.
This is a finite optimization/response-language effect, not a constitutive-law
or physical-energy claim.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_star_response_spectrum import star_minimum_total_impulse

STAR_CAPACITY_RESOLVED = "STAR_CAPACITY_RESOLVED"
STAR_CAPACITY_INSUFFICIENT = "STAR_CAPACITY_INSUFFICIENT"


def _require_inputs(
    leaf_count: int,
    closing_score: int,
    capacities: tuple[int, ...] | list[int],
) -> tuple[int, ...]:
    if isinstance(leaf_count, bool) or not isinstance(leaf_count, int) or leaf_count < 2:
        raise ValueError("leaf_count must be an integer at least two")
    if isinstance(closing_score, bool) or not isinstance(closing_score, int) or closing_score <= 0:
        raise ValueError("closing_score must be a positive integer")
    limits = tuple(capacities)
    if len(limits) != leaf_count:
        raise ValueError("capacities must contain one entry per star contact")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in limits
    ):
        raise ValueError("capacities must be non-negative integers")
    return limits


def star_capacity_minimum_total(
    leaf_count: int,
    closing_score: int,
    capacities: tuple[int, ...] | list[int],
) -> int | None:
    """Return the exact constrained minimum total, or ``None`` if capacities fail."""
    limits = _require_inputs(leaf_count, closing_score, capacities)
    unconstrained = star_minimum_total_impulse(leaf_count, closing_score)
    constrained = max(unconstrained, closing_score - min(limits))
    return constrained if constrained <= sum(limits) else None


def _bounded_compositions(
    total: int,
    lower: int,
    capacities: tuple[int, ...],
) -> tuple[tuple[int, ...], ...]:
    if not capacities:
        return ((),) if total == 0 else ()
    first_cap = capacities[0]
    result: list[tuple[int, ...]] = []
    minimum_first = lower
    maximum_first = min(first_cap, total)
    for first in range(minimum_first, maximum_first + 1):
        for tail in _bounded_compositions(
            total - first,
            lower,
            capacities[1:],
        ):
            result.append((first,) + tail)
    return tuple(result)


def star_capacity_minimum_relation(
    leaf_count: int,
    closing_score: int,
    capacities: tuple[int, ...] | list[int],
) -> tuple[tuple[int, ...], ...]:
    """Return every minimum-total response within the capacity box."""
    limits = _require_inputs(leaf_count, closing_score, capacities)
    minimum = star_capacity_minimum_total(leaf_count, closing_score, limits)
    if minimum is None:
        return ()
    lower = max(0, closing_score - minimum)
    relation = tuple(
        vector
        for vector in _bounded_compositions(minimum, lower, limits)
        if sum(vector) == minimum
    )
    if not relation:
        raise AssertionError("closed-form star capacity minimum has no response")
    if any(
        any(value < lower or value > limit for value, limit in zip(vector, limits))
        for vector in relation
    ):
        raise AssertionError("star capacity relation escaped its exact box")
    return relation


def star_capacity_vector_is_feasible(
    impulse_vector: tuple[int, ...] | list[int],
    closing_score: int,
    capacities: tuple[int, ...] | list[int],
) -> bool:
    values = tuple(impulse_vector)
    limits = tuple(capacities)
    if len(values) != len(limits) or len(values) < 2:
        raise ValueError("impulse_vector and capacities require common star width >=2")
    if isinstance(closing_score, bool) or not isinstance(closing_score, int) or closing_score <= 0:
        raise ValueError("closing_score must be a positive integer")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in values + limits
    ):
        raise ValueError("impulses and capacities must be non-negative integers")
    if any(value > limit for value, limit in zip(values, limits)):
        return False
    total = sum(values)
    return all(total + value >= closing_score for value in values)


@dataclass(frozen=True)
class StarCapacitySpectrumReport:
    leaf_count: int
    closing_score: int
    capacities: tuple[int, ...]
    unconstrained_minimum_total: int
    minimum_capacity: int
    total_capacity: int
    constrained_minimum_total: int | None
    capacity_penalty: int | None
    lower_impulse_floor: int | None
    response_relation: tuple[tuple[int, ...], ...]
    status: str

    @property
    def resolved(self) -> bool:
        return self.status == STAR_CAPACITY_RESOLVED

    @property
    def single_valued(self) -> bool:
        return self.resolved and len(self.response_relation) == 1


def star_capacity_spectrum_report(
    leaf_count: int,
    closing_score: int,
    capacities: tuple[int, ...] | list[int],
) -> StarCapacitySpectrumReport:
    limits = _require_inputs(leaf_count, closing_score, capacities)
    unconstrained = star_minimum_total_impulse(leaf_count, closing_score)
    constrained = star_capacity_minimum_total(leaf_count, closing_score, limits)
    if constrained is None:
        relation: tuple[tuple[int, ...], ...] = ()
        status = STAR_CAPACITY_INSUFFICIENT
        penalty = None
        lower = None
    else:
        relation = star_capacity_minimum_relation(
            leaf_count, closing_score, limits
        )
        status = STAR_CAPACITY_RESOLVED
        penalty = constrained - unconstrained
        lower = max(0, closing_score - constrained)
    return StarCapacitySpectrumReport(
        leaf_count=leaf_count,
        closing_score=closing_score,
        capacities=limits,
        unconstrained_minimum_total=unconstrained,
        minimum_capacity=min(limits),
        total_capacity=sum(limits),
        constrained_minimum_total=constrained,
        capacity_penalty=penalty,
        lower_impulse_floor=lower,
        response_relation=relation,
        status=status,
    )
