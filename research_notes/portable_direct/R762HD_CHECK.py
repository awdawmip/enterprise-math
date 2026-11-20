#!/usr/bin/env python3
"""R762HD: exact positive-branch Port/Cell checker, no third-party dependencies."""
from collections import defaultdict
from itertools import combinations, permutations
import json

I = range(6)
PORTS = tuple(combinations(I, 2))
NBR = {p: tuple(q for q in PORTS if len(set(p) & set(q)) == 1) for p in PORTS}
ZERO = (0,) * 6
P0 = (0, 1)

def increment(p, q):
    support = set(p) | set(q)
    assert len(support) == 3
    return tuple(int(i in support) for i in I)

def matrix_counts():
    cur = {p: int(p == P0) for p in PORTS}
    out = []
    for m in range(13):
        actual = cur[P0]
        closed = (8**m + 5 * 2**m + 9 * (-2)**m) // 15
        assert 15 * closed == 8**m + 5 * 2**m + 9 * (-2)**m
        assert actual == closed
        out.append(2**m * actual)
        nxt = {p: sum(cur[q] for q in NBR[p]) for p in PORTS}
        cur = nxt
    return out

def check_s6():
    # Entire axis permutation group and every choice of prior and next Port.
    assert all(len(NBR[p]) == 8 for p in PORTS)
    tested = 0
    for pi in permutations(I):
        for p in PORTS:
            pp = tuple(sorted(pi[i] for i in p))
            image = {tuple(sorted(pi[i] for i in q)) for q in NBR[p]}
            assert image == set(NBR[pp])
            for q in NBR[p]:
                q2 = tuple(sorted(pi[i] for i in q))
                old = increment(p, q)
                new = increment(pp, q2)
                assert all(new[pi[i]] == old[i] for i in I)
                tested += 1
    return tested

def check_A2():
    for p in PORTS:
        for q in PORTS:
            n = sum(q in NBR[r] for r in NBR[p])
            assert n == 4 + 4 * (p == q)

def joint_counts(max_m=6):
    dp = {(P0, ZERO): 1}
    out = []
    for m in range(max_m + 1):
        port = sum(w for (p, _), w in dp.items() if p == P0)
        joint = dp.get((P0, ZERO), 0)
        assert sum(dp.values()) == 16**m
        assert port == (8**m + 5 * 2**m + 9 * (-2)**m) * 2**m // 15
        out.append({'m': m, 'port_return': port, 'cell_port_return': joint, 'total_histories': 16**m, 'reached_states': len(dp)})
        if m == max_m: break
        next_dp = defaultdict(int)
        for (p, c), weight in dp.items():
            for q in NBR[p]:
                h = increment(p, q)
                for sigma in (-1, +1):
                    c2 = tuple(c[i] + sigma * h[i] for i in I)
                    next_dp[(q, c2)] += weight
        dp = next_dp
    assert [v['cell_port_return'] for v in out] == [1, 0, 16, 0, 624, 0, 34688]
    return out

def check_local_lattice():
    for p in PORTS:
        outside = tuple(i for i in I if i not in p)
        # Independent coordinate decoder for all 4 local generators.
        for k in outside:
            h = tuple(int(i in set(p) | {k}) for i in I)
            assert h[k] == 1 and all(h[j] == int(j == k) for j in outside)
            assert h[p[0]] == h[p[1]] == sum(h[j] for j in outside)
        for choices in (-2, -1, 0, 1, 2), (2, 1, 0, -1, -2):
            n = {k: choices[z] for z, k in enumerate(outside)}
            y = tuple(sum(n[k] * int(i in set(p) | {k}) for k in outside) for i in I)
            assert y[p[0]] == y[p[1]] == sum(y[k] for k in outside)
            assert tuple(y[k] for k in outside) == tuple(n[k] for k in outside)
    # Every unordered triple occurs under exactly its three Port subedges.
    triples = tuple(combinations(I, 3))
    for s in triples:
        assert sum(set(p) <= set(s) for p in PORTS) == 3

if __name__ == '__main__':
    check_A2()
    check_local_lattice()
    tested = check_s6()
    port = matrix_counts()
    joint = joint_counts()
    print(json.dumps({'schema': 'R762HD_EXACT_EVIDENCE_V1',
                      'model': 'S6_EQUIVARIANT_K6_PORT_GATED_THREE_AXIS_COMPOSITE_CANDIDATE',
                      'axis_permutations': 720, 'covariance_transition_cases': tested,
                      'ports': 15, 'unsigned_next_edges_per_port': 8,
                      'signed_branches_per_port': 16,
                      'signed_port_return_m0_to_12': port,
                      'joint_counts_m0_to_6': joint,
                      'author_check': 'PASS',
                      'independent_review': 'NOT_REVIEWED'}, indent=2))
