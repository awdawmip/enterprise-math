#!/usr/bin/env python3
"""X6 R63: conditional positive-BRC star moments with common additive bias.

Exact integer/rational test only; no native heartbeat/time or physical model is executed.
"""
from fractions import Fraction
from itertools import product
from math import comb, factorial
import json


def signed_stirling_first(D):
    s = [[0] * (D + 1) for _ in range(D + 1)]
    s[0][0] = 1
    for k in range(1, D + 1):
        for t in range(1, k + 1):
            s[k][t] = s[k - 1][t - 1] - (k - 1) * s[k - 1][t]
    return s


def moment(c, t):
    return sum(cd * d ** t for d, cd in enumerate(c))


def restore_high_degrees(y):
    """y[t-1] = m_t + common bias, exact or noisy.

    Computes B_2..B_D (rational) then triangular inverse.
    Caller rounds B first for the noisy version.
    """
    D = len(y)
    s = signed_stirling_first(D)
    B = [Fraction(0)] * (D + 1)
    for k in range(2, D + 1):
        B[k] = sum(s[k][t] * y[t - 1] for t in range(1, k + 1)) / factorial(k)
    return B


def high_from_binomial(B):
    D = len(B) - 1
    c = [0] * (D + 1)
    for d in range(D, 1, -1):
        c[d] = B[d] - sum(comb(k, d) * c[k] for k in range(d + 1, D + 1))
    return c[2:]


def histograms(D, p):
    def rec(n, s):
        if n == 1:
            yield (s,)
            return
        for a in range(s + 1):
            for more in rec(n - 1, s - a):
                yield (a,) + more
    return rec(D + 1, p)


def branch_star_mass(S, t):
    """Literal typed successful AB branches, t independently reset trials.

    The common first Port i is part of the named cross-trial predicate.
    """
    if t == 0:
        return len(S)  # known p, a formal observer convention, not a trial
    p = len(S)
    total = 0
    for i in range(p):
        for choices in product(range(p), repeat=t):
            if all(S[i][j] == 1 for j in choices):
                total += 1
    return total


def near_int(x):
    return (x + Fraction(1, 2)).numerator // (x + Fraction(1, 2)).denominator


def run():
    exact_cases = noisy_cases = branch_cases = 0
    observations = []
    for D in range(1, 7):
        for p in range(D, min(8, D + 2) + 1):
            for c in histograms(D, p):
                m = [moment(c, t) for t in range(1, D + 1)]
                for b in (-13, 0, 7):
                    y = [Fraction(mt + b) for mt in m]
                    B = restore_high_degrees(y)
                    rec_raw = high_from_binomial(B)
                    assert all(x.denominator == 1 for x in rec_raw)
                    rec = [int(x) for x in rec_raw]
                    assert rec == list(c[2:]), (D, p, c, b, rec)
                    low_count = p - sum(rec)
                    assert low_count == c[0] + c[1]
                    beta = y[0] - sum(d * c[d] for d in range(2, D + 1))
                    assert beta == c[1] + b
                    for c1 in range(low_count + 1):
                        cc = [low_count - c1, c1] + rec
                        bb = beta - c1
                        assert [moment(cc, t) + bb for t in range(1, D + 1)] == y
                    exact_cases += 1
                # Every B_k error <= 2/5 when each observed y_t error <= 2/5;
                # integer rounding then recovers c_2,...,c_D exactly.
                y = [Fraction(mt) + Fraction(5, 7) + ((-1) ** t) * Fraction(2, 5)
                     for t, mt in enumerate(m, 1)]
                B = restore_high_degrees(y)
                B_round = [Fraction(0), Fraction(0)] + [Fraction(near_int(B[k])) for k in range(2, D + 1)]
                assert high_from_binomial(B_round) == list(c[2:])
                noisy_cases += 1
    # Independent literal enumeration of the actual named positive AB branches.
    for p in range(1, 4):
        for bits in product((0, 1), repeat=p * p):
            S = [bits[i * p:(i + 1) * p] for i in range(p)]
            degrees = [sum(row) for row in S]
            for t in range(1, p + 1):
                assert branch_star_mass(S, t) == sum(d ** t for d in degrees)
                branch_cases += 1
    # R62's D=4 example and an exact common-bias collision.
    a = (1, 0, 6, 0, 1)
    a_prime = (0, 1, 6, 0, 1)
    obs_a = [moment(a, t) + 5 for t in range(1, 5)]
    obs_prime = [moment(a_prime, t) + 4 for t in range(1, 5)]
    assert obs_a == obs_prime == [21, 45, 117, 357]
    B = restore_high_degrees([Fraction(x) for x in obs_a])
    assert high_from_binomial(B) == [6, 0, 1]
    # Sharpness of the universal error bound for (D,p)=(2,2):
    # y=(5/2,7/2) is within 1/2 of both candidates after choosing their biases.
    c_a, c_b = (1, 0, 1), (0, 2, 0)
    y = [Fraction(5, 2), Fraction(7, 2)]
    assert all(abs(y[i] - (moment(c_a, i + 1) + 0)) == Fraction(1, 2) for i in range(2))
    assert all(abs(y[i] - (moment(c_b, i + 1) + 1)) == Fraction(1, 2) for i in range(2))
    result = {
        "experiment": "X6 R63 conditional positive-BRC star moments/common additive bias",
        "arithmetic": "exact Python integer and Fraction; no generic physical propagator",
        "scope": "D=1..6, p=D..min(8,D+2), b in {-13,0,7}; literal AB p=1..3",
        "exact_recovery_cases": exact_cases,
        "noisy_recovery_cases": noisy_cases,
        "literal_positive_branch_count_checks": branch_cases,
        "example_observation": obs_a,
        "example_recovered_high_degrees": [6, 0, 1],
        "sharpness_example": {"D": 2, "p": 2, "y": ["5/2", "7/2"], "eta": "1/2", "distinct_high_degrees": True},
        "status": "PASS"
    }
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))


if __name__ == '__main__':
    run()
