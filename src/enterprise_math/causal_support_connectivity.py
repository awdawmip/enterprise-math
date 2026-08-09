"""Connectivity of resonant code-generated primitive geometry from glue supports.

In a binary grade-four resonance construction, local axis primitive events live
at coordinates and weight-four codeword lifts glue four coordinates at a time.
The minimum-support hypergraph has coordinates as vertices and weight-four
codeword supports as hyperedges.

If every coordinate occurs in at least one minimum support, the primitive event
graph is connected exactly when this support hypergraph is connected.  A support
component cannot communicate with another because no primitive glue spans them;
within a connected support component, sign lifts provide paths linking the local
axis channels across every overlapping hyperedge.

This gives a causal shadow of root-system irreducibility/direct-sum structure.
"""

from __future__ import annotations

from collections import deque

from .causal_code_lattice import hamming_weight

Support = frozenset[int]


def minimum_weight_supports(codewords) -> tuple[Support, ...]:
    nonzero = [word for word in codewords if any(word)]
    if not nonzero:
        return ()
    minimum = min(hamming_weight(word) for word in nonzero)
    return tuple(
        frozenset(index for index, bit in enumerate(word) if bit)
        for word in nonzero
        if hamming_weight(word) == minimum
    )


def support_hypergraph_components(slot_count: int, supports: tuple[Support, ...]) -> tuple[tuple[int, ...], ...]:
    if slot_count < 1:
        raise ValueError("slot_count must be positive")
    adjacency = {index: set() for index in range(slot_count)}
    for support in supports:
        for left in support:
            for right in support:
                if left != right:
                    adjacency[left].add(right)
    unseen = set(range(slot_count))
    components = []
    while unseen:
        seed = unseen.pop()
        queue = deque([seed])
        component = {seed}
        while queue:
            current = queue.popleft()
            for nxt in adjacency[current]:
                if nxt in unseen:
                    unseen.remove(nxt)
                    component.add(nxt)
                    queue.append(nxt)
        components.append(tuple(sorted(component)))
    return tuple(sorted(components, key=lambda component: (len(component), component), reverse=True))


def every_slot_is_glued(slot_count: int, supports: tuple[Support, ...]) -> bool:
    covered = set().union(*supports) if supports else set()
    return covered == set(range(slot_count))


def support_hypergraph_connected(slot_count: int, supports: tuple[Support, ...]) -> bool:
    return len(support_hypergraph_components(slot_count, supports)) == 1
