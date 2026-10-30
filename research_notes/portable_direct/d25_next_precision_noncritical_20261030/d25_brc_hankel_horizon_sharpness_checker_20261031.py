#!/usr/bin/env python3
"""Exact author check for strictly positive BRC shared-label horizon sharpness.

This checks a declared finite collection of auxiliary integer kernels;
no native Heartbeat World state update is executed.
"""
from __future__ import annotations

from itertools import product
from math import comb, factorial
import json
from pathlib import Path

Z = (1, -1, -1, 1)


def value(label: int, word: tuple[int, ...], baseline: int) -> int:
    mass = 1
    for y in word:
        mass *= baseline + label * Z[y]
    return mass


def counts(m: int, word: tuple[int, ...]) -> tuple[int, int]:
    n = 2 * m - 1
    baseline = n + 1
    a = sum(comb(n, j) * value(j, word, baseline) for j in range(0, n + 1, 2))
    b = sum(comb(n, j) * value(j, word, baseline) for j in range(1, n + 1, 2))
    return a, b


def check_one(m: int) -> dict:
    assert isinstance(m, int) and m >= 1
    n = 2 * m - 1
    baseline = n + 1
    assert min(baseline + j * z for j in range(n + 1) for z in Z) >= 1
    assert sum(comb(n, j) for j in range(0, n + 1, 2)) == 2 ** (n - 1)
    assert sum(comb(n, j) for j in range(1, n + 1, 2)) == 2 ** (n - 1)
    by_length = []
    evaluated_words = 0
    evaluated_original_label_terms = 0
    first_difference = None
    for t in range(n + 1):
        total_a = 0
        total_b = 0
        l1_diff = 0
        for word in product(range(4), repeat=t):
            a, b = counts(m, word)
            evaluated_words += 1
            evaluated_original_label_terms += n + 1
            total_a += a
            total_b += b
            difference = a - b
            if t < n:
                assert difference == 0, (m, word, difference)
            else:
                expected = (-1) ** n * factorial(n)
                for symbol in word:
                    expected *= Z[symbol]
                assert difference == expected, (m, word, difference, expected)
                assert difference != 0
                if first_difference is None:
                    first_difference = {"word": list(word), "a": a, "b": b, "a_minus_b": difference}
            l1_diff += abs(difference)
        expected_total = 2 ** (n - 1) * (4 * baseline) ** t
        assert total_a == total_b == expected_total, (m, t, total_a, total_b)
        assert l1_diff == (4**n * factorial(n) if t == n else 0)
        by_length.append({
            "length": t,
            "observed_words": 4**t,
            "source_mass_each_type": expected_total,
            "full_history_L1_gap": l1_diff,
        })
    assert first_difference is not None
    return {
        "m_each_type": m,
        "comparison_dimension_d": 2*m,
        "sharp_horizon_d_minus_1": n,
        "baseline_per_joint_output": baseline,
        "label_indices_type_A_even": list(range(0, n + 1, 2)),
        "label_indices_type_B_odd": list(range(1, n + 1, 2)),
        "initial_integer_weight_sum_each": 2 ** (n - 1),
        "strictly_positive_joint_kernels": True,
        "transition": "I_m (persistent labels; admissible special case of evolving-label models)",
        "evaluated_words": evaluated_words,
        "evaluated_original_label_terms": evaluated_original_label_terms,
        "first_difference": first_difference,
        "length_summary": by_length,
    }


def main() -> None:
    cases = [check_one(m) for m in range(1, 5)]
    certificate = {
        "schema": "EM_D25_BRC_HANKEL_SHARPNESS_AUTHOR_EXACT_V1",
        "status": "PASS",
        "date": "2026-10-31",
        "model_scope": "auxiliary two-source four-symbol positive integer path kernels; T=identity",
        "math_claim": "all words of length < 2m-1 agree, and all length 2m-1 words differ by signed factorial, for every m>=1",
        "argument": "binomial N-th finite differences; universal m is proven algebraically, finite checks only for m=1..4",
        "total_word_cases": sum(x["evaluated_words"] for x in cases),
        "total_source_label_terms": sum(x["evaluated_original_label_terms"] for x in cases),
        "cases": cases,
        "evidence_level": "AUTHOR_EXACT_CHECKED_NOT_INDEPENDENT_NOT_NATIVE",
    }
    target = Path(__file__).with_name("d25_brc_hankel_horizon_sharpness_author_check_20261031.json")
    target.write_text(json.dumps(certificate, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(f"PASS cases={len(cases)} words={certificate['total_word_cases']} label_terms={certificate['total_source_label_terms']} output={target}")


if __name__ == "__main__":
    main()
