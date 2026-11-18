#!/usr/bin/env python3
"""Exact pure-Python dyadic-gap named-XOR collision certificate, p=32.
No network, floats, or stochastic computation. Recomputes PRIOR E and P sets.
"""
import json

P_BITS = 32
N = 1 << P_BITS
T = (P_BITS + 1) * N
LO, HI, STEP = 262145, 524287, 2
Q_SIZE = (HI - LO) // STEP + 1
S = [262147, 280001, 300001, 320003, 340007, 360007, 380003,
     400009, 420001, 440003, 460001, 480007, 500383, 510007,
     520001, 524285]
A32 = [262145, 262657, 266305, 270805, 294903, 299593, 328965,
       338613, 349525, 349867, 360437, 372827, 402905, 416179,
       422733, 427445, 429325, 430185, 449829, 463419, 475107,
       479349, 486737, 524287]
R = [400011 + 2 * j for j in range(256)] + [480011 + 2 * j for j in range(256)]
U = set(S + A32 + R)
P = set(510001 + 194 * j for j in range(64))
P.update(510003 + 194 * j for j in range(64))
P.update(510005 + 194 * j for j in range(64))
assert len(U) == 552 and len(P) == 192 and not U.intersection(P)


def witness(a, b, h):
    """For a-b=2**h, give two same-labelled named flips colliding at (a,b)."""
    assert a - b == 1 << h and a % 2 == b % 2 == 1
    bit = 1 << (h - 1)
    r = a % (2 * bit)
    x = 0 if r >= bit else bit - r
    y = x + a
    assert 0 <= x < y < N
    assert not (x & bit) and (y & bit)
    assert x ^ bit == x + bit
    assert y ^ bit == y - bit
    assert x % a == y % a
    assert (x ^ bit) % b == (y ^ bit) % b
    return x, y, h-1


def in_previous_E(a, b):
    # Complete PREFIX-897 E. lcm(a,b)=a*b for dyadic gaps, since gcd=1.
    assert a % 2 == b % 2 == 1 and ((a-b) & (a-b-1)) == 0
    assert a*b > N
    return (a*b < T or a in U or b in U
            or 33 * ((N+a-1)//a) > b
            or 33 * ((N+b-1)//b) > a)


def main():
    totals = {k: 0 for k in ('all', 'E', 'panel', 'overlap', 'prior_union', 'new')}
    rows = []
    for h in range(1, 18):
        d = 1 << h
        t = {k: 0 for k in totals}
        for b in range(LO, HI - d + 1, 2):
            a = b + d
            witness(a, b, h)
            E = in_previous_E(a, b)
            panel = a in P or b in P
            t['all'] += 2
            t['E'] += 2 * E
            t['panel'] += 2 * panel
            t['overlap'] += 2 * (E and panel)
            t['prior_union'] += 2 * (E or panel)
            t['new'] += 2 * (not E and not panel)
        assert t['all'] == 2 * (Q_SIZE - d//2)
        assert t['E'] + t['panel'] - t['overlap'] == t['prior_union']
        assert t['prior_union'] + t['new'] == t['all']
        rows.append(dict(h=h, gap=d, **t))
        for k in t: totals[k] += t[k]
    assert totals == {'all': 4194306, 'E': 1846732, 'panel': 10878,
                      'overlap': 16, 'prior_union': 1857594, 'new': 2336712}, totals
    prior = 7614875038
    result = {
        'schema': 'PREFIX903_R6_DYADIC_GAP_COLLISION_EXACT_V1',
        'date': '2026-11-18',
        'science_pin': 'f42f2906d77f24085c123f3ccfe9667d41caa96d',
        'model': {'p': P_BITS, 'N': N, 'Q_min': LO, 'Q_max': HI,
                  'Q_step': STEP, 'Q_count': Q_SIZE,
                  'trajectory': 'zero step or one named XOR bit flip',
                  'observer': '(start mod a, end mod b)'},
        'pair_family': 'ordered (a,b) in Q^2 with abs(a-b)=2^h, 1<=h<=17',
        'prior_certificate': 'PREFIX902 E union 192 symmetric rows',
        'prior_certified_union': prior,
        'rows': rows,
        'totals': totals,
        'new_cumulative_certified_union': prior + totals['new'],
        'remaining_outside_stated_union': Q_SIZE**2 - prior - totals['new'],
        'verification': {'exact_integer': True,
                         'positive_gap_pairs_directly_witness_checked': totals['all']//2,
                         'reverse_orientations_proved_by_named_flip_time_reversal': True,
                         'count_membership_exhaustive': True,
                         'no_new_shared_claim': True},
        'scientific_status': 'AUTHOR_PROVED/EXACT_FINITE_CHECKED/NOT_INDEPENDENTLY_REVIEWED/NOT_ADMITTED'
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
