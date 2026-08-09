"""E001.1 exact collision by a shared terminal collapse target.

For one axis-aligned square ``Body2D`` with integer center ``(x, y)`` and
integer ``radius``, define its terminal collapse-target set as the finite
Chebyshev ball

    T(B) = {(u, v) : max(|u-x|, |v-y|) <= radius}.

Two bodies co-collapse when ``T(A)`` and ``T(B)`` share at least one terminal
state. For the E001 square-body geometry this is exactly equivalent to the
existing terminal collision predicate. The formulation is relational rather
than "same coarse cell", so it has no arbitrary grid-boundary false negative.

The inverted implementation groups body ids by collapse target. It therefore
finds exact collisions without first enumerating body pairs. Its cost is tied
to the number of emitted finite target states plus actual shared-target
multiplicity; this is favorable for small discrete bodies and deliberately not
claimed to dominate when body footprints are very large.
"""

from __future__ import annotations

from itertools import combinations
from typing import Iterator

from .engineering_collision import Body2D, Pair

Target2D = tuple[int, int]
TargetBounds2D = tuple[int, int, int, int]


def terminal_collapse_target_bounds(body: Body2D) -> TargetBounds2D:
    """Return the exact rectangular bounds of ``T(body)``."""
    return (
        body.x - body.radius,
        body.x + body.radius,
        body.y - body.radius,
        body.y + body.radius,
    )


def iter_terminal_collapse_targets(body: Body2D) -> Iterator[Target2D]:
    """Yield every finite terminal state to which this body can co-collapse."""
    x_lo, x_hi, y_lo, y_hi = terminal_collapse_target_bounds(body)
    for x in range(x_lo, x_hi + 1):
        for y in range(y_lo, y_hi + 1):
            yield (x, y)


def common_collapse_target_bounds(
    left: Body2D, right: Body2D
) -> TargetBounds2D | None:
    """Return the exact intersection rectangle ``T(left) ∩ T(right)``."""
    left_x_lo, left_x_hi, left_y_lo, left_y_hi = terminal_collapse_target_bounds(left)
    right_x_lo, right_x_hi, right_y_lo, right_y_hi = terminal_collapse_target_bounds(right)
    x_lo = max(left_x_lo, right_x_lo)
    x_hi = min(left_x_hi, right_x_hi)
    y_lo = max(left_y_lo, right_y_lo)
    y_hi = min(left_y_hi, right_y_hi)
    if x_lo > x_hi or y_lo > y_hi:
        return None
    return (x_lo, x_hi, y_lo, y_hi)


def common_collapse_multiplicity(left: Body2D, right: Body2D) -> int:
    """Number of shared terminal collapse targets; zero means separation."""
    bounds = common_collapse_target_bounds(left, right)
    if bounds is None:
        return 0
    x_lo, x_hi, y_lo, y_hi = bounds
    return (x_hi - x_lo + 1) * (y_hi - y_lo + 1)


def common_collapse_witness(left: Body2D, right: Body2D) -> Target2D | None:
    """Return a deterministic shared target witness when the bodies collide."""
    bounds = common_collapse_target_bounds(left, right)
    if bounds is None:
        return None
    x_lo, _x_hi, y_lo, _y_hi = bounds
    return (x_lo, y_lo)


def common_collapse_collision(left: Body2D, right: Body2D) -> bool:
    """Whether two bodies can be absorbed into at least one shared terminal state."""
    return common_collapse_target_bounds(left, right) is not None


def common_collapse_pairs(bodies: list[Body2D]) -> tuple[Pair, ...]:
    """Find exact collisions by inverting body -> terminal-collapse-target relation.

    At terminal precision every target is one integer lattice state. If two
    body ids occur in the same target bucket, the two exact square footprints
    overlap at that state and hence collide. Pairs are deduplicated because a
    deep overlap may have more than one shared collapse target.
    """
    ids = [body.body_id for body in bodies]
    if len(ids) != len(set(ids)):
        raise ValueError("body ids must be unique")

    by_target: dict[Target2D, list[int]] = {}
    for body in sorted(bodies):
        for target in iter_terminal_collapse_targets(body):
            by_target.setdefault(target, []).append(body.body_id)

    collisions: set[Pair] = set()
    for occupants in by_target.values():
        if len(occupants) < 2:
            continue
        for left_id, right_id in combinations(occupants, 2):
            collisions.add(tuple(sorted((left_id, right_id))))
    return tuple(sorted(collisions))
