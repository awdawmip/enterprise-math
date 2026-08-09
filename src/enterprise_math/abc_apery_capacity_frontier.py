"""Finite Apéry capacity frontiers for exact signed block access.

For a primitive positive coefficient row ``b`` with ``P=sum(b)``, fix a defect
residue ``j`` and its Apéry element ``a_j``.  Let

    L_j(k) = min ||y||_infinity
             over y>=0 with b*y = a_j + k*P.

For a target ``N`` in the opposite residue, put ``r0=(N+a_j)/P``.  At access
radius ``r0+k`` the defect is ``a_j+kP`` and the coordinate cap is
``2*(r0+k)``.  Hence feasibility is equivalent to

    q_j(k) <= r0,

where

    q_j(k) = max(0, ceil((L_j(k)-2*k)/2)).

Adding one to every nonnegative factorization coordinate proves
``L_j(k+1)<=L_j(k)+1``.  Therefore ``q_j(k)`` is nonincreasing and reaches zero
in finitely many steps.  Keeping only the first occurrence of each strict drop
produces a finite Pareto antichain that reconstructs the exact access response
for every nonnegative target in the residue class.

Apéry sets and L-infinity factorization lengths are prior numerical-semigroup
mathematics.  This module records the task-relative signed-access interface.
"""

from __future__ import annotations

from dataclasses import dataclass

from .abc_block_access_apery import (
    apery_values,
    minimum_nonnegative_linf_factorization,
    primitive_positive_row,
)


@dataclass(frozen=True)
class CapacityPoint:
    shift: int
    factorization_radius: int
    capacity_threshold: int


@dataclass(frozen=True)
class ResidueCapacityFrontier:
    target_residue: int
    defect_residue: int
    apery_value: int
    points: tuple[CapacityPoint, ...]


@dataclass(frozen=True)
class CapacityFrontierSignature:
    coefficients: tuple[int, ...]
    period: int
    residues: tuple[ResidueCapacityFrontier, ...]


def _ceil_div_two(value: int) -> int:
    return -((-value) // 2)


def capacity_threshold(factorization_radius: int, shift: int) -> int:
    """Return ``max(0, ceil((L-2k)/2))`` for one defect-factorization level."""
    if (
        isinstance(factorization_radius, bool)
        or not isinstance(factorization_radius, int)
        or factorization_radius < 0
    ):
        raise ValueError("factorization_radius must be a non-negative integer")
    if isinstance(shift, bool) or not isinstance(shift, int) or shift < 0:
        raise ValueError("shift must be a non-negative integer")
    return max(0, _ceil_div_two(factorization_radius - 2 * shift))


def residue_capacity_sequence(
    coefficients: tuple[int, ...], defect_residue: int
) -> tuple[CapacityPoint, ...]:
    """Return the finite exact ``q_j(k)`` sequence through its first zero.

    The length is bounded by ``L_j(0)+1`` because adding the all-ones vector at
    each step yields ``L_j(k)<=L_j(0)+k``, hence
    ``L_j(k)-2k<=L_j(0)-k``.
    """
    primitive, _scale = primitive_positive_row(coefficients)
    period = sum(primitive)
    if (
        isinstance(defect_residue, bool)
        or not isinstance(defect_residue, int)
        or not 0 <= defect_residue < period
    ):
        raise ValueError("defect_residue must lie in [0, period)")
    a = apery_values(primitive)[defect_residue]
    L0 = minimum_nonnegative_linf_factorization(primitive, a)
    result: list[CapacityPoint] = []
    previous_q: int | None = None
    for shift in range(L0 + 1):
        value = a + shift * period
        L = minimum_nonnegative_linf_factorization(primitive, value)
        q = capacity_threshold(L, shift)
        if previous_q is not None and q > previous_q:
            raise AssertionError("capacity threshold must be nonincreasing")
        result.append(
            CapacityPoint(
                shift=shift,
                factorization_radius=L,
                capacity_threshold=q,
            )
        )
        previous_q = q
        if q == 0:
            return tuple(result)
    raise AssertionError("capacity sequence failed finite zero bound")


def residue_capacity_frontier(
    coefficients: tuple[int, ...], defect_residue: int
) -> ResidueCapacityFrontier:
    """Compress a capacity sequence to its nondominated strict-drop antichain."""
    primitive, _scale = primitive_positive_row(coefficients)
    period = sum(primitive)
    a = apery_values(primitive)[defect_residue]
    target_residue = (-defect_residue) % period
    sequence = residue_capacity_sequence(primitive, defect_residue)
    frontier: list[CapacityPoint] = []
    previous_q: int | None = None
    for point in sequence:
        if previous_q is None or point.capacity_threshold < previous_q:
            frontier.append(point)
            previous_q = point.capacity_threshold
    if not frontier or frontier[-1].capacity_threshold != 0:
        raise AssertionError("capacity frontier must terminate at zero threshold")
    return ResidueCapacityFrontier(
        target_residue=target_residue,
        defect_residue=defect_residue,
        apery_value=a,
        points=tuple(frontier),
    )


def capacity_frontier_signature(
    coefficients: tuple[int, ...],
) -> CapacityFrontierSignature:
    """Return finite capacity frontiers for every defect residue modulo ``P``."""
    primitive, _scale = primitive_positive_row(coefficients)
    period = sum(primitive)
    residues = tuple(
        sorted(
            (
                residue_capacity_frontier(primitive, j)
                for j in range(period)
            ),
            key=lambda record: record.target_residue,
        )
    )
    return CapacityFrontierSignature(
        coefficients=primitive,
        period=period,
        residues=residues,
    )


def exact_access_from_capacity_frontier(
    signature: CapacityFrontierSignature, target: int
) -> int:
    """Reconstruct exact ``kappa_b(target)`` from the finite frontier signature."""
    if isinstance(target, bool) or not isinstance(target, int) or target < 0:
        raise ValueError("target must be a non-negative integer")
    residue = target % signature.period
    record = next(item for item in signature.residues if item.target_residue == residue)
    numerator = target + record.apery_value
    if numerator % signature.period:
        raise AssertionError("target/Apéry residue mismatch")
    base_radius = numerator // signature.period
    for point in record.points:
        if point.capacity_threshold <= base_radius:
            return base_radius + point.shift
    raise AssertionError("zero-threshold frontier endpoint should always be feasible")


def frontier_size_bound_holds(coefficients: tuple[int, ...]) -> bool:
    """Check the exact finite cardinality bound ``|F_j|<=ceil(L_j(0)/2)+1``."""
    primitive, _scale = primitive_positive_row(coefficients)
    period = sum(primitive)
    for j in range(period):
        a = apery_values(primitive)[j]
        L0 = minimum_nonnegative_linf_factorization(primitive, a)
        frontier = residue_capacity_frontier(primitive, j)
        if len(frontier.points) > (L0 + 1) // 2 + 1:
            raise AssertionError("capacity frontier exceeded distinct-threshold bound")
    return True
