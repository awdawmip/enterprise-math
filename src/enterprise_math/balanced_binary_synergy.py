"""Optimal binary-helper compilation for a pure k-way conjunction.

For raw antecedents a_1,...,a_k and output z, a sound binary positive-Horn
compiler whose output genuinely depends on all k raw inputs needs:

* at least k-1 derived gates in an ancestor proof DAG, hence at least k-2
  auxiliary labels besides z;
* derivation depth at least ceil(log2 k), since one binary gate at depth t can
  depend on at most 2^t raw sources.

A balanced reduction tree attains both bounds simultaneously with k-1 rules,
k-2 helpers, maximum premise arity two, and depth ceil(log2 k).

These are classical fan-in-two circuit facts, packaged here for P025 precision
accounting.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import ceil, log2

from .closure_implication_bases import Implication, forward_chaining_trace
from .closure_helper_state_boundary import pure_synergy_states
from .closure_implication_circuits import closure_of


@dataclass(frozen=True)
class BalancedBinarySynergy:
    arity: int
    antecedents: tuple[str, ...]
    helpers: tuple[str, ...]
    root: str
    labels: tuple[str, ...]
    rules: tuple[Implication, ...]
    depth: int
    helper_lower_bound: int
    depth_lower_bound: int
    raw_projection_verified: bool


def balanced_binary_synergy(arity: int) -> BalancedBinarySynergy:
    if isinstance(arity, bool) or not isinstance(arity, int) or arity < 2:
        raise ValueError("arity must be an integer >= 2")

    antecedents = tuple(f"a{i}" for i in range(1, arity + 1))
    root = "z"
    next_helper = 1
    helpers: list[str] = []
    rules: list[Implication] = []
    current = list(antecedents)

    # Reduce the live signal list by maximum parallel pairing each round.
    while len(current) > 2:
        nxt: list[str] = []
        index = 0
        while index + 1 < len(current):
            helper = f"h{next_helper}"
            next_helper += 1
            helpers.append(helper)
            rules.append(Implication(frozenset({current[index], current[index + 1]}), helper))
            nxt.append(helper)
            index += 2
        if index < len(current):
            nxt.append(current[index])
        current = nxt

    rules.append(Implication(frozenset(current), root))
    labels = antecedents + tuple(helpers) + (root,)
    rule_tuple = tuple(rules)
    trace = forward_chaining_trace(frozenset(antecedents), rule_tuple)
    depth = len(trace) - 1

    raw_labels, raw_states = pure_synergy_states(arity)
    raw_label_set = frozenset(raw_labels)
    raw_projection_verified = True

    # Exhaust raw seeds without materializing helper coordinates in the input.
    from itertools import combinations

    for size in range(len(raw_labels) + 1):
        for subset in combinations(raw_labels, size):
            seed = frozenset(subset)
            expected = closure_of(raw_labels, raw_states, seed)
            final = forward_chaining_trace(seed, rule_tuple)[-1]
            projected = frozenset(label for label in final if label in raw_label_set)
            if projected != expected:
                raw_projection_verified = False
                break
        if not raw_projection_verified:
            break

    lower_depth = ceil(log2(arity))
    if len(helpers) != arity - 2:
        raise AssertionError("balanced binary tree must use exactly k-2 helper labels")
    if len(rules) != arity - 1:
        raise AssertionError("balanced binary tree must use exactly k-1 rules")
    if depth != lower_depth:
        raise AssertionError("balanced binary tree must attain ceil(log2 k) depth")

    return BalancedBinarySynergy(
        arity=arity,
        antecedents=antecedents,
        helpers=tuple(helpers),
        root=root,
        labels=labels,
        rules=rule_tuple,
        depth=depth,
        helper_lower_bound=arity - 2,
        depth_lower_bound=lower_depth,
        raw_projection_verified=raw_projection_verified,
    )
