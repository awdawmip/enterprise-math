"""Finite diagnostics for causal relation-language extension across dimensions.

A higher-dimensional construction may add primitive states and also change the
local observable attached to primitive states that already existed.  Replacing
an old observable by a new one can both split and merge old classes.  A genuine
language extension instead retains the old observable and appends the new one;
its cumulative signature can only refine the old partition.

This module keeps those two operations distinct and provides P011-compatible
integer revelation counts for the old states that split under the appended
observation.  It deliberately does not identify dimension increase with
precision increase unless the old observation is retained.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from math import comb
from typing import Hashable, Iterable

State = Hashable
Signature = Hashable


@dataclass(frozen=True)
class ExtensionTransition:
    old_class_size: int
    new_signature_counts: tuple[tuple[Signature, int], ...]

    @property
    def split_count(self) -> int:
        return len(self.new_signature_counts)

    @property
    def is_homogeneous(self) -> bool:
        return self.split_count == 1


def _group_counts(
    states: Iterable[State],
    signature: dict[State, Signature],
) -> Counter[Signature]:
    return Counter(signature[state] for state in states)


def old_to_new_transition_inventory(
    old_states: tuple[State, ...],
    old_signature: dict[State, Signature],
    new_signature: dict[State, Signature],
) -> dict[Signature, ExtensionTransition]:
    """How each old signature class is seen by the new current observation."""
    grouped: dict[Signature, list[State]] = defaultdict(list)
    for state in old_states:
        grouped[old_signature[state]].append(state)
    return {
        old: ExtensionTransition(
            old_class_size=len(states),
            new_signature_counts=tuple(
                sorted(_group_counts(states, new_signature).items(), key=repr)
            ),
        )
        for old, states in grouped.items()
    }


def cumulative_signature(
    old_states: tuple[State, ...],
    old_signature: dict[State, Signature],
    new_signature: dict[State, Signature],
) -> dict[State, tuple[Signature, Signature]]:
    """Retain the old observation and append the new one."""
    return {
        state: (old_signature[state], new_signature[state])
        for state in old_states
    }


def revelation_spectrum_for_transition(
    transition: ExtensionTransition,
    max_order: int | None = None,
) -> tuple[int, ...]:
    """P011-style groups newly distinguished inside one old class.

    Coordinate k (1-based in the mathematical interpretation) is

        C(N,k) - sum_i C(N_i,k),

    where ``N`` is the old class size and ``N_i`` are cumulative sub-class
    sizes after appending the new observation.  The k=1 coordinate is always
    zero; k>=2 counts formerly collapsed k-state groups that the new language
    reveals.
    """
    n = transition.old_class_size
    if max_order is None:
        max_order = n
    if max_order < 1:
        return ()
    sizes = tuple(count for _, count in transition.new_signature_counts)
    return tuple(
        comb(n, k) - sum(comb(size, k) for size in sizes)
        for k in range(1, min(max_order, n) + 1)
    )


def total_revelation_spectrum(
    inventory: dict[Signature, ExtensionTransition],
    max_order: int,
) -> tuple[int, ...]:
    if max_order < 1:
        return ()
    totals = [0] * max_order
    for transition in inventory.values():
        spectrum = revelation_spectrum_for_transition(transition, max_order)
        for index, value in enumerate(spectrum):
            totals[index] += value
    return tuple(totals)


def newly_created_signature_counts(
    new_states: tuple[State, ...],
    new_signature: dict[State, Signature],
) -> tuple[tuple[Signature, int], ...]:
    return tuple(sorted(_group_counts(new_states, new_signature).items(), key=repr))
