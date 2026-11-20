#!/usr/bin/env python3
"""Exact 6D primitive short-ball projective collision certificate."""
from itertools import combinations, product
from collections import Counter
from math import gcd, isqrt

def witnesses(B):
    r = isqrt(B)
    return [v for v in product(range(-r, r + 1), repeat=6)
            if 0 < sum(x*x for x in v) <= B
            and gcd(*v) == 1
            and next(x for x in v if x != 0) > 0]

def minor_content(v, w):
    return gcd(*(v[i]*w[j] - v[j]*w[i]
                 for i in range(6) for j in range(i+1, 6)))

def proportional_mod(v, w, m):
    """Independent direct search for a unit scalar."""
    return any(gcd(a, m) == 1 and all((w[i]-a*v[i]) % m == 0
                                      for i in range(6))
               for a in range(m))

def check(B):
    vs = witnesses(B)
    counts = Counter()
    checks = 0
    for idx, (v, w) in enumerate(combinations(vs, 2)):
        d = minor_content(v, w)
        assert 1 <= d <= B
        counts[d] += 1
        if d > 1 or idx % 257 == 0:
            for m in (2, 3, 4, 5, 6, 7, 8, 9, 10, 11):
                assert (d % m == 0) == proportional_mod(v, w, m)
                checks += 1
    return len(vs), dict(sorted(counts.items())), checks

if __name__ == '__main__':
    for B in (3, 5, 7, 9):
        n, contents, checks = check(B)
        print(f'B={B}: classes={n}, content_hist={contents}, congruence_tests={checks}')
