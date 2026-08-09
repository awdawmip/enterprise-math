"""E001.4 primitive motion conflicts as shared finite transition targets.

Static support overlap is not enough to describe a discrete transition.  Two
point bodies can swap adjacent vertices in one tick: their final supports are
disjoint, yet both traverse the same atomic edge in opposite directions.

For the E001 pressure test, one primitive center step has each coordinate in
``{-1, 0, 1}``, matching the 8-neighbor integer geometry already used to derive
square supports.  A moving body emits two kinds of finite transition targets:

* ``("vertex", z)`` for every terminal support cell occupied at the end;
* ``("edge", {z0,z1})`` for every terminal support cell translated along one
  nonzero primitive edge during the tick.

Two motions conflict exactly when these finite target sets intersect.  This
recovers endpoint-support conflicts and atomic edge-swap conflicts in one
common-target formulation.  Distinct geometric edges that merely cross in an
external embedding are *not* identified unless the primitive geometry itself
adds a shared transition target; no hidden continuum is assumed.

Vertex/edge conflicts and maximum conflict-free move selection are established
multi-agent path-finding ideas.  This module is an engineering pressure test of
how they fit the Enterprise Math finite-support/common-collapse representation,
not a novelty claim for MAPF.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations

from .common_collapse import iter_terminal_collapse_targets
from .engineering_collision import Body2D, Pair

Vector2D = tuple[int, int]
Point2D = tuple[int, int]
MotionTarget = tuple[str, object]


def _validate_step(step: Vector2D) -> None:
    if len(step) != 2:
        raise ValueError("step must be two-dimensional")
    for component in step:
        if isinstance(component, bool) or not isinstance(component, int):
            raise ValueError("primitive step components must be integers")
        if component < -1 or component > 1:
            raise ValueError("primitive step components must lie in {-1,0,1}")


@dataclass(frozen=True, order=True)
class BodyMotion2D:
    """One finite proposed primitive translation for an E001 body."""

    body: Body2D
    step: Vector2D

    def __post_init__(self) -> None:
        _validate_step(self.step)

    @property
    def body_id(self) -> int:
        return self.body.body_id

    @property
    def end_body(self) -> Body2D:
        return Body2D(
            self.body.body_id,
            self.body.x + self.step[0],
            self.body.y + self.step[1],
            self.body.radius,
        )

    @property
    def is_wait(self) -> bool:
        return self.step == (0, 0)


def _edge_target(start: Point2D, end: Point2D) -> MotionTarget:
    if start == end:
        raise ValueError("wait actions do not have an edge target")
    low, high = sorted((start, end))
    return ("edge", (low, high))


def iter_motion_targets(motion: BodyMotion2D):
    """Yield finite endpoint-vertex and primitive-edge targets for one motion."""
    dx, dy = motion.step
    for end_target in iter_terminal_collapse_targets(motion.end_body):
        yield ("vertex", end_target)

    if motion.is_wait:
        return
    for start_target in iter_terminal_collapse_targets(motion.body):
        end_target = (start_target[0] + dx, start_target[1] + dy)
        yield _edge_target(start_target, end_target)


def motion_target_set(motion: BodyMotion2D) -> frozenset[MotionTarget]:
    """Materialize one motion's finite transition-target set."""
    return frozenset(iter_motion_targets(motion))


def motion_conflict_witnesses(
    left: BodyMotion2D, right: BodyMotion2D
) -> frozenset[MotionTarget]:
    """Return all shared transition targets for two motions."""
    if left.body_id == right.body_id:
        raise ValueError("motion pair must contain distinct body ids")
    return motion_target_set(left).intersection(motion_target_set(right))


def motion_conflict(left: BodyMotion2D, right: BodyMotion2D) -> bool:
    """Whether two primitive motions share at least one transition target."""
    return bool(motion_conflict_witnesses(left, right))


def motion_conflict_pairs(motions: list[BodyMotion2D]) -> tuple[Pair, ...]:
    """Find all conflicts by inverting transition target -> body membership."""
    ids = [motion.body_id for motion in motions]
    if len(ids) != len(set(ids)):
        raise ValueError("motion body ids must be unique")

    by_target: dict[MotionTarget, list[int]] = {}
    for motion in sorted(motions, key=lambda item: item.body_id):
        for target in motion_target_set(motion):
            by_target.setdefault(target, []).append(motion.body_id)

    conflicts: set[Pair] = set()
    for occupants in by_target.values():
        if len(occupants) < 2:
            continue
        for left_id, right_id in combinations(sorted(set(occupants)), 2):
            conflicts.add((left_id, right_id))
    return tuple(sorted(conflicts))


def _effective_motions(
    motions: list[BodyMotion2D], accepted_moving_ids: frozenset[int]
) -> list[BodyMotion2D]:
    result: list[BodyMotion2D] = []
    for motion in motions:
        if motion.is_wait or motion.body_id in accepted_moving_ids:
            result.append(motion)
        else:
            result.append(BodyMotion2D(motion.body, (0, 0)))
    return result


def maximum_conflict_free_move_sets(
    motions: list[BodyMotion2D],
) -> tuple[frozenset[int], ...]:
    """Exact small-instance oracle for accepting the most proposed nonzero moves.

    Every nonzero proposal is a binary decision: accept its primitive step or
    replace it by a wait.  The function exhaustively returns *all* maximum-size
    accepted moving-id sets whose resulting transition targets are conflict-free.
    Returning every optimum preserves genuine symmetry instead of hiding an
    arbitrary body-id priority.  This is exponential and is deliberately a
    reference oracle, not the intended large-N production solver.
    """
    ids = [motion.body_id for motion in motions]
    if len(ids) != len(set(ids)):
        raise ValueError("motion body ids must be unique")

    initial_waits = [BodyMotion2D(motion.body, (0, 0)) for motion in motions]
    if motion_conflict_pairs(initial_waits):
        raise ValueError("initial body supports must be pairwise conflict-free")

    moving_ids = tuple(sorted(motion.body_id for motion in motions if not motion.is_wait))
    best_size = -1
    best: list[frozenset[int]] = []
    count = len(moving_ids)
    for mask in range(1 << count):
        accepted = frozenset(
            moving_ids[index] for index in range(count) if mask & (1 << index)
        )
        size = len(accepted)
        if size < best_size:
            continue
        effective = _effective_motions(motions, accepted)
        if motion_conflict_pairs(effective):
            continue
        if size > best_size:
            best_size = size
            best = [accepted]
        else:
            best.append(accepted)

    if best_size < 0:
        raise AssertionError("all-wait transition should be feasible after initial validation")
    return tuple(sorted(set(best), key=lambda item: tuple(sorted(item))))
