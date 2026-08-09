"""Exact bulk/residual structure from a declared causal composition law.

Integer subtraction is only one special way to remove already-settled bulk from
a future observation.  The primitive object is a declared causal composition
law

    combine(bulk, increment) -> total.

For fixed bulk b, left translation L_b:r -> combine(b,r) partitions reachable
future increments into fibers.  A singleton fiber gives a uniquely recoverable
residual.  A larger fiber is not automatically a defect: if future evolution
continues through the same associative composition law, every increment in that
fiber has already become causally indistinguishable after combining with b.
Thus non-cancellativity is itself a causal collapse whose P011-style collision
spectrum measures which future increments the current bulk has swallowed.

If the observation respects word composition,

    O(p+s) = combine(O(p), O(s)),

then a left-cancellative reachable regime is the special case where all these
residual fibers are singletons and the future residual is exactly O(s).
Traditional cancellation/quotient language is therefore a shadow of fiber
structure, not a primitive requirement.
"""

from __future__ import annotations

from collections import defaultdict
from itertools import product
from math import comb
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


def residual_candidates(
    bulk: Value,
    total: Value,
    candidate_increments: Iterable[Value],
    combine: Combine,
) -> tuple[Value, ...]:
    """All distinct reachable increments r with combine(bulk,r)==total."""
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
    return tuple(matches)


def unique_residual(
    bulk: Value,
    total: Value,
    candidate_increments: Iterable[Value],
    combine: Combine,
) -> Value:
    """Return the unique reachable residual, raising on empty or non-singleton fiber."""
    matches = residual_candidates(bulk, total, candidate_increments, combine)
    if not matches:
        raise ValueError("no reachable residual reconstructs the total from the bulk")
    if len(matches) != 1:
        raise ValueError("bulk law does not uniquely determine a future residual")
    return matches[0]


def left_translation_fibers(
    bulk: Value,
    increment_values: tuple[Value, ...],
    combine: Combine,
) -> dict[Value, tuple[Value, ...]]:
    """Fibers of r -> combine(bulk,r) on declared reachable increments."""
    if not isinstance(increment_values, tuple) or not increment_values:
        raise ValueError("increment_values must be a non-empty tuple")
    grouped: dict[Value, list[Value]] = defaultdict(list)
    seen = set()
    for increment in increment_values:
        try:
            hash(increment)
        except TypeError as error:
            raise ValueError("increment values must be hashable") from error
        if increment in seen:
            raise ValueError("increment_values must be unique")
        seen.add(increment)
        total = combine(bulk, increment)
        try:
            hash(total)
        except TypeError as error:
            raise ValueError("combined totals must be hashable") from error
        grouped[total].append(increment)
    return {
        total: tuple(values)
        for total, values in grouped.items()
    }


def left_translation_collision_spectrum(
    bulk: Value,
    increment_values: tuple[Value, ...],
    combine: Combine,
    maximum_order: int | None = None,
) -> tuple[int, ...]:
    """P011-style collision spectrum of the bulk left-translation collapse."""
    fibers = left_translation_fibers(bulk, increment_values, combine)
    total = len(increment_values)
    limit = total if maximum_order is None else maximum_order
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 0:
        raise ValueError("maximum_order must be a non-negative integer")
    sizes = tuple(len(values) for values in fibers.values())
    return tuple(
        sum(comb(size, order) for size in sizes if size >= order)
        for order in range(limit + 1)
    )


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
    """Unique-residual specialization of a declared bulk composition law."""
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


def bounded_associativity_check(
    values: tuple[Value, ...],
    combine: Combine,
) -> bool:
    """Finite pressure test of combine(combine(a,b),c)==combine(a,combine(b,c))."""
    for first in values:
        for second in values:
            for third in values:
                if combine(combine(first, second), third) != combine(
                    first, combine(second, third)
                ):
                    return False
    return True


def same_bulk_fiber_is_future_safe_under_associative_extension(
    bulk: Value,
    left_increment: Value,
    right_increment: Value,
    future_increments: tuple[Value, ...],
    combine: Combine,
) -> bool:
    """Check the causal consequence of associativity for two collided residuals.

    If both residuals produce the same current total after the bulk, then every
    later right-composition by the same future increment must also agree under an
    associative combine law.  This function checks the finite declared future set.
    """
    left_total = combine(bulk, left_increment)
    right_total = combine(bulk, right_increment)
    if left_total != right_total:
        return False
    return all(
        combine(left_total, future) == combine(right_total, future)
        for future in future_increments
    )


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
