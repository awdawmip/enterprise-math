#!/usr/bin/env python3
"""R13: exact source/Port-labelled Boolean BRC support on fixed +axis0 lanes.

This is a CONDITIONAL vacancy-guarded event model in six signed native Cell
coordinates. No native TRIADIC_CLOSURE_E permission, force or physical time
is inferred. Every branch preserves its complete source/Port-labelled word.
"""
from itertools import product
import json


def configurations(lanes, max_gap):
    """All independent adjacent gaps and exact six-component placements."""
    n = sum(map(len, lanes))
    edges = [(lane[j], lane[j + 1])
             for lane in lanes for j in range(len(lane) - 1)]
    for gaps in product(range(max_gap + 1), repeat=len(edges)):
        gap_map = dict(zip(edges, gaps))
        x = [0] * n
        for lane in lanes:
            here = 0
            for j, source in enumerate(lane):
                if j:
                    here += 1 + gap_map[(lane[j - 1], source)]
                x[source] = here
        positions = tuple(
            (x[source],
             next(idx for idx, lane in enumerate(lanes) if source in lane),
             0, 0, 0, 0)
            for source in range(n))
        assert len(set(positions)) == n
        yield positions, gaps


def full_labelled_brc_support(positions, horizon):
    """True vacancy-guarded native-axis branch support, including empty word."""
    branches = {((), positions)}
    support = {()}
    for _ in range(horizon):
        next_branches = set()
        for word, state in branches:
            occupied = set(state)
            for source, point in enumerate(state):
                target = (point[0] + 1,) + point[1:]
                if target in occupied:
                    continue
                updated = list(state)
                updated[source] = target
                next_word = word + ((source, 0),)
                next_branches.add((next_word, tuple(updated)))
                support.add(next_word)
        branches = next_branches
    return frozenset(support)


def adjacent_gap_brc_support(lanes, gaps, horizon):
    """Independent typed-gap Boolean support, for comparison with real Cells."""
    edges = [(lane[j], lane[j + 1])
             for lane in lanes for j in range(len(lane) - 1)]
    n = sum(map(len, lanes))
    branches = {((), tuple(gaps))}
    support = {()}
    for _ in range(horizon):
        next_branches = set()
        for word, current in branches:
            for source in range(n):
                updated = tuple(
                    g + int(source == front) - int(source == rear)
                    for g, (rear, front) in zip(current, edges))
                if any(g < 0 for g in updated):
                    continue
                next_word = word + ((source, 0),)
                next_branches.add((next_word, updated))
                support.add(next_word)
        branches = next_branches
    return frozenset(support)


def run():
    patterns = [
        [(0,)],
        [(0, 1)],
        [(0, 1, 2)],
        [(0, 1, 2, 3)],
        [(0, 2), (1, 3)],
        [(0, 1), (2, 3)],
        [(0, 1, 2), (3,)],
        [(0,), (1,), (2,), (3,)],
    ]
    max_gap = 3
    horizon_limit = 5
    total_cases = 0
    total_graded_transitions = 0
    cumulative_supported_words = 0
    records = []
    for lanes in patterns:
        n = sum(map(len, lanes))
        edges = [(lane[j], lane[j + 1])
                 for lane in lanes for j in range(len(lane) - 1)]
        instances = list(configurations(lanes, max_gap))
        for horizon in range(horizon_limit + 1):
            by_clipped_signature = {}
            for positions, gaps in instances:
                actual = full_labelled_brc_support(positions, horizon)
                certificate = adjacent_gap_brc_support(lanes, gaps, horizon)
                assert actual == certificate, ('cell-vs-gap', lanes, gaps, horizon)
                signature = tuple(min(g, horizon) for g in gaps)
                if signature in by_clipped_signature:
                    assert by_clipped_signature[signature] == actual, (
                        'sufficiency', lanes, gaps, horizon)
                else:
                    by_clipped_signature[signature] = actual
                total_cases += 1
                cumulative_supported_words += len(actual)
                if horizon:
                    for source in range(n):
                        new_gaps = tuple(
                            g + int(source == front) - int(source == rear)
                            for g, (rear, front) in zip(gaps, edges))
                        if any(g < 0 for g in new_gaps):
                            continue
                        exact_next = tuple(min(g, horizon - 1) for g in new_gaps)
                        clipped_next = tuple(
                            min(horizon - 1, min(g, horizon)
                                + int(source == front) - int(source == rear))
                            for g, (rear, front) in zip(gaps, edges))
                        assert exact_next == clipped_next, (
                            'graded-update', lanes, gaps, horizon, source)
                        total_graded_transitions += 1
            expected = (min(max_gap, horizon) + 1) ** len(edges)
            # Necessity and sufficiency: count expected distinct actual languages.
            assert len(by_clipped_signature) == expected, (
                'class-count', lanes, horizon, len(by_clipped_signature), expected)
            assert len(set(by_clipped_signature.values())) == expected, (
                'minimality', lanes, horizon)
        records.append({
            'lanes': lanes,
            'sources': n,
            'adjacent_edges': len(edges),
            'gap_domain': [0, max_gap],
            'horizons': [0, horizon_limit],
            'configs_per_horizon': len(instances),
            'h5_classes': (min(max_gap, horizon_limit) + 1) ** len(edges),
        })
    assert total_cases == 804
    assert total_graded_transitions == 2140
    assert cumulative_supported_words == 121355
    return {
        'suite': 'X6_FIXED_LANE_TRUNCATED_GAP_TYPED_BOOLEAN_BRC',
        'status': 'PASS',
        'model': ('Six-component signed integer positions; per-source native '
                  '+axis0; labelled Boolean branch support; fixed lane '
                  'partition and within-lane source order; vacant target'),
        'runs': records,
        'state_horizon_configurations': total_cases,
        'direct_vs_gap_language_checks': total_cases,
        'checked_legal_graded_transitions': total_graded_transitions,
        'total_labeled_branch_word_observations': cumulative_supported_words,
        'unbounded_gap_horizon_counterexample': (
            'two sources with gap h versus h+1 have identical L_h but '
            'distinct L_(h+1), witness rear^(h+1); all h>=0'),
        'general_theorem_status': (
            'proved symbolically in accompanying note; '
            'finite suite is corroboration'),
    }


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True, ensure_ascii=False))
