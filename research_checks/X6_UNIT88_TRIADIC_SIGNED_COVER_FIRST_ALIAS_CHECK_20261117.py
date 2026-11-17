#!/usr/bin/env python3
"""Independent source-typed X6 triadic 3-at-once event cover return check."""
from collections import Counter
from itertools import combinations, product
from math import comb
import json

N = 6
TRIADS = tuple(combinations(range(N), 3))
SIGNED = tuple(tuple((a, s[i]) for i, a in enumerate(S)) for S in TRIADS for s in product((-1, 1), repeat=3))


def degree_count(m):
    """Coefficient of x_1^m...x_6^m in (e_3(x_1,...,x_6))^(2m)."""
    dist = {(0,)*N: 1}
    for step in range(2*m):
        new = {}
        for D, n in dist.items():
            for triad in TRIADS:
                inc = tuple(D[i] + (i in triad) for i in range(N))
                if max(inc) <= m:
                    new[inc] = new.get(inc, 0) + n
        dist = new
    return dist.get((m,)*N, 0), len(dist)


def vector(tau):
    z = [0] * N
    for i, sign in tau:
        z[i] += sign
    return tuple(z)


def two_event_census():
    moves = [vector(t) for t in SIGNED]
    count = Counter(tuple(a[i]+b[i] for i in range(N)) for a in moves for b in moves)
    return dict(native_return=count[(0,)*N], diagonal_plus=count[(1,)*N], diagonal_minus=count[(-1,)*N], finite_m1_return=sum(n for z,n in count.items() if len(set(z))==1))


def four_event_pair_census():
    moves = [vector(t) for t in SIGNED]
    pair = Counter(tuple(a[i]+b[i] for i in range(N)) for a in moves for b in moves)
    zero = sum(v*pair.get(tuple(-x for x in z),0) for z,v in pair.items())
    target = (2,)*N
    plus = sum(v*pair.get(tuple(target[i]-z[i] for i in range(N)),0) for z,v in pair.items())
    minus = sum(v*pair.get(tuple(-2-z[i] for i in range(N)),0) for z,v in pair.items())
    return dict(native_return=zero, diagonal_plus2=plus, diagonal_minus2=minus, finite_m2_return=zero+plus+minus, pair_states=len(pair))


def run():
    E=[]
    for m in range(1,6):
        v, states=degree_count(m)
        E.append(dict(modulus=m, first_separating_event_length=2*m, plus_diagonal_count=v, minus_diagonal_count=v, alias_extra=2*v, bounded_degree_states=states))
    first = two_event_census()
    second = four_event_pair_census()
    if E[0]['plus_diagonal_count'] != first['diagonal_plus'] or first != {'native_return':160,'diagonal_plus':20,'diagonal_minus':20,'finite_m1_return':200}:
        raise ValueError(('first event census discrepancy',E[0],first))
    if E[1]['plus_diagonal_count'] != second['diagonal_plus2'] or second['diagonal_plus2'] != second['diagonal_minus2']:
        raise ValueError(('four event census discrepancy', E[1], second))
    return dict(schema='EM_X6_UNIT88_TRIADIC_COVER_FIRST_ALIAS_V1',source_consumer='experiments/x6_triadic_decomposition_brc_v2_20260906/check_triadic_decomposition_brc.py',model='160 labeled signed 3-axis simultaneous event types over Z6',scientific_input_p000='59538f585d037d09ef687b28715c4bc1a3f9fe03',events_per_primitive='one triadic event is 3 signed-axis updates, not one P000 primitive spatial direction',status='AUTHOR_EXACT_EXECUTED_UNREVIEWED_NOT_ADMITTED',cases=E,independent_two_event=first,independent_four_event=second,checks='bounded degree-vector DP and independent direct 160^2 and pair-convolution 160^4; integer exact',native_benchmark_reexecuted=False,failures=0)

if __name__=='__main__':
    print(json.dumps(run(),ensure_ascii=False,sort_keys=True,separators=(',',':')))
