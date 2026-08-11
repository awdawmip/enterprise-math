"""Minimum precision design as a target geodesic in a presented OR semilattice.

For the Set-Cover action family, semantic effects are universe masks and action i
acts on effect state x by

    x -> x OR mask_i.

The identity effect is0 and full precision corresponds to the full-universe mask
Omega.  Because OR generators are commuting/idempotent, every word can be
reduced to the subset of generators that occur.  Therefore

    minimum preserving subset size

is exactly

    shortest path distance 0 -> Omega

in the right Cayley graph induced by the declared generator presentation.

With nonnegative generator costs, minimum weighted preserving design is the
weighted shortest-path distance in the same graph.

This reframes the design/execution separation algebraically.  The abstract OR
monoid can be fixed while changing the generator presentation changes the induced
word metric and target geodesic.  If all 2^m mask states are expanded explicitly,
BFS/Dijkstra is polynomial in that expanded graph; the Set Cover hardness arises
from the exponentially succinct generator-mask presentation relative to universe
size m.

Cayley graphs, word metrics, BFS/Dijkstra and Set Cover are standard prior
mathematics/CS.  The Enterprise Math value is locating minimum semantic design as
an inverse-synthesis geometry distinct from forward execution.
"""

from __future__ import annotations

from dataclasses import dataclass
from heapq import heappop, heappush
from math import inf
from typing import Iterable, Mapping, Sequence

from .same_monoid_design_gap import (
    duplicate_singleton_catalogue,
    full_action_catalogue,
)
from .set_cover_formulaic_execution import (
    action_masks,
    minimum_cover_size_exact,
)


def _universe_size(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("universe_size must be a positive integer")
    return value


def full_mask(universe_size: int) -> int:
    return (1 << _universe_size(universe_size)) - 1


def _target_mask(value: int | None, universe_size: int) -> int:
    limit = 1 << _universe_size(universe_size)
    if value is None:
        return limit - 1
    if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value < limit:
        raise ValueError("target mask outside universe")
    return value


@dataclass(frozen=True)
class GeodesicSynthesisResult:
    universe_size: int
    target_mask: int
    distance: int | None
    action_indices: tuple[int, ...] | None
    visited_effect_states: int
    total_explicit_monoid_states: int

    @property
    def reachable(self) -> bool:
        return self.distance is not None


def shortest_or_geodesic(
    universe_size: int,
    sets: Sequence[Iterable[int]],
    target_mask: int | None = None,
) -> GeodesicSynthesisResult:
    size = _universe_size(universe_size)
    masks = action_masks(size, sets)
    if not masks:
        raise ValueError("at least one generator is required")
    target = _target_mask(target_mask, size)
    if target == 0:
        return GeodesicSynthesisResult(
            universe_size=size,
            target_mask=target,
            distance=0,
            action_indices=(),
            visited_effect_states=1,
            total_explicit_monoid_states=1 << size,
        )

    queue = [0]
    predecessor: dict[int, tuple[int, int] | None] = {0: None}
    cursor = 0
    found = None
    while cursor < len(queue):
        state = queue[cursor]
        cursor += 1
        if state == target:
            found = state
            break
        for action_index, mask in enumerate(masks):
            nxt = state | mask
            if nxt in predecessor:
                continue
            predecessor[nxt] = (state, action_index)
            queue.append(nxt)
    if found is None and target in predecessor:
        found = target
    if found is None:
        return GeodesicSynthesisResult(
            universe_size=size,
            target_mask=target,
            distance=None,
            action_indices=None,
            visited_effect_states=len(predecessor),
            total_explicit_monoid_states=1 << size,
        )

    actions = []
    current = target
    while current != 0:
        previous = predecessor[current]
        if previous is None:
            raise AssertionError("nonidentity target lost geodesic predecessor")
        current, action_index = previous
        actions.append(action_index)
    actions.reverse()
    return GeodesicSynthesisResult(
        universe_size=size,
        target_mask=target,
        distance=len(actions),
        action_indices=tuple(actions),
        visited_effect_states=len(predecessor),
        total_explicit_monoid_states=1 << size,
    )


def geodesic_equals_minimum_cover(
    universe_size: int,
    sets: Sequence[Iterable[int]],
) -> bool:
    geodesic = shortest_or_geodesic(universe_size, sets)
    cover = minimum_cover_size_exact(universe_size, sets)
    if geodesic.distance != cover:
        raise AssertionError("target geodesic disagreed with minimum Set Cover size")
    return True


def _costs(action_count: int, costs: Mapping[int, int | float]) -> tuple[float, ...]:
    if set(costs) != set(range(action_count)):
        raise ValueError("costs must provide exactly one value per action index")
    result = []
    for index in range(action_count):
        value = costs[index]
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("action costs must be numeric")
        if value < 0:
            raise ValueError("action costs must be nonnegative")
        result.append(float(value))
    return tuple(result)


@dataclass(frozen=True)
class WeightedGeodesicSynthesisResult:
    universe_size: int
    target_mask: int
    cost: float | None
    action_indices: tuple[int, ...] | None
    visited_effect_states: int


def minimum_cost_or_geodesic(
    universe_size: int,
    sets: Sequence[Iterable[int]],
    costs: Mapping[int, int | float],
    target_mask: int | None = None,
) -> WeightedGeodesicSynthesisResult:
    size = _universe_size(universe_size)
    masks = action_masks(size, sets)
    if not masks:
        raise ValueError("at least one generator is required")
    weights = _costs(len(masks), costs)
    target = _target_mask(target_mask, size)

    distance: dict[int, float] = {0: 0.0}
    predecessor: dict[int, tuple[int, int] | None] = {0: None}
    heap: list[tuple[float, int]] = [(0.0, 0)]
    while heap:
        current_cost, state = heappop(heap)
        if current_cost != distance[state]:
            continue
        if state == target:
            break
        for action_index, (mask, edge_cost) in enumerate(zip(masks, weights, strict=True)):
            nxt = state | mask
            candidate = current_cost + edge_cost
            if candidate < distance.get(nxt, inf):
                distance[nxt] = candidate
                predecessor[nxt] = (state, action_index)
                heappush(heap, (candidate, nxt))

    if target not in distance:
        return WeightedGeodesicSynthesisResult(
            universe_size=size,
            target_mask=target,
            cost=None,
            action_indices=None,
            visited_effect_states=len(distance),
        )

    actions = []
    current = target
    while current != 0:
        previous = predecessor[current]
        if previous is None:
            raise AssertionError("weighted target lost predecessor")
        current, action_index = previous
        actions.append(action_index)
    actions.reverse()
    return WeightedGeodesicSynthesisResult(
        universe_size=size,
        target_mask=target,
        cost=distance[target],
        action_indices=tuple(actions),
        visited_effect_states=len(distance),
    )


def explicit_boolean_monoid_state_count(universe_size: int) -> int:
    return 1 << _universe_size(universe_size)


def compact_generator_incidence_bits(
    universe_size: int,
    sets: Sequence[Iterable[int]],
) -> int:
    """Simple dense input-size proxy for a Set-Cover generator catalogue."""
    size = _universe_size(universe_size)
    masks = action_masks(size, sets)
    return size * len(masks)


@dataclass(frozen=True)
class SameMonoidGeodesicGapReport:
    universe_size: int
    semantic_monoid_states: int
    action_count: int
    duplicate_catalogue_distance: int
    full_action_catalogue_distance: int
    distance_gap: int


def same_monoid_geodesic_gap_report(universe_size: int) -> SameMonoidGeodesicGapReport:
    size = _universe_size(universe_size)
    if size < 2:
        raise ValueError("same-monoid gap requires universe_size at least two")
    left = duplicate_singleton_catalogue(size)
    right = full_action_catalogue(size)
    left_result = shortest_or_geodesic(size, left)
    right_result = shortest_or_geodesic(size, right)
    if left_result.distance != size:
        raise AssertionError("duplicate catalogue geodesic was not universe size")
    if right_result.distance != 1:
        raise AssertionError("full-action catalogue geodesic was not one")
    return SameMonoidGeodesicGapReport(
        universe_size=size,
        semantic_monoid_states=1 << size,
        action_count=size + 1,
        duplicate_catalogue_distance=left_result.distance,
        full_action_catalogue_distance=right_result.distance,
        distance_gap=left_result.distance - right_result.distance,
    )
