#!/usr/bin/env python3
"""Exhaustive exact finite checks for R5 non-isolated two-choice pair-block family.
Python standard library only. Exact integer arithmetic; all binomial center sets.
"""
from itertools import combinations, product
import json

BASE_GAPS = (3, 2, 2, 3)
RADIUS = 2

def positions(gaps, mask):
    d = list(gaps)
    if mask & 1:
        d[0] -= 1
    if mask & 2:
        d[3] -= 1
    x = [0]
    for gap in d:
        x.append(x[-1] + gap)
    return x

def opt_family(x, k):
    best, family = None, set()
    for s in combinations(range(len(x)), k):
        d = [min(abs(x[i]-x[j]) for j in s) for i in range(len(x))]
        if max(d) > RADIUS:
            continue
        cost = sum(d)
        if best is None or cost < best:
            best, family = cost, {s}
        elif cost == best:
            family.add(s)
    return best, family

def edges(s):
    k = len(s)
    return {(0, -1, s[0]), (k, s[-1], -2)} | {
        (i+1, s[i], s[i+1]) for i in range(k-1)
    }

def all_edges(family):
    out = set()
    for s in family:
        out.update(edges(s))
    return out

def run():
    base = [opt_family(positions(BASE_GAPS, mask), 3)[1]
            for mask in range(4)]
    assert list(map(len, base)) == [1, 4, 4, 8]
    assert [opt_family(positions(BASE_GAPS, mask), 2)[0]
            for mask in range(4)] == [None, None, None, 6]
    assert (base[1] & base[2]) - base[0] == set()
    assert base[3] - base[1] - base[2] == {(1, 2, 3)}
    assert all_edges(base[3]) == all_edges(base[1]) | all_edges(base[2])

    rows = []
    for m in range(7):
        gaps = BASE_GAPS + (3, 1) * m
        k, n = 3+m, 5+2*m
        checks = [opt_family(positions(gaps, mask), k)
                  for mask in range(4)]
        costs, fam = [c for c, _ in checks], [f for _, f in checks]
        H = {tuple(5 + 2*j + choice for j, choice in enumerate(bits))
             for bits in product((0, 1), repeat=m)}
        expected = [{s + h for s in b for h in H} for b in base]
        assert costs == [4+m]*4, (m, costs)
        assert fam == expected, ('optimizer-product', m)
        f0, fa, fb, fab = fam
        p = (fa & fb) - f0
        q = fab - fa - fb
        assert not p
        assert q == {(1, 2, 3) + h for h in H}
        assert all_edges(fab) == all_edges(fa) | all_edges(fb)
        assert list(map(len, fam)) == [2**m, 4*2**m, 4*2**m, 8*2**m]
        for j in range(m):
            for mask_family in fam:
                assert sum(5+2*j in s for s in mask_family) == len(mask_family)//2
                assert sum(6+2*j in s for s in mask_family) == len(mask_family)//2
        rows.append({
            'm': m, 'n': n, 'K': k, 'J': 4+m,
            'gap_word': list(gaps),
            'opt_counts': list(map(len, fam)),
            'P_count': len(p), 'Q_count': len(q),
            'rank_edges_AB': len(all_edges(fab)),
            'rank_edges_union': len(all_edges(fa) | all_edges(fb)),
            'q_first': list(min(q))
        })
    return {
        'status': 'PASS_R5_NONISOLATING_PAIR_BLOCK_FAMILY',
        'frozen_science_input': '435e77af0d180eac32bd1f9c4c464bc4010b7551',
        'model': 'radius=2, integer indexed-center observer; two original gap3 closures',
        'finite_range': 'm=0..6 exhaustive all C(n,K) index sets, four masks',
        'rows': rows,
        'independent_review': 'NOT_REVIEWED'
    }

if __name__ == '__main__':
    print(json.dumps(run(), indent=2, sort_keys=True))
