#!/usr/bin/env python3
"""Exact finite certificate: scalar-symmetric K=562392/8039 has no balanced dual-optimal policy."""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product

N = 14
K = F(562392, 8039)
P = tuple(F(z, 24) for z in (3, 1, 20))
Q = tuple(F(z, 24) for z in (2, 2, 20))
ROOT = (0, 0, 0)
STATES = [(n, a, b) for n in range(N + 1) for a in range(n + 1) for b in range(n - a + 1)]
def child(s, j):
    return (s[0] + 1, s[1] + (j == 0), s[2] + (j == 1))

@lru_cache(None)
def bellman(s):
    n, a, b = s
    acts = {'P': K * F(2 ** (a + b), 3 ** a), 'Q': K}
    if n < N:
        acts['C'] = 1 + sum(P[j] * bellman(child(s, j))[0] for j in range(3))
    m = min(acts.values())
    return m, tuple(act for act, value in acts.items() if value == m), acts

TIES = {s: bellman(s)[1] for s in STATES if len(bellman(s)[1]) > 1}
assert TIES == {(9, 1, 0): ('P', 'C'), (14, 0, 0): ('P', 'Q')}
assert len(STATES) == 680
positive = [v - bellman(s)[0] for s in STATES for v in bellman(s)[2].values() if v > bellman(s)[0]]
assert len(positive) == 1238 and min(positive) == F(11225, 868212)
tie_states = tuple(TIES)

@lru_cache(None)
def errors(s, bits):
    action = TIES[s][bits[tie_states.index(s)]] if s in TIES else bellman(s)[1][0]
    if action != 'C':
        return (F(action == 'Q'), F(action == 'P'))
    children = [errors(child(s, j), bits) for j in range(3)]
    return (sum(P[j] * children[j][0] for j in range(3)),
            sum(Q[j] * children[j][1] for j in range(3)))

expected = {
    (0, 0): F(-1213677595, 6879707136),
    (0, 1): F(-103520966755, 5015306502144),
    (1, 0): F(-116454914635, 743008370688),
    (1, 1): F(-19282695145, 20061226008576),
}
for bits in product((0, 1), repeat=2):
    eP, eQ = errors(ROOT, bits)
    assert eP - eQ == expected[bits] < 0
    print('SYMMETRIC_K_CORNER', ''.join(map(str, bits)), f'{(eP-eQ).numerator}/{(eP-eQ).denominator}')
print('SYMMETRIC_K_NO_BALANCED_OPTIMAL_FACE_PASS')
