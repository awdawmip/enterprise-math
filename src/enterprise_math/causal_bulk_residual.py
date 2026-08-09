"""Exact bulk/residual separation from a declared causal composition law.

Integer subtraction is only one special way to remove already-settled bulk from
a future observation.  The more primitive question is whether a declared bulk
composition law

    combine(bulk, increment) -> total

admits a unique reachable increment for the observed `(bulk,total)` pair.  Only
then is an identity-free residual state well-defined.

If the observation itself respects word composition,

    O(p+s) = combine(O(p), O(s)),

and left translation by every reachable bulk value is injective, then the exact
future residual of prefix p is simply O(s), independent of p.  Traditional
left-cancellative monoid language is a shadow of this causal unique-recovery
condition, not a primitive assumption.
"""

from __future__ import annotations

from itertools import product
from typing import Callable, Hashable, Iterable

Symbol = Hashable
Word = tuple[Symbol, ...]
Value = Hashable
Observation = Callable[[Word], Value]
Combine = Callable[[Value, Value], Value]


def words(alphabet: tuple[Symbol, ...], length: int) -> tuple[Word, ...]:
    if not isinstance(alphabet, tuple) or not alphabet or len(set(alphabet)) != len(alphabet):
        raise ValueError("alphabet must be a non-empty tuple of unique symbols")
    if isinstance(length, bool) or not isinstance(length, int) or length < 0:
        raise ValueError("length must be a non-negative integer")
    return tuple(tuple(items) for items in product(alphabet, repeat=length))


def unique_residual(
    bulk: Value,
    total: Value,
    candidate_increments: Iterable[Value],
    combine: Combine,
) -> Value:
    """Return the unique increment r with combine(bulk,r)==total.

    Raises when the declared bulk law cannot explain the total, or when several
    reachable increments are observationally indistinguishable after combining
    with the same bulk.  In the latter case exact bulk/structure separation has
    not been causally justified.
    """
    matches = []
    seen = set()
    for increment in candidate_increments:
        try:
            hash(increment)
        except TypeError as error:
            raise ValueError("candidate increments must be hashable") from error
        if increment in seen:
            continue
        seen.add(increment)
        if combine(bulk, increment) == total:
            matches.append(increment)
    if not matches:
        raise ValueError("no reachable residual reconstructs the total from the bulk")
    if len(matches) != 1:
        raise ValueError("bulk law does not uniquely determine a future residual")
    return matches[0]


def bounded_reachable_values(
    alphabet: tuple[Symbol, ...],
    maximum_length: int,
    observation: Observation,
) -> tuple[Value, ...]:
    """All distinct observation values reachable by suffixes up to a finite length."""
    if (
        isinstance(maximum_length, bool)
        or not isinstance(maximum_length, int)
        or maximum_length < 0
    ):
        raise ValueError("maximum_length must be a non-negative integer")
    result = []
    seen = set()
    for length in range(maximum_length + 1):
        for word in words(alphabet, length):
            value = observation(word)
            try:
                hash(value)
            except TypeError as error:
                raise ValueError("observation values must be hashable") from error
            if value not in seen:
                seen.add(value)
                result.append(value)
    return tuple(result)


def residual_signature_under_bulk_law(
    alphabet: tuple[Symbol, ...],
    prefix: Word,
    maximum_suffix_length: int,
    observation: Observation,
    combine: Combine,
) -> tuple[tuple[Value, ...], ...]:
    """Exact residual signature recovered through a declared bulk composition law."""
    if not isinstance(prefix, tuple) or any(symbol not in alphabet for symbol in prefix):
        raise ValueError("prefix symbols must belong to alphabet")
    candidates = bounded_reachable_values(alphabet, maximum_suffix_length, observation)
    bulk = observation(prefix)
    return tuple(
        tuple(
            unique_residual(
                bulk,
                observation(prefix + suffix),
                candidates,
                combine,
            )
            for suffix in words(alphabet, suffix_length)
        )
        for suffix_length in range(maximum_suffix_length + 1)
    )


def bounded_homomorphism_check(
    alphabet: tuple[Symbol, ...],
    maximum_left_length: int,
    maximum_right_length: int,
    observation: Observation,
    combine: Combine,
) -> bool:
    """Finite pressure test of O(p+s)==combine(O(p),O(s))."""
    for left_length in range(maximum_left_length + 1):
        for right_length in range(maximum_right_length + 1):
            for left in words(alphabet, left_length):
                for right in words(alphabet, right_length):
                    if observation(left + right) != combine(observation(left), observation(right)):
                        return False
    return True


def bounded_left_recovery_is_unique(
    bulk_values: tuple[Value, ...],
    increment_values: tuple[Value, ...],
    combine: Combine,
) -> bool:
    """Whether each reachable bulk has injective left translation on tested increments."""
    for bulk in bulk_values:
        outputs = [combine(bulk, increment) for increment in increment_values]
        if len(set(outputs)) != len(outputs):
            return False
    return True
