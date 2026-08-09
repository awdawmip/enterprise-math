"""Adjoint boundary-pullback precision for P024.

P024 Stage 1 treats translations, for which a future threshold ``b`` pulls back
to ``b-a``.  This module isolates the lower-level order-theoretic mechanism.

An action is supplied together with a boundary pullback ``lambda`` satisfying

    lambda(b) <= x  iff  b <= F(x).

Thus ``lambda`` is a left adjoint of the forward action ``F``.  Future threshold
boundaries compose contravariantly: if the forward word applies ``F`` then
``G``, the pulled boundary is ``lambda_F(lambda_G(b))``.

The executable layer uses Python callables as theorem witnesses; it never tries
to discover an adjoint by unbounded search.  Finite-box audit helpers are only
regressions, not proof procedures.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Callable, Iterable, Sequence

from .core import collapse, integer_nth_root


IntMap = Callable[[int], int]
Word = tuple[int, ...]


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _require_natural(name: str, value: int) -> None:
    _require_int(name, value)
    if value < 0:
        raise ValueError(f"{name} must be nonnegative")


def _require_positive(name: str, value: int) -> None:
    _require_int(name, value)
    if value <= 0:
        raise ValueError(f"{name} must be positive")


def ceil_div(numerator: int, denominator: int) -> int:
    _require_int("numerator", numerator)
    _require_positive("denominator", denominator)
    return -((-numerator) // denominator)


@dataclass(frozen=True)
class AdjointChainAction:
    """Forward chain action with an explicit principal-boundary pullback."""

    name: str
    forward: IntMap
    pullback: IntMap

    def apply(self, state: int) -> int:
        _require_int("state", state)
        result = self.forward(state)
        _require_int("forward result", result)
        return result

    def pullback_cut(self, boundary: int) -> int:
        _require_int("boundary", boundary)
        result = self.pullback(boundary)
        _require_int("pullback result", result)
        return result

    def adjunction_holds(self, boundary: int, state: int) -> bool:
        """Audit ``lambda(b)<=x iff b<=F(x)`` at one supplied pair."""
        return (self.pullback_cut(boundary) <= state) == (boundary <= self.apply(state))


def translation_action(increment: int) -> AdjointChainAction:
    _require_int("increment", increment)
    return AdjointChainAction(
        name=f"translate({increment})",
        forward=lambda x, a=increment: x + a,
        pullback=lambda b, a=increment: b - a,
    )


def dilation_action(multiplier: int) -> AdjointChainAction:
    """Action ``x -> k*x`` on Z, with pullback ``ceil(b/k)``."""
    _require_positive("multiplier", multiplier)
    return AdjointChainAction(
        name=f"dilate({multiplier})",
        forward=lambda x, k=multiplier: k * x,
        pullback=lambda b, k=multiplier: ceil_div(b, k),
    )


def floor_division_action(divisor: int) -> AdjointChainAction:
    """Action ``x -> x//d`` on Z, with pullback ``d*b``."""
    _require_positive("divisor", divisor)
    return AdjointChainAction(
        name=f"floor_div({divisor})",
        forward=lambda x, d=divisor: x // d,
        pullback=lambda b, d=divisor: d * b,
    )


def natural_root_action(power: int) -> AdjointChainAction:
    """P008 integer root on N0, with power map as threshold pullback."""
    _require_positive("power", power)

    def forward(value: int, p: int = power) -> int:
        _require_natural("root state", value)
        return integer_nth_root(value, p)

    def pullback(boundary: int, p: int = power) -> int:
        _require_natural("root boundary", boundary)
        return boundary**p

    return AdjointChainAction(f"root({power})", forward, pullback)


def natural_quotient_action(divisor: int) -> AdjointChainAction:
    """Natural-number quotient ``n//d``, with multiplication pullback."""
    _require_positive("divisor", divisor)

    def forward(value: int, d: int = divisor) -> int:
        _require_natural("quotient state", value)
        return value // d

    def pullback(boundary: int, d: int = divisor) -> int:
        _require_natural("quotient boundary", boundary)
        return boundary * d

    return AdjointChainAction(f"natural_quotient({divisor})", forward, pullback)


def natural_collapse_action(power: int) -> AdjointChainAction:
    """P008/P003 perfect-power collapse with next-power boundary pullback."""
    _require_positive("power", power)

    def forward(value: int, p: int = power) -> int:
        _require_natural("collapse state", value)
        return collapse(value, p)

    def pullback(boundary: int, p: int = power) -> int:
        _require_natural("collapse boundary", boundary)
        root = integer_nth_root(boundary, p)
        if root**p < boundary:
            root += 1
        return root**p

    return AdjointChainAction(f"collapse({power})", forward, pullback)


def _actions(actions: Iterable[AdjointChainAction]) -> tuple[AdjointChainAction, ...]:
    result = tuple(actions)
    if not result:
        raise ValueError("at least one action is required")
    return result


def _boundaries(boundaries: Iterable[int]) -> tuple[int, ...]:
    result = tuple(sorted(set(boundaries)))
    if not result:
        raise ValueError("at least one boundary is required")
    for boundary in result:
        _require_int("boundary", boundary)
    return result


def action_words(action_count: int, horizon: int) -> tuple[Word, ...]:
    _require_positive("action_count", action_count)
    _require_int("horizon", horizon)
    if horizon < 0:
        raise ValueError("horizon must be nonnegative")
    words: list[Word] = []
    for length in range(horizon + 1):
        words.extend(product(range(action_count), repeat=length))
    return tuple(words)


def apply_action_word(
    state: int,
    actions: Iterable[AdjointChainAction],
    word: Sequence[int],
) -> int:
    value = state
    action_values = _actions(actions)
    for index in word:
        if isinstance(index, bool) or not isinstance(index, int) or not 0 <= index < len(action_values):
            raise ValueError("word contains an invalid action index")
        value = action_values[index].apply(value)
    return value


def pullback_boundary_word(
    boundary: int,
    actions: Iterable[AdjointChainAction],
    word: Sequence[int],
) -> int:
    """Pull a terminal threshold back through a forward action word."""
    value = boundary
    action_values = _actions(actions)
    for index in reversed(tuple(word)):
        if isinstance(index, bool) or not isinstance(index, int) or not 0 <= index < len(action_values):
            raise ValueError("word contains an invalid action index")
        value = action_values[index].pullback_cut(value)
    return value


def boundary_orbit_levels(
    boundaries: Iterable[int],
    actions: Iterable[AdjointChainAction],
    horizon: int,
) -> tuple[tuple[int, ...], ...]:
    """Exact pulled cuts created by words of each *exact* length."""
    current = set(_boundaries(boundaries))
    action_values = _actions(actions)
    _require_int("horizon", horizon)
    if horizon < 0:
        raise ValueError("horizon must be nonnegative")
    levels = [tuple(sorted(current))]
    for _ in range(horizon):
        current = {
            action.pullback_cut(boundary)
            for action in action_values
            for boundary in current
        }
        levels.append(tuple(sorted(current)))
    return tuple(levels)


def boundary_orbit(
    boundaries: Iterable[int],
    actions: Iterable[AdjointChainAction],
    horizon: int,
) -> tuple[int, ...]:
    reached: set[int] = set()
    for level in boundary_orbit_levels(boundaries, actions, horizon):
        reached.update(level)
    return tuple(sorted(reached))


def boundary_rank(state: int, cuts: Iterable[int]) -> int:
    _require_int("state", state)
    values = tuple(sorted(set(cuts)))
    for cut in values:
        _require_int("cut", cut)
    return sum(cut <= state for cut in values)


def future_boundary_rank(
    state: int,
    boundaries: Iterable[int],
    actions: Iterable[AdjointChainAction],
    horizon: int,
) -> int:
    return boundary_rank(state, boundary_orbit(boundaries, actions, horizon))


def direct_future_threshold_signature(
    state: int,
    boundaries: Iterable[int],
    actions: Iterable[AdjointChainAction],
    horizon: int,
) -> tuple[tuple[bool, ...], ...]:
    boundary_values = _boundaries(boundaries)
    action_values = _actions(actions)
    return tuple(
        tuple(boundary <= apply_action_word(state, action_values, word) for boundary in boundary_values)
        for word in action_words(len(action_values), horizon)
    )


def pullback_word_signature(
    word: Sequence[int],
    boundaries: Iterable[int],
    actions: Iterable[AdjointChainAction],
) -> tuple[int, ...]:
    boundary_values = _boundaries(boundaries)
    action_values = _actions(actions)
    return tuple(
        pullback_boundary_word(boundary, action_values, word)
        for boundary in boundary_values
    )


def naive_boundary_cut_bound(boundary_count: int, action_count: int, horizon: int) -> int:
    """Word-count upper bound on distinct finite-horizon pulled cuts."""
    _require_positive("boundary_count", boundary_count)
    _require_positive("action_count", action_count)
    _require_int("horizon", horizon)
    if horizon < 0:
        raise ValueError("horizon must be nonnegative")
    if action_count == 1:
        word_count = horizon + 1
    else:
        word_count = (action_count ** (horizon + 1) - 1) // (action_count - 1)
    return boundary_count * word_count


@dataclass(frozen=True)
class BoundaryStabilization:
    cuts: tuple[int, ...]
    horizon: int
    stabilized: bool


def stabilize_boundary_orbit(
    boundaries: Iterable[int],
    actions: Iterable[AdjointChainAction],
    max_horizon: int,
) -> BoundaryStabilization:
    """Detect finite closure of the pulled-boundary orbit up to a declared cap."""
    boundary_values = _boundaries(boundaries)
    action_values = _actions(actions)
    _require_int("max_horizon", max_horizon)
    if max_horizon < 0:
        raise ValueError("max_horizon must be nonnegative")

    reached = set(boundary_values)
    frontier = set(boundary_values)
    if not frontier:
        return BoundaryStabilization((), 0, True)

    for horizon in range(1, max_horizon + 1):
        next_frontier = {
            action.pullback_cut(boundary)
            for action in action_values
            for boundary in frontier
        }
        new = next_frontier - reached
        reached.update(next_frontier)
        if not new:
            return BoundaryStabilization(tuple(sorted(reached)), horizon, True)
        frontier = next_frontier
    return BoundaryStabilization(tuple(sorted(reached)), max_horizon, False)


def audit_adjunction_box(
    action: AdjointChainAction,
    boundaries: Iterable[int],
    states: Iterable[int],
) -> bool:
    """Finite regression audit only; not a proof of a global adjunction."""
    boundary_values = _boundaries(boundaries)
    state_values = tuple(states)
    if not state_values:
        raise ValueError("at least one state is required")
    for state in state_values:
        _require_int("state", state)
    return all(
        action.adjunction_holds(boundary, state)
        for boundary in boundary_values
        for state in state_values
    )
