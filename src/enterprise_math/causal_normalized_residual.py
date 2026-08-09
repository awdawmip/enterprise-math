"""Normalized future signatures separate carried integer bulk from structure.

For an integer-valued observation O on finite LEGO words, the raw residual
signature of a prefix p is the function s -> O(p+s).  Distinct prefixes may have
different raw signatures only because they already carry different settled bulk
values.  Remove that value by

    Rhat_p(s) = O(p+s) - O(p).

Prefixes with the same normalized residual have the same *structural* response
to every future suffix.  Runtime state may then be represented as

    (current_bulk_value, structural_continuation_type)

rather than treating every different bulk value as a new relation type.

This is exact integer factorization, not approximation.  It is especially useful
for additive totals and finite-range accumulated grades.  It does not apply to
arbitrary non-integer/non-translation observations without an explicit output
composition law.
"""

from __future__ import annotations

from itertools import product
from typing import Callable, Hashable

Symbol = Hashable
Word = tuple[Symbol, ...]
IntegerObservation = Callable[[Word], int]


def words(alphabet: tuple[Symbol, ...], length: int) -> tuple[Word, ...]:
    if not isinstance(alphabet, tuple) or not alphabet or len(set(alphabet)) != len(alphabet):
        raise ValueError("alphabet must be a non-empty tuple of unique symbols")
    if isinstance(length, bool) or not isinstance(length, int) or length < 0:
        raise ValueError("length must be a non-negative integer")
    return tuple(tuple(items) for items in product(alphabet, repeat=length))


def _integer_observation(observation: IntegerObservation, word: Word) -> int:
    value = observation(word)
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError("observation must return integers")
    return value


def normalized_residual_signature(
    alphabet: tuple[Symbol, ...],
    prefix: Word,
    maximum_suffix_length: int,
    observation: IntegerObservation,
) -> tuple[tuple[int, ...], ...]:
    """Bounded exact samples of s -> O(prefix+s)-O(prefix), grouped by suffix length."""
    if isinstance(maximum_suffix_length, bool) or not isinstance(maximum_suffix_length, int) or maximum_suffix_length < 0:
        raise ValueError("maximum_suffix_length must be a non-negative integer")
    if not isinstance(prefix, tuple) or any(symbol not in alphabet for symbol in prefix):
        raise ValueError("prefix symbols must belong to alphabet")
    base = _integer_observation(observation, prefix)
    return tuple(
        tuple(
            _integer_observation(observation, prefix + suffix) - base
            for suffix in words(alphabet, suffix_length)
        )
        for suffix_length in range(maximum_suffix_length + 1)
    )


def structural_classes(
    alphabet: tuple[Symbol, ...],
    prefixes: tuple[Word, ...],
    maximum_suffix_length: int,
    observation: IntegerObservation,
) -> dict[Word, int]:
    signatures = {
        prefix: normalized_residual_signature(
            alphabet, prefix, maximum_suffix_length, observation
        )
        for prefix in prefixes
    }
    ids: dict[tuple[tuple[int, ...], ...], int] = {}
    result: dict[Word, int] = {}
    for prefix in sorted(prefixes, key=repr):
        signature = signatures[prefix]
        if signature not in ids:
            ids[signature] = len(ids)
        result[prefix] = ids[signature]
    return result


def structural_class_count(
    alphabet: tuple[Symbol, ...],
    prefixes: tuple[Word, ...],
    maximum_suffix_length: int,
    observation: IntegerObservation,
) -> int:
    return len(
        set(
            structural_classes(
                alphabet, prefixes, maximum_suffix_length, observation
            ).values()
        )
    )


def reconstruct_future_value(
    current_bulk: int,
    normalized_future_increment: int,
) -> int:
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for value in (current_bulk, normalized_future_increment)
    ):
        raise ValueError("values must be integers")
    return current_bulk + normalized_future_increment
