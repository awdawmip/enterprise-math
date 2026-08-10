"""Two-sided guarded actions retain future information inside net-zero words.

Canonical P024 total integer translations depend on an action word only through
its cumulative translation, and a genuinely two-sided action family completes
to its gcd subgroup.  A state-dependent guard changes that conclusion because
word legality depends on prefix height, not only on the final total.

Take one positive action ``p>0`` and one negative action ``-q<0``.  Put

    L = lcm(p,q).

For every multiplier ``N>=1`` consider the block word consisting of

    N*L/p copies of +p,
    followed by N*L/q copies of -q.

Its net translation is exactly zero, but its preterminal prefix peak is exactly
``N*L``.  Under the common upper guard ``x<g`` the word is therefore legal
exactly for

    x < g - N*L.

Hence the algebraic identity translation class contains infinitely many words
with pairwise different legal domains.  At horizon ``h`` a chosen positive /
negative pair with block length

    c = L/p + L/q

already gives at least ``1 + floor(h/c)`` distinct guarded profiles in the
net-zero class when the empty word is included.  This is a lower bound; other
words may split the identity class further.

The unit signed alphabet ``{-1,+1}`` gives an exact model.  With no terminal
observation boundaries, words of length at most ``h>=1`` produce exactly the
legality cuts

    g, g-1, ..., g-h+1.

Thus the horizon-``h`` future quotient has exactly ``h+1`` classes on ``Z``.
As ``h -> infinity``, every integer state below the guard becomes a singleton
future class, while all states ``x>=g`` remain one common disabled class.  The
declared operation language alone therefore recovers exact state below the
guard even when terminal observation is constant.

This is the sharp boundary to the positive guarded-semigroup reduction: under
genuinely two-sided guarded actions, total-translation group completion can
hide an unbounded prefix-legality hierarchy inside its own kernel.

Zero-sum words, lcm balancing, lattice paths and prefix maxima are standard
prior mathematics.  The Enterprise Math result is the P024 state-dependent
precision interpretation and exact finite/infinite boundary statement.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import lcm
from typing import Iterable

from .guarded_translation_precision import (
    GuardedTranslationProfile,
    guarded_reachable_boundary_cuts,
)


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _require_positive(name: str, value: int) -> None:
    _require_int(name, value)
    if value <= 0:
        raise ValueError(f"{name} must be positive")


def _two_sided_actions(actions: Iterable[int]) -> tuple[int, ...]:
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


@dataclass(frozen=True)
class ZeroTranslationGuardWitness:
    positive_action: int
    negative_action: int
    balance_lcm: int
    multiplier: int
    positive_count: int
    negative_count: int
    word_length: int
    profile: GuardedTranslationProfile

    @property
    def guard_peak(self) -> int:
        assert self.profile.preterminal_peak is not None
        return self.profile.preterminal_peak


def zero_translation_block_witness(
    positive_action: int,
    negative_action: int,
    multiplier: int = 1,
) -> ZeroTranslationGuardWitness:
    """Construct the exact net-zero positive-block/negative-block profile."""
    _require_positive("positive_action", positive_action)
    _require_int("negative_action", negative_action)
    if negative_action >= 0:
        raise ValueError("negative_action must be negative")
    _require_positive("multiplier", multiplier)

    negative_magnitude = -negative_action
    balance = lcm(positive_action, negative_magnitude)
    positive_count = multiplier * (balance // positive_action)
    negative_count = multiplier * (balance // negative_magnitude)
    peak = multiplier * balance
    return ZeroTranslationGuardWitness(
        positive_action=positive_action,
        negative_action=negative_action,
        balance_lcm=balance,
        multiplier=multiplier,
        positive_count=positive_count,
        negative_count=negative_count,
        word_length=positive_count + negative_count,
        profile=GuardedTranslationProfile(0, peak),
    )


def shortest_balanced_pair_cost(actions: Iterable[int]) -> tuple[int, int, int]:
    """Return ``(word_length_per_multiplier, p, n)`` for the cheapest sign pair."""
    values = _two_sided_actions(actions)
    candidates = []
    for positive in values:
        if positive <= 0:
            continue
        for negative in values:
            if negative >= 0:
                continue
            witness = zero_translation_block_witness(positive, negative)
            candidates.append((witness.word_length, positive, negative))
    return min(candidates)


def zero_translation_profile_lower_bound(
    actions: Iterable[int],
    horizon: int,
) -> int:
    """Guaranteed number of distinct profiles inside net translation zero.

    Includes the empty word.  The best two-sign block construction gives one
    new peak for every full balanced block length that fits inside ``horizon``.
    """
    values = _two_sided_actions(actions)
    _require_int("horizon", horizon)
    if horizon < 0:
        raise ValueError("horizon must be non-negative")
    cycle_length, _, _ = shortest_balanced_pair_cost(values)
    return 1 + horizon // cycle_length


def zero_translation_witness_guard_cut(
    witness: ZeroTranslationGuardWitness,
    guard: int,
) -> int:
    _require_int("guard", guard)
    return guard - witness.guard_peak


def unit_signed_legality_cuts(guard: int, horizon: int) -> tuple[int, ...]:
    """Exact no-observation cuts for action alphabet ``{-1,+1}``."""
    _require_int("guard", guard)
    _require_int("horizon", horizon)
    if horizon < 0:
        raise ValueError("horizon must be non-negative")
    if horizon == 0:
        return ()
    return tuple(range(guard - horizon + 1, guard + 1))


def unit_signed_legality_class_count(horizon: int) -> int:
    """Exact class count on ``Z`` with constant terminal observation."""
    _require_int("horizon", horizon)
    if horizon < 0:
        raise ValueError("horizon must be non-negative")
    return horizon + 1


def unit_signed_infinite_future_equivalent(
    left: int,
    right: int,
    guard: int,
) -> bool:
    """Infinite-horizon equivalence for ``{-1,+1}`` with no terminal cuts."""
    _require_int("left", left)
    _require_int("right", right)
    _require_int("guard", guard)
    if left >= guard and right >= guard:
        return True
    return left == right


def unit_signed_general_compiler_matches_closed_form(
    guard: int,
    horizon: int,
) -> bool:
    """Check the exact closed cuts against the general guarded compiler."""
    return guarded_reachable_boundary_cuts(
        (), (-1, 1), guard, horizon
    ) == unit_signed_legality_cuts(guard, horizon)
