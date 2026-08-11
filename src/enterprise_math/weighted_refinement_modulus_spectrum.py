"""Exact modulus spectrum for one fixed finite integer-weighted transition world.

A universal local-alphabet reflection theorem can be conservative.  For one
fixed world, only coefficient differences that actually cause a split along the
exact refinement sequence matter.

At exact stage h, take x,y in one current block that land in different blocks at
the next stage.  Flatten their complete integer local-weight signatures over all
actions and current target blocks, take the coordinatewise difference, and let

    g_(h,x,y) = gcd(abs(differences)).

Because the exact signatures differ, g>0.  Modulus M collapses this exact split
pair iff every coordinate difference vanishes modulo M, equivalently iff M|g.

Therefore the complete mod-M refinement sequence equals the exact integer
sequence iff M divides **none** of the finitely many split contents g.

The bad-modulus set is a finite union of divisor down-sets.  The exact-modulus
set is its complement and is upward closed under divisibility.  This gives a
relation-specific precision spectrum strictly sharper than requiring the
quotient to be injective on every subset sum that could occur under arbitrary
partitions.

GCD content and modular signature collisions are standard arithmetic.  The
project value is the exact one-world precision-spectrum interpretation.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import reduce
from math import gcd
from typing import Callable, Hashable, Mapping, Sequence

from .bounded_local_law_reflection import (
    Action,
    Observation,
    State,
    WeightedFamily,
    _states,
    _weighted_family,
    exact_target_block_aggregate,
    weighted_refinement_sequence,
    weighted_refinement_step,
)
from .relation_support_stable_refinement import (
    Partition,
    normalize_partition,
    partition_from_observation,
)


def exact_weight_signature_vector(
    partition: Sequence[Sequence[State] | frozenset[State]],
    family: WeightedFamily,
    state: State,
) -> tuple[int, ...]:
    current = normalize_partition(partition)
    states = tuple(sorted(frozenset().union(*current), key=repr))
    weighted = _weighted_family(states, family)
    if state not in states:
        raise ValueError("state outside partition")
    names = tuple(sorted(weighted, key=repr))
    return tuple(
        exact_target_block_aggregate(
            current,
            weighted[name],
            state,
            target_block_index,
        )
        for name in names
        for target_block_index in range(len(current))
    )


def difference_content(left: Sequence[int], right: Sequence[int]) -> int:
    a = tuple(left)
    b = tuple(right)
    if len(a) != len(b):
        raise ValueError("signature vectors must share one dimension")
    if not a:
        raise ValueError("signature vectors must be nonempty")
    differences = tuple(abs(x - y) for x, y in zip(a, b, strict=True))
    return reduce(gcd, differences, 0)


@dataclass(frozen=True)
class WeightedSplitContentEvent:
    horizon: int
    left_state: State
    right_state: State
    gcd_content: int
    left_signature: tuple[int, ...]
    right_signature: tuple[int, ...]

    def collapsed_by_modulus(self, modulus: int) -> bool:
        if isinstance(modulus, bool) or not isinstance(modulus, int):
            raise TypeError("modulus must be an integer")
        if modulus <= 1:
            raise ValueError("modulus must exceed one")
        return self.gcd_content % modulus == 0


def exact_weighted_split_content_events(
    states: Sequence[State],
    family: WeightedFamily,
    observation: Callable[[State], Observation],
) -> tuple[WeightedSplitContentEvent, ...]:
    order = _states(states)
    weighted = _weighted_family(order, family)
    current = partition_from_observation(order, observation)
    events: list[WeightedSplitContentEvent] = []
    horizon = 0

    while True:
        nxt = weighted_refinement_step(current, weighted)
        if nxt == current:
            return tuple(events)
        next_block_of = {
            state: index
            for index, block in enumerate(nxt)
            for state in block
        }
        for block in current:
            values = tuple(sorted(block, key=repr))
            signatures = {
                state: exact_weight_signature_vector(current, weighted, state)
                for state in values
            }
            for left_index, left in enumerate(values):
                for right in values[left_index + 1 :]:
                    if next_block_of[left] == next_block_of[right]:
                        continue
                    content = difference_content(signatures[left], signatures[right])
                    if content <= 0:
                        raise AssertionError("strict exact split had zero signature content")
                    events.append(
                        WeightedSplitContentEvent(
                            horizon=horizon,
                            left_state=left,
                            right_state=right,
                            gcd_content=content,
                            left_signature=signatures[left],
                            right_signature=signatures[right],
                        )
                    )
        current = nxt
        horizon += 1
        if horizon > len(order):
            raise AssertionError("weighted split-content scan exceeded state bound")


def positive_divisors(value: int) -> tuple[int, ...]:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError("value must be an integer")
    if value <= 0:
        raise ValueError("value must be positive")
    result = []
    for divisor in range(2, value + 1):
        if value % divisor == 0:
            result.append(divisor)
    return tuple(result)


def exact_bad_moduli_for_weighted_refinement(
    states: Sequence[State],
    family: WeightedFamily,
    observation: Callable[[State], Observation],
) -> frozenset[int]:
    bad = set()
    for event in exact_weighted_split_content_events(states, family, observation):
        bad.update(positive_divisors(event.gcd_content))
    return frozenset(bad)


def modulus_reproduces_exact_weighted_sequence_by_contents(
    states: Sequence[State],
    family: WeightedFamily,
    observation: Callable[[State], Observation],
    modulus: int,
) -> bool:
    if isinstance(modulus, bool) or not isinstance(modulus, int):
        raise TypeError("modulus must be an integer")
    if modulus <= 1:
        raise ValueError("modulus must exceed one")
    events = exact_weighted_split_content_events(states, family, observation)
    predicted = all(not event.collapsed_by_modulus(modulus) for event in events)

    initial = partition_from_observation(states, observation)
    exact = weighted_refinement_sequence(initial, family)
    modular = weighted_refinement_sequence(initial, family, modulus=modulus)
    actual = exact == modular
    if predicted != actual:
        raise AssertionError("split-content modulus criterion disagreed with actual refinement")
    return predicted


def least_numeric_exact_modulus_from_contents(
    states: Sequence[State],
    family: WeightedFamily,
    observation: Callable[[State], Observation],
) -> int:
    events = exact_weighted_split_content_events(states, family, observation)
    maximum_content = max((event.gcd_content for event in events), default=1)
    for modulus in range(2, maximum_content + 2):
        if all(not event.collapsed_by_modulus(modulus) for event in events):
            return modulus
    raise AssertionError("a modulus above every split content should be exact")


def exact_moduli_are_upward_closed_sample(
    states: Sequence[State],
    family: WeightedFamily,
    observation: Callable[[State], Observation],
    limit: int,
) -> bool:
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 2:
        raise ValueError("limit must be an integer at least two")
    exact = {
        modulus
        for modulus in range(2, limit + 1)
        if modulus_reproduces_exact_weighted_sequence_by_contents(
            states,
            family,
            observation,
            modulus,
        )
    }
    for modulus in exact:
        for multiple in range(2 * modulus, limit + 1, modulus):
            if multiple not in exact:
                raise AssertionError("exact weighted-refinement moduli were not upward closed")
    return True
