#!/usr/bin/env python3
"""Exact checks for R156 padded three-one scalar Sturmian aliases.

Only Python stdlib fractions and integers; no floating point.
"""
from fractions import Fraction
import json


def core(h):
    return "1" + "0" * (h - 1) + "1" + "0" * h + "1"


def words(h, t, s):
    w = core(h)
    return ("0" * t + w + "0" * s,
            "0" * t + w[::-1] + "0" * s)


def exact_cuts(w):
    m = len(w)
    pref = [0]
    for bit in w:
        pref.append(pref[-1] + int(bit))
    lower, upper = Fraction(0), Fraction(1)
    for i in range(m):
        for j in range(i + 1, m + 1):
            ones = pref[j] - pref[i]
            k = j - i
            lower = max(lower, Fraction(ones - 1, k))
            upper = min(upper, Fraction(ones + 1, k))
    if lower >= upper:
        return None
    U = lower.denominator * (1 + min(
        Fraction(pref[j]) - j * lower for j in range(m + 1)))
    V = upper.denominator * max(
        Fraction(pref[j]) - j * upper for j in range(m + 1))
    return lower, upper, int(U), int(V)


def count(L, cuts):
    alpha, beta, U, V = cuts
    # ceil(p/q) == -((-p)//q) for q>0
    top_num = L * beta.numerator - V
    bot_num = L * alpha.numerator - U
    return -((-top_num) // beta.denominator) - (
        bot_num // alpha.denominator) - 1


def main():
    result = {
        "marker": "R156_PADDED_THREE_ONE_ALIASES_PASS",
        "model": "external scalar tied-phase S23 observer",
        "h_range_inclusive": [2, 14],
        "pad_pair_cases": 0,
        "non_reversal_pairs": 0,
        "count_shift_checks": 0,
        "last_zero_and_after_checks": 0,
        "representative": {},
    }
    for h in range(2, 15):
        base_cuts = (Fraction(1, h + 1), Fraction(1, h), h + 1, h - 1)
        for t in range(h):
            for s in range(h):
                left, right = words(h, t, s)
                expected = (Fraction(1, h + 1), Fraction(1, h),
                            h + 1 - t, h - 1 - t)
                assert left != right
                assert exact_cuts(left) == expected, (h, t, s, left)
                assert exact_cuts(right) == expected, (h, t, s, right)
                if t != s:
                    assert left[::-1] != right
                    result["non_reversal_pairs"] += 1
                # Includes small coefficients, the exact last zero and
                # 10**12+17 to check exact arithmetic at large L.
                for L in (1, 2, h, h * h - 1 - t,
                          h * h - t, h * h + 1, 10**12 + 17):
                    actual = count(L, expected)
                    assert actual == count(L + t, base_cuts)
                    assert actual >= 0
                    result["count_shift_checks"] += 1
                assert count(h * h - 1 - t, expected) == 0
                assert count(h * h - t, expected) >= 1
                result["pad_pair_cases"] += 1
                result["last_zero_and_after_checks"] += 1
                if (h, t, s) == (2, 1, 0):
                    result["representative"] = {
                        "h": h, "t": t, "s": s,
                        "word_pair": [left, right],
                        "lower": str(expected[0]),
                        "upper": str(expected[1]),
                        "U": expected[2], "V": expected[3],
                        "last_absent_K": h * h - t,
                        "permanent_K": h * h + 1 - t,
                        "C_K2": count(1, expected),
                        "C_K3": count(2, expected),
                        "C_K4": count(3, expected),
                    }
    print(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
