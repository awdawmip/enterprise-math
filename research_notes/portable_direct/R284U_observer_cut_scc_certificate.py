#!/usr/bin/env python3
"""Exact checks for R284U. Standard library; deterministic rational arithmetic."""
from __future__ import annotations
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
import json


def determinant(matrix):
    m = [list(row) for row in matrix]
    n = len(m)
    sign = 1
    det = F(1)
    for col in range(n):
        k = next((i for i in range(col, n) if m[i][col]), None)
        if k is None:
            return F(0)
        if k != col:
            m[k], m[col] = m[col], m[k]
            sign *= -1
        a = m[col][col]
        det *= a
        for row in range(col + 1, n):
            v = m[row][col] / a
            for j in range(col + 1, n):
                m[row][j] -= v * m[col][j]
            m[row][col] = F(0)
    return sign * det


def matrices(n, baseline, edits, vals):
    m = [[F(int(i == j)) for j in range(n)] for i in range(n)]
    for (u, v), weight in baseline.items():
        m[u][v] -= weight
    for tag, (u, v) in edits.items():
        m[u][v] -= vals.get(tag, F(0))
    return m


def numerator_and_denominator(n, p, baseline, edits, vals):
    m = matrices(n, baseline, edits, vals)
    minor = [row[:p] + row[p+1:] for i, row in enumerate(m) if i != p]
    return determinant(minor), determinant(m)


def paths_present(n, baseline, edits, p):
    adj = defaultdict(set)
    for (u, v), weight in baseline.items():
        if weight and u != p and v != p:
            adj[u].add(v)
    for u, v in edits.values():
        if u != p and v != p:
            adj[u].add(v)
    def reachable(a, b):
        todo = [a]
        seen = set()
        while todo:
            v = todo.pop()
            if v == b:
                return True
            if v not in seen:
                seen.add(v)
                todo.extend(adj[v] - seen)
        return False
    return {tag: (u != p and v != p and reachable(v, u)) for tag, (u, v) in edits.items()}


def as_pair(v):
    return [v.numerator, v.denominator]


def run():
    n, p = 3, 0
    edits = {'x': (1, 2), 'y': (0, 0)}
    b1 = {(0, 0): F(1, 5), (0, 1): F(1, 4), (2, 0): F(1, 3)}
    b2 = {(0, 0): F(1, 5), (0, 1): F(1, 5), (2, 0): F(1, 4)}
    roots = [F(0), F(1, 8), F(1, 16)]
    sample_count = 0
    observed = []
    assert paths_present(n, b1, edits, p) == {'x': False, 'y': False}
    assert paths_present(n, b2, edits, p) == {'x': False, 'y': False}
    for x, y in product(roots, repeat=2):
        v = {'x': x, 'y': y}
        n1, d1 = numerator_and_denominator(n, p, b1, edits, v)
        n2, d2 = numerator_and_denominator(n, p, b2, edits, v)
        assert n1 == n2 == 1
        assert d1 == F(4, 5) - y - x / 12
        assert d2 == F(4, 5) - y - x / 20
        assert n1*d2 - n2*d1 == x / 30
        assert d1 > 0 and d2 > 0
        sample_count += 1
        observed.append({'x': as_pair(x), 'y': as_pair(y), 'P': as_pair(n1*d2-n2*d1)})
    assert observed[0]['P'] == [0, 1]
    assert observed[3]['P'] != [0, 1]  # x = 1/8, y = 0

    # A cycle surviving deletion of observer p can give a true quadratic obstruction.
    ed2 = {'x': (1, 2)}
    c1 = {(0, 1): F(1, 4), (2, 0): F(1, 4)}
    c2 = {(0, 1): F(1, 4), (2, 0): F(15, 64), (2, 1): F(1, 4)}
    assert paths_present(n, c1, ed2, p)['x'] is False
    assert paths_present(n, c2, ed2, p)['x'] is True
    negative_count = 0
    for x in roots + [F(1, 4), F(1, 2)]:
        n1,d1 = numerator_and_denominator(n,p,c1,ed2,{'x':x})
        n2,d2 = numerator_and_denominator(n,p,c2,ed2,{'x':x})
        assert n1*d2-n2*d1 == x / 256 - x*x / 64
        negative_count += 1

    # Structural graph condition is sufficient, not necessary: two internal cycles
    # can cancel across matched models even though both individual numerators vary.
    e1 = {(0, 1): F(1, 4), (2, 0): F(1, 4), (2, 1): F(1, 8)}
    e2 = {(0, 1): F(1, 4), (2, 0): F(1, 2), (2, 1): F(1, 4)}
    assert paths_present(n,e1,ed2,p)['x'] is True
    assert paths_present(n,e2,ed2,p)['x'] is True
    cancellation_count = 0
    for x in roots + [F(1, 4), F(1, 2)]:
        n1,d1 = numerator_and_denominator(n,p,e1,ed2,{'x':x})
        n2,d2 = numerator_and_denominator(n,p,e2,ed2,{'x':x})
        assert n1 == 1-F(1,8)*x and n2 == 1-F(1,4)*x
        assert n1*d2-n2*d1 == -x/16
        cancellation_count += 1


    # Exhaustive finite structural check: all 9 directed edit endpoints,
    # all 2^8 subsets of the remaining baseline edges on 3 vertices.
    # Every selected baseline edge has weight 1/16. Edits have tested weight 1/8.
    edges = [(u,v) for u in range(3) for v in range(3)]
    exhaustive_count = 0
    for e in edges:
        other = [f for f in edges if f != e]
        for mask in range(1 << len(other)):
            baseline = {f:F(1,16) for j,f in enumerate(other) if mask & (1<<j)}
            edit = {'z':e}
            n0,_ = numerator_and_denominator(3,0,baseline,edit,{'z':F(0)})
            n1,_ = numerator_and_denominator(3,0,baseline,edit,{'z':F(1,8)})
            predicted = paths_present(3,baseline,edit,0)['z']
            assert (n1 != n0) == predicted, (e, mask, n0, n1, predicted)
            exhaustive_count += 1
    assert exhaustive_count == 9*256

    return {
      'schema':'R284U_EXACT_FRACTION_VERIFICATION_V1',
      'exhaustive_3port_graph_check':{'edit_endpoint_choices':9,'baseline_edge_subsets_per_endpoint':256,'cases':exhaustive_count,'all_exact_derivative_vs_deleted_observer_reachability':'PASS','baseline_edge_weight':[1,16],'edit_test_weight':[1,8]},
      'result':'PASS',
      'arithmetic':'Python standard-library Fraction; exact Gaussian-elimination determinant',
      'graph_classification':'structural directed reachability after deleting observer p=0',
      'positive_case':{'models':2,'ports':3,'edits':['x:1->2','y:0->0'], 'support_cycle_after_deleting_p':{'x':False,'y':False},'cross_polynomial':'x/30','exact_grid_points':sample_count,'sample_observations':observed},
      'quadratic_obstruction_control':{'P':'x/256-x^2/64','coefficient_x2':[-1,64],'exact_points':negative_count,'graph_cycle_after_deleting_p':{'model1':False,'model2':True}},
      'cancellation_control':{'P':'-x/16','coefficient_x2':[0,1],'exact_points':cancellation_count,'graph_cycle_after_deleting_p':{'model1':True,'model2':True}},
      'verification_scope':'finite, fully specified rational examples; general theorem separately proved in paper',
    }

if __name__ == '__main__':
    print(json.dumps(run(), ensure_ascii=False, indent=2, sort_keys=True))
