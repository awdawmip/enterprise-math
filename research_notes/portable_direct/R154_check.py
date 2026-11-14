#!/usr/bin/env python3
"""Exhaustive exact mechanical-word slope-endpoint classification.
All computations use integer cross products and gcd; no floats.
"""
import json
from math import gcd

def support(s):
    m = len(s)
    p = [0]
    for a in s:
        p.append(p[-1] + (a == '1'))
    an, ad, cn, cd = 0, 1, 1, 1
    for i in range(m):
        pi = p[i]
        for j in range(i + 1, m + 1):
            k = j - i
            q = p[j] - pi
            lo, hi = q - 1, q + 1
            if lo * ad > an * k:
                an, ad = lo, k
            if hi * cd < cn * k:
                cn, cd = hi, k
    if an * cd >= cn * ad:
        return None
    g = gcd(an, ad)
    a, b = an // g, ad // g
    g = gcd(cn, cd)
    c, d = cn // g, cd // g
    return (a, b, c, d)

def expected(m):
    if m == 1:
        return {'0', '1'}
    if m == 2:
        return {'01', '10'}
    if m % 2 == 0:
        return {'01' * (m // 2), '10' * (m // 2)}
    return set()

def verify(M=16):
    stats = []
    total_words = total_sturm = total_equal = 0
    for m in range(1, M + 1):
        equal = []
        num_sturm = 0
        for v in range(1 << m):
            s = format(v, f'0{m}b')
            q = support(s)
            if q is None:
                continue
            num_sturm += 1
            a, b, c, d = q
            if b == d:
                equal.append(s)
                if m >= 4:
                    assert a > 0 and c < b and c == a + 1
                    assert b == m - 1 and (a, c) == ((b - 1)//2, (b + 1)//2)
        assert set(equal) == expected(m), (m, equal)
        total_words += 1 << m
        total_sturm += num_sturm
        total_equal += len(equal)
        stats.append({'m': m, 'binary_words': 1 << m, 'admissible_words': num_sturm,
                      'equal_denominator_words': len(equal), 'equal_words': equal})
    return {'tag': 'R154_EXACT_ALL_LENGTH_CLASSIFICATION_FINITE_CHECK_PASS',
            'arithmetic': 'integer cross products and gcd only',
            'checked_lengths': [1, M], 'all_binary_words': total_words,
            'admissible_sturmian_factors': total_sturm,
            'equal_denominator_factors': total_equal,
            'rows': stats,
            'scope': 'Finite exhaustive corroboration only; all-length claim follows from the separate human proof.'}

if __name__ == '__main__':
    import sys
    M = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    result = verify(M)
    with open('R154_verification.json', 'w') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
        f.write('\n')
    print(result['tag'])
    print({k: result[k] for k in ('checked_lengths', 'all_binary_words',
                                  'admissible_sturmian_factors', 'equal_denominator_factors')})
    print([(r['m'], r['equal_denominator_words']) for r in result['rows']])
