"""Leaf-identity quotient of the symmetric branching-star response relation.

This E001 specialization consumes the exact labeled minimum-response relation
from ``material_star_response_spectrum`` and asks a P024-style question:
what remains if future actions/observables do not distinguish the identities of
identical leaves?

For ``k>=2`` leaves and common closing score ``-q``, write the Euclidean
remainder decomposition

    q = (k+1)*b + R,      0 <= R <= k.

The minimum-total response formulas from the parent owner simplify to

    S* = k*b + R,
    j_i = b + x_i,        x_i >= 0,  sum_i x_i = R.

Thus the entire ambiguity above the uniform baseline ``b`` depends only on the
residue ``R=q mod (k+1)``.  Under the full leaf-permutation group ``S_k``, two
labeled minimum responses are equivalent exactly when the multisets of their
``x_i`` agree.  Orbit representatives are therefore integer partitions of
``R`` (zero-padded to length ``k``), and the exact number of unlabeled response
shapes is the ordinary partition number ``p(R)``.  Because ``R<=k``, the usual
'at most k parts' restriction is automatic.

Consequences:

* ``R=0``: the labeled minimum response itself is unique and symmetric;
* ``R=1``: the labeled relation has ``k`` minimizers but one unlabeled orbit, so
  forgetting leaf identity makes the minimum response single-valued;
* ``R>=2``: identity coarsening alone leaves at least two response shapes, so a
  further selector/observable quotient or finer impulse policy is still needed;
* a coarse symmetric labeled minimum exists exactly for ``R in {0,k}``, but for
  ``R=k>=2`` the *whole* minimum relation still has ``p(k)>1`` unlabeled shapes.
  Existence of one symmetric minimizer must not be confused with a single-valued
  minimum relation.

The minimum symmetric refined impulse denominator also becomes purely residue
controlled:

    d_sym = k / gcd(k,R),

with ``gcd(k,0)=k``.  The denominator-scaled final contact-score surplus of that
symmetric minimum is

    R / gcd(k,R).

Hence the star response/precision pattern is periodic in ``q`` with period
``k+1`` after removing the uniform baseline.  This is a finite E001/P024
application of standard partition/permutation-orbit arithmetic; no novelty is
claimed for integer partitions or group actions themselves.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd

from .material_star_response_spectrum import (
    star_minimum_relation_parameters,
    star_minimum_symmetric_refinement,
    star_minimum_total_integer_relation,
)


def _require_star_inputs(leaf_count: int, closing_score: int) -> None:
    if isinstance(leaf_count, bool) or not isinstance(leaf_count, int) or leaf_count < 2:
        raise ValueError("leaf_count must be an integer at least two")
    if isinstance(closing_score, bool) or not isinstance(closing_score, int) or closing_score <= 0:
        raise ValueError("closing_score must be a positive integer")


def star_response_residue(
    leaf_count: int,
    closing_score: int,
) -> tuple[int, int]:
    """Return ``(uniform baseline b, residue R)`` for ``q=(k+1)b+R``."""
    _require_star_inputs(leaf_count, closing_score)
    baseline, residue = divmod(closing_score, leaf_count + 1)
    total, parent_baseline, parent_excess = star_minimum_relation_parameters(
        leaf_count, closing_score
    )
    if parent_baseline != baseline or parent_excess != residue:
        raise AssertionError("residue decomposition disagrees with parent star spectrum")
    if total != leaf_count * baseline + residue:
        raise AssertionError("minimum-total impulse lost residue normal form")
    return baseline, residue


def integer_partition_number(total: int) -> int:
    """Return the ordinary partition number ``p(total)`` by finite integer DP."""
    if isinstance(total, bool) or not isinstance(total, int) or total < 0:
        raise ValueError("total must be a non-negative integer")
    counts = [0] * (total + 1)
    counts[0] = 1
    for part in range(1, total + 1):
        for value in range(part, total + 1):
            counts[value] += counts[value - part]
    return counts[total]


def _partitions_nonincreasing(
    total: int,
    maximum_part: int | None = None,
) -> tuple[tuple[int, ...], ...]:
    if total == 0:
        return ((),)
    maximum = total if maximum_part is None else min(total, maximum_part)
    result: list[tuple[int, ...]] = []
    for first in range(maximum, 0, -1):
        for tail in _partitions_nonincreasing(total - first, first):
            result.append((first,) + tail)
    return tuple(result)


def star_minimum_unlabeled_response_shapes(
    leaf_count: int,
    closing_score: int,
) -> tuple[tuple[int, ...], ...]:
    """Return one sorted impulse vector for every full leaf-permutation orbit."""
    baseline, residue = star_response_residue(leaf_count, closing_score)
    shapes = tuple(
        tuple(baseline + value for value in partition)
        + (baseline,) * (leaf_count - len(partition))
        for partition in _partitions_nonincreasing(residue)
    )
    if len(shapes) != integer_partition_number(residue):
        raise AssertionError("unlabeled response shapes lost partition count")
    if any(tuple(sorted(shape, reverse=True)) != shape for shape in shapes):
        raise AssertionError("unlabeled response shape is not in canonical order")
    return shapes


def star_minimum_unlabeled_orbit_count(
    leaf_count: int,
    closing_score: int,
) -> int:
    """Return the exact number of minimum-response orbits under ``S_k``."""
    _, residue = star_response_residue(leaf_count, closing_score)
    return integer_partition_number(residue)


def star_identity_quotient_is_single_valued(
    leaf_count: int,
    closing_score: int,
) -> bool:
    """Whether forgetting leaf labels collapses the whole minimum relation to one shape."""
    _, residue = star_response_residue(leaf_count, closing_score)
    return residue <= 1


def star_coarse_symmetric_minimum_exists_from_residue(
    leaf_count: int,
    closing_score: int,
) -> bool:
    """Residue criterion for existence of one permutation-fixed coarse minimizer."""
    _, residue = star_response_residue(leaf_count, closing_score)
    return residue in (0, leaf_count)


def star_residue_symmetric_refinement(
    leaf_count: int,
    closing_score: int,
) -> tuple[int, int]:
    """Return ``(denominator, scaled final-score surplus)`` from the residue alone."""
    _, residue = star_response_residue(leaf_count, closing_score)
    divisor = gcd(leaf_count, residue)
    denominator = leaf_count // divisor
    surplus = residue // divisor
    parent_denominator, _ = star_minimum_symmetric_refinement(
        leaf_count, closing_score
    )
    if parent_denominator != denominator:
        raise AssertionError("residue refinement disagrees with parent star spectrum")
    return denominator, surplus


@dataclass(frozen=True)
class StarResponseQuotientReport:
    leaf_count: int
    closing_score: int
    uniform_baseline: int
    residue: int
    labeled_minimum_count: int
    unlabeled_orbit_count: int
    unlabeled_shapes: tuple[tuple[int, ...], ...]
    identity_quotient_single_valued: bool
    coarse_symmetric_minimum_exists: bool
    symmetric_refinement_denominator: int
    refined_final_score_surplus: int


def star_response_quotient_report(
    leaf_count: int,
    closing_score: int,
) -> StarResponseQuotientReport:
    baseline, residue = star_response_residue(leaf_count, closing_score)
    relation = star_minimum_total_integer_relation(leaf_count, closing_score)
    shapes = star_minimum_unlabeled_response_shapes(leaf_count, closing_score)
    denominator, surplus = star_residue_symmetric_refinement(
        leaf_count, closing_score
    )
    return StarResponseQuotientReport(
        leaf_count=leaf_count,
        closing_score=closing_score,
        uniform_baseline=baseline,
        residue=residue,
        labeled_minimum_count=len(relation),
        unlabeled_orbit_count=len(shapes),
        unlabeled_shapes=shapes,
        identity_quotient_single_valued=residue <= 1,
        coarse_symmetric_minimum_exists=residue in (0, leaf_count),
        symmetric_refinement_denominator=denominator,
        refined_final_score_surplus=surplus,
    )
