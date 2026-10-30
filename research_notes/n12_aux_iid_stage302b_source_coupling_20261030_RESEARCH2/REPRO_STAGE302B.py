#!/usr/bin/env python3
"""Stage302-B: exact rational audit of source-coupled and posterior repair."""
from fractions import Fraction as F
from itertools import product
from math import comb

P = (F(1, 4), F(3, 4))
HALF = F(1, 2)


def tv(a, b):
    assert a.keys() == b.keys()
    return sum((abs(a[k] - b[k]) for k in a), F(0)) / 2


def pred(d):
    t = F(3) ** d
    return (P[0] + P[1] * t) / (1 + t)


def step_prob(a, y, s):
    v = P[s] if a else HALF
    return v if y else 1 - v


def exact_law(plan, source):
    out = {}
    for x, y, z in product(range(2), repeat=3):
        a = plan[x]
        b = plan[2 + x * 2 + y]
        path = (x, a, y, b, z)
        out[path] = HALF * step_prob(a, y, source) * step_prob(b, z, source)
    assert len(out) == 8 and sum(out.values()) == 1 and all(v > 0 for v in out.values())
    return out


def filter_law(plan):
    out = {}
    for x, y, z in product(range(2), repeat=3):
        a = plan[x]
        b = plan[2 + x * 2 + y]
        d = (2 * y - 1) * a
        q1 = pred(0) if a else HALF
        q2 = pred(d) if b else HALF
        out[(x, a, y, b, z)] = HALF * (q1 if y else 1 - q1) * (q2 if z else 1 - q2)
    assert sum(out.values()) == 1
    return out


def law_k(s, k):
    out = {}
    for word in product(range(2), repeat=k):
        j = sum(word)
        out[word] = P[s] ** j * (1 - P[s]) ** (k - j)
    assert sum(out.values()) == 1
    return out


def binomial_tv_formula(k):
    upper_tail = sum((F(comb(k, j), 1) * P[0] ** j * (1 - P[0]) ** (k - j)
                      for j in range(k // 2 + 1, k + 1)), F(0))
    tie = (F(comb(k, k // 2), 1) * P[0] ** (k // 2) * (1 - P[0]) ** (k // 2)) if k % 2 == 0 else F(0)
    return 1 - tie - 2 * upper_tail


def main():
    total_positive = 0
    max_risk = F(0)
    for plan in product(range(2), repeat=6):
        p0 = exact_law(plan, 0)
        p1 = exact_law(plan, 1)
        q = filter_law(plan)
        for key in p0:
            assert q[key] == (p0[key] + p1[key]) / 2
        risk = (tv(p0, q) + tv(p1, q)) / 2
        assert risk == tv(p0, p1) / 2
        max_risk = max(max_risk, risk)
        total_positive += len(p0) * 2
    assert max_risk == F(1, 4)

    rows = []
    for k in range(1, 8):
        v = tv(law_k(0, k), law_k(1, k))
        assert v == binomial_tv_formula(k)
        assert all(pred(2 * j - k) != pred(2 * m - k)
                   for j in range(k + 1) for m in range(j))
        rows.append((k, str(v), str(v / 2)))
    assert rows[:4] == [(1, '1/2', '1/4'), (2, '1/2', '1/4'),
                        (3, '11/16', '11/32'), (4, '11/16', '11/32')]
    assert (P[0] ** 2 + P[1] ** 2) / 2 - HALF ** 2 == F(1, 16)
    for q0, q1 in [(F(0), F(1)), (HALF, HALF), (F(1, 8), F(7, 8))]:
        risk = (abs(P[0] - (P[0] + (P[1]-P[0]) * q0))
                + abs(P[1] - (P[0] + (P[1]-P[0]) * q1))) / 2
        assert risk == (q0 + 1 - q1) / 4
    mismatch = {(s, j): (HALF if s == j else F(0)) for s, j in product(range(2), repeat=2)}
    independent = {(s, j): F(1, 4) for s, j in product(range(2), repeat=2)}
    assert tv(mismatch, independent) == HALF
    print('deterministic_policies=64; source_positive_paths_checked=', total_positive)
    print('adaptive_two_round_source_blind_tagged_minimax=', max_risk)
    print('k,TV(P0^k,P1^k),source_blind_tagged_optimal_risk=', rows)
    print('shared_parameter_two_draw_covariance=1/16; minimal_latent_states=2')
    print('independent_S_J_joint_TV=1/2; all_rational_checks=PASS')
    print('STAGE302B_SOURCE_COUPLING_POSTERIOR_EXACT_PASS')


if __name__ == '__main__':
    main()
