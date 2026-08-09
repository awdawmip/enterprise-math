"""Saved-state interaction-depth scheduling comparator for the impulse world.

No continuous path is reconstructed.  Given positive saved start/free-end wall
clearances ``g0,g1`` at collapse factor ``d``, define the endpoint layer depth

    k(g) = max(d-g, 0).

Two legal discrete sampling schedules are then:

* START_SAMPLE: use only ``k(g0)`` before the tick drift;
* FREE_PROPOSAL_SAMPLE: construct one free saved endpoint and use the deeper of
  the two saved endpoint layers, equivalently ``k(min(g0,g1))``.

The exact identity is

    k_proposal = max(k(g0), k(g1)) >= k_start.

The inequality is strict exactly when the free saved endpoint is closer to the
wall than the start and lies in a strictly deeper visible interaction layer.
Thus proposal sampling can enter a layer one tick earlier or read a deeper
material state during approach, but it does not turn an outside->outside high-
speed skip into a hidden collision when both endpoint gaps are resolved.

This module compares finite scheduling semantics only; it does not select one as
the canonical physical integrator.
"""

from __future__ import annotations

from dataclasses import dataclass

START_SAMPLE = "START_SAMPLE"
FREE_PROPOSAL_SAMPLE = "FREE_PROPOSAL_SAMPLE"


def endpoint_layer_depth(positive_gap: int, collapse_factor: int) -> int:
    """Return max(d-g,0) for a positive saved endpoint clearance."""
    if (
        isinstance(positive_gap, bool)
        or not isinstance(positive_gap, int)
        or positive_gap <= 0
    ):
        raise ValueError("positive_gap must be a positive integer")
    if (
        isinstance(collapse_factor, bool)
        or not isinstance(collapse_factor, int)
        or collapse_factor <= 0
    ):
        raise ValueError("collapse_factor must be a positive integer")
    return max(collapse_factor - positive_gap, 0)


@dataclass(frozen=True)
class ImpulseDepthScheduleComparison:
    start_gap: int
    free_end_gap: int
    collapse_factor: int
    start_depth: int
    free_end_depth: int
    proposal_depth: int
    proposal_is_deeper: bool
    both_endpoints_resolved: bool


def compare_impulse_depth_schedules(
    start_gap: int,
    free_end_gap: int,
    collapse_factor: int,
) -> ImpulseDepthScheduleComparison:
    """Compare start-sampled and two-saved-endpoint proposal depth semantics."""
    start_depth = endpoint_layer_depth(start_gap, collapse_factor)
    end_depth = endpoint_layer_depth(free_end_gap, collapse_factor)
    proposal_depth = endpoint_layer_depth(
        min(start_gap, free_end_gap),
        collapse_factor,
    )
    if proposal_depth != max(start_depth, end_depth):
        raise AssertionError("proposal depth failed max-of-endpoint-depth identity")
    if proposal_depth < start_depth:
        raise AssertionError("proposal schedule unexpectedly sampled shallower than start")
    strict_expected = free_end_gap < start_gap and end_depth > start_depth
    if (proposal_depth > start_depth) != strict_expected:
        raise AssertionError("strict schedule-depth criterion failed")
    return ImpulseDepthScheduleComparison(
        start_gap=start_gap,
        free_end_gap=free_end_gap,
        collapse_factor=collapse_factor,
        start_depth=start_depth,
        free_end_depth=end_depth,
        proposal_depth=proposal_depth,
        proposal_is_deeper=proposal_depth > start_depth,
        both_endpoints_resolved=start_depth == 0 and end_depth == 0,
    )
