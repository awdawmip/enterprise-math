"""Additive coarse-borrow calculus for finite reductive trajectories (P023)."""

from __future__ import annotations

from collections.abc import Callable, Iterable

from .p023_precision_compatibility import precision_project

ReductiveMap = Callable[[int], int]


def coarse_borrow(n: int, transformed: int, ratio: int) -> int:
    """Exact coarse-state drop Q_r(n)-Q_r(transformed)."""
    if n < 0 or transformed < 0 or transformed > n:
        raise ValueError("require natural transformed <= n")
    if ratio <= 0:
        raise ValueError("ratio must be positive")
    return precision_project(n, ratio) - precision_project(transformed, ratio)


def compose_reductive_borrow(
    n: int, first: ReductiveMap, second: ReductiveMap, ratio: int
) -> tuple[int, int, int]:
    """Return (first borrow, second borrow, composite borrow)."""
    mid = first(n)
    end = second(mid)
    if mid > n or end > mid or mid < 0 or end < 0:
        raise ValueError("maps must be reductive on the visited states")
    first_borrow = coarse_borrow(n, mid, ratio)
    second_borrow = coarse_borrow(mid, end, ratio)
    total = coarse_borrow(n, end, ratio)
    if total != first_borrow + second_borrow:
        raise AssertionError("coarse borrow must telescope")
    return first_borrow, second_borrow, total


def trajectory_borrows(states: Iterable[int], ratio: int) -> tuple[int, ...]:
    """Borrow count on each edge of a finite reductive state trajectory."""
    trajectory = tuple(states)
    if not trajectory:
        raise ValueError("trajectory must be nonempty")
    if ratio <= 0:
        raise ValueError("ratio must be positive")
    if any(state < 0 for state in trajectory):
        raise ValueError("trajectory states must be natural")
    if any(right > left for left, right in zip(trajectory, trajectory[1:])):
        raise ValueError("trajectory must be reductive")
    return tuple(
        coarse_borrow(left, right, ratio)
        for left, right in zip(trajectory, trajectory[1:])
    )


def telescoping_borrow_identity(states: Iterable[int], ratio: int) -> tuple[int, int]:
    """Return (sum of local borrows, endpoint coarse drop) and verify equality."""
    trajectory = tuple(states)
    borrows = trajectory_borrows(trajectory, ratio)
    total = sum(borrows)
    endpoint = precision_project(trajectory[0], ratio) - precision_project(
        trajectory[-1], ratio
    )
    if total != endpoint:
        raise AssertionError("trajectory borrow sum must equal endpoint coarse drop")
    return total, endpoint
