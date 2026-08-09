"""Closed P011 revelation law for a collapse basin resolved one unit at a time.

In the boundary-pullback regime with primitive +1 and nondecreasing neighboring
basin widths, a current basin of w fine integer states is refined from its upper
boundary.  After t unit steps of future budget, 0<=t<=w-1, the partition consists
of one unresolved block of size w-t plus t singletons.

Hence for every collision order k>=2,

    J_k(t) = C(w-t,k)

and the newly revealed collisions at step t>=1 are

    Lambda_k(t) = C(w-t,k-1).

The total revelation telescopes to C(w,k), exactly the original collision
coordinate of one size-w collapse fiber.  With primitive unit cost c, the t-th
release occurs at causal budget t*c.
"""

from __future__ import annotations

from math import comb


def _validate(width: int, steps: int | None = None) -> None:
    if isinstance(width, bool) or not isinstance(width, int) or width <= 0:
        raise ValueError("width must be a positive integer")
    if steps is not None and (
        isinstance(steps, bool)
        or not isinstance(steps, int)
        or not (0 <= steps <= width - 1)
    ):
        raise ValueError("steps must lie in 0..width-1")


def unit_revelation_partition_sizes(width: int, steps: int) -> tuple[int, ...]:
    _validate(width, steps)
    unresolved = width - steps
    return (unresolved,) + (1,) * steps


def unit_revelation_collision_coordinate(
    width: int,
    steps: int,
    order: int,
) -> int:
    _validate(width, steps)
    if isinstance(order, bool) or not isinstance(order, int) or order < 1:
        raise ValueError("order must be a positive integer")
    if order == 1:
        return width
    unresolved = width - steps
    return comb(unresolved, order) if unresolved >= order else 0


def unit_revelation_increment(
    width: int,
    step: int,
    order: int,
) -> int:
    """Lambda_k(step)=J_k(step-1)-J_k(step), for step 1..w-1."""
    _validate(width)
    if isinstance(step, bool) or not isinstance(step, int) or not (1 <= step <= width - 1):
        raise ValueError("step must lie in 1..width-1")
    if isinstance(order, bool) or not isinstance(order, int) or order < 1:
        raise ValueError("order must be a positive integer")
    if order == 1:
        return 0
    remaining_after_split = width - step
    return comb(remaining_after_split, order - 1) if remaining_after_split >= order - 1 else 0


def unit_revelation_increment_from_difference(
    width: int,
    step: int,
    order: int,
) -> int:
    return (
        unit_revelation_collision_coordinate(width, step - 1, order)
        - unit_revelation_collision_coordinate(width, step, order)
    )


def revelation_telescopes_to_original_collision(
    width: int,
    order: int,
) -> bool:
    _validate(width)
    if isinstance(order, bool) or not isinstance(order, int) or order < 2:
        raise ValueError("order must be at least two")
    released = sum(
        unit_revelation_increment(width, step, order)
        for step in range(1, width)
    )
    original = comb(width, order) if width >= order else 0
    return released == original


def budgeted_revelation_spectrum(
    width: int,
    unit_cost: int,
    maximum_budget: int,
    maximum_order: int,
) -> tuple[tuple[int, ...], ...]:
    """Rows R=1..B, columns k=1..K; releases occur only at multiples of unit_cost."""
    _validate(width)
    if isinstance(unit_cost, bool) or not isinstance(unit_cost, int) or unit_cost <= 0:
        raise ValueError("unit_cost must be a positive integer")
    if isinstance(maximum_budget, bool) or not isinstance(maximum_budget, int) or maximum_budget < 0:
        raise ValueError("maximum_budget must be non-negative")
    if isinstance(maximum_order, bool) or not isinstance(maximum_order, int) or maximum_order < 1:
        raise ValueError("maximum_order must be positive")
    rows = []
    for budget in range(1, maximum_budget + 1):
        if budget % unit_cost != 0:
            rows.append((0,) * maximum_order)
            continue
        step = budget // unit_cost
        if not (1 <= step <= width - 1):
            rows.append((0,) * maximum_order)
            continue
        rows.append(
            tuple(
                unit_revelation_increment(width, step, order)
                for order in range(1, maximum_order + 1)
            )
        )
    return tuple(rows)
