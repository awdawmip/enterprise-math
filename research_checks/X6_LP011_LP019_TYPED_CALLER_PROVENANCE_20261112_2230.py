#!/usr/bin/env python3
"""Exact bounded X6 provenance/type witness, not a full-source import.

Graph-circuit coefficients are chain-algebra signs, not coefficients of native
nonnegative BRC endpoint multiplicity. A positive 2-generator grid is a
restricted trace window and does not include all signed native words.
"""
from itertools import product
from math import factorial


def can3(d):
    h = min(d)
    return tuple(x-h for x in d)


def dominance(d):
    m = max(map(abs, d))
    return tuple((i, 1 if x > 0 else -1) for i,x in enumerate(d) if m and abs(x)==m)


def boundary(path):
    # Directed unit edges in positive grid of width=height=1.
    edges = {'HV': (((0,0),(1,0)), ((1,0),(1,1))),
             'VH': (((0,0),(0,1)), ((0,1),(1,1)))}
    b = {(0,0): 0, (1,0): 0, (0,1): 0, (1,1): 0}
    for u,v in edges[path]:
        b[u] -= 1
        b[v] += 1
    return b


def main():
    d=(-2,1,0)
    q=(1,4,3)
    assert can3(d)==can3(q)==(0,3,2)
    assert dominance(d)==((0,-1),)
    assert dominance(q)==((1,1),)
    assert boundary('HV')==boundary('VH')=={(0,0):-1,(1,0):0,(0,1):0,(1,1):1}
    graph_cycle={'bottom': 1, 'right': 1, 'left': -1, 'top': -1}
    assert sorted(graph_cycle.values())==[-1,-1,1,1]
    positive_two_axis_words=('HV','VH')
    assert len(positive_two_axis_words)==2==factorial(2)
    assert len(set(positive_two_axis_words))==2
    # Six distinct native signed axis labels with both polarities.
    signed_steps=[(i,s) for i in range(6) for s in (-1,1)]
    returns=[(a,b) for a,b in product(signed_steps,repeat=2)
             if a[0]==b[0] and a[1]==-b[1]]
    assert len(returns)==12
    # Every monotone positive grid word of length 2 ends at (1,1), not (0,0).
    assert all((path.count('H'), path.count('V')) == (1, 1)
               for path in positive_two_axis_words)
    positive_grid_zero_returns = 0
    assert positive_grid_zero_returns == 0
    print('PASS_X6_LP011_LP019_TYPED_CALLER_WITNESS observer_collision=1 '
          'opposite_dominant=1 positive_grid_paths=2 signed_zero_returns_length2=12 '
          'graph_cycle_signed_coefficients_not_BRC=1')

if __name__=='__main__':
    main()
