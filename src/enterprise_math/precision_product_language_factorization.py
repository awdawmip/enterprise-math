"""Product-observation factorization and a minimal coupled-observation boundary.

For a product state X=prod X_i with componentwise actions and a full product
observable O(x)=(O_i(x_i)), future-signature equality under any correlated joint
action language A is exactly the product of the marginal future-signature
equalities for proj_i(A).  Joint action-label correlation is therefore invisible
to the coarsest safe quotient in this declared setting.

A two-bit AND-observation counterexample shows the boundary: once the observable
couples coordinates, two action languages with the same cardinality and the same
marginal action sets can induce different future-safe partitions.

The generic product-kernel fact is elementary prior mathematics.  R004 uses it
to locate where a future representation compiler must leave axiswise states and
retain joint relation/coupling information.
"""
from __future__ import annotations

from collections.abc import Callable, Sequence
from itertools import product
from typing import Hashable

BitState = tuple[int, int]
BitAction = tuple[int, int]
Partition = frozenset[frozenset[BitState]]

BIT_STATES: tuple[BitState, ...] = tuple(product((0, 1), repeat=2))
BIT_ACTIONS: tuple[BitAction, ...] = BIT_STATES


def _bit_pair(value: tuple[int, int], name: str) -> None:
    if (
        not isinstance(value, tuple)
        or len(value) != 2
        or any(isinstance(bit, bool) or bit not in (0, 1) for bit in value)
    ):
        raise ValueError(f"{name} must be a two-bit tuple")


def xor_action(state: BitState, action: BitAction) -> BitState:
    _bit_pair(state, "state")
    _bit_pair(action, "action")
    return state[0] ^ action[0], state[1] ^ action[1]


def full_product_observable(state: BitState) -> BitState:
    _bit_pair(state, "state")
    return state


def coupled_and_observable(state: BitState) -> int:
    _bit_pair(state, "state")
    return state[0] * state[1]


def future_signature(
    state: BitState,
    actions: Sequence[BitAction],
    observable: Callable[[BitState], Hashable],
) -> tuple[Hashable, ...]:
    _bit_pair(state, "state")
    language = tuple(actions)
    if not language:
        raise ValueError("action language must be nonempty")
    for action in language:
        _bit_pair(action, "action")
    return tuple(observable(xor_action(state, action)) for action in language)


def signature_partition(
    actions: Sequence[BitAction],
    observable: Callable[[BitState], Hashable],
) -> Partition:
    groups: dict[tuple[Hashable, ...], set[BitState]] = {}
    for state in BIT_STATES:
        groups.setdefault(future_signature(state, actions, observable), set()).add(state)
    return frozenset(frozenset(group) for group in groups.values())


def marginal_action_sets(actions: Sequence[BitAction]) -> tuple[frozenset[int], frozenset[int]]:
    language = tuple(actions)
    if not language:
        raise ValueError("action language must be nonempty")
    for action in language:
        _bit_pair(action, "action")
    return (
        frozenset(action[0] for action in language),
        frozenset(action[1] for action in language),
    )


def marginal_identity_partition(actions: Sequence[BitAction], axis: int) -> frozenset[frozenset[int]]:
    if axis not in (0, 1):
        raise ValueError("axis must be 0 or 1")
    marginal = marginal_action_sets(actions)[axis]
    groups: dict[tuple[int, ...], set[int]] = {}
    for state in (0, 1):
        signature = tuple(state ^ action for action in sorted(marginal))
        groups.setdefault(signature, set()).add(state)
    return frozenset(frozenset(group) for group in groups.values())


def product_of_marginal_partitions(actions: Sequence[BitAction]) -> Partition:
    left = marginal_identity_partition(actions, 0)
    right = marginal_identity_partition(actions, 1)
    groups = []
    for left_class in left:
        for right_class in right:
            groups.append(
                frozenset((a, b) for a in left_class for b in right_class)
            )
    return frozenset(groups)


def full_vector_factorization_holds(actions: Sequence[BitAction]) -> bool:
    return signature_partition(actions, full_product_observable) == product_of_marginal_partitions(actions)


def coupled_correlation_counterexample() -> tuple[Partition, Partition]:
    """Return two different safe partitions with identical action marginals."""
    diagonal = ((0, 0), (1, 1))
    cross = ((0, 1), (1, 0))
    if len(diagonal) != len(cross):
        raise AssertionError("counterexample languages must have equal cardinality")
    if marginal_action_sets(diagonal) != marginal_action_sets(cross):
        raise AssertionError("counterexample languages must have identical marginals")
    left = signature_partition(diagonal, coupled_and_observable)
    right = signature_partition(cross, coupled_and_observable)
    if left == right:
        raise AssertionError("coupled observation must expose joint action correlation")
    return left, right
