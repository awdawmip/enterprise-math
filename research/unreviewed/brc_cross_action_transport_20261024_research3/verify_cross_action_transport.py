#!/usr/bin/env python3
"""Standalone exact-integer check of a two-action BRC cross-action transport certificate.
Author-side evidence only; proof of all-future assertion is in the companion note.
"""
from itertools import product
import json

Q = 7
ROWS = ((1, 1, 1, 4), (1, 1, 4, 1))
EDGES = ((0, 3), (1, 2))
BASE = (2, 0)
DEG = tuple(sum(i in e for e in EDGES) for i in range(4))
FLOW = (
    ((0, 1, 6), (1, 1, 6), (2, 1, 6), (3, 0, 48)),
    ((0, 0, 6), (1, 0, 6), (2, 1, 3), (3, 0, 96)),
)

def product_weight(counts, rates):
    return rates[0] ** counts[0] * rates[1] ** counts[1]

def vector_for_vertex(i):
    return tuple(row[i] for row in ROWS)

def vector_for_edge(j):
    v, w = EDGES[j]
    return tuple(row[v] + row[w] for row in ROWS)

def numerator(counts):
    if sum(counts) == 0:
        return 0
    pos = sum(product_weight(counts, vector_for_edge(j)) for j in range(2))
    neg = sum(DEG[i] * product_weight(counts, vector_for_vertex(i)) for i in range(4))
    return pos - neg

def increment_numerator(counts, a):
    nxt = list(counts); nxt[a] += 1
    return numerator(tuple(nxt)) - Q * numerator(counts)

def demand(a):
    return [(Q - ROWS[a][i]) * DEG[i] * product_weight(BASE, vector_for_vertex(i)) for i in range(4)]

def capacity(a):
    return [(Q - vector_for_edge(j)[a]) * product_weight(BASE, vector_for_edge(j)) for j in range(2)]

def support_dp(word):
    dp = [0] * (1 << 4); dp[0] = 1
    for a in word:
        nxt = [0] * (1 << 4)
        for mask, w in enumerate(dp):
            if w:
                for i, p in enumerate(ROWS[a]):
                    nxt[mask | (1 << i)] += w * p
        dp = nxt
    return sum(dp[(1 << i) | (1 << j)] for i, j in EDGES)

def run():
    assert DEG == (1, 1, 1, 1)
    d = [demand(a) for a in range(2)]
    cap = [capacity(a) for a in range(2)]
    assert d == [[6,6,6,48],[6,6,3,96]], d
    assert cap == [[50,20],[125,8]], cap
    # Standard incidence-Hall obstruction: subsets {0,3}, {1,2}.
    assert d[0][0]+d[0][3] > cap[0][0]
    assert d[1][1]+d[1][2] > cap[1][1]
    spare = []
    for a in range(2):
        used_d = [0] * 4
        used_c = [0] * 2
        for i,j,amt in FLOW[a]:
            assert amt > 0
            used_d[i] += amt
            used_c[j] += amt
            assert all(t <= s for t,s in zip(vector_for_vertex(i), vector_for_edge(j))), (a,i,j)
        assert used_d == d[a]
        assert all(used_c[j] <= cap[a][j] for j in range(2))
        spare.append([cap[a][j] - used_c[j] for j in range(2)])
    assert spare == [[2,2],[17,5]], spare
    assert numerator(BASE) == 10
    checks_dp = 0
    checks_grid = 0
    for n in range(0,9):
        for word in product((0,1),repeat=n):
            counts = (2+word.count(0),word.count(1))
            full_word = (0,0)+word
            assert numerator(counts) == support_dp(full_word)
            checks_dp += 1
    for u in range(11):
        for v in range(11):
            c = (BASE[0]+u, BASE[1]+v)
            for a in range(2):
                inc = increment_numerator(c,a)
                upper = -sum(spare[a][j] * product_weight((u,v),vector_for_edge(j)) for j in range(2))
                # Both numerator expressions have common denominator 7^(3+u+v).
                assert inc <= upper < 0, (c,a,inc,upper)
                checks_grid += 1
    result = {
       "schema":"EM_BRC_CROSS_ACTION_TRANSPORT_EXACT_EVIDENCE_V1",
       "status":"AUTHOR_SIDE_EXACT_VERIFIED_UNREVIEWED",
       "integer_denominator":7,
       "rows":ROWS,
       "good_edges":EDGES,
       "base_action_counts":BASE,
       "vertex_demand_numerators":d,
       "edge_capacity_numerators":cap,
       "flows":FLOW,
       "spare_edge_capacities":spare,
       "ordinary_hall_fails_action0": "D0+D3=54>C03=50",
       "ordinary_hall_fails_action1": "D1+D2=9>C12=8",
       "initial_occupancy": "10/49",
       "increment_at_base": [f"{increment_numerator(BASE,a)}/343" for a in range(2)],
       "support_mask_word_checks":checks_dp,
       "arbitrary_future_increment_checks":checks_grid,
       "proof_of_all_futures":"exact coordinatewise domination of every flow edge; see companion proof"
    }
    print(json.dumps(result,indent=2,ensure_ascii=False))

if __name__ == '__main__':
    run()
