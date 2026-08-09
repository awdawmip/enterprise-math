"""Exact integer E6 primitive geometry from three hexagonal local cells.

Each local A2/hexagonal cell is represented in fundamental-weight coordinates
(u,v) in Z^2.  The root-lattice residue is r=u-v mod 3 and the integer-normalized
quadratic grade is

    q_hex(u,v)=u^2+u*v+v^2.

The zero residue sector has six minimum nonzero grade-three roots.  Each nonzero
residue sector has three grade-one minimum representatives.  Three local cells
are glued by the ternary repetition constraint r_1=r_2=r_3.  Minimum global
grade three then contains 18 local roots plus 54 repetition-sector lifts, for 72
primitive events.

Adjacency of primitive directions is defined causally by closure of the primitive
event grammar: alpha~beta iff alpha-beta is another primitive event.  Direct
integer enumeration gives a uniform first-link degree 20 and a uniform fixed-edge
common-neighbor graph with 20 vertices, degree 9, and 90 internal edges, matching
the traditional simply-laced E6 root geometry shadow.
"""

from __future__ import annotations

from collections import Counter, deque
from itertools import product

Local = tuple[int, int]
Event = tuple[int, int, int, int, int, int]
Context = tuple[int, int, tuple[int, ...], tuple[tuple[int, int], ...]]


def hex_residue(local: Local) -> int:
    return (local[0] - local[1]) % 3


def hex_grade(local: Local) -> int:
    u, v = local
    return u * u + u * v + v * v


def local_minimum_representatives(residue: int) -> tuple[Local, ...]:
    if residue not in (0, 1, 2):
        raise ValueError("residue must lie in Z/3Z")
    candidates = [
        (u, v)
        for u in range(-3, 4)
        for v in range(-3, 4)
        if (u, v) != (0, 0) or residue != 0
        if hex_residue((u, v)) == residue
    ]
    if residue == 0:
        candidates = [local for local in candidates if local != (0, 0)]
    minimum = min(hex_grade(local) for local in candidates)
    return tuple(sorted(local for local in candidates if hex_grade(local) == minimum))


def local_hex_profile() -> dict[int, tuple[int, int]]:
    return {
        residue: (
            hex_grade(local_minimum_representatives(residue)[0]),
            len(local_minimum_representatives(residue)),
        )
        for residue in (0, 1, 2)
    }


def _flatten(locals_: tuple[Local, Local, Local]) -> Event:
    return tuple(value for local in locals_ for value in local)  # type: ignore[return-value]


def e6_primitive_events() -> tuple[Event, ...]:
    zero_roots = local_minimum_representatives(0)
    residue_one = local_minimum_representatives(1)
    residue_two = local_minimum_representatives(2)
    zero = (0, 0)
    events = set()

    for slot in range(3):
        for root in zero_roots:
            locals_ = [zero, zero, zero]
            locals_[slot] = root
            events.add(_flatten(tuple(locals_)))

    for representatives in (residue_one, residue_two):
        for choices in product(representatives, repeat=3):
            events.add(_flatten(tuple(choices)))

    if len(events) != 72:
        raise AssertionError("ternary hex repetition construction must yield 72 primitive events")
    return tuple(sorted(events))


def e6_event_grade(event: Event) -> int:
    return sum(hex_grade((event[index], event[index + 1])) for index in (0, 2, 4))


def event_difference(left: Event, right: Event) -> Event:
    return tuple(a - b for a, b in zip(left, right))  # type: ignore[return-value]


def e6_adjacent(left: Event, right: Event) -> bool:
    if left == right:
        return False
    return event_difference(left, right) in set(e6_primitive_events())


def e6_link_neighbors(event: Event) -> tuple[Event, ...]:
    events = e6_primitive_events()
    if event not in events:
        raise ValueError("event must be an E6 primitive event")
    event_set = set(events)
    return tuple(
        other
        for other in events
        if other != event and event_difference(event, other) in event_set
    )


def e6_link_degree_set() -> tuple[int, ...]:
    return tuple(sorted({len(e6_link_neighbors(event)) for event in e6_primitive_events()}))


def e6_edge_context(event: Event) -> Context:
    common = e6_link_neighbors(event)
    event_set = set(e6_primitive_events())
    adjacency = {vertex: set() for vertex in common}
    edge_count = 0
    for index, left in enumerate(common):
        for right in common[index + 1 :]:
            if event_difference(left, right) in event_set or event_difference(right, left) in event_set:
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


def e6_all_edge_contexts_uniform() -> bool:
    return len({e6_edge_context(event) for event in e6_primitive_events()}) == 1
