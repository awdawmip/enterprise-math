#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import time
from array import array
from collections import Counter


def linear_sieve(limit: int):
    spf = array("I", [0]) * (limit + 1)
    Omega = bytearray(limit + 1)
    omega = bytearray(limit + 1)
    primes = array("I")
    if limit >= 1:
        spf[1] = 1
    for i in range(2, limit + 1):
        if spf[i] == 0:
            spf[i] = i
            primes.append(i)
            Omega[i] = 1
            omega[i] = 1
        for p in primes:
            x = i * p
            if x > limit:
                break
            spf[x] = p
            Omega[x] = Omega[i] + 1
            if i % p == 0:
                omega[x] = omega[i]
                break
            omega[x] = omega[i] + 1
    return spf, Omega, omega, primes


def d_times(a: int, b: int, Omega) -> int:
    g = math.gcd(a, b)
    return Omega[a // g] + Omega[b // g]


def census(limit: int, spf, Omega, omega):
    sem_d = Counter()
    sem_shared = Counter()
    comp_d = Counter()
    comp_gap = Counter()
    comp_d_gap1 = Counter()
    comp_d_gap2 = Counter()
    sem_count = comp_count = 0
    prev_sem = prev_comp = None
    sem_max_gap = (-1, None, None, None)
    comp_max_d = (-1, None, None, None)
    comp_min_d = (10**9, None, None)
    d2_max_gap = (-1, None, None, None)
    sem_omega_types = Counter()

    for n in range(2, limit + 1):
        is_prime = spf[n] == n
        if Omega[n] == 2:
            sem_count += 1
            if prev_sem is not None:
                d = d_times(prev_sem, n, Omega)
                g = math.gcd(prev_sem, n)
                gap = n - prev_sem
                sem_d[d] += 1
                sem_omega_types[(omega[prev_sem], omega[n], d)] += 1
                if g > 1:
                    sem_shared[g] += 1
                    if gap > d2_max_gap[0]:
                        d2_max_gap = (gap, prev_sem, n, g)
                if gap > sem_max_gap[0]:
                    sem_max_gap = (gap, prev_sem, n, d)
            prev_sem = n

        if n >= 4 and not is_prime:
            comp_count += 1
            if prev_comp is not None:
                d = d_times(prev_comp, n, Omega)
                gap = n - prev_comp
                comp_d[d] += 1
                comp_gap[gap] += 1
                if gap == 1:
                    comp_d_gap1[d] += 1
                elif gap == 2:
                    comp_d_gap2[d] += 1
                else:
                    raise AssertionError(("composite adjacency gap > 2", prev_comp, n, gap))
                if d == 1:
                    raise AssertionError(("T3 failure", prev_comp, n))
                if d < comp_min_d[0]:
                    comp_min_d = (d, prev_comp, n)
                if d > comp_max_d[0]:
                    comp_max_d = (d, prev_comp, n, gap)
            prev_comp = n

    return {
        "semiprime_count": sem_count,
        "semiprime_pair_count": max(0, sem_count - 1),
        "semiprime_distance_counts": dict(sorted(sem_d.items())),
        "semiprime_shared_gcd_counts": dict(sorted(sem_shared.items())),
        "semiprime_omega_types": {str(k): v for k, v in sorted(sem_omega_types.items())},
        "semiprime_max_gap": sem_max_gap,
        "semiprime_d2_max_gap": d2_max_gap,
        "composite_count": comp_count,
        "composite_pair_count": max(0, comp_count - 1),
        "composite_gap_counts": dict(sorted(comp_gap.items())),
        "composite_distance_counts": dict(sorted(comp_d.items())),
        "composite_distance_gap1": dict(sorted(comp_d_gap1.items())),
        "composite_distance_gap2": dict(sorted(comp_d_gap2.items())),
        "composite_min_distance": comp_min_d,
        "composite_max_distance": comp_max_d,
    }


def verify_theorem_identities(limit: int, Omega):
    bound = min(limit, 5000)
    for a in range(1, bound + 1, 17):
        for b in range(1, bound + 1, 19):
            g = math.gcd(a, b)
            d = Omega[a // g] + Omega[b // g]
            rhs = Omega[a] + Omega[b] - 2 * Omega[g]
            if d != rhs:
                raise AssertionError(("distance identity", a, b, d, rhs))
            if a != b and Omega[a] == Omega[b]:
                if not (d >= 2 and d % 2 == 0):
                    raise AssertionError(("T1", a, b, d))


def verify_crt_distortion(max_k: int = 32):
    witnesses = []
    for k in range(2, max_k + 1):
        a = 2**k
        m = 3**k
        t = (-pow(a, -1, m)) % m
        n = a * t
        if n == 0:
            n += a * m
        assert n % a == 0
        assert (n + 1) % m == 0
        assert math.gcd(n, n + 1) == 1
        witnesses.append((k, n))
    return witnesses


def m2_adj(v, w):
    common = 0
    used = [False, False]
    for x in v:
        for j, y in enumerate(w):
            if not used[j] and x == y:
                used[j] = True
                common += 1
                break
    return common == 1


def semiprime_gray_spine(r: int):
    if r < 1:
        return []
    seq = [(1, 1)]
    for j in range(2, r + 1):
        seq.append((j - 1, j))
        for i in range(1, j - 1):
            seq.append((i, j))
        seq.append((j, j))
    return seq


def verify_gray_spine(max_r: int = 64):
    prev = None
    checks = []
    for r in range(1, max_r + 1):
        h = semiprime_gray_spine(r)
        expected = {(i, j) for j in range(1, r + 1) for i in range(1, j + 1)}
        assert len(h) == r * (r + 1) // 2
        assert len(set(h)) == len(h)
        assert set(h) == expected
        if prev is not None:
            assert h[: len(prev)] == prev
        for a, b in zip(h, h[1:]):
            assert m2_adj(a, b), (r, a, b)
        assert h[-1] == (r, r)
        V = r * (r + 1) // 2
        E = r * r * (r - 1) // 2
        if r >= 2:
            retention_num = V - 1
            retention_den = E
            assert retention_num * r * r == retention_den * (r + 2)
        checks.append((r, V, E))
        prev = h

    for r in range(3, min(max_r, 24) + 1):
        h = semiprime_gray_spine(r)
        pos = {v: i for i, v in enumerate(h)}
        max_stretch = 0
        for x in h:
            for y in h:
                if pos[x] < pos[y] and m2_adj(x, y):
                    max_stretch = max(max_stretch, pos[y] - pos[x])
        assert max_stretch == r * (r - 1) // 2 + 1, (r, max_stretch)
    return checks


EXPECTED_1E6 = {
    "semiprime_count": 210035,
    "semiprime_pair_count": 210034,
    "semiprime_distance_counts": {2: 4855, 4: 205179},
    "composite_count": 921501,
    "composite_pair_count": 921500,
    "composite_gap_counts": {1: 843004, 2: 78496},
    "composite_min_distance": (2, 4, 6),
    "composite_max_distance": (24, 262143, 262144, 1),
}

EXPECTED_1E7 = {
    "semiprime_count": 1904324,
    "semiprime_pair_count": 1904323,
    "semiprime_distance_counts": {2: 41533, 4: 1862790},
    "semiprime_shared_gcd_counts": {2: 28623, 3: 10338, 5: 1973, 7: 514, 11: 70, 13: 15},
    "semiprime_max_gap": (74, 5835191, 5835265, 4),
    "semiprime_d2_max_gap": (48, 6950631, 6950679, 3),
    "composite_count": 9335420,
    "composite_pair_count": 9335419,
    "composite_gap_counts": {1: 8670842, 2: 664577},
    "composite_min_distance": (2, 4, 6),
    "composite_max_distance": (26, 1048575, 1048576, 1),
}


def assert_expected(stats, expected):
    for key, val in expected.items():
        got = stats[key]
        if got != val:
            raise AssertionError((key, got, val))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=1_000_000)
    ap.add_argument("--full", action="store_true", help="equivalent to --limit 10000000")
    args = ap.parse_args()
    limit = 10_000_000 if args.full else args.limit
    if limit < 100:
        raise SystemExit("limit must be >=100")

    t0 = time.time()
    spf, Omega, omega, primes = linear_sieve(limit)
    t1 = time.time()
    verify_theorem_identities(limit, Omega)
    crt = verify_crt_distortion()
    spine = verify_gray_spine()
    stats = census(limit, spf, Omega, omega)
    t2 = time.time()

    if limit == 1_000_000:
        assert_expected(stats, EXPECTED_1E6)
    if limit == 10_000_000:
        assert_expected(stats, EXPECTED_1E7)
        assert stats["composite_distance_counts"].get(2, 0) == 1
        assert min(stats["composite_distance_gap1"]) >= 4

    result = {
        "status": "PASS",
        "limit": limit,
        "prime_count": len(primes),
        "sieve_seconds": round(t1 - t0, 3),
        "total_seconds": round(t2 - t0, 3),
        "crt_witnesses_checked": len(crt),
        "gray_spine_max_r": spine[-1][0],
        "stats": stats,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
