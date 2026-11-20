#!/usr/bin/env python3
"""Exact odd-part divisor-fiber index for adjacent odd-core named XOR collisions.
Generation uses no prior pair list. Small-width checks enumerate raw XOR equations.
"""
from collections import Counter, defaultdict
from hashlib import sha256
from struct import pack
from time import perf_counter
import argparse
import json

PIN = "f42f2906d77f24085c123f3ccfe9667d41caa96d"
PRIOR = "1caec71f97ddb97c60c8506629f65651f0f3030b3526aeca30195948ee0cff75"

def residuals(p):
    z = defaultdict(list)
    for i in range(p):
        for j in range(p):
            for s in (-1, 1):
                z[(1 << i) - s * (1 << j)].append((i, j, s))
    return z

def actual_names(product, sources):
    return sum(s == 1 - 2 * ((product >> j) & 1) for _, j, s in sources)

def reconstruct(p, k, lo_gap, hi_gap):
    H = 1 << (p - 1)
    low, high, half = H + 1, 2 * H - 1, H // 2
    z = residuals(p)
    cache, stats = {}, Counter()
    out, bygap = Counter(), defaultdict(Counter)

    def b_fiber(oddpart):
        if oddpart in cache:
            stats["cache_hits"] += 1
            return cache[oddpart]
        stats["cache_misses"] += 1
        choices = []
        if oddpart >= low:
            lower = max(1, (oddpart + high - 1) // high)
            upper = oddpart // low
            lower += 1 - (lower & 1)
            for q in range(lower, upper + 1, 2):
                stats["unique_oddpart_divisibility_probes"] += 1
                if oddpart % q == 0:
                    b = oddpart // q
                    assert low <= b <= high and b & 1
                    choices.append((b, q))
        cache[oddpart] = choices
        return choices

    for m in range(lo_gap, hi_gap + 1):
        for c, S1 in z.items():
            for C, S2 in z.items():
                delta = C - c
                if m & 1:
                    if delta % 2 != 1:
                        continue
                elif m % 4 == 0:
                    if delta % 4 != 2:
                        continue
                else:
                    if delta % 4 != 0:
                        continue
                stats["numeric_entries_after_mod4"] += 1
                N = k * C - (k + 2) * c
                if N == 0:
                    stats["zero_numerator_entries"] += 1
                    if m in (2, 4) and c % k == 0:
                        r, shift = m // 2, c // k
                        for b in range(low, high + 1, 2):
                            a = r * b + shift
                            if not (low <= a <= high and a & 1 and a != b):
                                continue
                            v = actual_names(k * a, S1)
                            w = actual_names((k + 2) * a, S2)
                            if v and w:
                                ident = ((a - low) // 2) * half + (b - low) // 2
                                out[ident] += v * w
                                bygap[m][ident] += v * w
                                stats["resonance_named_histories"] += v * w
                    continue
                h = (abs(N) & -abs(N)).bit_length() - 1
                oddpart = abs(N) >> h
                stats["nonzero_numerator_entries"] += 1
                for b, q in b_fiber(oddpart):
                    D = (q << h) if N > 0 else -(q << h)
                    if (D + k * m) & 1:
                        continue
                    if m & 1 and (m * b + delta) % 4 != 2:
                        continue
                    t, T = (D + k * m) // 2, (D + k * m) // 2 + m
                    if not (1 <= t <= 2 * k and T >= 1):
                        continue
                    stats["admissible_divisor_fiber_candidates"] += 1
                    twice_a = m * b + delta
                    if twice_a & 1:
                        continue
                    a = twice_a // 2
                    if not (low <= a <= high and a & 1 and a != b):
                        continue
                    assert k * a - t * b == c
                    assert (k + 2) * a - T * b == C
                    stats["domain_candidates"] += 1
                    u = actual_names(k * a, S1)
                    v = actual_names((k + 2) * a, S2)
                    if u and v:
                        ident = ((a - low) // 2) * half + (b - low) // 2
                        out[ident] += u * v
                        bygap[m][ident] += u * v
    binary = b"".join(pack("<Q", i) for i in sorted(out))
    return out, bygap, binary, {
        "p": p, "k": k, "m_range": [lo_gap, hi_gap],
        "frozen_science_pin": PIN,
        "pairs": len(out), "joint_named_histories": sum(out.values()),
        "gap_pairs": {str(m): len(bygap[m]) for m in range(lo_gap, hi_gap + 1)},
        "gap_named": {str(m): sum(bygap[m].values()) for m in range(lo_gap, hi_gap + 1)},
        "pair_id_sha256": sha256(binary).hexdigest(),
        "pair_id_bytes": len(binary),
        "named_multiplicity_histogram": dict(sorted(Counter(out.values()).items())),
        "stats": dict(stats), "cached_distinct_oddparts": len(cache)
    }

def original_brute(p, k):
    H, n = 1 << (p - 1), 1 << (p - 2)
    pair, gap = Counter(), defaultdict(Counter)
    for a in range(H + 1, H * 2, 2):
        for b in range(H + 1, H * 2, 2):
            if a == b:
                continue
            fibers = []
            for core in (k, k + 2):
                f, prod = Counter(), core * a
                for i in range(p):
                    for j in range(p):
                        v = (prod ^ (1 << j)) - (1 << i)
                        if v > 0 and v % b == 0:
                            f[v // b] += 1
                fibers.append(f)
            idx = ((a - H - 1) // 2) * n + (b - H - 1) // 2
            for t, u in fibers[0].items():
                for T, v in fibers[1].items():
                    pair[idx] += u * v
                    gap[T - t][idx] += u * v
    return pair, gap

def main(prefix):
    small = []
    for p in range(4, 8):
        H = 1 << (p - 1)
        for k in range(1, H - 2, 2):
            expected, eg = original_brute(p, k)
            got, gg, _, _ = reconstruct(p, k, 1 - 2 * k, 2 * (k + 2) - 1)
            assert expected == got, (p, k, "pair")
            assert {m: dict(z) for m, z in eg.items()} == {
                m: dict(z) for m, z in gg.items() if z}, (p, k, "gap")
            small.append([p, k, len(got), sum(got.values())])
    timer = perf_counter()
    named, gaps, binary, result = reconstruct(19, 21, 0, 6)
    result["q19_seconds"] = round(perf_counter() - timer, 5)
    assert result["pair_id_sha256"] == PRIOR
    assert len(named) == 6203 and sum(named.values()) == 8649
    assert [len(gaps[m]) for m in range(7)] == [6, 442, 4724, 839, 190, 3, 0]
    assert [sum(gaps[m].values()) for m in range(7)] == [6, 614, 6509, 1286, 231, 3, 0]
    result["small_width_exhaustive_cases"] = len(small)
    result["small_width_cases"] = small
    result["prior_sha256"] = PRIOR
    result["prefix958_divisor_window_probes"] = 538183
    result["prefix959_progression_probes"] = 134582
    with open(prefix + "_EXACT_RESULTS.json", "w") as f:
        json.dump(result, f, indent=2, sort_keys=True)
        f.write("\n")
    with open(prefix + "_OFFDIAG_IDS.bin", "wb") as f:
        f.write(binary)
    print(json.dumps({k: v for k, v in result.items() if k not in (
        "small_width_cases", "named_multiplicity_histogram")}, sort_keys=True, indent=2))

if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--prefix", default="PREFIX959B_R6")
    main(a.parse_args().prefix)
