"""Finite-horizon continuation-signature complexity for repeated LEGO slots.

For a finite alphabet and a terminal observation on words of fixed length N,
two prefixes of equal depth are continuation-equivalent exactly when every
possible suffix produces the same terminal observation.  The number of such
classes is the minimum number of anonymous finite continuation labels needed at
that depth for the declared terminal task.

A prefix-to-continuation-class map is itself a finite causal collapse.  Hence its
fiber multiplicities and P011-style collision spectrum quantify exactly how many
distinct pasts may be forgotten without changing any declared future response.

Bounded continuation-class count is a strong finite-type uniformity criterion.
Unbounded count rules out a fixed finite label set, although a syntactically
fixed integer update schema may still exist; such an encoding does not erase the
representation-independent class-count capacity.
"""

from __future__ import annotations

from collections import Counter
from itertools import product
from math import comb
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


def continuation_fiber_sizes(
    alphabet: tuple[Symbol, ...],
    horizon: int,
    depth: int,
    observation: TerminalObservation,
) -> tuple[int, ...]:
    """Sorted multiplicities of past prefixes per future continuation class."""
    classes = continuation_classes_at_depth(alphabet, horizon, depth, observation)
    counts = Counter(classes.values())
    return tuple(sorted(counts.values(), reverse=True))


def future_distinction_loss(
    alphabet: tuple[Symbol, ...],
    horizon: int,
    depth: int,
    observation: TerminalObservation,
) -> int:
    """First-order class-loss count |prefixes|-|continuation classes|."""
    classes = continuation_classes_at_depth(alphabet, horizon, depth, observation)
    return len(classes) - len(set(classes.values()))


def future_collapse_spectrum(
    alphabet: tuple[Symbol, ...],
    horizon: int,
    depth: int,
    observation: TerminalObservation,
    maximum_order: int | None = None,
) -> tuple[int, ...]:
    """P011-style J_k spectrum of the prefix -> continuation-type collapse.

    J_k counts k-subsets of distinct past prefixes that are already identical
    for every declared remaining future observation.
    """
    sizes = continuation_fiber_sizes(alphabet, horizon, depth, observation)
    total = sum(sizes)
    limit = total if maximum_order is None else maximum_order
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 0:
        raise ValueError("maximum_order must be a non-negative integer")
    return tuple(
        sum(comb(size, order) for size in sizes if size >= order)
        for order in range(limit + 1)
    )
