#!/usr/bin/env python3
"""Stage305-B exact external positive-rational BRC-style branch audit.

This is NOT an execution of a typed native P000-X6/BRC arithmetic kernel.
The source S is a fair bit. J is its persistent noisy label, W a later noisy
signal, and Y1 an original F output. The simulator controls only subsequent
visits. A public examiner adapts to (W,Y1,prior actions and outputs), not S/J.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import prod

BITS = (0, 1)
P = (F(1, 4), F(3, 4))
J_ONE = (F(1, 8), F(7, 8))  # Pr(J=1 | S=s)
R = F(3, 4)                 # Pr(W=S | S)
T_PUBLIC = {               # (W,Y1): (rate if J=0, rate if J=1)
    (0, 0): (F(9, 40), F(3, 5)),
    (0, 1): (F(1, 4), F(3, 4)),
    (1, 0): (F(1, 4), F(3, 4)),
    (1, 1): (F(2, 5), F(31, 40)),
}


def bern(p, bit):
    return p if bit else 1 - p


# Unnormalized positive rational mass of the shared, immutable prefix.
PREFIX = defaultdict(lambda: [F(0), F(0)])
for s, j, w, y1 in product(BITS, repeat=4):
    PREFIX[(j, w, y1)][s] += (
        F(1, 2) * bern(J_ONE[s], j)
        * (R if w == s else 1 - R) * bern(P[s], y1)
    )
assert all(x > 0 for v in PREFIX.values() for x in v)
assert sum(sum(v) for v in PREFIX.values()) == 1


def posterior(j, w, y1):
    a, b = PREFIX[j, w, y1]
    return b / (a + b)


def mean_rate(j, w, y1):
    u = posterior(j, w, y1)
    return (1 - u) * P[0] + u * P[1]


def output_law(model, s, j, w, y1, policy, y2, y3):
    """Exact probability of two outputs for a chosen public local policy."""
    a2, a3_if_0, a3_if_1 = policy
    a3 = a3_if_1 if y2 else a3_if_0
    h = (j, w, y1)
    if model == 'ideal':
        rate2 = rate3 = P[s]
    elif model == 'mean_frozen':
        rate2 = rate3 = mean_rate(*h)
    elif model == 'J_two_moment':
        rate2 = rate3 = T_PUBLIC[w, y1][j]
    elif model == 'sequential_posterior':
        rate2 = mean_rate(*h)
        if a2 == 1:  # An F bit updates S posterior. H is source-free.
            a, b = PREFIX[h]
            ap = a * bern(P[0], y2)
            bp = b * bern(P[1], y2)
            u2 = bp / (ap + bp)
            rate3 = (1 - u2) * P[0] + u2 * P[1]
        else:
            rate3 = rate2
    else:
        raise ValueError(model)
    p2 = bern(rate2 if a2 else F(1, 2), y2)
    p3 = bern(rate3 if a3 else F(1, 2), y3)
    return p2 * p3


def local_tv(model, g, policy, fields):
    """TV contribution for one disjoint public prefix g=(W,Y1)."""
    p_dist, q_dist = defaultdict(F), defaultdict(F)
    w, y1 = g
    for j, s, y2, y3 in product(BITS, repeat=4):
        prefix = PREFIX[j, w, y1][s]
        a2, a3_if_0, a3_if_1 = policy
        a3 = a3_if_1 if y2 else a3_if_0
        event = dict(s=s, j=j, w=w, y1=y1, a2=a2, y2=y2, a3=a3, y3=y3)
        key = tuple(event[f] for f in fields)
        p_dist[key] += prefix * output_law('ideal', s, j, w, y1, policy, y2, y3)
        q_dist[key] += prefix * output_law(model, s, j, w, y1, policy, y2, y3)
    assert sum(p_dist.values()) == sum(q_dist.values()) == sum(
        sum(PREFIX[j, w, y1]) for j in BITS
    )
    return sum(abs(p_dist[k] - q_dist[k]) for k in p_dist.keys() | q_dist.keys()) / 2


PUBLIC_G = tuple(product(BITS, repeat=2))
LOCAL_POLICIES = tuple(product(BITS, repeat=3))
ALL_F = (1, 1, 1)
FIELDS = {
    'W': ('w', 'y1', 'a2', 'y2', 'a3', 'y3'),
    'J': ('j', 'w', 'y1', 'a2', 'y2', 'a3', 'y3'),
    'S': ('s', 'w', 'y1', 'a2', 'y2', 'a3', 'y3'),
    'SJ': ('s', 'j', 'w', 'y1', 'a2', 'y2', 'a3', 'y3'),
}
EXPECTED = {
    'mean_frozen': {'W': F(651, 16384), 'J': F(651, 16384),
                    'S': F(3255, 32768), 'SJ': F(3255, 32768)},
    'sequential_posterior': {'W': F(0), 'J': F(0),
                             'S': F(651, 8192), 'SJ': F(651, 8192)},
    'J_two_moment': {'W': F(0), 'J': F(111, 1600),
                     'S': F(5487, 102400), 'SJ': F(549, 6400)},
}
for model, by_observer in EXPECTED.items():
    for obs, fields in FIELDS.items():
        risks = {
            g: {pol: local_tv(model, g, pol, fields) for pol in LOCAL_POLICIES}
            for g in PUBLIC_G
        }
        all_f = sum(risks[g][ALL_F] for g in PUBLIC_G)
        assert all_f == by_observer[obs], (model, obs, all_f, by_observer[obs])
        # All 8^4=4096 deterministic publicly adaptive two-step policies.
        all_risks = (
            sum(risks[g][pol] for g, pol in zip(PUBLIC_G, choices))
            for choices in product(LOCAL_POLICIES, repeat=4)
        )
        assert max(all_risks) == all_f
        print(f'EXACT_ADAPTIVE_MINIMAX model={model} observer={obs} TV={all_f}')

# Verify the public two-moment construction for every W,Y1 branch.
for w, y1 in PUBLIC_G:
    masses = [sum(PREFIX[j, w, y1]) for j in BITS]
    total = sum(masses)
    target_moments = [
        sum(PREFIX[j, w, y1][s] * P[s]**k
            for j, s in product(BITS, repeat=2)) / total
        for k in range(1, 4)
    ]
    simulated_moments = [
        sum(masses[j] * T_PUBLIC[w, y1][j]**k for j in BITS) / total
        for k in range(1, 4)
    ]
    assert target_moments[:2] == simulated_moments[:2]
    delta3 = target_moments[2] - simulated_moments[2]
    expected = { (0, 0): F(63, 16000), (0, 1): F(0),
                 (1, 0): F(0), (1, 1): -F(63, 16000) }[w, y1]
    assert delta3 == expected
    print(f'PUBLIC_MOMENTS W={w} Y1={y1} prefix_mass={total} '
          f'm1={target_moments[0]} m2={target_moments[1]} delta_m3={delta3}')

# On three future F visits, the first two moments remain identical while
# each of 8 ordered words has signed difference +/-delta_m3.
original_3, repaired_3 = defaultdict(F), defaultdict(F)
for (j, w, y1), ws in PREFIX.items():
    t = T_PUBLIC[w, y1][j]
    for s in BITS:
        for word in product(BITS, repeat=3):
            key = (w, y1) + word
            original_3[key] += ws[s] * prod(bern(P[s], b) for b in word)
            repaired_3[key] += ws[s] * prod(bern(t, b) for b in word)
assert sum(original_3.values()) == sum(repaired_3.values()) == 1
three_tv = sum(abs(original_3[k] - repaired_3[k]) for k in original_3) / 2
assert three_tv == F(63, 6400)
print(f'THREE_F_PUBLIC_EXACT_TV={three_tv}')

# Analytic identity for mean freeze (per terminal J history):
# TV(M_u, Bern(mean p)^2)=u(1-u)/2.
mean_formula = sum(
    sum(masses) * (masses[1] / sum(masses))
    * (masses[0] / sum(masses)) / 2
    for masses in PREFIX.values()
)
assert mean_formula == F(651, 16384)

# Exact optimized terminal-J audit risk under arbitrary per-history fixed
# Bernoulli t in [0,1]: R* = -89/64+sqrt(142)/16+3sqrt(2)/8+sqrt(22)/32.
# Its global optimality is proved algebraically in PROOF_STAGE305B.md.
from sympy import Rational, sqrt, simplify  # exact radical cross-check
opt = 0
for masses in PREFIX.values():
    total = sum(masses)
    u = Rational(masses[1].numerator, masses[1].denominator) / Rational(total.numerator, total.denominator)
    v = min(u, 1 - u)
    opt += Rational(total.numerator, total.denominator) * (v - Rational(3, 2) + sqrt(9-8*v)/2)
closed = -Rational(89, 64) + sqrt(142)/16 + 3*sqrt(2)/8 + sqrt(22)/32
assert simplify(opt - closed) == 0
assert 0 < opt.evalf(30) < float(mean_formula)
print(f'OPTIMAL_FIXED_RATE_J_AUDIT={closed} APPROX={opt.evalf(16)}')
print('STAGE305B_NOISY_POSTERIOR_MOMENT_EXACT_PASS')
