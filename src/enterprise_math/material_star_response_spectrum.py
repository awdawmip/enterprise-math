"""Exact minimum-response spectrum for a symmetric branching contact star.

This continues the q=1 symmetry/precision counterexample without changing the
contact-network mother algebra.  Let ``k>=2`` identical leaf contacts share one
center, all masses one, and let every initial contact score be the same closing
value ``-q`` with ``q>=1``.  The star Gram has diagonal two and off-diagonal one.
For one non-negative integer impulse vector ``j`` with total ``S``:

    r'_i = -q + S + j_i.

The minimum possible total impulse is

    S* = ceil(k*q/(k+1)).

Write

    b = q-S*,
    R = (k+1)S* - kq,     0 <= R <= k.

Then every minimum-total integer response, and only those responses, has

    j_i = b + x_i,
    x_i >= 0,
    sum_i x_i = R.

Hence the minimum-response relation contains exactly

    C(R+k-1, k-1)

labeled impulse vectors.  A coarse deterministic response preserving the full
leaf-permutation symmetry must be constant-coordinate.  Its least feasible
integer value is ``c=ceil(q/(k+1))``, with total ``k*c``.  It is also
minimum-total exactly when ``S*`` is divisible by ``k`` (equivalently the
minimum relation contains a constant vector).

At minimum-total level, the unique symmetric rational response has each contact
carry ``S*/k``.  In lowest terms its common denominator is

    k / gcd(k,S*).

Thus the impulse precision required to restore deterministic symmetry is a
number-theoretic function of the contact multiplicity and closing magnitude; it
need not always equal ``k``.  This is a finite lattice statement only.  A world
that actually delivers refined impulses must separately declare compatible
fine momentum state.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import comb, gcd


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _ceil_div(numerator: int, denominator: int) -> int:
    return (numerator + denominator - 1) // denominator


def star_minimum_total_impulse(leaf_count: int, closing_score: int) -> int:
    _require_positive("leaf_count", leaf_count)
    _require_positive("closing_score", closing_score)
    if leaf_count < 2:
        raise ValueError("leaf_count must be at least two")
    return _ceil_div(leaf_count * closing_score, leaf_count + 1)


def star_minimum_relation_parameters(
    leaf_count: int,
    closing_score: int,
) -> tuple[int, int, int]:
    """Return ``(S*, baseline b, excess-composition R)``."""
    total = star_minimum_total_impulse(leaf_count, closing_score)
    baseline = closing_score - total
    excess = (leaf_count + 1) * total - leaf_count * closing_score
    if baseline < 0 or not 0 <= excess <= leaf_count:
        raise AssertionError("star minimum-relation parameters left their exact range")
    return total, baseline, excess


def star_minimum_relation_cardinality(leaf_count: int, closing_score: int) -> int:
    _, _, excess = star_minimum_relation_parameters(leaf_count, closing_score)
    return comb(excess + leaf_count - 1, leaf_count - 1)


def _weak_compositions(total: int, length: int) -> tuple[tuple[int, ...], ...]:
    if length == 1:
        return ((total,),)
    result = []
    for first in range(total + 1):
        for tail in _weak_compositions(total - first, length - 1):
            result.append((first,) + tail)
    return tuple(result)


def star_minimum_total_integer_relation(
    leaf_count: int,
    closing_score: int,
) -> tuple[tuple[int, ...], ...]:
    """Enumerate the exact finite relation of labeled minimum-total responses."""
    total, baseline, excess = star_minimum_relation_parameters(
        leaf_count, closing_score
    )
    relation = tuple(
        tuple(baseline + value for value in composition)
        for composition in _weak_compositions(excess, leaf_count)
    )
    if len(relation) != star_minimum_relation_cardinality(leaf_count, closing_score):
        raise AssertionError("star relation enumeration disagrees with stars-and-bars count")
    if any(sum(vector) != total for vector in relation):
        raise AssertionError("star minimum relation lost total-impulse normalization")
    return relation


def star_score_vector(
    impulse_vector: tuple[int, ...] | list[int],
    closing_score: int,
) -> tuple[int, ...]:
    values = tuple(impulse_vector)
    if len(values) < 2:
        raise ValueError("star requires at least two contacts")
    _require_positive("closing_score", closing_score)
    if any(isinstance(value, bool) or not isinstance(value, int) or value < 0 for value in values):
        raise ValueError("impulse entries must be non-negative integers")
    total = sum(values)
    return tuple(-closing_score + total + value for value in values)


def star_minimum_symmetric_integer_total(leaf_count: int, closing_score: int) -> int:
    _require_positive("leaf_count", leaf_count)
    _require_positive("closing_score", closing_score)
    if leaf_count < 2:
        raise ValueError("leaf_count must be at least two")
    coordinate = _ceil_div(closing_score, leaf_count + 1)
    return leaf_count * coordinate


def star_minimum_total_has_symmetric_integer_selector(
    leaf_count: int,
    closing_score: int,
) -> bool:
    minimum = star_minimum_total_impulse(leaf_count, closing_score)
    return minimum % leaf_count == 0


def star_minimum_symmetric_refinement(
    leaf_count: int,
    closing_score: int,
) -> tuple[int, int]:
    """Return reduced ``(denominator, per-contact numerator)`` at minimum total."""
    minimum = star_minimum_total_impulse(leaf_count, closing_score)
    divisor = gcd(leaf_count, minimum)
    denominator = leaf_count // divisor
    numerator = minimum // divisor
    if leaf_count * numerator != denominator * minimum:
        raise AssertionError("symmetric refined impulse lost total normalization")
    return denominator, numerator


@dataclass(frozen=True)
class StarResponseSpectrumReport:
    leaf_count: int
    closing_score: int
    minimum_total_impulse: int
    baseline_impulse: int
    composition_excess: int
    minimum_relation_cardinality: int
    minimum_symmetric_integer_total: int
    coarse_symmetric_minimum_exists: bool
    refined_symmetric_denominator: int
    refined_per_contact_numerator: int
    refined_final_score_numerator: int

    @property
    def coarse_symmetry_overresponse(self) -> int:
        return self.minimum_symmetric_integer_total - self.minimum_total_impulse


def star_response_spectrum_report(
    leaf_count: int,
    closing_score: int,
) -> StarResponseSpectrumReport:
    total, baseline, excess = star_minimum_relation_parameters(
        leaf_count, closing_score
    )
    denominator, numerator = star_minimum_symmetric_refinement(
        leaf_count, closing_score
    )
    final_score_numerator = (
        -closing_score * denominator
        + (leaf_count + 1) * numerator
    )
    if final_score_numerator < 0:
        raise AssertionError("refined symmetric minimum response is not feasible")
    return StarResponseSpectrumReport(
        leaf_count=leaf_count,
        closing_score=closing_score,
        minimum_total_impulse=total,
        baseline_impulse=baseline,
        composition_excess=excess,
        minimum_relation_cardinality=star_minimum_relation_cardinality(
            leaf_count, closing_score
        ),
        minimum_symmetric_integer_total=star_minimum_symmetric_integer_total(
            leaf_count, closing_score
        ),
        coarse_symmetric_minimum_exists=star_minimum_total_has_symmetric_integer_selector(
            leaf_count, closing_score
        ),
        refined_symmetric_denominator=denominator,
        refined_per_contact_numerator=numerator,
        refined_final_score_numerator=final_score_numerator,
    )
