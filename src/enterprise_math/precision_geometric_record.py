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
    """Expose the task-relative isotropic law used by this bridge.

    Geometry enters only through the intrinsic graph distance.  Hence equal
    distances are forced to have equal overlap inside this toy subfamily.
    """
    return threshold_record_overlap(distance, record_resolution)
