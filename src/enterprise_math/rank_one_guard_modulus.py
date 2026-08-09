"""Canonical modulus refinements for rank-one A3 guard-image lattices.

For a parent partition with W(K_P)=Z*h, every fine coordinate inside one
parent block has an integer hidden label lambda_i relative to a block anchor:

    W_i - W_anchor = lambda_i * h.

To force a child guard image inside q*Z*h, coordinates that remain in one child
block must have equal labels modulo q. Splitting every parent block by these
residue classes is therefore the coarsest partition with that divisibility
property.
"""

from __future__ import annotations

from .guard_image_lattice import GuardFamily, guard_rank_one_step
from .linear_relation_quotient import Partition


def _require_modulus(modulus: int) -> None:
    if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus <= 0:
        raise ValueError("modulus must be a positive integer")


def rank_one_guard_labels(
    guards: GuardFamily, parent_partition: Partition
) -> tuple[tuple[tuple[int, int], ...], ...]:
    """Return `(coordinate,label)` pairs in each parent block."""
    parent_step = guard_rank_one_step(guards, parent_partition)
    pivot = next(index for index, value in enumerate(parent_step) if value != 0)
    result = []
    for group in parent_partition:
        anchor = group[0]
        labels = [(anchor, 0)]
        for coordinate in group[1:]:
            difference = tuple(
                guard[coordinate] - guard[anchor]
                for guard in guards
            )
            if difference[pivot] % parent_step[pivot] != 0:
                raise AssertionError("rank-one coefficient difference must be a multiple of parent step")
            label = difference[pivot] // parent_step[pivot]
            if tuple(label * value for value in parent_step) != difference:
                raise AssertionError("rank-one hidden label reconstruction failed")
            labels.append((coordinate, label))
        result.append(tuple(labels))
    return tuple(result)


def rank_one_modulus_refinement(
    guards: GuardFamily,
    parent_partition: Partition,
    modulus: int,
) -> Partition:
    """Coarsest refinement whose guard image lies inside modulus * W(K_parent)."""
    _require_modulus(modulus)
    labeled_groups = rank_one_guard_labels(guards, parent_partition)
    refined = []
    for group in labeled_groups:
        buckets: dict[int, list[int]] = {}
        order = []
        for coordinate, label in group:
            residue = label % modulus
            if residue not in buckets:
                buckets[residue] = []
                order.append(residue)
            buckets[residue].append(coordinate)
        refined.extend(tuple(buckets[residue]) for residue in order)
    return tuple(refined)


def rank_one_modulus_visibility_bound(
    guards: GuardFamily, parent_partition: Partition
) -> int:
    """A finite modulus after which residue refinement equals label equality.

    If q is larger than every within-parent-block label span, two unequal labels
    cannot be congruent modulo q. Thus all q>=returned bound produce the same
    label-equality refinement (the guard-visible refinement relative to the
    already-separated parent blocks).
    """
    labeled_groups = rank_one_guard_labels(guards, parent_partition)
    maximum_span = 0
    for group in labeled_groups:
        values = [label for _, label in group]
        maximum_span = max(maximum_span, max(values) - min(values))
    return maximum_span + 1
