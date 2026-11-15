#!/usr/bin/env python3
"""Independent source-aware polynomial-semantics gate for R063, r=1..512.

This script does not run the frozen loader/parts or their 17 gates. It validates
exact integer coefficients and deliberately wrong-degree mutations on the
exact positive two-generator local chart. Source archived N=2500 values are
pinned by literal source-verified integer lexemes, not binary floating point.
"""
import hashlib
import json
import re
from math import comb, isqrt
from pathlib import Path

FROZEN = [
    (0, 50, "1"),
    (14, 48, "29078984349975"),
    (30, 40, "55347740058143507128"),
    (40, 30, "55347740058143507128"),
    (48, 14, "29078984349975"),
    (50, 0, "1"),
]
ARCHIVED_TOTAL = 110695538274255714208
PATTERN = re.compile(r"^\[u\^(\d+) v\^(\d+)\]\(uX_i\+vX_j\)\^(\d+)$")


def direct_roots(r):
    """Exact ordered nonnegative roots; no original Gaussian/Euclid code imported."""
    for a in range(r + 1):
        b2 = r * r - a * a
        b = isqrt(b2)
        if b * b == b2:
            yield a, b


def check_word_coefficient(a, b, expression):
    """Returns the number of distinct noncommuting words in the formal coefficient."""
    m = PATTERN.fullmatch(expression)
    if m is None:
        raise ValueError("not an R063 two-generator coefficient-extraction expression")
    A, B, n = map(int, m.groups())
    if (A, B) != (a, b):
        raise AssertionError("the coefficient marker does not match the branch")
    return comb(n, a) if n == a + b else 0


def pascal(n, k):
    """Second exact integer route, using Pascal's recursion rather than math.comb."""
    row = [1]
    for _ in range(n):
        row = [1] + [row[i - 1] + row[i] for i in range(1, len(row))] + [1]
    return row[k]


def run():
    all_results = []
    branch_count = 0
    mutant_rejections = 0
    root_distribution = {}
    sample = []
    for r in range(1, 513):
        roots = list(direct_roots(r))
        root_distribution[str(len(roots))] = root_distribution.get(str(len(roots)), 0) + 1
        for a, b in roots:
            n = a + b
            original_formula = f"[u^{a} v^{b}](uX_i+vX_j)^{n}"
            actual = check_word_coefficient(a, b, original_formula)
            independent = pascal(n, a)
            assert actual == comb(n, a) == independent
            assert check_word_coefficient(a, b, f"[u^{a} v^{b}](uX_i+vX_j)^{n+1}") == 0
            assert check_word_coefficient(a, b, f"[u^{a} v^{b}](uX_i+vX_j)^{n-1}") == 0
            branch_count += 1
            mutant_rejections += 2
            if r == 50:
                sample.append((a, b, str(actual)))
        # save canonical exact decimal counts and original ordered pairs per radius
        all_results.append([r, [[a, b, str(comb(a + b, a))] for a, b in roots]])
    assert branch_count == 1820 and len(all_results) == 512
    assert [(a, b, int(c)) for a, b, c in sample] == [(a, b, int(c)) for a, b, c in FROZEN]
    exact_total = sum(int(z) for _, _, z in sample)
    assert exact_total == ARCHIVED_TOTAL

    # Test downstream binary64 decoding failure separately. Integer-to-float conversion
    # is intentionally performed ONLY here, never in evidence accumulation.
    lossy_branch_count = sum(int(float(int(s))) != int(s) for _, _, s in sample)
    lossy_total_delta = int(float(exact_total)) - exact_total
    parsed_branch_sum_delta = sum(int(float(int(s))) for _, _, s in sample) - exact_total
    assert lossy_branch_count == 2
    assert lossy_total_delta == 2144
    assert parsed_branch_sum_delta == -1392

    raw = json.dumps(all_results, ensure_ascii=False, separators=(',', ':'), sort_keys=True).encode()
    result = {
        'schema': 'X6_R063_STAGE0_POLYNOMIAL_LOSSLESS_1820_CHECK_V1',
        'science_pin': 'P000_V5_FROZEN',
        'original_loader_blob': 'b4e000a6377f2858ae434eb0eecd0c25c33e8592',
        'original_part02_blob': 'b543e185ec415b512c0ca0421616404cc12a19a7',
        'original_part04_blob': 'a1834a4b39a9d528760e67220b5fe5f368c9e655',
        'archived_path_certificate_blob': 'd4278d6c301587330252ff6683e87773d42cf4e2',
        'r_range': [1, 512],
        'exact_chart_branches_checked': branch_count,
        'wrong_degree_mutants_rejected': mutant_rejections,
        'root_count_distribution': root_distribution,
        'N2500_archived_branches': [[a, b, s] for a, b, s in sample],
        'N2500_exact_total': str(exact_total),
        'N2500_lossy_binary64_branch_fields': lossy_branch_count,
        'N2500_binary64_total_delta_integer': lossy_total_delta,
        'N2500_binary64_sum_branches_delta_integer': parsed_branch_sum_delta,
        'canonical_512_path_count_rows_sha256': hashlib.sha256(raw).hexdigest(),
        'native_original_loader_executed': False,
        'native_17_gates_executed': False,
        'claim_strength': 'INDEPENDENT_AUTHOR_SIDE_EXACT_INTEGER_GATE; NOT_FORMAL_RESULT_OR_NATIVE_BENCHMARK',
    }
    out = Path('/mnt/data/X6_R063_STAGE0_POLYNOMIAL_LOSSLESS_1820_RESULTS_20261115_2200.json')
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('PASS_X6_R063_POLYNOMIAL_SEMANTIC_GATE_1820')
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    run()
