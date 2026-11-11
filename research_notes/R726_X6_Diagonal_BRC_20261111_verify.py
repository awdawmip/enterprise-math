#!/usr/bin/env python3
"""R726: exact signed X6 diagonal-fiber and BRC cardinality verifier, stdlib only."""
from collections import defaultdict, Counter
from itertools import combinations
from math import factorial
from fractions import Fraction
import json

def signed_vectors(L, n=6):
    def rec(i, rem, prefix):
        if i == n:
            if rem >= 0 and rem % 2 == 0:
                yield tuple(prefix)
            return
        for a in range(-rem, rem + 1):
            prefix.append(a)
            yield from rec(i + 1, rem - abs(a), prefix)
            prefix.pop()
    return rec(0, L, [])

def relative_key(v):
    return tuple(x - v[0] for x in v)

def path_count(L, v):
    # P000 signed N-BRC formula, exact rational coefficient extraction.
    k = (L - sum(abs(x) for x in v)) // 2
    assert k >= 0
    f = [Fraction(1)] + [Fraction(0)] * k
    for x in v:
        a, b = max(x, 0), max(-x, 0)
        g = [Fraction(0) for _ in range(k + 1)]
        for j in range(k + 1):
            for t in range(k - j + 1):
                g[j + t] += f[j] / (factorial(a + t) * factorial(b + t))
        f = g
    n = f[k] * factorial(L)
    assert n.denominator == 1
    return int(n)

def run():
    samples = []
    for L in range(8):
        fibers = defaultdict(list)
        for v in signed_vectors(L):
            fibers[relative_key(v)].append(v)
        hist = Counter(len(f) for f in fibers.values())
        assert max(hist) == L // 3 + 1, (L, hist)
        samples.append({"L": L, "total_states": sum(n * count for n, count in hist.items()),
                        "quotient_classes": len(fibers), "largest_fiber": max(hist),
                        "histogram": dict(sorted(hist.items()))})
    pairs = 0
    for H in combinations(range(6), 3):
        a = tuple(1 if i in H else 0 for i in range(6))
        b = tuple(0 if i in H else -1 for i in range(6))
        assert relative_key(a) == relative_key(b)
        assert tuple(x - y for x, y in zip(a, b)) == (1,) * 6
        assert path_count(3, a) == path_count(3, b) == 6
        assert path_count(5, a) == path_count(5, b) == 540
        assert sum(a) == 3 and sum(b) == -3
        pairs += 1
    assert pairs == 20
    result = {
        "schema": "EM_R726_DIAGONAL_BRC_FIBER_V1",
        "model": "X6 signed primitive coordinate steps; NOT native force closure",
        "frozen_science_commit": "a72226e2430ffa4786321ac86e7f0c599d5f0389",
        "coverage": "all W_L for L=0..7; 20 complementary triad pairs; exact N3 and N5",
        "sample_histograms": samples, "pair_count": pairs,
        "pair_counts": {"N3": 6, "N5": 540, "sigma_plus": 3, "sigma_minus": -3},
        "result": "R726_DIAGONAL_BRC_FIBERS_EXACT_PASS"
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    print(result["result"])
    return result

if __name__ == "__main__":
    run()
