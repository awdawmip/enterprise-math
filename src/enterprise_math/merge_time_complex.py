"""Labelled first-merger times for deterministic finite observations.

For a deterministic endomap, a finite set of histories first lies in one kernel
fiber exactly when every pair in the set has already coalesced.  Consequently
the first common-fiber time of a finite subset is the maximum of its pairwise
first-coalescence times.  This module pressure-tests the resulting compression:
the labelled pairwise merge-time matrix reconstructs the entire kernel
filtration and every time-resolved P011 collision count.

General dendrogram/ultrametric equivalences are established mathematics; this
module only tests the exact Enterprise Math P010/P011/P018 interface.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Callable, Iterable, Sequence
from itertools import combinations

from .coalescence_time import first_coalescence_time, iterate, kernel_pairs_at_step
from .collision_increment import collision_polynomial_from_fiber_sizes

NaturalOperation = Callable[[int], int]


def _states_tuple(states: Iterable[int]) -> tuple[int, ...]:
    materialized = tuple(states)
    if len(set(materialized)) != len(materialized):
        raise ValueError("states must be distinct labels")
    for state in materialized:
        if isinstance(state, bool) or not isinstance(state, int) or state < 0:
            raise ValueError("states must be non-negative integers")
    return materialized


def subset_first_common_time(
    operation: NaturalOperation,
    subset: Sequence[int],
    *,
    max_steps: int = 10000,
) -> int | None:
    """First common time at which all labelled histories have one image.

    ``None`` means no common time was found within ``max_steps``.  A singleton
    has common time zero.
    """
    states = _states_tuple(subset)
    if not states:
        raise ValueError("subset must be nonempty")
    for step in range(max_steps + 1):
        images = {iterate(operation, state, step) for state in states}
        if len(images) == 1:
            return step
    return None


def subset_time_from_pair_times(
    operation: NaturalOperation,
    subset: Sequence[int],
    *,
    max_steps: int = 10000,
) -> int | None:
    """Compute the finite-subset merger time as max pairwise merger time."""
    states = _states_tuple(subset)
    if not states:
        raise ValueError("subset must be nonempty")
    if len(states) == 1:
        return 0
    pair_times: list[int] = []
    for left, right in combinations(states, 2):
        tau = first_coalescence_time(
            operation, left, right, max_steps=max_steps
        )
        if tau is None:
            return None
        pair_times.append(tau)
    return max(pair_times)


def labelled_pair_merge_times(
    operation: NaturalOperation,
    states: Iterable[int],
    *,
    max_steps: int = 10000,
) -> dict[tuple[int, int], int | None]:
    """Return the labelled extended pairwise merge-time matrix.

    ``None`` is the executable stand-in for infinity / no observed merger.
    Ordered pairs are returned to match the kernel-pair representation.
    """
    materialized = _states_tuple(states)
    result: dict[tuple[int, int], int | None] = {}
    for left in materialized:
        for right in materialized:
            result[(left, right)] = first_coalescence_time(
                operation, left, right, max_steps=max_steps
            )
    return result


def kernel_pairs_from_merge_times(
    merge_times: dict[tuple[int, int], int | None], step: int
) -> set[tuple[int, int]]:
    """Threshold a labelled merge-time matrix to reconstruct one kernel level."""
    if isinstance(step, bool) or not isinstance(step, int) or step < 0:
        raise ValueError("step must be a non-negative integer")
    return {
        pair
        for pair, tau in merge_times.items()
        if tau is not None and tau <= step
    }


def fiber_sizes_at_step(
    operation: NaturalOperation, states: Iterable[int], step: int
) -> tuple[int, ...]:
    """Return the multiset of kernel-fiber sizes on a finite labelled domain."""
    materialized = _states_tuple(states)
    images = [iterate(operation, state, step) for state in materialized]
    return tuple(sorted(Counter(images).values()))


def collision_coefficients_at_step(
    operation: NaturalOperation, states: Iterable[int], step: int
) -> tuple[int, ...]:
    """P011 collision-polynomial coefficients for the step-n kernel partition."""
    return collision_polynomial_from_fiber_sizes(
        fiber_sizes_at_step(operation, states, step)
    )


def coefficient(coefficients: tuple[int, ...], degree: int) -> int:
    """Read one degree from a degree-1-indexed coefficient vector."""
    if isinstance(degree, bool) or not isinstance(degree, int) or degree <= 0:
        raise ValueError("degree must be a positive integer")
    index = degree - 1
    return coefficients[index] if index < len(coefficients) else 0


def first_merge_count_from_subsets(
    operation: NaturalOperation,
    states: Iterable[int],
    degree: int,
    step: int,
    *,
    max_steps: int = 10000,
) -> int:
    """Count labelled k-subsets whose first common-fiber time equals ``step``."""
    materialized = _states_tuple(states)
    if isinstance(degree, bool) or not isinstance(degree, int) or degree <= 0:
        raise ValueError("degree must be a positive integer")
    if degree > len(materialized):
        return 0
    return sum(
        subset_time_from_pair_times(
            operation, subset, max_steps=max_steps
        )
        == step
        for subset in combinations(materialized, degree)
    )


def collision_increment_degree(
    operation: NaturalOperation,
    states: Iterable[int],
    degree: int,
    step: int,
) -> int:
    """Return J_k(F^step)-J_k(F^(step-1)) on one finite observation set."""
    if isinstance(step, bool) or not isinstance(step, int) or step <= 0:
        raise ValueError("step must be a positive integer")
    materialized = _states_tuple(states)
    current = coefficient(
        collision_coefficients_at_step(operation, materialized, step), degree
    )
    previous = coefficient(
        collision_coefficients_at_step(operation, materialized, step - 1), degree
    )
    return current - previous


def merge_times_reconstruct_kernel(
    operation: NaturalOperation,
    states: Iterable[int],
    step: int,
    *,
    max_steps: int = 10000,
) -> bool:
    """Check that tau<=n reconstructs ker(F^n) exactly on finite labels."""
    materialized = _states_tuple(states)
    merge_times = labelled_pair_merge_times(
        operation, materialized, max_steps=max_steps
    )
    return kernel_pairs_from_merge_times(merge_times, step) == kernel_pairs_at_step(
        operation, materialized, step
    )
