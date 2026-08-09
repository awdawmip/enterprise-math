"""Composition-to-partition geometry of Barlow collision-polynomial states.

For final-observing selected-layer schedules, ordered positive segment lengths
are compositions of the horizon.  The complete P011 collision polynomial
recovers exactly the segment-length multiset, so collision states are indexed by
integer partitions of the same horizon.

Allowing a hidden tail adds one visible-prefix length parameter: a general
selected-layer schedule on total horizon N is encoded by ``(tail, partition of
N-tail)``.  All counting remains finite and integer.
"""

from __future__ import annotations

from functools import lru_cache
from math import comb, gcd

Rational = tuple[int, int]


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _reduce(numerator: int, denominator: int) -> Rational:
    if denominator <= 0:
        raise ValueError("denominator must be positive")
    divisor = gcd(abs(numerator), denominator)
    return numerator // divisor, denominator // divisor


@lru_cache(maxsize=None)
def partition_count_exact_parts(total: int, parts: int) -> int:
    """Number p_parts(total) of partitions into exactly ``parts`` positive parts.

    The recurrence

        p_k(n)=p_(k-1)(n-1)+p_k(n-k)

    separates partitions containing a part 1 from those whose k parts are all
    at least 2.
    """
    _require_natural("total", total)
    _require_natural("parts", parts)
    if total == 0:
        return 1 if parts == 0 else 0
    if parts == 0 or parts > total:
        return 0
    if parts == 1 or parts == total:
        return 1
    return partition_count_exact_parts(total - 1, parts - 1) + (
        partition_count_exact_parts(total - parts, parts)
    )


@lru_cache(maxsize=None)
def partition_number(total: int) -> int:
    """Ordinary integer partition number p(total), with p(0)=1."""
    _require_natural("total", total)
    return sum(
        partition_count_exact_parts(total, parts)
        for parts in range(total + 1)
    )


def ordered_final_schedule_count(total: int, checkpoint_count: int) -> int:
    """Positive compositions of N into m segments: C(N-1,m-1)."""
    _require_positive("total", total)
    _require_positive("checkpoint_count", checkpoint_count)
    if checkpoint_count > total:
        return 0
    return comb(total - 1, checkpoint_count - 1)


def collision_state_count_final(
    total: int, checkpoint_count: int
) -> int:
    """Complete collision-polynomial states = partitions into m parts."""
    _require_positive("total", total)
    _require_positive("checkpoint_count", checkpoint_count)
    return partition_count_exact_parts(total, checkpoint_count)


def average_order_fiber_over_collision_states(
    total: int, checkpoint_count: int
) -> Rational:
    """Mean ordered-geometry fiber size when collision states are equally weighted."""
    images = collision_state_count_final(total, checkpoint_count)
    if images == 0:
        raise ValueError("no schedules exist for this total/checkpoint count")
    return _reduce(
        ordered_final_schedule_count(total, checkpoint_count),
        images,
    )


def all_final_observing_ordered_schedule_count(total: int) -> int:
    """All nonempty final-observing checkpoint schedules across m=1..N."""
    _require_positive("total", total)
    # Every subset of the N-1 internal boundaries gives one composition.
    return 2 ** (total - 1)


def all_final_observing_collision_state_count(total: int) -> int:
    """Distinct complete collision polynomials across all final-observing schedules."""
    _require_positive("total", total)
    return partition_number(total)


def all_selected_layer_schedule_count(total: int) -> int:
    """All checkpoint subsets of layers 1..N, including the empty set."""
    _require_natural("total", total)
    return 2**total


def all_selected_layer_collision_state_count(total: int) -> int:
    """Distinct complete collision states with arbitrary hidden tail.

    Let L be the last observed layer, with L=0 for no checkpoint.  The complete
    collision polynomial recovers tail ``N-L`` and a partition of L.  Hence the
    image count is ``sum_{L=0}^N p(L)``.
    """
    _require_natural("total", total)
    return sum(partition_number(prefix) for prefix in range(total + 1))


def average_geometry_fiber_all_selected_layers(total: int) -> Rational:
    """Mean schedule fiber over complete collision states for all checkpoint sets."""
    _require_natural("total", total)
    return _reduce(
        all_selected_layer_schedule_count(total),
        all_selected_layer_collision_state_count(total),
    )
