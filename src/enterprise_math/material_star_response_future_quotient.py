"""Task-relative quotient structure of the E001 branching-star minimum relation.

This generation asks what becomes deterministic after the branching-star
minimum-response relation is quotiented by the exact symmetry of identical
leaves.  It consumes the denominator/residue phase from
``material_star_response_precision_phase`` and does not add a new response
selector.

At one precision phase write

    q*s = (k+1)*t + r,

and every minimum response as

    a_i = t + x_i,
    x_i >= 0,
    sum_i x_i = r.

Leaf permutations act only on the residual distribution ``x``.  Therefore one
minimum-response orbit is completely described by sorting the positive residual
entries in non-increasing order.  These orbit signatures are exactly the
integer partitions of ``r``.  Since the star phase always has ``0<=r<=k``, no
partition-length truncation is active, and the exact number of symmetry orbits
is the ordinary partition number ``p(r)``.

This yields three distinct determinism layers:

* ``r=0``: the minimum response is already unique on the labeled contact state;
* ``r=1``: there are ``k`` labeled minimum responses but only one
  leaf-permutation orbit, so the response is deterministic only after the
  declared symmetry quotient;
* ``r>=2``: at least two symmetry orbits remain, so even forgetting all leaf
  labels leaves a genuinely relation-valued minimum response.

The ``r=k`` phase is especially important.  A fully symmetric minimum response
exists (residual ``(1,...,1)``), but the concentrated residual ``(k,0,...,0)``
is also minimum.  They lie in different permutation orbits.  Thus

    a symmetry-preserving minimum representative exists

is strictly weaker than

    symmetry determines a unique minimum-response quotient state.

For ``r>=2`` all minimum responses have the same total residual ``r`` yet a
permutation-invariant future observable such as ``max(x_i)`` distinguishes the
concentrated partition ``(r)`` from ``(r-1,1)``.  Hence quotienting the response
state to total minimum impulse or total residual is not future-safe for the full
language of permutation-invariant contact-local observables.  The exact
permutation orbit is the natural complete signature for that declared symmetric
future language.

Integer partitions and finite group-orbit facts are standard prior art.  The
E001 value is the concrete response-language pressure test: labeled
non-determinism, quotient determinism, and set-valued dynamics after quotient
must not be conflated.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_star_response_precision_phase import (
    star_minimum_response_relation_at_precision,
    star_response_refinement_phase,
    star_symmetric_minimum_numerators,
)


def _partition_count(value: int) -> int:
    if value < 0:
        raise ValueError("partition value must be non-negative")
    counts = [0] * (value + 1)
    counts[0] = 1
    for part in range(1, value + 1):
        for total in range(part, value + 1):
            counts[total] += counts[total - part]
    return counts[value]


def star_residual_partition_signature(
    impulse_numerators: tuple[int, ...] | list[int],
    baseline: int,
) -> tuple[int, ...]:
    """Return the complete leaf-permutation orbit signature above ``baseline``."""
    values = tuple(impulse_numerators)
    if len(values) < 2:
        raise ValueError("star response requires at least two contacts")
    if isinstance(baseline, bool) or not isinstance(baseline, int) or baseline < 0:
        raise ValueError("baseline must be a non-negative integer")
    residual = tuple(value - baseline for value in values)
    if any(isinstance(value, bool) or not isinstance(value, int) or value < 0 for value in residual):
        raise ValueError("impulse vector must lie at or above the declared baseline")
    return tuple(sorted((value for value in residual if value), reverse=True))


def star_minimum_response_symmetry_orbits(
    leaf_count: int,
    closing_quantum: int,
    denominator: int,
) -> tuple[tuple[int, ...], ...]:
    """Return every residual partition signature of the minimum relation."""
    phase = star_response_refinement_phase(
        leaf_count, closing_quantum, denominator
    )
    relation = star_minimum_response_relation_at_precision(
        leaf_count, closing_quantum, denominator
    )
    signatures = {
        star_residual_partition_signature(vector, phase.quotient_level)
        for vector in relation
    }
    result = tuple(sorted(signatures, reverse=True))
    expected = _partition_count(phase.residue)
    if len(result) != expected:
        raise AssertionError("star symmetry-orbit count disagrees with partition number")
    for signature in result:
        if sum(signature) != phase.residue:
            raise AssertionError("star orbit signature lost residue total")
        if len(signature) > leaf_count:
            raise AssertionError("star orbit signature exceeds available contacts")
    return result


def star_permutation_invariant_residual_observables(
    impulse_numerators: tuple[int, ...] | list[int],
    baseline: int,
) -> tuple[int, int, int, tuple[int, ...]]:
    """Return simple symmetric observables plus the complete partition signature."""
    signature = star_residual_partition_signature(impulse_numerators, baseline)
    total = sum(signature)
    maximum = signature[0] if signature else 0
    nonzero_count = len(signature)
    square_sum = sum(value * value for value in signature)
    return total, maximum, square_sum, signature


@dataclass(frozen=True)
class StarResponseQuotientReport:
    leaf_count: int
    closing_quantum: int
    denominator: int
    residue: int
    labeled_minimum_count: int
    permutation_orbit_count: int
    orbit_signatures: tuple[tuple[int, ...], ...]
    symmetric_minimum_exists: bool
    symmetric_minimum_orbit: tuple[int, ...] | None

    @property
    def labeled_unique(self) -> bool:
        return self.labeled_minimum_count == 1

    @property
    def permutation_quotient_unique(self) -> bool:
        return self.permutation_orbit_count == 1

    @property
    def determinism_class(self) -> str:
        if self.labeled_unique:
            return "LABELED_UNIQUE"
        if self.permutation_quotient_unique:
            return "PERMUTATION_QUOTIENT_UNIQUE"
        return "RELATION_VALUED_AFTER_QUOTIENT"


def star_response_quotient_report(
    leaf_count: int,
    closing_quantum: int,
    denominator: int,
) -> StarResponseQuotientReport:
    """Classify labeled vs symmetry-quotient determinism at one precision phase."""
    phase = star_response_refinement_phase(
        leaf_count, closing_quantum, denominator
    )
    relation = star_minimum_response_relation_at_precision(
        leaf_count, closing_quantum, denominator
    )
    orbits = star_minimum_response_symmetry_orbits(
        leaf_count, closing_quantum, denominator
    )
    symmetric = star_symmetric_minimum_numerators(
        leaf_count, closing_quantum, denominator
    )
    symmetric_orbit = (
        None
        if symmetric is None
        else star_residual_partition_signature(
            symmetric, phase.quotient_level
        )
    )

    report = StarResponseQuotientReport(
        leaf_count=leaf_count,
        closing_quantum=closing_quantum,
        denominator=denominator,
        residue=phase.residue,
        labeled_minimum_count=len(relation),
        permutation_orbit_count=len(orbits),
        orbit_signatures=orbits,
        symmetric_minimum_exists=symmetric is not None,
        symmetric_minimum_orbit=symmetric_orbit,
    )

    expected_class = (
        "LABELED_UNIQUE"
        if phase.residue == 0
        else "PERMUTATION_QUOTIENT_UNIQUE"
        if phase.residue == 1
        else "RELATION_VALUED_AFTER_QUOTIENT"
    )
    if report.determinism_class != expected_class:
        raise AssertionError("star quotient determinism no longer follows residue class")
    return report
