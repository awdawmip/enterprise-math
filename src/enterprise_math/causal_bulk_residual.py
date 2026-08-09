"""Exact bulk/residual structure from a declared causal composition law.

For fixed bulk b, left translation L_b:r -> combine(b,r) partitions reachable
future increments into residual fibers.  Singleton fibers recover an exact
residual; larger fibers are legitimate causal collapse when future evolution
continues through the same associative composition law.

When combine is commutative and a new bulk is causally obtained as
`b'=combine(b,u)`, the residual partition can only coarsen.  Therefore actual
bulk contexts generate canonical quotient maps between residual-resolution
states:

    [r]_b -> [r]_b'.

These maps compose exactly along further accumulation.  Precision/resolution is
therefore derivable as a context-indexed family of causal quotient states rather
than declared a priori.
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
    return {total: tuple(values) for total, values in grouped.items()}


def left_translation_partition(
    bulk: Value,
    increment_values: tuple[Value, ...],
    combine: Combine,
) -> dict[Value, int]:
    fibers = left_translation_fibers(bulk, increment_values, combine)
    result = {}
    for class_id, total in enumerate(sorted(fibers, key=repr)):
        for increment in fibers[total]:
            result[increment] = class_id
    return result


def partition_refines(
    finer: dict[Value, int],
    coarser: dict[Value, int],
) -> bool:
    if set(finer) != set(coarser):
        raise ValueError("partitions must cover the same increment set")
    values = tuple(finer)
    return all(
        finer[left] != finer[right] or coarser[left] == coarser[right]
        for left in values
        for right in values
    )


def residual_resolution_map(
    fine_bulk: Value,
    coarse_bulk: Value,
    increment_values: tuple[Value, ...],
    combine: Combine,
) -> dict[int, int]:
    """Canonical quotient map from residual classes at fine_bulk to coarse_bulk.

    The map exists exactly when the first residual partition refines the second.
    Class ids are local representation labels; the induced mapping itself is
    representative-independent.
    """
    fine = left_translation_partition(fine_bulk, increment_values, combine)
    coarse = left_translation_partition(coarse_bulk, increment_values, combine)
    if not partition_refines(fine, coarse):
        raise ValueError("residual partitions are not ordered by refinement")
    mapping: dict[int, int] = {}
    for increment in increment_values:
        fine_class = fine[increment]
        coarse_class = coarse[increment]
        previous = mapping.get(fine_class)
        if previous is not None and previous != coarse_class:
            raise AssertionError("refinement failed to induce a class map")
        mapping[fine_class] = coarse_class
    return mapping


def compose_class_maps(
    first: dict[int, int],
    second: dict[int, int],
) -> dict[int, int]:
    """Compose finite residual-resolution maps."""
    result = {}
    for source, middle in first.items():
        if middle not in second:
            raise ValueError("second class map must define every reachable middle class")
        result[source] = second[middle]
    return result


def left_translation_collision_spectrum(
    bulk: Value,
    increment_values: tuple[Value, ...],
    combine: Combine,
    maximum_order: int | None = None,
) -> tuple[int, ...]:
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


def bulk_extension_coarsens_residuals(
    bulk: Value,
    absorbed: Value,
    increment_values: tuple[Value, ...],
    combine: Combine,
) -> bool:
    old = left_translation_partition(bulk, increment_values, combine)
    new_bulk = combine(bulk, absorbed)
    new = left_translation_partition(new_bulk, increment_values, combine)
    return partition_refines(old, new)


def collision_spectrum_nondecreasing_under_bulk_extension(
    bulk: Value,
    absorbed: Value,
    increment_values: tuple[Value, ...],
    combine: Combine,
    maximum_order: int | None = None,
) -> bool:
    old = left_translation_collision_spectrum(
        bulk, increment_values, combine, maximum_order
    )
    new = left_translation_collision_spectrum(
        combine(bulk, absorbed), increment_values, combine, maximum_order
    )
    return all(new_value >= old_value for old_value, new_value in zip(old, new))


def bounded_reachable_values(
    alphabet: tuple[Symbol, ...],
    maximum_length: int,
    observation: Observation,
) -> tuple[Value, ...]:
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
    for bulk in bulk_values:
        outputs = [combine(bulk, increment) for increment in increment_values]
        if len(set(outputs)) != len(outputs):
            return False
    return True
