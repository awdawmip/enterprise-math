#!/usr/bin/env python3
"""R712: source-labelled BRC candidate odd-ring phase residual certificate.
Run: python R712_ODD_RING_VERIFY.py
No numerical physics, trigonometry, or untyped BRC amplitude arithmetic.
"""
from itertools import combinations
from functools import lru_cache
import json

PHASES = range(1, 6)
PAIRS = tuple(combinations(PHASES, 2))
ADJ = {p: tuple(q for q in PAIRS if set(p).isdisjoint(q)) for p in PAIRS}
WEIGHT = lambda p: p[1] - p[0] - 1


def simple_odd_cycles():
    unique = set()
    for start in PAIRS:
        def dfs(path):
            here = path[-1]
            if len(path) >= 3 and start in ADJ[here] and len(path) % 2:
                seq = tuple(path)
                forms = [tuple(seq[i:] + seq[:i]) for i in range(len(seq))]
                rev = seq[::-1]
                forms += [tuple(rev[i:] + rev[:i]) for i in range(len(rev))]
                unique.add(min(forms))
            for q in ADJ[here]:
                if q not in path:
                    dfs(path + [q])
        dfs([start])
    counts = {k: [] for k in (3, 5, 7, 9)}
    for cycle in unique:
        counts[len(cycle)].append(sum(WEIGHT(p) for p in cycle))
    assert {k: len(v) for k, v in counts.items()} == {3: 0, 5: 12, 7: 0, 9: 20}
    assert min(counts[5]) == 3 and min(counts[9]) == 7
    return {str(k): {"cycles": len(v), "min_excess": min(v) if v else None} for k, v in counts.items()}


def certificate(m):
    assert m >= 5 and m % 2 == 1
    a = (m - 1) // 4
    b = (m - 1) // 2 - a
    pairs = [(1, 2), (3, 4)] * a + [(1, 5)] + [(2, 3), (4, 5)] * b
    assert len(pairs) == m
    assert all(set(pairs[i]).isdisjoint(pairs[(i+1) % m]) for i in range(m))
    residuals = [sum(lo <= t < hi for lo, hi in pairs) for t in range(1, 5)]
    assert residuals == [a + 1, b + 1, a + 1, b + 1]
    assert sum(residuals) == m + 3
    assert max(residuals) == (m + 6) // 4  # ceil((m+3)/4)
    assert sum(hi-lo for lo, hi in pairs) == m + 3
    # Two source-labelled opposite events per edge; incidence capacity <=1.
    for t in PHASES:
        used = []
        for i, slots in enumerate(pairs):
            if t in slots:
                used.extend([i, (i + 1) % m])
        assert len(used) == len(set(used))
    return {"m": m, "a": a, "b": b, "residuals": residuals,
            "peak": max(residuals), "area": sum(residuals),
            "phase_pairs": [f"{lo}{hi}" for lo, hi in pairs]}


def exact_dp(m):
    """Independently optimize (peak,area) over ALL five-phase matchings."""
    masks = [mask for mask in range(1 << m) if not any(
        (mask >> i & 1) and (mask >> ((i + 1) % m) & 1)
        for i in range(m))]
    powers = [3**i for i in range(m)]
    target = 2 * sum(powers)
    @lru_cache(None)
    def solve(state, stage):
        if stage == 5:
            return (0, 0) if state == target else None
        digits = [(state // x) % 3 for x in powers]
        remaining = sum(2-x for x in digits)
        capacity = (m // 2) * (4-stage)
        best = None
        for mask in masks:
            if mask.bit_count() > remaining or remaining-mask.bit_count() > capacity:
                continue
            if any(digits[i] == 2 and (mask >> i & 1) for i in range(m)):
                continue
            nxt = state + sum(powers[i] for i in range(m) if mask >> i & 1)
            d = sum(digits[i] + (mask >> i & 1) == 1 for i in range(m))
            tail = solve(nxt, stage + 1)
            if tail is None:
                continue
            val = (max(d, tail[0]), d+tail[1])
            if best is None or val < best:
                best = val
        return best
    got = solve(0, 0)
    claimed = certificate(m)
    assert got == (claimed["peak"], claimed["area"]), (m, got, claimed)
    return {"m": m, "optimum": list(got), "states": solve.cache_info().currsize,
            "matchings": len(masks)}


def main():
    graph = simple_odd_cycles()
    constructions = [certificate(m) for m in range(5, 102, 2)]
    dp = [exact_dp(m) for m in (5, 7, 9, 11, 13)]
    out = {"verdict": "R712_ODD_RING_MICROCURRENT_SHARP_PASS",
           "observer": "D_t=sum_e abs(j_e(t)), t=1..4; positive BRC event counts retained separately",
           "source_pin": "a72226e2430ffa4786321ac86e7f0c599d5f0389",
           "petersen_odd_cycles": graph, "construction_count": len(constructions),
           "construction_examples": [c for c in constructions if c["m"] in (5, 7, 9, 11, 13, 101)],
           "independent_dp": dp}
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
