#!/usr/bin/env python3
"""Exact rational certificate for the four-signature convex-rate no-go family.

All comparisons are Fraction-exact. Finite strategy sampling is regression,
not the universal proof; see RESEARCH.md.
"""
from fractions import Fraction as F
from random import Random

S = (F(1, 2), F(1), F(3, 2), F(5, 2))
R, RIDX = F(3, 2), 2
ZERO = F(0)
UNIT = tuple(F(int(j == RIDX)) for j in range(4))
W = (F(1, 4), F(1, 3), ZERO, F(5, 12))
V = (F(3), F(-4), ZERO, F(1))
K = tuple(F(3, 5) * (W[j] - UNIT[j]) for j in range(4))
ROOT = (F(1, 4), F(1, 4))
OUTSIDE_Q = F(1, 2)  # likelihood ratio 1/2, mandatory stop at t=1


def vec(*items):
    return tuple(items)


def mass_mean(p):
    return sum(p), sum(s * q for s, q in zip(S, p))


def call(p, t):
    return sum(q * max(ZERO, s - t) for s, q in zip(S, p))


def make_source(c, perturb):
    first = tuple(c * UNIT[j] + (1 - c) * W[j] + perturb * V[j]
                  for j in range(4))
    second = tuple(UNIT[j] + ((1 + c) * K[j] - (first[j] - UNIT[j])) / c
                   for j in range(4))
    first_rate = tuple(first[j] - UNIT[j] for j in range(4))
    gap = tuple(K[j] - first_rate[j] for j in range(4))
    assert all(p > 0 for p in first + second)
    assert mass_mean(first) == (1, R)
    assert mass_mean(second) == (1, R)
    assert first[RIDX] == c
    assert all(call(gap, t) >= 0 for t in S)
    assert mass_mean(gap) == (0, 0)
    full_rate = tuple((first_rate[j] + c * (second[j] - UNIT[j])) / (1 + c)
                      for j in range(4))
    assert full_rate == K
    return (c, first, second, gap)


A = make_source(F(1, 2), F(1, 200))
B = make_source(F(3, 5), -F(1, 200))
SOURCES = (A, B)
EMAX = sum(a * (1 + row[0]) for a, row in zip(ROOT, SOURCES))
assert EMAX == F(31, 40)
assert mass_mean(K) == (0, 0)
assert tuple(K) == (F(3, 20), F(1, 5), -F(3, 5), F(1, 4))
assert A[1][0] * B[1][1] - B[1][0] * A[1][1] == F(9, 1000)
assert (call(A[3], S[1]), call(A[3], S[2])) == (F(1, 200), F(11, 300))
assert (call(B[3], S[1]), call(B[3], S[2])) == (F(13, 400), F(53, 600))


def full_weights(alpha, gamma):
    weights = [ZERO] * len(S)
    weights[0] = OUTSIDE_Q
    extra = ZERO
    for a, row, al, ga in zip(ROOT, SOURCES, alpha, gamma):
        c, mu, sigma, _ = row
        extra += a * al * (1 + c * ga)
        weights[RIDX] += a * (1 - al)
        for j in range(4):
            weights[j] += a * al * (mu[j] - (c * ga if j == RIDX else ZERO)
                                   + c * ga * sigma[j])
    return tuple(weights), extra


def lr_weights(extra):
    assert 0 <= extra <= EMAX
    weights = [extra * x for x in K]
    weights[0] += OUTSIDE_Q
    weights[RIDX] += sum(ROOT)
    alpha = extra / EMAX
    assert 0 <= alpha <= 1
    return tuple(weights), alpha


def test_masses(q):
    assert all(x >= 0 for x in q)
    assert mass_mean(q) == (1, 1)  # Q total and P total


def zonotope_contains(q, pdecl, qdecl):
    """Exact 2D zonotope facet test; generator (s*q_s,q_s)."""
    for t in S:
        z = pdecl - t * qdecl
        low = sum(m * min(ZERO, s - t) for s, m in zip(S, q))
        high = sum(m * max(ZERO, s - t) for s, m in zip(S, q))
        if not low <= z <= high:
            return False
    return True


# A nontrivial exact full-history strategy and a constructive LR label rule.
alpha = (F(1), F(1, 2))
gamma = (ZERO, F(1, 3))
full, e = full_weights(alpha, gamma)
lr, common_alpha = lr_weights(e)
assert e == F(2, 5) and common_alpha == F(16, 31)
test_masses(full)
test_masses(lr)
assert all(lr[j] >= full[j] for j in (1, 3))
prob = {1: full[1] / lr[1], 3: full[3] / lr[3]}
pdecl = sum(S[j] * full[j] for j in (1, 3))
qdecl = sum(full[j] for j in (1, 3))
assert sum(S[j] * lr[j] * prob[j] for j in prob) == pdecl
assert sum(lr[j] * prob[j] for j in prob) == qdecl
OBS = (1 - pdecl, qdecl, 1 + R * e, 1 + e)
assert zonotope_contains(lr, pdecl, qdecl)

# Exact arbitrary source/time-dependent decisions (not just label-wise rules).
rng = Random(20261029)
for trial in range(1400):
    al = (F(rng.randrange(101), 100), F(rng.randrange(101), 100))
    ga = (F(rng.randrange(101), 100), F(rng.randrange(101), 100))
    q = [ZERO] * 4
    pd, qd = ZERO, ZERO
    def push(idx, mass):
        global pd, qd
        assert mass >= 0
        theta = F(rng.randrange(41), 40)
        q[idx] += mass
        qd += mass * theta
        pd += S[idx] * mass * theta
    push(0, OUTSIDE_Q)
    for root, row, aa, gg in zip(ROOT, SOURCES, al, ga):
        c, first, second, _ = row
        push(RIDX, root * (1 - aa))
        for j in range(4):
            if j != RIDX:
                push(j, root * aa * first[j])
        push(RIDX, root * aa * c * (1 - gg))
        for j in range(4):
            push(j, root * aa * c * gg * second[j])
    expected_q, expected_e = full_weights(al, ga)
    assert tuple(q) == expected_q
    lrq, _ = lr_weights(expected_e)
    test_masses(lrq)
    assert zonotope_contains(lrq, pd, qd)
    # Convex-order certificate for arbitrary full policy, checked at all knots.
    assert all(call(lrq, t) >= call(expected_q, t) for t in S)

print('SIGNATURES', S)
print('FIRST_A', A[1])
print('SECOND_A', A[2])
print('FIRST_B', B[1])
print('SECOND_B', B[2])
print('COMMON_INFORMATION_RATE', K)
print('CALL_GAPS_A', tuple(call(A[3], t) for t in S))
print('CALL_GAPS_B', tuple(call(B[3], t) for t in S))
print('RANK_TWO_DETERMINANT', F(9, 1000))
print('MAX_EXTRA_Q_TIME', EMAX)
print('WITNESS_FULL_Q_TERMINAL', full)
print('WITNESS_LR_Q_TERMINAL', lr)
print('WITNESS_EXTRA_Q_TIME', e)
print('WITNESS_LR_ALPHA', common_alpha)
print('WITNESS_LR_DECLARATION_PROBABILITIES', prob)
print('WITNESS_FOUR_OBSERVATIONS', OBS)
print('EXACT_RANDOM_POLICY_CHECKS', 1400)
print('PASS_EXACT_FOUR_SIGNATURE_RANK_TWO_CONVEX_RATE_NO_GO')
