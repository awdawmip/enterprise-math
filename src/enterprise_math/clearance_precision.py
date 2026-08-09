"""Finite clearance-space quotients induced by declared future observables.

A clearance state is an n-tuple of non-negative integers inside one coarse
contact box ``{0,...,d-1}^n``.  The all-zero state is primitive contact and is
kept outside the positive coarse-only layer studied here.

For a positive clearance vector g, put ``q=max(g_i)`` and ``k=d-q``.  The scalar
``k`` is the minimum unit increase along one clearance coordinate needed to leave
the coarse contact box.  Different future languages require different exact
quotients:

* SCALAR_DEPTH: retain only k;
* ACTIVE_COUNT: also retain how many coordinates attain q;
* ACTIVE_SET: retain the exact nonempty set of coordinates attaining q;
* FULL_VECTOR: retain the complete clearance vector.

The exact class counts are ``d-1``, ``n(d-1)``, ``(2^n-1)(d-1)``, and
``d^n-1`` respectively.  This is an E001 specialization of future-compatible
quotient semantics, not a new generic quotient theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import comb

SCALAR_DEPTH = "SCALAR_DEPTH"
ACTIVE_COUNT = "ACTIVE_COUNT"
ACTIVE_SET = "ACTIVE_SET"
FULL_VECTOR = "FULL_VECTOR"


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def clearance_shell_multiplicity(
    dimension: int,
    collapse_factor: int,
    layer_depth: int,
) -> int:
    """Count positive clearance vectors on one scalar-depth shell."""
    _require_positive("dimension", dimension)
    _require_positive("collapse_factor", collapse_factor)
    _require_positive("layer_depth", layer_depth)
    if layer_depth >= collapse_factor:
        raise ValueError("positive coarse-only depth must be below collapse factor")
    q = collapse_factor - layer_depth
    return (q + 1) ** dimension - q**dimension


def active_axis_count_multiplicity(
    dimension: int,
    collapse_factor: int,
    layer_depth: int,
    active_axis_count: int,
) -> int:
    """Count shell states with exactly m coordinates attaining the maximum."""
    _require_positive("dimension", dimension)
    _require_positive("collapse_factor", collapse_factor)
    _require_positive("layer_depth", layer_depth)
    _require_positive("active_axis_count", active_axis_count)
    if layer_depth >= collapse_factor:
        raise ValueError("positive coarse-only depth must be below collapse factor")
    if active_axis_count > dimension:
        raise ValueError("active_axis_count must not exceed dimension")
    q = collapse_factor - layer_depth
    return comb(dimension, active_axis_count) * q ** (dimension - active_axis_count)


@dataclass(frozen=True)
class ClearancePrecisionClassCounts:
    dimension: int
    collapse_factor: int
    coarse_only_states: int
    scalar_depth_classes: int
    active_count_classes: int
    active_set_classes: int
    full_vector_classes: int


def clearance_precision_class_counts(
    dimension: int,
    collapse_factor: int,
) -> ClearancePrecisionClassCounts:
    """Return exact quotient sizes for four future-observable languages."""
    _require_positive("dimension", dimension)
    _require_positive("collapse_factor", collapse_factor)
    shell_count = collapse_factor - 1
    full = collapse_factor**dimension - 1
    return ClearancePrecisionClassCounts(
        dimension=dimension,
        collapse_factor=collapse_factor,
        coarse_only_states=full,
        scalar_depth_classes=shell_count,
        active_count_classes=dimension * shell_count,
        active_set_classes=(2**dimension - 1) * shell_count,
        full_vector_classes=full,
    )


def clearance_behavior_signature(
    clearance_vector: tuple[int, ...] | list[int],
    collapse_factor: int,
    mode: str,
) -> tuple[object, ...]:
    """Return the exact signature required by one declared future language."""
    _require_positive("collapse_factor", collapse_factor)
    vector = tuple(clearance_vector)
    if not vector:
        raise ValueError("clearance vector must be nonempty")
    for value in vector:
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError("clearance coordinates must be non-negative integers")
        if value >= collapse_factor:
            raise ValueError("clearance vector must lie inside the coarse contact box")
    q = max(vector)
    if q == 0:
        raise ValueError("primitive-contact origin is not a positive coarse-only state")

    depth = collapse_factor - q
    active = tuple(index for index, value in enumerate(vector) if value == q)
    if mode == SCALAR_DEPTH:
        return (depth,)
    if mode == ACTIVE_COUNT:
        return (depth, len(active))
    if mode == ACTIVE_SET:
        return (depth, active)
    if mode == FULL_VECTOR:
        return vector
    raise ValueError("unknown clearance future-observable mode")
