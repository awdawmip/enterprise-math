"""Finite coalescence-time observables for deterministic state dynamics.

The core construction is subtraction-free.  For a deterministic endomap F, two
states coalesce at time n when F^n sends their State Pair to the diagonal.  On
any eventual-coalescence class, the first coalescence time is an integer-valued
ultrametric because equality persists under every common deterministic suffix.
"""

from __future__ import annotations

from collections.abc import Callable, Iterable

NaturalOperation = Callable[[int], int]


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def iterate(operation: NaturalOperation, state: int, steps: int) -> int:
    """Apply ``operation`` exactly ``steps`` times."""
    _require_natural("state", state)
    _require_natural("steps", steps)
    current = state
    for _ in range(steps):
        current = operation(current)
        _require_natural("operation output", current)
    return current


def first_fixed_time(
    operation: NaturalOperation, state: int, *, max_steps: int = 10000
) -> int | None:
    """Return the first n with F^n(x) fixed, or ``None`` within the search bound."""
    _require_natural("state", state)
    _require_natural("max_steps", max_steps)
    current = state
    for step in range(max_steps + 1):
        nxt = operation(current)
        _require_natural("operation output", nxt)
        if nxt == current:
            return step
        current = nxt
    return None


def stabilized_state(
    operation: NaturalOperation, state: int, *, max_steps: int = 10000
) -> tuple[int, int]:
    """Return ``(first_fixed_time, fixed_state)`` when finite within the bound."""
    step = first_fixed_time(operation, state, max_steps=max_steps)
    if step is None:
        raise ValueError("no fixed state reached within max_steps")
    return step, iterate(operation, state, step)


def first_coalescence_time(
    operation: NaturalOperation,
    left: int,
    right: int,
    *,
    max_steps: int = 10000,
) -> int | None:
    """Return the first n with ``F^n(left) == F^n(right)`` within the bound."""
    _require_natural("left", left)
    _require_natural("right", right)
    _require_natural("max_steps", max_steps)
    left_state = left
    right_state = right
    for step in range(max_steps + 1):
        if left_state == right_state:
            return step
        left_state = operation(left_state)
        right_state = operation(right_state)
        _require_natural("left operation output", left_state)
        _require_natural("right operation output", right_state)
    return None


def same_eventual_fixed_state(
    operation: NaturalOperation,
    left: int,
    right: int,
    *,
    max_steps: int = 10000,
) -> bool:
    """Compare the finite fixed states reached by two trajectories."""
    _, left_fixed = stabilized_state(operation, left, max_steps=max_steps)
    _, right_fixed = stabilized_state(operation, right, max_steps=max_steps)
    return left_fixed == right_fixed


def canonical_coalescence_bound(
    operation: NaturalOperation,
    left: int,
    right: int,
    *,
    max_steps: int = 10000,
) -> int | None:
    """Return max individual stabilization times when the fixed states agree."""
    left_steps, left_fixed = stabilized_state(operation, left, max_steps=max_steps)
    right_steps, right_fixed = stabilized_state(operation, right, max_steps=max_steps)
    if left_fixed != right_fixed:
        return None
    return max(left_steps, right_steps)


def kernel_pairs_at_step(
    operation: NaturalOperation, states: Iterable[int], step: int
) -> set[tuple[int, int]]:
    """Return ordered state pairs coalesced after exactly ``step`` common iterations."""
    _require_natural("step", step)
    materialized = tuple(states)
    for state in materialized:
        _require_natural("state", state)
    images = {state: iterate(operation, state, step) for state in materialized}
    return {
        (left, right)
        for left in materialized
        for right in materialized
        if images[left] == images[right]
    }


def stabilization_kernel_pairs(
    operation: NaturalOperation,
    states: Iterable[int],
    *,
    max_steps: int = 10000,
) -> set[tuple[int, int]]:
    """Return ordered pairs with the same finite stabilized state."""
    materialized = tuple(states)
    fixed = {
        state: stabilized_state(operation, state, max_steps=max_steps)[1]
        for state in materialized
    }
    return {
        (left, right)
        for left in materialized
        for right in materialized
        if fixed[left] == fixed[right]
    }


def finite_saturation_step(
    operation: NaturalOperation,
    states: Iterable[int],
    *,
    max_steps: int = 10000,
) -> int:
    """Maximum first-fixed time on a finite observation set."""
    materialized = tuple(states)
    if not materialized:
        return 0
    return max(
        stabilized_state(operation, state, max_steps=max_steps)[0]
        for state in materialized
    )


def ultrametric_inequality_holds(
    operation: NaturalOperation,
    x: int,
    y: int,
    z: int,
    *,
    max_steps: int = 10000,
) -> bool:
    """Check tau(x,z) <= max(tau(x,y),tau(y,z)) when all three are finite."""
    xy = first_coalescence_time(operation, x, y, max_steps=max_steps)
    yz = first_coalescence_time(operation, y, z, max_steps=max_steps)
    xz = first_coalescence_time(operation, x, z, max_steps=max_steps)
    if xy is None or yz is None or xz is None:
        raise ValueError("states do not lie in one observed coalescence class")
    return xz <= max(xy, yz)
