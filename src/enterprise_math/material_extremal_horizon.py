"""Future-safe extremal certificates for multibody box contacts under deletions.

A current axis-aligned common box needs only one extremal facet per bound.  That
certificate is not sufficient if future operations may remove bodies: deleting
the current extremal witness exposes the next order statistic.

For a declared future horizon allowing at most ``h`` body deletions, keep the
first ``h+1`` ranked candidates for each lower/upper bound.  After any allowed
removal set, at least one retained candidate remains and the first surviving
candidate is exactly the new extremum.

In n dimensions this uses at most ``2*n*(h+1)`` facet records.  The count is
worst-case necessary when facet values are strictly ordered: after removing the
first ``h`` witnesses, the ``h+1``-st value determines the new bound.

This is an E001 box-contact specialization of future-language-relative state
retention, not a new generic order-statistics theorem.
"""

from __future__ import annotations

from dataclasses import dataclass

from .common_collapse import TargetBounds2D, terminal_collapse_target_bounds
from .engineering_collision import Body2D


@dataclass(frozen=True, order=True)
class RankedFacetCandidate2D:
    axis: str
    side: str
    rank: int
    body_id: int
    value: int


@dataclass(frozen=True)
class RemovalSafeExtremalCertificate2D:
    body_ids: tuple[int, ...]
    deletion_horizon: int
    candidates: tuple[RankedFacetCandidate2D, ...]


def _validate_bodies(
    bodies: tuple[Body2D, ...] | list[Body2D],
    deletion_horizon: int,
) -> tuple[Body2D, ...]:
    items = tuple(sorted(tuple(bodies), key=lambda body: body.body_id))
    if not items:
        raise ValueError("at least one body is required")
    ids = [body.body_id for body in items]
    if len(ids) != len(set(ids)):
        raise ValueError("body ids must be unique")
    if (
        isinstance(deletion_horizon, bool)
        or not isinstance(deletion_horizon, int)
        or deletion_horizon < 0
    ):
        raise ValueError("deletion_horizon must be a non-negative integer")
    if deletion_horizon >= len(items):
        raise ValueError("deletion_horizon must leave at least one body")
    return items


def _ranked_candidates(
    items: tuple[Body2D, ...],
    bound_index: int,
    axis: str,
    side: str,
    descending: bool,
    count: int,
) -> tuple[RankedFacetCandidate2D, ...]:
    values = [
        (terminal_collapse_target_bounds(body)[bound_index], body.body_id)
        for body in items
    ]
    values.sort(key=lambda item: ((-item[0] if descending else item[0]), item[1]))
    return tuple(
        RankedFacetCandidate2D(
            axis=axis,
            side=side,
            rank=rank,
            body_id=body_id,
            value=value,
        )
        for rank, (value, body_id) in enumerate(values[:count], start=1)
    )


def removal_safe_extremal_certificate(
    bodies: tuple[Body2D, ...] | list[Body2D],
    deletion_horizon: int,
) -> RemovalSafeExtremalCertificate2D:
    """Compile top/bottom ``h+1`` facet order statistics for each 2D bound."""
    items = _validate_bodies(bodies, deletion_horizon)
    count = deletion_horizon + 1
    candidates = (
        _ranked_candidates(items, 0, "x", "lo", True, count)
        + _ranked_candidates(items, 1, "x", "hi", False, count)
        + _ranked_candidates(items, 2, "y", "lo", True, count)
        + _ranked_candidates(items, 3, "y", "hi", False, count)
    )
    return RemovalSafeExtremalCertificate2D(
        body_ids=tuple(body.body_id for body in items),
        deletion_horizon=deletion_horizon,
        candidates=candidates,
    )


def reconstruct_bounds_after_removals(
    certificate: RemovalSafeExtremalCertificate2D,
    removed_body_ids: frozenset[int] | set[int] | tuple[int, ...],
) -> TargetBounds2D:
    """Recover exact remaining-body extrema for any allowed removal set."""
    removed = frozenset(removed_body_ids)
    if not removed.issubset(certificate.body_ids):
        raise ValueError("removed ids must belong to the certified body family")
    if len(removed) > certificate.deletion_horizon:
        raise ValueError("removal set exceeds certificate deletion horizon")
    if len(removed) == len(certificate.body_ids):
        raise ValueError("at least one body must remain")

    values: dict[tuple[str, str], int] = {}
    for label in (("x", "lo"), ("x", "hi"), ("y", "lo"), ("y", "hi")):
        ranked = sorted(
            (
                candidate
                for candidate in certificate.candidates
                if (candidate.axis, candidate.side) == label
            ),
            key=lambda candidate: candidate.rank,
        )
        survivor = next(
            (candidate for candidate in ranked if candidate.body_id not in removed),
            None,
        )
        if survivor is None:
            raise AssertionError("h+1 extremal candidates failed allowed-deletion coverage")
        values[label] = survivor.value
    return (
        values[("x", "lo")],
        values[("x", "hi")],
        values[("y", "lo")],
        values[("y", "hi")],
    )


def direct_remaining_bounds(
    bodies: tuple[Body2D, ...] | list[Body2D],
    removed_body_ids: frozenset[int] | set[int] | tuple[int, ...],
) -> TargetBounds2D:
    """Independent direct extrema used as an engineering differential oracle."""
    removed = frozenset(removed_body_ids)
    remaining = [body for body in bodies if body.body_id not in removed]
    if not remaining:
        raise ValueError("at least one body must remain")
    bounds = [terminal_collapse_target_bounds(body) for body in remaining]
    return (
        max(bound[0] for bound in bounds),
        min(bound[1] for bound in bounds),
        max(bound[2] for bound in bounds),
        min(bound[3] for bound in bounds),
    )
