#!/usr/bin/env python3
"""PREFIX-893 independent exact carry-DP completion of the 67 C++ residual pairs.
Usage: python3 PREFIX893_R6_REMAINDER_FF_DP.py PREFIX893_R6_PANEL_EXCLUSION_PRECERT.json
Python 3 stdlib exact integers; no external I/O, no floating point.
"""
import json
import sys
from math import gcd


def least_base(a, i, si, j, sj, p):
    """Find x: 0<=x,x+a<2**p and signed XOR deltas si*2**i, sj*2**j."""
    states = {0: 0}  # addition carry -> reconstructed low bits of x
    for h in range(p):
        next_states = {}
        for carry, x in states.items():
            for xb in (0, 1):
                if h == i and xb != (0 if si == 1 else 1):
                    continue
                full = xb + ((a >> h) & 1) + carry
                if h == j and (full & 1) != (0 if sj == 1 else 1):
                    continue
                next_states.setdefault(full >> 1, x | (xb << h))
        states = next_states
        if not states:
            return None
    return states.get(0)  # final carry zero ensures x+a<2**p


def general_ff(q1, q2, p=32):
    n = 1 << p
    kmax = (n - 1) // q1
    g = gcd(q1, q2)
    m = q2 // g
    assert q1 * m >= n and m > kmax  # zero-step branch was removed
    inv = pow(q1 // g, -1, m)
    for i in range(p):
        bi = 1 << i
        for si in (1, -1):
            d = si * bi
            for j in range(p):
                bj = 1 << j
                for sj in (1, -1):
                    e = sj * bj
                    if (d - e) % g:
                        continue
                    k = (((d - e) // g) * inv) % m
                    if not (1 <= k <= kmax):
                        continue
                    a = k * q1
                    x = least_base(a, i, si, j, sj, p)
                    if x is None:
                        continue
                    X, Y = (x, x + d), (x + a, x + a + e)
                    assert 0 <= min(*X, *Y) and max(*X, *Y) < n
                    assert X[1] == (X[0] ^ bi) and Y[1] == (Y[0] ^ bj)
                    assert X != Y
                    assert (X[0] % q1, X[1] % q2) == (Y[0] % q1, Y[1] % q2)
                    return dict(q1=q1, q2=q2, k=k, a=a, i=i, j=j, d=d,
                                e=e, x=x, X=list(X), Y=list(Y))
    return None


def test_dp():
    total = 0
    for p in range(2, 7):
        n = 1 << p
        for a in range(1, n):
            for i in range(p):
                for si in (-1, 1):
                    for j in range(p):
                        for sj in (-1, 1):
                            pred = least_base(a, i, si, j, sj, p)
                            direct = next((x for x in range(n-a)
                                           if ((x ^ (1 << i)) - x) == si * (1 << i)
                                           and (((x+a) ^ (1 << j)) - (x+a)) == sj * (1 << j)), None)
                            assert (pred is None) == (direct is None)
                            total += 1
    return total


def main(path):
    base = json.load(open(path, encoding='utf-8'))
    assert base['schema'] == 'PREFIX893_R6_PANEL_EXCLUSION_V1'
    assert base['totals'] == {'pairs': 2097152, 'zf': 1308292,
                              'positive_completion_only': 10386,
                              'zero_step_only': 15250,
                              'zero_anchored_ff_only': 763157,
                              'requires_general_ff': 67}
    rem = base['remainder']
    assert len(rem) == 67 and len(set(map(tuple, rem))) == 67
    witnesses = [general_ff(*pair) for pair in rem]
    assert all(w is not None for w in witnesses)
    checks = test_dp()
    print(json.dumps({'schema': 'PREFIX893_R6_FULL_PANEL_CERTIFICATE_V1',
                      'frozen_scientific_pin': 'f42f2906d77f24085c123f3ccfe9667d41caa96d',
                      'p': 32, 'modulus_range': [262145, 524287],
                      'panel_totals': base['totals'],
                      'general_ff_witnesses': witnesses,
                      'general_ff_unresolved': [],
                      'small_dp_direct_comparison_cases': checks,
                      'classification': 'AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED'},
                     indent=2, ensure_ascii=False, sort_keys=True))


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'PREFIX893_R6_PANEL_EXCLUSION_PRECERT.json')
