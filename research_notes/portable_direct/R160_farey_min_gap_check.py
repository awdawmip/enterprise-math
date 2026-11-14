"""Exact finite checks for R160; independent of project source implementation.
Tests every binary word of lengths 1..18, using Fraction and full factor scan.
"""
from fractions import Fraction
from collections import Counter
import json


def slope_support(word):
    m = len(word)
    prefix = [0]
    for bit in word:
        prefix.append(prefix[-1] + bit)
    low, high = Fraction(0), Fraction(1)
    for i in range(m):
        for j in range(i + 1, m + 1):
            k, q = j - i, prefix[j] - prefix[i]
            low = max(low, Fraction(q - 1, k))
            high = min(high, Fraction(q + 1, k))
            if low >= high:
                return None
    return low, high


def run(max_m=18):
    out = []
    for m in range(1, max_m + 1):
        count, gap, minimizers = 0, None, []
        for x in range(1 << m):
            word = tuple((x >> j) & 1 for j in range(m - 1, -1, -1))
            interval = slope_support(word)
            if interval is None:
                continue
            count += 1
            width = interval[1] - interval[0]
            if gap is None or width < gap:
                gap = width
                minimizers = ["".join(map(str, word))]
            elif width == gap:
                minimizers.append("".join(map(str, word)))
        if m >= 5:
            expected = Fraction(2, m * (m - 2))
            assert gap == expected, (m, gap, expected)
            assert sorted(minimizers) == sorted(["1" + "0" * (m - 2) + "1", "0" + "1" * (m - 2) + "0"]), (m, minimizers)
        out.append({"m": m, "binary_candidates": 1 << m, "admitted_words": count,
                    "minimum_gap": f"{gap.numerator}/{gap.denominator}", "minimizers": sorted(minimizers)})
    return {"status": "R160_FAREY_GAP_EXACT_PASS", "arithmetic": "fractions.Fraction, no float",
            "complete_binary_enumeration_m": [1, max_m],
            "total_binary_candidates": sum(1 << m for m in range(1, max_m + 1)),
            "total_admitted_words": sum(r["admitted_words"] for r in out), "per_length": out}

if __name__ == "__main__":
    result = run()
    print(json.dumps(result, ensure_ascii=False, indent=2))
