"""Reachability-defined precision for integer translation action languages.

P024 specializes the generic P023 future-compatible quotient to one-dimensional
integer translations and ordered threshold observations.

The central object is the reachable boundary orbit.  If ``B`` is a finite set
of integer observation boundaries and ``M_h`` is the set of cumulative
translations reachable by action words of length at most ``h``, then all
future-visible cuts are exactly

    C_h = {b - m : b in B, m in M_h}.

Two integer states are future-equivalent through horizon ``h`` iff no cut in
``C_h`` lies strictly between them (with the upper endpoint included).

For one-sided positive action languages this exposes numerical-semigroup holes.
For genuinely two-sided signed languages the additive action monoid equals its
group completion ``g Z`` and the induced single-threshold cells become uniform
gcd cells.  On a finite cyclic phase space, even a one-sided generated monoid is
automatically a subgroup, explaining why E002's periodic within-cell action
calculus collapses directly to a gcd law.
"""

from __future__ import annotations

from dataclasses import dataclass
from heapq import heappop, heappush
from math import gcd
from typing import Iterable


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _require_nonnegative(name: str, value: int) -> None:
    _require_int(name, value)
    if value < 0:
        raise ValueError(f"{name} must be non-negative")


def _require_positive(name: str, value: int) -> None:
    _require_int(name, value)
    if value <= 0:
        raise ValueError(f"{name} must be positive")


def _integer_actions(actions: Iterable[int], *, allow_empty: bool = False) -> tuple[int, ...]:
    values = tuple(actions)
    if not values and not allow_empty:
        raise ValueError("at least one action is required")
    for action in values:
        _require_int("action", action)
    return values


def _positive_actions(actions: Iterable[int]) -> tuple[int, ...]:
    values = _integer_actions(actions)
    if any(action <= 0 for action in values):
        raise ValueError("one-sided semigroup actions must all be positive")
    return tuple(sorted(set(values)))


def action_grain(actions: Iterable[int]) -> int:
    """Return the positive gcd grain of a nontrivial integer action family."""
    values = _integer_actions(actions)
    common = 0
    for action in values:
        common = gcd(common, abs(action))
    if common == 0:
        raise ValueError("all-zero action family has no positive grain")
    return common


def reachable_translations(actions: Iterable[int], horizon: int) -> tuple[int, ...]:
    """Cumulative translations realized by words of length at most ``horizon``."""
    values = _integer_actions(actions, allow_empty=True)
    _require_nonnegative("horizon", horizon)
    reached = {0}
    frontier = {0}
    for _ in range(horizon):
        frontier = {total + action for total in frontier for action in values}
        reached.update(frontier)
        if not frontier:
            break
    return tuple(sorted(reached))


def ordered_threshold_observation(value: int, boundaries: Iterable[int]) -> int:
    """Index of the interval containing ``value`` for distinct integer cuts.

    A boundary ``b`` lies between integer states ``b-1`` and ``b``.  The return
    value is the number of boundaries not exceeding ``value``.
    """
    _require_int("value", value)
    cuts = tuple(sorted(set(boundaries)))
    for boundary in cuts:
        _require_int("boundary", boundary)
    return sum(boundary <= value for boundary in cuts)


def reachable_boundary_cuts(
    boundaries: Iterable[int],
    actions: Iterable[int],
    horizon: int,
) -> tuple[int, ...]:
    """Return the horizon-``h`` future-visible cut set ``B - M_h``."""
    cuts = tuple(sorted(set(boundaries)))
    for boundary in cuts:
        _require_int("boundary", boundary)
    translations = reachable_translations(actions, horizon)
    return tuple(sorted({boundary - total for boundary in cuts for total in translations}))


def future_observation_signature(
    value: int,
    boundaries: Iterable[int],
    actions: Iterable[int],
    horizon: int,
) -> tuple[tuple[int, int], ...]:
    """Exact future signature indexed by every reachable cumulative translation."""
    _require_int("value", value)
    cuts = tuple(sorted(set(boundaries)))
    translations = reachable_translations(actions, horizon)
    return tuple(
        (total, ordered_threshold_observation(value + total, cuts))
        for total in translations
    )


def boundary_orbit_equivalent(
    left: int,
    right: int,
    boundaries: Iterable[int],
    actions: Iterable[int],
    horizon: int,
) -> bool:
    """Whether two states lie in one cell of the reachable boundary orbit."""
    _require_int("left", left)
    _require_int("right", right)
    if left == right:
        return True
    low, high = sorted((left, right))
    cuts = reachable_boundary_cuts(boundaries, actions, horizon)
    return not any(low < cut <= high for cut in cuts)


def positive_semigroup_below(actions: Iterable[int], cutoff: int) -> tuple[int, ...]:
    """Elements of ``<actions>`` in ``[0, cutoff)`` for positive generators."""
    values = _positive_actions(actions)
    _require_positive("cutoff", cutoff)
    reached = {0}
    frontier = [0]
    while frontier:
        total = frontier.pop()
        for action in values:
            nxt = total + action
            if nxt < cutoff and nxt not in reached:
                reached.add(nxt)
                frontier.append(nxt)
    return tuple(sorted(reached))


def one_sided_threshold_rank(
    distance_to_boundary: int,
    actions: Iterable[int],
    horizon: int | None = None,
) -> int:
    """Future rank inside one side of a threshold."""
    _require_positive("distance_to_boundary", distance_to_boundary)
    values = _positive_actions(actions)
    if horizon is None:
        reached = positive_semigroup_below(values, distance_to_boundary)
    else:
        _require_nonnegative("horizon", horizon)
        reached = tuple(
            total
            for total in reachable_translations(values, horizon)
            if 0 <= total < distance_to_boundary
        )
    return sum(total > 0 for total in reached)


def one_sided_window_class_count(
    window_width: int,
    actions: Iterable[int],
    horizon: int | None = None,
) -> int:
    """Exact predictive class count in a threshold-side window of ``window_width``."""
    _require_positive("window_width", window_width)
    values = _positive_actions(actions)
    if horizon is None:
        reached = positive_semigroup_below(values, window_width)
    else:
        _require_nonnegative("horizon", horizon)
        reached = tuple(
            total
            for total in reachable_translations(values, horizon)
            if 0 <= total < window_width
        )
    return 1 + sum(total > 0 for total in reached)


def group_completed_window_class_count(window_width: int, actions: Iterable[int]) -> int:
    """Uniform gcd-cell count after replacing a positive semigroup by its group completion."""
    _require_positive("window_width", window_width)
    grain = action_grain(actions)
    return (window_width + grain - 1) // grain


def relevant_semigroup_holes(window_width: int, actions: Iterable[int]) -> tuple[int, ...]:
    """Positive gcd multiples below the window width missing from the one-sided semigroup."""
    _require_positive("window_width", window_width)
    values = _positive_actions(actions)
    grain = action_grain(values)
    reached = set(positive_semigroup_below(values, window_width))
    return tuple(
        total
        for total in range(grain, window_width, grain)
        if total not in reached
    )


def group_completion_overrefinement_defect(window_width: int, actions: Iterable[int]) -> int:
    """Extra classes retained by uniform gcd refinement versus actual one-sided reachability."""
    return len(relevant_semigroup_holes(window_width, actions))


@dataclass(frozen=True)
class NumericalSemigroupProfile:
    """Normalized numerical-semigroup data for a positive action language."""

    grain: int
    normalized_generators: tuple[int, ...]
    apery_set: tuple[int, ...]
    conductor: int
    physical_irregular_depth: int


def numerical_semigroup_profile(actions: Iterable[int]) -> NumericalSemigroupProfile:
    """Return gcd normalization, Apéry set, conductor and physical boundary depth."""
    values = _positive_actions(actions)
    grain = action_grain(values)
    generators = tuple(sorted({action // grain for action in values}))
    multiplicity = min(generators)

    infinity = 10**30
    distances = [infinity] * multiplicity
    distances[0] = 0
    queue: list[tuple[int, int]] = [(0, 0)]
    while queue:
        distance, residue = heappop(queue)
        if distance != distances[residue]:
            continue
        for generator in generators:
            candidate = distance + generator
            target = candidate % multiplicity
            if candidate < distances[target]:
                distances[target] = candidate
                heappush(queue, (candidate, target))

    apery = tuple(distances)
    conductor = max(apery) - multiplicity + 1
    return NumericalSemigroupProfile(
        grain=grain,
        normalized_generators=generators,
        apery_set=apery,
        conductor=conductor,
        physical_irregular_depth=grain * conductor,
    )


def signed_group_completion_grain(actions: Iterable[int]) -> int:
    """Return gcd grain for a genuinely two-sided signed translation language."""
    values = _integer_actions(actions)
    if not any(action > 0 for action in values) or not any(action < 0 for action in values):
        raise ValueError("signed group completion requires at least one positive and one negative action")
    return action_grain(values)


def threshold_group_coordinate(value: int, threshold: int, grain: int) -> int:
    """Uniform single-threshold coordinate ``ceil((threshold-value)/grain)``."""
    _require_int("value", value)
    _require_int("threshold", threshold)
    _require_positive("grain", grain)
    return -((value - threshold) // grain)


def translate_group_coordinate(coordinate: int, action: int, grain: int) -> int:
    """Exact transport ``K -> K - action/grain`` for a group-completed action."""
    _require_int("coordinate", coordinate)
    _require_int("action", action)
    _require_positive("grain", grain)
    if action % grain != 0:
        raise ValueError("action must be divisible by the group-completion grain")
    return coordinate - action // grain


def cyclic_reachable_residues(width: int, actions: Iterable[int]) -> tuple[int, ...]:
    """Submonoid generated by action residues in the finite cyclic group ``Z/width Z``."""
    _require_positive("width", width)
    values = _integer_actions(actions, allow_empty=True)
    residues = tuple(action % width for action in values)
    reached = {0}
    frontier = [0]
    while frontier:
        residue = frontier.pop()
        for action in residues:
            nxt = (residue + action) % width
            if nxt not in reached:
                reached.add(nxt)
                frontier.append(nxt)
    return tuple(sorted(reached))


def cyclic_gcd_subgroup(width: int, actions: Iterable[int]) -> tuple[int, ...]:
    """The subgroup generated by the same residues, written as gcd-spaced residues."""
    _require_positive("width", width)
    values = _integer_actions(actions, allow_empty=True)
    grain = width
    for action in values:
        grain = gcd(grain, abs(action))
    return tuple(range(0, width, grain))
