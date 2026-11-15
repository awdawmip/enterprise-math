#!/usr/bin/env python3
"""Exact finite V17 frame / axis-exchange ledger census, integer-only.
The axis-context transfer observer is a conditional V29-style bridge, not a
native signed TRIADIC_CLOSURE_E Cell/Link/Port event predicate.
"""
import json
from collections import Counter, defaultdict
from itertools import combinations

U = (1, 2, 3, 4, 5, 6)
BASE = (1, 2, 3)
ARCS = tuple((a, b) for a in U for b in U if a != b)
ARC_IDX = {arc: k for k, arc in enumerate(ARCS)}
EDGES = tuple(combinations(U, 2))
ZERO = (0,) * len(ARCS)

def successors(frame):
    used = set(frame)
    for pos in range(3):
        old = frame[pos]
        for new in U:
            if new not in used:
                nxt = list(frame)
                nxt[pos] = new
                yield tuple(nxt), (old, new)

def flux(hist):
    return tuple(hist[ARC_IDX[a, b]] - hist[ARC_IDX[b, a]] for a, b in EDGES)

def arc_history(path):
    out = []
    for f, g in zip(path, path[1:]):
        changed = [i for i in range(3) if f[i] != g[i]]
        assert len(changed) == 1
        pos = changed[0]
        assert g[pos] not in f
        out.append((f[pos], g[pos]))
    return out

def hist_from_path(path):
    h = [0] * 30
    for e in arc_history(path):
        h[ARC_IDX[e]] += 1
    return tuple(h)

def run():
    five_identity = ((1,2,3),(4,2,3),(1,2,3),(1,4,3),(1,5,3),(1,2,3))
    five_swap = ((1,2,3),(4,2,3),(5,2,3),(5,4,3),(2,4,3),(2,1,3))
    six_zero_current_swap = ((1,2,3),(4,2,3),(5,2,3),(5,4,3),(5,1,3),(4,1,3),(2,1,3))
    assert hist_from_path(five_identity) == hist_from_path(five_swap)
    assert five_identity[-1] != five_swap[-1]
    assert all(v == 0 for v in flux(hist_from_path(six_zero_current_swap)))
    assert six_zero_current_swap[-1] != BASE
    assert len(arc_history(five_identity)) == 5
    assert len(arc_history(six_zero_current_swap)) == 6

    # Exact multiplicity is added only on a complete frame-plus-histogram key.
    states = {(BASE, ZERO): 1}
    result = []
    for length in range(7):
        by_hist, by_flux = defaultdict(set), defaultdict(set)
        zero_flux = Counter()
        based_paths = 0
        for (frame, hist), count in states.items():
            if set(frame) != set(BASE):
                continue
            based_paths += count
            by_hist[hist].add(frame)
            j = flux(hist)
            by_flux[j].add(frame)
            if not any(j):
                zero_flux[''.join(map(str, frame))] += count
        sizes = Counter(map(len, by_hist.values()))
        result.append({
            'length': length,
            'all_ordered_switch_paths': 9**length,
            'based_return_paths': based_paths,
            'directed_histogram_classes': len(by_hist),
            'directed_histogram_holonomy_pairs': sum(k*v for k,v in sizes.items()),
            'directed_histogram_mixed_classes': sum(v for k,v in sizes.items() if k > 1),
            'histogram_holonomy_fiber_sizes': dict(sorted(sizes.items())),
            'antisymmetric_current_classes': len(by_flux),
            'current_mixed_classes': sum(len(hol) > 1 for hol in by_flux.values()),
            'zero_current_paths_by_terminal_frame': dict(sorted(zero_flux.items()))
        })
        if length == 6:
            break
        nxt = defaultdict(int)
        for (frame, hist), count in states.items():
            adj = list(successors(frame))
            assert len(adj) == 9
            for new_frame, arc in adj:
                new_hist = list(hist)
                new_hist[ARC_IDX[arc]] += 1
                nxt[new_frame, tuple(new_hist)] += count
        states = nxt

    assert [x['based_return_paths'] for x in result] == [1,0,9,36,369,2952,26937]
    assert [x['directed_histogram_mixed_classes'] for x in result] == [0,0,0,0,0,144,1008]
    assert [x['current_mixed_classes'] for x in result] == [0,0,0,0,0,38,505]
    assert result[5]['directed_histogram_classes'] == 684
    assert result[5]['histogram_holonomy_fiber_sizes'] == {1:540,2:144}
    assert result[6]['histogram_holonomy_fiber_sizes'] == {1:1563,2:936,4:72}
    assert result[6]['zero_current_paths_by_terminal_frame'] == {
        '123':5265,'132':24,'213':24,'321':24
    }
    assert all(set(x['zero_current_paths_by_terminal_frame']) <= {'123'} for x in result[:6])

    evidence = {
        'schema':'ENTERPRISE_MATH_R762BW_EXACT_V17_EXCHANGE_LEDGER_EVIDENCE_V1',
        'task_id':'RS-X6-TRIADIC-CLOSURE-DYNAMICS',
        'scope':'CONDITIONAL_V17_JOHNSON_REPLACEMENT_PLUS_AXIS_CONTEXT_V29_STYLE_TRANSFER; NOT_NATIVE_EVENT_PERMISSION',
        'base_ordered_frame':list(BASE),
        'axis_count':6,
        'transition_rule':'replace exactly one of 3 frame slots with one of the 3 absent labels',
        'ledger':'30 nonnegative directed old_axis->new_axis counts; antisymmetric current on 15 unordered label pairs',
        'arithmetic':'exact_nonnegative_integers',
        'enumeration':'complete dynamic programming on (ordered_frame, 30-vector directed_histogram) for 0<=length<=6',
        'by_length':result,
        'five_same_hist_identity_path':[list(x) for x in five_identity],
        'five_same_hist_transposition_path':[list(x) for x in five_swap],
        'six_zero_current_transposition_path':[list(x) for x in six_zero_current_swap],
        'status':'AUTHOR_EXACT_CHECK_ALL_PASS_NOT_INDEPENDENTLY_REVIEWED',
        'next_question':'Find native signed TRIADIC_CLOSURE_E admissibility rule and an event-to-axis-exchange transducer preserving Cell/Link/Port semantics; restrict reachable language and recompute observer fibers.'
    }
    print(json.dumps(evidence, ensure_ascii=False, indent=2, sort_keys=True))

if __name__ == '__main__':
    run()
