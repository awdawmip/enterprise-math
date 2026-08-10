"""Bridge R004 precision geometry to the threshold-record P016 premodel.

The previous threshold-record toy used an integer alternative separation
``delta``.  This module removes that independent coordinate in two declared
geometry families by setting ``delta`` equal to intrinsic graph distance:

- ordered one-axis precision refinement -> path distance;
- product of independent ordered precision axes -> L1 grid distance.

The resulting record overlap is therefore derived from geometry plus one record
resolution parameter.  This remains a physical-hypothesis bridge, not an
apparatus calibration or a derivation of quantum decoherence.
"""
from __future__ import annotations

from fractions import Fraction
from collections.abc import Sequence

from enterprise_math.precision_ordered_geometry import ordered_path_distance_for_scales
from enterprise_math.precision_product_geometry import product_grid_distance
from enterprise_math.precision_threshold_record import threshold_record_overlap


def _pos(value: int, name: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def path_geometric_record_overlap(
    left: int,
    right: int,
    scales: Sequence[int],
    record_resolution: int,
) -> Fraction:
    separation = ordered_path_distance_for_scales(left, right, scales)
    return threshold_record_overlap(separation, record_resolution)


def grid_geometric_record_overlap(
    left: tuple[int, ...],
    right: tuple[int, ...],
    axis_scales: Sequence[Sequence[int]],
    record_resolution: int,
) -> Fraction:
    separation = product_grid_distance(left, right, axis_scales)
    return threshold_record_overlap(separation, record_resolution)


def path_representative_visibility_region_excluded(
    left: int,
    right: int,
    scales: Sequence[int],
    record_resolution: int,
) -> bool:
    separation = ordered_path_distance_for_scales(left, right, scales)
    return 100 * separation > 91 * record_resolution


def grid_representative_visibility_region_excluded(
    left: tuple[int, ...],
    right: tuple[int, ...],
    axis_scales: Sequence[Sequence[int]],
    record_resolution: int,
) -> bool:
    separation = product_grid_distance(left, right, axis_scales)
    return 100 * separation > 91 * record_resolution


def overlap_from_distance(distance: int, record_resolution: int) -> Fraction:
    """Expose the task-relative isotropic law used by this bridge."""
    return threshold_record_overlap(distance, record_resolution)


def unordered_pair_count(size: int) -> int:
    _pos(size, "size")
    return size * (size - 1) // 2


def path_zero_overlap_pair_count(size: int, record_resolution: int) -> int:
    """Count unordered distinct pairs with graph distance >= record resolution.

    In the path ``P_size`` there are exactly ``size-s`` unordered pairs at
    distance ``s``.  Hence, when ``size>record_resolution``, the zero-overlap
    count is the finite triangular number

    ``(size-d)*(size-d+1)//2``.
    """
    _pos(size, "size")
    _pos(record_resolution, "record_resolution")
    remaining = size - record_resolution
    if remaining <= 0:
        return 0
    return remaining * (remaining + 1) // 2


def path_positive_overlap_pair_count(size: int, record_resolution: int) -> int:
    return unordered_pair_count(size) - path_zero_overlap_pair_count(
        size, record_resolution
    )


def path_zero_overlap_pair_fraction(size: int, record_resolution: int) -> Fraction:
    total = unordered_pair_count(size)
    if total == 0:
        return Fraction(0, 1)
    return Fraction(path_zero_overlap_pair_count(size, record_resolution), total)


def path_zero_overlap_fraction_monotone_step(
    size: int, record_resolution: int
) -> bool:
    """Check one exact finite growth step ``f(N+1)>=f(N)``.

    For ``N>=d`` and ``d>1`` the exact difference is

    ``2*(d-1)*(N-d+1)/(N*(N-1)*(N+1))``;

    the boundary cases are handled by the exact Fraction comparison.  No
    infinite-size limit is used.
    """
    _pos(size, "size")
    _pos(record_resolution, "record_resolution")
    return path_zero_overlap_pair_fraction(
        size + 1, record_resolution
    ) >= path_zero_overlap_pair_fraction(size, record_resolution)
