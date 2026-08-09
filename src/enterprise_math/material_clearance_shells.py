"""Generic finite clearance-space shells for E001 material interaction layers.

This module is deliberately independent of any concrete collision-body type.
A clearance state is a nonempty tuple of non-negative primitive coordinate
clearances.  For spatial collapse factor ``d``:

* the all-zero vector is primitive contact;
* a positive vector with ``max(g)<d`` is coarse-only contact;
* a vector with ``max(g)>=d`` is resolved at this spatial precision.

For positive coarse-only contact define ``q=max(g)`` and escape depth ``k=d-q``.
All vectors on one depth shell have exact multiplicity

    (q+1)^n - q^n.

Exactly ``m`` maximal coordinates occur with multiplicity

    C(n,m) q^(n-m).

Concrete body/geometry adapters belong outside this module so the material
response spectrum does not depend on the historical E001 terminal collision
engine.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import comb

PRIMITIVE_CONTACT = "PRIMITIVE_CONTACT"
COARSE_ONLY_CONTACT = "COARSE_ONLY_CONTACT"
RESOLVED = "RESOLVED"


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _validated_clearances(clearances: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    values = tuple(clearances)
    if not values:
        raise ValueError("clearance vector must be nonempty")
    for value in values:
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError("clearance coordinates must be non-negative integers")
    return values


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
    """Count shell states for one fixed active-coordinate subset of declared size."""
    total = active_axis_count_multiplicity(
        dimension,
        collapse_factor,
        layer_depth,
        active_axis_count,
    )
    return total // comb(dimension, active_axis_count)


@dataclass(frozen=True)
class ClearanceLayerSignature:
    """Generic nD coarse-contact signature with scalar and directional witnesses."""

    collapse_factor: int
    clearances: tuple[int, ...]
    max_clearance: int
    status: str
    layer_depth: int | None
    axis_margins: tuple[int, ...] | None
    active_indices: tuple[int, ...]
    shell_multiplicity: int | None
    specific_active_set_multiplicity: int | None

    @property
    def dimension(self) -> int:
        return len(self.clearances)


def clearance_layer_signature(
    clearances: tuple[int, ...] | list[int],
    collapse_factor: int,
) -> ClearanceLayerSignature:
    """Classify one primitive clearance vector without any body-specific adapter."""
    _require_positive("collapse_factor", collapse_factor)
    values = _validated_clearances(clearances)
    gap = max(values)

    if gap == 0:
        return ClearanceLayerSignature(
            collapse_factor=collapse_factor,
            clearances=values,
            max_clearance=0,
            status=PRIMITIVE_CONTACT,
            layer_depth=None,
            axis_margins=None,
            active_indices=(),
            shell_multiplicity=None,
            specific_active_set_multiplicity=None,
        )
    if gap >= collapse_factor:
        return ClearanceLayerSignature(
            collapse_factor=collapse_factor,
            clearances=values,
            max_clearance=gap,
            status=RESOLVED,
            layer_depth=None,
            axis_margins=None,
            active_indices=(),
            shell_multiplicity=None,
            specific_active_set_multiplicity=None,
        )

    margins = tuple(collapse_factor - value for value in values)
    depth = min(margins)
    if depth != collapse_factor - gap:
        raise AssertionError("clearance margins disagree with scalar escape depth")
    active = tuple(index for index, margin in enumerate(margins) if margin == depth)
    dimension = len(values)
    return ClearanceLayerSignature(
        collapse_factor=collapse_factor,
        clearances=values,
        max_clearance=gap,
        status=COARSE_ONLY_CONTACT,
        layer_depth=depth,
        axis_margins=margins,
        active_indices=active,
        shell_multiplicity=clearance_shell_multiplicity(
            dimension, collapse_factor, depth
        ),
        specific_active_set_multiplicity=specific_active_set_multiplicity(
            dimension, collapse_factor, depth, len(active)
        ),
    )
