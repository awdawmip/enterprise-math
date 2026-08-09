"""Finite contextual refinement for multiplicity/grade-sensitive causal joins.

Raw witness identity may be collapsed only when every allowed left/right partner
context sees the same current observation and the same joint-output profile,
where an output profile records `(current output class, integer grade shift,
multiplicity)`.

Iterating this refinement yields a safe contextual type partition for a finite
weighted join system.  The induced typed kernel is then well-defined.  If the
raw weighted witness join is associative, the induced typed kernel is also
associative, so arbitrary-dimensional recursive composition can proceed without
recovering raw witness identity.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Hashable

from .causal_recursive_join import JoinKernel, kernel_is_associative

State = Hashable
Observation = Hashable
RawJoinKernel = dict[tuple[State, State, State, int], int]


def _canonical_classes(signatures: dict[State, Hashable]) -> dict[State, int]:
    states = tuple(sorted(signatures, key=repr))
    ids: dict[Hashable, int] = {}
    result = {}
    for state in states:
        signature = signatures[state]
        if signature not in ids:
            ids[signature] = len(ids)
        result[state] = ids[signature]
    return result


def _validate(
    states: tuple[State, ...],
    observations: dict[State, Observation],
    raw_kernel: RawJoinKernel,
) -> None:
    if not isinstance(states, tuple) or not states or len(set(states)) != len(states):
        raise ValueError("states must be a non-empty tuple of unique labels")
    if set(observations) != set(states):
        raise ValueError("observations must define every raw state")
    if not isinstance(raw_kernel, dict):
        raise ValueError("raw_kernel must be a dict")
    declared = set(states)
    for (left, right, out, shift), count in raw_kernel.items():
        if left not in declared or right not in declared or out not in declared:
            raise ValueError("raw kernel references an undeclared state")
        if isinstance(shift, bool) or not isinstance(shift, int):
            raise ValueError("grade shifts must be integers")
        if isinstance(count, bool) or not isinstance(count, int) or count < 0:
            raise ValueError("multiplicities must be non-negative integers")


def _pair_profile(
    left: State,
    right: State,
    classes: dict[State, int],
    raw_kernel: RawJoinKernel,
) -> tuple[tuple[int, int, int], ...]:
    counts: dict[tuple[int, int], int] = defaultdict(int)
    for (raw_left, raw_right, out, shift), multiplicity in raw_kernel.items():
        if raw_left == left and raw_right == right and multiplicity:
            counts[(classes[out], shift)] += multiplicity
    return tuple(
        (out_class, shift, multiplicity)
        for (out_class, shift), multiplicity in sorted(counts.items())
    )


def refine_weighted_context_once(
    states: tuple[State, ...],
    observations: dict[State, Observation],
    raw_kernel: RawJoinKernel,
    classes: dict[State, int],
) -> dict[State, int]:
    _validate(states, observations, raw_kernel)
    if set(classes) != set(states):
        raise ValueError("classes must define every raw state")
    partners = tuple(sorted(states, key=repr))
    signatures = {
        state: (
            observations[state],
            tuple(_pair_profile(state, partner, classes, raw_kernel) for partner in partners),
            tuple(_pair_profile(partner, state, classes, raw_kernel) for partner in partners),
        )
        for state in states
    }
    return _canonical_classes(signatures)


def stable_weighted_contextual_types(
    states: tuple[State, ...],
    observations: dict[State, Observation],
    raw_kernel: RawJoinKernel,
) -> tuple[dict[State, int], int]:
    """Coarsest partition stable under all raw left/right weighted join contexts."""
    _validate(states, observations, raw_kernel)
    classes = _canonical_classes(observations)
    rounds = 0
    while True:
        refined = refine_weighted_context_once(states, observations, raw_kernel, classes)
        rounds += 1
        same = all(
            (classes[left] == classes[right]) == (refined[left] == refined[right])
            for left in states
            for right in states
        )
        if same:
            return refined, rounds
        classes = refined
        if rounds > len(states):
            raise AssertionError("finite weighted contextual refinement failed to stabilize")


def induced_weighted_type_kernel(
    states: tuple[State, ...],
    raw_kernel: RawJoinKernel,
    classes: dict[State, int],
) -> JoinKernel:
    """Aggregate a context-compatible raw kernel to continuation types.

    Every pair of raw representatives from the same pair of classes must yield
    the same typed output profile.  Otherwise the supplied partition is not safe
    for binary composition.
    """
    if set(classes) != set(states):
        raise ValueError("classes must define every raw state")
    class_ids = tuple(sorted(set(classes.values())))
    result: JoinKernel = {}
    for left_class in class_ids:
        left_states = [state for state in states if classes[state] == left_class]
        for right_class in class_ids:
            right_states = [state for state in states if classes[state] == right_class]
            expected_profile = None
            for left in left_states:
                for right in right_states:
                    profile = _pair_profile(left, right, classes, raw_kernel)
                    if expected_profile is None:
                        expected_profile = profile
                    elif profile != expected_profile:
                        raise ValueError("partition is not safe for weighted binary composition")
            if expected_profile is None:
                continue
            for out_class, shift, multiplicity in expected_profile:
                if multiplicity:
                    result[(left_class, right_class, out_class, shift)] = multiplicity
    return result


def compile_weighted_contextual_kernel(
    states: tuple[State, ...],
    observations: dict[State, Observation],
    raw_kernel: RawJoinKernel,
) -> tuple[dict[State, int], JoinKernel, int]:
    classes, rounds = stable_weighted_contextual_types(states, observations, raw_kernel)
    induced = induced_weighted_type_kernel(states, raw_kernel, classes)
    if kernel_is_associative(states, raw_kernel):
        typed = tuple(sorted(set(classes.values())))
        if not kernel_is_associative(typed, induced):
            raise AssertionError("safe quotient of associative raw join lost associativity")
    return classes, induced, rounds
