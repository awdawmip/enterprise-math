"""Subtraction-free state-pair and kernel evolution for deterministic maps.

This module is the executable specification for P018 Supplement 12.  Pair and
kernel constructions are elementary established mathematics; the purpose here is
to pressure-test their role as a weaker substrate beneath numeric defect
coordinates and deterministic irreversibility.
"""

from __future__ import annotations

from collections.abc import Callable, Iterable
from typing import TypeVar

X = TypeVar("X")
Y = TypeVar("Y")
Z = TypeVar("Z")

NaturalOperation = Callable[[int], int]


def pair_map(operation: Callable[[X], Y], pair: tuple[X, X]) -> tuple[Y, Y]:
    """Apply one deterministic map to both components of a state pair."""
    first, second = pair
    return operation(first), operation(second)


def composed_pair_map(
    first: Callable[[X], Y],
    second: Callable[[Y], Z],
    pair: tuple[X, X],
) -> tuple[tuple[Z, Z], tuple[Z, Z]]:
    """Return direct and staged pair evolution for ``second ∘ first``."""
    direct = pair_map(lambda value: second(first(value)), pair)
    staged = pair_map(second, pair_map(first, pair))
    return direct, staged


def on_diagonal(pair: tuple[X, X]) -> bool:
    """Return whether both components are the same state."""
    return pair[0] == pair[1]


def diagonal_is_absorbing(operation: Callable[[X], Y], state: X) -> bool:
    """Executable P018-T111 at one diagonal state."""
    return on_diagonal(pair_map(operation, (state, state)))


def kernel_pair_member(
    operation: Callable[[X], Y], first: X, second: X
) -> bool:
    """Return whether ``(first, second)`` belongs to the kernel relation of F."""
    return operation(first) == operation(second)


def kernel_equals_diagonal_preimage(
    operation: Callable[[X], Y], first: X, second: X
) -> bool:
    """Check P018-T112 at one pair."""
    kernel = kernel_pair_member(operation, first, second)
    diagonal_preimage = on_diagonal(pair_map(operation, (first, second)))
    if kernel != diagonal_preimage:
        raise AssertionError("kernel relation disagrees with diagonal preimage")
    return kernel


def pair_to_difference(first: int, second: int) -> tuple[int, int]:
    """P018-T113 coordinate map ``(a,b) -> (a,b-a)`` on natural states."""
    if isinstance(first, bool) or not isinstance(first, int) or first < 0:
        raise ValueError("first must be a non-negative integer")
    if isinstance(second, bool) or not isinstance(second, int) or second < 0:
        raise ValueError("second must be a non-negative integer")
    return first, second - first


def difference_to_pair(base_state: int, difference: int) -> tuple[int, int]:
    """Inverse coordinate map ``(a,h) -> (a,a+h)`` when admissible."""
    if isinstance(base_state, bool) or not isinstance(base_state, int) or base_state < 0:
        raise ValueError("base_state must be a non-negative integer")
    if isinstance(difference, bool) or not isinstance(difference, int):
        raise ValueError("difference must be an integer")
    second = base_state + difference
    if second < 0:
        raise ValueError("difference is not admissible from base_state")
    return base_state, second


def endpoint_pair(
    first_path: Callable[[X], Y], second_path: Callable[[X], Y], state: X
) -> tuple[Y, Y]:
    """P018-T114 endpoint pair for two parallel deterministic paths."""
    return first_path(state), second_path(state)


def suffix_pair_propagation(
    first_path: Callable[[X], Y],
    second_path: Callable[[X], Y],
    suffix: Callable[[Y], Z],
    state: X,
) -> tuple[tuple[Z, Z], tuple[Z, Z]]:
    """Return direct and pair-map propagated common-suffix endpoint pairs."""
    direct = endpoint_pair(
        lambda value: suffix(first_path(value)),
        lambda value: suffix(second_path(value)),
        state,
    )
    propagated = pair_map(suffix, endpoint_pair(first_path, second_path, state))
    return direct, propagated


def critical_square_pair(
    fine_operation: NaturalOperation,
    coarse_operation: NaturalOperation,
    state: int,
    ratio: int,
) -> tuple[int, int]:
    """P018-T115 endpoint pair ``(Q(F_e(x)), F_d(Q(x)))``."""
    if isinstance(state, bool) or not isinstance(state, int) or state < 0:
        raise ValueError("state must be a non-negative integer")
    if isinstance(ratio, bool) or not isinstance(ratio, int) or ratio <= 0:
        raise ValueError("ratio must be a positive integer")
    upper_then_project = fine_operation(state) // ratio
    project_then_lower = coarse_operation(state // ratio)
    if upper_then_project < 0 or project_then_lower < 0:
        raise ValueError("operations must map natural states to natural states")
    return upper_then_project, project_then_lower


def kernel_monotonic_under_suffix(
    first: Callable[[X], Y],
    suffix: Callable[[Y], Z],
    left: X,
    right: X,
) -> bool:
    """Check P018-T118: kernel membership persists under deterministic suffix."""
    if not kernel_pair_member(first, left, right):
        return True
    return kernel_pair_member(lambda value: suffix(first(value)), left, right)


def cumulative_map(operations: Iterable[Callable[[X], X]]) -> Callable[[X], X]:
    """Compose same-type operations in iteration order."""
    operation_list = list(operations)

    def cumulative(value: X) -> X:
        current = value
        for operation in operation_list:
            current = operation(current)
        return current

    return cumulative


def cumulative_kernel_monotone(
    prefixes: Iterable[Callable[[X], X]],
    next_operation: Callable[[X], X],
    left: X,
    right: X,
) -> bool:
    """Check one step of kernel monotonicity for a cumulative deterministic path."""
    current = cumulative_map(prefixes)
    if not kernel_pair_member(current, left, right):
        return True
    extended = lambda value: next_operation(current(value))
    return kernel_pair_member(extended, left, right)
