#!/usr/bin/env python3
"""
Verify the <=4 weighted local Ramanujan-trace signature for odd-prime-power lifts.

Researcher-ID: EM-DIRECT-66DE45
No RSA factor is used or produced.
"""
import random


def ramanujan_prime_power(l, e, k):
    m = l ** e
    n = l ** (e - 1)
    k %= m
    if k == 0:
        return (l - 1) * n
    if k % n == 0:
        return -n
    return 0


def tau_odd(r, m):
    r %= 2 * m
    assert r % 2 == 1
    return ((r + m) // 2) % m


def candidate_lifts(prev_pair, N, l, e):
    m = l ** e
    n = l ** (e - 1)
    p0, q0 = prev_pair
    out = set()
    for i in range(l):
        P = (p0 + 2 * n * i) % (2 * m)
        for j in range(l):
            Q = (q0 + 2 * n * j) % (2 * m)
            if (P * Q - N) % (2 * m) == 0:
                out.add(tuple(sorted((P, Q))))
    return sorted(out)


def occupied_bases(prev_pair, l, e):
    n = l ** (e - 1)
    bases = set()
    for r in prev_pair:
        t = tau_odd(r, n) % n
        bases.add(t)
        bases.add((-t) % n)
    assert len(bases) <= 4
    return sorted(bases)


def weighted_signature(pair, prev_pair, l, e, B=10):
    m = l ** e
    n = l ** (e - 1)
    P, Q = pair
    tp = tau_odd(P, m)
    tq = tau_odd(Q, m)
    signed_exponents = [
        (tp, +1),
        ((-tp) % m, -1),
        (tq, +1),
        ((-tq) % m, -1),
    ]

    signature = []
    for base in occupied_bases(prev_pair, l, e):
        packed = 0
        for j in range(l):
            r = (base + j * n) % m
            L = sum(
                eps * ramanujan_prime_power(l, e, t - r)
                for t, eps in signed_exponents
            )
            packed += (B ** j) * L
        signature.append(packed)
    return tuple(signature)


def check_random_states():
    rng = random.Random(20260908)
    total = 0
    max_bases = 0

    for l in (3, 5, 7, 11, 13):
        for e in (2, 3, 4):
            m = l ** e
            n = l ** (e - 1)
            for _ in range(200):
                P = rng.randrange(1, 2 * m, 2)
                while P % l == 0:
                    P = rng.randrange(1, 2 * m, 2)
                Q = rng.randrange(1, 2 * m, 2)
                while Q % l == 0:
                    Q = rng.randrange(1, 2 * m, 2)

                N = P * Q
                prev = tuple(sorted((P % (2 * n), Q % (2 * n))))
                cands = candidate_lifts(prev, N, l, e)
                assert 1 <= len(cands) <= l

                bases = occupied_bases(prev, l, e)
                max_bases = max(max_bases, len(bases))

                sigs = [weighted_signature(c, prev, l, e) for c in cands]
                assert len(sigs) == len(set(sigs)), (l, e, prev, cands)
                total += 1

    return total, max_bases


def check_packing_injectivity():
    # If two signed histograms C_j in [-2,2] differ, their difference digits
    # lie in [-4,4]. B=10 gives unique balanced-base encoding.
    B = 10
    for l in range(3, 14, 2):
        # It is enough to test all one/two signed monomial histograms explicitly.
        histograms = set()
        items = [(j, s) for j in range(l) for s in (-1, +1)]
        histograms.add((0,) * l)
        for j, s in items:
            h = [0] * l
            h[j] += s
            histograms.add(tuple(h))
        for j1, s1 in items:
            for j2, s2 in items:
                h = [0] * l
                h[j1] += s1
                h[j2] += s2
                histograms.add(tuple(h))

        codes = {sum((B ** j) * c for j, c in enumerate(h)) for h in histograms}
        assert len(codes) == len(histograms)


if __name__ == "__main__":
    check_packing_injectivity()
    total, max_bases = check_random_states()
    print("packing injectivity: PASS")
    print("random local states:", total, "PASS")
    print("max occupied base fibers:", max_bases)
    assert max_bases <= 4
    print("ALL PASS")
