"""Constraint relaxation can either enrich or replace the primitive geometry shell.

For a fixed binary integer local alphabet, enlarging a residue code weakens the
conservation constraints.  The minimum nonzero code lift grade can only stay the
same or decrease.

If the primitive grade stays unchanged, old primitive events remain primitive
and the shell expands monotonically.  If the grade drops, newly allowed smaller
events define a new primitive shell; old events remain legal but move to higher
grade.  Thus weaker conservation does not imply monotone primitive coordination.

An explicit length-eight chain inside the extended-Hamming/even-parity family:

    C2 subset C3 subset C4=extended Hamming subset C_even

has primitive profiles 48 -> 112 -> 240 at grade four, followed by a drop to
112 primitive grade-two D8 events when all even-parity weight-two sectors are
allowed.  The first C2 event graph has two 24-event components; C3 and C4 are
connected with link degrees 24 and 56.
"""

from __future__ import annotations

from collections import deque

from .causal_code_event_context import primitive_neighbors
from .causal_code_lattice import (
    binary_span,
    construction_a_primitive_events,
    construction_a_primitive_grade,
    even_parity_code,
    extended_hamming_8_code,
)

Code = tuple[tuple[int, ...], ...]
Vector = tuple[int, ...]


def _all_ones(length: int) -> tuple[int, ...]:
    return (1,) * length


def e8_nested_subcodes() -> tuple[Code, Code, Code, Code]:
    full = extended_hamming_8_code()
    weight_four = [word for word in full if sum(word) == 4]
    ones = _all_ones(8)
    first = weight_four[0]
    c2 = binary_span((ones, first))
    second = next(word for word in weight_four[1:] if word not in c2)
    c3 = binary_span((ones, first, second))
    c4 = full
    even = even_parity_code(8)
    if not (set(c2) < set(c3) < set(c4) < set(even)):
        raise AssertionError("expected strict nested binary conservation-code chain")
    return c2, c3, c4, even


def primitive_profile(code: Code) -> tuple[int, int, tuple[int, ...]]:
    events = construction_a_primitive_events(code)
    degrees = tuple(sorted({len(primitive_neighbors(events, event)) for event in events}))
    return construction_a_primitive_grade(code), len(events), degrees


def primitive_graph_component_sizes(code: Code) -> tuple[int, ...]:
    events = construction_a_primitive_events(code)
    unseen = set(events)
    sizes = []
    while unseen:
        seed = unseen.pop()
        queue = deque([seed])
        size = 1
        while queue:
            current = queue.popleft()
            for nxt in primitive_neighbors(events, current):
                if nxt in unseen:
                    unseen.remove(nxt)
                    queue.append(nxt)
                    size += 1
        sizes.append(size)
    return tuple(sorted(sizes, reverse=True))


def relaxation_preserves_primitive_shell(old_code: Code, new_code: Code) -> bool:
    if not set(old_code) <= set(new_code):
        raise ValueError("new code must be a relaxation/superset of old code")
    old_grade = construction_a_primitive_grade(old_code)
    new_grade = construction_a_primitive_grade(new_code)
    if new_grade != old_grade:
        return False
    return construction_a_primitive_events(old_code) <= construction_a_primitive_events(new_code)


def relaxation_lowers_primitive_grade(old_code: Code, new_code: Code) -> bool:
    if not set(old_code) <= set(new_code):
        raise ValueError("new code must contain old code")
    return construction_a_primitive_grade(new_code) < construction_a_primitive_grade(old_code)


def e8_relaxation_profiles() -> tuple[tuple[int, int, tuple[int, ...]], ...]:
    return tuple(primitive_profile(code) for code in e8_nested_subcodes())
