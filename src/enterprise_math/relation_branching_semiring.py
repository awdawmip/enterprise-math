"""Semiring-parametric branching signatures for finite relation-valued actions.

A raw finite relation contributes a finite number of successor states of each
previous-depth behavioural type. Rather than fixing how those multiplicities
are interpreted, choose a commutative semiring K and send the natural successor
count ``n`` to ``n * 1_K``.

The recursive K-branching signature is

    beta^K_0(x) = O(x)

    beta^K_(h+1)(x)
      = (O(x), (sum-by-child-type 1_K)_a).

Equivalently, for each action it stores a finitely supported K-valued function
on depth-h successor behavioural types.

Concrete coefficient worlds include:

* N: exact successor multiplicity;
* Boolean: successor support/presence;
* Z/MZ: successor multiplicity modulo M;
* products such as Boolean x Z/MZ: retain several coefficient capabilities at
  once.

If ``phi:K->L`` is a semiring homomorphism, recursively map every child type,
map its coefficient by phi, and add coefficients whose richer child types
collapse to the same poorer child type. The result is exactly the directly
constructed L-branching signature. Hence coefficient morphisms induce natural
coarse maps of branching future signatures and the K-kernel always refines the
L-kernel.

Terminal word semantics is a second, independent fold: recursively multiply a
successor-type coefficient by the suffix trace and add over successor types.
This gives the usual K-valued path trace. Semiring morphisms commute with this
trace fold, producing a coefficient/structure commuting square.

A direct product semiring KxL is always a common refinement of the separate K
and L branching views, but need not be their **coarsest task join**. Its child
types pair K- and L-behaviour on the same successor and can therefore retain
cross-capability correlation that is absent when the two interfaces are stored
side by side independently.

Semiring-weighted automata, coalgebras, multiset functors and weighted
bisimulation are standard prior mathematics/CS. The project value is the exact
separation between local coefficient quotient, structural trace aggregation,
and cross-capability correlation introduced by a representation product.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Callable, Hashable, Mapping, Sequence

from .admissible_support import Relation
from .relation_support_stable_refinement import (
    Partition,
    normalize_partition,
    partition_refines,
)


State = Hashable
Action = Hashable
Observation = Hashable
Coefficient = Hashable


@dataclass(frozen=True)
class SemiringSpec:
    name: str
    zero: Coefficient
    one: Coefficient
    add: Callable[[Coefficient, Coefficient], Coefficient]
    mul: Callable[[Coefficient, Coefficient], Coefficient]

    def natural(self, value: int) -> Coefficient:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("natural coefficient source must be an integer")
        if value < 0:
            raise ValueError("natural coefficient source must be nonnegative")
        result = self.zero
        for _ in range(value):
            result = self.add(result, self.one)
        return result

    def sum(self, values: Sequence[Coefficient]) -> Coefficient:
        result = self.zero
        for value in values:
            result = self.add(result, value)
        return result


@dataclass(frozen=True)
class SemiringMorphism:
    name: str
    source: SemiringSpec
    target: SemiringSpec
    map_value: Callable[[Coefficient], Coefficient]


def natural_semiring() -> SemiringSpec:
    return SemiringSpec(
        name="N",
        zero=0,
        one=1,
        add=lambda left, right: int(left) + int(right),
        mul=lambda left, right: int(left) * int(right),
    )


def boolean_semiring() -> SemiringSpec:
    return SemiringSpec(
        name="B",
        zero=0,
        one=1,
        add=lambda left, right: int(bool(left) or bool(right)),
        mul=lambda left, right: int(bool(left) and bool(right)),
    )


def modular_semiring(modulus: int) -> SemiringSpec:
    if isinstance(modulus, bool) or not isinstance(modulus, int):
        raise TypeError("modulus must be an integer")
    if modulus <= 1:
        raise ValueError("modulus must exceed one")
    return SemiringSpec(
        name=f"Z/{modulus}Z",
        zero=0,
        one=1 % modulus,
        add=lambda left, right: (int(left) + int(right)) % modulus,
        mul=lambda left, right: (int(left) * int(right)) % modulus,
    )


def product_semiring(left: SemiringSpec, right: SemiringSpec) -> SemiringSpec:
    return SemiringSpec(
        name=f"{left.name}x{right.name}",
        zero=(left.zero, right.zero),
        one=(left.one, right.one),
        add=lambda a, b: (
            left.add(a[0], b[0]),
            right.add(a[1], b[1]),
        ),
        mul=lambda a, b: (
            left.mul(a[0], b[0]),
            right.mul(a[1], b[1]),
        ),
    )


def natural_to_boolean_morphism() -> SemiringMorphism:
    source = natural_semiring()
    target = boolean_semiring()
    return SemiringMorphism(
        name="positivity",
        source=source,
        target=target,
        map_value=lambda value: int(int(value) > 0),
    )


def natural_to_modular_morphism(modulus: int) -> SemiringMorphism:
    source = natural_semiring()
    target = modular_semiring(modulus)
    return SemiringMorphism(
        name=f"mod-{modulus}",
        source=source,
        target=target,
        map_value=lambda value: int(value) % modulus,
    )


def product_projection_left(
    left: SemiringSpec,
    right: SemiringSpec,
) -> SemiringMorphism:
    source = product_semiring(left, right)
    return SemiringMorphism(
        name=f"proj-{left.name}",
        source=source,
        target=left,
        map_value=lambda value: value[0],
    )


def product_projection_right(
    left: SemiringSpec,
    right: SemiringSpec,
) -> SemiringMorphism:
    source = product_semiring(left, right)
    return SemiringMorphism(
        name=f"proj-{right.name}",
        source=source,
        target=right,
        map_value=lambda value: value[1],
    )


def verify_semiring_morphism(
    morphism: SemiringMorphism,
    source_samples: Sequence[Coefficient],
) -> bool:
    samples = tuple(source_samples)
    if not samples:
        raise ValueError("morphism verification needs at least one source sample")
    phi = morphism.map_value
    source = morphism.source
    target = morphism.target
    if phi(source.zero) != target.zero:
        return False
    if phi(source.one) != target.one:
        return False
    for left in samples:
        for right in samples:
            if phi(source.add(left, right)) != target.add(phi(left), phi(right)):
                return False
            if phi(source.mul(left, right)) != target.mul(phi(left), phi(right)):
                return False
    return True


@dataclass(frozen=True)
class SemiringBranchingSignature:
    horizon: int
    observation: Observation
    successors: tuple[
        tuple[Action, frozenset[tuple["SemiringBranchingSignature", Coefficient]]],
        ...,
    ]

    def weights_for(
        self,
        action: Action,
    ) -> frozenset[tuple["SemiringBranchingSignature", Coefficient]]:
        for name, weights in self.successors:
            if name == action:
                return weights
        raise ValueError("action is not represented at this branching horizon")


def _states(values: Sequence[State]) -> tuple[State, ...]:
    result = tuple(values)
    if not result or len(set(result)) != len(result):
        raise ValueError("states must be a nonempty distinct sequence")
    return result


def _family(
    states: tuple[State, ...],
    relations: Mapping[Action, Relation],
) -> dict[Action, Relation]:
    if not relations:
        raise ValueError("relation family must be nonempty")
    state_set = set(states)
    result: dict[Action, Relation] = {}
    for name, relation in relations.items():
        if not isinstance(relation, frozenset):
            raise TypeError("every relation must be a frozenset of ordered pairs")
        if any(source not in state_set or target not in state_set for source, target in relation):
            raise ValueError("relation contains state outside declared state set")
        result[name] = relation
    return result


def semiring_branching_signature_map(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    horizon: int,
    semiring: SemiringSpec,
) -> dict[State, SemiringBranchingSignature]:
    order = _states(states)
    family = _family(order, relations)
    if isinstance(horizon, bool) or not isinstance(horizon, int):
        raise TypeError("horizon must be an integer")
    if horizon < 0:
        raise ValueError("horizon must be nonnegative")
    names = tuple(sorted(family, key=repr))

    current: dict[State, SemiringBranchingSignature] = {}
    for state in order:
        label = observation(state)
        hash(label)
        current[state] = SemiringBranchingSignature(
            horizon=0,
            observation=label,
            successors=(),
        )

    for level in range(1, horizon + 1):
        nxt: dict[State, SemiringBranchingSignature] = {}
        for state in order:
            action_weights = []
            for name in names:
                counts: dict[SemiringBranchingSignature, int] = {}
                for source, target in family[name]:
                    if source != state:
                        continue
                    child = current[target]
                    counts[child] = counts.get(child, 0) + 1
                sparse = []
                for child, count in counts.items():
                    coefficient = semiring.natural(count)
                    if coefficient != semiring.zero:
                        hash(coefficient)
                        sparse.append((child, coefficient))
                action_weights.append((name, frozenset(sparse)))
            nxt[state] = SemiringBranchingSignature(
                horizon=level,
                observation=current[state].observation,
                successors=tuple(action_weights),
            )
        current = nxt
    return current


def semiring_branching_partition(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    horizon: int,
    semiring: SemiringSpec,
) -> Partition:
    signatures = semiring_branching_signature_map(
        states,
        relations,
        observation,
        horizon,
        semiring,
    )
    groups: dict[SemiringBranchingSignature, set[State]] = {}
    for state, signature in signatures.items():
        groups.setdefault(signature, set()).add(state)
    return normalize_partition(tuple(groups.values()))


def joint_partition(left: Partition, right: Partition) -> Partition:
    """Coarsest state partition that refines both supplied partitions."""
    left_normalized = normalize_partition(left)
    right_normalized = normalize_partition(right)
    left_states = frozenset().union(*left_normalized)
    right_states = frozenset().union(*right_normalized)
    if left_states != right_states:
        raise ValueError("partitions must cover the same state set")
    left_block = {
        state: index
        for index, block in enumerate(left_normalized)
        for state in block
    }
    right_block = {
        state: index
        for index, block in enumerate(right_normalized)
        for state in block
    }
    groups: dict[tuple[int, int], set[State]] = {}
    for state in left_states:
        groups.setdefault(
            (left_block[state], right_block[state]),
            set(),
        ).add(state)
    return normalize_partition(tuple(groups.values()))


def _map_signature_recursive(
    signature: SemiringBranchingSignature,
    morphism: SemiringMorphism,
    memo: dict[SemiringBranchingSignature, SemiringBranchingSignature],
) -> SemiringBranchingSignature:
    if signature in memo:
        return memo[signature]
    if signature.horizon == 0:
        mapped = SemiringBranchingSignature(
            horizon=0,
            observation=signature.observation,
            successors=(),
        )
        memo[signature] = mapped
        return mapped

    target = morphism.target
    action_entries = []
    for action, weighted_children in signature.successors:
        accumulated: dict[SemiringBranchingSignature, Coefficient] = {}
        for child, coefficient in weighted_children:
            mapped_child = _map_signature_recursive(child, morphism, memo)
            mapped_weight = morphism.map_value(coefficient)
            previous = accumulated.get(mapped_child, target.zero)
            accumulated[mapped_child] = target.add(previous, mapped_weight)
        sparse = frozenset(
            (child, coefficient)
            for child, coefficient in accumulated.items()
            if coefficient != target.zero
        )
        action_entries.append((action, sparse))
    mapped = SemiringBranchingSignature(
        horizon=signature.horizon,
        observation=signature.observation,
        successors=tuple(action_entries),
    )
    memo[signature] = mapped
    return mapped


def map_branching_signature(
    signature: SemiringBranchingSignature,
    morphism: SemiringMorphism,
) -> SemiringBranchingSignature:
    return _map_signature_recursive(signature, morphism, {})


def morphism_commutes_with_branching_construction(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    horizon: int,
    morphism: SemiringMorphism,
) -> bool:
    order = _states(states)
    source = semiring_branching_signature_map(
        order,
        relations,
        observation,
        horizon,
        morphism.source,
    )
    target = semiring_branching_signature_map(
        order,
        relations,
        observation,
        horizon,
        morphism.target,
    )
    for state in order:
        if map_branching_signature(source[state], morphism) != target[state]:
            raise AssertionError("semiring morphism failed to commute with branching signature")
    return True


def morphism_source_partition_refines_target(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    horizon: int,
    morphism: SemiringMorphism,
) -> bool:
    source = semiring_branching_partition(
        states,
        relations,
        observation,
        horizon,
        morphism.source,
    )
    target = semiring_branching_partition(
        states,
        relations,
        observation,
        horizon,
        morphism.target,
    )
    if not partition_refines(source, target):
        raise AssertionError("richer coefficient branching failed to refine its morphic image")
    return True


def semiring_trace_from_branching_signature(
    signature: SemiringBranchingSignature,
    word: Sequence[Action],
    semiring: SemiringSpec,
) -> dict[Observation, Coefficient]:
    actions = tuple(word)
    if len(actions) > signature.horizon:
        raise ValueError("word exceeds branching signature horizon")
    if not actions:
        return {signature.observation: semiring.one}

    action = actions[0]
    suffix = actions[1:]
    result: dict[Observation, Coefficient] = {}
    for child, edge_weight in signature.weights_for(action):
        child_trace = semiring_trace_from_branching_signature(
            child,
            suffix,
            semiring,
        )
        for label, suffix_weight in child_trace.items():
            contribution = semiring.mul(edge_weight, suffix_weight)
            result[label] = semiring.add(
                result.get(label, semiring.zero),
                contribution,
            )
    return {
        label: coefficient
        for label, coefficient in result.items()
        if coefficient != semiring.zero
    }


def raw_semiring_word_trace(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    source: State,
    word: Sequence[Action],
    semiring: SemiringSpec,
) -> dict[Observation, Coefficient]:
    order = _states(states)
    family = _family(order, relations)
    if source not in order:
        raise ValueError("source lies outside declared state set")
    current: dict[State, Coefficient] = {source: semiring.one}
    for action in word:
        if action not in family:
            raise ValueError("word contains undeclared action")
        nxt: dict[State, Coefficient] = {}
        for state, state_weight in current.items():
            for left, target in family[action]:
                if left != state:
                    continue
                nxt[target] = semiring.add(
                    nxt.get(target, semiring.zero),
                    state_weight,
                )
        current = {
            state: coefficient
            for state, coefficient in nxt.items()
            if coefficient != semiring.zero
        }

    observed: dict[Observation, Coefficient] = {}
    for state, coefficient in current.items():
        label = observation(state)
        observed[label] = semiring.add(
            observed.get(label, semiring.zero),
            coefficient,
        )
    return {
        label: coefficient
        for label, coefficient in observed.items()
        if coefficient != semiring.zero
    }


def trace_projection_matches_raw_semiring_execution(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
    source: State,
    word: Sequence[Action],
    semiring: SemiringSpec,
) -> bool:
    signature = semiring_branching_signature_map(
        states,
        relations,
        observation,
        len(tuple(word)),
        semiring,
    )[source]
    projected = semiring_trace_from_branching_signature(signature, word, semiring)
    raw = raw_semiring_word_trace(
        states,
        relations,
        observation,
        source,
        word,
        semiring,
    )
    if projected != raw:
        raise AssertionError("branching trace fold disagreed with raw semiring execution")
    return True


def map_trace_coefficients(
    trace: Mapping[Observation, Coefficient],
    morphism: SemiringMorphism,
) -> dict[Observation, Coefficient]:
    target = morphism.target
    return {
        label: mapped
        for label, coefficient in trace.items()
        if (mapped := morphism.map_value(coefficient)) != target.zero
    }


def morphism_commutes_with_trace_fold(
    signature: SemiringBranchingSignature,
    word: Sequence[Action],
    morphism: SemiringMorphism,
) -> bool:
    source_trace = semiring_trace_from_branching_signature(
        signature,
        word,
        morphism.source,
    )
    mapped_signature = map_branching_signature(signature, morphism)
    target_trace = semiring_trace_from_branching_signature(
        mapped_signature,
        word,
        morphism.target,
    )
    mapped_trace = map_trace_coefficients(source_trace, morphism)
    if mapped_trace != target_trace:
        raise AssertionError("semiring morphism failed to commute with terminal trace fold")
    return True


def words_through_horizon(actions: Sequence[Action], horizon: int) -> tuple[tuple[Action, ...], ...]:
    if horizon < 0:
        raise ValueError("horizon must be nonnegative")
    names = tuple(actions)
    return tuple(
        word
        for length in range(horizon + 1)
        for word in product(names, repeat=length)
    )
