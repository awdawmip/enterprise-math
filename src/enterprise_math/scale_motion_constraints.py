"""E001.9 scale-dependent binary MOVE/WAIT constraints from macro endpoint contact.

This module is an explicit engineering toy policy for the active precision-
inversion research direction.  It assigns no force/impulse law.  It asks only
whether the *resulting endpoint supports* of two action variants are collapsed
into macro contact at spatial factor ``d``.

For each body with a nonzero proposed primitive motion there are MOVE and WAIT
variants.  Pairwise endpoint macro contact induces the same binary clauses used
by E001.5:

* MOVE/MOVE contact -> mutex;
* MOVE_i/WAIT_j contact -> MOVE_i implies MOVE_j;
* conflict with an explicitly waiting body's WAIT endpoint -> forced wait.

WAIT/WAIT macro contact means the current coarse state is already invalid for
this hard-exclusion action language and must be repaired before evolution.

Because endpoint macro contact for primitive gap ``g`` is exactly ``g<d``, each
purely spatial clause has a finite refinement lifetime and can only disappear
as ``d`` decreases.  ``transition_aware_macro_constraints`` unions these coarse
endpoint clauses with E001's exact primitive transition-target constraints;
therefore atomic edge conflicts can survive after all sampled endpoint clauses
have extinguished.

The policy is a falsification/engineering probe, not a claim that natural
collisions must use hard exclusion or endpoint-only triggering.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations

from .collision_phase_diagram import macro_contact_from_gap, primitive_clearance
from .engineering_collision import Pair
from .motion_action_constraints import (
    BinaryMotionConstraintReport,
    binary_motion_constraints,
)
from .motion_collapse import BodyMotion2D


@dataclass(frozen=True)
class ScaleMotionConstraintReport:
    """Scale-tagged exact binary constraint report for the endpoint toy policy."""

    collapse_factor: int
    constraints: BinaryMotionConstraintReport


def _wait_variant(motion: BodyMotion2D) -> BodyMotion2D:
    return BodyMotion2D(motion.body, (0, 0))


def _endpoint_macro_conflict(
    left: BodyMotion2D,
    right: BodyMotion2D,
    collapse_factor: int,
) -> bool:
    gap = primitive_clearance(left.end_body, right.end_body)
    return macro_contact_from_gap(gap, collapse_factor)


def _merge_binary_reports(
    left: BinaryMotionConstraintReport,
    right: BinaryMotionConstraintReport,
) -> BinaryMotionConstraintReport:
    if left.moving_ids != right.moving_ids:
        raise ValueError("cannot merge constraint reports with different move variables")
    return BinaryMotionConstraintReport(
        moving_ids=left.moving_ids,
        forced_wait_ids=tuple(sorted(set(left.forced_wait_ids).union(right.forced_wait_ids))),
        mutex_pairs=tuple(sorted(set(left.mutex_pairs).union(right.mutex_pairs))),
        implications=tuple(sorted(set(left.implications).union(right.implications))),
    )


def sampled_endpoint_macro_constraints(
    motions: list[BodyMotion2D],
    collapse_factor: int,
) -> ScaleMotionConstraintReport:
    """Build scale-dependent binary constraints from endpoint macro contact only."""
    if (
        isinstance(collapse_factor, bool)
        or not isinstance(collapse_factor, int)
        or collapse_factor <= 0
    ):
        raise ValueError("collapse_factor must be a positive integer")
    ids = [motion.body_id for motion in motions]
    if len(ids) != len(set(ids)):
        raise ValueError("motion body ids must be unique")

    by_id = {motion.body_id: motion for motion in motions}
    waits = {body_id: _wait_variant(motion) for body_id, motion in by_id.items()}
    for left_id, right_id in combinations(sorted(by_id), 2):
        if _endpoint_macro_conflict(
            waits[left_id], waits[right_id], collapse_factor
        ):
            raise ValueError(
                "current endpoint supports are already macro-contact at this factor"
            )

    moving_ids = tuple(sorted(body_id for body_id, motion in by_id.items() if not motion.is_wait))
    moving_set = set(moving_ids)
    forced_waits: set[int] = set()
    mutex_pairs: set[Pair] = set()
    implications: set[tuple[int, int]] = set()

    for left_id, right_id in combinations(sorted(by_id), 2):
        left_moving = left_id in moving_set
        right_moving = right_id in moving_set
        left_move = by_id[left_id]
        right_move = by_id[right_id]
        left_wait = waits[left_id]
        right_wait = waits[right_id]

        if left_moving and right_moving:
            if _endpoint_macro_conflict(left_move, right_move, collapse_factor):
                mutex_pairs.add((left_id, right_id))
            if _endpoint_macro_conflict(left_move, right_wait, collapse_factor):
                implications.add((left_id, right_id))
            if _endpoint_macro_conflict(left_wait, right_move, collapse_factor):
                implications.add((right_id, left_id))
        elif left_moving:
            if _endpoint_macro_conflict(left_move, right_wait, collapse_factor):
                forced_waits.add(left_id)
        elif right_moving:
            if _endpoint_macro_conflict(left_wait, right_move, collapse_factor):
                forced_waits.add(right_id)

    return ScaleMotionConstraintReport(
        collapse_factor=collapse_factor,
        constraints=BinaryMotionConstraintReport(
            moving_ids=moving_ids,
            forced_wait_ids=tuple(sorted(forced_waits)),
            mutex_pairs=tuple(sorted(mutex_pairs)),
            implications=tuple(sorted(implications)),
        ),
    )


def transition_aware_macro_constraints(
    motions: list[BodyMotion2D],
    collapse_factor: int,
) -> ScaleMotionConstraintReport:
    """Union sampled-endpoint macro clauses with exact primitive transition clauses."""
    macro = sampled_endpoint_macro_constraints(motions, collapse_factor)
    transition = binary_motion_constraints(motions)
    return ScaleMotionConstraintReport(
        collapse_factor=collapse_factor,
        constraints=_merge_binary_reports(macro.constraints, transition),
    )


def endpoint_clause_finest_active_factor(primitive_endpoint_gap: int) -> int | None:
    """Finest spatial factor where an endpoint macro-contact clause is still active.

    ``None`` means primitive endpoint contact ``g=0`` persists at terminal
    factor 1.  Positive gap ``g`` gives activity exactly for ``d>=g+1``.
    """
    if (
        isinstance(primitive_endpoint_gap, bool)
        or not isinstance(primitive_endpoint_gap, int)
        or primitive_endpoint_gap < 0
    ):
        raise ValueError("primitive_endpoint_gap must be a non-negative integer")
    return None if primitive_endpoint_gap == 0 else primitive_endpoint_gap + 1
