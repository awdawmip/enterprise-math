"""Exact scheduling helpers for BRC multi-strip smooth-relation collection.

The minimum-gap scheduler is a finite k-way merge of the monotone vertical gap
sequences attached to retained multiplier states.  Choosing smaller auxiliary
values first is classical smooth-relation practice; this module makes the BRC
strip scheduling exact and provenance-preserving.
"""

from __future__ import annotations

import heapq
from dataclasses import dataclass
from typing import Iterable

from .brc_multiplier_factor_scan import AdmissibleMultiplierRootState
from .brc_multiplier_vertical_wheel import vertical_state_from_multiplier_state


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


@dataclass(frozen=True)
class ScheduledRelationPoint:
    state: AdmissibleMultiplierRootState
    vertical_offset: int
    x: int
    gap: int

    def __post_init__(self) -> None:
        if self.vertical_offset < 0 or self.gap < 0 or self.x <= 0:
            raise ValueError("scheduled relation coordinates are out of range")
        if self.x * self.x - self.gap != self.state.multiplier * self.state.n:
            raise ValueError("scheduled relation point failed reconstruction")


def minimum_gap_relation_points(
    states: tuple[AdmissibleMultiplierRootState, ...],
    point_limit: int,
) -> Iterable[ScheduledRelationPoint]:
    """Yield the exact union of strip points in nondecreasing gap order.

    Each strip has

        D_t = D_0 + t(2*x_0+t)

    and therefore strictly increasing gaps.  A heap containing one live head
    from each strip is the exact k-way merge.  Every emitted point retains its
    original multiplier and vertical offset.
    """
    _require_positive("point_limit", point_limit)
    if not states:
        return
    n = states[0].n
    if any(state.n != n for state in states):
        raise ValueError("all multiplier states must belong to one n")

    heap: list[tuple[int, int, int, int, int]] = []
    for index, state in enumerate(states):
        vertical = vertical_state_from_multiplier_state(state)
        heapq.heappush(
            heap,
            (vertical.base_gap, state.multiplier, 0, vertical.base_x, index),
        )

    for _ in range(point_limit):
        gap, _, offset, x, index = heapq.heappop(heap)
        state = states[index]
        yield ScheduledRelationPoint(
            state=state,
            vertical_offset=offset,
            x=x,
            gap=gap,
        )
        next_gap = gap + 2 * x + 1
        heapq.heappush(
            heap,
            (next_gap, state.multiplier, offset + 1, x + 1, index),
        )


__all__ = [
    "ScheduledRelationPoint",
    "minimum_gap_relation_points",
]
