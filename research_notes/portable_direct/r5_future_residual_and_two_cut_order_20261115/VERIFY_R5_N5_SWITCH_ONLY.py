#!/usr/bin/env python3
"""Exact five-event, two-cut switch-only Q witness; stdlib Python >=3.9."""
from itertools import combinations, product
import json

RADIUS = 2

def point_coordinates(gaps, a, b, mask):
    gaps = list(gaps)
    if mask & 1:
        gaps[a] -= 1
    if mask & 2:
        gaps[b] -= 1
    x = [0]
    for d in gaps:
        x.append(x[-1] + d)
    return x

def optimal_family(x, k):
    best = None
    family = set()
    for S in combinations(range(len(x)), k):
        distances = [min(abs(x[i] - x[j]) for j in S) for i in range(len(x))]
        if max(distances) > RADIUS:
            continue
        cost = sum(distances)
        if best is None or cost < best:
            best, family = cost, {S}
        elif cost == best:
            family.add(S)
    return best, family

def families(gaps, a, b, k):
    data = [optimal_family(point_coordinates(gaps, a, b, m), k) for m in range(4)]
    return [v[0] for v in data], [v[1] for v in data]

def path_edges(path):
    k = len(path)
    return {(0, -1, path[0]), (k, path[-1], -2)} | {
        (r + 1, path[r], path[r + 1]) for r in range(k - 1)
    }

def all_edges(family):
    return set().union(*(path_edges(s) for s in family))

def witness():
    gaps = (3, 2, 2, 3)
    a, b, k = 0, 3, 3
    costs, fam = families(gaps, a, b, k)
    assert costs == [4, 4, 4, 4]
    f0, fa, fb, fab = fam
    assert list(map(len, fam)) == [1, 4, 4, 8]
    assert f0 == {(0, 2, 4)}
    assert fa & fb == f0
    q = fab - fa - fb
    assert q == {(1, 2, 3)}
    ea, eb, eab = (all_edges(f) for f in (fa, fb, fab))
    assert not (eab - ea - eb)
    qpath = next(iter(q))
    signature = [(list(e), 'A' if e in ea and e not in eb else
                  'B' if e in eb and e not in ea else 'AB')
                 for e in sorted(path_edges(qpath))]
    assert [entry[1] for entry in signature] == ['A', 'A', 'B', 'B']
    # Verify rank-labeled edge languages are faithful to the complete families.
    for F, E in ((fa, ea), (fb, eb), (fab, eab)):
        recognized = {s for s in combinations(range(5), k) if path_edges(s) <= E}
        assert recognized == F
    return {
        'gaps': gaps, 'cuts_zero_based': [a, b], 'K': k,
        'coordinates': [point_coordinates(gaps, a, b, m) for m in range(4)],
        'optimum_costs': costs,
        'optimum_families': [[list(s) for s in sorted(F)] for F in fam],
        'P': [], 'Q': [list(qpath)],
        'joint_neutral_edges': 0,
        'Q_edge_colors': signature,
        'family_graphs_exact': True,
    }

def smaller_cases():
    tested = equal = q_cases = switch_only = 0
    for n in (3, 4):
        for gaps in product((1, 2, 3), repeat=n - 1):
            cuts = [i for i, d in enumerate(gaps) if d == 3]
            for a, b in combinations(cuts, 2):
                for k in range(1, n + 1):
                    tested += 1
                    costs, fam = families(gaps, a, b, k)
                    if costs[0] is None or len(set(costs)) != 1:
                        continue
                    equal += 1
                    q = fam[3] - fam[1] - fam[2]
                    q_cases += bool(q)
                    if q and not (all_edges(fam[3]) - all_edges(fam[1]) - all_edges(fam[2])):
                        switch_only += 1
    assert (q_cases, switch_only) == (0, 0)
    return {'declared_domain': 'n=3..4; gaps in {1,2,3}; two gaps of length 3 contract to 2; all 1<=K<=n',
            'tested': tested, 'common_finite_optimum': equal,
            'Q_nonempty': q_cases, 'switch_only_Q': switch_only}

if __name__ == '__main__':
    print(json.dumps({'status': 'PASS_R5_N5_GEOMETRIC_SWITCH_ONLY_Q',
                      'frozen_science_input': '435e77af0d180eac32bd1f9c4c464bc4010b7551',
                      'witness': witness(), 'minimality_domain': smaller_cases(),
                      'independent_review': 'NOT_REVIEWED'},
                     indent=2, sort_keys=True))
