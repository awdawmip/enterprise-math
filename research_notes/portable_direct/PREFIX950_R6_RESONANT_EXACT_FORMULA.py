#!/usr/bin/env python3
"""PREFIX-950: exact integer quarter-balanced resonance formulas and independent Q19 scan.

Scientific input pin: f42f2906d77f24085c123f3ccfe9667d41caa96d
Auxiliary named-XOR observer; no native X6/BRC arithmetic is asserted.
"""
import json
from pathlib import Path

A = 1 << 18
LO, HI = A + 1, (A << 1) - 1
STATE = 1 << 32
EXPECTED_TOTALS = {
    3: 485798, 4: 456313, 5: 424864, 6: 392657,
    7: 360193, 8: 327553, 9: 294784, 10: 262144,
    11: 229376, 12: 196608, 13: 163760, 14: 0,
}


def ceil_half(x):
    return (x + 1) // 2


def dyadic_formula(m, v):
    M, V = 1 << m, 1 << v
    l = M + 1
    if m + v <= 17:
        whole_period_count = A // 8
        boundary_cut = ceil_half(V // l)
        before_state_cut = whole_period_count - boundary_cut
    elif m + v == 18:
        before_state_cut = 0
        for r in range(1, V, 2):
            g = (l * r) // V
            alpha = ((M - 1) * r // V) & 1
            if alpha == 0:
                before_state_cut += max(0, ceil_half(M - g) - 1)
            else:
                before_state_cut += ceil_half(g)
    else:
        raise ValueError((m, v))

    state_upper = min(HI, (STATE - 1) // l)
    cut = 0
    start = max(LO + V, state_upper + 1)
    if start % 2 == 0:
        start += 1
    for a in range(start, HI + 1, 2):
        low_bit = ((M - 1) * a >> v) & 1
        high_bit = (l * a >> (m + v)) & 1
        if low_bit == 0 and high_bit == 1:
            cut += 1
    return {
        "untruncated_formula_count": before_state_cut,
        "state_tail_cut": cut,
        "exact_count": before_state_cut - cut,
    }


def direct_scan(m, v):
    M, V = 1 << m, 1 << v
    l, k = M + 1, M - 1
    upper = min(HI, (STATE - 1) // l)
    ans = 0
    for a in range(LO + V, upper + 1, 2):
        if (((k*a >> v) & 1) == 0 and
            ((l*a >> (m+v)) & 1) == 1):
            ans += 1
    return ans


def check_periods():
    for m in range(3, 7):
        for v in range(1, 7):
            M, V = 1 << m, 1 << v
            P = 2 * M * V
            count = sum(1 for a in range(1, P, 2)
                        if (((M-1)*a >> v) & 1) == 0
                        and (((M+1)*a >> (m+v)) & 1) == 1)
            assert count == P // 8, (m, v, count)


def main():
    check_periods()
    rows = []
    for m in range(3, 15):
        by_v = {}
        for v in range(1, 19 - m):
            f = dyadic_formula(m, v)
            direct = direct_scan(m, v)
            assert direct == f["exact_count"], (m, v, f, direct)
            by_v[str(v)] = f
        total = sum(x["exact_count"] for x in by_v.values())
        assert total == EXPECTED_TOTALS[m], (m, total)
        rows.append({"m": m, "cores": [(1<<m)-1, (1<<m)+1],
                     "total": total, "by_v": by_v})
        print(f"m={m} total={total} checked_v={len(by_v)}")
    obj = {
        "schema": "PREFIX950_R6_EXACT_RESONANCE_COUNT_FORMULA_V1",
        "scientific_input_pin": "f42f2906d77f24085c123f3ccfe9667d41caa96d",
        "model": "auxiliary two-port named-XOR Q19/32-bit",
        "domain": {"m_inclusive": [3,14], "source_bit_max": 18,
                   "odd_moduli_inclusive": [LO,HI],
                   "state_upper_exclusive": STATE},
        "evidence": "Exact formula vs independent full Q19 direct integer scan; bounded period assertions passed",
        "rows": rows, "all_assertions_passed": True,
        "independent_review": False, "formal_admission": False
    }
    path = Path(__file__).with_name("PREFIX950_R6_EXACT_FORMULA_RESULTS.json")
    path.write_text(json.dumps(obj, indent=2) + "\n")
    print("RESULTS", path)


if __name__ == "__main__":
    main()
