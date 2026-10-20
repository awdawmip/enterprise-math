"""Task-relative precision for one repeated action under conjunctive linear guards.

Let ``x in Z^d`` and let a finite family of nonconstant integer upper guards be
interpreted as strict action-domain conditions

    row_i . x < threshold_i.

One fixed vector translation ``a`` may be repeated while *every* guard remains
satisfied.  The future language in this module observes only whether words
``a^m`` are defined; it does not observe which guard is closest to failure.

Normalize each guard to its primitive integer score ``s_i`` and cut ``g_i``.
Let ``delta_i`` be the primitive score shift produced by one action.  The exact
number of legal action repetitions allowed by guard ``i`` is

    tau_i = 0                                  if s_i >= g_i,
            infinity                           if s_i < g_i and delta_i <= 0,
            ceil((g_i-s_i)/delta_i)             if delta_i > 0.

The conjunctive action survives exactly

    tau(x) = min_i tau_i(x)

repetitions.  Hence through finite horizon ``h`` the complete definedness future
signature is determined by the single capped lifetime

    min(h, tau(x)),

with infinity capped to ``h``.  There are therefore at most ``h+1`` predictive
classes regardless of the number of guards or ambient dimension.

This is a sharp task-relative compression boundary.  Retaining every individual
guard score/rank is future-safe but can be much finer than necessary when the
future language observes only the conjunction.  If later futures inspect which
guard failed, individual guard values, or additional actions, the scalar
lifetime need not remain sufficient.

Linear-guard normalization and projected action shifts are canonical P024
machinery.  Minimum-lifetime/bottleneck reasoning is standard.  This module
owns only the exact finite guarded-action specialization.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence

from .lattice_guard_precision import (
    IntegerGuard,
    ceil_div,
    projected_action_generators,
    translated_point,
)

Vector = tuple[int, ...]


def _guards(guards: Iterable[IntegerGuard]) -> tuple[IntegerGuard, ...]:
    values = tuple(guards)
    if not values:
        raise ValueError("at least one guard is required")
    if any(not isinstance(guard, IntegerGuard) for guard in values):
        raise TypeError("guards must contain IntegerGuard values")
    if any(guard.is_constant for guard in values):
        raise ValueError("conjunctive lifetime requires nonconstant guards")
    dimension = len(values[0].row)
    if any(len(guard.row) != dimension for guard in values):
        raise ValueError("all guards must have the same state dimension")
    return values


def _vector(values: Sequence[int] | Iterable[int], dimension: int, name: str) -> Vector:
    result = tuple(values)
    if len(result) != dimension:
        raise ValueError(f"{name} dimension differs from guard dimension")
    for value in result:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(f"{name} entries must be integers")
    return result


@dataclass(frozen=True)
class GuardLifetime:
    primitive_score: int
    primitive_cut: int
    action_shift: int
    legal_repetitions: int | None

    @property
    def is_infinite(self) -> bool:
        return self.legal_repetitions is None


def single_guard_lifetime(
    point: Sequence[int],
    guard: IntegerGuard,
    action: Sequence[int],
) -> GuardLifetime:
    """Exact legal repetition count for one strict upper guard.

    ``None`` denotes infinity.
    """
    values = _guards((guard,))
    dimension = len(values[0].row)
    x = _vector(point, dimension, "point")
    a = _vector(action, dimension, "action")
    score = guard.primitive_score(x)
    cut = guard.primitive_threshold
    shift = projected_action_generators(guard, (a,))[0]

    if score >= cut:
        repetitions: int | None = 0
    elif shift <= 0:
        repetitions = None
    else:
        repetitions = ceil_div(cut - score, shift)
    return GuardLifetime(
        primitive_score=score,
        primitive_cut=cut,
        action_shift=shift,
        legal_repetitions=repetitions,
    )


def conjunctive_guard_lifetimes(
    point: Sequence[int],
    guards: Iterable[IntegerGuard],
    action: Sequence[int],
) -> tuple[GuardLifetime, ...]:
    values = _guards(guards)
    dimension = len(values[0].row)
    x = _vector(point, dimension, "point")
    a = _vector(action, dimension, "action")
    return tuple(single_guard_lifetime(x, guard, a) for guard in values)


def conjunctive_guard_lifetime(
    point: Sequence[int],
    guards: Iterable[IntegerGuard],
    action: Sequence[int],
) -> int | None:
    """Minimum legal repetition count; ``None`` means every guard is infinite."""
    lifetimes = conjunctive_guard_lifetimes(point, guards, action)
    finite = [
        lifetime.legal_repetitions
        for lifetime in lifetimes
        if lifetime.legal_repetitions is not None
    ]
    if not finite:
        return None
    return min(finite)


def capped_conjunctive_guard_lifetime(
    point: Sequence[int],
    guards: Iterable[IntegerGuard],
    action: Sequence[int],
    horizon: int,
) -> int:
    if isinstance(horizon, bool) or not isinstance(horizon, int):
        raise TypeError("horizon must be an integer")
    if horizon < 0:
        raise ValueError("horizon must be non-negative")
    lifetime = conjunctive_guard_lifetime(point, guards, action)
    if lifetime is None:
        return horizon
    return min(horizon, lifetime)


def repeated_action_defined_direct(
    point: Sequence[int],
    guards: Iterable[IntegerGuard],
    action: Sequence[int],
    repetitions: int,
) -> bool:
    """Direct vector oracle for ``action^repetitions`` under conjunction."""
    if isinstance(repetitions, bool) or not isinstance(repetitions, int):
        raise TypeError("repetitions must be an integer")
    if repetitions < 0:
        raise ValueError("repetitions must be non-negative")
    values = _guards(guards)
    dimension = len(values[0].row)
    current = _vector(point, dimension, "point")
    a = _vector(action, dimension, "action")
    for _ in range(repetitions):
        if any(guard.evaluate(current) for guard in values):
            return False
        current = translated_point(current, a)
    return True


def repeated_action_defined_closed_form(
    point: Sequence[int],
    guards: Iterable[IntegerGuard],
    action: Sequence[int],
    repetitions: int,
) -> bool:
    """Word definedness from the scalar bottleneck lifetime."""
    if isinstance(repetitions, bool) or not isinstance(repetitions, int):
        raise TypeError("repetitions must be an integer")
    if repetitions < 0:
        raise ValueError("repetitions must be non-negative")
    lifetime = conjunctive_guard_lifetime(point, guards, action)
    return lifetime is None or repetitions <= lifetime


def conjunctive_definedness_signature(
    point: Sequence[int],
    guards: Iterable[IntegerGuard],
    action: Sequence[int],
    horizon: int,
) -> tuple[bool, ...]:
    """Definedness of words ``a^m`` for ``m=0,...,h``."""
    capped = capped_conjunctive_guard_lifetime(
        point, guards, action, horizon
    )
    return tuple(length <= capped for length in range(horizon + 1))


def lifetime_class_count_upper_bound(horizon: int) -> int:
    if isinstance(horizon, bool) or not isinstance(horizon, int):
        raise TypeError("horizon must be an integer")
    if horizon < 0:
        raise ValueError("horizon must be non-negative")
    return horizon + 1
