#!/usr/bin/env python3
"""R8: finite typed Boolean-BRC one-shot triadic/Port overlap certificate.
Conditional candidate: three ordered nonzero signed +axis tokens as a preserved triad,
source/target occupancy guards, and only one original-source exit per episode.
No physical/native event-admission claim or signed-force numerical cancellation.
"""
from itertools import permutations
import json

D = 6
ZERO = (0,) * D


def shift(cell, axis):
    nxt = list(cell)
    nxt[axis] += 1
    return tuple(nxt)


def difference_cell(axis_i, axis_j):
    x = [0] * D
    x[axis_i] += 1
    x[axis_j] -= 1
    return tuple(x)


def one_shot(state, identity, slot, frame, source_cells):
    """Typed BRC labelled source-port append: preserves ordered triad + occupancy.

    state=(occupied Cell->(original-source-id, ordered force tokens), moved-id-set)
    The derived one-shot episode never reactivates moved sources; this is narrower
    than a model that allows relocated triads to emit again.
    """
    occupancy, moved = state
    if identity in moved:
        return None
    origin = source_cells[identity]
    tokens = (identity, tuple((axis, '+', slot_id) for slot_id, axis in enumerate(frame)))
    if occupancy.get(origin) != tokens:
        return None
    target = shift(origin, frame[slot])
    if target in occupancy:
        return None
    nxt = dict(occupancy)
    nxt.pop(origin)
    nxt[target] = tokens
    return nxt, frozenset(moved | {identity})


def first_layer(frame, d):
    cells = {'A': ZERO, 'B': d}
    initial = ({c: (identity, tuple((axis, '+', slot_id)
                                  for slot_id, axis in enumerate(frame)))
                for identity, c in cells.items()}, frozenset())
    histories = {}
    for r in range(3):
        after = one_shot(initial, 'A', r, frame, cells)
        assert after is not None
        future = frozenset(('B', s) for s in range(3)
                           if one_shot(after, 'B', s, frame, cells) is not None)
        histories[r] = future
        assert one_shot(after, 'A', r, frame, cells) is None
        assert len(after[0]) == 2
        assert len(after[1]) == 1
    # All three histories have identical source-event counts (1,0) and quota.
    return histories


def check_future_safe_quotient(frame, d):
    """All reachable one-shot branches: (remaining sources, relevant occupied targets)."""
    cells = {'A': ZERO, 'B': d}
    tokens = lambda identity: (identity, tuple((axis, '+', t)
                                                for t, axis in enumerate(frame)))
    initial = ({c: tokens(identity) for identity, c in cells.items()}, frozenset())
    alphabet = tuple((name, slot) for name in cells for slot in range(3))

    def projection(state):
        occupancy, moved = state
        remaining = frozenset(name for name in cells if name not in moved)
        remaining_targets = {shift(cells[name], frame[slot])
                             for name in remaining for slot in range(3)}
        moved_destinations = {cell for cell, (name, _tokens) in occupancy.items()
                              if name in moved}
        return remaining, frozenset(moved_destinations & remaining_targets)

    def abstract_step(abstraction, name, slot):
        remaining, relevant = abstraction
        if name not in remaining:
            return None
        destination = shift(cells[name], frame[slot])
        if destination in relevant or destination in {cells[z] for z in remaining}:
            return None
        updated_remaining = remaining - {name}
        later_targets = {shift(cells[z], frame[r])
                         for z in updated_remaining for r in range(3)}
        return updated_remaining, frozenset((relevant | {destination}) & later_targets)

    frontier = [initial]
    visited = {(tuple(sorted(initial[0].items())), tuple(sorted(initial[1])))}
    transitions = 0
    while frontier:
        state = frontier.pop()
        quotient = projection(state)
        for name, slot in alphabet:
            real = one_shot(state, name, slot, frame, cells)
            estimated = abstract_step(quotient, name, slot)
            assert (real is None) == (estimated is None)
            if real is not None:
                assert projection(real) == estimated
                transitions += 1
                # Occupancy dictionaries are unhashable, use canonical typed key.
                key = (tuple(sorted(real[0].items())), tuple(sorted(real[1])))
                if key not in visited:
                    visited.add(key)
                    frontier.append(real)
    return transitions


def run():
    tests = 0
    overlap_histories = 0
    disjoint_checks = 0
    quotient_transitions = 0
    for frame in permutations(range(D), 3):
        remote = (10, 0, 0, 0, 0, 0)
        far = first_layer(frame, remote)
        assert len(set(far.values())) == 1
        assert all(len(lang) == 3 for lang in far.values())
        disjoint_checks += 1
        quotient_transitions += check_future_safe_quotient(frame, remote)
        for r in range(3):
            for s in range(3):
                if r == s:
                    continue
                d = difference_cell(frame[r], frame[s])
                assert d != ZERO
                langs = first_layer(frame, d)
                full = frozenset(('B', j) for j in range(3))
                one_blocked = full - {('B', s)}
                assert langs[r] == one_blocked
                assert all(langs[q] == full for q in range(3) if q != r)
                assert len(set(langs.values())) == 2
                assert len({w for w in langs.values()}) == 2
                tests += 1
                overlap_histories += len(langs)
                quotient_transitions += check_future_safe_quotient(frame, d)
    return {
        'schema': 'X6_TRIADIC_ONE_SHOT_PORT_OVERLAP_R8_V1',
        'status': 'PASS',
        'frames': 120,
        'distinct_shared_target_offsets_per_frame': 6,
        'overlap_models_checked': tests,
        'overlap_first_event_histories_checked': overlap_histories,
        'disjoint_frame_checks': disjoint_checks,
        'quotient_transition_checks': quotient_transitions,
        'overlap_future_language_classes_at_same_source_counts': 2,
        'information_to_restore_future_languages_bits': 1,
        'boolean_BRC_carrier': 'ordered (source_id,port_id) branch, occupied native-X6 Cell -> ordered signed-positive triad tokens, one-shot moved-source ledger',
        'scope': 'declared guarded one-shot triadic relocation; no native physical admission, no signed amplitude, no unrestricted future recurrence'
    }


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True, ensure_ascii=False))
