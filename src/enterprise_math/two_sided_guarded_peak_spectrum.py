"""Exact guard-only peak spectrum for integer translation action languages.

The generic guarded-word profile records both final translation ``T`` and the
maximum preterminal prefix translation ``H``.  If terminal observations are
constant and the future language asks only whether each guarded word is
defined, then only the possible peak values ``H`` matter.

For any finite integer action alphabet containing both signs and horizon
``h>=1``, let ``M_(h-1)`` be the cumulative translations reachable by words of
length at most ``h-1``.  Then the exact set of preterminal peak values realized
by words of length at most ``h`` is

    P_h = M_(h-1) intersect N_0.

The forward inclusion is immediate because every peak is one proper prefix
total.  Conversely, if ``t>=0`` is reachable in at most ``h-1`` actions, reorder
one realizing multiset with all negative actions first and all nonnegative
actions last.  The reordered prefix reaches ``t`` without exceeding ``t``;
appending any declared action makes that occurrence preterminal, so the full
word has peak exactly ``t``.

Therefore with upper guard ``x<g`` and no terminal observation boundaries the
exact horizon cut set is

    C_h = {g-t : t in P_h},

and the future quotient on ``Z`` has exactly ``1+|P_h|`` classes.

For a genuinely two-sided action alphabet the canonical P024 group-completion
theorem gives ``M_infinity = d Z`` with ``d=gcd(actions)``.  Hence

    P_infinity = d N_0,
    C_infinity = {g-n d : n>=0}.

All states ``x>=g`` form one disabled class.  Below the guard, future classes
are the uniform gcd cells measured by

    ceil((g-x)/d).

This sharpens the earlier net-zero witness result: total translation is still
too coarse as an *operation-word* quotient, because different zero-net words
can have different peaks, but after the entire guarded word language is
aggregated the induced *state* precision can again collapse to the canonical
gcd grain.

Reachable translations, gcd group completion, prefix maxima and reordering of
commuting integer translations are standard mathematics.  This module is the
P024 guarded-language specialization only.
"""

from __future__ import annotations

from typing import Iterable

from .action_language_precision import (
    reachable_translations,
    signed_group_completion_grain,
    threshold_group_coordinate,
)
from .guarded_translation_precision import guarded_reachable_boundary_cuts


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _normalize_two_sided_actions(actions: Iterable[int]) -> tuple[int, ...]:
    values = tuple(actions)
    if not values:
        raise ValueError("at least one action is required")
    for action in values:
        _require_int("action", action)
    values = tuple(sorted(set(values)))
    if not any(action > 0 for action in values):
        raise ValueError("two-sided action family requires a positive action")
    if not any(action < 0 for action in values):
        raise ValueError("two-sided action family requires a negative action")
    return values


def two_sided_guard_peak_values(
    actions: Iterable[int],
    horizon: int,
) -> tuple[int, ...]:
    """Exact preterminal peak values realized by words through ``horizon``.

    For ``horizon>=1`` this is exactly the nonnegative part of the canonical
    reachable-translation set at horizon ``horizon-1``.
    """
    values = _normalize_two_sided_actions(actions)
    _require_int("horizon", horizon)
    if horizon < 0:
        raise ValueError("horizon must be non-negative")
    if horizon == 0:
        return ()
    return tuple(
        translation
        for translation in reachable_translations(values, horizon - 1)
        if translation >= 0
    )


def two_sided_guard_only_cuts(
    guard: int,
    actions: Iterable[int],
    horizon: int,
) -> tuple[int, ...]:
    """Exact guard-definedness cuts with no terminal observation boundaries."""
    _require_int("guard", guard)
    peaks = two_sided_guard_peak_values(actions, horizon)
    return tuple(sorted(guard - peak for peak in peaks))


def two_sided_guard_only_class_count(
    actions: Iterable[int],
    horizon: int,
) -> int:
    """Exact number of future-definedness classes on ``Z``."""
    return 1 + len(two_sided_guard_peak_values(actions, horizon))


def two_sided_guard_only_compiler_matches_closed_form(
    guard: int,
    actions: Iterable[int],
    horizon: int,
) -> bool:
    """Compare the peak closed form with the generic guarded profile compiler."""
    values = _normalize_two_sided_actions(actions)
    return guarded_reachable_boundary_cuts(
        (),
        values,
        guard,
        horizon,
    ) == two_sided_guard_only_cuts(guard, values, horizon)


def two_sided_guard_only_infinite_coordinate(
    value: int,
    guard: int,
    actions: Iterable[int],
) -> int:
    """Infinite-horizon guard-only class coordinate.

    ``0`` is the common disabled class ``value>=guard``.  Below the guard,
    positive coordinates are the canonical gcd cells.
    """
    _require_int("value", value)
    _require_int("guard", guard)
    values = _normalize_two_sided_actions(actions)
    if value >= guard:
        return 0
    grain = signed_group_completion_grain(values)
    return threshold_group_coordinate(value, guard, grain)


def two_sided_guard_only_infinite_equivalent(
    left: int,
    right: int,
    guard: int,
    actions: Iterable[int],
) -> bool:
    """Whether two states have identical infinite guard-definedness futures."""
    return two_sided_guard_only_infinite_coordinate(
        left, guard, actions
    ) == two_sided_guard_only_infinite_coordinate(
        right, guard, actions
    )
