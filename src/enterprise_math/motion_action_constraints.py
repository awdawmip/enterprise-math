"""E001.5 exact binary move/wait action constraints from transition targets.

For an initially conflict-free body configuration, each nonzero proposed motion
has two action variants for one tick: MOVE or WAIT.  Pairwise transition-target
intersection for the four action combinations can be factored into three kinds
of Boolean constraints:

* MOVE_i / MOVE_j conflict  -> mutex(i,j);
* MOVE_i / WAIT_j conflict  -> MOVE_i implies MOVE_j;
* WAIT_i / MOVE_j conflict  -> MOVE_j implies MOVE_i.

A body whose proposed move conflicts with an explicitly waiting body is forced
to wait.  Initial WAIT/WAIT conflicts are rejected before this reduction.

The same report can be built in two ways:

1. ``binary_motion_constraints`` is the direct pairwise definition/oracle;
2. ``binary_motion_constraints_target_first`` inverts finite action-target
   incidence and emits mutex/implication/forced-wait constraints locally at the
   shared targets, avoiding a required all-pairs scan in the construction.

The resulting clauses are Horn 2-CNF forms ``~x_i``, ``~x_i or ~x_j``, and
``~x_i or x_j``.  The implication relation therefore gives a finite required-
move closure for any seed set.  If that closure reaches a forced wait or
contains a mutex pair, the seed is already impossible before global search.

Boolean implication/Horn logic and incidence inversion are established prior
art.  This module records the E001 engineering factorization and does not claim
the general logic as new mathematics.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations

from .engineering_collision import Pair
from .motion_collapse import BodyMotion2D, motion_conflict, motion_target_set

Implication = tuple[int, int]


@dataclass(frozen=True)
class BinaryMotionConstraintReport:
    """Exact finite constraints for accepting nonzero proposed motions."""

    moving_ids: tuple[int, ...]
    forced_wait_ids: tuple[int, ...]
    mutex_pairs: tuple[Pair, ...]
    implications: tuple[Implication, ...]


def _wait_variant(motion: BodyMotion2D) -> BodyMotion2D:
    return BodyMotion2D(motion.body, (0, 0))


def _finalize_report(
    moving_ids: tuple[int, ...],
    forced_waits: set[int],
    mutex_pairs: set[Pair],
    implications: set[Implication],
) -> BinaryMotionConstraintReport:
    return BinaryMotionConstraintReport(
        moving_ids=moving_ids,
        forced_wait_ids=tuple(sorted(forced_waits)),
        mutex_pairs=tuple(sorted(mutex_pairs)),
        implications=tuple(sorted(implications)),
    )


def binary_motion_constraints(
    motions: list[BodyMotion2D],
) -> BinaryMotionConstraintReport:
    """Pairwise oracle: factor exact move/wait conflicts into constraints."""
    ids = [motion.body_id for motion in motions]
    if len(ids) != len(set(ids)):
        raise ValueError("motion body ids must be unique")

    by_id = {motion.body_id: motion for motion in motions}
    waits = {body_id: _wait_variant(motion) for body_id, motion in by_id.items()}

    for left_id, right_id in combinations(sorted(by_id), 2):
        if motion_conflict(waits[left_id], waits[right_id]):
            raise ValueError("initial body supports must be pairwise conflict-free")

    moving_ids = tuple(sorted(body_id for body_id, motion in by_id.items() if not motion.is_wait))
    moving_set = set(moving_ids)
    forced_waits: set[int] = set()
    mutex_pairs: set[Pair] = set()
    implications: set[Implication] = set()

    for left_id, right_id in combinations(sorted(by_id), 2):
        left_moving = left_id in moving_set
        right_moving = right_id in moving_set
        left_move = by_id[left_id]
        right_move = by_id[right_id]
        left_wait = waits[left_id]
        right_wait = waits[right_id]

        if left_moving and right_moving:
            if motion_conflict(left_move, right_move):
                mutex_pairs.add((left_id, right_id))
            if motion_conflict(left_move, right_wait):
                implications.add((left_id, right_id))
            if motion_conflict(left_wait, right_move):
                implications.add((right_id, left_id))
        elif left_moving:
            if motion_conflict(left_move, right_wait):
                forced_waits.add(left_id)
        elif right_moving:
            if motion_conflict(left_wait, right_move):
                forced_waits.add(right_id)

    return _finalize_report(moving_ids, forced_waits, mutex_pairs, implications)


def binary_motion_constraints_target_first(
    motions: list[BodyMotion2D],
) -> BinaryMotionConstraintReport:
    """Build the same exact report by inverting MOVE/WAIT transition targets.

    For each finite target ``z`` retain the bodies whose MOVE variant uses ``z``
    and the bodies whose WAIT variant uses ``z``.  Local occupancy then gives:

    * pairs of movers at ``z`` -> mutex;
    * mover ``i`` and waiter ``j`` at ``z`` -> ``i -> j`` when ``j`` has a
      nonzero proposal, otherwise ``i`` is forced to wait;
    * pairs of waiters at any target -> invalid initial overlap.

    Constraint sets are deduplicated across targets.
    """
    ids = [motion.body_id for motion in motions]
    if len(ids) != len(set(ids)):
        raise ValueError("motion body ids must be unique")

    by_id = {motion.body_id: motion for motion in motions}
    moving_ids = tuple(sorted(body_id for body_id, motion in by_id.items() if not motion.is_wait))
    moving_set = set(moving_ids)

    move_by_target: dict[object, set[int]] = {}
    wait_by_target: dict[object, set[int]] = {}
    for body_id, motion in by_id.items():
        wait = _wait_variant(motion)
        for target in motion_target_set(wait):
            wait_by_target.setdefault(target, set()).add(body_id)
        if body_id in moving_set:
            for target in motion_target_set(motion):
                move_by_target.setdefault(target, set()).add(body_id)

    for waiters in wait_by_target.values():
        if len(waiters) > 1:
            raise ValueError("initial body supports must be pairwise conflict-free")

    forced_waits: set[int] = set()
    mutex_pairs: set[Pair] = set()
    implications: set[Implication] = set()

    all_targets = set(move_by_target).union(wait_by_target)
    for target in all_targets:
        movers = sorted(move_by_target.get(target, ()))
        waiters = sorted(wait_by_target.get(target, ()))

        for left_id, right_id in combinations(movers, 2):
            mutex_pairs.add((left_id, right_id))

        for mover_id in movers:
            for waiter_id in waiters:
                if mover_id == waiter_id:
                    continue
                if waiter_id in moving_set:
                    implications.add((mover_id, waiter_id))
                else:
                    forced_waits.add(mover_id)

    return _finalize_report(moving_ids, forced_waits, mutex_pairs, implications)


def required_move_closure(
    report: BinaryMotionConstraintReport,
    seed_ids: frozenset[int],
) -> frozenset[int]:
    """Return the least implication-closed MOVE superset of ``seed_ids``."""
    moving = set(report.moving_ids)
    if not seed_ids.issubset(moving):
        raise ValueError("seed_ids must contain only moving ids")

    required = set(seed_ids)
    changed = True
    while changed:
        changed = False
        for source_id, required_id in report.implications:
            if source_id in required and required_id not in required:
                required.add(required_id)
                changed = True
    return frozenset(required)


def move_closure_is_feasible(
    report: BinaryMotionConstraintReport,
    seed_ids: frozenset[int],
) -> bool:
    """Whether the implication closure of seeds avoids forced waits and mutexes."""
    closure = required_move_closure(report, seed_ids)
    if closure.intersection(report.forced_wait_ids):
        return False
    return all(
        not (left_id in closure and right_id in closure)
        for left_id, right_id in report.mutex_pairs
    )


def individually_feasible_move_ids(
    report: BinaryMotionConstraintReport,
) -> tuple[int, ...]:
    """Return moves whose own required closure is not already contradictory."""
    return tuple(
        body_id
        for body_id in report.moving_ids
        if move_closure_is_feasible(report, frozenset({body_id}))
    )


def accepted_set_satisfies_constraints(
    report: BinaryMotionConstraintReport,
    accepted_moving_ids: frozenset[int],
) -> bool:
    """Check one accepted MOVE set against the factored finite constraints."""
    moving = set(report.moving_ids)
    if not accepted_moving_ids.issubset(moving):
        return False
    if accepted_moving_ids.intersection(report.forced_wait_ids):
        return False
    for left_id, right_id in report.mutex_pairs:
        if left_id in accepted_moving_ids and right_id in accepted_moving_ids:
            return False
    for source_id, required_id in report.implications:
        if source_id in accepted_moving_ids and required_id not in accepted_moving_ids:
            return False
    return True


def maximum_constraint_solutions(
    report: BinaryMotionConstraintReport,
) -> tuple[frozenset[int], ...]:
    """Exact exponential oracle for maximum-cardinality satisfying MOVE sets."""
    ids = report.moving_ids
    best_size = -1
    best: list[frozenset[int]] = []
    for mask in range(1 << len(ids)):
        accepted = frozenset(
            ids[index] for index in range(len(ids)) if mask & (1 << index)
        )
        size = len(accepted)
        if size < best_size:
            continue
        if not accepted_set_satisfies_constraints(report, accepted):
            continue
        if size > best_size:
            best_size = size
            best = [accepted]
        else:
            best.append(accepted)
    if best_size < 0:
        raise AssertionError("all-wait assignment should satisfy valid binary constraints")
    return tuple(sorted(set(best), key=lambda item: tuple(sorted(item))))
