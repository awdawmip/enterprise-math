#!/usr/bin/env python3
"""Exact polynomial signatures for all 12 oriented 3-node trees, H=2,3.
Requires R284BM_connected_port_graph_checker.py in the same directory.
"""
from itertools import combinations, product
import json
from R284BM_connected_port_graph_checker import polynomial


def run():
    n = 3
    all_edges = [(i,j) for i in range(n) for j in range(n) if i != j]
    trees = [E for E in combinations(all_edges, 2)
             if len({frozenset(edge) for edge in E}) == 2
             and len({v for edge in E for v in edge}) == 3]
    assert len(trees) == 12
    results = {}
    for H in (2,3):
        count = 0
        for E in trees:
            seen = set()
            for flat in product(range(1,H+1), repeat=9):
                C = [flat[0:3], flat[3:6], flat[6:9]]
                s = tuple(sorted(polynomial(C,E).items()))
                assert s not in seen, (H, E, flat)
                seen.add(s)
            assert len(seen) == H**9
            count += len(seen)
        results[f'H={H}'] = {'oriented_trees':len(trees),
                             'matrices_per_tree':H**9,
                             'checked_signatures':count,
                             'all_injective':True}
    return {'exact_arithmetic':'integer polynomial coefficient dictionaries',
            'results':results, 'status':'PASS',
            'scope':'Finite exhaustive n=3, H=2,3; general n=3 positivity proved algebraically in theorem'}

if __name__ == '__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
