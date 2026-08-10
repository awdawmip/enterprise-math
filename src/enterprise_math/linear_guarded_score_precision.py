"""Higher-dimensional translations with one linear guard reduce to scalar P024.

Let ``x in Z^d`` and let one nonconstant integer guard row ``r`` with threshold
``theta`` declare an action legal exactly while

    r . x < theta.

Write ``c=gcd(r)`` and ``rbar=r/c``.  Since ``r.x`` is always a multiple of
``c``, the guard is exactly

    s(x) = rbar . x < ceil(theta/c).

Every vector translation ``a`` changes this primitive score by the integer

    delta(a) = rbar . a.

Therefore the entire state-dependent action language, including prefix
legality and terminal ordered-threshold observations of the same primitive
score, factors through the one-dimensional guarded-translation calculus of
``guarded_translation_precision``.  A literal vector word has exactly the same
``(T,H)`` profile as its word of projected scalar increments.

Consequences:

* ambient state dimension is future-invisible once primitive score is fixed;
* vector actions with the same projected increment are indistinguishable for
  this declared future language;
* the exact horizon partition is obtained by the scalar guarded boundary cuts
  in primitive score space and then pulled back through ``s``.

This is the state-dependent analogue of canonical P024 lattice-guard score
factorization.  Multiple simultaneous guards or aggregate Boolean guard
languages can require a richer task-relative quotient and are not claimed here.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence

from .action_language_precision import ordered_threshold_observation
from .guarded_translation_precision import (
    GuardedTranslationProfile,
    guarded_boundary_equivalent,
    guarded_future_signature,
    guarded_reachable_boundary_cuts,
    guarded_word_profile,
)
from .lattice_guard_precision import (
    IntegerGuard,
    dot,
    projected_action_generators,
    translated_point,
)

Vector = tuple[int, ...]


def _require_nonconstant_guard(guard: IntegerGuard) -> None:
    if not isinstance(guard, IntegerGuard):
        raise TypeError("guard must be IntegerGuard")
    if guard.is_constant:
        raise ValueError("linear guarded score reduction requires a nonconstant guard")


def _vector(value: Sequence[int] | Iterable[int], dimension: int, name: str) -> Vector:
    result = tuple(value)
    if len(result) != dimension:
        raise ValueError(f"{name} dimension differs from guard dimension")
    for entry in result:
        if isinstance(entry, bool) or not isinstance(entry, int):
            raise TypeError(f"{name} entries must be integers")
    return result


def primitive_upper_guard_cut(guard: IntegerGuard) -> int:
    """Exact integer cut ``ceil(theta/gcd(row))`` for the strict raw guard."""
    _require_nonconstant_guard(guard)
    return guard.primitive_threshold


def linear_guard_enabled(point: Sequence[int], guard: IntegerGuard) -> bool:
    """Whether ``row.point < threshold`` in exact raw and primitive coordinates."""
    _require_nonconstant_guard(guard)
    vector = _vector(point, len(guard.row), "point")
    raw = dot(guard.row, vector) < guard.threshold
    primitive = guard.primitive_score(vector) < primitive_upper_guard_cut(guard)
    if raw != primitive:
        raise AssertionError("raw and primitive strict guard semantics disagree")
    return raw


def projected_action_word(
    word: Iterable[Sequence[int]],
    guard: IntegerGuard,
) -> tuple[int, ...]:
    """Project a literal vector-action word to primitive score increments."""
    _require_nonconstant_guard(guard)
    dimension = len(guard.row)
    result = []
    for action in word:
        vector = _vector(action, dimension, "action")
        result.append(dot(guard.primitive_row, vector))
    return tuple(result)


def linear_guarded_word_profile(
    word: Iterable[Sequence[int]],
    guard: IntegerGuard,
) -> GuardedTranslationProfile:
    return guarded_word_profile(projected_action_word(word, guard))


@dataclass(frozen=True)
class LinearGuardedOutcome:
    defined: bool
    final_point: Vector | None
    final_primitive_score: int | None
    observation: int | None


def apply_linear_guarded_word(
    point: Sequence[int],
    word: Iterable[Sequence[int]],
    guard: IntegerGuard,
    score_boundaries: Iterable[int] = (),
) -> LinearGuardedOutcome:
    """Direct vector oracle for one strict linear guard and score observation."""
    _require_nonconstant_guard(guard)
    dimension = len(guard.row)
    current = _vector(point, dimension, "point")
    boundaries = tuple(score_boundaries)
    for boundary in boundaries:
        if isinstance(boundary, bool) or not isinstance(boundary, int):
            raise TypeError("score boundaries must be integers")

    for action in tuple(word):
        vector = _vector(action, dimension, "action")
        if not linear_guard_enabled(current, guard):
            return LinearGuardedOutcome(False, None, None, None)
        current = translated_point(current, vector)

    score = guard.primitive_score(current)
    return LinearGuardedOutcome(
        True,
        current,
        score,
        ordered_threshold_observation(score, boundaries),
    )


def projected_action_alphabet(
    guard: IntegerGuard,
    actions: Iterable[Sequence[int]],
) -> tuple[int, ...]:
    """Distinct primitive-score increments generated by the vector action alphabet."""
    _require_nonconstant_guard(guard)
    shifts = projected_action_generators(guard, actions)
    return tuple(sorted(set(shifts)))


def linear_guarded_future_signature(
    point: Sequence[int],
    guard: IntegerGuard,
    actions: Iterable[Sequence[int]],
    score_boundaries: Iterable[int],
    horizon: int,
):
    """Exact future signature in the reduced one-dimensional primitive score world."""
    _require_nonconstant_guard(guard)
    score = guard.primitive_score(point)
    projected = projected_action_alphabet(guard, actions)
    return guarded_future_signature(
        score,
        score_boundaries,
        projected,
        primitive_upper_guard_cut(guard),
        horizon,
    )


def linear_guarded_score_cuts(
    guard: IntegerGuard,
    actions: Iterable[Sequence[int]],
    score_boundaries: Iterable[int],
    horizon: int,
) -> tuple[int, ...]:
    """Exact future-visible cuts in the primitive scalar score coordinate."""
    _require_nonconstant_guard(guard)
    projected = projected_action_alphabet(guard, actions)
    return guarded_reachable_boundary_cuts(
        score_boundaries,
        projected,
        primitive_upper_guard_cut(guard),
        horizon,
    )


def linear_guarded_points_equivalent(
    left: Sequence[int],
    right: Sequence[int],
    guard: IntegerGuard,
    actions: Iterable[Sequence[int]],
    score_boundaries: Iterable[int],
    horizon: int,
) -> bool:
    """Future equivalence pulled back from the primitive score coordinate."""
    _require_nonconstant_guard(guard)
    left_score = guard.primitive_score(left)
    right_score = guard.primitive_score(right)
    projected = projected_action_alphabet(guard, actions)
    return guarded_boundary_equivalent(
        left_score,
        right_score,
        score_boundaries,
        projected,
        primitive_upper_guard_cut(guard),
        horizon,
    )
