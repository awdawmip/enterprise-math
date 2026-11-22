#!/usr/bin/env python3
"""Exact p=11^2 denominator profile injection for the T6 shape-moment model.

Standard library only. Integer arithmetic throughout. This is a finite exhaustive
certificate for nonnegative per-side multiplicity vectors under mass <=2331.
"""
from collections import defaultdict

P, CAP = 11, 2331
JS = tuple(j for j in range(1, CAP // (P * P) + 1) if j % P)
WEIGHTS = tuple(P * P * j - 1 for j in JS)


def enumerated_profiles():
    profile = [0] * len(JS)
    def walk(i, budget):
        if i == len(JS):
            yield tuple(profile)
            return
        w = WEIGHTS[i]
        for n in range(budget // w + 1):
            profile[i] = n
            yield from walk(i + 1, budget - n * w)
        profile[i] = 0
    return list(walk(0, CAP))


def independent_dp_count():
    dp = [0] * (CAP + 1)
    dp[0] = 1
    for w in WEIGHTS:
        for b in range(w, CAP + 1):
            dp[b] += dp[b - w]
    return sum(dp)


def signature(profile, order):
    vals = []
    for k in range(1, order + 1):
        modulus = P ** k
        vals.append(sum(n * pow(pow(j, k, modulus), -1, modulus)
                        for j, n in zip(JS, profile)) % modulus)
    return tuple(vals)


def run():
    profiles = enumerated_profiles()
    assert len(profiles) == independent_dp_count() == 2020
    expected = ((11, 184537), (1038, 1498), (2020, 0))
    for k, (unique, collisions) in enumerate(expected, start=1):
        fibers = defaultdict(int)
        for profile in profiles:
            assert sum(n * w for n, w in zip(profile, WEIGHTS)) <= CAP
            fibers[signature(profile, k)] += 1
        assert len(fibers) == unique
        assert sum(n * (n - 1) // 2 for n in fibers.values()) == collisions
        print(f"K={k}: profiles={len(profiles)}, signatures={unique}, collisions={collisions}")
    # Independent computation of the k=3 signature via inv(j) powers.
    distinct = set()
    for profile in profiles:
        sig = tuple(sum(n * pow(pow(j, -1, P ** k), k, P ** k)
                        for j, n in zip(JS, profile)) % (P ** k)
                    for k in (1, 2, 3))
        assert sig == signature(profile, 3)
        assert sig not in distinct
        distinct.add(sig)
    print("PASS p11^2 injective signature; 2020 exact feasible profiles")


if __name__ == "__main__":
    run()
