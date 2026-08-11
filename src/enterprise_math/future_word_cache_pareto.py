"""Storage/execution-depth Pareto for cached finite future-operation words.

Fix k named total deterministic action generators and a declared word horizon H.
If every literal word effect of length 1..d is cached, any word of length h<=H
can be split into consecutive blocks of length at most d and executed in

    ceil(h/d)

cached-operation rounds.

Literal cache storage is

    S(k,d)=sum_{i=1}^d k^i.

Within this block-cache model the round bound is optimal: one cached primitive
consumes at most d input symbols, so a length-h word needs at least ceil(h/d)
primitives.

For a desired worst-case round budget r at horizon H, the least admissible cache
depth is therefore

    d_min=ceil(H/r),

and because literal storage grows strictly with d, this also gives the minimum
literal-cache storage for that round budget.

The module additionally computes actual unique transformation effects on a
finite state set.  This separates two storage notions:

* literal table entries -- one key per word;
* distinct semantic effects -- several words may induce one operation.

A prefix-append finite fixture realizes all word effects through a chosen cache
depth distinctly, making the literal storage bound sharp.  Systems with
algebraic/behavioral word normal forms can have much smaller semantic effect
sets, but exploiting that collapse requires a word-to-normal-form compiler whose
cost belongs to a separate resource axis.

Time-memory tradeoffs, transformation semigroups and block caching are standard
prior CS/algebra.  The Enterprise Math value is the Stage131 precision-law
interpretation: one exact future law admits a continuum of storage/runtime
representations even after semantic exactness is fixed.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Hashable, Mapping, Sequence


State = Hashable
Action = Hashable
Transformation = tuple[int, ...]


def literal_word_count(action_count: int, cache_depth: int) -> int:
    if isinstance(action_count, bool) or not isinstance(action_count, int) or action_count < 1:
        raise ValueError("action_count must be a positive integer")
    if isinstance(cache_depth, bool) or not isinstance(cache_depth, int) or cache_depth < 1:
        raise ValueError("cache_depth must be a positive integer")
    if action_count == 1:
        return cache_depth
    return action_count * (action_count**cache_depth - 1) // (action_count - 1)


def cache_execution_rounds(word_length: int, cache_depth: int) -> int:
    if isinstance(word_length, bool) or not isinstance(word_length, int) or word_length < 0:
        raise ValueError("word_length must be a nonnegative integer")
    if isinstance(cache_depth, bool) or not isinstance(cache_depth, int) or cache_depth < 1:
        raise ValueError("cache_depth must be a positive integer")
    if word_length == 0:
        return 0
    return (word_length + cache_depth - 1) // cache_depth


def minimum_cache_depth_for_round_budget(horizon: int, round_budget: int) -> int:
    if isinstance(horizon, bool) or not isinstance(horizon, int) or horizon < 1:
        raise ValueError("horizon must be a positive integer")
    if isinstance(round_budget, bool) or not isinstance(round_budget, int) or round_budget < 1:
        raise ValueError("round_budget must be a positive integer")
    effective_rounds = min(round_budget, horizon)
    return (horizon + effective_rounds - 1) // effective_rounds


def minimum_literal_storage_for_round_budget(
    action_count: int,
    horizon: int,
    round_budget: int,
) -> int:
    depth = minimum_cache_depth_for_round_budget(horizon, round_budget)
    return literal_word_count(action_count, depth)


def words_of_length(actions: Sequence[Action], length: int) -> tuple[tuple[Action, ...], ...]:
    names = tuple(actions)
    if not names or len(set(names)) != len(names):
        raise ValueError("actions must be a nonempty distinct sequence")
    if isinstance(length, bool) or not isinstance(length, int) or length < 0:
        raise ValueError("length must be nonnegative")
    return tuple(product(names, repeat=length))


def words_through_depth(actions: Sequence[Action], depth: int) -> tuple[tuple[Action, ...], ...]:
    if isinstance(depth, bool) or not isinstance(depth, int) or depth < 1:
        raise ValueError("depth must be positive")
    names = tuple(actions)
    return tuple(
        word
        for length in range(1, depth + 1)
        for word in words_of_length(names, length)
    )


def block_decompose_word(word: Sequence[Action], cache_depth: int) -> tuple[tuple[Action, ...], ...]:
    values = tuple(word)
    if isinstance(cache_depth, bool) or not isinstance(cache_depth, int) or cache_depth < 1:
        raise ValueError("cache_depth must be positive")
    return tuple(
        values[index : index + cache_depth]
        for index in range(0, len(values), cache_depth)
    )


def _validated_operations(
    states: Sequence[State],
    operations: Mapping[Action, Mapping[State, State]],
) -> tuple[tuple[State, ...], tuple[Action, ...], dict[Action, dict[State, State]]]:
    order = tuple(states)
    if not order or len(set(order)) != len(order):
        raise ValueError("states must be nonempty and distinct")
    names = tuple(operations)
    if not names or len(set(names)) != len(names):
        raise ValueError("operation names must be nonempty and distinct")
    state_set = set(order)
    family: dict[Action, dict[State, State]] = {}
    for name in names:
        mapping = dict(operations[name])
        if set(mapping) != state_set:
            raise ValueError("every operation must be total on the state set")
        if any(target not in state_set for target in mapping.values()):
            raise ValueError("operation target outside state set")
        family[name] = mapping
    return order, names, family


def word_transformation(
    states: Sequence[State],
    operations: Mapping[Action, Mapping[State, State]],
    word: Sequence[Action],
) -> Transformation:
    order, names, family = _validated_operations(states, operations)
    index = {state: position for position, state in enumerate(order)}
    name_set = set(names)
    values = tuple(word)
    if any(action not in name_set for action in values):
        raise ValueError("word contains undeclared action")
    outputs = []
    for source in order:
        current = source
        for action in values:
            current = family[action][current]
        outputs.append(index[current])
    return tuple(outputs)


def compose_transformations(left: Transformation, right: Transformation) -> Transformation:
    """Apply left first, then right."""
    if len(left) != len(right) or not left:
        raise ValueError("transformations must share one positive state dimension")
    size = len(left)
    if any(not 0 <= value < size for value in left + right):
        raise ValueError("transformation contains invalid state index")
    return tuple(right[left[index]] for index in range(size))


def cached_word_effects(
    states: Sequence[State],
    operations: Mapping[Action, Mapping[State, State]],
    cache_depth: int,
) -> dict[tuple[Action, ...], Transformation]:
    order, names, family = _validated_operations(states, operations)
    return {
        word: word_transformation(order, family, word)
        for word in words_through_depth(names, cache_depth)
    }


def execute_from_cache(
    states: Sequence[State],
    operations: Mapping[Action, Mapping[State, State]],
    word: Sequence[Action],
    cache_depth: int,
) -> Transformation:
    order, _names, family = _validated_operations(states, operations)
    cache = cached_word_effects(order, family, cache_depth)
    blocks = block_decompose_word(word, cache_depth)
    identity = tuple(range(len(order)))
    result = identity
    for block in blocks:
        if block not in cache:
            raise AssertionError("block cache omitted required literal block")
        result = compose_transformations(result, cache[block])
    direct = word_transformation(order, family, word)
    if result != direct:
        raise AssertionError("cached block execution disagreed with literal word")
    return result


def unique_effect_count(
    states: Sequence[State],
    operations: Mapping[Action, Mapping[State, State]],
    cache_depth: int,
) -> int:
    cache = cached_word_effects(states, operations, cache_depth)
    return len(set(cache.values()))


@dataclass(frozen=True)
class WordCacheParetoPoint:
    action_count: int
    horizon: int
    cache_depth: int
    literal_cache_entries: int
    worst_case_execution_rounds: int


def word_cache_pareto_point(action_count: int, horizon: int, cache_depth: int) -> WordCacheParetoPoint:
    if isinstance(horizon, bool) or not isinstance(horizon, int) or horizon < 1:
        raise ValueError("horizon must be positive")
    if not 1 <= cache_depth <= horizon:
        raise ValueError("cache_depth must lie in 1..horizon")
    return WordCacheParetoPoint(
        action_count=action_count,
        horizon=horizon,
        cache_depth=cache_depth,
        literal_cache_entries=literal_word_count(action_count, cache_depth),
        worst_case_execution_rounds=cache_execution_rounds(horizon, cache_depth),
    )


def cache_point_dominates(left: WordCacheParetoPoint, right: WordCacheParetoPoint) -> bool:
    weak = (
        left.literal_cache_entries <= right.literal_cache_entries
        and left.worst_case_execution_rounds <= right.worst_case_execution_rounds
    )
    strict = (
        left.literal_cache_entries < right.literal_cache_entries
        or left.worst_case_execution_rounds < right.worst_case_execution_rounds
    )
    return weak and strict


def word_cache_pareto_frontier(action_count: int, horizon: int) -> tuple[WordCacheParetoPoint, ...]:
    points = tuple(
        word_cache_pareto_point(action_count, horizon, depth)
        for depth in range(1, horizon + 1)
    )
    frontier = tuple(
        point
        for point in points
        if not any(
            cache_point_dominates(other, point)
            for other in points
            if other != point
        )
    )
    return tuple(sorted(frontier, key=lambda point: point.cache_depth))


def prefix_append_free_effect_fixture(
    action_count: int,
    depth: int,
) -> tuple[
    tuple[object, ...],
    dict[int, dict[object, object]],
]:
    """Finite fixture where every literal word through ``depth`` has distinct effect.

    States are all action words of length<=depth plus one absorbing overflow
    marker.  Action a appends symbol a while capacity remains, otherwise enters
    overflow.  Different words w of length<=depth send the empty state to
    different prefix states, so their transformations are distinct.
    """
    if isinstance(action_count, bool) or not isinstance(action_count, int) or action_count < 1:
        raise ValueError("action_count must be positive")
    if isinstance(depth, bool) or not isinstance(depth, int) or depth < 1:
        raise ValueError("depth must be positive")
    actions = tuple(range(action_count))
    word_states = tuple(
        word
        for length in range(depth + 1)
        for word in product(actions, repeat=length)
    )
    overflow = ("OVERFLOW", depth)
    states: tuple[object, ...] = (*word_states, overflow)
    operations: dict[int, dict[object, object]] = {}
    for action in actions:
        mapping: dict[object, object] = {}
        for state in states:
            if state == overflow:
                mapping[state] = overflow
            elif isinstance(state, tuple) and len(state) < depth:
                mapping[state] = (*state, action)
            else:
                mapping[state] = overflow
        operations[action] = mapping
    return states, operations


def free_fixture_hits_literal_storage_bound(action_count: int, depth: int) -> bool:
    states, operations = prefix_append_free_effect_fixture(action_count, depth)
    unique = unique_effect_count(states, operations, depth)
    expected = literal_word_count(action_count, depth)
    if unique != expected:
        raise AssertionError("free-prefix fixture failed distinct word-effect bound")
    return True
