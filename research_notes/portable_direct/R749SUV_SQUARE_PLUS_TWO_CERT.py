#!/usr/bin/env python3
"""R749SUV exact integer certificate: B=t^2+2 Q=+1 Port observer.

Dependencies: Python standard library. No floating-point.
Run: python R749SUV_SQUARE_PLUS_TWO_CERT.py
"""
import json
from collections import Counter
from math import isqrt


def score(x, y):
    n = x * y
    return (n - 1) * (n - x - 1) * (n - y - 1)


def classify(t):
    """Return (family, x, y) for the unique unordered optimizer, t>=3."""
    assert isinstance(t, int) and t >= 3
    if t % 2:
        q = isqrt(2 * t - 1)
        if q * q == 2 * t - 1 and q >= 3 and q % 2:
            k = (q - 1) // 2
            return ("n2_j2", t - 2 * k, t + 2 * k + 2)
        q = isqrt(4 * t - 3)
        if q * q == 4 * t - 3 and q >= 3 and q % 2:
            r = (q - 1) // 2
            return ("n1_j1", t - r, t + r + 1)
    else:
        q = isqrt(4 * t - 7)
        if q * q == 4 * t - 7 and q >= 3 and q % 2:
            r = (q - 1) // 2
            return ("n2_j1", t - r, t + r + 1)
        q = isqrt(12 * t + 1)
        if q * q == 12 * t + 1 and q % 2:
            x, y = (2 * t + 3 - q) // 2, (2 * t + 3 + q) // 2
            if x >= 2 and x * y == t * t + 2:
                return ("n2_j3", x, y)
        k = isqrt(t // 2)
        if k >= 2 and t == 2 * k * k:
            return ("n1_j2", t - 2 * k + 1, t + 2 * k + 1)
    return ("base", t, t)


def bounded_discriminant(t):
    """Independent search of ALL candidates allowed by the score cutoff."""
    B = t * t + 2
    candidates = {(t, t)}
    for n, shifts in (
        (B - 1, (1,) if t % 2 else (2,)),
        (B, (2, 4) if t % 2 else (1, 3, 5)),
    ):
        for j in shifts:
            ss = 2 * t + j
            disc = ss * ss - 4 * n
            if disc < 0:
                continue
            root = isqrt(disc)
            if root * root != disc or (ss - root) % 2:
                continue
            x, y = (ss - root) // 2, (ss + root) // 2
            if x >= 2 and x <= y and x * y == n and n - x - y >= 1:
                candidates.add((x, y))
    best = max(score(x, y) for x, y in candidates)
    return best, sorted((x, y) for x, y in candidates if score(x, y) == best)


def exhaustive_oracle(t):
    """Independently enumerate EVERY legal unordered factor pair xy<=t^2+2."""
    B = t * t + 2
    best = -1
    winners = []
    for x in range(2, isqrt(B) + 1):
        for y in range(x, B // x + 1):
            if x * y - x - y < 1:
                continue
            z = score(x, y)
            if z > best:
                best, winners = z, [(x, y)]
            elif z == best:
                winners.append((x, y))
    return best, winners


def endpoint_oracle(t):
    """Independent all-x oracle: for fixed x, the largest legal y is optimal."""
    B = t * t + 2
    best = -1
    winners = []
    for x in range(2, isqrt(B) + 1):
        y = B // x
        if y < x or x * y - x - y < 1:
            continue
        z = score(x, y)
        if z > best:
            best, winners = z, [(x, y)]
        elif z == best:
            winners.append((x, y))
    return best, winners


def check():
    counts = Counter()
    for t in range(3, 50001):
        fam, x, y = classify(t)
        assert 2 <= x <= y and x*y <= t*t+2 and x*y-x-y >= 1
        a = bounded_discriminant(t)
        assert a == (score(x, y), [(x, y)]), (t, a, (fam, x, y))
        counts[fam] += 1

    for t in range(3, 140):
        fam, x, y = classify(t)
        assert exhaustive_oracle(t) == (score(x, y), [(x, y)]), t

    for t in range(3, 2501):
        fam, x, y = classify(t)
        assert endpoint_oracle(t) == (score(x, y), [(x, y)]), t

    samples = {}
    for t in (3, 4, 5, 6, 7, 8, 10, 13, 18, 24, 50, 10**6, 10**12):
        fam, x, y = classify(t)
        n = x*y
        samples[str(t)] = {
            "family": fam, "x": str(x), "y": str(y),
            "n": str(n), "B_minus_n": str(t*t+2-n),
            "score": str(score(x, y))
        }

    # Symbolic inequalities required by the proof, integer-only sample checking.
    for t in range(3, 10001):
        S = score(t,t)
        def by_n_s(n,s):
            return (n-1)*((n-1)**2-(n-1)*s+n)
        assert by_n_s(t*t+1, 2*t+(3 if t%2 else 4)) < S
        assert by_n_s(t*t+2, 2*t+6) < S
        if t%2:
            assert by_n_s(t*t+2,2*t+2) > by_n_s(t*t+1,2*t+1) > S
        else:
            assert by_n_s(t*t+2,2*t+1) > by_n_s(t*t+2,2*t+3) > S
            if t >= 8:
                assert by_n_s(t*t+2,2*t+3) > by_n_s(t*t+1,2*t+2) > S

    return {
        "result":"PASS",
        "model":"Q=+1 named WBRC two-Port integer observer (not native X6)",
        "theorem":"all t>=3; exactly one unordered optimum",
        "exhaustive_t":"3..139 (137)",
        "endpoint_t":"3..2500 (2498)",
        "independent_bounded_discriminant_t":"3..50000 (49998)",
        "polynomial_regression_t":"3..10000 (9998)",
        "counts_through_50000":dict(sorted(counts.items())),
        "samples":samples,
        "arithmetic":"exact Python integers; large values serialized as decimal strings",
        "status":"AUTHOR_EXACT_NOT_REVIEWED"
    }


if __name__ == "__main__":
    data = check()
    with open("R749SUV_SQUARE_PLUS_TWO_RESULTS.json", "w", encoding="utf-8") as fp:
        json.dump(data,fp,ensure_ascii=False,indent=2,sort_keys=True)
        fp.write("\n")
    print("PASS", data["counts_through_50000"])
