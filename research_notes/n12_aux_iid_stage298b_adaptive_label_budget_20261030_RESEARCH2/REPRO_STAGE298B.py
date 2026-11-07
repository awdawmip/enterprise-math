#!/usr/bin/env python3
"""Stage298-B exact rational BRC-style two-visit adaptive-query witness.

This is an external finite source-labelled positive-path model; not native X6.
All arithmetic that supports the exact witness uses fractions.Fraction.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product, combinations

SOURCES = (0, 1, 2)
ACTIONS = ('B', 'C')
WEIGHT = F(1, 3)


def source_branches(s):
    # Positive source/U branch masses. A is the initial observation.
    if s == 2:
        return [(2, F(1))]
    return [(0, F(1, 2)), (1, F(1, 2))]


def response(s, a, action):
    if s == 1:
        return int((a == 0 and action == 'B') or
                   (a == 1 and action == 'C'))
    return 0


def law(s, policy):
    # The path observer retains (first output A, second action, second output Y).
    d = defaultdict(F)
    for a, w in source_branches(s):
        act = policy[a]
        d[(a, act, response(s, a, act))] += w
    assert sum(d.values(), F(0)) == 1
    assert all(w > 0 for w in d.values())
    return dict(d)


def mix(lhs, rhs):
    keys = set(lhs) | set(rhs)
    return {k: (lhs.get(k, F(0)) + rhs.get(k, F(0))) / 2
            for k in keys}


def tv(p, q):
    keys = set(p) | set(q)
    return sum((abs(p.get(k, F(0)) - q.get(k, F(0)))
                for k in keys), F(0)) / 2


def pair_cost(pair, policy):
    # Group two equal-weight sources at one label, singleton at other.
    a, b = pair
    pa, pb = law(a, policy), law(b, policy)
    q = mix(pa, pb)  # One globally specified causal simulator via latent 50/50 source.
    return WEIGHT * (tv(pa, q) + tv(pb, q))


def pair_lower_bound(pair, policy):
    # Triangle inequality: weighted conditional TV >= weight * TV(P_a,P_b).
    a, b = pair
    return WEIGHT * tv(law(a, policy), law(b, policy))


def prefix_a_tv(s, t):
    ds = dict(source_branches(s))
    dt = dict(source_branches(t))
    return tv(ds, dt)


policies = list(product(ACTIONS, repeat=3))  # action for A=0,1,2.
nonadaptive = [('B',) * 3, ('C',) * 3]
assert len(policies) == 8
pairs = list(combinations(SOURCES, 2))

assert prefix_a_tv(0, 1) == 0
assert prefix_a_tv(0, 2) == prefix_a_tv(1, 2) == 1

for pair in pairs:
    for policy in policies:
        assert pair_cost(pair, policy) == pair_lower_bound(pair, policy)
        assert pair_cost(pair, policy) >= 0

# The exact complete finite policy table and both optimizations.
max_adaptive = {pair: max(pair_cost(pair, p) for p in policies) for pair in pairs}
max_fixed = {pair: max(pair_cost(pair, p) for p in nonadaptive) for pair in pairs}
assert max_adaptive == {(0, 1): F(1, 3), (0, 2): F(1, 3), (1, 2): F(1, 3)}
assert max_fixed == {(0, 1): F(1, 6), (0, 2): F(1, 3), (1, 2): F(1, 3)}
assert min(max_adaptive.values()) == F(1, 3)
assert min(max_fixed.values()) == F(1, 6)

p_star = ('B', 'C', 'B')
assert tv(law(0, p_star), law(1, p_star)) == 1
assert tv(law(0, nonadaptive[0]), law(1, nonadaptive[0])) == F(1, 2)
assert tv(law(0, nonadaptive[1]), law(1, nonadaptive[1])) == F(1, 2)

# Check BRC exact path mass for each source, each adaptive policy and each
# distinct branch; tags (source, A, action, second output) remain explicit.
weighted_path_count = 0
for p in policies:
    total_source_tagged = F(0)
    for s in SOURCES:
        for h, w in law(s, p).items():
            assert w > 0
            total_source_tagged += WEIGHT * w
            weighted_path_count += 1
    assert total_source_tagged == 1
assert weighted_path_count == 8 * (2 + 2 + 1) == 40

# The parabola contains infinitely many distinct exposed lower-bound points:
# for each rational t in (0,1), (m1,m2)=(t,t*t) is attained by delta_t;
# the variance identity m2-m1*m1=0 forces a point mass. Strictly positive
# rational mixtures exhibit the interior m1*m1<m2<m1.
for t in (F(1, 7), F(1, 3), F(1, 2), F(2, 3), F(6, 7)):
    m1, m2 = t, t*t
    assert m1*m1 == m2 and m2 < m1
    assert (F(1) - 2*t + m2) + 2*(m1-m2) + m2 == 1
    assert m1-m2 > 0  # two ordered asymmetric outcomes each have this mass

print('source_prefix_A: TV_01=0, TV_02=1, TV_12=1')
print('pair_max_adaptive:', {str(k): str(v) for k, v in max_adaptive.items()})
print('pair_max_nonadaptive:', {str(k): str(v) for k, v in max_fixed.items()})
print('global_k2_minimax_adaptive=1/3')
print('global_k2_minimax_nonadaptive=1/6')
print('strict_gap=1/6')
print('positive_source_tagged_leaf_occurrences=40; all_per_policy_probability=1')
print('shared_iid_moment_boundary_checked=5 rational point masses')
print('STAGE298B_ADAPTIVE_TWO_LABEL_EXACT_PASS')
