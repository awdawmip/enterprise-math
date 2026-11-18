#!/usr/bin/env python3
"""R749SUP exact integer regression for the O(M^(3/4)) short-interval optimizer.
The all-M theorem rests on the companion paper's analytic inequalities.
"""
from math import isqrt
import json


def near_product(M):
    t = isqrt(M + 1)
    assert t >= 100
    k = M + 1 - t * t
    j = 1 if k <= t else 2
    z = 0
    while z * (z + j) < j * t - k:
        z += 1
    r, s = t - z, t + z + j
    p = r * s - 1
    delta = M - p
    c = isqrt(t) + (isqrt(t) ** 2 != t)
    assert 0 <= delta <= 2 * c + 1
    assert (c + 1) ** 2 < 2 * (t - c)
    assert p * (p - r) * (p - s) > 0
    assert (p-r)*(p-s) - p*(p-r-s+1) == 1
    # A sufficient integer inequality for 20 B < M, with B <= 2t+6c+13.
    assert 20 * (2 * t + 6 * c + 13) < M
    return p, delta, t, z


def closest_factor(n):
    for x in range(isqrt(n), 1, -1):
        if n % x == 0:
            y = n // x
            if n - x - y >= 1:
                return x, y
            return None
    return None


def short_optimizer(M):
    p, delta, t, z = near_product(M)
    best = -1
    winners = []
    for n in range(p + 1, M + 2):
        xy = closest_factor(n)
        if xy is None:
            continue
        x, y = xy
        score = (n - 1) * (n - x - 1) * (n - y - 1)
        if score > best:
            best, winners = score, []
        if score == best:
            winners.append((n, x, y))
    return best, winners, delta, t


def all_prefix_by_sieve(N):
    closest = [0] * (N + 2)
    for x in range(2, isqrt(N + 1) + 1):
        for n in range(x * x, N + 2, x):
            closest[n] = x
    scores = [-1] * (N + 1)
    counts = [0] * (N + 1)
    best, count = -1, 0
    for M in range(2, N + 1):
        n = M + 1
        x = closest[n]
        if x:
            y = n // x
            if n - x - y >= 1:
                score = (n - 1) * (n - x - 1) * (n - y - 1)
                labeled = 2 if x == y else 4
                if score > best:
                    best, count = score, 0
                if score == best:
                    count += labeled
        scores[M], counts[M] = best, count
    return scores, counts


def verify(N=25000):
    scores, counts = all_prefix_by_sieve(N)
    max_delta = -1
    max_lower_slack = -1
    tests = 0
    samples = {}
    for M in range(9999, N + 1):
        score, wins, delta, t = short_optimizer(M)
        labeled = sum(2 if x == y else 4 for n, x, y in wins)
        assert score == scores[M], (M, score, scores[M])
        assert labeled == counts[M], (M, labeled, counts[M])
        assert all(M + 1 - n <= delta for n, x, y in wins)
        max_delta = max(max_delta, delta)
        max_lower_slack = max(max_lower_slack, max(delta - (M + 1 - n) for n, x, y in wins))
        if M in {9999, 10000, 12000, 17000, 25000}:
            samples[str(M)] = dict(score=score, delta=delta, winners=wins)
        tests += 1
    return {
        'record': 'R749SUP',
        'status': 'PASS',
        'arithmetic': 'exact integers only',
        'finite_band': f'9999..{N}',
        'tested_scales': tests,
        'score_and_labeled_ties_match': True,
        'maximum_competitor_gap_M_minus_p': max_delta,
        'maximum_observed_delta_minus_optimal_port_gap': max_lower_slack,
        'samples': samples,
        'infinite_proof': 'analytic closest-factor continuous envelope, derivative lower bound, and near-product witness',
        'complexity': 'O(M^(3/4)) arithmetic operations, O(1) working memory excluding winner output',
        'not_reviewed': True,
    }


if __name__ == '__main__':
    print(json.dumps(verify(), indent=2, ensure_ascii=False))
