#!/usr/bin/env python3
"""Exact log-interaction sign certificate for frozen R5's two-cut optimizer counts.

Run from any directory:
  python research_notes/portable_direct/r5_requirement_zeta_20261114/VERIFY_R5_LOG_INTERACTION.py
Input: adjacent EXACT_R5_REQUIREMENT_ZETA.json at the frozen scientific commit.
Pure Python arbitrary-precision integers. No floating point is used.
"""
import json
from pathlib import Path

def main():
    source = Path(__file__).with_name("EXACT_R5_REQUIREMENT_ZETA.json")
    rows = json.loads(source.read_text(encoding="utf-8"))["coefficients"]
    assert [r["K"] for r in rows] == list(range(292, 316))
    positive, negative, zero = [], [], []
    determinants = {}
    for row in rows:
        k = row["K"]
        a, b, c, d = (int(row[key]) for key in
                       ("a_empty", "a_15", "a_17", "a_15_17"))
        assert min(a, b, c, d) >= 0 and a > 0
        assert row["N_both_equals_N_all"] is True
        n00, n10, n01, n11 = a, a + b, a + c, a + b + c + d
        delta = n11 * n00 - n10 * n01
        assert delta == a * d - b * c
        determinants[k] = str(delta)
        (positive if delta > 0 else negative if delta < 0 else zero).append(k)
    assert positive == [299, 300, 301]
    assert negative == list(range(293, 299)) + list(range(302, 315))
    assert zero == [292, 315]
    assert determinants[298] == "-1076497326375075298857659506959110681944917740001621115404288000"
    assert determinants[299] == "6318107756242913535087549531738362202519376369239425089850572800"
    assert determinants[301] == "1031647069261457610452470419175449149063555367684265525290152755200"
    assert determinants[302] == "-4583113930077162997476534526313635690686196046485536133081359974400"
    print(json.dumps({"status": "PASS_EXACT_R5_LOG_INTERACTION",
        "input_source": str(source.name),
        "positive": positive, "negative": negative, "zero": zero,
        "integer_arithmetic": True,
        "independent_review": "NOT_REVIEWED"}, sort_keys=True))

if __name__ == "__main__":
    main()
