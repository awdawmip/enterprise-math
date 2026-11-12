#!/usr/bin/env python3
"""Exact R063 all-pair trace-fiber gluing test for X6, no third-party modules."""
from itertools import combinations, product
from math import comb, factorial, isqrt


def roots(r):
    return [(a, isqrt(r*r-a*a)) for a in range(r+1)
            if isqrt(r*r-a*a)**2 == r*r-a*a]


def labeled_fibers(d, r, signed):
    # A path's identity is its signed labelled primitive-step word. Different
    # charts share exactly the axial words, so count a shared word only once.
    endpoints, chart_roots = {}, {}
    for i, j in combinations(range(d), 2):
        for a, b in roots(r):
            for sx in ((-1, 1) if signed and a else (1,)):
                for sy in ((-1, 1) if signed and b else (1,)):
                    point = [0] * d
                    point[i], point[j] = sx * a, sy * b
                    point = tuple(point)
                    w = comb(a+b, a)
                    assert endpoints.get(point, w) == w
                    endpoints[point] = w
                    chart_roots.setdefault(point, set()).add((i, j, a, b))
    return endpoints, chart_roots


def one_case(d, r):
    plus, charts_plus = labeled_fibers(d, r, signed=False)
    signed, charts = labeled_fibers(d, r, signed=True)
    root_set = roots(r)
    nonax = len(root_set) - 2
    positive_count = d + comb(d, 2) * nonax
    signed_count = 2*d + 4*comb(d, 2)*nonax
    P = sum(comb(a+b, a) for a, b in root_set)
    positive_mass = d + comb(d, 2) * (P-2)
    signed_mass = 2*d + 4*comb(d, 2) * (P-2)
    assert (len(plus), len(signed)) == (positive_count, signed_count)
    assert (sum(plus.values()), sum(signed.values())) == (positive_mass, signed_mass)
    assert len({tuple(abs(v) for v in x) for x in signed}) == len(plus)
    # Per-axis endpoint is incident to d-1 pair charts, yet is one word.
    assert all(len(charts_plus[tuple(r if k == i else 0 for k in range(d))]) == d-1 for i in range(d))
    # No global R_r-root quotient can agree with every pair chart for d>=3.
    conflicting = [(x, data) for x, data in charts_plus.items()
                   if len({(a,b) for _, _, a, b in data}) > 1]
    assert bool(conflicting) == (d >= 3)
    return positive_count, signed_count, positive_mass, signed_mass, len(conflicting)


def main():
    n = 0
    for d in range(2, 7):
        for r in range(1, 129):
            one_case(d, r)
            n += 1
    pos, sig, mp, ms, conflicts = one_case(6, 50)
    assert (pos, sig, mp, ms, conflicts) == (
        66, 252, 1660433074113835713096, 6641732296455342852372, 4)
    # At d=6, the four interior axes (2..5) have incompatible axial root labels.
    assert one_case(3, 5)[-1] == 1
    print('PASS', n, 'dimensions/radii, both sign modes')
    print('d=6, r=50, positive/signed endpoints:', pos, sig)
    print('positive/signed path words:', mp, ms)
    print('exact end-trace collision defect:', ms - sig)
    print('exact absolute-trace collision defect:', ms - pos)
    print('axial label-conflict endpoints:', conflicts)


if __name__ == '__main__':
    main()
