#!/usr/bin/env python3
"""R762CE: independent finite verification of all observer-conditioned budget certificates."""
from collections import defaultdict, Counter
from itertools import combinations, product
import json
from pathlib import Path

R = (1, 1, 3, 3)
W = (1, 1, 3, 3)
Q = 12

def population():
    fibers = defaultdict(list)
    for states in product(*(range(-1, 1 << r) for r in R)):
        n = [0, 0, 0, 0]
        word = 0
        for i, x in enumerate(states):
            if x >= 0:
                word |= 1 << i
                n[x.bit_count()] += W[i]
        shift = 4
        for i, x in enumerate(states):
            for j in range(R[i]):
                if x >= 0 and ((x >> j) & 1):
                    word |= 1 << shift
                shift += 1
        fibers[tuple(n)].append(word)
    return fibers

def maximum_collision(fiber, query_mask):
    return max(Counter(word & query_mask for word in fiber).values())

def query_masks(q):
    for subset in combinations(range(Q), q):
        yield sum(1 << j for j in subset)

def check():
    evidence = json.loads(Path(__file__).with_name("R762CE_EVIDENCE.json").read_text(encoding="utf-8"))
    fibers = population()
    assert len(fibers) == 90 and sum(map(len, fibers.values())) == 729
    assert max(map(len, fibers.values())) == 36
    assert evidence["population"] == 729 and evidence["A_classes"] == 90
    assert len(evidence["certificates"]) == 90
    histograms = [Counter() for _ in range(7)]
    extrema = [0] * 7
    for name, fiber in fibers.items():
        key = ",".join(map(str, name))
        cert = evidence["certificates"][key]
        assert len(cert) == 7
        for q, item in enumerate(cert):
            mask, advertised = item["mask"], item["max_residual"]
            assert 0 <= mask < (1 << Q) and mask.bit_count() == q
            assert maximum_collision(fiber, mask) == advertised
            # Separate exhaustive recomputation checks optimality for this entire A fiber.
            optimum = min(maximum_collision(fiber, m) for m in query_masks(q))
            assert optimum == advertised, (key, q, optimum, advertised)
            histograms[q][optimum] += 1
            extrema[q] = max(extrema[q], optimum)
    expected = [(36 + (1 << q) - 1) // (1 << q) for q in range(7)]
    assert extrema == expected
    assert evidence["global_max_residual"] == expected
    for q, hist in enumerate(histograms):
        assert evidence["per_budget_histograms"][str(q)] == {
            str(k): v for k, v in sorted(hist.items())
        }
    assert len(fibers[(1, 3, 3, 0)]) == 36
    print("R762CE PASS: 729 laws, 90 A fibers, all 90x7 exhaustive q-atom optima")
    print("global_max_residual:", extrema)

if __name__ == "__main__":
    check()
