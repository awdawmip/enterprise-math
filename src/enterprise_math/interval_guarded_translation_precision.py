"""Exact prefix-envelope precision for interval-guarded integer translations.

Actions translate ``x -> x+a`` and are legal only while the current state before
each action lies in one declared half-open interval

    lower <= x < upper.

For a nonempty word with prefix sums ``s_j`` before the terminal update, define

    T = final total translation,
    L = min {s_j : 0 <= j < m},
    H = max {s_j : 0 <= j < m}.

Then the word is legal exactly on

    lower - L <= x < upper - H,

and, when legal, ends at ``x+T``.  Thus ``(T,L,H)`` is an exact word quotient for
all interval-legality and ordered-threshold terminal observations.

The profile composes without literal history.  For two nonempty profiles:

    T(uv) = T(u)+T(v),
    L(uv) = min(L(u), T(u)+L(v)),
    H(uv) = max(H(u), T(u)+H(v)).

Appending one action uses the old final total as the new preterminal prefix.
For action magnitude ``M`` and horizon ``h>=1``, distinct profiles are bounded by

    1 + (2hM+1) ((h-1)M+1)^2,

cubic in horizon for fixed alphabet rather than exponential in word count.

For a nonempty profile, put

    A = lower-L,
    G = upper-H.

If ``A>=G`` the word is nowhere legal.  Otherwise its outcome can change only at
the two domain breakpoints ``A,G`` and at shifted observation boundaries ``b-T``
strictly inside ``(A,G)``.  The empty word is always legal and contributes only
current observation boundaries.

Crucial negative boundary: unlike the one-sided upper-guard case, the union of
these breakpoints is generally *not* itself the exact future quotient.  States
on opposite sides of a bounded legal interval can both have the same
``UNDEFINED`` behavior and therefore belong to one disconnected future fiber.
The breakpoint arrangement is a finite refinement on which the future signature
is locally constant; the exact quotient is equality of the compiled profile
signatures and may merge nonadjacent arrangement cells.

Generic interval automata/prefix envelopes are prior art.  This is the P024
integer specialization extending the one-sided guarded profile of PR #310 and
recording the exact convexity failure at two-sided action domains.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .action_language_precision import ordered_threshold_observation


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _require_nonnegative(name: str, value: int) -> None:
    _require_int(name, value)
    if value < 0:
        raise ValueError(f"{name} must be non-negative")


def _actions(actions: Iterable[int]) -> tuple[int, ...]:
    values = tuple(actions)
    if not values:
        raise ValueError("at least one action is required")
    for action in values:
        _require_int("action", action)
    return tuple(sorted(set(values)))


def _boundaries(boundaries: Iterable[int]) -> tuple[int, ...]:
    values = tuple(boundaries)
    for boundary in values:
        _require_int("boundary", boundary)
    return tuple(sorted(set(values)))


def _guard(lower: int, upper: int) -> None:
    _require_int("lower", lower)
    _require_int("upper", upper)
    if lower >= upper:
        raise ValueError("guard interval must satisfy lower < upper")


@dataclass(frozen=True)
class IntervalGuardedProfile:
    total_translation: int
    preterminal_minimum: int | None
    preterminal_maximum: int | None

    @property
    def is_empty(self) -> bool:
        return self.preterminal_minimum is None


def _validate_profile(profile: IntervalGuardedProfile) -> None:
    if not isinstance(profile, IntervalGuardedProfile):
        raise TypeError("profile must be IntervalGuardedProfile")
    _require_int("total_translation", profile.total_translation)
    if profile.is_empty:
        if profile.total_translation != 0 or profile.preterminal_maximum is not None:
            raise ValueError("empty interval profile must be (0,None,None)")
        return
    if profile.preterminal_maximum is None:
        raise ValueError("nonempty interval profile requires both envelope bounds")
    _require_int("preterminal_minimum", profile.preterminal_minimum)
    _require_int("preterminal_maximum", profile.preterminal_maximum)
    if profile.preterminal_minimum > 0 or profile.preterminal_maximum < 0:
        raise ValueError("preterminal envelope must contain the zero prefix")
    if profile.preterminal_minimum > profile.preterminal_maximum:
        raise ValueError("preterminal minimum must not exceed maximum")


def empty_interval_guarded_profile() -> IntervalGuardedProfile:
    return IntervalGuardedProfile(0, None, None)


def interval_guarded_word_profile(word: Iterable[int]) -> IntervalGuardedProfile:
    values = tuple(word)
    for action in values:
        _require_int("action", action)
    if not values:
        return empty_interval_guarded_profile()
    total = 0
    low = 0
    high = 0
    for action in values:
        low = min(low, total)
        high = max(high, total)
        total += action
    return IntervalGuardedProfile(total, low, high)


def append_interval_guarded_action(
    profile: IntervalGuardedProfile,
    action: int,
) -> IntervalGuardedProfile:
    _validate_profile(profile)
    _require_int("action", action)
    if profile.is_empty:
        return IntervalGuardedProfile(action, 0, 0)
    assert profile.preterminal_minimum is not None
    assert profile.preterminal_maximum is not None
    return IntervalGuardedProfile(
        profile.total_translation + action,
        min(profile.preterminal_minimum, profile.total_translation),
        max(profile.preterminal_maximum, profile.total_translation),
    )


def compose_interval_guarded_profiles(
    left: IntervalGuardedProfile,
    right: IntervalGuardedProfile,
) -> IntervalGuardedProfile:
    _validate_profile(left)
    _validate_profile(right)
    if left.is_empty:
        return right
    if right.is_empty:
        return left
    assert left.preterminal_minimum is not None
    assert left.preterminal_maximum is not None
    assert right.preterminal_minimum is not None
    assert right.preterminal_maximum is not None
    return IntervalGuardedProfile(
        left.total_translation + right.total_translation,
        min(
            left.preterminal_minimum,
            left.total_translation + right.preterminal_minimum,
        ),
        max(
            left.preterminal_maximum,
            left.total_translation + right.preterminal_maximum,
        ),
    )


def _profile_sort_key(profile: IntervalGuardedProfile) -> tuple[int, int, int, int]:
    return (
        0 if profile.is_empty else 1,
        profile.total_translation,
        0 if profile.preterminal_minimum is None else profile.preterminal_minimum,
        0 if profile.preterminal_maximum is None else profile.preterminal_maximum,
    )


def interval_guarded_profiles(
    actions: Iterable[int],
    horizon: int,
) -> tuple[IntervalGuardedProfile, ...]:
    values = _actions(actions)
    _require_nonnegative("horizon", horizon)
    empty = empty_interval_guarded_profile()
    reached = {empty}
    frontier = {empty}
    for _ in range(horizon):
        frontier = {
            append_interval_guarded_action(profile, action)
            for profile in frontier
            for action in values
        }
        reached.update(frontier)
    return tuple(sorted(reached, key=_profile_sort_key))


def interval_guarded_profile_count_upper_bound(
    actions: Iterable[int],
    horizon: int,
) -> int:
    values = _actions(actions)
    _require_nonnegative("horizon", horizon)
    if horizon == 0:
        return 1
    amplitude = max(abs(action) for action in values)
    envelope_count = (horizon - 1) * amplitude + 1
    return 1 + (2 * horizon * amplitude + 1) * envelope_count * envelope_count


def interval_guarded_domain(
    profile: IntervalGuardedProfile,
    lower: int,
    upper: int,
) -> tuple[int, int] | None:
    """Return integer half-open domain ``[A,G)`` or ``None`` if nowhere legal.

    The empty word is globally defined and therefore has no action-domain
    interval; it is represented by ``None`` here only to distinguish it from a
    nonempty bounded domain.
    """
    _validate_profile(profile)
    _guard(lower, upper)
    if profile.is_empty:
        return None
    assert profile.preterminal_minimum is not None
    assert profile.preterminal_maximum is not None
    start = lower - profile.preterminal_minimum
    stop = upper - profile.preterminal_maximum
    if start >= stop:
        return None
    return start, stop


@dataclass(frozen=True)
class IntervalGuardedOutcome:
    defined: bool
    final_value: int | None
    observation: int | None


def apply_interval_guarded_word(
    value: int,
    word: Iterable[int],
    lower: int,
    upper: int,
    boundaries: Iterable[int] = (),
) -> IntervalGuardedOutcome:
    _require_int("value", value)
    _guard(lower, upper)
    cuts = _boundaries(boundaries)
    current = value
    for action in tuple(word):
        _require_int("action", action)
        if not lower <= current < upper:
            return IntervalGuardedOutcome(False, None, None)
        current += action
    return IntervalGuardedOutcome(
        True,
        current,
        ordered_threshold_observation(current, cuts),
    )


def apply_interval_guarded_profile(
    value: int,
    profile: IntervalGuardedProfile,
    lower: int,
    upper: int,
    boundaries: Iterable[int] = (),
) -> IntervalGuardedOutcome:
    _require_int("value", value)
    _validate_profile(profile)
    _guard(lower, upper)
    cuts = _boundaries(boundaries)
    if not profile.is_empty:
        domain = interval_guarded_domain(profile, lower, upper)
        if domain is None or not domain[0] <= value < domain[1]:
            return IntervalGuardedOutcome(False, None, None)
    final = value + profile.total_translation
    return IntervalGuardedOutcome(
        True,
        final,
        ordered_threshold_observation(final, cuts),
    )


def interval_guarded_profile_breakpoints(
    profile: IntervalGuardedProfile,
    boundaries: Iterable[int],
    lower: int,
    upper: int,
) -> tuple[int, ...]:
    """Points where one compiled profile outcome can change.

    These breakpoints make the profile outcome locally constant on each
    arrangement cell.  They do not imply that distinct cells have distinct
    outcomes: the two exterior cells of a bounded legal interval can both be
    ``UNDEFINED``.
    """
    _validate_profile(profile)
    _guard(lower, upper)
    cuts = _boundaries(boundaries)
    if profile.is_empty:
        return cuts
    domain = interval_guarded_domain(profile, lower, upper)
    if domain is None:
        return ()
    start, stop = domain
    result = {start, stop}
    for boundary in cuts:
        shifted = boundary - profile.total_translation
        if start < shifted < stop:
            result.add(shifted)
    return tuple(sorted(result))


def interval_guarded_reachable_breakpoints(
    boundaries: Iterable[int],
    actions: Iterable[int],
    lower: int,
    upper: int,
    horizon: int,
) -> tuple[int, ...]:
    """Finite arrangement on which the complete horizon signature is locally constant."""
    cuts = _boundaries(boundaries)
    values = _actions(actions)
    _guard(lower, upper)
    _require_nonnegative("horizon", horizon)
    result: set[int] = set()
    for profile in interval_guarded_profiles(values, horizon):
        result.update(
            interval_guarded_profile_breakpoints(
                profile, cuts, lower, upper
            )
        )
    return tuple(sorted(result))


def interval_guarded_future_signature(
    value: int,
    boundaries: Iterable[int],
    actions: Iterable[int],
    lower: int,
    upper: int,
    horizon: int,
) -> tuple[tuple[IntervalGuardedProfile, bool, int | None], ...]:
    """Exact legality-sensitive future signature after word-profile compilation."""
    _require_int("value", value)
    cuts = _boundaries(boundaries)
    values = _actions(actions)
    _guard(lower, upper)
    _require_nonnegative("horizon", horizon)
    result = []
    for profile in interval_guarded_profiles(values, horizon):
        outcome = apply_interval_guarded_profile(
            value, profile, lower, upper, cuts
        )
        result.append((profile, outcome.defined, outcome.observation))
    return tuple(result)


def interval_guarded_future_equivalent(
    left: int,
    right: int,
    boundaries: Iterable[int],
    actions: Iterable[int],
    lower: int,
    upper: int,
    horizon: int,
) -> bool:
    """Exact future equivalence; fibers may be disconnected subsets of ``Z``."""
    _require_int("left", left)
    _require_int("right", right)
    return interval_guarded_future_signature(
        left, boundaries, actions, lower, upper, horizon
    ) == interval_guarded_future_signature(
        right, boundaries, actions, lower, upper, horizon
    )


def interval_guarded_breakpoint_cell_equivalent(
    left: int,
    right: int,
    boundaries: Iterable[int],
    actions: Iterable[int],
    lower: int,
    upper: int,
    horizon: int,
) -> bool:
    """Whether two states lie in one cell of the finite breakpoint arrangement.

    Same arrangement cell always implies future equivalence.  The converse can
    fail because different cells may carry the same legality/observation
    signature.
    """
    _require_int("left", left)
    _require_int("right", right)
    if left == right:
        return True
    lo, hi = sorted((left, right))
    breakpoints = interval_guarded_reachable_breakpoints(
        boundaries, actions, lower, upper, horizon
    )
    return not any(lo < cut <= hi for cut in breakpoints)
