#!/usr/bin/env python3
"""Exact PREFIX-874 32-source 19-bit odd-half-gap sieve, two independent algorithms."""
import json
from math import isqrt

P, B = 32, 19
N, Q = 1 << P, (1 << B) - 1
GMAX = (Q - 3) // 2


def signed_order(g):
    if g == 1:
        return 1, -1
    x = 2 % g
    for m in range(1, P - 1):
        if x == 1:
            return m, -1
        if x == g - 1:
            return m, 1
        x = x * 2 % g
    return None


def certificate(g, m, sigma, k, high):
    low = high - 2 * g
    r = next(t for t in range(4)
             if (((k * high + t) >> 1) & 1) == (sigma == 1))
    old, new = r, r + (1 << (m + 1))
    old2, new2 = r + k * high, (r + k * high) ^ 2
    assert 0 <= old < N and 0 <= new < N
    assert 0 <= old2 < N and 0 <= new2 < N
    assert (old ^ new).bit_count() == 1
    assert (old2 ^ new2).bit_count() == 1
    assert old % high == old2 % high and new % low == new2 % low
    assert new2 - new == k * low
    return [old, new, old2, new2]


def assemble(g, m, sigma):
    k = ((1 << m) + sigma) // g
    cap = min(Q, (N - 4) // k)
    cap -= (cap % 2 == 0)
    minimum = 2 * g + 3
    count = max(0, (cap - minimum) // 2 + 1)
    if not count:
        return None
    return {"g": g, "m": m, "sigma": sigma, "k": k,
            "max_q_high": cap, "pair_count": count,
            "witness_at_max": certificate(g, m, sigma, k, cap)}


def direct_scan():
    rows = []
    for g in range(1, GMAX + 1, 2):
        signed = signed_order(g)
        if signed is None:
            continue
        item = assemble(g, *signed)
        if item:
            rows.append(item)
    return rows


def independent_divisor_enumeration():
    options = {}
    for m in range(1, P - 1):
        for sigma in (-1, 1):
            val = (1 << m) + sigma
            for d in range(1, isqrt(val) + 1, 2):
                if val % d == 0:
                    for g in (d, val // d):
                        if g <= GMAX and g not in options:
                            options[g] = (m, sigma)
    rows = []
    for g in sorted(options):
        item = assemble(g, *options[g])
        if item:
            rows.append(item)
    return rows


def main():
    a, b = direct_scan(), independent_divisor_enumeration()
    assert a == b
    total = sum(t["pair_count"] for t in a)
    full = sum(t["max_q_high"] == Q for t in a)
    assert len(a) == 360 and full == 239 and total == 61017906
    print(json.dumps({
        "schema": "PREFIX874_ALL_ODD_HALF_GAPS_V1",
        "p": P, "peak_bits": B,
        "frozen_scientific_pin": "f42f2906d77f24085c123f3ccfe9667d41caa96d",
        "tested_odd_half_gap_domain": [1, GMAX],
        "algorithm_1": "DIRECT_MODULAR_SIGNED_ORDER_SCAN",
        "algorithm_2": "INDEPENDENT_DIVISOR_ENUMERATION",
        "families": len(a), "full_width_families": full,
        "partial_families": len(a) - full,
        "excluded_unordered": total, "excluded_ordered": 2 * total,
        "rows": a, "verification": "ALL_EXACT_ASSERTIONS_PASSED"
    }, indent=2))


if __name__ == "__main__":
    main()
