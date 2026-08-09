"""Finite-horizon continuation-signature complexity for repeated LEGO slots.

For a finite alphabet and a terminal observation on words of fixed length N,
two prefixes of equal depth are continuation-equivalent exactly when every
possible suffix produces the same terminal observation.  The number of such
classes is the minimum number of anonymous finite continuation labels needed at
that depth for the declared terminal task.

This distinguishes two notions of cross-dimensional simplicity:

* bounded class count across N => a uniform finite-type law is possible;
* unbounded class count rules out a fixed finite label set, but does **not** rule
  out a fixed integer-state schema (for example an accumulated integer sum).

No logarithm, entropy, probability, or continuous state is used.
"""

from __future__ import annotations

from itertools import product
from typing import Callable, Hashable

Symbol = Hashable
Observation = Hashable
Word = tuple[Symbol, ...]
TerminalObservation = Callable[[Word], Observation]


def words(alphabet: tuple[Symbol, ...], length: int) -> tuple[Word, ...]:
    if not isinstance(alphabet, tuple) or not alphabet or len(set(alphabet)) != len(alphabet):
        raise ValueError("alphabet must be a non-empty tuple of unique symbols")
    if isinstance(length, bool) or not isinstance(length, int) or length < 0:
        raise ValueError("length must be a non-negative integer")
    return tuple(tuple(items) for items in product(alphabet, repeat=length))


def residual_signature(
    alphabet: tuple[Symbol, ...],
    horizon: int,
    prefix: Word,
    observation: TerminalObservation,
) -> tuple[Observation, ...]:
    """Complete fixed-horizon future signature of one prefix."""
    if isinstance(horizon, bool) or not isinstance(horizon, int) or horizon < 0:
        raise ValueError("horizon must be a non-negative integer")
    if not isinstance(prefix, tuple) or len(prefix) > horizon:
        raise ValueError("prefix must be a tuple no longer than horizon")
    if any(symbol not in alphabet for symbol in prefix):
        raise ValueError("prefix symbols must belong to the alphabet")
    suffix_length = horizon - len(prefix)
    return tuple(
        observation(prefix + suffix)
        for suffix in words(alphabet, suffix_length)
    )


def continuation_classes_at_depth(
    alphabet: tuple[Symbol, ...],
    horizon: int,
    depth: int,
    observation: TerminalObservation,
) -> dict[Word, int]:
    if isinstance(depth, bool) or not isinstance(depth, int) or not (0 <= depth <= horizon):
        raise ValueError("depth must lie between zero and horizon")
    prefixes = words(alphabet, depth)
    signatures = {
        prefix: residual_signature(alphabet, horizon, prefix, observation)
        for prefix in prefixes
    }
    ids: dict[tuple[Observation, ...], int] = {}
    result: dict[Word, int] = {}
    for prefix in prefixes:
        signature = signatures[prefix]
        if signature not in ids:
            ids[signature] = len(ids)
        result[prefix] = ids[signature]
    return result


def continuation_complexity_profile(
    alphabet: tuple[Symbol, ...],
    horizon: int,
    observation: TerminalObservation,
) -> tuple[int, ...]:
    """Number C_(N,d) of residual future classes at each prefix depth d."""
    return tuple(
        len(set(continuation_classes_at_depth(alphabet, horizon, depth, observation).values()))
        for depth in range(horizon + 1)
    )


def finite_type_complexity(
    alphabet: tuple[Symbol, ...],
    horizon: int,
    observation: TerminalObservation,
) -> int:
    """Maximum continuation-class count required over the fixed horizon."""
    return max(continuation_complexity_profile(alphabet, horizon, observation))
