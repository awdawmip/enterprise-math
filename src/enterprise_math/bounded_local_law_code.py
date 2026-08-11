"""Generic finite codes for bounded local-law reflection.

A modulus is only one way to encode a finite local coefficient alphabet.  If the
workflow decodes the local law **before** future composition, the observation
code need not itself carry semiring operations.  It only needs to be injective on
the finite set of exact local aggregate values that can occur.

For integer-weighted transition laws, one refinement step depends only on those
local target-block aggregates.  Applying any hashable code ``c(value)`` that is
injective on the local alphabet therefore produces the same refinement as exact
integer values.  At the stable partition, the code can be inverted on that
alphabet to reconstruct the exact weighted machine; all later composition is
then performed in Z.

This separates three resources:

* local observation/coding precision;
* local decoding/reflection theorem;
* exact execution algebra used after reflection.

If instead one wants to compose directly inside the coded world, additional
algebraic structure and homomorphism laws are required.  They are not needed for
reflection-before-compose.
"""

from __future__ import annotations

from typing import Callable, Hashable, Mapping, Sequence

from .bounded_local_law_reflection import (
    Action,
    Observation,
    State,
    WeightedFamily,
    _states,
    _weighted_family,
    exact_target_block_aggregate,
    exact_weighted_quotient_matrices,
    weighted_local_aggregate_alphabet,
)
from .relation_support_stable_refinement import (
    Partition,
    normalize_partition,
    partition_from_observation,
    partition_refines,
)


LocalCode = Callable[[int], Hashable]


def code_is_injective_on_values(
    values: Sequence[int] | frozenset[int],
    code: LocalCode,
) -> bool:
    alphabet = tuple(set(values))
    if not alphabet:
        raise ValueError("value alphabet must be nonempty")
    encoded = tuple(code(value) for value in alphabet)
    for value in encoded:
        hash(value)
    return len(set(encoded)) == len(alphabet)


def decode_local_code(
    encoded: Hashable,
    alphabet: Sequence[int] | frozenset[int],
    code: LocalCode,
) -> int:
    values = tuple(set(alphabet))
    if not code_is_injective_on_values(values, code):
        raise ValueError("code is not injective on local alphabet")
    candidates = tuple(value for value in values if code(value) == encoded)
    if len(candidates) != 1:
        raise ValueError("encoded value has no unique local lift")
    return candidates[0]


def coded_weighted_refinement_step(
    partition: Sequence[Sequence[State] | frozenset[State]],
    family: WeightedFamily,
    code: LocalCode,
) -> Partition:
    current = normalize_partition(partition)
    states = tuple(sorted(frozenset().union(*current), key=repr))
    weighted = _weighted_family(states, family)
    names = tuple(sorted(weighted, key=repr))
    refined: list[set[State]] = []
    for block in current:
        groups: dict[tuple[object, ...], set[State]] = {}
        for state in block:
            signature = tuple(
                (
                    name,
                    tuple(
                        code(
                            exact_target_block_aggregate(
                                current,
                                weighted[name],
                                state,
                                target_block,
                            )
                        )
                        for target_block in range(len(current))
                    ),
                )
                for name in names
            )
            # Fail immediately if the caller's code returns non-hashable data.
            hash(signature)
            groups.setdefault(signature, set()).add(state)
        refined.extend(groups.values())
    result = normalize_partition(refined)
    if not partition_refines(result, current):
        raise AssertionError("coded local-law step failed to refine current partition")
    return result


def coded_weighted_refinement_sequence(
    initial_partition: Sequence[Sequence[State] | frozenset[State]],
    family: WeightedFamily,
    code: LocalCode,
) -> tuple[Partition, ...]:
    current = normalize_partition(initial_partition)
    states = tuple(sorted(frozenset().union(*current), key=repr))
    _weighted_family(states, family)
    steps = [current]
    while True:
        nxt = coded_weighted_refinement_step(current, family, code)
        if nxt == current:
            return tuple(steps)
        if len(nxt) <= len(current):
            raise AssertionError("strict coded refinement failed block growth")
        steps.append(nxt)
        current = nxt
        if len(steps) - 1 > len(states) - len(steps[0]):
            raise AssertionError("coded refinement exceeded finite block-growth bound")


def reflective_local_code_reproduces_exact_sequence(
    states: Sequence[State],
    family: WeightedFamily,
    observation: Callable[[State], Observation],
    code: LocalCode,
) -> bool:
    order = _states(states)
    weighted = _weighted_family(order, family)
    alphabet = weighted_local_aggregate_alphabet(order, weighted)
    if not code_is_injective_on_values(alphabet, code):
        raise ValueError("local code is not injective on aggregate alphabet")
    initial = partition_from_observation(order, observation)

    # Identity-code sequence is the exact integer refinement.
    exact = coded_weighted_refinement_sequence(initial, weighted, lambda value: value)
    coded = coded_weighted_refinement_sequence(initial, weighted, code)
    if exact != coded:
        raise AssertionError("injective local code changed exact weighted refinement")
    return True


def reconstruct_exact_quotient_from_local_code(
    partition: Sequence[Sequence[State] | frozenset[State]],
    states: Sequence[State],
    family: WeightedFamily,
    code: LocalCode,
) -> dict[Action, tuple[tuple[int, ...], ...]]:
    """Decode stable coded local weights and recover the exact integer machine."""
    order = _states(states)
    current = normalize_partition(partition)
    weighted = _weighted_family(order, family)
    alphabet = weighted_local_aggregate_alphabet(order, weighted)
    if not code_is_injective_on_values(alphabet, code):
        raise ValueError("local code is not injective on aggregate alphabet")

    matrices: dict[Action, tuple[tuple[int, ...], ...]] = {}
    for name, relation in weighted.items():
        columns = []
        for source_block_index, source_block in enumerate(current):
            encoded_vectors = tuple(
                tuple(
                    code(
                        exact_target_block_aggregate(
                            current,
                            relation,
                            source,
                            target_block,
                        )
                    )
                    for target_block in range(len(current))
                )
                for source in source_block
            )
            if len(set(encoded_vectors)) != 1:
                raise ValueError(
                    f"partition is not coded-weight-stable for action {name!r} at block {source_block_index}"
                )
            lifted = tuple(
                decode_local_code(encoded, alphabet, code)
                for encoded in encoded_vectors[0]
            )
            columns.append(lifted)
        matrices[name] = tuple(
            tuple(columns[source][target] for source in range(len(current)))
            for target in range(len(current))
        )

    exact = exact_weighted_quotient_matrices(current, weighted)
    if matrices != exact:
        raise AssertionError("decoded local code failed to recover exact weighted quotient")
    return matrices
