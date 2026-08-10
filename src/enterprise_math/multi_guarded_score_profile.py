"""Exact word profiles for translations guarded by multiple linear scores.

Let ``x in Z^d`` and let ``r`` nonconstant integer upper guards define one
conjunctive action domain.  After canonical gcd normalization, state information
visible to the guards is the primitive score vector

    s(x) = (s_1(x), ..., s_r(x)).

Every vector action projects to an integer score-shift vector ``delta(a)``.  For
one nonempty literal word define, coordinatewise,

    T_i = final cumulative projected shift,
    H_i = maximum projected prefix shift before the terminal update.

The word is executable exactly when

    s_i(x) < g_i - H_i      for every guard i,

and, if executable, the exact terminal score vector is ``s(x)+T``.  Therefore
``(T,H)`` is a complete literal-word quotient for conjunctive legality and every
future observation that factors through the full terminal primitive score
vector.

Profiles compose coordinatewise:

    T(uv) = T(u)+T(v),
    H(uv) = max(H(u), T(u)+H(v)).

For guard count ``r``, horizon ``h>=1`` and maximum absolute projected action
shift ``M``, the number of distinct profiles is bounded by

    1 + ((2 h M + 1) ((h-1) M + 1))^r.

Thus for fixed effective guard rank and action alphabet the word language has a
polynomial-size exact profile even though literal word count is exponential.
The polynomial degree depends on guard-score dimension, not ambient state
dimension.

This module is the multi-guard word-level layer between the one-guard reduction
and more task-specific quotients such as bottleneck lifetime.  It does not claim
that the full score/profile vector is minimal for every aggregate future
language.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence

from .lattice_guard_precision import IntegerGuard, dot, translated_point

Vector = tuple[int, ...]


def _guards(guards: Iterable[IntegerGuard]) -> tuple[IntegerGuard, ...]:
    values = tuple(guards)
    if not values:
        raise ValueError("at least one guard is required")
    if any(not isinstance(guard, IntegerGuard) for guard in values):
        raise TypeError("guards must contain IntegerGuard values")
    if any(guard.is_constant for guard in values):
        raise ValueError("multi-guard profile requires nonconstant guards")
    dimension = len(values[0].row)
    if any(len(guard.row) != dimension for guard in values):
        raise ValueError("all guards must have the same state dimension")
    return values


def _vector(values: Sequence[int] | Iterable[int], dimension: int, name: str) -> Vector:
    result = tuple(values)
    if len(result) != dimension:
        raise ValueError(f"{name} dimension differs from state dimension")
    for value in result:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(f"{name} entries must be integers")
    return result


def _actions(
    actions: Iterable[Sequence[int]],
    dimension: int,
) -> tuple[Vector, ...]:
    values = tuple(_vector(action, dimension, "action") for action in actions)
    if not values:
        raise ValueError("at least one action is required")
    return tuple(sorted(set(values)))


def primitive_guard_cuts(guards: Iterable[IntegerGuard]) -> tuple[int, ...]:
    values = _guards(guards)
    return tuple(guard.primitive_threshold for guard in values)


def primitive_score_vector(
    point: Sequence[int],
    guards: Iterable[IntegerGuard],
) -> tuple[int, ...]:
    values = _guards(guards)
    x = _vector(point, len(values[0].row), "point")
    return tuple(guard.primitive_score(x) for guard in values)


def projected_action_shift_vector(
    action: Sequence[int],
    guards: Iterable[IntegerGuard],
) -> tuple[int, ...]:
    values = _guards(guards)
    vector = _vector(action, len(values[0].row), "action")
    return tuple(dot(guard.primitive_row, vector) for guard in values)


@dataclass(frozen=True)
class MultiGuardedProfile:
    total_shifts: tuple[int, ...]
    preterminal_peaks: tuple[int, ...] | None

    @property
    def is_empty(self) -> bool:
        return self.preterminal_peaks is None


def _validate_profile(profile: MultiGuardedProfile, guard_count: int | None = None) -> None:
    if not isinstance(profile, MultiGuardedProfile):
        raise TypeError("profile must be MultiGuardedProfile")
    for value in profile.total_shifts:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("profile shifts must be integers")
    if guard_count is not None and len(profile.total_shifts) != guard_count:
        raise ValueError("profile dimension differs from guard count")
    if profile.is_empty:
        if any(profile.total_shifts):
            raise ValueError("empty profile must have zero total shift")
        return
    assert profile.preterminal_peaks is not None
    if len(profile.preterminal_peaks) != len(profile.total_shifts):
        raise ValueError("profile peak and total dimensions must agree")
    for peak in profile.preterminal_peaks:
        if isinstance(peak, bool) or not isinstance(peak, int):
            raise TypeError("profile peaks must be integers")
        if peak < 0:
            raise ValueError("preterminal peaks must contain the zero prefix")


def empty_multi_guarded_profile(guard_count: int) -> MultiGuardedProfile:
    if isinstance(guard_count, bool) or not isinstance(guard_count, int):
        raise TypeError("guard_count must be an integer")
    if guard_count <= 0:
        raise ValueError("guard_count must be positive")
    return MultiGuardedProfile((0,) * guard_count, None)


def multi_guarded_word_profile(
    word: Iterable[Sequence[int]],
    guards: Iterable[IntegerGuard],
) -> MultiGuardedProfile:
    guard_values = _guards(guards)
    dimension = len(guard_values[0].row)
    actions = tuple(_vector(action, dimension, "action") for action in word)
    count = len(guard_values)
    if not actions:
        return empty_multi_guarded_profile(count)
    total = [0] * count
    peaks = [0] * count
    for action in actions:
        for index in range(count):
            peaks[index] = max(peaks[index], total[index])
        shift = projected_action_shift_vector(action, guard_values)
        for index, value in enumerate(shift):
            total[index] += value
    return MultiGuardedProfile(tuple(total), tuple(peaks))


def append_multi_guarded_action(
    profile: MultiGuardedProfile,
    action: Sequence[int],
    guards: Iterable[IntegerGuard],
) -> MultiGuardedProfile:
    guard_values = _guards(guards)
    count = len(guard_values)
    _validate_profile(profile, count)
    shift = projected_action_shift_vector(action, guard_values)
    if profile.is_empty:
        return MultiGuardedProfile(shift, (0,) * count)
    assert profile.preterminal_peaks is not None
    return MultiGuardedProfile(
        tuple(
            total + delta
            for total, delta in zip(profile.total_shifts, shift, strict=True)
        ),
        tuple(
            max(peak, total)
            for peak, total in zip(
                profile.preterminal_peaks,
                profile.total_shifts,
                strict=True,
            )
        ),
    )


def compose_multi_guarded_profiles(
    left: MultiGuardedProfile,
    right: MultiGuardedProfile,
) -> MultiGuardedProfile:
    _validate_profile(left)
    _validate_profile(right)
    if len(left.total_shifts) != len(right.total_shifts):
        raise ValueError("profile dimensions must agree")
    if left.is_empty:
        return right
    if right.is_empty:
        return left
    assert left.preterminal_peaks is not None
    assert right.preterminal_peaks is not None
    return MultiGuardedProfile(
        tuple(
            a + b
            for a, b in zip(left.total_shifts, right.total_shifts, strict=True)
        ),
        tuple(
            max(h1, t1 + h2)
            for h1, t1, h2 in zip(
                left.preterminal_peaks,
                left.total_shifts,
                right.preterminal_peaks,
                strict=True,
            )
        ),
    )


def _profile_sort_key(profile: MultiGuardedProfile):
    return (
        0 if profile.is_empty else 1,
        profile.total_shifts,
        () if profile.preterminal_peaks is None else profile.preterminal_peaks,
    )


def multi_guarded_profiles(
    actions: Iterable[Sequence[int]],
    guards: Iterable[IntegerGuard],
    horizon: int,
) -> tuple[MultiGuardedProfile, ...]:
    guard_values = _guards(guards)
    dimension = len(guard_values[0].row)
    action_values = _actions(actions, dimension)
    if isinstance(horizon, bool) or not isinstance(horizon, int):
        raise TypeError("horizon must be an integer")
    if horizon < 0:
        raise ValueError("horizon must be non-negative")
    empty = empty_multi_guarded_profile(len(guard_values))
    reached = {empty}
    frontier = {empty}
    for _ in range(horizon):
        frontier = {
            append_multi_guarded_action(profile, action, guard_values)
            for profile in frontier
            for action in action_values
        }
        reached.update(frontier)
    return tuple(sorted(reached, key=_profile_sort_key))


def projected_profile_count_upper_bound(
    actions: Iterable[Sequence[int]],
    guards: Iterable[IntegerGuard],
    horizon: int,
) -> int:
    guard_values = _guards(guards)
    dimension = len(guard_values[0].row)
    action_values = _actions(actions, dimension)
    if isinstance(horizon, bool) or not isinstance(horizon, int):
        raise TypeError("horizon must be an integer")
    if horizon < 0:
        raise ValueError("horizon must be non-negative")
    if horizon == 0:
        return 1
    amplitude = max(
        abs(shift)
        for action in action_values
        for shift in projected_action_shift_vector(action, guard_values)
    )
    per_total = 2 * horizon * amplitude + 1
    per_peak = (horizon - 1) * amplitude + 1
    return 1 + (per_total * per_peak) ** len(guard_values)


def multi_guarded_profile_defined(
    point: Sequence[int],
    profile: MultiGuardedProfile,
    guards: Iterable[IntegerGuard],
) -> bool:
    guard_values = _guards(guards)
    _validate_profile(profile, len(guard_values))
    if profile.is_empty:
        return True
    assert profile.preterminal_peaks is not None
    scores = primitive_score_vector(point, guard_values)
    cuts = primitive_guard_cuts(guard_values)
    return all(
        score < cut - peak
        for score, cut, peak in zip(
            scores, cuts, profile.preterminal_peaks, strict=True
        )
    )


@dataclass(frozen=True)
class MultiGuardedOutcome:
    defined: bool
    final_point: Vector | None
    final_scores: tuple[int, ...] | None


def apply_multi_guarded_word(
    point: Sequence[int],
    word: Iterable[Sequence[int]],
    guards: Iterable[IntegerGuard],
) -> MultiGuardedOutcome:
    guard_values = _guards(guards)
    dimension = len(guard_values[0].row)
    current = _vector(point, dimension, "point")
    for action in tuple(word):
        vector = _vector(action, dimension, "action")
        if any(guard.evaluate(current) for guard in guard_values):
            return MultiGuardedOutcome(False, None, None)
        current = translated_point(current, vector)
    return MultiGuardedOutcome(
        True,
        current,
        primitive_score_vector(current, guard_values),
    )


def apply_multi_guarded_profile(
    point: Sequence[int],
    profile: MultiGuardedProfile,
    guards: Iterable[IntegerGuard],
) -> MultiGuardedOutcome:
    guard_values = _guards(guards)
    dimension = len(guard_values[0].row)
    x = _vector(point, dimension, "point")
    _validate_profile(profile, len(guard_values))
    if not multi_guarded_profile_defined(x, profile, guard_values):
        return MultiGuardedOutcome(False, None, None)
    initial_scores = primitive_score_vector(x, guard_values)
    final_scores = tuple(
        score + shift
        for score, shift in zip(initial_scores, profile.total_shifts, strict=True)
    )
    # The ambient final point is not reconstructible from projected profile
    # alone when the guard-score map has a kernel.  Preserve that boundary.
    final_point = x if profile.is_empty else None
    return MultiGuardedOutcome(True, final_point, final_scores)
