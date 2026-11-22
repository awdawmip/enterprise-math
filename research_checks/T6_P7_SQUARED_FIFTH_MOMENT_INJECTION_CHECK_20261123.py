#!/usr/bin/env python3
"""Exact universal p=7^2 denominator cancellation: finite mass-bounded certificate.

Checks the already-used p7^3 elimination and the full p7^2 layer.
All signatures use integer modular inverses, no floating point.
"""
from collections import Counter, defaultdict

P, CAP = 7, 2331


def types(level):
    base = P ** level
    return tuple((j, base * j - 1) for j in range(1, CAP // base + 1)
                 if j % P)


def count_profiles(items):
    dp = [0] * (CAP + 1)
    dp[0] = 1
    for _, w in items:
        for b in range(w, CAP + 1):
            dp[b] += dp[b-w]
    return sum(dp)


def visit_profiles(items, K, on_profile):
    mods = tuple(P ** k for k in range(1, K+1))
    coeff = tuple(tuple(pow(pow(j, k, mod), -1, mod)
                        for k, mod in enumerate(mods, 1)) for j, _ in items)
    sig = [0]*K
    count = 0

    def go(i, cap):
        nonlocal count
        if i == len(items):
            count += 1
            on_profile(tuple(sig))
            return
        old = sig[:]
        w = items[i][1]
        for n in range(cap//w + 1):
            if n:
                for k in range(K):
                    sig[k] = (sig[k] + coeff[i][k]) % mods[k]
            go(i+1, cap-n*w)
        sig[:] = old
    go(0, CAP)
    return count


def run():
    high = types(3)
    assert len(high) == 6
    high_signatures = set()
    n = visit_profiles(high, 3, lambda s: high_signatures.add(s))
    assert n == count_profiles(high) == len(high_signatures) == 30
    print("p7^3: 30 profiles; 30 three-moment signatures; injective")

    items = types(2)
    assert len(items) == 41
    counts = Counter()
    n = visit_profiles(items, 4, lambda s: counts.update((s,)))
    assert n == count_profiles(items) == 512672
    collision_keys = {s for s, multiplicity in counts.items() if multiplicity > 1}
    assert len(counts) == 512416
    assert len(collision_keys) == 256
    assert all(counts[s] == 2 for s in collision_keys)
    print("p7^2: 512672 profiles, 512416 four-moment signatures, 256 pairs")

    # The fifth-moment check only needs the 256 fibers that collided at K=4.
    refined = defaultdict(set)
    def check_fifth(sig):
        key = sig[:4]
        if key in collision_keys:
            assert sig[4] not in refined[key]
            refined[key].add(sig[4])
    assert visit_profiles(items, 5, check_fifth) == n
    assert len(refined) == 256 and all(len(v) == 2 for v in refined.values())
    print("p7^2: all 256 fibers split at K=5; all 512672 signatures unique; PASS")


if __name__ == "__main__":
    run()
