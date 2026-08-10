"""Weighted relation cut sums are the exact coarse cut-response coordinates.

For coarse blocks i with capacities m_i and totals c_i, define the A3 weighted
relation field

    Z_ij = m_j c_i - m_i c_j.

For a subset S of coarse blocks,

    Z(S,S^c) = sum_{i in S,j notin S} Z_ij
             = M c_S - m_S C,

where M=sum_i m_i and C=sum_i c_i.  Dividing by M (exactly as a rational probe
coordinate, not hidden floating point) gives the centered capacity-weighted cut
response c_S-(m_S/M)C.  At C=0 it reduces to c_S.

Thus the complete-transfer response/Voronoi cut probes are already encoded by the
weighted relation field.  Under partition coarsening, only unions of coarse
blocks remain valid cuts, exactly matching the surviving-response theorem.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations

Capacities = tuple[int, ...]
Totals = tuple[int, ...]
RelationMatrix = tuple[tuple[int, ...], ...]


def _validate(capacities: Capacities, totals: Totals) -> None:
    if not capacities or len(capacities) != len(totals):
        raise ValueError("capacities and totals must be equal-length nonempty tuples")
    if any(isinstance(value, bool) or not isinstance(value, int) or value <= 0 for value in capacities):
        raise ValueError("capacities must be positive integers")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in totals):
        raise ValueError("totals must be integers")


def weighted_relation_matrix(capacities: Capacities, totals: Totals) -> RelationMatrix:
    _validate(capacities, totals)
    return tuple(
        tuple(capacities[j] * totals[i] - capacities[i] * totals[j] for j in range(len(capacities)))
        for i in range(len(capacities))
    )


def subset_capacity(capacities: Capacities, subset: tuple[int, ...]) -> int:
    chosen = set(subset)
    if not chosen or len(chosen) == len(capacities) or not chosen <= set(range(len(capacities))):
        raise ValueError("subset must be nonempty and proper")
    return sum(capacities[index] for index in chosen)


def subset_total(totals: Totals, subset: tuple[int, ...]) -> int:
    chosen = set(subset)
    if not chosen or len(chosen) == len(totals) or not chosen <= set(range(len(totals))):
        raise ValueError("subset must be nonempty and proper")
    return sum(totals[index] for index in chosen)


def weighted_cut_relation_sum(
    capacities: Capacities,
    totals: Totals,
    subset: tuple[int, ...],
) -> int:
    relation = weighted_relation_matrix(capacities, totals)
    chosen = set(subset)
    if not chosen or len(chosen) == len(capacities) or not chosen <= set(range(len(capacities))):
        raise ValueError("subset must be nonempty and proper")
    return sum(
        relation[i][j]
        for i in chosen
        for j in range(len(capacities))
        if j not in chosen
    )


def weighted_cut_closed_form(
    capacities: Capacities,
    totals: Totals,
    subset: tuple[int, ...],
) -> int:
    _validate(capacities, totals)
    M = sum(capacities)
    C = sum(totals)
    mS = subset_capacity(capacities, subset)
    cS = subset_total(totals, subset)
    return M * cS - mS * C


def weighted_cut_identity(
    capacities: Capacities,
    totals: Totals,
    subset: tuple[int, ...],
) -> bool:
    return weighted_cut_relation_sum(capacities, totals, subset) == weighted_cut_closed_form(
        capacities, totals, subset
    )


def centered_capacity_cut_response(
    capacities: Capacities,
    totals: Totals,
    subset: tuple[int, ...],
) -> Fraction:
    M = sum(capacities)
    return Fraction(weighted_cut_closed_form(capacities, totals, subset), M)


def all_weighted_cut_responses(
    capacities: Capacities,
    totals: Totals,
) -> dict[tuple[int, ...], Fraction]:
    _validate(capacities, totals)
    return {
        subset: centered_capacity_cut_response(capacities, totals, subset)
        for size in range(1, len(capacities))
        for subset in combinations(range(len(capacities)), size)
    }


def zero_total_cut_response_is_subset_total(
    capacities: Capacities,
    totals: Totals,
    subset: tuple[int, ...],
) -> bool:
    if sum(totals) != 0:
        raise ValueError("zero-total specialization requires grand total zero")
    return centered_capacity_cut_response(capacities, totals, subset) == subset_total(totals, subset)


def maximum_absolute_weighted_cut_response(
    capacities: Capacities,
    totals: Totals,
) -> Fraction:
    responses = all_weighted_cut_responses(capacities, totals)
    return max((abs(value) for value in responses.values()), default=Fraction(0))
