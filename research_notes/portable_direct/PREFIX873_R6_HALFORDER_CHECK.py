#!/usr/bin/env python3
"""PREFIX-873: exact signed-half-order BRC near-gap exclusion certificates.

Usage: python3 PREFIX873_R6_HALFORDER_CHECK.py
Emits JSON to stdout. Pure Python integers; no external dependencies.
"""
import json
from math import gcd

G = (1, 3, 5, 7, 9, 11, 13, 15, 19, 21, 23, 25, 27, 29,
     35, 37, 39, 47, 49, 53, 55, 59, 61)


def signed_order(g):
    if g == 1:
        return 1, -1
    for m in range(1, 100):
        residue = pow(2, m, g)
        if residue == 1:
            return m, -1
        if residue == g - 1:
            return m, +1
    raise AssertionError("unexpected missing signed order")


def certificate(p, g, qh, m, sigma, k):
    n = 1 << p
    ql = qh - 2 * g
    assert qh % 2 == ql % 2 == 1 and ql >= 3
    assert m >= 1 and m + 1 < p
    assert (1 << m) + sigma == k * g
    assert k * qh + 3 < n

    target = 1 if sigma == 1 else 0
    r = next(t for t in range(4) if ((k * qh + t) >> 1) & 1 == target)
    u, v = r, r + (1 << (m + 1))
    old2 = r + k * qh
    new2 = old2 ^ 2
    assert 0 <= u < n and 0 <= v < n
    assert 0 <= old2 < n and 0 <= new2 < n
    assert (u ^ v).bit_count() == 1 and (old2 ^ new2).bit_count() == 1
    assert u % qh == old2 % qh
    assert v % ql == new2 % ql
    assert new2 - v == k * ql
    return [u, v, old2, new2]


def main():
    p = 32
    n, q = 1 << p, (1 << 19) - 1
    records = []
    total = 0
    extremal_eligible = 0

    for g in G:
        m, sigma = signed_order(g)
        k = ((1 << m) + sigma) // g
        high_cap = min(q, (n - 4) // k)
        if high_cap % 2 == 0:
            high_cap -= 1
        low_high = 2 * g + 3
        count = max(0, (high_cap - low_high) // 2 + 1)
        assert count > 0 and m + 1 < p

        maximal = certificate(p, g, high_cap, m, sigma, k)
        extremal_cofactor = q // g
        if extremal_cofactor % 2 == 0:
            extremal_cofactor -= 1
        extremal_qh = g * extremal_cofactor
        check_extremal = (extremal_qh <= high_cap)
        if check_extremal:
            certificate(p, g, extremal_qh, m, sigma, k)
            extremal_eligible += 1

        total += count
        records.append({
            "g_half_gap": g, "signed_half_order": m, "sigma": sigma,
            "k": k, "max_odd_qH": high_cap,
            "count_unordered": count, "count_ordered": 2 * count,
            "witness_at_max_qH": maximal,
            "old_extremal_pair_covered": check_extremal
        })

    assert total == 4632684
    assert extremal_eligible == 17
    checks = {}
    for pp in range(6, 13):
        nn = 1 << pp
        count = 0
        for g in range(1, 32, 2):
            m, sigma = signed_order(g)
            if m + 1 >= pp:
                continue
            k = ((1 << m) + sigma) // g
            for qh in range(2 * g + 3, nn - 3, 2):
                if k * qh + 3 >= nn:
                    continue
                certificate(pp, g, qh, m, sigma, k)
                count += 1
        checks[str(pp)] = count
    assert checks == {"6": 146, "7": 409, "8": 973, "9": 2109,
                      "10": 4378, "11": 8962, "12": 18157}
    assert sum(checks.values()) == 35134
    print(json.dumps({
        "schema": "PREFIX873_SIGNED_HALFORDER_V1",
        "p": p, "peak_bits": 19,
        "frozen_scientific_pin": "f42f2906d77f24085c123f3ccfe9667d41caa96d",
        "half_gap_parameters": len(G),
        "excluded_unordered_pairs": total,
        "excluded_ordered_pairs": 2 * total,
        "covered_extremal_half_gaps": extremal_eligible,
        "bounded_witness_checks_by_p": checks,
        "bounded_witness_checks_total": sum(checks.values()),
        "records": records,
        "verification": "ALL_EXACT_ASSERTIONS_PASSED"
    }, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
