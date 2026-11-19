#!/usr/bin/env python3
"""X6 Unit158: exact independent P022/Unit157 formula reconciliation.

This is a reconstructed formula-level checker, not an execution of the frozen
P022 Python module or its original tests. Scientific inputs are unchanged.
"""
from math import comb, factorial
import hashlib
import json
import sys


def stirling2(n: int, k: int) -> int:
    if n == 0:
        return int(k == 0)
    row = [0] * (k + 1)
    row[0] = 1
    for size in range(1, n + 1):
        next_row = [0] * (k + 1)
        for blocks in range(1, min(size, k) + 1):
            next_row[blocks] = blocks * row[blocks] + row[blocks - 1]
        row = next_row
    return row[k]


def onto_by_inclusion(m: int, a: int) -> int:
    return sum((-1)**j * comb(a, j) * (a - j)**m for j in range(a + 1))


def historical_p022_sum(n: int, m: int) -> int:
    if m == 0:
        return 1
    return sum(
        comb(n, a) * comb(n-a, b) * factorial(a) * stirling2(m, a)
        * factorial(b) * stirling2(m, b)
        for a in range(1, min(n-1, m)+1)
        for b in range(1, min(n-a, m)+1)
    )


def unit157_onto_sum(n: int, m: int) -> int:
    if m == 0:
        return 1
    return sum(
        comb(n,a)*comb(n-a,b)*onto_by_inclusion(m,a)*onto_by_inclusion(m,b)
        for a in range(1,min(n,m)+1)
        for b in range(1,min(n-a,m)+1)
    )


def checker() -> dict:
    cases = []
    for m in range(1, 13):
        for a in range(1, m+1):
            v=onto_by_inclusion(m,a)
            w=factorial(a)*stirling2(m,a)
            if v!=w:
                raise ValueError((m,a,v,w))
    for n in range(2,9):
        for m in range(0,9):
            old=historical_p022_sum(n,m)
            new=unit157_onto_sum(n,m)
            if old!=new:
                raise ValueError((n,m,old,new))
            native=comb(2*m,m)*old
            cases.append({'n':n,'m':m,'p022_A_root_words':old,'unit157_A_root_words':new,
                          'signed_native_words':native,'shuffle_factor':comb(2*m,m)})
    return {
        'schema':'X6_UNIT158_P022_UNIT157_EXISTING_SOURCE_REUSE_AUDIT_V1',
        'scientific_input_pin':'59538f585d037d09ef687b28715c4bc1a3f9fe03',
        'historical_comparison_pin':'fd2bcff10ca6e147348b6c1236027fc0d2877df3',
        'p022_existing_source':'src/enterprise_math/p022_geodesic_multiplicity.py',
        'p022_existing_test':'tests/test_p022_geodesic_multiplicity.py',
        'formula_equivalence_cases':len(cases),
        'onto_stirling_cases':sum(m for m in range(1,13)),
        'six_axis_new_radius_rows':[r for r in cases if r['n']==6 and 5<=r['m']<=8],
        'existing_P022_module_executed':False,
        'existing_P022_tests_executed':False,
        'unit157_original_checks_rerun':False,
        'claims':['P022 preexisting W_A formula exactly equals Unit157 onto-sum via T(m,a)=a!S(m,a)',
                  'On zero-sum x, signed-native SC count equals C(2m,m) times P022 A_p endpoint count'],
    }

if __name__=='__main__':
    print(json.dumps(checker(), ensure_ascii=False, sort_keys=True, separators=(',',':')))
