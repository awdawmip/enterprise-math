"""Task-relative support precision for A3 -> A4 -> P023.

For a partition of the A3 zero-relation quotient, the all-radius A4 MAY/MUST
query language has exact integer thresholds:

    d_minus(A,B) = min rho(x,y)
    d_plus(A,B)  = max rho(x,y)

across the fine quotient classes in coarse blocks A,B.

MAY_r is equivalent to d_minus <= r; MUST_r is equivalent to d_plus <= r.
The direct A3 coarse relation threshold is a different aggregate observable.
It is always <= d_plus, but has no universal order relation with d_minus.

This module keeps the computation integer-only and provides the concrete repair
coordinates used by the P023 future-compatibility reading.
"""

from __future__ import annotations

from dataclasses import dataclass

from .relation_support_bridge import (
    DistanceMatrix,
    integer_relation_distance_matrix,
    zero_relation_classes,
)
from .weighted_relation_field import WeightedField

ClassPartition = tuple[tuple[int, ...], ...]


@dataclass(frozen=True)
class SupportPrecisionProfile:
    """Finite all-radius MAY/MUST precision profile for one coarse partition."""

    may_threshold: DistanceMatrix
    must_threshold: DistanceMatrix
    uncertainty_width: DistanceMatrix
    coarse_threshold: DistanceMatrix
    hidden_must_defect: DistanceMatrix


def _require_class_partition(class_count: int, partition: ClassPartition) -> None:
    if not isinstance(partition, tuple) or not partition:
        raise ValueError("class partition must be a non-empty tuple")
    flattened: list[int] = []
    for group in partition:
        if not isinstance(group, tuple) or not group:
            raise ValueError("each class-partition group must be non-empty")
        if len(set(group)) != len(group):
            raise ValueError("class indices must be unique within a group")
        if any(
            isinstance(index, bool)
            or not isinstance(index, int)
            or index < 0
            or index >= class_count
            for index in group
        ):
            raise ValueError("class-partition index out of range")
        flattened.extend(group)
    if sorted(flattened) != list(range(class_count)):
        raise ValueError("class partition must cover every zero-relation class once")


def _raw_groups_from_class_partition(
    classes: tuple[tuple[int, ...], ...], partition: ClassPartition
) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(raw for class_index in group for raw in classes[class_index])
        for group in partition
    )


def support_threshold_matrices(
    block_sizes: tuple[int, ...],
    field: WeightedField,
    partition: ClassPartition,
) -> tuple[DistanceMatrix, DistanceMatrix]:
    """Return all-radius MAY and MUST thresholds (d_minus, d_plus)."""
    metric = integer_relation_distance_matrix(block_sizes, field)
    _require_class_partition(len(metric), partition)
    may_rows: list[tuple[int, ...]] = []
    must_rows: list[tuple[int, ...]] = []
    for left_group in partition:
        may_row: list[int] = []
        must_row: list[int] = []
        for right_group in partition:
            values = [metric[i][j] for i in left_group for j in right_group]
            may_row.append(min(values))
            must_row.append(max(values))
        may_rows.append(tuple(may_row))
        must_rows.append(tuple(must_row))
    return tuple(may_rows), tuple(must_rows)


def coarse_partition_threshold_matrix(
    block_sizes: tuple[int, ...],
    field: WeightedField,
    partition: ClassPartition,
) -> DistanceMatrix:
    """Return the direct threshold of the aggregated A3 coarse relation state."""
    classes = zero_relation_classes(block_sizes, field)
    _require_class_partition(len(classes), partition)
    raw_groups = _raw_groups_from_class_partition(classes, partition)
    rows: list[tuple[int, ...]] = []
    for left_group in raw_groups:
        row: list[int] = []
        left_size = sum(block_sizes[i] for i in left_group)
        for right_group in raw_groups:
            right_size = sum(block_sizes[j] for j in right_group)
            numerator = abs(
                sum(field[i][j] for i in left_group for j in right_group)
            )
            denominator = left_size * right_size
            row.append((numerator + denominator - 1) // denominator)
        rows.append(tuple(row))
    return tuple(rows)


def support_precision_profile(
    block_sizes: tuple[int, ...],
    field: WeightedField,
    partition: ClassPartition,
) -> SupportPrecisionProfile:
    """Build B10-B12 endpoint support precision coordinates."""
    may, must = support_threshold_matrices(block_sizes, field, partition)
    coarse = coarse_partition_threshold_matrix(block_sizes, field, partition)
    width_rows: list[tuple[int, ...]] = []
    defect_rows: list[tuple[int, ...]] = []
    for i in range(len(may)):
        width_row: list[int] = []
        defect_row: list[int] = []
        for j in range(len(may)):
            if may[i][j] > must[i][j]:
                raise AssertionError("MAY threshold cannot exceed MUST threshold")
            if coarse[i][j] > must[i][j]:
                raise AssertionError(
                    "direct coarse threshold cannot exceed universal fine threshold"
                )
            width_row.append(must[i][j] - may[i][j])
            defect_row.append(must[i][j] - coarse[i][j])
        width_rows.append(tuple(width_row))
        defect_rows.append(tuple(defect_row))
    return SupportPrecisionProfile(
        may_threshold=may,
        must_threshold=must,
        uncertainty_width=tuple(width_rows),
        coarse_threshold=coarse,
        hidden_must_defect=tuple(defect_rows),
    )


def may_supported(profile: SupportPrecisionProfile, left: int, right: int, radius: int) -> bool:
    """Answer an all-fine-state MAY query from its minimal threshold coordinate."""
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be a non-negative integer")
    return profile.may_threshold[left][right] <= radius


def must_supported(profile: SupportPrecisionProfile, left: int, right: int, radius: int) -> bool:
    """Answer an all-fine-state MUST query from its minimal threshold coordinate."""
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be a non-negative integer")
    return profile.must_threshold[left][right] <= radius
