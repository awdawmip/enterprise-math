"""Future-language precision hierarchy for multidimensional coarse-clearance shells.

Inside the positive coarse-only contact box ``{0,...,d-1}^n \ {0}``, different
future observables require different exact quotients:

* SCALAR_DEPTH keeps only ``k=d-max(g_i)``;
* ACTIVE_COUNT also keeps how many coordinates attain the maximum;
* ACTIVE_SET keeps the exact nonempty set of maximal coordinates;
* FULL_VECTOR keeps the complete clearance vector.

For ``d>=1`` the exact numbers of coarse-only behavior classes are

    scalar depth : (d-1)
    active count : n*(d-1)
    active set   : (2^n-1)*(d-1)
    full vector  : d^n-1.

The formulas hold because every positive shell ``q=max(g_i)`` realizes every
nonempty active-coordinate subset: set coordinates in the subset to ``q`` and
all others below ``q``.  This module is an E001 specialization of the project's
future-compatible quotient viewpoint, not a new generic quotient theory.
"""

from __future__ import annotations

from dataclasses import dataclass

SCALAR_DEPTH = "SCALAR_DEPTH"
ACTIVE_COUNT = "ACTIVE_COUNT"
ACTIVE_SET = "ACTIVE_SET"
FULL_VECTOR = "FULL_VECTOR"


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


@dataclass(frozen=True)
class ClearancePrecisionClassCounts:
    """Exact class counts for four future-observable languages."""

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
    """Return exact quotient sizes on the positive coarse-only clearance box."""
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
    """Return the exact behavior signature for one declared future language.

    The input must be a positive coarse-only clearance vector: every coordinate
    lies in ``0..d-1`` and at least one coordinate is positive.  Primitive
    contact and resolved states belong to separate outer classifications.
    """
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
        raise ValueError("primitive-contact origin is not a coarse-only clearance state")

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
