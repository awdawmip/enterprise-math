"""Support-order causal tomography of unit-amplitude conservation laws.

A conservation law is probed only by finite unit-amplitude events delta_i in
{-1,0,+1}.  Its support-order observation at depth s is the exact set of accepted
nonzero events whose support is at most s.  Two laws are indistinguishable to
that depth iff these event sets agree.  The first support at which they differ is
the minimum number of simultaneously involved LEGO slots needed to distinguish
the laws under this probe language.

For total modular laws sum(delta)=0 mod m, with enough slots:

* no constraint versus a nontrivial modulus differs at support one;
* mod 2 versus any modulus >=3 differs at support two;
* exact total conservation versus mod m differs first at support m;
* two distinct positive moduli m,n differ first at support min(m,n).

Thus primitive A-type support-two geometry for mod m>=3 does not identify the
underlying modulus.  Higher-support causal probes are required.
"""

from __future__ import annotations

from itertools import product
from typing import Callable

Vector = tuple[int, ...]
Law = Callable[[Vector], bool]


def support_size(event: Vector) -> int:
    return sum(value != 0 for value in event)


def unit_amplitude_events(slot_count: int, maximum_support: int | None = None) -> tuple[Vector, ...]:
    if isinstance(slot_count, bool) or not isinstance(slot_count, int) or slot_count < 1:
        raise ValueError("slot_count must be positive")
    limit = slot_count if maximum_support is None else maximum_support
    if isinstance(limit, bool) or not isinstance(limit, int) or not (0 <= limit <= slot_count):
        raise ValueError("maximum_support must lie in 0..slot_count")
    return tuple(
        tuple(event)
        for event in product((-1, 0, 1), repeat=slot_count)
        if any(event) and support_size(tuple(event)) <= limit
    )


def unconstrained_law(event: Vector) -> bool:
    return any(event)


def exact_total_law(event: Vector) -> bool:
    return any(event) and sum(event) == 0


def modular_total_law(modulus: int) -> Law:
    if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus < 1:
        raise ValueError("modulus must be positive")
    return lambda event: any(event) and sum(event) % modulus == 0


def accepted_events_through_support(
    slot_count: int,
    law: Law,
    maximum_support: int,
) -> frozenset[Vector]:
    return frozenset(
        event
        for event in unit_amplitude_events(slot_count, maximum_support)
        if law(event)
    )


def laws_agree_through_support(
    slot_count: int,
    left: Law,
    right: Law,
    maximum_support: int,
) -> bool:
    return accepted_events_through_support(
        slot_count, left, maximum_support
    ) == accepted_events_through_support(
        slot_count, right, maximum_support
    )


def first_distinguishing_support(
    slot_count: int,
    left: Law,
    right: Law,
) -> int | None:
    for support in range(1, slot_count + 1):
        if not laws_agree_through_support(slot_count, left, right, support):
            return support
    return None


def first_distinguishing_event(
    slot_count: int,
    left: Law,
    right: Law,
) -> Vector | None:
    support = first_distinguishing_support(slot_count, left, right)
    if support is None:
        return None
    left_events = accepted_events_through_support(slot_count, left, support)
    right_events = accepted_events_through_support(slot_count, right, support)
    candidates = sorted(
        (left_events ^ right_events),
        key=lambda event: (support_size(event), event),
    )
    return candidates[0] if candidates else None


def accepted_support_histogram(slot_count: int, law: Law) -> tuple[int, ...]:
    counts = [0] * (slot_count + 1)
    for event in unit_amplitude_events(slot_count):
        if law(event):
            counts[support_size(event)] += 1
    return tuple(counts[1:])


def exact_vs_modular_tomography_order(slot_count: int, modulus: int) -> int | None:
    return first_distinguishing_support(
        slot_count,
        exact_total_law,
        modular_total_law(modulus),
    )


def modular_pair_tomography_order(slot_count: int, left_modulus: int, right_modulus: int) -> int | None:
    return first_distinguishing_support(
        slot_count,
        modular_total_law(left_modulus),
        modular_total_law(right_modulus),
    )
