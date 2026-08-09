"""Operation fibers induced by a finite causal state quotient.

Let E partition a finite raw state set X into quotient classes B_i.  A raw
endomap f:X->X is E-safe exactly when each source block B_i is mapped wholly into
one target block.  Every safe raw map therefore induces a quotient endomap
phi:X/E -> X/E.

For a fixed quotient map phi, the exact number of raw lifts is

    m(phi) = product_i |B_(phi(i))| ^ |B_i|.

Hence the operation projection Safe(E)->End(X/E) is always surjective and has an
exact integer fiber structure.  This is the operation-side analogue of state
collapse multiplicity and can be analyzed by the P011 collision spectrum.

The maximal safe set is a semantic compatibility envelope, not a claim that all
such raw operations are physically available.
"""

from __future__ import annotations

from collections import Counter
from math import comb
from typing import Hashable

from .causal_operation_language import Partition

State = Hashable


def quotient_class_sizes(
    states: tuple[State, ...],
    partition: Partition,
) -> tuple[int, ...]:
    if set(partition) != set(states):
        raise ValueError("partition must cover the state set")
    counts = Counter(partition[state] for state in states)
    class_ids = tuple(sorted(counts))
    if class_ids != tuple(range(len(class_ids))):
        raise ValueError("partition class ids must be canonical consecutive integers")
    return tuple(counts[class_id] for class_id in class_ids)


def quotient_endomorphism_count(
    states: tuple[State, ...],
    partition: Partition,
) -> int:
    classes = len(quotient_class_sizes(states, partition))
    return classes ** classes


def safe_raw_endomorphism_count(
    states: tuple[State, ...],
    partition: Partition,
) -> int:
    """Exact number of all raw endomaps preserving the quotient equivalence."""
    sizes = quotient_class_sizes(states, partition)
    return _safe_count_from_sizes(sizes)


def _safe_count_from_sizes(sizes: tuple[int, ...]) -> int:
    result = 1
    for source_size in sizes:
        result *= sum(target_size ** source_size for target_size in sizes)
    return result


def quotient_map_lift_count(
    states: tuple[State, ...],
    partition: Partition,
    quotient_map: tuple[int, ...],
) -> int:
    """Number of raw E-safe maps inducing the supplied quotient endomap.

    `quotient_map[i]=j` means source class i maps to target class j.
    """
    sizes = quotient_class_sizes(states, partition)
    classes = len(sizes)
    if (
        not isinstance(quotient_map, tuple)
        or len(quotient_map) != classes
        or any(
            isinstance(target, bool)
            or not isinstance(target, int)
            or not (0 <= target < classes)
            for target in quotient_map
        )
    ):
        raise ValueError("quotient_map must choose one target class for every source class")
    result = 1
    for source_class, target_class in enumerate(quotient_map):
        result *= sizes[target_class] ** sizes[source_class]
    return result


def operation_projection_fiber_histogram(
    states: tuple[State, ...],
    partition: Partition,
) -> dict[int, int]:
    """Histogram {raw-lift multiplicity: number of quotient endomaps}.

    Dynamic programming avoids enumerating all c^c quotient maps explicitly.
    """
    sizes = quotient_class_sizes(states, partition)
    histogram = {1: 1}
    for source_size in sizes:
        next_histogram: dict[int, int] = {}
        for current_product, ways in histogram.items():
            for target_size in sizes:
                product_value = current_product * (target_size ** source_size)
                next_histogram[product_value] = next_histogram.get(product_value, 0) + ways
        histogram = next_histogram
    return dict(sorted(histogram.items()))


def operation_projection_audit(
    states: tuple[State, ...],
    partition: Partition,
) -> bool:
    histogram = operation_projection_fiber_histogram(states, partition)
    quotient_maps = sum(histogram.values())
    raw_safe = sum(multiplicity * count for multiplicity, count in histogram.items())
    return (
        quotient_maps == quotient_endomorphism_count(states, partition)
        and raw_safe == safe_raw_endomorphism_count(states, partition)
    )


def operation_projection_collision_spectrum(
    states: tuple[State, ...],
    partition: Partition,
    maximum_order: int,
) -> tuple[int, ...]:
    """P011 J_1,...,J_K for raw operations collapsed to quotient operations."""
    if isinstance(maximum_order, bool) or not isinstance(maximum_order, int) or maximum_order < 1:
        raise ValueError("maximum_order must be a positive integer")
    histogram = operation_projection_fiber_histogram(states, partition)
    return tuple(
        sum(
            quotient_map_count * comb(multiplicity, order)
            for multiplicity, quotient_map_count in histogram.items()
            if multiplicity >= order
        )
        for order in range(1, maximum_order + 1)
    )


def uniform_partition_operation_fiber(
    class_count: int,
    class_size: int,
) -> tuple[int, int, int]:
    """Closed uniform-block law `(quotient_maps, lift_per_map, safe_raw_maps)`.

    For c equal classes of size b on n=c*b raw states, every quotient endomap has
    exactly b^n raw lifts.  Thus |Safe(E)|=c^c*b^n.
    """
    if (
        isinstance(class_count, bool)
        or not isinstance(class_count, int)
        or class_count <= 0
        or isinstance(class_size, bool)
        or not isinstance(class_size, int)
        or class_size <= 0
    ):
        raise ValueError("class_count and class_size must be positive integers")
    raw_states = class_count * class_size
    quotient_maps = class_count ** class_count
    lift_per_map = class_size ** raw_states
    return quotient_maps, lift_per_map, quotient_maps * lift_per_map
