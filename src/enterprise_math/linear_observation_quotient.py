"""Observation-aware exact partition synthesis for P019 integer dynamics.

A linear observable lambda(c)=w^T c factors through a coordinate partition A
iff its coefficients are constant inside every partition block.  Combining
those required observation splits with the linear-dynamics refinement yields
the coarsest refinement of an initial partition that preserves every declared
linear score and every declared integer linear/affine dynamics exactly.
"""

from __future__ import annotations

from .linear_relation_quotient import (
    Matrix,
    Partition,
    linear_family_descends,
    refine_partition_for_linear_family,
)


Observable = tuple[int, ...]


def _require_observables(size: int, observables: tuple[Observable, ...]) -> None:
    if not isinstance(observables, tuple):
        raise ValueError("observables must be a tuple")
    for observable in observables:
        if not isinstance(observable, tuple) or len(observable) != size:
            raise ValueError("every observable must have one coefficient per fine coordinate")
        if any(
            isinstance(value, bool) or not isinstance(value, int)
            for value in observable
        ):
            raise ValueError("observable coefficients must be integers")


def _require_partition(size: int, partition: Partition) -> None:
    if not isinstance(partition, tuple) or not partition:
        raise ValueError("partition must be non-empty")
    flattened = [index for group in partition for index in group]
    if any(not isinstance(group, tuple) or not group for group in partition):
        raise ValueError("partition groups must be non-empty tuples")
    if any(
        isinstance(index, bool)
        or not isinstance(index, int)
        or index < 0
        or index >= size
        for index in flattened
    ):
        raise ValueError("partition index out of range")
    if sorted(flattened) != list(range(size)):
        raise ValueError("partition must cover every coordinate exactly once")


def descended_linear_observable(
    observable: Observable, partition: Partition
) -> tuple[int, ...]:
    """Return coarse coefficients wbar with w^T=wbar^T A, or raise."""
    size = len(observable)
    _require_observables(size, (observable,))
    _require_partition(size, partition)
    coarse = []
    for group in partition:
        coefficient = observable[group[0]]
        if any(observable[index] != coefficient for index in group[1:]):
            raise ValueError("observable reads distinctions erased by the partition")
        coarse.append(coefficient)
    return tuple(coarse)


def linear_observable_descends(
    observable: Observable, partition: Partition
) -> bool:
    """Whether one exact integer linear score factors through the partition."""
    try:
        descended_linear_observable(observable, partition)
    except ValueError as error:
        if str(error) == "observable reads distinctions erased by the partition":
            return False
        raise
    return True


def observation_family_descends(
    observables: tuple[Observable, ...], partition: Partition
) -> bool:
    """Whether every declared exact linear score is quotient-readable."""
    if not observables:
        return True
    size = len(observables[0])
    _require_observables(size, observables)
    _require_partition(size, partition)
    return all(linear_observable_descends(observable, partition) for observable in observables)


def refine_partition_for_linear_observations(
    observables: tuple[Observable, ...], initial_partition: Partition
) -> Partition:
    """Coarsest refinement of initial_partition preserving all exact linear scores."""
    if not initial_partition:
        raise ValueError("initial_partition must be non-empty")
    size = sum(len(group) for group in initial_partition)
    _require_partition(size, initial_partition)
    _require_observables(size, observables)
    if not observables:
        return initial_partition

    refined = []
    for group in initial_partition:
        buckets: dict[tuple[int, ...], list[int]] = {}
        order: list[tuple[int, ...]] = []
        for coordinate in group:
            signature = tuple(observable[coordinate] for observable in observables)
            if signature not in buckets:
                buckets[signature] = []
                order.append(signature)
            buckets[signature].append(coordinate)
        refined.extend(tuple(buckets[signature]) for signature in order)
    result = tuple(refined)
    if not observation_family_descends(observables, result):
        raise AssertionError("observation signature refinement must preserve every score")
    return result


def minimum_exact_partition_for_linear_language(
    matrices: tuple[Matrix, ...],
    observables: tuple[Observable, ...],
    initial_partition: Partition | None = None,
) -> Partition:
    """Coarsest refinement preserving all declared linear operations and scores.

    Fixed affine offsets and affine observable constants do not affect the
    partition: after the linear part descends, they aggregate as ordinary
    coarse integer offsets/constants.
    """
    if matrices:
        size = len(matrices[0])
    elif observables:
        size = len(observables[0])
    elif initial_partition:
        size = sum(len(group) for group in initial_partition)
    else:
        raise ValueError("at least one matrix, observable, or initial partition is required")

    if initial_partition is None:
        initial = (tuple(range(size)),)
    else:
        _require_partition(size, initial_partition)
        initial = initial_partition
    _require_observables(size, observables)

    observation_refined = refine_partition_for_linear_observations(
        observables, initial
    )
    if matrices:
        result = refine_partition_for_linear_family(
            matrices, observation_refined
        )
    else:
        result = observation_refined

    if not observation_family_descends(observables, result):
        raise AssertionError("final partition must preserve all observations")
    if matrices and not linear_family_descends(matrices, result):
        raise AssertionError("final partition must preserve all dynamics")
    return result
