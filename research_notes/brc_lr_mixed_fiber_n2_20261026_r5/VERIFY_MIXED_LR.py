"""Exact 8-leaf horizon-two mixed likelihood-ratio witness.

Only uses Python standard library Fraction. No external/probabilistic approximation.
"""
from fractions import Fraction as F
from itertools import product

q = {'a': F(1, 8), 'b': F(1, 8), 'c': F(1, 4), 'd': F(1, 2)}
l = {'a': F(1), 'b': F(1), 'c': F(2), 'd': F(1, 2)}
p = {h: q[h] * l[h] for h in q}
qp = {h: (F(1, 2), F(1, 2)) for h in q}
pp = {h: ((F(3, 4), F(1, 4)) if h == 'a' else qp[h]) for h in q}
leaves = {(h, i): (q[h] * qp[h][i], p[h] * pp[h][i])
          for h in q for i in (0, 1)}
ratio = {k: pv / qv for k, (qv, pv) in leaves.items()}
first_levels = sorted(set(l.values()))
last_levels = sorted(set(ratio.values()))
assert sum(q.values()) == sum(p.values()) == 1
assert sum(z[0] for z in leaves.values()) == sum(z[1] for z in leaves.values()) == 1
assert all(qv > 0 and pv > 0 for qv, pv in leaves.values())
assert first_levels == [F(1, 2), F(1), F(2)]
assert last_levels == [F(1, 2), F(1), F(3, 2), F(2)]
assert ratio['a', 0] == F(3, 2) and ratio['a', 1] == F(1, 2)
assert ratio['b', 0] == ratio['b', 1] == F(1)

# J=eP+eQ+(1/8)tQ. At first node m=min(L,1),
# continuation is 1/8+E_Q[min(R,1)|h].
C, D = F(0), F(1, 8)
m = {h: min(l[h], F(1)) for h in q}
f = {h: sum(qp[h][i] * min(ratio[h, i], F(1)) for i in (0, 1)) for h in q}
d = {h: m[h] - f[h] for h in q}
assert f == {'a': F(3, 4), 'b': F(1), 'c': F(1), 'd': F(1, 2)}
assert d == {'a': F(1, 4), 'b': F(0), 'c': F(0), 'd': F(0)}
full_first = sum(q[h] * min(m[h], (C * l[h] + D) + f[h]) for h in q)
full_value = min(F(1), C + D + full_first)
q_levels = {v: sum(q[h] for h in q if l[h] == v) for v in first_levels}
compressed_first = sum(min(q_levels[v] * min(v, F(1)),
                           sum(q[h] * ((C * v + D) + f[h]) for h in q if l[h] == v))
                       for v in first_levels)
compressed_value = min(F(1), C + D + compressed_first)
assert (full_value, compressed_value, compressed_value - full_value) == (
    F(55, 64), F(7, 8), F(1, 64))

# Decisions P and Q are read as the final declaration, not the true law.
def observe(root_action, first_action, terminal_action):
    eP = eQ = tP = tQ = F(0)
    if root_action != 'C':
        if root_action == 'Q': eP = F(1)
        else: eQ = F(1)
        return (eP, eQ, tP, tQ)
    for h in q:
        action = first_action(h)
        if action != 'C':
            if action == 'Q': eP += p[h]
            else: eQ += q[h]
            tP += p[h]; tQ += q[h]
        else:
            tP += 2 * p[h]; tQ += 2 * q[h]
            for i in (0, 1):
                qv, pv = leaves[h, i]
                if terminal_action(h, i) == 'Q': eP += pv
                else: eQ += qv
    return (eP, eQ, tP, tQ)

def score(o):
    return o[0] + o[1] + C * o[2] + D * o[3]

full_decisions = {'a': 'C', 'b': 'P', 'c': 'P', 'd': 'Q'}
full_obs = observe('C', lambda h: full_decisions[h],
                   lambda h, i: 'P' if ratio[h, i] >= 1 else 'Q')
assert full_obs == (F(9, 32), F(7, 16), F(9, 8), F(9, 8))
assert score(full_obs) == full_value

# Exhaust all 3 * (3^3) * (2^4) = 1296 deterministic LR-only
# action tables. Their convex hull contains all randomized LR-only policies.
minimum = None
num = 0
for root in ('P', 'Q', 'C'):
    for first in product(('P', 'Q', 'C'), repeat=len(first_levels)):
        fdict = dict(zip(first_levels, first))
        for terminal in product(('P', 'Q'), repeat=len(last_levels)):
            tdict = dict(zip(last_levels, terminal))
            obs = observe(root, lambda h: fdict[l[h]],
                          lambda h, i: tdict[ratio[h, i]])
            val = score(obs)
            minimum = val if minimum is None else min(minimum, val)
            num += 1
assert num == 1296 and minimum == F(7, 8)

# Exhaust all deterministic full-history tables as a second certificate.
minimum_full = None
num_full = 0
for root in ('P', 'Q', 'C'):
    for first in product(('P', 'Q', 'C'), repeat=len(q)):
        fdict = dict(zip(q, first))
        for terminal in product(('P', 'Q'), repeat=len(leaves)):
            tdict = dict(zip(leaves, terminal))
            obs = observe(root, lambda h: fdict[h],
                          lambda h, i: tdict[h, i])
            val = score(obs)
            minimum_full = val if minimum_full is None else min(minimum_full, val)
            num_full += 1
assert num_full == 62208 and minimum_full == F(55, 64)

print('MODEL: strictly positive exact rational N=2, 4 first histories, 8 leaves')
print('FIRST_LR:', l)
print('TERMINAL_LR:', ratio)
print('FIRST_CONTINUATION_DEFICIT:', d)
print('FULL_POLICY_OBSERVERS:', full_obs)
print('FULL_BELLMAN_OPTIMUM:', full_value)
print('LR_ONLY_BELLMAN_OPTIMUM:', compressed_value)
print('STRICT_GAP:', compressed_value - full_value)
print('EXHAUSTIVE_LR_DETERMINISTIC:', num, 'minimum', minimum)
print('EXHAUSTIVE_FULL_DETERMINISTIC:', num_full, 'minimum', minimum_full)
print('STATUS: PASS (exact Fraction; no floating point)')
