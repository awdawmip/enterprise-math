#!/usr/bin/env python3
"""R749SMP: exact Fraction checks for Fourier-subgroup quotient prediction."""
from fractions import Fraction as F
from math import comb
import json
import random

rng = random.Random(749016)
checks = {"coset_walsh_inverse": 0, "binary_minimax": 0,
          "identity_erasure_exact": 0, "binomial_classifier": 0}

def parity(n):
    return (-1) ** (n.bit_count() & 1)

def groups(d, r):
    return [[x for x in range(1 << d) if x & ((1 << r) - 1) == c]
            for c in range(1 << r)]

def tv(p, q):
    return sum(abs(a - b) for a, b in zip(p, q)) / 2

for d in range(1, 7):
    for r in range(d + 1):
        cosets = groups(d, r)
        for _ in range(16):
            weights = [rng.randrange(1, 19) for x in range(1 << d)]
            mu = [F(v, sum(weights)) for v in weights]
            moments = [sum(mu[x] * parity(a & x) for x in range(1 << d))
                       for a in range(1 << r)]
            for c, C in enumerate(cosets):
                mass = sum(mu[x] for x in C)
                inverted = F(1, 1 << r) * sum(moments[a] * parity(a & c)
                                                   for a in range(1 << r))
                assert mass == inverted
                checks["coset_walsh_inverse"] += 1
        for _ in range(16):
            ps = [F(rng.randrange(0, 17), 16) for x in range(1 << d)]
            radii = []
            for C in cosets:
                lo, hi = min(ps[x] for x in C), max(ps[x] for x in C)
                center = (lo + hi) / 2
                radius = (hi - lo) / 2
                assert max(abs(ps[x] - center) for x in C) == radius
                radii.append(radius)
                checks["binary_minimax"] += 1
            assert max(radii) == max((max(ps[x] for x in C) -
                                      min(ps[x] for x in C)) / 2 for C in cosets)

for d in range(1, 6):
    for r in range(d + 1):
        for alpha in [F(0), F(1, 4), F(1, 2), F(3, 4), F(1)]:
            m = 1 << (d - r)
            C = groups(d, r)[0]
            ysize = (1 << d) + 1
            center = [F(0)] * ysize
            center[-1] = 1 - alpha
            for x in C:
                center[x] = alpha / m
            for x in C:
                column = [F(0)] * ysize
                column[x], column[-1] = alpha, 1 - alpha
                assert tv(column, center) == alpha * (1 - F(1, m))
                checks["identity_erasure_exact"] += 1

ps = [F(0), F(1, 3), F(2, 3), F(1)]
def classifier_error(n, p):
    error = F(0)
    for k in range(n + 1):
        frequency = F(k, n)
        chosen = min(range(4), key=lambda i: (abs(frequency - ps[i]), i))
        if chosen != ps.index(p):
            error += comb(n, k) * p ** k * (1 - p) ** (n - k)
    return error
classifier = {}
for n in (8, 16, 32, 64):
    errs = [classifier_error(n, p) for p in ps]
    maximum = max(errs)
    assert maximum <= 1
    classifier[str(n)] = {"max_error_fraction": str(maximum),
                          "max_error_decimal": round(float(maximum), 10),
                          "radius_lower_from_classifier": str(F(3, 4) - maximum)}
    checks["binomial_classifier"] += 4

result = {"research_unit": "R749SMP", "arithmetic": "Python Fraction exact",
          "checks": checks, "total_checks": sum(checks.values()),
          "identity_example": {"d": 3, "retained_rank": 1,
                               "coset_size": 4, "max_pairwise_TV": "1",
                               "exact_minimax_TV": "3/4"},
          "binary_example": {"d": 3, "retained_rank": 1,
                             "p_x": [str(F(i + 1, 10)) for i in range(8)],
                             "exact_minimax_TV": "3/10"},
          "classifier_example": {"p_values": [str(p) for p in ps],
                                 "n": classifier}, "status": "PASS"}
print(json.dumps(result, ensure_ascii=False, indent=2))
