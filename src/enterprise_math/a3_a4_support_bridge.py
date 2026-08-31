"""Thin bridge from canonical A3 weighted relation states to canonical A4 supports.

This module keeps only statements whose hypotheses genuinely mention both
owner structures.  Generic finite-relation composition, converse, common-target
logic, and support-family diagnostics are consumed from canonical A4 rather than
reimplemented here.

For positive A3 capacities ``m_i`` and a closed weighted field

    Z_ij = m_j*c_i - m_i*c_j,

define zero-relation classes by ``Z_ij = 0``.  On those classes, radius ``r``
generates the finite A4 support

    [i] R_r [j]  iff  |Z_ij| <= r*m_i*m_j.

The historical bridge established a one-way partition boundary: if every fine
pair across two coarse groups satisfies the radius bound, the aggregated coarse
relation satisfies it; the converse may fail because signed A3 relation entries
can cancel under aggregation.

This owner also records the exact future-language-dependent repair for repeated
merge/query words on fine normalized potentials ``rho_i=c_i/m_i``:

- universal all-pairs threshold language: the globally coarsest compositional
  block state is the interval hull ``[min rho, max rho]``;
- existential threshold language: the globally coarsest compositional block
  state is the exact set of distinct normalized potentials;
- if both languages are declared, exact support dominates because its interval
  hull is derived by min/max.

These are finite Enterprise specializations of standard interval/support
semantics. They are not language-independent claims about all A3/A4 quotients.
Filtered-relation mathematics itself is established prior art.
"""

from __future__ import annotations

from fractions import Fraction

from .admissible_support import (
    AdmissibleSupportReport,
    Relation,
    analyze_admissible_support_family,
    common_target_relation,
)
from .weighted_relation_field import WeightedField, weighted_relation_field_is_closed

PartitionBlock = tuple[int, ...]
IntervalHull = tuple[Fraction, Fraction]
PotentialSupport = frozenset[Fraction]


def _require_radius(radius: int) -> None:
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be a non-negative integer")


def _require_block_state(
    block_sizes: tuple[int, ...],
    totals: tuple[int, ...],
    block: PartitionBlock,
) -> None:
    if not isinstance(block_sizes, tuple) or not block_sizes:
        raise ValueError("block_sizes must be a non-empty tuple")
    if any(
        isinstance(size, bool) or not isinstance(size, int) or size <= 0
        for size in block_sizes
    ):
        raise ValueError("block sizes must be positive integers")
    if not isinstance(totals, tuple) or len(totals) != len(block_sizes):
        raise ValueError("totals must match block_sizes")
    if any(isinstance(total, bool) or not isinstance(total, int) for total in totals):
        raise ValueError("block totals must be integers")
    if not isinstance(block, tuple) or not block:
        raise ValueError("block must be a non-empty tuple of indices")
    if len(set(block)) != len(block):
        raise ValueError("block indices must be unique")
    if any(
        isinstance(index, bool)
        or not isinstance(index, int)
        or index < 0
        or index >= len(block_sizes)
        for index in block
    ):
        raise ValueError("block index out of range")


def _require_interval_hull(hull: IntervalHull) -> None:
    if not isinstance(hull, tuple) or len(hull) != 2:
        raise ValueError("interval hull must be a pair")
    if any(not isinstance(value, Fraction) for value in hull):
        raise ValueError("interval hull values must be Fractions")
    if hull[0] > hull[1]:
        raise ValueError("interval hull must be ordered")


def _require_potential_support(support: PotentialSupport) -> None:
    if not isinstance(support, frozenset) or not support:
        raise ValueError("potential support must be a non-empty frozenset")
    if any(not isinstance(value, Fraction) for value in support):
        raise ValueError("potential support values must be Fractions")


def zero_relation_classes(
    block_sizes: tuple[int, ...], field: WeightedField
) -> tuple[tuple[int, ...], ...]:
    """Return canonical A3 classes for ``i ~ j`` iff ``Z_ij = 0``."""
    if not weighted_relation_field_is_closed(block_sizes, field):
        raise ValueError("weighted relation field must be closed")
    unseen = set(range(len(block_sizes)))
    classes: list[tuple[int, ...]] = []
    while unseen:
        seed = min(unseen)
        group = tuple(index for index in sorted(unseen) if field[seed][index] == 0)
        if any(field[left][right] != 0 for left in group for right in group):
            raise AssertionError("zero relation must be transitive on a closed weighted field")
        classes.append(group)
        unseen.difference_update(group)
    return tuple(classes)


def generated_support_relation(
    block_sizes: tuple[int, ...], field: WeightedField, radius: int
) -> Relation:
    """Generate one A4 support relation from an A3 weighted relation field."""
    _require_radius(radius)
    classes = zero_relation_classes(block_sizes, field)
    relation: set[tuple[int, int]] = set()
    for left_class, left_members in enumerate(classes):
        for right_class, right_members in enumerate(classes):
            decisions = {
                abs(field[i][j]) <= radius * block_sizes[i] * block_sizes[j]
                for i in left_members
                for j in right_members
            }
            if len(decisions) != 1:
                raise AssertionError(
                    "generated support must be representative-independent on zero classes"
                )
            if True in decisions:
                relation.add((left_class, right_class))
    return frozenset(relation)


def generated_support_family(
    block_sizes: tuple[int, ...], field: WeightedField, max_radius: int
) -> dict[int, Relation]:
    """Return the finite radius family ``R_0,...,R_max_radius`` generated by A3."""
    _require_radius(max_radius)
    return {
        radius: generated_support_relation(block_sizes, field, radius)
        for radius in range(max_radius + 1)
    }


def generated_support_report(
    block_sizes: tuple[int, ...], field: WeightedField, max_radius: int
) -> AdmissibleSupportReport:
    """Audit the generated family through the canonical A4 contract."""
    classes = zero_relation_classes(block_sizes, field)
    family = generated_support_family(block_sizes, field, max_radius)
    return analyze_admissible_support_family(
        frozenset(range(len(classes))),
        family,
    )


def common_target_support(
    block_sizes: tuple[int, ...],
    field: WeightedField,
    left_radius: int,
    right_radius: int,
) -> Relation:
    """Return the canonical A4 common-target relation for the A3-generated family."""
    left = generated_support_relation(block_sizes, field, left_radius)
    right = generated_support_relation(block_sizes, field, right_radius)
    return common_target_relation(left, right)


def split_complete_at(
    block_sizes: tuple[int, ...],
    field: WeightedField,
    left_radius: int,
    right_radius: int,
) -> bool:
    """Check whether every combined-budget support pair has an intermediate class."""
    _require_radius(left_radius)
    _require_radius(right_radius)
    return common_target_support(
        block_sizes, field, left_radius, right_radius
    ) == generated_support_relation(
        block_sizes, field, left_radius + right_radius
    )


def missing_interpolations(
    block_sizes: tuple[int, ...],
    field: WeightedField,
    left_radius: int,
    right_radius: int,
) -> Relation:
    """Return total-budget endpoint pairs lacking an A4 split witness."""
    _require_radius(left_radius)
    _require_radius(right_radius)
    combined = generated_support_relation(
        block_sizes, field, left_radius + right_radius
    )
    witnessed = common_target_support(
        block_sizes, field, left_radius, right_radius
    )
    return frozenset(combined.difference(witnessed))


def all_cross_pairs_supported(
    block_sizes: tuple[int, ...],
    field: WeightedField,
    left_group: PartitionBlock,
    right_group: PartitionBlock,
    radius: int,
) -> bool:
    """Return whether every fine A3 cross-pair satisfies the A4 radius bound."""
    _require_radius(radius)
    return all(
        abs(field[i][j]) <= radius * block_sizes[i] * block_sizes[j]
        for i in left_group
        for j in right_group
    )


def coarse_pair_supported_from_partition(
    block_sizes: tuple[int, ...],
    field: WeightedField,
    left_group: PartitionBlock,
    right_group: PartitionBlock,
    radius: int,
) -> bool:
    """Evaluate the A4 radius bound after A3 partition aggregation."""
    _require_radius(radius)
    left_size = sum(block_sizes[i] for i in left_group)
    right_size = sum(block_sizes[j] for j in right_group)
    coarse_relation = sum(field[i][j] for i in left_group for j in right_group)
    return abs(coarse_relation) <= radius * left_size * right_size


def universal_fine_support_implies_coarse_support(
    block_sizes: tuple[int, ...],
    field: WeightedField,
    left_group: PartitionBlock,
    right_group: PartitionBlock,
    radius: int,
) -> bool:
    """Audit the one-way A3 partition -> A4 support compatibility statement."""
    if not all_cross_pairs_supported(
        block_sizes, field, left_group, right_group, radius
    ):
        return True
    return coarse_pair_supported_from_partition(
        block_sizes, field, left_group, right_group, radius
    )


def existential_threshold_block_state(
    block_sizes: tuple[int, ...],
    totals: tuple[int, ...],
    block: PartitionBlock,
) -> PotentialSupport:
    """Exact compositional state for the existential threshold future language.

    The declared language may repeatedly merge blocks and ask, at any integer
    radius ``r``, whether at least one fine pair across two current blocks has
    ``|rho_i-rho_j| <= r``.  The globally coarsest contextual congruence for
    that language is equality of the set of distinct normalized potentials.
    Radius-zero singleton probes recover support membership exactly.
    """
    _require_block_state(block_sizes, totals, block)
    return frozenset(Fraction(totals[index], block_sizes[index]) for index in block)


def interval_hull_from_potential_support(support: PotentialSupport) -> IntervalHull:
    """Derive the universal-language interval hull from exact potential support."""
    _require_potential_support(support)
    return min(support), max(support)


def universal_threshold_block_state(
    block_sizes: tuple[int, ...],
    totals: tuple[int, ...],
    block: PartitionBlock,
) -> IntervalHull:
    """Globally coarsest compositional state for universal all-pairs thresholds.

    The declared language may repeatedly merge blocks and ask, at any integer
    radius ``r``, whether every fine cross-pair satisfies
    ``|rho_i-rho_j| <= r``.  Equality of interval hulls is the globally coarsest
    contextual congruence for that language.
    """
    return interval_hull_from_potential_support(
        existential_threshold_block_state(block_sizes, totals, block)
    )


def merge_existential_threshold_states(
    left: PotentialSupport,
    right: PotentialSupport,
) -> PotentialSupport:
    """Merge existential-language block states by exact support union."""
    _require_potential_support(left)
    _require_potential_support(right)
    return left | right


def merge_universal_threshold_states(
    left: IntervalHull,
    right: IntervalHull,
) -> IntervalHull:
    """Merge universal-language block states by interval hull union."""
    _require_interval_hull(left)
    _require_interval_hull(right)
    return min(left[0], right[0]), max(left[1], right[1])


def existential_threshold_query(
    left: PotentialSupport,
    right: PotentialSupport,
    radius: int,
) -> bool:
    """Evaluate the declared existential threshold query from support states."""
    _require_potential_support(left)
    _require_potential_support(right)
    _require_radius(radius)
    return min(abs(left_value - right_value) for left_value in left for right_value in right) <= radius


def universal_threshold_query(
    left: IntervalHull,
    right: IntervalHull,
    radius: int,
) -> bool:
    """Evaluate the declared universal all-pairs query from interval hulls."""
    _require_interval_hull(left)
    _require_interval_hull(right)
    _require_radius(radius)
    max_distance = max(left[1] - right[0], right[1] - left[0])
    return max_distance <= radius
