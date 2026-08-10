"""Biaxial local-update laws for the P025 dyadic Ferrers precision boundary.

The Stage-93 state has three equivalent coordinates: threshold crossings,
per-node ranks, and a monotone H/V boundary word.

Adding one threshold is local in crossing coordinates but may rewrite a suffix
of node ranks.  Adding one orbit node is local in rank coordinates but may
resolve several previously infinite threshold crossings.  The boundary word is
symmetric: either extension is exactly one symbol insertion (V for a threshold,
H for an orbit node).

This module compares those exact update costs on arithmetic staircases.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .abc_dyadic_ferrers_boundary import ferrers_boundary_from_staircase
from .abc_dyadic_threshold_staircase import (
    DyadicThresholdStaircase,
    dyadic_threshold_staircase,
)


@dataclass(frozen=True)
class BoundaryAxisUpdate:
    extension_axis: str
    old_crossings: tuple[int | None, ...]
    new_crossings: tuple[int | None, ...]
    old_ranks: tuple[int, ...]
    new_ranks: tuple[int, ...]
    old_boundary_word: str
    new_boundary_word: str
    crossing_coordinate_write_count: int
    rank_coordinate_write_count: int
    inserted_boundary_symbol: str
    boundary_single_insertion_verified: bool


def _single_symbol_insertion(old: str, new: str, symbol: str) -> bool:
    if len(new) != len(old) + 1:
        return False
    return any(
        new[index] == symbol and new[:index] + new[index + 1 :] == old
        for index in range(len(new))
    )


def threshold_axis_extension(
    staircase: DyadicThresholdStaircase,
    new_threshold: Fraction,
) -> BoundaryAxisUpdate:
    """Insert one threshold and compare updates in the three dual coordinates."""
    if not isinstance(new_threshold, Fraction) or new_threshold <= 0:
        raise ValueError("new_threshold must be a positive Fraction")
    if new_threshold in staircase.thresholds:
        raise ValueError("new_threshold must not duplicate an existing threshold")
    thresholds = tuple(sorted((*staircase.thresholds, new_threshold)))
    inserted_index = thresholds.index(new_threshold)
    updated = dyadic_threshold_staircase(
        staircase.q,
        staircase.p,
        staircase.base_exponent,
        staircase.horizon_steps,
        thresholds,
    )
    old_boundary = ferrers_boundary_from_staircase(staircase)
    new_boundary = ferrers_boundary_from_staircase(updated)

    stripped_crossings = (
        updated.crossing_depths[:inserted_index]
        + updated.crossing_depths[inserted_index + 1 :]
    )
    if stripped_crossings != staircase.crossing_depths:
        raise AssertionError("threshold insertion changed old crossing coordinates")

    if len(old_boundary.node_ranks) != len(new_boundary.node_ranks):
        raise AssertionError("threshold extension changed orbit-node count")
    rank_writes = sum(
        old != new
        for old, new in zip(old_boundary.node_ranks, new_boundary.node_ranks)
    )
    crossing_writes = 1
    boundary_ok = _single_symbol_insertion(
        old_boundary.boundary_word, new_boundary.boundary_word, "V"
    )
    if not boundary_ok:
        raise AssertionError("threshold extension was not one V insertion")

    return BoundaryAxisUpdate(
        extension_axis="threshold",
        old_crossings=staircase.crossing_depths,
        new_crossings=updated.crossing_depths,
        old_ranks=old_boundary.node_ranks,
        new_ranks=new_boundary.node_ranks,
        old_boundary_word=old_boundary.boundary_word,
        new_boundary_word=new_boundary.boundary_word,
        crossing_coordinate_write_count=crossing_writes,
        rank_coordinate_write_count=rank_writes,
        inserted_boundary_symbol="V",
        boundary_single_insertion_verified=True,
    )


def orbit_axis_extension(
    staircase: DyadicThresholdStaircase,
) -> BoundaryAxisUpdate:
    """Append one dyadic orbit node and compare updates in the dual coordinates."""
    updated = dyadic_threshold_staircase(
        staircase.q,
        staircase.p,
        staircase.base_exponent,
        staircase.horizon_steps + 1,
        staircase.thresholds,
    )
    old_boundary = ferrers_boundary_from_staircase(staircase)
    new_boundary = ferrers_boundary_from_staircase(updated)

    if new_boundary.node_ranks[:-1] != old_boundary.node_ranks:
        raise AssertionError("orbit extension changed old node ranks")
    rank_writes = 1
    crossing_writes = sum(
        old != new
        for old, new in zip(staircase.crossing_depths, updated.crossing_depths)
    )
    for old, new in zip(staircase.crossing_depths, updated.crossing_depths):
        if old is not None and new != old:
            raise AssertionError("orbit extension changed an already finite crossing")
        if old is None and new is not None and new != staircase.horizon_steps + 1:
            raise AssertionError("new crossing must occur at the appended orbit depth")

    boundary_ok = _single_symbol_insertion(
        old_boundary.boundary_word, new_boundary.boundary_word, "H"
    )
    if not boundary_ok:
        raise AssertionError("orbit extension was not one H insertion")

    return BoundaryAxisUpdate(
        extension_axis="orbit",
        old_crossings=staircase.crossing_depths,
        new_crossings=updated.crossing_depths,
        old_ranks=old_boundary.node_ranks,
        new_ranks=new_boundary.node_ranks,
        old_boundary_word=old_boundary.boundary_word,
        new_boundary_word=new_boundary.boundary_word,
        crossing_coordinate_write_count=crossing_writes,
        rank_coordinate_write_count=rank_writes,
        inserted_boundary_symbol="H",
        boundary_single_insertion_verified=True,
    )
