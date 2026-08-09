"""Multibody common-collapse geometry for the current E001 square-support family.

General admissible-support relations need not be Helly: pairwise common targets
can fail to imply one target shared by the whole family.  The current E001
terminal supports are more special.  Every ``Body2D`` target set is an
axis-aligned integer rectangle, and finite families of such boxes have Helly
number 2.

Hence, for this geometry only, a pairwise collision clique is enough to certify
existence of one whole-family common target.  It is *not* enough to reconstruct
that common target box or its multiplicity; even the complete matrix of pairwise
common-target multiplicities can lose higher-order intersection information.

The exact whole-family box nevertheless has a compact certificate.  In n box
dimensions it is determined by at most ``2n`` extremal facets: the body/facet
attaining the maximum lower bound and minimum upper bound on each axis.  This
module records the 2D specialization with at most four deterministic facet
witnesses.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations

from .common_collapse import (
    Target2D,
    TargetBounds2D,
    common_collapse_collision,
    common_collapse_multiplicity,
    terminal_collapse_target_bounds,
)
from .engineering_collision import Body2D


@dataclass(frozen=True)
class MultiBodyCollapse2D:
    """Exact terminal target intersection of a finite square-body family."""

    body_ids: tuple[int, ...]
    bounds: TargetBounds2D
    x_count: int
    y_count: int
    target_count: int
    witness: Target2D


@dataclass(frozen=True, order=True)
class FacetWitness2D:
    """One extremal body facet that determines a whole-family intersection bound."""

    axis: str
    side: str
    body_id: int
    value: int


@dataclass(frozen=True)
class MultiBodyExtremalCertificate2D:
    """At-most-four-facet certificate reconstructing the exact common box."""

    body_ids: tuple[int, ...]
    bounds: TargetBounds2D
    facets: tuple[FacetWitness2D, ...]
    unique_witness_body_ids: tuple[int, ...]


def _validated_bodies(
    bodies: tuple[Body2D, ...] | list[Body2D],
) -> tuple[Body2D, ...]:
    items = tuple(bodies)
    if len(items) < 2:
        raise ValueError("multibody collapse requires at least two bodies")
    ids = [body.body_id for body in items]
    if len(ids) != len(set(ids)):
        raise ValueError("body ids must be unique")
    return tuple(sorted(items, key=lambda body: body.body_id))


def multibody_common_collapse_bounds(
    bodies: tuple[Body2D, ...] | list[Body2D],
) -> TargetBounds2D | None:
    """Return the exact intersection box of every body's terminal target set."""
    items = _validated_bodies(bodies)
    bounds = [terminal_collapse_target_bounds(body) for body in items]
    x_lo = max(bound[0] for bound in bounds)
    x_hi = min(bound[1] for bound in bounds)
    y_lo = max(bound[2] for bound in bounds)
    y_hi = min(bound[3] for bound in bounds)
    if x_lo > x_hi or y_lo > y_hi:
        return None
    return (x_lo, x_hi, y_lo, y_hi)


def pairwise_common_collapse_clique(
    bodies: tuple[Body2D, ...] | list[Body2D],
) -> bool:
    """Whether every body pair has a common terminal collapse target."""
    items = _validated_bodies(bodies)
    return all(
        common_collapse_collision(left, right)
        for left, right in combinations(items, 2)
    )


def pairwise_common_multiplicity_signature(
    bodies: tuple[Body2D, ...] | list[Body2D],
) -> tuple[tuple[int, int, int], ...]:
    """Return sorted ``(left_id,right_id,multiplicity)`` pair data."""
    items = _validated_bodies(bodies)
    return tuple(
        (
            left.body_id,
            right.body_id,
            common_collapse_multiplicity(left, right),
        )
        for left, right in combinations(items, 2)
    )


def box_helly_equivalence(
    bodies: tuple[Body2D, ...] | list[Body2D],
) -> bool:
    """Verify pairwise-clique iff whole-family intersection for E001 boxes."""
    items = _validated_bodies(bodies)
    pairwise = pairwise_common_collapse_clique(items)
    global_common = multibody_common_collapse_bounds(items) is not None
    return pairwise == global_common


def multibody_common_collapse_profile(
    bodies: tuple[Body2D, ...] | list[Body2D],
) -> MultiBodyCollapse2D | None:
    """Return common rectangle/multiplicity and assert the box-Helly specialization."""
    items = _validated_bodies(bodies)
    pairwise = pairwise_common_collapse_clique(items)
    bounds = multibody_common_collapse_bounds(items)
    if pairwise != (bounds is not None):
        raise AssertionError("axis-aligned E001 boxes violated their Helly-2 property")
    if bounds is None:
        return None
    x_lo, x_hi, y_lo, y_hi = bounds
    x_count = x_hi - x_lo + 1
    y_count = y_hi - y_lo + 1
    return MultiBodyCollapse2D(
        body_ids=tuple(body.body_id for body in items),
        bounds=bounds,
        x_count=x_count,
        y_count=y_count,
        target_count=x_count * y_count,
        witness=(x_lo, y_lo),
    )


def _extremal_witness(
    items: tuple[Body2D, ...],
    bound_index: int,
    choose_maximum: bool,
    axis: str,
    side: str,
) -> FacetWitness2D:
    candidates = [
        (terminal_collapse_target_bounds(body)[bound_index], body.body_id)
        for body in items
    ]
    extreme = (
        max(value for value, _body_id in candidates)
        if choose_maximum
        else min(value for value, _body_id in candidates)
    )
    body_id = min(body_id for value, body_id in candidates if value == extreme)
    return FacetWitness2D(axis=axis, side=side, body_id=body_id, value=extreme)


def reconstruct_common_bounds_from_certificate(
    certificate: MultiBodyExtremalCertificate2D,
) -> TargetBounds2D:
    """Reconstruct exact common bounds from four labeled extremal facet values."""
    by_label = {(facet.axis, facet.side): facet.value for facet in certificate.facets}
    required = (("x", "lo"), ("x", "hi"), ("y", "lo"), ("y", "hi"))
    if set(by_label) != set(required):
        raise ValueError("certificate must contain exactly one witness for each 2D bound")
    return (
        by_label[("x", "lo")],
        by_label[("x", "hi")],
        by_label[("y", "lo")],
        by_label[("y", "hi")],
    )


def multibody_extremal_certificate(
    bodies: tuple[Body2D, ...] | list[Body2D],
) -> MultiBodyExtremalCertificate2D | None:
    """Return deterministic <=4-body/facet certificate for a nonempty common box."""
    items = _validated_bodies(bodies)
    bounds = multibody_common_collapse_bounds(items)
    if bounds is None:
        return None
    facets = (
        _extremal_witness(items, 0, True, "x", "lo"),
        _extremal_witness(items, 1, False, "x", "hi"),
        _extremal_witness(items, 2, True, "y", "lo"),
        _extremal_witness(items, 3, False, "y", "hi"),
    )
    certificate = MultiBodyExtremalCertificate2D(
        body_ids=tuple(body.body_id for body in items),
        bounds=bounds,
        facets=facets,
        unique_witness_body_ids=tuple(sorted({facet.body_id for facet in facets})),
    )
    reconstructed = reconstruct_common_bounds_from_certificate(certificate)
    if reconstructed != bounds:
        raise AssertionError("extremal facet certificate failed exact box reconstruction")
    if len(certificate.unique_witness_body_ids) > 4:
        raise AssertionError("2D extremal certificate exceeded four witness bodies")
    return certificate
