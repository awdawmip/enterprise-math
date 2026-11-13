#!/usr/bin/env python3
"""Exact finite R749N checker; Python standard library only.
Exhaustive 60 signed-Port pairs, 960 edges, n=2,3,4 all blocks.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations
from math import comb
import json

PORTS = tuple((i, s) for i in range(6) for s in (-1, 1))
V = tuple(frozenset((a, b)) for a, b in combinations(PORTS, 2) if a[0] != b[0])

def adjacent(v, w):
    return len(v & w) == 1 and len({a[0] for a in v | w}) == 3

N = {v: tuple(w for w in V if adjacent(v, w)) for v in V}

def forced(u, v):
    return u ^ v

assert len(V) == 60 and all(len(N[v]) == 16 for v in V)
assert all(forced(u, v) in N[v] for v in V for u in N[v])
assert all(forced(forced(u, v), v) == u for v in V for u in N[v])

# Precisely one incoming forced predecessor for every target (v,w).
for v in V:
    for w in N[v]:
        assert sum(forced(u, v) == w for u in N[v]) == 1

counts, reverse_checks = {}, {}
for n in (2, 3, 4):
    blocks = [(u, v) for u in V for v in N[u]]
    for _ in range(2, n):
        blocks = [b + (w,) for b in blocks for w in N[b[-1]]]
    def good(b):
        return sum(b[t] == forced(b[t - 2], b[t - 1]) for t in range(2, len(b)))
    hist = Counter(good(b) for b in blocks)
    expected = {k: 960 * comb(n - 2, k) * 15 ** (n - 2 - k) for k in range(n - 1)}
    assert dict(hist) == expected, (n, hist, expected)
    assert all(good(b) == good(b[::-1]) for b in blocks)
    counts[str(n)] = {str(k): v for k, v in sorted(hist.items())}
    reverse_checks[str(n)] = len(blocks)

probabilities = {}
for p in (Q(0), Q(1, 4), Q(1, 2), Q(1)):
    q = (1 + 15 * p) / 16
    r = (1 - p) / 16
    assert q + 15 * r == 1
    m = 2
    binomial = [Q(comb(m, k)) * q**k * (1 - q)**(m - k) for k in range(m + 1)]
    assert sum(binomial) == 1
    assert sum(Q(counts['4'][str(k)], 960) * q**k * r**(m - k) for k in range(m + 1)) == 1
    probabilities[str(p)] = {
        'forced_probability': str(q),
        'each_deviation_probability': str(r),
        'K_distribution_n4': [str(x) for x in binomial],
        'TV_pure_retained_n4': str(1 - q**2)
    }

a = Q(1, 16)
def beta_tail_integral(power, rem):
    return sum(Q((-1)**j * comb(rem, j)) * (1 - a**(power + j + 1)) / (power + j + 1)
               for j in range(rem + 1))

posterior_mean = {}
for m in range(4):
    for k in range(m + 1):
        posterior_mean[f'{m}:{k}'] = str(beta_tail_integral(k + 1, m - k) /
                                       beta_tail_integral(k, m - k))
assert posterior_mean['0:0'] == '17/32'
assert posterior_mean['1:0'] == '3/8'
assert posterior_mean['1:1'] == '91/136'

result = {
    'schema': 'EM_R749N_NOISY_C1_EXACT_CHECK_V1',
    'status': 'PASS',
    'vertices': len(V),
    'directed_edges': sum(map(len, N.values())),
    'exhaustive_block_K_histograms': counts,
    'exhaustive_reversal_checks': reverse_checks,
    'rational_p_cases_n4': probabilities,
    'uniform_p_prior_posterior_mean_q': posterior_mean,
    'native_event_permission': False,
    'task_claim': False,
}
print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
