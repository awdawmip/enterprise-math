#!/usr/bin/env python3
"""Stage415-B finite exact observer certificate; Python standard library only.
No native Enterprise-Math backend experiment or role authority is claimed.
"""
import json
from collections import Counter, defaultdict

A, B = 'A', 'B'  # native +E1, -E1 within the 12 native directions

def history(n, r, s, i):
    assert n >= 5 and 2 <= r and r + 2 <= s <= n - 1 and i in (r, s)
    p = A * (i - 1) + B + A * (n - i)
    q = A * (r - 1) + B + A * (s - r - 1) + B + A * (n - s)
    assert len(p) == len(q) == n
    return p, q

def fiber(n):
    return [(r, s, i, *history(n, r, s, i))
            for r in range(2, n - 2)
            for s in range(r + 2, n)
            for i in (r, s)]

def adjacent(word):
    return tuple(Counter(zip(word, word[1:])).get(z, 0)
                 for z in ((A, A), (A, B), (B, A), (B, B)))

def observer(p, q):
    z_p = (p.count(A) - p.count(B), 0, 0, 0, 0, 0)
    z_q = (q.count(A) - q.count(B), 0, 0, 0, 0, 0)
    return (len(p), len(q), z_p, z_q, adjacent(p), adjacent(q),
            sum(x == y for x, y in zip(p, q)))

def cancel_ok(p, q):
    return (len(p) >= 2 and len(q) >= 2 and
            p[-2:] in ('AB', 'BA') and q[-2:] in ('AB', 'BA'))

def run(p, q, trace):
    record = [('INIT', observer(p, q))]
    for action in trace:
        if action[0] == 'APP':
            p += action[1]; q += action[2]
        elif action[0] == 'POP':
            if not q:
                record.append(('DENIED-POP',))
                return tuple(record)
            q = q[:-1]
        elif action[0] == 'CANCEL':
            if not cancel_ok(p, q):
                record.append(('DENIED-CANCEL',))
                return tuple(record)
            p, q = p[:-2], q[:-2]
        else:
            raise ValueError(action)
        record.append(('OK', observer(p, q)))
    return tuple(record)

T7 = (
    (('APP', 'B', 'A'), ('POP',), ('POP',), ('CANCEL',), ('APP', 'B', 'B'), ('CANCEL',)),
    (('APP', 'A', 'A'), ('APP', 'B', 'B'), ('CANCEL',), ('POP',), ('CANCEL',), ('POP',)),
    (('APP', 'B', 'B'), ('CANCEL',), ('APP', 'B', 'A'), ('POP',), ('POP',), ('CANCEL',)),
)
T9 = (
    (('APP', 'B', 'B'), ('CANCEL',), ('POP',), ('POP',), ('APP', 'B', 'B'), ('CANCEL',)),
    (('APP', 'B', 'B'), ('CANCEL',), ('APP', 'B', 'A'), ('POP',), ('POP',), ('CANCEL',)),
    (('APP', 'B', 'B'), ('CANCEL',), ('CANCEL',), ('POP',), ('POP',)),
)

def test_partition(n, suite):
    fs = fiber(n)
    signatures = [tuple(run(x[3], x[4], t) for t in suite) for x in fs]
    parts = defaultdict(list)
    for x, sig in zip(fs, signatures):
        parts[sig].append(x[:3])
    column_ranks = []
    for j in range(len(suite)):
        options = sorted({signature[j] for signature in signatures}, key=repr)
        rank = {repr(value): k for k, value in enumerate(options)}
        column_ranks.append(rank)
    reps = []
    for sig, members in parts.items():
        rep = min(members)
        reps.append({'representative': list(rep),
                     'test_ranks': [column_ranks[j][repr(sig[j])] for j in range(len(suite))],
                     'class_size': len(members)})
    return sorted(reps, key=lambda x: x['representative']), len(fs)

def suffix_keys(n, k=7):
    return { (p[-k:], q[-k:]) for _, _, _, p, q in fiber(n)}

def main():
    n7, s7 = test_partition(7, T7)
    n9, s9 = test_partition(9, T9)
    assert (s7, len(n7)) == (12, 12)
    assert (s9, len(n9)) == (30, 16)
    assert len({tuple(r['test_ranks']) for r in n7}) == 12
    assert len({tuple(r['test_ranks']) for r in n9}) == 16
    assert len({(tuple(x['representative'])) for x in n9}) == 16
    sizes = {}
    for n in range(5, 23):
        reps, size = test_partition(n, T9)
        assert size == (n - 3) * (n - 4)
        sizes[str(n)] = {'fiber_size': size, 'T9_distinct_observation_signatures': len(reps),
                         'last7_pair_suffix_keys': len(suffix_keys(n))}
    assert all(sizes[str(n)]['T9_distinct_observation_signatures'] == 16 for n in range(9, 23))
    assert all(sizes[str(n)]['last7_pair_suffix_keys'] == 33 for n in range(11, 23))
    p1, q1 = history(7, 2, 4, 2)
    p2, q2 = history(7, 2, 4, 4)
    assert p1[-3:] == p2[-3:] and q1[-4:] == q2[-4:]
    assert observer(p1, q1) == observer(p2, q2)
    assert run(p1, q1, T7[2]) != run(p2, q2, T7[2])
    # Appending h leading A letters to both words preserves equality/distinction
    # of this fixed tail-operation suite; checked here for h=0..12.
    for h in range(13):
        codes = set()
        for entry in n9:
            r, s, i = entry['representative']
            p, q = history(9, r, s, i)
            observed = tuple(run(A*h+p, A*h+q, t) for t in T9)
            assert observed not in codes
            codes.add(observed)
        assert len(codes) == 16
    result = {'marker': 'STAGE415B_TWO_CANCEL_EXACT_CERT_PASS',
              'science_pins': {'global':'bf84bd7c61a2444b59b1da96be57df0e9ae47e53',
                               'enterprise_math':'2af3fc484eb11060b69e0afc1b562bcaf5ad1419',
                               'p000_blob':'bcc2590d3168a28f72e8b9f0f9b1f76faadcd488'},
              'coverage':'Exact finite A/B traces; all 12 directions are not exhaustively tested',
              'trace_suites': {'n7': T7, 'n9': T9},
              'n7_full_fiber_pairwise_distinguishable': n7,
              'n9_sixteen_distinguishable_representatives': n9,
              'n5_through_n22': sizes,
              'padding_crosscheck_h_0_to_12': 'PASS',
              'fresh_explicit_witness':'n7 (r,s,i)=(2,4,2) and (2,4,4) share Stage414 key but T7[2] distinguishes them; only two CANCELs.'}
    print(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))

if __name__ == '__main__':
    main()
