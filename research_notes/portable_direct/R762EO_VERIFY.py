#!/usr/bin/env python3
"""R762EO: exact Newton-polygon certificate.
Usage: python R762EO_VERIFY.py /path/to/R762EM_Q9_SPECTRAL_EVIDENCE.json
The input is the immutable evidence from R762EM PR #2724@b21958c0.
Python standard library only, integer/rational arithmetic only.
"""
import json
import sys
from collections import defaultdict
from fractions import Fraction


def v3(n):
    if not n:
        return None  # +infinity, skip point on lower hull
    k = 0
    while n % 3 == 0:
        n //= 3
        k += 1
    return k


def newton(coeff):
    pts = [(i, v3(c)) for i, c in enumerate(coeff) if c]
    hull = []
    for pt in pts:
        while len(hull) >= 2:
            a, b = hull[-2:]
            cross = (b[0]-a[0])*(pt[1]-a[1]) - (b[1]-a[1])*(pt[0]-a[0])
            if cross <= 0:
                hull.pop()
            else:
                break
        hull.append(pt)
    edges = []
    for a, b in zip(hull, hull[1:]):
        dx = b[0]-a[0]
        valuation = Fraction(a[1]-b[1], dx)
        edges.append((valuation, dx))
    return hull, edges


def multiply(a, b):
    c = [0] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def main(path):
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    factors = data['factors']
    assert len(factors) == 27
    mu = [1]
    distinct = defaultdict(int)
    weighted = defaultdict(int)
    zeros = 0
    for item in factors:
        coeff = item['polynomial_low_to_high']
        assert coeff[-1] == 1 and len(coeff)-1 == item['degree']
        multiplicity = item['multiplicity']
        mu = multiply(mu, coeff)
        if coeff[0] == 0 and len(coeff) == 2:  # the exact root T
            assert coeff == [0, 1]
            zeros += multiplicity
            continue
        assert coeff[0] != 0
        _, edges = newton(coeff)
        for valuation, degree in edges:
            distinct[str(valuation)] += degree
            weighted[str(valuation)] += degree * multiplicity
    hull, edges = newton(mu)
    assert hull == [(1, 58), (13, 46), (37, 30), (127, 0)]
    assert [(str(s), h) for s, h in edges] == [('1', 12), ('2/3', 24), ('1/3', 90)]
    assert dict(distinct) == {'1/3': 90, '2/3': 24, '1': 12}
    assert dict(weighted) == {'1/3': 486, '2/3': 144, '1': 39}
    assert zeros == 60 and len(mu) == 128 and mu[0] == 0 and mu[-1] == 1
    assert sum(weighted.values()) + zeros == 729
    print(json.dumps({'status': 'PASS', 'mu_degree': len(mu)-1,
                      'newton_vertices': hull,
                      'distinct_nonzero_by_valuation': dict(sorted(distinct.items())),
                      'characters_nonzero_by_valuation': dict(sorted(weighted.items())),
                      'zero_characters': zeros,
                      'v3_mu_linear_coefficient': v3(mu[1])}, ensure_ascii=False))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('usage: python R762EO_VERIFY.py R762EM_Q9_SPECTRAL_EVIDENCE.json')
    main(sys.argv[1])
