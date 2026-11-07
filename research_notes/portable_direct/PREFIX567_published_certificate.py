#!/usr/bin/env python3
"""Exact extremal gate coefficient certificate; frozen BRC pin f42f2906d77f24085c123f3ccfe9667d41caa96d.
Uses published PREFIX565 and PREFIX566 native kernels. Python standard library only.
"""
from collections import Counter, defaultdict
from math import comb
import json
from PREFIX565_positive_marginal_certificate import ROOTS, ZERO_ROOT, ACTIONS, edge, clean
from PREFIX566_gate_quotient_certificate import (marginal_gate_rows, weighted_quotient,
    step_gate, native_involution, symmetric_to_uvz)


def first_hit(rows):
    prev = [{(0, 0): 1} for _ in range(96)]
    delta, leading = {}, {}
    for depth in range(1, 6):
        curr = []
        for row in rows:
            out = Counter()
            for (j, a, b, gate), mult in row.items():
                if gate != int(depth == 1):
                    continue
                for (x, y), c in prev[j].items():
                    out[x+a, y+b] += mult*c
            curr.append(clean(out))
        for i, poly in enumerate(curr):
            if poly and i not in delta:
                delta[i], leading[i] = depth, poly
        prev = curr
    assert len(delta) == 96
    return delta, leading


def product(a, b):
    out = Counter()
    for (x, y), v in a.items():
        for (i, j), w in b.items():
            out[x+i, y+j] += v*w
    return clean(out)


def expected(first, k):
    power = Counter()
    for j in range(k):
        c = comb(k-1, j)*4**(k-1-j)*8**j
        for a in range(j+1):
            power[a, j-a] += c*comb(j, a)
    return product(first, power)


def verify(max_k=12):
    rows = marginal_gate_rows(ZERO_ROOT)
    checked_edges = 0
    for root in ROOTS:
        for i in range(96):
            for a in ACTIONS:
                j, w = edge(i, a, root)
                j0, w0 = edge(i, a, ZERO_ROOT)
                assert j == j0 and w[4:] == w0[4:]
                checked_edges += 1
    delta, leading = first_hit(rows)
    assert Counter(delta.values()) == {1:3, 2:18, 3:36, 4:30, 5:9}
    assert len({(delta[i],tuple(sorted(leading[i].items()))) for i in range(96)}) == 25
    assert delta[9] == 4 and leading[9] == {(0,0):4, (1,0):8, (0,1):8}
    fixed = [i for i, j in enumerate(native_involution()) if i == j]
    assert len(fixed) == 32
    classes = defaultdict(list)
    for i in fixed:
        poly = {(a,b,0): c for (a,b),c in leading[i].items()}
        assert all(poly.get((b,a,0)) == c for (a,b,_),c in poly.items())
        uv = symmetric_to_uvz(poly)
        assert all(c>0 for c in uv.values())
        classes[(delta[i],tuple(sorted(uv.items())))].append(i)
    assert len(classes) == 9
    ids, quotient, _ = weighted_quotient(rows)
    assert len(quotient) == 37
    cur = [{(0,0,0):1} for _ in quotient]
    compared, positions = 0, 0
    last_depth = max(delta.values())+4*(max_k-1)
    for depth in range(last_depth+1):
        for i in range(96):
            k = (depth-delta[i])//4+1
            if k>=1 and k<=max_k and delta[i]+4*(k-1)==depth:
                got = {(a,b):c for (a,b,z),c in cur[ids[i]].items() if z==k}
                want = expected(leading[i], k)
                assert got == want, (depth,i,k)
                compared += 1
                positions += len(want)
        if depth < last_depth:
            cur = step_gate(cur, quotient)
    return {'status':'ALL_CHECKS_PASS', 'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
        'native_edge_checks':checked_edges, 'first_hit_classes':25,
        'fixed_ports':len(fixed), 'fixed_uv_first_hit_classes':len(classes),
        'exact_gate_onset_checks':compared, 'nonzero_positions':positions,
        'k_range':[1,max_k], 'max_depth':last_depth,
        'fixed_classes':[{'delta':d,'uv_terms':[[a,b,c] for ((a,b,g),c) in terms],
                          'ports':ports} for (d,terms),ports in sorted(classes.items())]}


if __name__ == '__main__':
    print(json.dumps(verify(),ensure_ascii=False,indent=2))
