"""Local relation contexts of binary code-generated E7/E8 primitive events.

Binary grade-four Construction-A primitive events have two visible construction
provenance sectors: coordinate-axis +/-2 events and weight-four codeword sign
lifts.  The current primitive relation graph need not preserve that historical
label.

For the [7,3,4] simplex/E7 construction all 126 primitive events, including 14
axis and 112 glue events, have link degree 32 and the same fixed-edge context:
32 common neighbors, a connected 15-regular common-neighbor graph with 240 edges.
For the extended [8,4,4] Hamming/E8 construction all 240 primitive events,
including 16 axis and 224 glue events, have link degree 56 and the same 56-vertex
27-regular / 756-edge context.

Thus at this local future-relation language the construction-sector label is
provenance rather than current geometry.  This is not a proof that all future
physical observations may forget that provenance.
"""

from __future__ import annotations

from collections import Counter, deque

from .causal_code_lattice import construction_a_primitive_events
from .causal_code_root_shadow import simplex_7_code
from .causal_code_lattice import extended_hamming_8_code

Vector = tuple[int, ...]
Context = tuple[int, int, tuple[int, ...], tuple[tuple[int, int], ...]]


def event_provenance(event: Vector) -> str:
    support = sum(value != 0 for value in event)
    if support == 1 and any(abs(value) == 2 for value in event):
        return "axis"
    return "glue"


def _difference(left: Vector, right: Vector) -> Vector:
    return tuple(a - b for a, b in zip(left, right))


def primitive_neighbors(events: set[Vector], event: Vector) -> tuple[Vector, ...]:
    if event not in events:
        raise ValueError("event must belong to primitive event set")
    return tuple(
        other
        for other in events
        if other != event and _difference(event, other) in events
    )


def primitive_edge_context(events: set[Vector], event: Vector) -> Context:
    common = primitive_neighbors(events, event)
    adjacency = {vertex: set() for vertex in common}
    edge_count = 0
    for index, left in enumerate(common):
        for right in common[index + 1 :]:
            if _difference(left, right) in events or _difference(right, left) in events:
                adjacency[left].add(right)
                adjacency[right].add(left)
                edge_count += 1

    unseen = set(common)
    components = []
    while unseen:
        seed = unseen.pop()
        queue = deque([seed])
        size = 1
        while queue:
            current = queue.popleft()
            for nxt in adjacency[current]:
                if nxt in unseen:
                    unseen.remove(nxt)
                    queue.append(nxt)
                    size += 1
        components.append(size)
    degree_hist = tuple(sorted(Counter(len(adjacency[v]) for v in common).items()))
    return len(common), edge_count, tuple(sorted(components, reverse=True)), degree_hist


def provenance_context_histogram(codewords) -> dict[tuple[str, int, Context], int]:
    events = construction_a_primitive_events(codewords)
    counts = Counter()
    for event in events:
        counts[(event_provenance(event), len(primitive_neighbors(events, event)), primitive_edge_context(events, event))] += 1
    return dict(counts)


def e7_provenance_context_histogram():
    return provenance_context_histogram(simplex_7_code())


def e8_provenance_context_histogram():
    return provenance_context_histogram(extended_hamming_8_code())


def local_context_forgets_provenance(codewords) -> bool:
    histogram = provenance_context_histogram(codewords)
    relation_signatures = {(degree, context) for (_, degree, context) in histogram}
    provenances = {provenance for (provenance, _, _) in histogram}
    return len(provenances) > 1 and len(relation_signatures) == 1
