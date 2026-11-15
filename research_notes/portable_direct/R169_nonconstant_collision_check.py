#!/usr/bin/env python3
"""R169: independent exact strip-pair oracle for a multi-one collision family."""
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
import json

@lru_cache(maxsize=None)
def phase_signature(word):
    n = len(word)
    p = [0]
    for c in word:
        assert c in '01'
        p.append(p[-1] + int(c))
    alpha = Q(0)
    beta = Q(1)
    for i in range(n):
        for j in range(i + 1, n + 1):
            d = p[j] - p[i]
            alpha = max(alpha, Q(d - 1, j - i))
            beta = min(beta, Q(d + 1, j - i))
    if not alpha < beta:
        return None
    A = min(Q(p[i] + 1) - i * alpha for i in range(n + 1))
    B = max(Q(p[i]) - i * beta for i in range(n + 1))
    return alpha, beta, A, B

def family(k):
    assert k >= 2
    return ('01' + '0' * k + '1' + '0' * (k - 1) + '1',
            '01' + '0' * (k - 1) + '1' + '0' * k + '1')

def str_fraction(q):
    return f'{q.numerator}/{q.denominator}'

def main():
    checks = {'family_members': 0, 'precollision_prefixes': 0,
              'zero_extension_cases': 0, 'exhaustive_suffix_cases': 0,
              'exhaustive_aliases': 0}
    sample = []
    # Full endpoint oracle, not the proposed closed formula, provides ground truth.
    for k in range(2, 29):
        u, v = family(k)
        m = 2 * k + 3
        target = (Q(1, k + 1), Q(1, k), Q(k, k + 1), Q(k - 2, k))
        assert len(u) == len(v) == m
        assert phase_signature(u) == phase_signature(v) == target
        checks['family_members'] += 2
        for n in range(k + 3, m):
            su = phase_signature(u[:n])
            sv = phase_signature(v[:n])
            assert su is not None and sv is not None
            assert su[0] == Q(1, k + 2)
            assert sv[0] == Q(1, k + 1)
            assert su != sv
            checks['precollision_prefixes'] += 1
        # The first k-1 zeros preserve the original exact signature. The k-th splits it.
        for h in range(0, min(k + 2, 13)):
            su, sv = phase_signature(u + '0' * h), phase_signature(v + '0' * h)
            assert (su is not None and sv is not None and su == sv) == (h <= k - 1)
            if h <= k - 1:
                assert su == target
            checks['zero_extension_cases'] += 1
        if k <= 7:
            sample.append({'k': k, 'm': m, 'u': u, 'v': v,
                           'signature': [str_fraction(t) for t in target],
                           'first_collision_after_appends': k,
                           'max_additional_preserving_length': k - 1})
    # All common binary continuations of bounded length; both invalid is NOT collision.
    for k in range(2, 10):
        u, v = family(k)
        for h in range(0, 7):
            for z in product('01', repeat=h):
                suffix = ''.join(z)
                su, sv = phase_signature(u + suffix), phase_signature(v + suffix)
                actual = su is not None and sv is not None and su == sv
                expected = h <= k - 1 and suffix == '0' * h
                assert actual == expected, (k, suffix, su, sv)
                checks['exhaustive_suffix_cases'] += 1
                checks['exhaustive_aliases'] += int(actual)
    data = {
        'schema': 'EM_R169_EXACT_REPRODUCIBILITY_V1',
        'frozen_science_pin': '43ec6098b1330ae86d0a7863be336c5d97f6ef34',
        'method': 'Exact Fraction O(n^2) strip-pair support oracle, all endpoint extrema',
        'k_full_prefix_and_zero_range': [2, 28],
        'k_exhaustive_suffix_range': [2, 9],
        'exhaustive_suffix_length_range': [0, 6],
        'checks': checks,
        'examples': sample,
        'marker': 'R169_NONCONSTANT_BIRTH_LIFESPAN_EXACT_PASS',
        'review': 'AUTHOR_CHECKED_NOT_INDEPENDENTLY_REVIEWED'
    }
    print(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()
