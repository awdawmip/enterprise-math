#!/usr/bin/env python3
"""R143B exact periodic slack growth and asymptotic lift-count regression."""
from fractions import Fraction
from math import lcm
from random import Random
from check_r143 import observed


def data(K, word):
    m = len(word)
    L = K - 1
    assert K >= 2
    s = [0]
    for b in word:
        s.append(s[-1] + b)
    low, high = 0, L - 1
    alpha, beta = Fraction(0), Fraction(1)
    for i in range(m + 1):
        for j in range(i + 1, m + 1):
            h = j - i
            d = s[j] - s[i]
            alpha = max(alpha, Fraction(d - 1, h))
            beta = min(beta, Fraction(d + 1, h))
            B = L * (d - 1) + i * s[j] - j * (s[i] + 1)
            A = L * (d + 1) + i * (s[j] + 1) - j * s[i]
            low = max(low, B // h + 1)
            high = min(high, -((-A) // h) - 1)
    return low, high, alpha, beta


def run():
    rng = Random(20261114)
    result = {
        "status": "R143B_PERIODIC_LIFT_MULTIPLICITY_PASS",
        "random_words": 0,
        "periodic_slack_checks": 0,
        "positive_lift_growth_checks": 0,
        "absolute_asymptotic_bound_checks": 0,
        "large_coefficient_checks": 0,
    }
    for m in range(1, 19):
        P = lcm(*range(1, m + 1))
        M = m * (m + 1) + 1
        for z in range(100):
            if z < 50:
                K = rng.randint(2, 10000)
                theta = Fraction(rng.randint(1, 20000), 20003)
                w = observed(K, m, theta)
            else:
                K = rng.randint(2, 10000)
                w = tuple(rng.getrandbits(1) for _ in range(m))
            n0, n1, alpha, beta = data(K, w)
            n0p, n1p, ap, bp = data(K + P, w)
            assert (alpha, beta) == (ap, bp)
            assert n0p <= n0 + P * alpha
            assert n1p >= n1 + P * beta
            result["periodic_slack_checks"] += 1
            if alpha < beta and n0 <= n1:
                assert n1p - n0p + 1 >= n1 - n0 + 1 + P * (beta - alpha)
                result["positive_lift_growth_checks"] += 1
            if alpha < beta:
                C = max(0, n1 - n0 + 1)
                assert abs(C - Fraction(K - 1) * (beta - alpha)) <= 2 * M + 1
                result["absolute_asymptotic_bound_checks"] += 1
            result["random_words"] += 1
    for m in (10, 20, 30, 40):
        for _ in range(25):
            K = 10 ** 80 + rng.randint(2, 100000)
            theta = Fraction(rng.randint(1, 100000), 100003)
            w = observed(K, m, theta)
            n0, n1, alpha, beta = data(K, w)
            assert alpha < beta and n0 <= n1
            C = n1 - n0 + 1
            assert abs(C - (K - 1) * (beta - alpha)) <= 2 * m * (m + 1) + 3
            result["large_coefficient_checks"] += 1
    print(result)


if __name__ == "__main__":
    run()
