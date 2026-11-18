#!/usr/bin/env python3
"""Finite labelled-branch / Boolean-support BRC certificate for a conditional two-chain event model.

Scope: abstract causal event semantics. These operators are not native Cell/Link/Port authorization.
Carrier: branch words over A,B with typed local counts; support quotient (i,j).
Allowed future operators: append A/B under count limits and the declared A_r < B_s guard.
Observers: kth-cut support and local exact period-p phase readout, never branch multiplicity.
"""
import json
from collections import defaultdict
from math import ceil


def permitted(i, j, a, b, r=None, s=None):
    if not (0 <= i <= a and 0 <= j <= b):
        return False
    return r is None or j < s or i >= r


def support_levels(a, b, r=None, s=None):
    level = {(0, 0)}
    out = [level]
    for _ in range(a + b):
        nxt = set()
        for i, j in level:
            if permitted(i + 1, j, a, b, r, s):
                nxt.add((i + 1, j))
            if permitted(i, j + 1, a, b, r, s):
                nxt.add((i, j + 1))
        level = nxt
        out.append(level)
    return out


def labelled_levels(a, b, r=None, s=None):
    words = {''}
    out = [{(0, 0)}]
    for k in range(a + b):
        nxt = set()
        for w in words:
            i = w.count('A'); j = k - i
            if permitted(i + 1, j, a, b, r, s):
                nxt.add(w + 'A')
            if permitted(i, j + 1, a, b, r, s):
                nxt.add(w + 'B')
        words = nxt
        out.append({(w.count('A'), len(w) - w.count('A')) for w in words})
    return out, len(words)


def interval(a, b, k, r=None, s=None):
    lo = max(0, k - b)
    hi = min(a, k)
    if r is not None:
        lo = max(lo, min(r, k - s + 1))
    return lo, hi


def phase_fibers(states, p):
    fibers = defaultdict(set)
    for i, j in states:
        fibers[(i % p, j % p)].add((i, j))
    return fibers


def formula_fiber(lo, hi, p, residue):
    if lo > hi:
        return 0
    return (hi - residue) // p - (lo - 1 - residue) // p


def validate_case(a, b, r, s, p, check_words=True):
    levels = support_levels(a, b, r, s)
    if check_words:
        words, _ = labelled_levels(a, b, r, s)
        assert levels == words, ('labelled-vs-support', a, b, r, s, p)
    for k, states in enumerate(levels):
        lo, hi = interval(a, b, k, r, s)
        assert states == {(i, k - i) for i in range(lo, hi + 1)}, ('interval', a, b, r, s, p, k)
        fibers = phase_fibers(states, p)
        assert sum(map(len, fibers.values())) == len(states)
        width = hi - lo + 1
        assert max(map(len, fibers.values()), default=0) == (width + p - 1) // p
        for residue in range(p):
            expected = formula_fiber(lo, hi, p, residue)
            got = sum(len(v) for (qi, _), v in fibers.items() if qi == residue)
            assert expected == got, ('phase-fiber', a, b, r, s, p, k, residue)
    return levels


def run():
    cases = 0
    for a in range(1, 6):
        for b in range(1, 6):
            for r in range(1, a + 1):
                for s in range(1, b + 1):
                    for p in (2, 3, 4, 5):
                        validate_case(a, b, r, s, p, check_words=True)
                        cases += 1
    # Explicit C12 test: support-only operator retains the proved future-safe cut quotient.
    uniform = 0
    for r in range(1, 13):
        for s in range(1, 13):
            levels = validate_case(12, 12, r, s, 12, check_words=False)
            assert all(max(map(len, phase_fibers(v, 12).values()), default=0) == 1 for v in levels)
            uniform += 1
    unlinked = validate_case(12, 12, None, None, 12, check_words=False)
    assert max(map(len, phase_fibers(unlinked[12], 12).values())) == 2
    longer = validate_case(24, 12, 2, 1, 12, check_words=False)
    assert phase_fibers(longer[24], 12)[(0, 0)] == {(12, 12), (24, 0)}
    sample = validate_case(3, 3, 2, 2, 12, check_words=True)
    assert [len(v) for v in sample] == [1, 2, 2, 2, 2, 2, 1]
    return {
        'result': 'PASS', 'model': 'finite typed labelled-branch/Boolean-support BRC event cut',
        'hypothesis': 'two local chains, optional symbolic edge A_r < B_s, local exact phase period p',
        'bounded_labeled_cases': cases, 'case_domain': 'a,b in 1..5, r in 1..a, s in 1..b, p in {2,3,4,5}',
        'C12_uniform_edge_cases': uniform, 'C12_uniform_all_k_phase_injective': True,
        'C12_unlinked_k12_max_fiber': 2,
        'C12_longer_edge_k24_collision': [[12, 12], [24, 0]],
        'sample_a3_b3_r2_s2_cut_histogram': [len(v) for v in sample],
        'scope_limit': 'finite conditional event-support combinatorics only; no native multi-Cell admission, no physical timing, no signed amplitude or scientific Result acceptance'
    }

if __name__ == '__main__':
    print(json.dumps(run(), ensure_ascii=False, indent=2, sort_keys=True))
