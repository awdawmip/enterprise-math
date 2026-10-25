#!/usr/bin/env python3
"""Exact positive ordered-six-edge BRC auxiliary fiber rank/prefix checker.

Scope: source-word multiplicities, terminal q=0, never signed amplitudes or X6 physics.
No external libraries and no floating-point comparisons are used.
"""
import json
import sys

LIMIT = 600
M_BOUND = 400
EDGES = {
    0: ((2, -1, -1), (2, +1, -1)),
    1: ((0, -1, -1), (0, +1, -1)),
    2: ((1, +1, +1), (2, +1, -1)),
}

# 4R_m^eps = a(m) + b(m) * sqrt(5); valid m >=0.
def rank_pair(sign, m):
    p = m & 1
    if sign == +1:
        return (-7 + 2*p - 10*m - 15*m*m,
                5 + 2*m + 7*m*m)
    return (-37 + 2*p + 40*m - 15*m*m,
            17 - 20*m + 7*m*m)

def compare_surd(p, q):
    """Exact sign of ((p[0]-q[0]) + (p[1]-q[1])*sqrt(5))."""
    a, b = p[0] - q[0], p[1] - q[1]
    if a == 0:
        return (b > 0) - (b < 0)
    if b == 0 or (a > 0) == (b > 0):
        return (a > 0) - (a < 0)
    s = a*a - 5*b*b
    assert s != 0
    return ((a > 0) - (a < 0)) * ((s > 0) - (s < 0))

predicted = {0: ((+1, 4), (-1, 4)), 1: ((-1, 3), (+1, 5))}
for p in (0, 1):
    items = [(sign, m) for m in range(p, M_BOUND + 1, 2) for sign in (-1, 1)]
    ranks = [rank_pair(sign, m) for sign, m in items]
    assert len(set(ranks)) == len(items), "finite scan found duplicate rank"
    # Exact comparisons below certify both winners (no floating-point ordering).
    first, second = predicted[p]
    for item in items:
        if item != first:
            assert compare_surd(rank_pair(*first), rank_pair(*item)) < 0, ('first',p,item)
        if item not in (first, second):
            assert compare_surd(rank_pair(*second), rank_pair(*item)) < 0, ('second',p,item)
    assert compare_surd(rank_pair(*first), rank_pair(*second)) < 0

# Independent source-preserving DP. Each key retains control q, full affine sign/k,
# and whether the last source bit was 0 (to enforce the forbidden 00).
dp = {(0, +1, 0, 0): 1}
checked = 0
first_gap = {}
terminal_effects = {}
peak_checks = 0
all_effect_count_comparisons = 0
for n in range(LIMIT + 1):
    counts = {}
    for (q, sign, k, last_zero), mass in dp.items():
        if q == 0:
            counts[(sign, k)] = counts.get((sign, k), 0) + mass
    if n >= 81:
        p = n & 1
        first, second = predicted[p]
        a = counts.get((first[0], -first[1]), 0)
        b = counts.get((second[0], -second[1]), 0)
        assert a > b > 0, ('first versus second',n,a,b)
        for effect, c in counts.items():
            if effect != (first[0], -first[1]):
                assert a > c, ('global largest',n,effect,a,c)
            if effect not in ((first[0], -first[1]),(second[0], -second[1])):
                assert b > c, ('global second',n,effect,b,c)
            all_effect_count_comparisons += 1
        peak_checks += 1
        if n in (81,82,180,400,600):
            first_gap[str(n)] = {
                'first_effect': [first[0],-first[1]],
                'second_effect': [second[0],-second[1]],
                'first_count': str(a), 'second_count': str(b),
                'gap': str(a-b), 'terminal_fibers':len(counts)
            }
    if n == LIMIT:
        break
    nxt = {}
    for (q, sign, k, last_zero), mass in dp.items():
        for bit, (q2, eta, c) in enumerate(EDGES[q]):
            if bit == 0 and last_zero:
                continue
            state = (q2, eta*sign, eta*k+c, int(bit == 0))
            nxt[state] = nxt.get(state, 0) + mass
    dp = nxt

result = {
    'schema': 'EM_R297_FIXED_EFFECT_RANK_INJECTIVITY_V1',
    'status': 'PASS',
    'mathematics': 'conditional on R294 source-to-algebraic-kernel correspondence and square-root transfer',
    'model': 'positive weighted BRC, ordered six edges, forbidden 00, full affine effect, terminal q0',
    'verification': 'independent Python arbitrary-precision integers and exact Q(sqrt(5)) comparator',
    'rank_search_m_up_to': M_BOUND,
    'rank_items_per_parity': [(M_BOUND//2+1)*2, (M_BOUND//2)*2],
    'dp_max_n': LIMIT,
    'global_unique_first_second_checked_n': [81,LIMIT],
    'checked_n_layers': peak_checks,
    'terminal_effect_comparisons': all_effect_count_comparisons,
    'sample_gaps': first_gap,
    'limitations': 'finite scans are independent checks, not proof of global rank injectivity or a uniform n threshold; source generator and singularity expansion remain author-side dependencies'
}
output_path = sys.argv[1] if len(sys.argv) > 1 else 'R297_EXACT_EVIDENCE.json'
with open(output_path,'w',encoding='utf-8') as f:
    json.dump(result,f,ensure_ascii=False,indent=2)
    f.write('\n')
print(json.dumps({'status':result['status'],'peak_checks':peak_checks,'terminal_effect_comparisons':all_effect_count_comparisons,'sample_gaps':first_gap},ensure_ascii=False))
