#!/usr/bin/env python3
"""Exact independent verification of the frozen R063 C2 prime-factor criterion.

The two-coordinate positive-sector chart is historical and sector-local.
No original pinned loader, 17 gates or original 512-row replay is executed here.
"""
import hashlib
import json
from collections import Counter
from math import isqrt
from pathlib import Path

MAX_R = 512
OUT = Path('/mnt/data/X6_R063_C2_UNSCALED_SQUARE_LIFT_PRIME_CRITERION_RESULTS_20261115_2230.json')


def factor(n):
    result = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            result[d] = result.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        result[n] = result.get(n, 0) + 1
    return result


def direct_norm_roots(n):
    out = set()
    for a in range(isqrt(n) + 1):
        b2 = n - a * a
        b = isqrt(b2)
        if b * b == b2:
            out.add((a, b))
    return out


def c2_unscaled(r):
    out = set()
    for m, n in direct_norm_roots(r):
        if m < n:
            continue
        a, b = m * m - n * n, 2 * m * n
        out.add((a, b))
        out.add((b, a))
    return out


def predicted(r):
    split_product, half_split_product = 1, 1
    inert_even = True
    split_present = False
    for p, exponent in factor(r).items():
        if p % 4 == 1:
            split_product *= 2 * exponent + 1
            half_split_product *= exponent + 1
            split_present = True
        elif p % 4 == 3 and exponent % 2:
            inert_even = False
    diagonal_or_axis = (isqrt(r) ** 2 == r or
                        (r % 2 == 0 and isqrt(r // 2) ** 2 == r // 2))
    c2_count = (half_split_product + int(diagonal_or_axis)) if inert_even else 0
    full_count = 1 + split_product
    category = 'inert_odd' if not inert_even else 'split' if split_present else 'complete'
    return c2_count, full_count, category


def main():
    totals = Counter()
    complete_radii = []
    examples = {}
    canonical_rows = []
    for r in range(1, MAX_R + 1):
        original_c2 = c2_unscaled(r)
        original_full = direct_norm_roots(r * r)
        expected_c2, expected_full, category = predicted(r)
        assert original_c2 <= original_full, ('extraneous C2 root', r)
        assert len(original_c2) == expected_c2, ('C2 formula mismatch', r)
        assert len(original_full) == expected_full, ('all-root formula mismatch', r)
        assert (original_c2 == original_full) == (category == 'complete'), ('criterion mismatch', r)
        missing = sorted(original_full - original_c2)
        totals[category] += 1
        totals['missing_' + category] += len(missing)
        totals['total_full_roots'] += len(original_full)
        totals['total_c2_roots'] += len(original_c2)
        if category == 'complete':
            complete_radii.append(r)
        if r in (3, 5, 50):
            examples[str(r)] = {'C2': sorted(original_c2), 'full': sorted(original_full),
                                'missing': missing, 'category': category}
        canonical_rows.append([r, len(original_c2), len(original_full), category,
                               [list(pair) for pair in missing]])
    assert totals['complete'] == 28 and totals['inert_odd'] == 332
    assert totals['split'] == 152
    assert totals['missing_inert_odd'] == 962 and totals['missing_split'] == 418
    assert totals['total_full_roots'] == 1820
    assert totals['total_full_roots'] - totals['total_c2_roots'] == 1380
    assert examples['50']['missing'] == [(30, 40), (40, 30)]
    data = {
        'schema': 'X6_R063_C2_PRIME_CLASSIFICATION_V1',
        'research_scope': 'FROZEN_R063_TWO_POSITIVE_GENERATOR_CHART',
        'loader_blob_sha1': 'b4e000a6377f2858ae434eb0eecd0c25c33e8592',
        'original_c2_source_blob_sha1': '913078c642b8995bfc135ef0350912387a17cdb8',
        'r_range': [1, MAX_R],
        'formula': 'D=1+product_{p=1 mod4}(2e_p+1); C2=I(inert exponents even)*(product_{p=1 mod4}(e_p+1)+I(r=square or twice square))',
        'exact_criterion': 'C2 complete iff r=2^a*s^2, a>=0, s odd and all prime factors of s are 3 mod 4',
        'category_radii': {name: totals[name] for name in ('complete', 'inert_odd', 'split')},
        'missing_roots_by_category': {name: totals['missing_' + name] for name in ('complete', 'inert_odd', 'split')},
        'full_roots_total': totals['total_full_roots'],
        'c2_roots_total': totals['total_c2_roots'],
        'missing_roots_total': totals['total_full_roots'] - totals['total_c2_roots'],
        'complete_radii': complete_radii,
        'examples': examples,
        'rows_sha256': hashlib.sha256(json.dumps(canonical_rows, separators=(',', ':'), sort_keys=True).encode()).hexdigest(),
        'original_native_loader_executed': False,
        'original_17_gates_executed': False,
        'evidence_status': 'AUTHOR_EXECUTED_EXACT_512_FINITE_CHECK_UNREVIEWED_NOT_ADMITTED',
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('PASS_X6_R063_C2_PRIME_CLASSIFICATION_512')
    print(json.dumps({'category_radii': data['category_radii'],
                      'missing_roots_by_category': data['missing_roots_by_category'],
                      'rows_sha256': data['rows_sha256']}, sort_keys=True))


if __name__ == '__main__':
    main()
