"""Asynchronous helper progress as the ideal lattice of a gate-dependency poset.

Fix a balanced binary conjunction compiler and assume all raw antecedents are
already present while helpers start absent.  Before the final output z fires,
allow one enabled helper gate to fire at a time.

The set of completed helpers is reachable iff it is an order ideal of the
helper dependency poset (helper prerequisite <= helper consumer).  Thus changing
scheduler semantics from synchronous parallel rounds to arbitrary asynchronous
helper firings changes runtime progress geometry from one path to an ideal
lattice / antichain-boundary state space.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations

from .balanced_binary_synergy import balanced_binary_synergy
from .closure_implication_bases import forward_chaining_trace


@dataclass(frozen=True)
class AsyncProgressReport:
    arity: int
    helper_count: int
    reachable_async_count: int
    ideal_count: int
    reachable_equals_ideals: bool
    helper_poset_width: int
    synchronous_preoutput_state_count: int
    synchronous_states: tuple[frozenset[str], ...]


def helper_predecessors(arity: int) -> dict[str, frozenset[str]]:
    compiler = balanced_binary_synergy(arity)
    helper_set = frozenset(compiler.helpers)
    predecessors: dict[str, frozenset[str]] = {}
    for rule in compiler.rules:
        if rule.root in helper_set:
            predecessors[rule.root] = frozenset(label for label in rule.premise if label in helper_set)
    if set(predecessors) != set(helper_set):
        raise AssertionError("every helper must have exactly one producing rule")
    return predecessors


def helper_ancestors(arity: int) -> dict[str, frozenset[str]]:
    predecessors = helper_predecessors(arity)
    memo: dict[str, frozenset[str]] = {}

    def ancestors(node: str) -> frozenset[str]:
        if node in memo:
            return memo[node]
        result: set[str] = set()
        for parent in predecessors[node]:
            result.add(parent)
            result.update(ancestors(parent))
        memo[node] = frozenset(result)
        return memo[node]

    for helper in predecessors:
        ancestors(helper)
    return memo


def _powerset(items: tuple[str, ...]):
    for size in range(len(items) + 1):
        for subset in combinations(items, size):
            yield frozenset(subset)


def helper_ideals(arity: int) -> tuple[frozenset[str], ...]:
    helpers = balanced_binary_synergy(arity).helpers
    ancestors = helper_ancestors(arity)
    ideals = []
    for subset in _powerset(helpers):
        if all(ancestors[helper].issubset(subset) for helper in subset):
            ideals.append(subset)
    return tuple(ideals)


def asynchronous_reachable_helper_sets(arity: int) -> tuple[frozenset[str], ...]:
    compiler = balanced_binary_synergy(arity)
    helper_set = frozenset(compiler.helpers)
    predecessors = helper_predecessors(arity)
    seen = {frozenset()}
    frontier = [frozenset()]
    while frontier:
        current = frontier.pop()
        for helper in compiler.helpers:
            if helper in current:
                continue
            if predecessors[helper].issubset(current):
                nxt = frozenset(set(current) | {helper})
                if nxt not in seen:
                    seen.add(nxt)
                    frontier.append(nxt)
    return tuple(sorted(seen, key=lambda state: (len(state), tuple(sorted(state)))))


def helper_poset_width(arity: int) -> int:
    helpers = balanced_binary_synergy(arity).helpers
    ancestors = helper_ancestors(arity)

    def comparable(left: str, right: str) -> bool:
        return left == right or left in ancestors[right] or right in ancestors[left]

    width = 0
    for subset in _powerset(helpers):
        items = tuple(subset)
        if all(not comparable(items[i], items[j]) for i in range(len(items)) for j in range(i + 1, len(items))):
            width = max(width, len(items))
    return width


def synchronous_preoutput_helper_states(arity: int) -> tuple[frozenset[str], ...]:
    compiler = balanced_binary_synergy(arity)
    raw_seed = frozenset(compiler.antecedents)
    helper_set = frozenset(compiler.helpers)
    trace = forward_chaining_trace(raw_seed, compiler.rules)
    states = []
    for state in trace:
        if compiler.root in state:
            break
        states.append(frozenset(label for label in state if label in helper_set))
    return tuple(states)


def asynchronous_progress_report(arity: int) -> AsyncProgressReport:
    if isinstance(arity, bool) or not isinstance(arity, int) or arity < 4:
        raise ValueError("arity must be an integer >= 4")
    compiler = balanced_binary_synergy(arity)
    reachable = set(asynchronous_reachable_helper_sets(arity))
    ideals = set(helper_ideals(arity))
    synchronous = synchronous_preoutput_helper_states(arity)
    return AsyncProgressReport(
        arity=arity,
        helper_count=len(compiler.helpers),
        reachable_async_count=len(reachable),
        ideal_count=len(ideals),
        reachable_equals_ideals=reachable == ideals,
        helper_poset_width=helper_poset_width(arity),
        synchronous_preoutput_state_count=len(synchronous),
        synchronous_states=synchronous,
    )
