"""Finite common-collapse certificates for labeled axis-aligned integer boxes.

This module isolates the box geometry discovered in the E001 pressure test from
historical collision-engine types.  A box is a Cartesian product of inclusive
integer intervals.

Finite axis-aligned box families have Helly number 2: every pair intersects iff
the whole family intersects.  Therefore a pairwise collision clique is enough
to certify *existence* of a common target in this geometry.

Pairwise data is not enough to reconstruct higher-order target multiplicity.  A
whole-family intersection box is instead determined by ``2n`` extrema:
``max lower_j`` and ``min upper_j`` on each axis.  Those extrema admit compact,
deterministic facet witnesses.  If future operations may delete at most ``h``
boxes, retaining the first ``h+1`` candidates for each extremum is sufficient to
reconstruct every allowed future bound.

These are standard interval/order-statistic facts used as E001/A4/P023
specializations; no generic novelty is claimed.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations


@dataclass(frozen=True, order=True)
class LabeledIntegerBox:
    label: int
    lows: tuple[int, ...]
    highs: tuple[int, ...]

    def __post_init__(self) -> None:
        if isinstance(self.label, bool) or not isinstance(self.label, int):
            raise ValueError("box label must be an integer")
        if not self.lows or len(self.lows) != len(self.highs):
            raise ValueError("box lows/highs must have one equal positive dimension")
        for lo, hi in zip(self.lows, self.highs, strict=True):
            if any(isinstance(value, bool) or not isinstance(value, int) for value in (lo, hi)):
                raise ValueError("box bounds must be integers")
            if lo > hi:
                raise ValueError("box lower bounds must not exceed upper bounds")

    @property
    def dimension(self) -> int:
        return len(self.lows)

    @property
    def cardinality(self) -> int:
        result = 1
        for lo, hi in zip(self.lows, self.highs, strict=True):
            result *= hi - lo + 1
        return result


@dataclass(frozen=True, order=True)
class FacetWitness:
    axis: int
    side: str
    label: int
    value: int
    rank: int = 1


@dataclass(frozen=True)
class BoxIntersectionCertificate:
    labels: tuple[int, ...]
    common_box: LabeledIntegerBox
    facets: tuple[FacetWitness, ...]


@dataclass(frozen=True)
class DeletionSafeBoxCertificate:
    labels: tuple[int, ...]
    deletion_horizon: int
    candidates: tuple[FacetWitness, ...]


def _validated_family(
    boxes: tuple[LabeledIntegerBox, ...] | list[LabeledIntegerBox],
) -> tuple[LabeledIntegerBox, ...]:
    items = tuple(sorted(tuple(boxes), key=lambda box: box.label))
    if len(items) < 2:
        raise ValueError("box family requires at least two boxes")
    labels = [box.label for box in items]
    if len(labels) != len(set(labels)):
        raise ValueError("box labels must be unique")
    dimension = items[0].dimension
    if any(box.dimension != dimension for box in items):
        raise ValueError("all boxes must have the same dimension")
    return items


def intersect_boxes(
    boxes: tuple[LabeledIntegerBox, ...] | list[LabeledIntegerBox],
    result_label: int = -1,
) -> LabeledIntegerBox | None:
    """Return the exact whole-family inclusive integer intersection box."""
    items = _validated_family(boxes)
    lows = tuple(max(box.lows[axis] for box in items) for axis in range(items[0].dimension))
    highs = tuple(min(box.highs[axis] for box in items) for axis in range(items[0].dimension))
    if any(lo > hi for lo, hi in zip(lows, highs, strict=True)):
        return None
    return LabeledIntegerBox(result_label, lows, highs)


def pair_intersection_cardinality(left: LabeledIntegerBox, right: LabeledIntegerBox) -> int:
    """Return exact common-target count for one same-dimensional box pair."""
    if left.dimension != right.dimension:
        raise ValueError("box pair must have the same dimension")
    result = 1
    for axis in range(left.dimension):
        lo = max(left.lows[axis], right.lows[axis])
        hi = min(left.highs[axis], right.highs[axis])
        if lo > hi:
            return 0
        result *= hi - lo + 1
    return result


def pairwise_intersection_clique(
    boxes: tuple[LabeledIntegerBox, ...] | list[LabeledIntegerBox],
) -> bool:
    items = _validated_family(boxes)
    return all(
        pair_intersection_cardinality(left, right) > 0
        for left, right in combinations(items, 2)
    )


def pairwise_multiplicity_signature(
    boxes: tuple[LabeledIntegerBox, ...] | list[LabeledIntegerBox],
) -> tuple[tuple[int, int, int], ...]:
    items = _validated_family(boxes)
    return tuple(
        (left.label, right.label, pair_intersection_cardinality(left, right))
        for left, right in combinations(items, 2)
    )


def box_helly_equivalence(
    boxes: tuple[LabeledIntegerBox, ...] | list[LabeledIntegerBox],
) -> bool:
    """Verify pairwise intersection iff whole-family intersection for boxes."""
    items = _validated_family(boxes)
    return pairwise_intersection_clique(items) == (intersect_boxes(items) is not None)


def _extremal_facet(
    items: tuple[LabeledIntegerBox, ...],
    axis: int,
    side: str,
) -> FacetWitness:
    if side == "lo":
        extreme = max(box.lows[axis] for box in items)
        label = min(box.label for box in items if box.lows[axis] == extreme)
    elif side == "hi":
        extreme = min(box.highs[axis] for box in items)
        label = min(box.label for box in items if box.highs[axis] == extreme)
    else:
        raise ValueError("facet side must be lo or hi")
    return FacetWitness(axis=axis, side=side, label=label, value=extreme)


def extremal_intersection_certificate(
    boxes: tuple[LabeledIntegerBox, ...] | list[LabeledIntegerBox],
) -> BoxIntersectionCertificate | None:
    """Return the deterministic 2n-facet certificate for a nonempty common box."""
    items = _validated_family(boxes)
    common = intersect_boxes(items)
    if common is None:
        return None
    facets = tuple(
        facet
        for axis in range(items[0].dimension)
        for facet in (_extremal_facet(items, axis, "lo"), _extremal_facet(items, axis, "hi"))
    )
    reconstructed_lows = tuple(
        next(facet.value for facet in facets if facet.axis == axis and facet.side == "lo")
        for axis in range(items[0].dimension)
    )
    reconstructed_highs = tuple(
        next(facet.value for facet in facets if facet.axis == axis and facet.side == "hi")
        for axis in range(items[0].dimension)
    )
    if reconstructed_lows != common.lows or reconstructed_highs != common.highs:
        raise AssertionError("extremal certificate failed exact intersection reconstruction")
    return BoxIntersectionCertificate(
        labels=tuple(box.label for box in items),
        common_box=common,
        facets=facets,
    )


def _ranked_facet_candidates(
    items: tuple[LabeledIntegerBox, ...],
    axis: int,
    side: str,
    count: int,
) -> tuple[FacetWitness, ...]:
    if side == "lo":
        ordered = sorted(items, key=lambda box: (-box.lows[axis], box.label))
        value_of = lambda box: box.lows[axis]
    elif side == "hi":
        ordered = sorted(items, key=lambda box: (box.highs[axis], box.label))
        value_of = lambda box: box.highs[axis]
    else:
        raise ValueError("facet side must be lo or hi")
    return tuple(
        FacetWitness(axis=axis, side=side, label=box.label, value=value_of(box), rank=rank)
        for rank, box in enumerate(ordered[:count], start=1)
    )


def deletion_safe_intersection_certificate(
    boxes: tuple[LabeledIntegerBox, ...] | list[LabeledIntegerBox],
    deletion_horizon: int,
) -> DeletionSafeBoxCertificate:
    """Keep h+1 ranked candidates per bound for any future <=h deletions."""
    items = _validated_family(boxes)
    if (
        isinstance(deletion_horizon, bool)
        or not isinstance(deletion_horizon, int)
        or deletion_horizon < 0
    ):
        raise ValueError("deletion_horizon must be a non-negative integer")
    if deletion_horizon >= len(items):
        raise ValueError("deletion_horizon must leave at least one box")
    count = deletion_horizon + 1
    candidates = tuple(
        candidate
        for axis in range(items[0].dimension)
        for side in ("lo", "hi")
        for candidate in _ranked_facet_candidates(items, axis, side, count)
    )
    return DeletionSafeBoxCertificate(
        labels=tuple(box.label for box in items),
        deletion_horizon=deletion_horizon,
        candidates=candidates,
    )


def reconstruct_bounds_after_deletions(
    certificate: DeletionSafeBoxCertificate,
    removed_labels: frozenset[int] | set[int] | tuple[int, ...],
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Recover exact remaining-family extrema for any allowed removal set."""
    removed = frozenset(removed_labels)
    if not removed.issubset(certificate.labels):
        raise ValueError("removed labels must belong to the certified family")
    if len(removed) > certificate.deletion_horizon:
        raise ValueError("removal set exceeds certificate deletion horizon")
    if len(removed) == len(certificate.labels):
        raise ValueError("at least one box must remain")

    dimension = max(candidate.axis for candidate in certificate.candidates) + 1
    lows = []
    highs = []
    for axis in range(dimension):
        for side, target in (("lo", lows), ("hi", highs)):
            ranked = sorted(
                (
                    candidate
                    for candidate in certificate.candidates
                    if candidate.axis == axis and candidate.side == side
                ),
                key=lambda candidate: candidate.rank,
            )
            survivor = next(
                (candidate for candidate in ranked if candidate.label not in removed),
                None,
            )
            if survivor is None:
                raise AssertionError("h+1 candidates failed allowed-deletion coverage")
            target.append(survivor.value)
    return tuple(lows), tuple(highs)
