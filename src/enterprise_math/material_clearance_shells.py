"""Finite clearance-space shells induced by E001 spatial collapse precision.

For an n-dimensional non-negative primitive clearance vector

    g = (g_1,...,g_n)

and spatial collapse factor ``d``, coarse contact means every coordinate is
strictly below ``d``.  Primitive contact is the all-zero vector and is kept
separate from the coarse-only material layer.

For a positive coarse-only clearance vector define

    q = max_i g_i,
    k = d-q.

``k`` is the minimum number of unit increases along one clearance coordinate
needed to leave the coarse contact box.  It is therefore the scalar escape-depth
observable used by the current isotropic material toy model.

All clearance vectors on the same depth shell have ``max_i g_i=q``.  Their exact
multiplicity is

    (q+1)^n - q^n.

If exactly ``m`` coordinates attain the maximum, their total multiplicity is

    C(n,m) * q^(n-m).

For one specific active-coordinate subset of size ``m`` the multiplicity is
``q^(n-m)``.  These formulas quantify exactly how much directional witness is
lost when a multidimensional clearance state is collapsed to scalar material
depth alone.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import comb

from .engineering_collision import Body2D, Pair

PRIMITIVE_CONTACT = "PRIMITIVE_CONTACT"
COARSE_ONLY_CONTACT = "COARSE_ONLY_CONTACT"
RESOLVED = "RESOLVED"


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def clearance_shell_multiplicity(
    dimension: int,
    collapse_factor: int,
    layer_depth: int,
) -> int:
    """Count clearance vectors on one positive coarse-only scalar-depth shell."""
    _require_positive("dimension", dimension)
    _require_positive("collapse_factor", collapse_factor)
    _require_positive("layer_depth", layer_depth)
    if layer_depth >= collapse_factor:
        raise ValueError("coarse-only layer depth must be strictly below collapse factor")
    q = collapse_factor - layer_depth
    return (q + 1) ** dimension - q**dimension


def active_axis_count_multiplicity(
    dimension: int,
    collapse_factor: int,
    layer_depth: int,
    active_axis_count: int,
) -> int:
    """Count shell states having exactly ``active_axis_count`` maximal coordinates."""
    _require_positive("dimension", dimension)
    _require_positive("collapse_factor", collapse_factor)
    _require_positive("layer_depth", layer_depth)
    _require_positive("active_axis_count", active_axis_count)
    if layer_depth >= collapse_factor:
        raise ValueError("coarse-only layer depth must be strictly below collapse factor")
    if active_axis_count > dimension:
        raise ValueError("active_axis_count must not exceed dimension")
    q = collapse_factor - layer_depth
    return comb(dimension, active_axis_count) * q ** (dimension - active_axis_count)


def specific_active_set_multiplicity(
    dimension: int,
    collapse_factor: int,
    layer_depth: int,
    active_axis_count: int,
) -> int:
    """Count shell states for one fixed active-axis subset of declared size."""
    total = active_axis_count_multiplicity(
        dimension,
        collapse_factor,
        layer_depth,
        active_axis_count,
    )
    return total // comb(dimension, active_axis_count)


def axis_clearances_2d(left: Body2D, right: Body2D) -> tuple[int, int]:
    """Return terminal x/y clearances between current E001 square supports."""
    if left.body_id == right.body_id:
        raise ValueError("clearance pair must contain distinct body ids")
    radius_sum = left.radius + right.radius
    return (
        max(0, abs(left.x - right.x) - radius_sum),
        max(0, abs(left.y - right.y) - radius_sum),
    )


@dataclass(frozen=True)
class ClearanceLayerSignature2D:
    """2D coarse-contact signature with scalar and directional escape witnesses."""

    pair: Pair
    collapse_factor: int
    axis_clearances: tuple[int, int]
    chebyshev_clearance: int
    status: str
    layer_depth: int | None
    axis_margins: tuple[int, int] | None
    active_axes: tuple[str, ...]
    shell_multiplicity: int | None
    specific_active_set_multiplicity: int | None


def clearance_layer_signature_2d(
    left: Body2D,
    right: Body2D,
    collapse_factor: int,
) -> ClearanceLayerSignature2D:
    """Lift scalar E001 gap-collapse contact to a 2D clearance-space signature."""
    _require_positive("collapse_factor", collapse_factor)
    gx, gy = axis_clearances_2d(left, right)
    gap = max(gx, gy)
    pair = tuple(sorted((left.body_id, right.body_id)))

    if gap == 0:
        return ClearanceLayerSignature2D(
            pair=pair,
            collapse_factor=collapse_factor,
            axis_clearances=(gx, gy),
            chebyshev_clearance=0,
            status=PRIMITIVE_CONTACT,
            layer_depth=None,
            axis_margins=None,
            active_axes=(),
            shell_multiplicity=None,
            specific_active_set_multiplicity=None,
        )
    if gap >= collapse_factor:
        return ClearanceLayerSignature2D(
            pair=pair,
            collapse_factor=collapse_factor,
            axis_clearances=(gx, gy),
            chebyshev_clearance=gap,
            status=RESOLVED,
            layer_depth=None,
            axis_margins=None,
            active_axes=(),
            shell_multiplicity=None,
            specific_active_set_multiplicity=None,
        )

    margins = (collapse_factor - gx, collapse_factor - gy)
    depth = min(margins)
    if depth != collapse_factor - gap:
        raise AssertionError("2D clearance margins disagree with scalar escape depth")
    active_axes = tuple(
        axis
        for axis, margin in (("x", margins[0]), ("y", margins[1]))
        if margin == depth
    )
    shell_count = clearance_shell_multiplicity(2, collapse_factor, depth)
    active_count = specific_active_set_multiplicity(
        2,
        collapse_factor,
        depth,
        len(active_axes),
    )
    return ClearanceLayerSignature2D(
        pair=pair,
        collapse_factor=collapse_factor,
        axis_clearances=(gx, gy),
        chebyshev_clearance=gap,
        status=COARSE_ONLY_CONTACT,
        layer_depth=depth,
        axis_margins=margins,
        active_axes=active_axes,
        shell_multiplicity=shell_count,
        specific_active_set_multiplicity=active_count,
    )
